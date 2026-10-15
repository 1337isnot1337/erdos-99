#!/usr/bin/env python3
"""Exact finite checks for the half-depth cap and fan-forest candidate.

Universal assertions are analytic in the report. Arc fixtures are nonglobal
and have no normalized full-source KKT stress. Local fan balances are not
full-source stress certificates.
"""
from fractions import Fraction as F
from itertools import combinations
from math import ceil, isqrt
import json


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[0], a[1]-b[1]


def scale(p, t):
    return p[0]*t, p[1]*t


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def dist2(a, b):
    r = sub(a, b)
    return dot(r, r)


def cross(a, b, c):
    ab, ac = sub(b, a), sub(c, a)
    return ab[0]*ac[1]-ab[1]*ac[0]


def hull(points):
    indexed = sorted((p, i) for i, p in enumerate(points))
    sides = []
    for order in (indexed, list(reversed(indexed))):
        chain = []
        for p, i in order:
            while len(chain) > 1 and cross(chain[-2][0], chain[-1][0], p) <= 0:
                chain.pop()
            chain.append((p, i))
        sides.append(chain[:-1])
    return [i for p, i in sides[0]+sides[1]]


def square_competitor(n, diameter):
    width = isqrt(n-1)+1
    points = [(F(j % width), F(j // width)) for j in range(n)]
    for a, b in combinations(points, 2):
        assert 1 <= dist2(a, b) < diameter*diameter
    return n*(n-1)//2


def quadratic_checks():
    count = 0
    for diameter in map(F, (10, 20, 40)):
        for delta in (1/diameter, 1/(2*diameter)):
            for ratio in map(F, (0, F(1, 8), F(1, 4), F(1, 2), 1, 2, 20)):
                e = ratio*delta
                a = e*e/delta+delta/2 if e <= delta/2 else e+delta/4
                assert a >= e and a >= delta/2
                for j in range(-20, 3):
                    t = F(j, 4)*delta
                    assert t <= delta/2
                    f = diameter*diameter+4*e*e-4*(a-t/2)**2-2*delta*t+delta*delta
                    if e <= delta/2:
                        assert f == diameter*diameter-(t-2*e*e/delta)**2
                    else:
                        assert f-diameter*diameter == (t-delta/2)*(4*e-3*delta/2-t)
                    assert f <= diameter*diameter
                    epsilon = delta/100
                    strict = diameter*diameter+4*e*e-4*(a+epsilon-t/2)**2-2*delta*t+delta*delta
                    assert strict < diameter*diameter
                    count += 1
    return count


def cap_samples():
    valid = increasing = 0
    cases = 0
    for diameter in map(F, (10, 20, 40)):
        for margin in map(F, (0, F(1, 8), F(1, 2))):
            radius = diameter/2+margin
            e2 = radius*radius-diameter*diameter/4
            candidates = set()
            for j in range(-16, 17):
                t = F(j, 16)
                direction = ((1-t*t)/(1+t*t), 2*t/(1+t*t))
                for radial in (F(1), F(7, 8), F(3, 4)):
                    candidates.add(scale(direction, radius*radial))
            candidates = sorted(candidates)
            for midpoint_shift in sorted({-margin, F(0), margin}):
                p = (diameter/2+midpoint_shift, F(0))
                a = (-diameter/2+midpoint_shift, F(0))
                assert dot(p, p) <= radius*radius
                assert dot(a, a) <= radius*radius
                assert dist2(p, a) == diameter*diameter
                available = [
                    x for x in candidates
                    if 1 <= dist2(x, p) <= diameter*diameter
                    and 1 <= dist2(x, a) <= diameter*diameter
                ]
                for delta in (1/diameter, 1/(2*diameter)):
                    cases += 1
                    for x in available:
                        if e2 <= delta*delta/4:
                            shallow = x[0] > e2/delta+delta/2
                        else:
                            h = x[0]-delta/4
                            shallow = h > 0 and h*h > e2
                        if not shallow:
                            continue
                        for y in available:
                            old = dist2(x, y)
                            if not 1 <= old <= diameter*diameter:
                                continue
                            moved = (x[0]-delta, x[1])
                            new = dist2(moved, y)
                            valid += 1
                            if new > old:
                                assert new < diameter*diameter, (diameter, radius, x, y)
                                increasing += 1
    assert valid and increasing
    return {"parameter_cases": cases, "valid_cross_pairs": valid,
            "increasing_cross_pairs": increasing}


def sharp_fixtures():
    source_pairs = competitor_pairs = cases = 0
    for diameter in map(F, (10, 20, 40)):
        radius, delta = diameter/2, 1/diameter
        for j in (1, 2, 10):
            t = delta/(4*radius)*(1-F(1, 10*j))
            x = (2*radius*t/(1+t*t), radius*(1-t*t)/(1+t*t))
            y = (x[0], -x[1])
            p, a = (radius, F(0)), (-radius, F(0))
            points = [p, a, x, y]
            assert dot(x, x) == radius*radius
            assert dot(y, y) == radius*radius
            assert 0 < x[0] < delta/2
            for v, w in combinations(points, 2):
                assert 1 <= dist2(v, w) <= diameter*diameter
                source_pairs += 1
            assert dist2(p, a) == diameter*diameter
            moved = (x[0]-delta, x[1])
            assert dist2(moved, y) > diameter*diameter
            proposed_margin = x[0]-delta/(100*j)
            assert 0 < proposed_margin < x[0] < delta/2
            assert radius-x[0] < radius-proposed_margin
            assert radius-x[0] > radius-delta/2
            competitor_pairs += square_competitor(4, diameter)
            cases += 1
    return {"cases": cases, "source_pairs": source_pairs,
            "competitor_pairs": competitor_pairs}


def arc_fixture(u_count):
    m = 32*u_count*u_count
    diameter = F(m)+F(1, 16*m)
    sigma = F(1, 4*m)
    w = (1-sigma*sigma)/(1+sigma*sigma)
    rotation = (1-1/(2*diameter*diameter), w/diameter)
    assert dot(rotation, rotation) == 1
    arc = [(diameter, F(0))]
    for j in range(u_count+1):
        old = arc[-1]
        arc.append((old[0]*rotation[0]-old[1]*rotation[1],
                    old[0]*rotation[1]+old[1]*rotation[0]))
    points = [(F(0), F(0))]+arc
    n = len(points)
    contacts, diameters = set(), set()
    pairs = 0
    for i, j in combinations(range(n), 2):
        d2 = dist2(points[i], points[j])
        assert 1 <= d2 <= diameter*diameter
        if d2 == 1:
            contacts.add((i, j))
        if d2 == diameter*diameter:
            diameters.add((i, j))
        pairs += 1
    assert contacts == {(i, i+1) for i in range(1, n-1)}
    assert diameters == {(0, i) for i in range(1, n)}
    neighbors = {i: set() for i in range(n)}
    h_neighbors = {i: set() for i in range(n)}
    for i, j in contacts:
        neighbors[i].add(j)
        neighbors[j].add(i)
    for i, j in diameters:
        h_neighbors[i].add(j)
        h_neighbors[j].add(i)
    fans = [
        i for i in range(n)
        if len(h_neighbors[i]) == 1 and len(neighbors[i]) == 2
        and all(dist2(points[next(iter(h_neighbors[i]))], points[v]) == diameter*diameter
                for v in neighbors[i])
    ]
    assert fans == list(range(2, n-1)) and len(fans) == u_count
    full_hull = hull(points)
    assert set(full_hull) == set(range(n))
    hull_edges = {
        tuple(sorted((i, j)))
        for i, j in zip(full_hull, full_hull[1:]+full_hull[:1])
    }
    assert contacts <= hull_edges
    fan_edges = {(i, j) for i, j in contacts if i in fans and j in fans}
    assert len(fan_edges) == u_count-1
    independent = fans[::2]
    assert len(independent) == ceil(u_count/2)
    assert all(not (i in independent and j in independent) for i, j in fan_edges)
    best = 0
    for mask in range(1 << u_count):
        if mask & (mask << 1):
            continue
        best = max(best, mask.bit_count())
    assert best == len(independent)
    incident = {(i, j) for i, j in contacts if i in fans or j in fans}
    assert len(incident) == u_count+1
    balances = 0
    for beta in (F(1, 3), F(1, 100), F(1, 10**12)):
        alpha = diameter*diameter*beta
        for i in fans:
            reaction = scale(sub(points[i], points[0]), beta)
            force = (F(0), F(0))
            for v in neighbors[i]:
                force = add(force, scale(sub(points[i], points[v]), alpha))
            assert force == reaction
            u = scale(points[i], 1/diameter)
            assert all(dot(sub(points[i], points[v]), u) == 1/(2*diameter)
                       for v in neighbors[i])
            balances += 1
        assert (u_count+1)*alpha == diameter*diameter*(u_count+1)*beta
        independent_edges = {(i, j) for i, j in contacts if i in independent or j in independent}
        assert len(independent_edges) == 2*len(independent)
    # Carrier is retained but has no contacts and all diameter vectors lie
    # in the same strict positive-x half-plane. No normalized KKT stress exists.
    assert not neighbors[0]
    assert all(points[i][0] > 0 for i in h_neighbors[0])
    return {"fans": u_count, "source_labels": n, "source_pairs": pairs,
            "competitor_pairs": square_competitor(n, diameter),
            "independent_fans": best, "local_balance_checks": balances}


def main():
    result = {
        "status": "PASS",
        "classification": "finite nonglobal fixtures and algebraic samples",
        "quadratic_identity_checks": quadratic_checks(),
        "circumcircle_cap_samples": cap_samples(),
        "sharp_half_depth_fixtures": sharp_fixtures(),
        "fan_arc_fixtures": [arc_fixture(u) for u in (3, 4, 7, 8, 12, 16)],
        "does_not_prove": [
            "universal claims by finite sampling",
            "full-source KKT equilibrium for the arc fixtures",
            "canonical shallow closure or bounded path congestion",
            "global optimality or C-II or Level I closure",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
