#!/usr/bin/env python3
"""Exact profile sorting packets and prefix/extension identities.

Listed finite configurations and combinatorial identities only. The
all-small-curvature classification and stress continuation are analytic
claims in the companion report, not consequences of sampled coordinates.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
import json
import verify_target_c_sorted_rate_packets_2026_10_06 as s
import verify_target_c_three_direction_corner_barrier_2026_10_06 as g


PROFILES = ((5, 0, -5), (7, 2, -2, -7),
            (11, 3, 0, -3, -11), (13, 8, 1, -1, -8, -13))


def rad(p):
    return max(abs(p[0]), abs(p[1]), abs(p[0]+p[1]))


def combinatorial(profile):
    m = len(profile)
    total = 0
    for order in permutations(profile):
        alpha = [sum(order[:r]) for r in range(m+1)]
        values = {(r, j): -sum(sorted(order[:r])[:j])
                  for r in range(m+1) for j in range(r+1)}
        assert alpha[0] == alpha[m] == 0
        for r in range(1, m+1):
            for j in range(r+1):
                value = values[r, j]
                if j < r:
                    assert value >= values[r-1, j]
                if j:
                    assert value >= values[r-1, j-1]-order[r-1]
                if 0 < j < r:
                    prefix = sorted(order[:r])
                    threshold = F(prefix[j-1]+prefix[j], 2)
                    selected_suffix = [q for q in order[r:] if q < threshold]
                    k = len(selected_suffix)
                    assert value == values[m, j+k]+sum(selected_suffix)
                total += 1
        assert sum(q*q for q in order) == sum(q*q for q in profile)
    return {'profile': profile, 'permutations': len(list(permutations(profile))),
            'prefix_and_extension_checks': total}


def finite(order):
    m = len(order)
    t = F(1, 100000)
    rotation = ((1-t*t)/(1+t*t), 2*t/(1+t*t))
    sixth = (g.Q(F(1, 2)), g.Q(0, F(1, 2)))
    w = g.sub(sixth, (g.Q(1), g.Q()))
    factors = [tuple(g.Q(q) for q in g.power(rotation, a)) for a in order]
    actual = {(0, 0): (g.Q(), g.Q())}
    for r in range(1, m+1):
        total = (sum(z[0] for z in factors[:r]), sum(z[1] for z in factors[:r]))
        chosen = sorted(range(r), key=lambda h: order[h])
        prefix = (g.Q(), g.Q())
        for j in range(r+1):
            if j:
                prefix = g.add(prefix, factors[chosen[j-1]])
            point = g.add(total, g.mul(prefix, w))
            label = (r-j, j)
            for _ in range(6):
                if label in actual:
                    assert actual[label] == point
                actual[label] = point
                label = s.rotate(label)
                point = g.mul(point, sixth)
    moving = sorted(p for p in actual if rad(p) < m)
    cols = {p: i for i, p in enumerate(moving)}
    contacts = 0
    rows = []
    pairs = 0
    for p, q in combinations(actual, 2):
        gap = g.distance(actual[p], actual[q])-1
        assert gap.sign() >= 0
        pairs += 1
        if gap != g.Q():
            continue
        contacts += 1
        if p not in cols and q not in cols:
            continue
        delta = (p[0]-q[0], p[1]-q[1])
        coeff = (2*delta[0]+delta[1], delta[0]+2*delta[1])
        row = [0]*(2*len(moving))
        for point, sign in ((p, 1), (q, -1)):
            if point in cols:
                row[2*cols[point]] += sign*coeff[0]
                row[2*cols[point]+1] += sign*coeff[1]
        rows.append(row)
    assert contacts == 6*m*(m+1) and len(rows) == 6*m*m
    rank = s.rank_mod(rows, 2*len(moving))
    assert rank == 2*len(moving)
    # A full modular minor is an exact rational-rank lower certificate.
    triangle = ((0, 0), (1, 0), (0, 1))
    assert all(g.distance(actual[p], actual[q]) == g.Q(1)
               for p, q in combinations(triangle, 2))
    wall = []
    rays = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
    for k in range(6):
        e, f = rays[k], rays[(k+1)%6]
        wall.extend(((m-j)*e[0]+j*f[0], (m-j)*e[1]+j*f[1]) for j in range(m))
    containment = 0
    for p in moving:
        for k, a in enumerate(wall):
            b = wall[(k+1)%len(wall)]
            assert g.cross(g.sub(actual[b], actual[a]), g.sub(actual[p], actual[a])).sign() > 0
            containment += 1
    return {'order': order, 'pair_checks': pairs, 'unit_contacts': contacts,
            'active_unit_rows': len(rows), 'exact_full_limiting_rank': rank,
            'interior_containment_checks': containment, 'first_ring_triangle': True}


def main():
    finite_cases = []
    for profile in PROFILES:
        finite_cases.append(finite(profile))
        finite_cases.append(finite(tuple(reversed(profile))))
        if len(profile) >= 4:
            finite_cases.append(finite(profile[::2]+profile[1::2]))
    print(json.dumps({'classification': 'exact finite profile checks',
                      'combinatorial': [combinatorial(p) for p in PROFILES],
                      'finite_cases': finite_cases,
                      'not_proved_by_script': ['normal-cone continuation',
                          'arbitrary-cloud classification', 'global optimality',
                          'macroscopic extraction', 'C-II or Level I']}, sort_keys=True))


if __name__ == '__main__':
    main()
