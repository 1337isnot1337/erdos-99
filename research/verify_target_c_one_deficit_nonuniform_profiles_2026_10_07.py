#!/usr/bin/env python3
"""Exact nonuniform-profile stress checks for the all-M packet theorem.

Checks two fixed symmetric profiles at t=1/10000. This is an edge-case
regression only; the arbitrary-profile and all-small-t result is analytic.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0] + p[1]))


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def geometry(m, rates, t):
    assert len(rates) == m and all(rates[i] > rates[i + 1]
                                    for i in range(m - 1))
    assert all(rates[m - 1 - i] == -rates[i] for i in range(m))
    base = ((1 - t*t) / (1 + t*t), 2*t / (1 + t*t))
    sixth = (g.Q(F(1, 2)), g.Q(F(0), F(1, 2)))
    w = g.sub(sixth, (g.Q(1), g.Q()))
    z = [tuple(g.Q(x) for x in g.power(base, k)) for k in rates]
    actual = {(0, 0): (g.Q(), g.Q())}
    for r in range(1, m + 1):
        total = (sum((q[0] for q in z[:r]), g.Q()),
                 sum((q[1] for q in z[:r]), g.Q()))
        order = sorted(range(r), key=lambda h: rates[h])
        prefix = (g.Q(), g.Q())
        for j in range(r + 1):
            if j:
                prefix = g.add(prefix, z[order[j - 1]])
            value = g.add(total, g.mul(prefix, w))
            site = (r - j, j)
            for _ in range(6):
                if site in actual:
                    assert actual[site] == value
                actual[site] = value
                site = (-site[1], site[0] + site[1])
                value = g.mul(value, sixth)
    return actual


def case(m, rates):
    t = F(1, 10000)
    epsilon = F(1, 10**24)
    actual = geometry(m, rates, t)
    hole, deleted = (1, m - 2), (1, m - 1)
    actual.pop(hole)
    moving = {p for p in actual if rad(p) < m}
    edges = set()
    pair_checks = 0
    for p, q in combinations(actual, 2):
        d = g.distance(actual[p], actual[q])
        assert (d - 1).sign() >= 0
        pair_checks += 1
        if d == g.Q(1) and (p in moving or q in moving):
            edges.add(frozenset((p, q)))

    original = set(edges)
    steps, normals = [], {}
    while True:
        changed = False
        for p in sorted(moving):
            incident = sorted((e for e in edges if p in e), key=lambda e: sorted(e))
            if not incident:
                continue
            neighbors = [next(iter(e - {p})) for e in incident]
            vectors = [g.sub(actual[q], actual[p]) for q in neighbors]
            for i, j in combinations_with_replacement(range(len(vectors)), 2):
                n = g.add(vectors[i], vectors[j])
                if all(dot(n, v).sign() > 0 for v in vectors):
                    normals[p] = n
                    steps.append(p)
                    edges.difference_update(incident)
                    changed = True
                    break
        if not changed:
            break
    assert not edges and len(steps) == len(moving)

    adjacency = {p: set() for p in actual}
    for edge in original:
        p, q = tuple(edge)
        adjacency[p].add(q)
        adjacency[q].add(p)
    zero = (g.Q(), g.Q())
    velocity = {}
    halvings = 0
    for p in steps:
        amplitude = F(1)
        while True:
            trial = g.scale(normals[p], -amplitude)
            open_so_far = all(
                dot(g.sub(actual[p], actual[q]),
                    g.sub(trial, velocity.get(q, zero))).sign() > 0
                for q in adjacency[p] if q not in moving or q in velocity)
            if open_so_far:
                break
            amplitude /= 2
            halvings += 1
            assert halvings < 10000
        velocity[p] = trial

    for p, q in original:
        assert dot(g.sub(actual[p], actual[q]),
                   g.sub(velocity.get(p, zero), velocity.get(q, zero))).sign() > 0
    inserted = [g.add(actual[p], g.scale(velocity[p], epsilon))
                for p in sorted(moving)]

    delta = rates[0] - rates[1]
    exponent_num = rates[0] + rates[1]
    assert delta % 2 == 0 and exponent_num % 2 == 0
    exponent = exponent_num // 2
    # sin(delta*atan(t)) from Im((1+i*t)^delta)/(1+t^2)^(delta/2).
    real = imag = F(0)
    from math import comb
    for k in range(delta + 1):
        term = F(comb(delta, k)) * t**k
        if k % 4 == 0:
            real += term
        elif k % 4 == 1:
            imag += term
        elif k % 4 == 2:
            real -= term
        else:
            imag -= term
    sine = imag / (1 + t*t)**(delta // 2)
    w = (g.Q(F(-1, 2)), g.Q(0, F(1, 2)))
    rotation = g.power(((1 - t*t)/(1 + t*t), 2*t/(1 + t*t)), exponent)
    tangent = g.mul(rotation, w)
    inward = (-tangent[1], tangent[0])
    root = g.add(actual[deleted], g.scale(inward, 3*sine))
    inserted.append(root)
    assert len(inserted) == 3*m*m - 3*m + 1

    rays = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
    wall = []
    for k in range(6):
        e, e1 = rays[k], rays[(k + 1) % 6]
        for j in range(m):
            wall.append(((m-j)*e[0] + j*e1[0],
                         (m-j)*e[1] + j*e1[1]))
    assert len(set(wall)) == 6*m
    wall_points = [actual[p] for p in wall]
    retained = [actual[p] for p in wall if p != deleted]
    for i in range(len(wall)):
        e1 = g.sub(wall_points[(i + 1) % len(wall)], wall_points[i])
        e2 = g.sub(wall_points[(i + 2) % len(wall)], wall_points[(i + 1) % len(wall)])
        assert g.cross(e1, e2).sign() > 0
        assert g.distance(wall_points[i], wall_points[(i + 1) % len(wall)]) == g.Q(1)
    wall_diameter2 = max((g.distance(p, q) for p, q in combinations(wall_points, 2)),
                         key=lambda x: float(x.a) + 1.7320508075688772*float(x.b))
    for p, q in combinations(wall_points, 2):
        assert (wall_diameter2 - g.distance(p, q)).sign() >= 0
    wall_contacts = 0
    for i, p in enumerate(wall_points):
        for j in range(i + 1, len(wall_points)):
            d = g.distance(p, wall_points[j])
            adjacent = j == i + 1 or (i == 0 and j == len(wall_points) - 1)
            assert (d == g.Q(1)) == adjacent
            wall_contacts += int(d == g.Q(1))

    lower = upper = containment = 0
    for x in inserted:
        for i, a in enumerate(wall_points):
            b = wall_points[(i + 1) % len(wall_points)]
            assert g.cross(g.sub(b, a), g.sub(x, a)).sign() > 0
            containment += 1
        for y in retained:
            d = g.distance(x, y)
            assert (d - 1).sign() > 0 and (wall_diameter2 - d).sign() > 0
            lower += 1
            upper += 1
    for x, y in combinations(inserted, 2):
        d = g.distance(x, y)
        assert (d - 1).sign() > 0 and (wall_diameter2 - d).sign() > 0
        lower += 1
        upper += 1

    return {'M': m, 'rates': rates, 't': str(t), 'epsilon': str(epsilon),
            'interior_sites_opened': len(moving), 'opened_unit_rows': len(original),
            'peeling_steps': len(steps), 'dyadic_halvings': halvings,
            'chart_pair_checks': pair_checks, 'wall_contacts': wall_contacts,
            'inserted_sites': len(inserted), 'strict_lower_pairs': lower,
            'strict_upper_pairs': upper, 'strict_wall_containment_checks': containment}


def main():
    cases = [case(4, [5, 1, -1, -5]),
             case(6, [8, 4, 1, -1, -4, -8])]
    print(json.dumps({'classification': 'exact nonuniform-profile stress checks',
                      'arithmetic': 'Q(sqrt(3)) and rational parameters',
                      'scope': 'two fixed profiles at t=1/10000; no asymptotic or source claim',
                      'cases': cases}, sort_keys=True))


if __name__ == '__main__':
    main()
