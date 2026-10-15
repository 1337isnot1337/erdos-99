#!/usr/bin/env python3
"""Certified strict competitors for two feasible pentagon-capped wall packets.

Reconstructs the 2026-10-05 capped near-triangular grid geometry and moves
the entire packet, using its actual global diameter in place of the
original arbitrary fixed wall pins. Directed rational bounds certify
all old/new pairs. Contact equalities follow from the stated unit-vector
and regular-pentagon radical identities, not from interval containment.
No source packet is claimed canonical or globally optimal.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json


Q = 10 ** 24


def rat(x):
    x = F(x)
    a = x.numerator * Q
    return a // x.denominator, -((-a) // x.denominator)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = [x * y for x in a for y in b]
    lo, hi = min(values), max(values)
    return lo // Q, -((-hi) // Q)


def scale(a, r):
    return mul(a, rat(r))


def root(a):
    assert a[0] >= 0
    lo, hi = isqrt(a[0] * Q), isqrt(a[1] * Q)
    return lo, hi + (hi * hi < a[1] * Q)


def p_add(a, b):
    return add(a[0], b[0]), add(a[1], b[1])


def p_scale(p, r):
    return scale(p[0], r), scale(p[1], r)


def p_mul(p, a):
    return mul(p[0], a), mul(p[1], a)


def p_neg(p):
    return neg(p[0]), neg(p[1])


def turn(p):
    return neg(p[1]), p[0]


def square_bounds(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2)
    return lo, max(a[0] ** 2, a[1] ** 2)


def distance_bounds(p, q):
    x, y = square_bounds(sub(p[0], q[0])), square_bounds(sub(p[1], q[1]))
    return x[0] + y[0], x[1] + y[1]


def packet(size, leaves, target):
    sqrt3, sqrt5 = root(rat(3)), root(rat(5))
    c72 = scale(sub(sqrt5, rat(1)), F(1, 4))
    s72 = scale(root(add(rat(10), scale(sqrt5, 2))), F(1, 4))
    s36 = scale(root(sub(rat(10), scale(sqrt5, 2))), F(1, 4))
    cap_height = add(s72, s36)
    t = F(1, 200 * size ** 3)
    cd, sd = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    v = (sub(rat(cd / 2), scale(sqrt3, sd / 2)),
         add(scale(sqrt3, cd / 2), rat(sd / 2)))
    s = F(1, 2000 * size ** 3) if target else F(0)
    cu, su = (1 - s * s) / (1 + s * s), -2 * s / (1 + s * s)
    assert cu * cu + su * su == cd * cd + sd * sd == 1
    u = rat(cu), rat(su)
    points, labels, contacts = [], {}, set()

    def insert(label, p):
        assert label not in labels
        labels[label] = len(points)
        points.append(p)
        return labels[label]

    def edge(a, b):
        contacts.add(tuple(sorted((a, b))))

    for i in range(size + 1):
        for j in range(size + 1):
            insert(('g', i, j), p_add(p_scale(u, i), p_scale(v, j)))
    for i in range(size + 1):
        for j in range(size + 1):
            a = labels['g', i, j]
            if i < size:
                edge(a, labels['g', i + 1, j])
            if j < size:
                edge(a, labels['g', i, j + 1])
    selections = range(8, size - 8, 8 if leaves else 6)
    caps = 0
    for side in range(4):
        for k in selections:
            if side == 0:
                a, b, w, normal = ('g', k, 0), ('g', k + 1, 0), u, p_neg(turn(u))
            elif side == 1:
                a, b, w, normal = ('g', k, size), ('g', k + 1, size), u, turn(u)
            elif side == 2:
                a, b, w, normal = ('g', 0, k), ('g', 0, k + 1), v, turn(v)
            else:
                a, b, w, normal = ('g', size, k), ('g', size, k + 1), v, p_neg(turn(v))
            pa, pb = points[labels[a]], points[labels[b]]
            pc = p_add(pb, p_add(p_mul(w, c72), p_mul(normal, s72)))
            pd = p_add(pa, p_add(p_scale(w, F(1, 2)), p_mul(normal, cap_height)))
            pe = p_add(pa, p_add(p_mul(w, neg(c72)), p_mul(normal, s72)))
            cap = [labels[a], labels[b], insert(('c', side, k), pc),
                   insert(('d', side, k), pd), insert(('e', side, k), pe)]
            for j in range(5):
                edge(cap[j], cap[(j + 1) % 5])
            if leaves:
                leaves_p = [p_add(pc, p_add(p_mul(w, s72), p_mul(normal, c72))),
                            p_add(pd, normal),
                            p_add(pe, p_add(p_mul(w, neg(s72)), p_mul(normal, c72))),
                            p_add(pd, p_add(p_scale(w, F(15, 17)), p_scale(normal, F(8, 17))))]
                leaf_ids = [insert(('n', side, k, j), p) for j, p in enumerate(leaves_p)]
                for j in range(3):
                    edge(cap[j + 2], leaf_ids[j])
                edge(cap[3], leaf_ids[3])
            caps += 1
    adjacency = [set() for _ in points]
    for a, b in contacts:
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert all(not (adjacency[a] & adjacency[b]) for a, b in contacts)
    return points, labels, contacts, caps


def main():
    # A quadratic coefficient certificate proves the actual corner diameter
    # for every M >= 24 and cosine in [49/100, 1/2], rather than sampling M.
    # Coordinates below are represented as a*M+b in the unit oblique basis.
    boxes = [(((0, F(0)), (1, F(0))), ((0, F(0)), (1, F(0)))),
             (((0, F(5)), (1, F(-5))), ((0, F(-7, 2)), (0, F(0)))),
             (((0, F(5)), (1, F(-5))), ((1, F(0)), (1, F(7, 2)))),
             (((0, F(-7, 2)), (0, F(0))), ((0, F(5)), (1, F(-5)))),
             (((1, F(0)), (1, F(7, 2))), ((0, F(5)), (1, F(-5))))]
    vertices = [(i, (x, y)) for i, (xs, ys) in enumerate(boxes)
                for x in xs for y in ys]
    polynomial_checks = 0
    for (box_a, pa), (box_b, pb) in combinations(vertices, 2):
        aa, bb = pa[0][0] - pb[0][0], pa[0][1] - pb[0][1]
        cc, dd = pa[1][0] - pb[1][0], pa[1][1] - pb[1][1]
        equal_corner_pair = box_a == box_b == 0 and abs(aa) == abs(cc) == 1 and aa == cc
        for cosine in (F(49, 100), F(1, 2)):
            c2 = aa * aa + cc * cc + 2 * cosine * aa * cc - 2 * (1 + cosine)
            c1 = 2 * aa * bb + 2 * cc * dd + 2 * cosine * (aa * dd + bb * cc)
            c0 = bb * bb + dd * dd + 2 * cosine * bb * dd
            # Substitute M = 24 + z. All three coefficients are affine
            # in cosine, so checking its endpoints certifies the interval.
            coefficients = c2, 48 * c2 + c1, 576 * c2 + 24 * c1 + c0
            if equal_corner_pair:
                assert coefficients == (0, 0, 0)
            else:
                assert coefficients[0] <= 0 and coefficients[1] <= 0 and coefficients[2] < 0
            polynomial_checks += 1
    results = []
    for size, leaves in ((24, False), (32, True)):
        old, labels, contacts, caps = packet(size, leaves, False)
        new, new_labels, new_contacts, new_caps = packet(size, leaves, True)
        assert labels == new_labels and contacts == new_contacts and caps == new_caps
        actual_pair = (labels['g', 0, 0], labels['g', size, size])
        dlo, dhi = distance_bounds(old[actual_pair[0]], old[actual_pair[1]])
        qsq = Q * Q
        pair_count, target_max_upper = 0, 0
        for i, j in combinations(range(len(old)), 2):
            olo, ohi = distance_bounds(old[i], old[j])
            nlo, nhi = distance_bounds(new[i], new[j])
            if (i, j) in contacts:
                assert olo <= qsq <= ohi and nlo <= qsq <= nhi
            else:
                assert olo > qsq and nlo > qsq, (size, leaves, i, j, 'lower')
            if (i, j) != actual_pair:
                assert ohi < dlo, (size, leaves, i, j, 'actual diameter')
            assert nhi < dlo, (size, leaves, i, j, 'target upper')
            target_max_upper = max(target_max_upper, nhi)
            pair_count += 1
        gap = F(dlo - target_max_upper, qsq)
        assert gap > F(1, 10 ** 7)
        results.append({'size': size, 'extra_leaves': leaves, 'points': len(old),
                        'pentagon_caps': caps, 'contacts_preserved': len(contacts),
                        'source_pair_checks': pair_count, 'target_pair_checks': pair_count,
                        'unique_actual_diameter_pair': actual_pair,
                        'certified_squared_diameter_decrease_lower_bound': '1/10000000'})
    print(json.dumps({'classification': 'feasible wall packet escape regression',
                      'box_polynomial_coefficient_certificates': polynomial_checks,
                      'box_certificate_scope': 'all real M>=24, cos(phi) in [49/100,1/2]',
                      'cases': results,
                      'omitted': ['canonical KKT and mixed rigidity',
                                  'global optimality of the old packet',
                                  'extension through an arbitrary retained source outside the packet']},
                     sort_keys=True))


if __name__ == '__main__':
    main()
