#!/usr/bin/env python3
"""Exact finite checks for the nested-hexagon selected stresses.

The all-M stress identities are proved algebraically in the independent audit.
This script checks the lattice supports, forces, guard reactions, and support
counts for M=3,...,12. It does not check a full feasible motion or a global
packing claim.
"""

from fractions import Fraction as F
from itertools import combinations
import json


RAYS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def scale(a, n):
    return n * a[0], n * a[1]


def norm2(a):
    return a[0] * a[0] + a[0] * a[1] + a[1] * a[1]


def ring(m, radius):
    points = {(i, j)
              for i in range(-(m - 1), m)
              for j in range(-(m - 1), m)
              if max(abs(i), abs(j), abs(i + j)) == radius}
    return points


def packet(m):
    radius = m - 1
    points = {(i, j)
              for i in range(-radius, radius + 1)
              for j in range(-radius, radius + 1)
              if abs(i + j) <= radius}
    assert len(points) == 3 * radius * radius + 3 * radius + 1
    guards = {scale(e, m) for e in RAYS}
    coordinates = points | guards
    all_unit_edges = {
        tuple(sorted(pair))
        for pair in combinations(points, 2)
        if norm2(sub(pair[0], pair[1])) == 1
    }

    support_union = set()
    equilibrium_checks = 0
    ring_checks = 0
    for r in range(radius + 1):
        boundary = ring(m, r)
        cycle_edges = {
            edge for edge in all_unit_edges
            if edge[0] in boundary and edge[1] in boundary
        }
        assert len(cycle_edges) == 6 * r
        selected = set(cycle_edges)
        for e in RAYS:
            for s in range(r, m):
                selected.add(tuple(sorted((scale(e, s), scale(e, s + 1)))))
        assert len(selected) == 6 * m
        for a, b in selected:
            assert norm2(sub(a, b)) == 1

        force = {p: (0, 0) for p in coordinates}
        for a, b in selected:
            edge = sub(a, b)
            force[a] = add(force[a], edge)
            force[b] = sub(force[b], edge)
        assert all(force[p] == (0, 0) for p in points)
        for e in RAYS:
            assert force[scale(e, m)] == e
        equilibrium_checks += len(points)
        ring_checks += 1
        support_union |= selected

    expected_union = 3 * m * (m + 1)
    assert len(support_union) == expected_union
    # Each of the six fixed guards has reaction e_k and second coefficient
    # -C e_k, so the summed acceleration contribution is -12 C.
    c = F(m * (m * m - 1), 6)
    guard_load = -sum(2 * c * norm2(e) for e in RAYS)
    assert guard_load == -12 * c
    return {
        "M": m,
        "packet_sites": len(points),
        "stress_rings_including_center": ring_checks,
        "selected_edges_per_stress": 6 * m,
        "selected_support_union": len(support_union),
        "expected_support_union": expected_union,
        "interior_equilibrium_checks": equilibrium_checks,
        "guard_load": str(12 * c),
        "ring_energy_lower_bound": str(12 * c),
    }


def main():
    cases = [packet(m) for m in range(3, 13)]
    print(json.dumps({
        "classification": "exact finite checks of selected stress identities",
        "cases": cases,
        "interior_equilibrium_checks": sum(c["interior_equilibrium_checks"] for c in cases),
        "not_checked": [
            "unselected-pair first variations",
            "existence of a feasible motion",
            "strict finite packet or energy upper bound",
            "canonical-source extraction or global optimality",
        ],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
