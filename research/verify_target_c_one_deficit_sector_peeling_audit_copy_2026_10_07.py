#!/usr/bin/env python3
"""Exact finite half-plane peeling and constructive strict opening.

The accompanying report proves the all-M>=4, sufficiently-small-curvature
statement analytically. These checks cover only the listed rational cases.
M=3 non-peeling is not an impossibility or global-optimality certificate.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
import json
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g

def geometry(m, order, t):
    """Independent exact construction of the sorted curved chart."""
    assert sorted(order) == list(range(-m + 1, m, 2))
    base = ((1 - t*t)/(1 + t*t), 2*t/(1 + t*t))
    sixth = (g.Q(F(1, 2)), g.Q(F(0), F(1, 2)))
    w = g.sub(sixth, (g.Q(1), g.Q()))
    z = [tuple(g.Q(x) for x in g.power(base, k)) for k in order]
    actual = {(0, 0): (g.Q(), g.Q())}
    for r in range(1, m + 1):
        total = (sum((q[0] for q in z[:r]), g.Q()),
                 sum((q[1] for q in z[:r]), g.Q()))
        chosen = sorted(range(r), key=lambda h: order[h])
        prefix = (g.Q(), g.Q())
        for j in range(r + 1):
            if j:
                prefix = g.add(prefix, z[chosen[j - 1]])
            value = g.add(total, g.mul(prefix, w))
            site = (r - j, j)
            for _ in range(6):
                if site in actual:
                    assert actual[site] == value
                actual[site] = value
                site = (-site[1], site[0] + site[1])
                value = g.mul(value, sixth)
    return actual


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0]+p[1]))


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


def encoded(v):
    return [[str(q.a), str(q.b)] for q in v]


def case(m, construct=False):
    t = F(1, 10000)
    actual = geometry(m, list(range(m-1, -m, -2)), t)
    actual.pop((1, m-2))
    moving = {p for p in actual if rad(p) < m}
    edges = set()
    pair_checks = 0
    for p, q in combinations(actual, 2):
        gap = g.distance(actual[p], actual[q])-1
        assert gap.sign() >= 0
        pair_checks += 1
        if gap == g.Q() and (p in moving or q in moving):
            edges.add(frozenset((p, q)))
    original = set(edges)
    steps = []
    normals = {}
    while True:
        changed = False
        for p in sorted(moving):
            incident = sorted((e for e in edges if p in e), key=lambda e: sorted(e))
            if not incident:
                continue
            neighbours = [next(iter(e-{p})) for e in incident]
            vectors = [g.sub(actual[q], actual[p]) for q in neighbours]
            for i, j in combinations_with_replacement(range(len(vectors)), 2):
                n = g.add(vectors[i], vectors[j])
                if all(dot(n, v).sign() > 0 for v in vectors):
                    normals[p] = n
                    steps.append({'site': p, 'neighbours': neighbours,
                                  'separator': encoded(n)})
                    edges.difference_update(incident)
                    changed = True
                    break
        if not changed:
            break
    result = {'M': m, 'half_angle_tangent': str(t),
              'all_lower_pair_checks': pair_checks, 'unit_rows': len(original),
              'remaining_rows': len(edges), 'half_plane_steps': len(steps),
              'steps': steps}
    if m == 3:
        assert len(edges) == len(original) == 50 and not steps
        result['classification'] = 'local peeling regression only'
        return result
    assert not edges and len(steps) == len(moving)
    result['classification'] = 'complete exact half-plane elimination'
    if construct:
        velocity = {}
        zero = (g.Q(), g.Q())
        adjacency = {p: set() for p in actual}
        for e in original:
            p, q = tuple(e)
            adjacency[p].add(q)
            adjacency[q].add(p)
        halvings = 0
        for step in steps:
            p = tuple(step['site'])
            n = normals[p]
            amplitude = F(1)
            while True:
                trial = g.scale(n, -amplitude)
                if all(dot(g.sub(actual[p], actual[q]),
                           g.sub(trial, velocity.get(q, zero))).sign() > 0
                       for q in adjacency[p] if q not in moving or q in velocity):
                    break
                amplitude /= 2
                halvings += 1
            velocity[p] = trial
        for e in original:
            p, q = tuple(e)
            assert dot(g.sub(actual[p], actual[q]),
                       g.sub(velocity.get(p, zero), velocity.get(q, zero))).sign() > 0
        result['constructive_opening_rows'] = len(original)
        result['successive_dyadic_halvings'] = halvings
        result['velocity'] = [{'site': p, 'value': encoded(velocity[p])}
                              for p in sorted(velocity)]
    return result


def main():
    results = [case(m, construct=m in (4, 6)) for m in range(3, 11)]
    print(json.dumps({'classification': 'exact finite peeling certificates',
                      'scope': 'listed rational cases, not global optimality',
                      'cases': results}, sort_keys=True))


if __name__ == '__main__':
    main()
