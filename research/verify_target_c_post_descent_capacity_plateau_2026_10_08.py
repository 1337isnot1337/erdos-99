#!/usr/bin/env python3
"""Exact nonglobal near-triangular wall-capacity plateau certificates.

Oler supplies the analytic packet upper bound. Finite samples do not
prove the all-M family, the weak-wall theorem, or global optimality.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g

Q = g.Q


def encode(x):
    x = Q.of(x)
    return {"rational": str(x.a), "sqrt3": str(x.b)}


def census(points):
    contacts = set()
    maximum = Q()
    diameters = set()
    checks = 0
    strict = True
    for i, j in combinations(range(len(points)), 2):
        d = g.distance(points[i], points[j])
        assert (d-1).sign() >= 0, (i, j, encode(d))
        if d == Q(1):
            contacts.add((i, j))
            strict = False
        direction = (d-maximum).sign()
        if direction > 0:
            maximum, diameters = d, {(i, j)}
        elif direction == 0:
            diameters.add((i, j))
        checks += 1
    adjacency = [set() for _ in points]
    for i, j in contacts:
        adjacency[i].add(j)
        adjacency[j].add(i)
    triangles = sum(len(adjacency[i] & adjacency[j]) for i, j in contacts)//3
    return {
        "contacts": contacts, "diameters": diameters,
        "diameter_squared": maximum, "checks": checks,
        "strict_separation": strict, "triangles": triangles,
        "adjacency": adjacency,
    }


def fixture(m):
    tau = F(1, 100*m**3)
    c, s = (1-tau*tau)/(1+tau*tau), 2*tau/(1+tau*tau)
    u = Q(1), Q()
    v = Q(c/2, -s/2), Q(s/2, c/2)
    assert g.norm(v) == Q(1)
    assert (v[0]-F(49, 100)).sign() > 0
    assert (Q(F(1, 2))-v[0]).sign() > 0
    indices = [(i, j) for j in range(m+1) for i in range(m+1)]
    grid = [g.add(g.scale(u, i), g.scale(v, j)) for i, j in indices]
    q, r = (Q(-2), Q(-2)), (Q(10*m), Q())
    points = grid+[q, r]
    old = census(points)
    expected_contacts = {
        (a, b) for a, b in combinations(range(len(grid)), 2)
        if abs(indices[a][0]-indices[b][0])
        + abs(indices[a][1]-indices[b][1]) == 1
    }
    assert old["contacts"] == expected_contacts
    assert len(expected_contacts) == 2*m*(m+1)
    assert old["triangles"] == 0
    assert not old["adjacency"][-1] and not old["adjacency"][-2]
    assert old["diameters"] == {(len(grid), len(grid)+1)}
    expected_diameter = Q((10*m+2)**2+4)
    assert old["diameter_squared"] == expected_diameter

    t = F(1, 10*m*m)
    length = 1+t
    retained = [g.scale(p, length) for p in points[:-1]]
    endpoint = census(retained)
    assert endpoint["strict_separation"]
    assert endpoint["triangles"] == 0
    assert (expected_diameter-endpoint["diameter_squared"]).sign() > 0
    assert not endpoint["adjacency"][-1]  # q remains, strictly isolated.
    coarse_bound = Q(length**2*(3*m*m+10*m+8))
    assert (coarse_bound-endpoint["diameter_squared"]).sign() >= 0
    assert (Q(20*m*m)-coarse_bound).sign() > 0

    label = {ij: a for a, ij in enumerate(indices)}
    boundary = (
        [(i, 0) for i in range(m)]
        + [(m, j) for j in range(m)]
        + [(i, m) for i in range(m, 0, -1)]
        + [(0, j) for j in range(m, 0, -1)]
    )
    boundary = [label[ij] for ij in boundary]
    interior = [label[i, j] for j in range(1, m) for i in range(1, m)]
    assert len(boundary) == len(set(boundary)) == 4*m
    assert len(interior) == (m-1)**2
    wall_checks = 0
    for a, b in zip(boundary, boundary[1:]+boundary[:1]):
        assert g.distance(retained[a], retained[b]) == Q(length**2)
        assert length**2 < 3
        wall_checks += 1
    guards = 0
    for a in interior:
        for b in boundary:
            assert (g.distance(retained[a], retained[b])-1).sign() > 0
            guards += 1

    full_grid_size = (m+1)**2
    oler = Q(length**2*m*m*c+2*length*m+1, length**2*m*m*s/3)
    excess = oler-full_grid_size
    assert excess.sign() > 0
    assert (Q(F(129, 400))-excess).sign() >= 0
    assert (oler-(full_grid_size+1)).sign() < 0
    # Integer upper bound on any weakly guarded packet, using Oler.
    capacity_upper = full_grid_size-len(boundary)
    assert capacity_upper == len(interior)
    assert capacity_upper < len(interior)+1  # Cannot restore deleted r.

    n = len(points)
    width = m+2
    competitor = [(Q(a % width), Q(a // width)) for a in range(n)]
    comparison = census(competitor)
    assert len(competitor) == n
    assert (Q((m+1)**2+m*m)-comparison["diameter_squared"]).sign() >= 0
    assert (expected_diameter-comparison["diameter_squared"]).sign() > 0

    return {
        "M": m, "source_points": n, "retained_points": len(retained),
        "source_pair_checks": old["checks"],
        "endpoint_pair_checks": endpoint["checks"],
        "competitor_pair_checks": comparison["checks"],
        "actual_old_contacts": len(old["contacts"]),
        "actual_old_diameters": len(old["diameters"]),
        "unit_triangles": old["triangles"],
        "retained_contact_isolates": 1,
        "wall_side_checks": wall_checks, "strict_wall_guard_checks": guards,
        "old_diameter_squared": encode(expected_diameter),
        "new_diameter_squared": encode(endpoint["diameter_squared"]),
        "competitor_diameter_squared": encode(comparison["diameter_squared"]),
        "oler_excess_over_full_grid": encode(excess),
        "old_interiors": len(interior),
        "exact_weak_wall_capacity": capacity_upper,
        "refill_capacity_needed": len(interior)+1,
        "scope": "nonglobal; unique old diameter joins two contact isolates; no KKT",
    }


def main():
    cases = [fixture(m) for m in (4, 6, 8, 12)]
    totals = {
        key: sum(case[key] for case in cases)
        for key in (
            "source_pair_checks", "endpoint_pair_checks",
            "competitor_pair_checks", "actual_old_contacts",
            "wall_side_checks", "strict_wall_guard_checks",
        )
    }
    print(json.dumps({
        "status": "PASS", "exact_field": "Q(sqrt(3))",
        "classification": "regression; canonical=false",
        "cases": cases, "totals": totals,
        "not_proved": [
            "canonical C-II source or global optimizer",
            "no possible alternative refill or larger finite motion",
            "all-M theorem from finite samples",
            "post-descent weak shielding from finite samples",
            "Level I or C-II closure",
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
