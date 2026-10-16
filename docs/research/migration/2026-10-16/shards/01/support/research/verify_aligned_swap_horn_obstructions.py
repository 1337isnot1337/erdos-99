#!/usr/bin/env python3
"""Exact regressions for aligned swaps and the axial-bracket lemma.

Encodes rational points, disjoint finite translations, and the local lower
distance truth table. It checks the repaired bracket estimate by exact constant
arithmetic and enumerates rational fixtures. It does not encode global
optimality, source KKT, train extraction, or canonicality. The proof, rather than
the finite samples, establishes the bracket lemma for real coordinates.
"""

from fractions import Fraction as Q
from itertools import product

from verify_binary_contact_swap_2sat import compile_source, squared


def local_distances(r, first, second):
    return {(i, j): sum((x + j * b - i * a) ** 2
                       for x, a, b in zip(r, first, second))
            for i, j in product((0, 1), repeat=2)}


def joint_only_fixture(t):
    # Both vectors are exact differences of unit directions, with one common
    # midpoint phase and coherent orientation. No source train cut is inferred.
    first_unit = ((1 - t*t) / (1 + t*t), 2*t / (1 + t*t))
    second_t = 2*t
    second_unit = ((1 - second_t*second_t) / (1 + second_t*second_t),
                   2*second_t / (1 + second_t*second_t))
    assert sum(x*x for x in first_unit) == sum(x*x for x in second_unit) == 1
    first = (Q(0), 2*first_unit[1])
    second = (Q(0), 2*second_unit[1])
    gap = second[1] - first[1]
    assert 0 < gap < first[1]
    r = (1 - gap*gap/4, -gap)
    values = local_distances(r, first, second)
    assert all(values[bits] > 1 for bits in ((0, 0), (1, 0), (0, 1)))
    assert values[1, 1] < 1
    points = [(Q(0), Q(0)), r, (Q(-10), Q(0)), (Q(10), Q(0))]
    result = compile_source(points, [([0], first), ([1], second)])
    assert result['horn_zero_closure']['incompatible_pairs'] == [(0, 1)]
    assert result['horn_zero_closure']['least_nonzero_models'] == {0: (1, 0), 1: (0, 1)}
    # No old diameter is changed in this regression, so it is not a competitor
    # packet for a canonical source. It tests a universal pair-compatibility claim.
    assert result['model'] is None
    return values


def two_hit_fixture(t):
    # Midpoint phases straddle zero; the two boundary phase intervals are
    # strictly separated. A single almost-unit axial pair blocks BOTH swaps.
    c, h = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    half_t = t*t
    ce, he = (1-half_t*half_t)/(1+half_t*half_t), 2*half_t/(1+half_t*half_t)
    assert h*ce > c*he
    s = 2*he
    first, second = (s*h, s*c), (-s*h, s*c)
    # The four actual unit directions giving these chord differences.
    for midpoint in ((c, -h), (c, h)):
        a, b = midpoint
        lower, upper = (a*ce+b*he, b*ce-a*he), (a*ce-b*he, b*ce+a*he)
        assert sum(x*x for x in lower) == sum(x*x for x in upper) == 1
        assert tuple(y-x for x, y in zip(lower, upper)) == (-2*he*b, 2*he*a)
    r = (1+s*h/4, Q(0))
    values = local_distances(r, first, second)
    assert values[0, 0] > 1
    assert all(values[bits] < 1 for bits in ((1, 0), (0, 1), (1, 1)))
    # Positive slack has the cubic t scale rather than the quadratic chord scale.
    assert r[0]-1 == s*h/4
    result = compile_source([(Q(0), Q(0)), r, (Q(-10), Q(0)), (Q(10), Q(0))],
                            [([0], first), ([1], second)])
    assert result['horn_zero_closure']['zero_is_unique']
    # Strengthening: give each variable a private actual diameter and retain a
    # fixed old unit contact. The same one inactive pair still blocks every
    # nonzero assignment. This source violates canonical trapping/KKT and has
    # the explicit eight-point unit-line competitor of diameter seven.
    points = [(Q(0), Q(0)), r, (Q(-6), Q(-8)), (Q(6), Q(-8)),
              (Q(6), Q(8)), (Q(-6), Q(8)), (Q(0), Q(3)), (Q(1), Q(3))]
    moves = [([0, 2], first), ([1, 3], second)]
    result = compile_source(points, moves)
    assert result['old_D2'] == 400
    assert result['model'] is None
    assert result['horn_zero_closure']['zero_is_unique']
    assert {(i, j) for i, j, _, _ in result['forbidden']} == {(0, 1)}
    assert squared(points[2], points[4]) == squared(points[3], points[5]) == 400
    for point, other, delta in ((points[2], points[4], first),
                                (points[3], points[5], second)):
        assert squared(tuple(x+y for x, y in zip(point, delta)), other) < 400
    return values


def main():
    for denominator in (100, 1000, 10000, 1000000):
        joint_only_fixture(Q(1, denominator))
    print('PASS: four arbitrarily small exact unit-chord joint-only regressions')
    for denominator in (100, 1000, 10000):
        two_hit_fixture(Q(1, denominator))
    print('PASS: disjoint intervals allow cubic-slack blockers, including private diameters')

    # A tempting slack estimate a <= 2 Delta_i.dot(Delta_j) is FALSE even
    # for parallel moves. The correct proof bounds transverse projection using
    # f11-f10 and f11-f01, without assuming this slack estimate.
    r = (1 - Q(1, 20000000), -Q(124, 1250))
    first, second = (Q(0), Q(1, 1000)), (Q(0), Q(1, 10))
    values = local_distances(r, first, second)
    assert all(values[bits] > 1 for bits in ((0, 0), (1, 0), (0, 1)))
    assert values[1, 1] < 1
    assert values[0, 0] - 1 > 2 * first[1] * second[1]
    print('PASS: false quadratic-slack estimate has an exact counterexample')

    # Rational constants in the continuous axial-bracket proof: |r| <= 6/5,
    # |r.dot(w)| < 11/50, so |r.dot(u)| > 19/20. A unit neighbor within
    # 1/10 of the appropriate signed u then lies less than one from q.
    assert 1 - Q(11, 50)**2 > Q(19, 20)**2
    neighbor_projection = Q(19, 20) - Q(6, 5)*Q(1, 10)
    assert neighbor_projection == Q(83, 100)
    assert Q(6, 5)**2 + 1 - 2*neighbor_projection == Q(39, 50) < 1
    print('PASS: axial-bracket contradiction constants are exact')
    assert Q(1, 10)+(1+Q(1, 10))*Q(2, 10) == Q(8, 25) < 1
    print('PASS: axial near-unit linear-forest neighbor exclusion constant')

    # Independent finite stress test: both horizontal unit neighbors are kept
    # in the source. All unit-separated near-unit q and positive vertical swap
    # amplitudes in this rational sample avoid a joint-only obstruction and
    # avoid simultaneous individual lower obstructions, as the lemma predicts.
    checked = 0
    p, minus, plus = (Q(0), Q(0)), (Q(-1), Q(0)), (Q(1), Q(0))
    for numerator_x, numerator_y in product(range(-30, 31), range(-30, 31)):
        q = (Q(numerator_x, 25), Q(numerator_y, 25))
        if not 1 < squared(p, q) <= Q(36, 25):
            continue
        if squared(minus, q) < 1 or squared(plus, q) < 1:
            continue
        for a, b in product((Q(1, 100), Q(1, 20), Q(1, 10)), repeat=2):
            values = local_distances(q, (Q(0), a), (Q(0), b))
            bad = {bits for bits, value in values.items() if value <= 1}
            assert bad != {(1, 1)}
            assert not {(1, 0), (0, 1)} <= bad
            checked += 1
    print(f'PASS: {checked} exact bracketed pair/move samples')

    # A genuine diameter-shortening, coherently oriented source family: each
    # least positive model found by Horn propagation shortens its private old
    # diameter. No global/KKT hypothesis is asserted for these three isolates.
    points = [(Q(-1), Q(0)), (Q(1), Q(0)), (Q(0), Q(10))]
    result = compile_source(points, [([0], (Q(0), Q(1, 20))),
                                     ([1], (Q(0), Q(1, 25)))])
    assert result['model'] is not None
    assert result['horn_zero_closure']['least_nonzero_models'] == {0: (1, 0), 1: (0, 1)}
    print('PASS: coherent unequal-amplitude source moves have exact finite escapes')

    # Pointwise upward bracketed implications do NOT give a layer potential.
    # Layer 0 owns the lowest and highest contact rows; layer 1 owns the two
    # middle rows. Both directed implications exist at different source sites.
    # Two remote diameter pairs give every individual move a strictly shortened
    # old diameter. The all-one union is an exact strict competitor, so this is
    # deliberately not a canonical source or a global-optimality regression.
    levels = [Q(0), Q(101, 100), Q(3), Q(401, 100)]
    points = [(Q(x), y) for y in levels for x in (-1, 0, 1)]
    points += [(Q(-6), Q(-8)), (Q(6), Q(-8)),
               (Q(6), Q(8)), (Q(-6), Q(8))]
    moves = [([0, 1, 2, 9, 10, 11, 12], (Q(0), Q(1, 20))),
             ([3, 4, 5, 6, 7, 8, 13], (Q(0), Q(1, 20)))]
    result = compile_source(points, moves)
    assert result['old_D2'] == 400
    assert result['model'] == (1, 1)
    assert result['new_D2'] == Q(159361, 400) < 400
    assert result['horn_zero_closure']['implications'] == [[1], [0]]
    assert result['horn_zero_closure']['incompatible_pairs'] == []
    assert result['horn_zero_closure']['forced_zero'] == []
    assert squared(points[1], points[4]) == squared(points[7], points[10]) == Q(10201, 10000)
    assert points[4][1]-points[1][1] > Q(1, 2)
    assert points[10][1]-points[7][1] > Q(1, 2)
    print('PASS: bracketed upward source implications form a layer cycle; union escapes')


if __name__ == '__main__':
    main()
