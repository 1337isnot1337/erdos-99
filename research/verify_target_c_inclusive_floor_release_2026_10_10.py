#!/usr/bin/env python3
"""Exact inclusive-floor closure and full-pair locked-reflection regressions.

Uses rational lexicographic shortest paths, independent linear elimination,
and symbolic identities / directed rational enclosures for six-point fixtures.
Neither the random graphs nor the geometric fixtures are canonical minimizers.
"""

import argparse
import heapq
import json
import random
from fractions import Fraction
from itertools import combinations

import sympy as S
from verify_target_c_source_realized_owner_sink_2026_10_10 import enclosure


def inclusive_floor_closure(edges, floors, bounds):
    """Return the maximal support and a rational endpoint for the stated class.

    An edge (i,j,c,k) means x_i-x_j<=c, strictly when k=1. Strict
    edges must have c>0. Every active x_i is positive and at least F_i.
    """
    nodes = {0, *floors}
    r = len(floors)
    reverse = {i: [] for i in nodes}
    all_edges = list(edges)
    all_edges.extend((i, 0, bounds[i], 0) for i in floors)
    for i, j, cost, strict in all_edges:
        assert i in nodes and j in nodes and cost >= 0
        assert strict in (0, 1) and (not strict or cost > 0)
        reverse[j].append((i, Fraction(cost), -strict))
    zero = {0}
    rounds = []
    while True:
        caps = {i: (Fraction(0), 0) for i in zero}
        heap = [(Fraction(0), 0, i) for i in zero]
        heapq.heapify(heap)
        while heap:
            real, negative_count, node = heapq.heappop(heap)
            if caps[node] != (real, negative_count):
                continue
            for source, cost, mark in reverse[node]:
                trial = (real + cost, negative_count + mark)
                if source not in caps or trial < caps[source]:
                    caps[source] = trial
                    heapq.heappush(heap, (*trial, source))
        assert nodes <= caps.keys()
        removed = set()
        for i in nodes - zero:
            real, negative_count = caps[i]
            floor = floors[i]
            if real < floor or real == floor and (floor == 0 or negative_count < 0):
                removed.add(i)
        rounds.append(
            {
                "zero": sorted(zero),
                "new_zero": sorted(removed),
                "caps": {str(i): [str(a), -m] for i, (a, m) in caps.items()},
            }
        )
        if not removed:
            break
        zero |= removed
    active = nodes - zero
    real_caps = {i: caps[i][0] for i in nodes}
    counts = {i: -caps[i][1] for i in nodes}
    assert all(0 <= m <= r for m in counts.values())
    margins = [Fraction(1)]
    for i in active:
        margin = real_caps[i] - floors[i]
        if margin > 0:
            margins.append(margin)
    for i, j, cost, strict in all_edges:
        slack = Fraction(cost) - real_caps[i] + real_caps[j]
        assert slack >= 0
        if slack:
            margins.append(slack)
        else:
            assert counts[i] >= counts[j] + strict
        if strict:
            margins.append(Fraction(cost))
    epsilon = min(margins) / (2 * (r + 1))
    heights = {i: real_caps[i] - counts[i] * epsilon for i in nodes}
    for i in floors:
        assert 0 <= heights[i] <= bounds[i]
        assert (heights[i] > 0 and heights[i] >= floors[i]) == (i in active)
    for i, j, cost, strict in all_edges:
        difference = heights[i] - heights[j]
        assert difference < cost if strict else difference <= cost
    return active, heights, epsilon, rounds


def linear_feasible(inequalities, dimension):
    """General exact Fourier--Motzkin elimination, including strict rows."""
    for remaining in range(dimension, -1, -1):
        tightest = {}
        for row, rhs, strict in inequalities:
            if not any(row):
                if rhs < 0 or strict and rhs == 0:
                    return False
                continue
            scale = abs(next(c for c in row if c))
            row = tuple(c / scale for c in row)
            rhs /= scale
            if row not in tightest or rhs < tightest[row][0]:
                tightest[row] = (rhs, strict)
            elif rhs == tightest[row][0]:
                tightest[row] = (rhs, strict or tightest[row][1])
        inequalities = [(row, rhs, strict) for row, (rhs, strict) in tightest.items()]
        if remaining == 0:
            assert not inequalities
            return True
        positive = [item for item in inequalities if item[0][0] > 0]
        negative = [item for item in inequalities if item[0][0] < 0]
        eliminated = [
            (row[1:], rhs, strict) for row, rhs, strict in inequalities if not row[0]
        ]
        for prow, prhs, pstrict in positive:
            for nrow, nrhs, nstrict in negative:
                pscale, nscale = -nrow[0], prow[0]
                eliminated.append(
                    (
                        tuple(
                            pscale * p + nscale * n for p, n in zip(prow[1:], nrow[1:])
                        ),
                        pscale * prhs + nscale * nrhs,
                        pstrict or nstrict,
                    )
                )
        inequalities = eliminated
    raise AssertionError("unreachable")


def enumerated_supports(edges, floors, bounds):
    """Enumerate every support using independent rational linear elimination."""
    r = len(floors)
    feasible = set()
    for bits in range(1 << r):
        support = {i for i in floors if bits & (1 << (i - 1))}
        inequalities = []
        for i, j, cost, strict in edges:
            row = [Fraction(0)] * r
            if i:
                row[i - 1] += 1
            if j:
                row[j - 1] -= 1
            inequalities.append((tuple(row), cost, strict))
        for i in floors:
            row = [Fraction(0)] * r
            row[i - 1] = 1
            inequalities.append(
                (tuple(row), bounds[i] if i in support else Fraction(0), False)
            )
            row[i - 1] = -1
            inequalities.append(
                (
                    tuple(row),
                    -floors[i] if i in support else Fraction(0),
                    i in support and floors[i] == 0,
                )
            )
        if linear_feasible(inequalities, r):
            feasible.add(frozenset(support))
    return feasible


def graph_checks(count, seed):
    rng = random.Random(seed)
    support_checks = 0
    for trial in range(count):
        r = 1 + trial % 4
        floors = {i: Fraction(rng.randrange(0, 7), 4) for i in range(1, r + 1)}
        bounds = {i: Fraction(rng.randrange(0, 9), 4) for i in floors}
        edges = []
        for i in range(r + 1):
            for j in range(r + 1):
                if i != j and rng.randrange(3):
                    cost = Fraction(rng.randrange(0, 9), 4)
                    strict = int(cost > 0 and rng.randrange(2))
                    edges.append((i, j, cost, strict))
        active, _, _, _ = inclusive_floor_closure(edges, floors, bounds)
        feasible = enumerated_supports(edges, floors, bounds)
        support_checks += 1 << r
        assert feasible
        union = set().union(*feasible)
        assert active == union and frozenset(active) in feasible
    return {
        "kind": "independent_exact_linear_elimination",
        "graphs": count,
        "enumerated_supports": support_checks,
        "seed": seed,
        "scope": "finite rational difference graphs, not source extraction",
    }


def critical_graph_checks():
    half = Fraction(1, 2)
    floors = {1: 3 * half, 2: Fraction(0), 3: Fraction(0)}
    bounds = {i: Fraction(3) for i in floors}
    checked = []
    for strict in (0, 1):
        edges = [(1, 2, half, 0), (2, 3, half, strict), (3, 0, half, 0)]
        active, heights, _, rounds = inclusive_floor_closure(edges, floors, bounds)
        assert active == ({2, 3} if strict else {1, 2, 3})
        feasible = enumerated_supports(edges, floors, bounds)
        assert active == set().union(*feasible) and frozenset(active) in feasible
        checked.append(
            {
                "strict_path": strict,
                "active": sorted(active),
                "heights": {str(i): str(x) for i, x in heights.items()},
                "rounds": rounds,
            }
        )
    cascade_floors = {1: Fraction(1), 2: Fraction(2)}
    cascade_bounds = {1: Fraction(3), 2: Fraction(1)}
    cascade_edges = [(1, 2, Fraction(0), 0)]
    active, _, _, rounds = inclusive_floor_closure(
        cascade_edges, cascade_floors, cascade_bounds
    )
    assert not active and rounds[0]["new_zero"] == [2] and rounds[1]["new_zero"] == [1]
    assert enumerated_supports(cascade_edges, cascade_floors, cascade_bounds) == {
        frozenset()
    }
    return {
        "kind": "critical_graphs",
        "cases": checked,
        "cascade_rounds": rounds,
        "enumerated_supports": 20,
    }


def geometric_fixture(D, strict_lock):
    t = S.Rational(1, 100)
    delta = 4 * t / (1 + t * t)
    a = (1 - t * t) / (1 + t * t)
    w = (-S.Rational(5, 13), S.Rational(12, 13))
    f = (-a, delta / 2)
    p = (
        -S.sqrt(
            D * D - (25 * delta * delta / 16 if strict_lock else delta * delta / 4)
        ),
        -delta / 4 if strict_lock else delta / 2,
    )
    q = (-S.sqrt(3) * D / 2, S.Integer(D) / 2)
    points = [(S.Integer(0), S.Integer(0)), w, f, (w[0] + f[0], w[1] + f[1]), p, q]
    owners = [1, 1, 0, 0, 0, 0]
    contacts = {(0, 1), (0, 2), (1, 3), (2, 3)}
    diameters = {(0, 5)} if strict_lock else {(0, 4), (0, 5)}
    states = []
    full_pair_checks = 0
    for shift in (S.Integer(0), delta):
        endpoint = [(x, y + shift * owner) for (x, y), owner in zip(points, owners)]
        found_c, found_h = set(), set()
        for i, j in combinations(range(6), 2):
            full_pair_checks += 1
            distance = S.simplify(
                sum((x - y) ** 2 for x, y in zip(endpoint[i], endpoint[j]))
            )
            if distance == 1:
                found_c.add((i, j))
            else:
                assert enclosure(distance)[0] > 1
            if S.simplify(distance - D * D) == 0:
                found_h.add((i, j))
            else:
                assert enclosure(distance)[1] < D * D
        assert found_c == contacts
        assert found_h == (diameters if shift == 0 else {(0, 4)})
        states.append(
            {
                "shift": str(shift),
                "contacts": sorted(found_c),
                "diameters": sorted(found_h),
            }
        )

    # Compile every intergroup pair. The locking cost is exactly delta;
    # other algebraic costs are rounded down, which can only restrict motions.
    # Both weak and strict locking cases therefore retain an exact bottleneck.
    edges = []
    witnesses = []
    for i, j in combinations(range(6), 2):
        oi, oj = owners[i], owners[j]
        if oi == oj:
            continue
        transverse = S.simplify(points[i][0] - points[j][0])
        projection = S.simplify(points[i][1] - points[j][1])
        radius = S.sqrt(S.simplify(D * D - transverse * transverse))
        upper_strict = int((i, j) not in diameters)
        for source, target, cost in (
            (oi, oj, radius - projection),
            (oj, oi, radius + projection),
        ):
            cost = S.simplify(cost)
            rational = (
                Fraction(int(cost.p), int(cost.q))
                if cost.is_Rational
                else enclosure(cost)[0]
            )
            assert rational >= 0 and (not upper_strict or rational > 0)
            edges.append((source, target, rational, upper_strict))
            witnesses.append(
                (source, target, str(rational), upper_strict, [i, j], "upper")
            )
        if (i, j) not in contacts and enclosure(transverse * transverse)[1] <= 1:
            lower_radius = S.sqrt(S.simplify(1 - transverse * transverse))
            if enclosure(projection)[1] < 0:
                source, target, cost = oi, oj, -projection - lower_radius
            else:
                assert enclosure(projection)[0] > 0
                source, target, cost = oj, oi, projection - lower_radius
            cost = S.simplify(cost)
            rational = enclosure(cost)[0]
            assert rational > 0
            edges.append((source, target, rational, 1))
            witnesses.append((source, target, str(rational), 1, [i, j], "lower"))
    floor = Fraction(int(delta.p), int(delta.q))
    active, heights, epsilon, rounds = inclusive_floor_closure(
        edges, {1: floor}, {1: Fraction(1)}
    )
    assert active == (set() if strict_lock else {1})
    assert heights[1] == (0 if strict_lock else floor)
    contact_edges = [
        (i, j, cost, 0 if kind == "upper" else strict)
        for (i, j, cost, strict), (*_, kind) in zip(edges, witnesses)
    ]
    contact_active, contact_heights, _, _ = inclusive_floor_closure(
        contact_edges, {1: floor}, {1: Fraction(1)}
    )
    assert contact_active == {1} and contact_heights[1] == floor
    assert any(edge[:4] == (1, 0, floor, int(strict_lock)) for edge in edges)
    assert (
        S.simplify(
            D * D
            - D * delta
            + delta * delta
            - sum((x - y) ** 2 for x, y in zip((0, delta), q))
        )
        == 0
    )
    return {
        "kind": "full_source_locked_reflection",
        "D": D,
        "lock": "inactive_strict" if strict_lock else "actual_weak",
        "floor": str(delta),
        "states": states,
        "lex_active": sorted(active),
        "contact_active": sorted(contact_active),
        "epsilon": str(epsilon),
        "closure_rounds": rounds,
        "pair_checks": full_pair_checks,
        "old_H_shortens_but_new_H_replaces": bool(strict_lock),
        "scope": "triangle-free six-point nonglobal source; no canonical KKT",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graphs", type=int, default=80)
    parser.add_argument("--seed", type=int, default=1001001)
    parser.add_argument("--diameters", type=int, nargs="+", default=[20, 30, 50])
    args = parser.parse_args()
    assert args.graphs >= 0
    print(json.dumps(critical_graph_checks(), sort_keys=True))
    print(json.dumps(graph_checks(args.graphs, args.seed), sort_keys=True))
    for D in args.diameters:
        assert D >= 20
        for strict in (False, True):
            print(json.dumps(geometric_fixture(D, strict), sort_keys=True))


if __name__ == "__main__":
    main()
