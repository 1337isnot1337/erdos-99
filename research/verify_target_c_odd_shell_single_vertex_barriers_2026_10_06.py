#!/usr/bin/env python3
"""Exact directed bounds for regular-shell one-vertex barriers.

Certifies three actual wall/collar packets, all source pairs, actual
diameters, and a smallest edge/singleton covering of all inward sites.
The interval arithmetic is self-contained. The deep filling and
whole-source lattice competitor use the analytic translation-average
packet theorem, not an uninspected image or solver.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, isqrt
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


def p_mul(p, a):
    return mul(p[0], a), mul(p[1], a)


def turn(p):
    return neg(p[1]), p[0]


def square_bounds(a):
    lo = 0 if a[0] <= 0 <= a[1] else min(a[0] ** 2, a[1] ** 2)
    return lo, max(a[0] ** 2, a[1] ** 2)


def distance_bounds(p, q):
    x = square_bounds(sub(p[0], q[0]))
    y = square_bounds(sub(p[1], q[1]))
    return x[0] + y[0], x[1] + y[1]


def inv(a):
    assert a[0] > 0
    return Q * Q // a[1], -((-Q * Q) // a[0])


def enclose(lo, hi):
    assert lo <= hi
    return rat(lo)[0], rat(hi)[1]


def atan_interval(x):
    assert 0 < x < 1
    value = sum((-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(40))
    return value, value + x ** 81 / 81


def trig_interval(lo, hi, sine):
    assert 0 < lo <= hi < F(1, 10)

    def bounds(x):
        shift = 1 if sine else 0
        value = sum((-1) ** j * x ** (2 * j + shift) / factorial(2 * j + shift)
                    for j in range(20))
        return value, value + x ** (40 + shift) / factorial(40 + shift)

    alo, ahi = bounds(lo)
    blo, bhi = bounds(hi)
    return enclose(alo, bhi) if sine else enclose(blo, ahi)


def fourier_identities(q):
    """Laurent identities modulo z^(2q)+1, where z=exp(i*pi/(2q))."""
    modulus = 2 * q

    def normalize(terms):
        result = {}
        for exponent, coefficient in terms:
            quotient, remainder = divmod(exponent, modulus)
            value = coefficient * (-1 if quotient % 2 else 1)
            result[remainder] = result.get(remainder, F(0)) + value
        return {i: a for i, a in result.items() if a}

    def monomial(exponent):
        return normalize([(exponent, F(1))])

    def plus(a, b):
        return normalize(list(a.items()) + list(b.items()))

    def times(a, b):
        return normalize([(i + j, c * d) for i, c in a.items() for j, d in b.items()])

    def scaled(a, t):
        return {i: c * t for i, c in a.items() if c * t}

    def minus(a, b):
        return plus(a, scaled(b, -1))

    def sine(n):
        return times(scaled(monomial(q), F(-1, 2)), minus(monomial(n), monomial(-n)))

    def cosine(n):
        return scaled(plus(monomial(n), monomial(-n)), F(1, 2))

    def sq(a):
        return times(a, a)

    k = (q - 1) // 2
    s1, c1 = sine(1), cosine(1)
    checks = 0
    for l in range(1, q):
        numerator = minus(sq(sine(2 * l)), scaled(times(sq(s1), sq(sine(2 * k * l))), 4))
        determinant = minus(times(times(sine(2), cosine(2 * l)),
                                  times(cosine(2 * k), sine(2 * k * l))),
                            times(times(sine(2 * k), cosine(2 * k * l)),
                                  times(cosine(2), sine(2 * l))))
        if l % 2 == 0:
            factor = minus(sq(cosine(l)), sq(s1))
            expected_numerator = scaled(times(sq(sine(l)), factor), 4)
            expected_determinant = scaled(times(times(c1, sine(l)), factor),
                                           2 * (-1) ** (l // 2 + 1))
        else:
            factor = minus(sq(sine(l)), sq(s1))
            expected_numerator = scaled(times(sq(cosine(l)), factor), 4)
            expected_determinant = scaled(times(times(c1, cosine(l)), factor),
                                           2 * (-1) ** ((l - 1) // 2 + 1))
        assert numerator == expected_numerator
        assert determinant == expected_determinant
        if l in (1, q - 1):
            assert not numerator and not determinant
        checks += 2
    return checks


def main():
    fourier_checks = sum(fourier_identities(q) for q in (5, 7, 9, 11, 19, 65, 101, 201))
    a, b = atan_interval(F(1, 5)), atan_interval(F(1, 239))
    pi_lo, pi_hi = 16 * a[0] - 4 * b[1], 16 * a[1] - 4 * b[0]
    assert F(3) < pi_lo < pi_hi < F(22, 7)
    pi_interval = enclose(pi_lo, pi_hi)
    a0 = scale(root(rat(3)), F(1, 2))
    cases = []
    for q in (65, 101, 201):
        sa = trig_interval(pi_lo / q, pi_hi / q, True)
        ca = trig_interval(pi_lo / q, pi_hi / q, False)
        s2 = trig_interval(2 * pi_lo / q, 2 * pi_hi / q, True)
        c2 = trig_interval(2 * pi_lo / q, 2 * pi_hi / q, False)
        cha = trig_interval(pi_lo / (2 * q), pi_hi / (2 * q), False)
        radius = inv(scale(sa, 2))
        assert radius[0] > 10 * Q
        epsilon = scale(inv(radius), 2)
        delta = scale(inv(mul(radius, radius)), F(1, 100))
        inner_radius = sub(radius, epsilon)
        pair_height = root(sub(mul(add(rat(1), delta), add(rat(1), delta)), rat(F(1, 4))))
        pair_radius = sub(mul(radius, ca), pair_height)
        singleton_radius = sub(radius, add(rat(1), delta))
        directions = [(rat(1), rat(0))]
        for _ in range(q - 1):
            x, y = directions[-1]
            directions.append((sub(mul(c2, x), mul(s2, y)), add(mul(s2, x), mul(c2, y))))
        wall = [p_mul(n, radius) for n in directions]
        proposals = [p_mul(n, inner_radius) for n in directions]
        blockers, expected = [], []
        for j in range(0, q - 1, 2):
            mid_direction = p_add(p_mul(directions[j], ca), p_mul(turn(directions[j]), sa))
            blockers.append(p_mul(mid_direction, pair_radius))
            expected.append({j, j + 1})
        blockers.append(p_mul(directions[-1], singleton_radius))
        expected.append({q - 1})
        contacts = {tuple(sorted((j, (j + 1) % q))) for j in range(q)}
        k = (q - 1) // 2
        diameter_pairs = {tuple(sorted((j, (j + k) % q))) for j in range(q)}
        actual_diameter = scale(mul(radius, cha), 2)
        diameter_squared = mul(actual_diameter, actual_diameter)
        source = wall + blockers
        pair_checks = 0
        for i, j in combinations(range(len(source)), 2):
            lo, hi = distance_bounds(source[i], source[j])
            if (i, j) in contacts:
                assert lo <= Q * Q <= hi
            else:
                assert lo > Q * Q, (q, i, j, 'source lower')
            if (i, j) in diameter_pairs:
                assert lo <= diameter_squared[1] * Q and hi >= diameter_squared[0] * Q
            else:
                assert hi < diameter_squared[0] * Q, (q, i, j, 'inactive upper')
            pair_checks += 1
        all_roots = set()
        blocker_checks = 0
        for z, wanted in zip(blockers, expected):
            actual = set()
            for j, x in enumerate(proposals):
                lo, hi = distance_bounds(z, x)
                if hi <= Q * Q:
                    actual.add(j)
                else:
                    assert lo > Q * Q, (q, j, 'undecided blocker')
                blocker_checks += 1
            assert actual == wanted
            all_roots.update(actual)
        assert all_roots == set(range(q))
        assert len(blockers) == (q + 1) // 2
        # A deep spacing-(1+q^-2) lattice can be translated to provide this
        # many strict interior sites. Its separation from the collar is >1.
        deep_radius = sub(radius, rat(3))
        assert pair_radius[0] > deep_radius[1] + Q
        assert singleton_radius[0] > deep_radius[1] + Q
        assert deep_radius[1] < mul(radius, ca)[0]
        lattice_spacing = F(1) + F(1, q * q)
        deep_cell = scale(a0, lattice_spacing * lattice_spacing)
        deep_mean = mul(mul(pi_interval, mul(deep_radius, deep_radius)), inv(deep_cell))
        deep_count = deep_mean[0] // Q
        assert deep_count == deep_mean[1] // Q
        count = q + len(blockers) + deep_count
        disk_mean = mul(scale(mul(pi_interval, diameter_squared), F(1, 4)), inv(a0))
        assert disk_mean[0] > (count + 1) * Q
        cases.append({'q': q, 'wall_and_collar_points': len(source),
                      'source_pair_checks': pair_checks, 'blocker_checks': blocker_checks,
                      'blocked_inward_sites': len(all_roots), 'collar_isolates': len(blockers),
                      'deep_isolates_from_translation_average': deep_count,
                      'full_constructed_cardinality': count,
                      'strict_independent_disk_packet_capacity': True})
    print(json.dumps({'classification': 'source barrier and nonglobal filling certificates',
                      'exact_fourier_factor_identities': fourier_checks,
                      'pi_bounds': 'exact Machin alternating series', 'cases': cases,
                      'omitted': ['global optimality', 'maximal protected filling capacity',
                                  'collective clearing of every canonical container']}, sort_keys=True))


if __name__ == '__main__':
    main()
