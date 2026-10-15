#!/usr/bin/env python3
"""Audit actual contact coverage for the finite radial-lifting certificates.

The companion audit replay checks exact lifting jumps and equilibrium. This
checker independently enumerates every actual unit pair at the sampled
curvature and verifies that each moving-involving contact is in the
triangulation support covered by that stress calculation.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import json

import verify_target_c_sorting_radial_lifting_stress_2026_10_07 as radial
import verify_target_c_three_direction_corner_barrier_2026_10_06 as geom


def listed_cases():
    cases = [(4, order) for order in permutations((3, 1, -1, -3))]
    for m in (6, 8, 10):
        descending = tuple(range(m - 1, -m, -2))
        cases.extend(
            (
                (m, descending),
                (m, tuple(reversed(descending))),
                (m, tuple(descending[::2] + descending[1::2])),
            )
        )
    return cases


def case(m, order):
    source = radial.case(order)
    assert source["M"] == m
    actual, _ = radial.geometry(m, list(order), F(1, 200 * m * m))

    triangles = set()
    for p in actual:
        neighbours = [
            (p[0] + d[0], p[1] + d[1]) for d in radial.DIRECTIONS
        ]
        neighbours = [q for q in neighbours if q in actual]
        for q, r in combinations(neighbours, 2):
            if radial.flatnorm((q[0] - r[0], q[1] - r[1])) == 1:
                triangles.add(frozenset((p, q, r)))
    assert len(triangles) == 6 * m * m

    face_count = {}
    for triangle in triangles:
        for p, q in combinations(triangle, 2):
            edge = frozenset((p, q))
            face_count[edge] = face_count.get(edge, 0) + 1

    all_unit_pairs = set()
    pair_checks = 0
    for p, q in combinations(actual, 2):
        distance2 = geom.distance(actual[p], actual[q])
        assert (distance2 - geom.Q(1)).sign() >= 0
        pair_checks += 1
        if distance2 == geom.Q(1):
            all_unit_pairs.add(frozenset((p, q)))

    moving = {p for p in actual if radial.rad(p) < m}
    active_pairs = {edge for edge in all_unit_pairs if edge & moving}
    covered_pairs = set(face_count)
    omitted_pairs = active_pairs - covered_pairs
    assert not omitted_pairs
    assert all(face_count[edge] == 2 for edge in active_pairs)
    assert len(active_pairs) == 6 * m * m
    assert source["positive_unit_rows"] == len(active_pairs)
    assert source["exact_moving_vertex_equilibria"] == len(moving)
    assert len(all_unit_pairs) == 6 * m * (m + 1)
    return {
        "M": m,
        "order": list(order),
        "stress_replay_pair_checks": source["all_pair_checks"],
        "contact_census_pair_checks": pair_checks,
        "total_pair_checks": source["all_pair_checks"] + pair_checks,
        "actual_unit_contacts": len(all_unit_pairs),
        "moving_involving_unit_contacts": len(active_pairs),
        "omitted_moving_contacts": len(omitted_pairs),
        "positive_stress_rows": source["positive_unit_rows"],
        "exact_moving_equilibria": source["exact_moving_vertex_equilibria"],
    }


def main():
    rows = [case(m, order) for m, order in listed_cases()]
    assert len(rows) == 33
    out = {
        "classification": "exact finite radial-lifting support audit",
        "scope": "33 listed packets at tan(theta/2)=1/(200 M^2)",
        "cases": rows,
        "totals": {
            key: sum(row[key] for row in rows)
            for key in (
                "stress_replay_pair_checks",
                "contact_census_pair_checks",
                "total_pair_checks",
                "actual_unit_contacts",
                "moving_involving_unit_contacts",
                "omitted_moving_contacts",
                "positive_stress_rows",
                "exact_moving_equilibria",
            )
        },
        "not_proved": [
            "all-M or all-permutation positivity",
            "arbitrary-cloud classification",
            "triangle-free source existence",
            "global optimality",
            "C-II or Level I closure",
        ],
    }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
