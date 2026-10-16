#!/usr/bin/env python3
"""Search a whole source plus arbitrary cloud; certify only positive outputs.

Every lower and upper forbidden pair is computed exactly. The floating MILP
search is only a candidate selector. The separate certificate checker knows
neither the MILP formulation nor the search bank.
"""

import argparse
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path


def parse_points(rows):
    return [(Q(x), Q(y)) for x, y in rows]


def distance2(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def diameter2(points):
    return max((distance2(p, q) for p, q in combinations(points, 2)), default=Q(0))


def point_rows(points):
    return [[str(x), str(y)] for x, y in points]


def check_certificate(data):
    source = parse_points(data["source"])
    output = parse_points(data["competitor"])
    assert len(source) >= 2
    assert len(output) == len(source), "Source cardinality was not preserved."
    assert all(distance2(p, q) >= 1 for p, q in combinations(source, 2))
    source_d2 = diameter2(source)
    assert Q(data["source_diameter_squared"]) == source_d2
    minimum2 = min(distance2(p, q) for p, q in combinations(output, 2))
    maximum2 = diameter2(output)
    assert minimum2 >= 1, "Lower pair constraint failed."
    assert maximum2 < source_d2, "Strict diameter improvement failed."
    assert Q(data["competitor_diameter_squared"]) == maximum2
    return {
        "labels": len(source),
        "source_diameter_squared": str(source_d2),
        "competitor_diameter_squared": str(maximum2),
        "minimum_squared_distance": str(minimum2),
        "strict_squared_margin": str(source_d2 - maximum2),
        "independent_full_pair_verification": "PASS",
        "level_i_resolved": False,
    }


def search(source, cloud, time_limit=30, label="supplied source"):
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import coo_matrix

    assert len(source) >= 2
    assert all(distance2(p, q) >= 1 for p, q in combinations(source, 2))
    source_d2 = diameter2(source)
    points = source + cloud
    n, total = len(source), len(points)
    forbidden = [(i, j) for i, j in combinations(range(total), 2)
                 if distance2(points[i], points[j]) < 1
                 or distance2(points[i], points[j]) >= source_d2]
    # Every original source label is a variable. Comparison-cloud points may
    # conflict with one another at either threshold; none are pre-deleted.
    row_ids = []
    column_ids = []
    for row, (i, j) in enumerate(forbidden):
        row_ids.extend((row, row))
        column_ids.extend((i, j))
    quota_row = len(forbidden)
    row_ids.extend([quota_row] * total)
    column_ids.extend(range(total))
    matrix = coo_matrix((np.ones(len(row_ids)), (row_ids, column_ids)),
                        shape=(quota_row + 1, total)).tocsc()
    lower = np.full(quota_row + 1, -np.inf)
    upper = np.ones(quota_row + 1)
    lower[-1], upper[-1] = n, np.inf
    # Seek an n-label witness while favoring retained source labels. Solver
    # optimality, bounds and infeasibility are never used as proof conclusions.
    cost = np.r_[np.zeros(n), np.ones(len(cloud))]
    result = milp(cost, integrality=np.ones(total), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix, lower, upper),
                  options={"time_limit": time_limit, "mip_rel_gap": 0})
    summary = {
        "label": label,
        "source_labels": n,
        "cloud_labels": len(cloud),
        "forbidden_pairs": len(forbidden),
        "solver_status": int(result.status),
        "solver_message": result.message,
        "negative_result_is_not_an_optimality_certificate": True,
    }
    if result.x is None:
        summary["strict_competitor_certified"] = False
        return summary, None
    selected = [i for i, x in enumerate(result.x) if x > 0.5]
    if len(selected) < n:
        summary["strict_competitor_certified"] = False
        return summary, None
    # Round only to suggest labels, then audit every geometric pair. No solver
    # tolerance is accepted at either distance threshold.
    chosen = [points[i] for i in selected]
    if not all(1 <= distance2(p, q) < source_d2 for p, q in combinations(chosen, 2)):
        summary["strict_competitor_certified"] = False
        summary["candidate_rejected_by_exact_geometry"] = True
        return summary, None
    selected = sorted(selected, key=lambda i: i >= n)[:n]
    chosen = [points[i] for i in selected]
    certificate = {
        "classification": "exact finite nonglobality certificate",
        "label": label,
        "source": point_rows(source),
        "competitor": point_rows(chosen),
        "source_diameter_squared": str(source_d2),
        "competitor_diameter_squared": str(diameter2(chosen)),
        "retained_source_labels": [i for i in selected if i < n],
        "inserted_cloud_labels": [i - n for i in selected if i >= n],
        "level_i_resolved": False,
    }
    checked = check_certificate(certificate)
    summary.update(checked)
    summary["retained_source_count"] = len(certificate["retained_source_labels"])
    summary["inserted_count"] = len(certificate["inserted_cloud_labels"])
    summary["strict_competitor_certified"] = True
    return summary, certificate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--seconds", type=float, default=30)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    if args.verify_only:
        print(json.dumps(check_certificate(data), sort_keys=True))
        return
    summary, certificate = search(parse_points(data["source"]),
                                  parse_points(data["cloud"]), args.seconds,
                                  data.get("label", "supplied source"))
    if certificate is not None and args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(certificate, sort_keys=True, indent=2) + "\n")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
