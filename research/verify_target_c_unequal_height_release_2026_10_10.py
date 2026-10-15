#!/usr/bin/env python3
"""Full-source unequal-height release and exact shortest-path certificate.

Requires SymPy and the preceding Slot 01 fixture helper. All decisions use
symbolic identities or rational enclosures. The source is explicitly nonglobal.
"""

import argparse
import heapq
import json
import math
from fractions import Fraction
from itertools import combinations

import sympy as S
from verify_target_c_source_realized_owner_sink_2026_10_10 import (
    Source,
    SymbolicSource,
    component_count,
    enclosure,
    squared_distance,
)


def largest_release_support(costs, floors, bounds):
    """Exact rational floor closure; zero and bound edges stay distinguished."""
    nodes = {0, *floors}
    reverse = {i: [] for i in nodes}
    for (i, j), cost in costs.items():
        assert cost >= 0
        reverse[j].append((i, cost))
    zero = {0}
    rounds = []
    while True:
        caps = {i: Fraction(0) if i in zero else bounds[i] for i in nodes}
        queue = [(value, i) for i, value in caps.items()]
        heapq.heapify(queue)
        while queue:
            value, i = heapq.heappop(queue)
            if caps[i] != value:
                continue
            for j, cost in reverse[i]:
                if value + cost < caps[j]:
                    caps[j] = value + cost
                    heapq.heappush(queue, (caps[j], j))
        removed = {i for i in floors if i not in zero and caps[i] <= floors[i]}
        rounds.append(
            {
                "caps": {str(i): str(caps[i]) for i in sorted(floors)},
                "new_zero": sorted(removed),
            }
        )
        if not removed:
            return set(floors) - zero, caps, rounds
        zero.update(removed)


def compile_costs(source, D2, cloud, direction=1):
    """Conservative rational costs for exact full-pair difference inequalities.

    Replacing an algebraic cost by its lower enclosure is sufficient for an
    endpoint certificate. Failure of this conservative graph is not by itself
    an exact infeasibility certificate for arbitrary algebraic source costs.
    """
    costs = {}
    witnesses = {}

    def add(i, j, expr, kind, pair):
        cost = enclosure(expr)[0]
        assert cost >= 0, (kind, pair, expr, cost)
        if i == j or cost >= cloud:
            return
        if (i, j) not in costs or cost < costs[i, j]:
            costs[i, j] = cost
            witnesses[i, j] = [kind, *(source.names[k] for k in pair)]

    for a, b in combinations(range(len(source.pts)), 2):
        i, j = source.owners[a], source.owners[b]
        if i == j:
            continue
        p, q = source.pts[a], source.pts[b]
        dx, dy = p[0] - q[0], direction * (p[1] - q[1])
        upper = S.sqrt(D2 - dx * dx)
        add(i, j, upper - dy, "upper", (a, b))
        add(j, i, upper + dy, "upper", (a, b))
        if (a, b) in source.edges:
            assert (i == 0) != (j == 0)
            continue
        transverse = enclosure(dx * dx)
        if transverse[0] > 1:
            continue
        if transverse[1] > 1:
            assert S.simplify(dx * dx - 1) == 0
            lower = S.Integer(0)
        else:
            lower = S.sqrt(1 - dx * dx)
        height = enclosure(dy)
        if height[0] > 0:
            add(j, i, dy - lower, "lower-order", (a, b))
        else:
            assert height[1] < 0
            add(i, j, -dy - lower, "lower-order", (a, b))
    return costs, witnesses


def release_floors(source, direction=1):
    """Conservative upper enclosures of all actual cut-contact thresholds."""
    floors = {i: Fraction(0) for i in source.owners if i}
    for a, b in source.edges:
        i, j = source.owners[a], source.owners[b]
        if i == j:
            continue
        assert (i == 0) != (j == 0)
        moving, fixed = (a, b) if i else (b, a)
        owner = source.owners[moving]
        threshold = enclosure(
            -2 * direction * (source.pts[moving][1] - source.pts[fixed][1])
        )[1]
        floors[owner] = max(floors[owner], threshold)
    return floors


def verify(H):
    assert H >= 30
    source = Source(H).build()
    da, db = source.delta
    guard_gap = S.Rational(5, 2) * db
    guard = source.point((5, 3 + guard_gap), 0, "U")
    right_top = source.strips[1][0][-1]
    n = len(source.pts)
    assert n == H + 80 and guard == n - 1
    D2 = H * H + 25
    cloud = 2 * da
    assert da > guard_gap > 2 * db > 0
    assert 2 * Fraction(cloud) * enclosure(S.sqrt(D2))[1] < 1
    count, adj = component_count(n, source.edges)
    assert count == 2 and not adj[guard]
    assert all(not (adj[a] & adj[b]) for a, b in source.edges)

    costs, witnesses = compile_costs(source, D2, Fraction(cloud))
    floors = release_floors(source)
    assert floors == {1: Fraction(da), 2: Fraction(db)}
    active, caps, rounds = largest_release_support(
        costs,
        floors,
        {1: Fraction(cloud), 2: Fraction(cloud)},
    )
    assert active == {1, 2}
    scale = Fraction(9, 10)
    computed = {i: scale * caps[i] for i in active}
    assert computed[1] > Fraction(da)
    assert computed[2] > Fraction(db)
    assert computed[1] > computed[2]
    assert computed[2] == Fraction(9, 4) * Fraction(db)
    for (i, j), cost in costs.items():
        assert computed.get(i, 0) - computed.get(j, 0) <= cost
        if witnesses[i, j][0] == "lower-order":
            assert computed.get(i, 0) - computed.get(j, 0) < cost

    # Give the retained isolate its own zero-floor height variable. No anchor
    # theorem is used: all its old and endpoint pairs are checked explicitly.
    source.owners[guard] = 3
    free_costs, free_witnesses = compile_costs(source, D2, Fraction(cloud))
    free_floors = release_floors(source)
    assert free_floors == {1: Fraction(da), 2: Fraction(db), 3: Fraction(0)}
    free_active, free_caps, free_rounds = largest_release_support(
        free_costs, free_floors, {i: Fraction(cloud) for i in free_floors}
    )
    assert free_active == {1, 2, 3}
    assert all(free_caps[i] == Fraction(cloud) for i in free_active)
    free_computed = {i: scale * free_caps[i] for i in free_active}
    negative_costs, negative_witnesses = compile_costs(source, D2, Fraction(cloud), -1)
    negative_floors = release_floors(source, -1)
    assert all(value == 0 for value in negative_floors.values())
    negative_active, _, negative_rounds = largest_release_support(
        negative_costs,
        negative_floors,
        {i: Fraction(cloud) for i in negative_floors},
    )
    assert negative_active == {3}
    assert negative_rounds[0]["new_zero"] == [1, 2]
    assert negative_costs[1, 0] == negative_costs[2, 0] == 0
    assert negative_witnesses[1, 0][0] == negative_witnesses[2, 0][0] == "upper"
    source.owners[guard] = 0

    states = [
        {},
        {1: cloud},
        {2: cloud},
        {1: cloud, 2: cloud},
        {1: da + db / 4, 2: 2 * db},
        {
            i: S.Rational(value.numerator, value.denominator)
            for i, value in computed.items()
        },
        {
            i: S.Rational(value.numerator, value.denominator)
            for i, value in free_computed.items()
        },
        {1: da + db / 4, 2: 2 * db, 3: -db / 4},
    ]
    old_diameters = set(source.diameter)
    right_diameter = source.diameter[1]
    bad = {}
    checks = 0
    opened = []
    endpoint_maxima = []
    for state, shifts in enumerate(states):
        points = [
            (
                p[0],
                p[1]
                + shifts.get(3 if state in (6, 7) and index == guard else owner, 0),
            )
            for index, (p, owner) in enumerate(zip(source.pts, source.owners))
        ]
        boxes = [tuple(enclosure(x) for x in p) for p in points]
        losses = 0
        target_D2 = D2 - 2 * H * shifts.get(2, 0) + shifts.get(2, 0) ** 2
        for a, b in combinations(range(n), 2):
            checks += 1
            pair = (a, b)
            distance = squared_distance(boxes[a], boxes[b])
            if pair in source.edges:
                target = S.Integer(1)
                if source.owners[a] != source.owners[b]:
                    owner = source.owners[a] or source.owners[b]
                    shift = shifts.get(owner, 0)
                    target += shift * (shift - source.delta[owner - 1])
                assert target >= 1
                assert (
                    S.simplify(
                        sum((x - y) ** 2 for x, y in zip(points[a], points[b])) - target
                    )
                    == 0
                )
                losses += int(bool(target > 1))
            elif distance[1] < 1:
                bad.setdefault(pair, []).append(state)
            else:
                assert distance[0] > 1, (
                    state,
                    source.names[a],
                    source.names[b],
                    distance,
                )
                if state >= 4:
                    dx = source.pts[a][0] - source.pts[b][0]
                    if enclosure(dx * dx)[1] <= 1:
                        old_dy = source.pts[a][1] - source.pts[b][1]
                        new_dy = points[a][1] - points[b][1]
                        assert enclosure(old_dy * new_dy)[0] > 0
            assert distance[1] <= D2
            if pair not in old_diameters:
                assert distance[1] < D2
            if state >= 4:
                assert (
                    distance == (target_D2, target_D2)
                    if pair == right_diameter or state == 6 and pair in old_diameters
                    else distance[1] < target_D2
                ), (state, source.names[a], source.names[b], distance, target_D2)
        opened.append(losses)
        if state >= 4:
            assert target_D2 < D2
            endpoint_maxima.append(str(target_D2))
    expected = {
        tuple(sorted(source.special[0])): [1],
        tuple(sorted(source.special[1])): [2],
        tuple(sorted([guard, right_top])): [2, 3],
    }
    assert bad == expected, (bad, expected)
    assert opened == [0, 12, 12, 24, 24, 24, 24, 24]
    width = math.isqrt(n - 1) + 1
    assert width * width >= n and 2 * (width - 1) ** 2 < D2
    return {
        "H": H,
        "vertices": n,
        "old_contacts": len(source.edges),
        "retained_contact_isolates": 1,
        "full_pair_state_checks": checks,
        "common_cloud": str(cloud),
        "common_height_interval_zero_only": {
            "lower": "0",
            "lower_open": True,
            "upper": str(cloud),
        },
        "common_directions_excluded": "all, by analytic CTG proof",
        "common_bad_pairs_at_cloud": {
            source.names[a] + ":" + source.names[b]: value
            for (a, b), value in bad.items()
        },
        "manual_unequal_heights": {
            str(i): str(value) for i, value in states[4].items()
        },
        "mixed_sign_heights": {str(i): str(value) for i, value in states[7].items()},
        "mixed_sign_positive_clipping_recovers_manual_endpoint": True,
        "computed_heights": {str(i): str(value) for i, value in computed.items()},
        "active_support": sorted(active),
        "floor_closure_rounds": rounds,
        "transported_isolate_heights": {
            str(i): str(value) for i, value in free_computed.items()
        },
        "transported_isolate_active_support": sorted(free_active),
        "transported_isolate_floor_closure_rounds": free_rounds,
        "negative_direction_active_support": sorted(negative_active),
        "negative_direction_floor_closure_rounds": negative_rounds,
        "transported_isolate_cost_arcs": [
            {"from": i, "to": j, "cost": str(value), "witness": free_witnesses[i, j]}
            for (i, j), value in sorted(free_costs.items())
        ],
        "binding_cost_arcs": [
            {"from": i, "to": j, "cost": str(value), "witness": witnesses[i, j]}
            for (i, j), value in sorted(costs.items())
        ],
        "contacts_removed_in_each_state": opened,
        "unequal_endpoint_maxima_squared": endpoint_maxima,
        "triangle_free_valid_endpoints": True,
        "all_upper_pairs_checked": True,
        "positive_KKT_claim": False,
        "global_minimizer": False,
        "classification": "exact regression and finite endpoints",
    }


def verify_symbolic_limit():
    t = S.Symbol("t", positive=True)
    source = SymbolicSource(parameter=t).build()
    da, db = source.delta
    guard = source.point((5, 3 + S.Rational(5, 2) * db), 0, "U")
    n = len(source.pts)
    limit_points = [tuple(S.simplify(x.subs(t, 0)) for x in p) for p in source.pts]
    limit_boxes = [tuple(enclosure(x) for x in p) for p in limit_points]
    rows = []
    strict = 0
    shifts = [
        {},
        {1: da + db / 4, 2: 2 * db},
        {1: 9 * da / 5, 2: 9 * da / 5, 3: 9 * da / 5},
        {1: da + db / 4, 2: 2 * db, 3: -db / 4},
    ]
    for a, b in combinations(range(n), 2):
        if (a, b) in source.edges:
            continue
        bounds = squared_distance(limit_boxes[a], limit_boxes[b])
        if bounds[0] > 1:
            strict += 1
            continue
        assert (
            S.simplify(
                sum((x - y) ** 2 for x, y in zip(limit_points[a], limit_points[b])) - 1
            )
            == 0
        )
        terms = []
        for mode, heights in enumerate(shifts):
            ps = [S.Matrix(source.pts[k]) for k in (a, b)]
            for k, p in zip((a, b), ps):
                owner = 3 if mode in (2, 3) and k == guard else source.owners[k]
                p[1] += heights.get(owner, 0)
            expr = S.cancel((ps[0] - ps[1]).dot(ps[0] - ps[1]) - 1)
            numerator, denominator = S.fraction(expr)
            den0 = S.simplify(denominator.subs(t, 0))
            assert den0 > 0
            poly = S.Poly(numerator, t)
            power = min(degree[0] for degree, _ in poly.terms())
            coefficient = S.simplify(poly.coeff_monomial(t**power) / den0)
            assert coefficient > 0
            terms.append([power, str(coefficient)])
        rows.append(
            {
                "pair": source.names[a] + ":" + source.names[b],
                "old_manual_transport_mixed_leading_slacks": terms,
            }
        )
    assert len(rows) == 13
    return {
        "critical_pairs": rows,
        "strict_limit_noncontact_pairs": strict,
        "classification": "asymptotic family proof support",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--heights", nargs="+", type=int, default=[30, 31, 100])
    parser.add_argument("--symbolic-limit", action="store_true")
    args = parser.parse_args()
    for H in args.heights:
        print(json.dumps(verify(H), sort_keys=True))
    if args.symbolic_limit:
        print(json.dumps(verify_symbolic_limit(), sort_keys=True))
