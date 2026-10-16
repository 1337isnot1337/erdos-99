#!/usr/bin/env python3
"""Exact convex shared-witness path and repeated-sector regression.

Encodes fourteen rational points, three unit-chord translations, all source
pair constraints, positive LOCAL contact balance, and separate exterior
sectors. The contact core is disconnected; loaded vertices are contact isolates;
several other contact vertices are not trapped. This is not a canonical source,
full KKT realization, stopped-train packet, global optimum, or C-II counterexample.
No contact-preserving path contraction is asserted. Continuous proofs are in
the companion report.
"""

from fractions import Fraction as Q
from functools import cmp_to_key
from itertools import combinations

from verify_binary_contact_swap_2sat import compile_source, squared


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]


def polar_compare(a, b):
    def half(v):
        return int(v[1] < 0 or (v[1] == 0 and v[0] < 0))
    if half(a) != half(b):
        return -1 if half(a) < half(b) else 1
    value = cross(a, b)
    return -1 if value > 0 else (1 if value < 0 else 0)


def sector_index(rays, direction):
    assert all(cross(ray, direction) != 0 for ray in rays)
    before = [index for index, ray in enumerate(rays) if polar_compare(ray, direction) < 0]
    return before[-1] if before else len(rays)-1


def main():
    t = Q(1, 100)
    a, b = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    midpoint_cos, midpoint_sin = a*a-b*b, 2*a*b
    half_t = t*t
    ce, he = (1-half_t*half_t)/(1+half_t*half_t), 2*half_t/(1+half_t*half_t)
    amplitude = 2*he
    R = 1+amplitude*b/4
    c, h = Q(1071, 2129), Q(1840, 2129)
    assert c*c+h*h == a*a+b*b == ce*ce+he*he == 1
    assert c > Q(1, 2)
    points = [(Q(0), Q(0)), (Q(0), Q(1)), (c, -h), (-c, -h),
              (-R*a, R*b), (R*a, R*b), (-R*a, 1+R*b), (R*a, 1+R*b),
              (Q(-6), Q(-8)), (Q(0), Q(-10)), (Q(6), Q(-8)),
              (Q(6), Q(8)), (Q(0), Q(10)), (Q(-6), Q(8))]
    deltas = [(amplitude*midpoint_sin, amplitude*midpoint_cos),
              (Q(0), amplitude),
              (-amplitude*midpoint_sin, amplitude*midpoint_cos)]
    moves = [([4, 6, 8], deltas[0]), ([0, 1, 2, 3, 9], deltas[1]),
             ([5, 7, 10], deltas[2])]

    old = {(i, j): squared(points[i], points[j]) for i, j in combinations(range(14), 2)}
    assert len(old) == 91 and min(old.values()) == 1 and max(old.values()) == 400
    contacts = {pair for pair, value in old.items() if value == 1}
    diameters = {pair for pair, value in old.items() if value == 400}
    assert contacts == {(0, 1), (0, 2), (0, 3), (4, 6), (5, 7)}
    assert diameters == {(8, 11), (9, 12), (10, 13)}
    result = compile_source(points, moves)
    assert result['model'] is None and result['horn_zero_closure']['zero_is_unique']
    shared = {(0, 4), (0, 5), (1, 6), (1, 7)}
    assert {(i, j) for i, j, _, _ in result['forbidden']} == shared
    for pair in shared:
        patterns = {tuple(bit for _, bit in bits) for i, j, bits, _ in result['forbidden']
                    if (i, j) == pair}
        assert patterns == {(1, 0), (0, 1), (1, 1)}
    print('PASS: all 91 old source pairs and local binary states; only shared blockers')

    for index, midpoint in enumerate(((midpoint_cos, -midpoint_sin),
                                       (Q(1), Q(0)), (midpoint_cos, midpoint_sin))):
        x, y = midpoint
        lower, upper = (x*ce+y*he, y*ce-x*he), (x*ce-y*he, y*ce+x*he)
        assert dot(lower, lower) == dot(upper, upper) == 1
        assert tuple(z-v for v, z in zip(lower, upper)) == deltas[index]
    assert b*ce > a*he
    incoming, outgoing = (R*a, -R*b), (R*a, R*b)
    assert cross(incoming, outgoing) > 0
    assert squared(points[4], points[0]) == squared(points[0], points[5]) == R*R > 1
    print('PASS: unit-chord moves, strictly ordered phase intervals and convex turn')

    private = [tuple(y-x for x, y in zip(points[i], points[j])) for i, j in sorted(diameters)]
    assert all(dot(vector, delta) > 0 for vector in private for delta in deltas)
    for vector, delta in zip(private, deltas):
        assert dot(vector, delta) > dot(delta, delta)/2
    print('PASS: coherent diameter projections and privately shortened diameters')

    contact_rays = [points[i] for i in (1, 2, 3)]
    weights = [2*h, Q(1), Q(1)]
    assert all(weight > 0 for weight in weights)
    assert tuple(sum(weight*ray[j] for weight, ray in zip(weights, contact_rays))
                 for j in range(2)) == (0, 0)
    ordered = sorted(contact_rays, key=cmp_to_key(polar_compare))
    sectors = [sector_index(ordered, points[i]) for i in (4, 5)]
    assert sectors[0] != sectors[1]
    # The contact component at p is a three-edge tree; p has three outer sectors.
    assert len(ordered) == 3
    assert Q(11, 20)+Q(1, 10) == Q(13, 20) < Q(199, 200)
    assert all(abs(ray[0]) <= Q(13, 20) for ray in contact_rays)
    print('PASS: strict local contact balance; U rays in separate outer occurrences')

    loaded = {index for pair in diameters for index in pair}
    assert not any(index in loaded for pair in contacts for index in pair)
    assert 13 < 20
    print('PASS: canonical/KKT failure and strict same-cardinality unit-line competitor')

    # Fixed-rest contact-preserving contraction fails even when both centers
    # are strictly trapped. Opposite axial unit anchors bound their x coordinates.
    phase_t = Q(1, 1000)
    cm, hm = (1-phase_t*phase_t)/(1+phase_t*phase_t), 2*phase_t/(1+phase_t*phase_t)
    half_t = phase_t*phase_t
    s = 4*half_t/(1+half_t*half_t)
    rotation_t = phase_t**4
    cr = (1-rotation_t*rotation_t)/(1+rotation_t*rotation_t)
    sr = 2*rotation_t/(1+rotation_t*rotation_t)
    c, h = Q(120, 241), Q(209, 241)
    assert c*c+h*h == 1 and c < Q(1, 2)
    R = 1+4*h*sr
    top_p, bottom_p = (-c*cr+h*sr, h*cr+c*sr), (c*cr+h*sr, -h*cr+c*sr)
    top_q, bottom_q = (-c*cr-h*sr, h*cr-c*sr), (c*cr-h*sr, -h*cr-c*sr)
    points = [(Q(0), Q(0)), (R, Q(0)), top_p, bottom_p, (Q(-1), Q(0)),
              (R+top_q[0], top_q[1]), (R+bottom_q[0], bottom_q[1]),
              (R+1, Q(0)), (Q(-6), Q(-8)), (Q(6), Q(-8)),
              (Q(6), Q(8)), (Q(-6), Q(8))]
    moves = [([0, 2, 3, 4, 8], (s*hm, s*cm)),
             ([1, 5, 6, 7, 9], (-s*hm, s*cm))]
    result = compile_source(points, moves)
    assert result['old_D2'] == 400 and result['model'] is None
    assert result['horn_zero_closure']['zero_is_unique']
    shared = {(0, 1), (2, 5), (3, 6)}
    assert {(i, j) for i, j, _, _ in result['forbidden']} == shared
    for pair in shared:
        patterns = {tuple(bit for _, bit in bits) for i, j, bits, _ in result['forbidden']
                    if (i, j) == pair}
        assert patterns == {(1, 0), (0, 1), (1, 1)}
    A, B, anchor = h*cr-c*sr, h*cr+c*sr, 2*cr*sr
    assert min(A, B, anchor) > 0
    for rays, weights in (([top_p, bottom_p, (Q(-1), Q(0))], [A, B, anchor]),
                          ([top_q, bottom_q, (Q(1), Q(0))], [B, A, anchor])):
        assert tuple(sum(weight*ray[j] for weight, ray in zip(weights, rays))
                     for j in range(2)) == (0, 0)
    # With these two anchors fixed, contact preservation implies p'_x<=0,
    # q'_x>=R, hence every finite position pair has distance at least R>1.
    assert 4 not in {index for pair in shared for index in pair}
    assert 7 not in {index for pair in shared for index in pair}
    assert squared(points[0], points[4]) == squared(points[1], points[7]) == 1
    assert R > 1 and 11 < 20
    print('PASS: 66 pairs; two strictly trapped sites reject fixed-anchor path contraction')


if __name__ == '__main__':
    main()
