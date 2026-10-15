#!/usr/bin/env python3
"""Exact paired-cap discovery/regression; no canonical/global-optimality claim.

Coordinates use the triangular basis (1,0),(1/2,sqrt(3)/2). Every source
pair is checked with integer squared norms, independently by the Cartesian
radical formula. The analytic family and its population comparison are in
docs/reports/target_c_paired_cap_spoke_global_comparison_2026-10-06.md.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

RAYS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
NEIGHBORS = ((0, 0),) + RAYS


def norm2(p):
    i, j = p
    return i * i + i * j + j * j


def cartesian_norm2_times4(p):
    i, j = p
    return (2 * i + j) ** 2 + 3 * j * j


def add(p, q):
    return p[0] + q[0], p[1] + q[1]


def sub(p, q):
    return p[0] - q[0], p[1] - q[1]


def mul(k, p):
    return k * p[0], k * p[1]


def dot_times2(p, q):
    i, j = p
    a, b = q
    return (2 * i + j) * a + (i + 2 * j) * b


def cross(o, a, b):
    x, y = sub(a, o), sub(b, o)
    return x[0] * y[1] - x[1] * y[0]


def hull(points):
    pts = sorted(set(points))
    halves = []
    for seq in (pts, list(reversed(pts))):
        half = []
        for p in seq:
            while len(half) >= 2 and cross(half[-2], half[-1], p) <= 0:
                half.pop()
            half.append(p)
        halves.append(half)
    return halves[0][:-1] + halves[1][:-1]


def area_coefficient_numerator(poly):
    """Area is result*sqrt(3)/(4*coordinate_denominator**2)."""
    return sum(a[0] * b[1] - a[1] * b[0]
               for a, b in zip(poly, poly[1:] + poly[:1]))


def instance(m):
    assert m >= 5
    den = 100 * m * m
    snum = den + 1
    core_indices = [mul(k, v) for v in RAYS for k in range(1, m + 1)]
    guards = {add(p, w) for p in core_indices for w in NEIGHBORS}
    lattice = [(i, j) for i in range(-2 * m, 2 * m + 1)
               for j in range(-2 * m, 2 * m + 1)
               if 16 * norm2((i, j)) <= (4 * m - 1) ** 2]
    exterior_indices = [p for p in lattice if p not in guards]
    points = [mul(den, p) for p in core_indices]
    points += [mul(snum, p) for p in exterior_indices]
    n = len(points)
    lost = len(set(lattice) & guards)

    # Analytic injection: two disjoint six-sector guard families.
    explicit_core = {mul(k, v) for v in RAYS for k in range(1, m)}
    explicit_offray = {add(mul(k, RAYS[j]), RAYS[(j + 1) % 6])
                       for j in range(6) for k in range(1, m - 1)}
    assert not explicit_core & explicit_offray
    assert len(explicit_core) == 6 * (m - 1)
    assert len(explicit_offray) == 6 * (m - 2)
    assert explicit_core | explicit_offray <= set(lattice) & guards
    assert lost >= 12 * m - 18 >= 6 * m
    assert n <= len(lattice)

    unit2 = den * den
    diam2 = 4 * m * m * unit2
    contacts, diameters = [], []
    min_isolate_lower = None
    max_isolate_upper = 0
    checked = 0
    for i, p in enumerate(points):
        for j in range(i):
            delta = sub(p, points[j])
            q = norm2(delta)
            assert cartesian_norm2_times4(delta) == 4 * q
            assert unit2 <= q <= diam2, (m, i, j, q)
            if q == unit2:
                contacts.append((j, i))
            if q == diam2:
                diameters.append((j, i))
            if i >= 6 * m:
                min_isolate_lower = q if min_isolate_lower is None else min(min_isolate_lower, q)
                max_isolate_upper = max(max_isolate_upper, q)
                assert unit2 < q < diam2
            checked += 1
    assert len(contacts) == 6 * m
    assert len(diameters) == 3
    adjacency = [set() for _ in points]
    forces = [[0, 0] for _ in points]
    for i, j in contacts:
        adjacency[i].add(j)
        adjacency[j].add(i)
        d = sub(points[i], points[j])
        for axis in range(2):
            forces[i][axis] += 2 * m * d[axis]
            forces[j][axis] -= 2 * m * d[axis]
    for i, j in diameters:
        d = sub(points[i], points[j])
        for axis in range(2):
            forces[i][axis] -= d[axis]
            forces[j][axis] += d[axis]
    assert all(f == [0, 0] for f in forces)
    assert all(not adjacency[i] & adjacency[j] for i, j in contacts)

    loaded = {i for e in diameters for i in e}
    assert len(loaded) == 6
    source_hull = hull(points)
    cap_populations = [0] * 6
    for p in points[6 * m:]:
        caps = [j for j in range(6)
                if dot_times2(p, add(RAYS[j], RAYS[(j + 1) % 6])) > 3 * m * den]
        assert len(caps) <= 1
        for j in caps:
            cap_populations[j] += 1
    cap_areas = []
    for j in range(6):
        a = mul(m * den, RAYS[j])
        b = mul(m * den, RAYS[(j + 1) % 6])
        ia, ib = source_hull.index(a), source_hull.index(b)
        arc = source_hull[ia:ib + 1] if ia <= ib else source_hull[ia:] + source_hull[:ib + 1]
        cap_areas.append(area_coefficient_numerator(arc))
    assert all(cap_populations[j] == cap_populations[j + 3] for j in range(3))
    assert all(cap_areas[j] == cap_areas[j + 3] for j in range(3))
    if m >= 8:
        assert min(cap_populations) > 0
        assert min(cap_areas) > 0

    # Same-cardinality competitor, allowed to contain unit triangles.
    competitor = sorted(lattice, key=lambda p: (norm2(p), p))[:n]
    assert len(competitor) == n == len(set(competitor))
    assert {(0, 0), (1, 0), (0, 1)} <= set(competitor)
    better_pairs = 0
    better_max4 = 0
    for i, p in enumerate(competitor):
        for q in competitor[:i]:
            d = sub(p, q)
            c4 = cartesian_norm2_times4(d)
            assert c4 >= 4
            assert c4 <= (4 * m - 1) ** 2
            better_max4 = max(better_max4, c4)
            better_pairs += 1
    assert better_max4 < 4 * (2 * m) ** 2

    record = {
        "M": m, "D": 2 * m, "source_population": n,
        "core_population": 6 * m, "isolate_population": n - 6 * m,
        "source_pair_checks": checked, "contacts": len(contacts),
        "actual_diameter_pairs": len(diameters), "loaded_vertices": 6,
        "positive_KKT": {"contact_alpha": [2 * m, 3], "diameter_beta": [1, 3]},
        "cap_populations": cap_populations,
        "cap_area_sqrt3_coefficients": [[x, 4 * den * den] for x in cap_areas],
        "lattice_container_population": len(lattice), "deleted_lattice_guards": lost,
        "competitor_population": n, "competitor_pair_checks": better_pairs,
        "competitor_max_squared_distance": [better_max4, 4],
        "guaranteed_competitor_diameter_bound": [4 * m - 1, 2],
        "isolate_min_squared_distance": [min_isolate_lower, unit2],
        "isolate_max_squared_distance": [max_isolate_upper, unit2],
        "canonical_rank_count_failure": {"e_plus_h": 6 * m + 3, "required": 12 * m - 2},
    }
    finite = {
        "basis": ["(1,0)", "(1/2,sqrt(3)/2)"],
        "coordinate_denominator": den,
        "old_basis_coordinate_numerators": points,
        "competitor_integer_basis_coordinates": competitor,
    }
    return record, finite


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-m", type=int, default=32)
    args = parser.parse_args()
    ms = [m for m in (5, 8, 12, 20, 32) if m <= args.max_m]
    records = []
    finite = None
    for m in ms:
        record, inst = instance(m)
        records.append(record)
        if m == 8:
            finite = inst
        print(f"M={m}: n={record['source_population']}, "
              f"pairs={record['source_pair_checks']}, "
              f"caps={record['cap_populations']}, "
              f"competitor <= D-1/2; PASS", flush=True)
    result = {
        "status": "exact feasible-source regression and restricted global comparison",
        "canonical_source": False, "global_minimizer": False,
        "instances": records, "explicit_M8_instance": finite,
        "scope": "The parametric proof is analytic. Samples do not certify the canonical cap branch.",
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: exact paired-cap populations, all pair distances, positive KKT, and same-cardinality strict competitor")


if __name__ == "__main__":
    main()
