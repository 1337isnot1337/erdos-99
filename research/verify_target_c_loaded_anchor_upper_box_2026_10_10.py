#!/usr/bin/env python3
"""Full-pair loaded-anchor upper-box examples and far-owner regression.

Exact rational / quadratic-field arithmetic. The sources are nonglobal and
do not satisfy canonical stress hypotheses. Phase and owner-count proofs
are analytic; this verifies the explicitly stated finite fixtures only.
"""

import argparse
import json
from itertools import combinations

import sympy as S
from verify_target_c_source_realized_owner_sink_2026_10_10 import enclosure


def fixture(D, localized):
    delta = S.Rational(2, D)
    rho = S.Rational(3, D)
    a = S.sqrt(1 - S.Rational(1, D * D))
    points = [(0, 0), (0, D), (-a, S.Rational(1, D)), (a, S.Rational(1, D))]
    moving = {0}
    contacts = {(0, 2), (0, 3)}
    old_H = {(0, 1)}
    if localized:
        points.extend(
            [
                (-S.Rational(D, 2), S.Rational(D, 2)),
                (S.Rational(D, 2), S.Rational(D, 2)),
                (0, 2),
            ]
        )
        moving.add(6)
        old_H.add((4, 5))
        R = S.Integer(2)
        # A rational bound on the actual phase and angle parameters, using
        # asin(x)<=2x for x<=1/2; the given completion is exactly a disk.
        assert 96 * (R + rho) / D < S.Rational(17, 20) ** 2
        assert S.Rational(17, 20) + 2 * R / (D - rho) + rho / (D - rho) < S.Rational(
            9, 10
        )
        assert R + rho <= S.Rational(D, 10)
        assert all(
            S.simplify(sum(S.sympify(x) ** 2 for x in points[i])) <= R * R
            for i in moving
        )
    else:
        L = S.sqrt(D * D - delta * delta / 2)
        points.extend(
            [
                (-L / 2, S.Rational(D, 2) - delta / 4),
                (L / 2, S.Rational(D, 2) + delta / 4),
            ]
        )
        moving.add(4)
        # The far label is not within a subdiameter anchor radius. Its
        # actual norm is rigorously at least D/2, rather than asserted small.
        far_distance = S.simplify(sum(S.sympify(x) ** 2 for x in points[4]))
        assert enclosure(far_distance)[0] > S.Rational(D * D, 4)

    # Every original point lies in the stated diameter-D disk.
    for x, y in points:
        radius2 = S.simplify(S.sympify(x) ** 2 + (S.sympify(y) - S.Rational(D, 2)) ** 2)
        assert radius2 <= S.Rational(D * D, 4)
    states, pair_checks = [], 0
    for shift in (S.Integer(0), delta, rho):
        endpoint = [
            (S.sympify(x), S.sympify(y) + (shift if i in moving else 0))
            for i, (x, y) in enumerate(points)
        ]
        found_contacts, found_H, upper_bad = set(), set(), []
        maximum = (
            S.Integer(D * D)
            if localized or shift == 0
            else D * D - delta * delta / 4
            if shift == delta
            else D * D + delta * delta / 2
        )
        maximum_pair = (4, 5) if localized or shift else (0, 1)
        for i, j in combinations(range(len(points)), 2):
            pair_checks += 1
            pair = (i, j)
            distance = S.simplify(
                sum((x - y) ** 2 for x, y in zip(endpoint[i], endpoint[j]))
            )
            if pair in contacts:
                target = 1 + shift * (shift - delta)
                assert S.simplify(distance - target) == 0 and target >= 1
                if target == 1:
                    found_contacts.add(pair)
            else:
                assert enclosure(distance)[0] > 1
            if S.simplify(distance - D * D) == 0:
                found_H.add(pair)
            elif enclosure(distance)[0] > D * D:
                upper_bad.append(pair)
            else:
                assert enclosure(distance)[1] < D * D
            if pair == maximum_pair:
                assert S.simplify(distance - maximum) == 0
            elif S.simplify(distance - maximum) == 0:
                assert localized and pair in old_H
            else:
                assert enclosure(distance - maximum)[1] < 0
        expected_c = contacts if shift in (0, delta) else set()
        assert found_contacts == expected_c
        assert upper_bad == ([] if localized or shift != rho else [(4, 5)])
        assert found_H == (old_H if shift == 0 else {(4, 5)} if localized else set())
        states.append(
            {
                "shift": str(shift),
                "contacts": sorted(found_contacts),
                "old_D_equalities": sorted(found_H),
                "upper_failures": upper_bad,
                "diameter_squared": str(maximum),
            }
        )
    return {
        "kind": "loaded_anchor_upper_box",
        "D": D,
        "localized": localized,
        "moving_labels": sorted(moving),
        "source_labels": len(points),
        "pair_checks": pair_checks,
        "states": states,
        "scope": "nonglobal fixtures; no canonical owner extraction or lower-system theorem",
    }


def native_direction_fixture(D):
    parameter = S.Rational(1, 80)
    cosine = (1 - parameter * parameter) / (1 + parameter * parameter)
    sine = 2 * parameter / (1 + parameter * parameter)
    delta, rho = S.Rational(2, D), S.Rational(3, D)
    a = S.sqrt(1 - S.Rational(1, D * D))
    z = (D * sine / 2, D * (1 - cosine) / 2)
    h = (-D * sine / 2, D * (1 + cosine) / 2)
    direction = (-sine, cosine)
    tangent = (cosine, sine)
    points = [(0, 0), (0, D), (-a, S.Rational(1, D)), (a, S.Rational(1, D)), z, h]
    points.extend(
        tuple(z[k] + sign * a * tangent[k] + direction[k] / D for k in range(2))
        for sign in (-1, 1)
    )
    directions = {0: (0, 0), 1: (0, 1), 2: direction}
    owners = [1, 0, 0, 0, 2, 0, 0, 0]
    contacts = {(0, 2), (0, 3), (4, 6), (4, 7)}
    old_H = {(0, 1), (4, 5)}
    assert cosine >= S.Rational(1, 2)
    assert cosine * cosine + sine * sine == 1
    assert 96 * rho / D < S.Rational(17, D) ** 2
    assert parameter + S.Rational(17, D) + rho / (D - rho) < S.Rational(1, 10)
    for x, y in points:
        assert (
            S.simplify(
                S.sympify(x) ** 2
                + (S.sympify(y) - S.Rational(D, 2)) ** 2
                - S.Rational(D * D, 4)
            )
            == 0
        )
    states, pair_checks = [], 0
    for heights in ({}, {1: rho}, {2: rho}, {1: rho, 2: rho}, {1: delta, 2: delta}):
        endpoint = [
            tuple(
                S.sympify(p[k]) + heights.get(owner, 0) * directions[owner][k]
                for k in range(2)
            )
            for p, owner in zip(points, owners)
        ]
        expected_H = {pair for pair in old_H if owners[pair[0]] not in heights}
        maximum = S.Integer(D * D) if expected_H else S.Integer(D * D - 1)
        found_c, found_h = set(), set()
        for i, j in combinations(range(8), 2):
            pair_checks += 1
            pair = (i, j)
            distance = S.simplify(
                sum((x - y) ** 2 for x, y in zip(endpoint[i], endpoint[j]))
            )
            if pair in contacts:
                height = heights.get(owners[i], 0)
                target = 1 + height * (height - delta)
                assert S.simplify(distance - target) == 0 and target >= 1
                if target == 1:
                    found_c.add(pair)
            else:
                assert enclosure(distance)[0] > 1, (
                    D,
                    heights,
                    pair,
                    distance,
                    enclosure(distance),
                )
            if S.simplify(distance - D * D) == 0:
                found_h.add(pair)
            else:
                assert enclosure(distance)[1] < D * D
            if S.simplify(distance - maximum) != 0:
                assert enclosure(distance - maximum)[1] < 0
        assert found_h == expected_H
        expected_C = {
            pair for pair in contacts if heights.get(owners[pair[0]], 0) in (0, delta)
        }
        assert found_c == expected_C
        maximizing_pair = next(iter(expected_H)) if expected_H else (1, 2)
        assert (
            S.simplify(
                sum(
                    (x - y) ** 2
                    for x, y in zip(
                        endpoint[maximizing_pair[0]], endpoint[maximizing_pair[1]]
                    )
                )
                - maximum
            )
            == 0
        )
        states.append(
            {
                "heights": {str(i): str(s) for i, s in heights.items()},
                "contacts": sorted(found_c),
                "diameters_at_original_D": sorted(found_h),
                "diameter_squared": str(maximum),
            }
        )
    return {
        "kind": "native_direction_box",
        "D": D,
        "pair_checks": pair_checks,
        "second_direction": [str(x) for x in direction],
        "states": states,
        "scope": "eight-point nonglobal circle fixture; no canonical KKT or capacity hypotheses",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diameters", type=int, nargs="+", default=[300, 500, 1000])
    args = parser.parse_args()
    for D in args.diameters:
        assert D >= 300
        for localized in (True, False):
            print(json.dumps(fixture(D, localized), sort_keys=True))
        print(json.dumps(native_direction_fixture(D), sort_keys=True))


if __name__ == "__main__":
    main()
