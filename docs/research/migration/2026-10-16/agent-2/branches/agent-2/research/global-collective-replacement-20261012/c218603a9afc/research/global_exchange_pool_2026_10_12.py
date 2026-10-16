#!/usr/bin/env python3
"""Whole-source finite replacement discovery; every certificate uses rational pairs.

The optional MILP only discovers selections. verify_selection is the certificate.
No finite result from this module establishes global optimality or Level I.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

Point = tuple[F, F]


def point(values) -> Point:
    if len(values) != 2 or any(isinstance(value, float) for value in values):
        raise ValueError("coordinates must be integer or rational strings")
    return tuple(F(value) for value in values)


def dist2(a: Point, b: Point) -> F:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def diameter2(points: list[Point]) -> F:
    return max((dist2(a, b) for a, b in combinations(points, 2)), default=F(0))


def conflicts(points: list[Point], target2: F) -> list[tuple[int, int]]:
    return [(i, j) for i, j in combinations(range(len(points)), 2)
            if not F(1) <= dist2(points[i], points[j]) <= target2]


def verify_selection(source: list[Point], proposals: list[Point], target2: F,
                     selected: list[int]) -> dict:
    if len(source) < 2 or any(dist2(a, b) < 1 for a, b in combinations(source, 2)):
        raise ValueError("source must be unit separated and have at least two labels")
    source2 = diameter2(source)
    if not 1 <= target2 < source2:
        raise ValueError("target squared diameter must be strictly below source")
    pool = source + proposals
    if len(set(selected)) != len(selected) or any(not 0 <= i < len(pool) for i in selected):
        raise ValueError("selection labels must be distinct valid pool indices")
    if len(selected) < len(source):
        raise ValueError("selection does not pay the full source cardinality")
    chosen = [pool[i] for i in selected]
    if conflicts(chosen, target2):
        raise ValueError("selected points fail a lower or upper pair constraint")
    retained = sum(i < len(source) for i in selected)
    return {"source_count": len(source), "proposal_count": len(proposals),
            "selected_count": len(selected), "retained_source_labels": retained,
            "deleted_source_labels": len(source) - retained,
            "inserted_points": len(selected) - retained,
            "source_diameter_squared": str(source2),
            "target_diameter_squared": str(target2),
            "selected_diameter_squared": str(diameter2(chosen)),
            "strict_squared_diameter_margin": str(source2 - diameter2(chosen)),
            "classification": "regression: source is not a global minimizer"}


def discover(source: list[Point], proposals: list[Point], target2: F,
             seconds: float) -> list[int]:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import coo_matrix

    pool = source + proposals
    edges = conflicts(pool, target2)
    rows, columns = [], []
    for row, (i, j) in enumerate(edges):
        rows.extend((row, row))
        columns.extend((i, j))
    matrix = coo_matrix((np.ones(len(columns)), (rows, columns)),
                        shape=(len(edges), len(pool))).tocsc()
    result = milp(-np.ones(len(pool)), integrality=np.ones(len(pool)),
                  bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix, -np.inf, 1),
                  options={"time_limit": seconds})
    if result.x is None:
        raise ValueError("discovery found no selection; this is not a proof of exclusion")
    return [i for i, value in enumerate(result.x) if value > 0.5]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    source = [point(p) for p in data["source"]]
    proposals = [point(p) for p in data["proposals"]]
    if isinstance(data["target_diameter_squared"], float):
        raise ValueError("target must be an integer or rational string")
    target2 = F(data["target_diameter_squared"])
    selected = discover(source, proposals, target2, args.seconds) if args.discover else data["selected"]
    result = verify_selection(source, proposals, target2, selected)
    if args.output:
        data["selected"] = selected
        data["verification"] = result
        args.output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
