#!/usr/bin/env python3
"""Exact heptagon-plus-center geometry for the collective-wall regression.

The D(8) global-optimality fact comes from the inspected Bezdek--Fodor
Theorem 1.1, not from this computation. The script certifies the finite
source geometry, core matrices and eligible deletion sets. The universal
exterior shield and safe-region capacity bound are analytic.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
import json

Q = 10 ** 24


def rat(x):
    x = F(x)
    a = x.numerator * Q
    return a // x.denominator, -((-a) // x.denominator)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def imul(a, b):
    values = [x * y for x in a for y in b]
    lo, hi = min(values), max(values)
    return lo // Q, -((-hi) // Q)


def iscale(a, c):
    return imul(a, rat(c))


def atan_interval(x):
    assert 0 < x < 1
    value = sum((-1) ** j * x ** (2 * j + 1) / (2 * j + 1)
                for j in range(40))
    return value, value + x ** 81 / 81


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def p_add(a, b):
    return trim([(a[j] if j < len(a) else F(0)) +
                 (b[j] if j < len(b) else F(0))
                 for j in range(max(len(a), len(b)))])


def p_scale(a, b):
    return trim([c * b for c in a])


def p_mul(a, b):
    if not a or not b:
        return []
    result = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return trim(result)


def p_divmod(a, b):
    a, b = trim(a), trim(b)
    assert b
    result = [F(0)] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        j, c = len(a) - len(b), a[-1] / b[-1]
        result[j] = c
        a = p_add(a, [F(0)] * j + p_scale(b, -c))
    return trim(result), a


class Field:
    def __init__(self, order, modulus):
        self.order, self.modulus = order, [F(c) for c in modulus]
        self.degree = len(modulus) - 1
        self.zero, self.one = self.element([]), self.element([1])
        self.z = self.element([0, 1])
        self.powers = [self.one]
        for _ in range(order - 1):
            self.powers.append(self.mul(self.powers[-1], self.z))
        assert self.mul(self.powers[-1], self.z) == self.one
        lo, hi = atan_interval(F(1, 5)), atan_interval(F(1, 239))
        pi = (16 * lo[0] - 4 * hi[1], 16 * lo[1] - 4 * hi[0])
        self.cosines = []
        for j in range(order):
            j = min(j, order - j)
            x = (rat(2 * j * pi[0] / order)[0],
                 rat(2 * j * pi[1] / order)[1])
            value, power = rat(0), rat(1)
            square = imul(x, x)
            for k in range(20):
                value = iadd(value, iscale(power, F((-1) ** k, factorial(2 * k))))
                power = imul(power, square)
            error = F(x[1], Q) ** 40 / factorial(40)
            self.cosines.append(iadd(value, (rat(-error)[0], rat(error)[1])))

    def element(self, a):
        a = p_divmod([F(c) for c in a], self.modulus)[1]
        return tuple(a + [F(0)] * (self.degree - len(a)))

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def scale(self, a, b):
        return tuple(x * b for x in a)

    def mul(self, a, b):
        return self.element(p_mul(a, b))

    def inv(self, a):
        assert a != self.zero
        r0, r1, s0, s1 = self.modulus, trim(a), [], [F(1)]
        while r1:
            quotient, remainder = p_divmod(r0, r1)
            r0, r1 = r1, remainder
            s0, s1 = s1, p_add(s0, p_scale(p_mul(quotient, s1), -1))
        assert len(r0) == 1
        return self.element(p_scale(s0, 1 / r0[0]))

    def conj(self, a):
        result = self.zero
        for j, c in enumerate(a):
            result = self.add(result, self.scale(self.powers[(-j) % self.order], c))
        return result

    def norm(self, a):
        return self.mul(a, self.conj(a))

    def real(self, a):
        return self.scale(self.add(a, self.conj(a)), F(1, 2))

    def real_bounds(self, a):
        assert self.conj(a) == a
        result = rat(0)
        for c, v in zip(a, self.cosines):
            result = iadd(result, iscale(v, c))
        return result

    def positive(self, a):
        result = self.real_bounds(a)
        assert result[0] > 0, result
        return result

    def sign(self, a):
        if a == self.zero:
            return 0
        result = self.real_bounds(a)
        assert result[0] > 0 or result[1] < 0, result
        return 1 if result[0] > 0 else -1

    def rank(self, matrix):
        matrix = [list(row) for row in matrix]
        pivot = 0
        for j in range(len(matrix[0])):
            k = next((k for k in range(pivot, len(matrix))
                      if matrix[k][j] != self.zero), None)
            if k is None:
                continue
            matrix[pivot], matrix[k] = matrix[k], matrix[pivot]
            inv = self.inv(matrix[pivot][j])
            matrix[pivot] = [self.mul(c, inv) for c in matrix[pivot]]
            for k in range(pivot + 1, len(matrix)):
                c = matrix[k][j]
                if c != self.zero:
                    matrix[k] = [self.sub(x, self.mul(c, y))
                                 for x, y in zip(matrix[k], matrix[pivot])]
            pivot += 1
            if pivot == len(matrix):
                break
        return pivot


def packet(order):
    f = Field(order, [1] * 7 if order == 7 else [1, -1, 1])
    points = [f.zero]
    for e in f.powers[:-1]:
        points.append(f.add(points[-1], e))
    center = f.inv(f.sub(f.one, f.z))
    contacts = {tuple(sorted((j, (j + 1) % order))) for j in range(order)}
    step = (order - 1) // 2 if order % 2 else order // 2
    diameters = {tuple(sorted((j, (j + step) % order))) for j in range(order)}
    diameter = f.norm(f.sub(points[step], points[0]))
    alpha, beta = f.scale(diameter, F(1, order)), F(1, len(diameters))
    f.positive(alpha)
    assert len(diameters) * beta == 1
    omega = [[f.zero] * order for _ in range(order)]
    rows = []
    for bank, weight in ((contacts, alpha),
                         (diameters, f.element([-beta]))):
        for i, j in sorted(bank):
            omega[i][i] = f.add(omega[i][i], weight)
            omega[j][j] = f.add(omega[j][j], weight)
            omega[i][j] = f.sub(omega[i][j], weight)
            omega[j][i] = f.sub(omega[j][i], weight)
            r = f.sub(points[i], points[j])
            x, iy = f.real(r), f.scale(f.sub(r, f.conj(r)), F(1, 2))
            row = [f.zero] * (2 * order)
            row[2 * i], row[2 * i + 1] = x, iy
            row[2 * j], row[2 * j + 1] = f.scale(x, -1), f.scale(iy, -1)
            rows.append(row)
    for p in ([f.one] * order, points, [f.conj(p) for p in points]):
        assert all(sum_field(f, [f.mul(x, y) for x, y in zip(row, p)]) == f.zero
                   for row in omega)
    schur, pivots = [list(row) for row in omega], 0
    for j in range(order):
        a = schur[j][j]
        if a == f.zero:
            assert all(schur[j][k] == f.zero for k in range(j, order))
            continue
        f.positive(a)
        pivots += 1
        inv = f.inv(a)
        for k in range(j + 1, order):
            for l in range(j + 1, order):
                schur[k][l] = f.sub(schur[k][l],
                    f.mul(inv, f.mul(schur[k][j], schur[j][l])))
    assert pivots == f.rank(omega)
    return f, points, center, contacts, diameters, diameter, pivots, f.rank(rows)


def sum_field(f, values):
    result = f.zero
    for a in values:
        result = f.add(result, a)
    return result


def main():
    f, wall, center, contacts, diameters, diameter, stress_rank, mixed_rank = packet(7)
    assert (stress_rank, mixed_rank) == (4, 11)
    radius_squared = f.norm(center)
    f.positive(f.sub(radius_squared, f.one))
    f.positive(f.sub(f.element([F(49, 36)]), radius_squared))
    source = wall + [center]
    pair_checks = 0
    for i, j in combinations(range(8), 2):
        d = f.norm(f.sub(source[i], source[j]))
        assert d == f.one if (i, j) in contacts else f.positive(f.sub(d, f.one))
        assert d == diameter if (i, j) in diameters else f.positive(f.sub(diameter, d))
        pair_checks += 1
    independent, sparse = [], []
    for state in product(range(2), repeat=7):
        selected = {j for j, bit in enumerate(state) if bit}
        if not selected:
            continue
        if all((j + 1) % 7 not in selected for j in selected):
            independent.append(state)
            remaining = [j for j in range(7) if j not in selected]
            assert max((remaining[(k + 1) % len(remaining)] - j) % 7
                       for k, j in enumerate(remaining)) <= 2
        if all(f.sign(f.sub(f.norm(f.sub(wall[i], wall[j])), f.element([4]))) >= 0
               for i, j in combinations(selected, 2)):
            sparse.append(state)
    assert (len(independent), len(sparse)) == (28, 14)
    print(json.dumps({
        'classification': 'exact D(8) source geometry and collective-wall capacity regression',
        'heptagon_full_source_pair_checks': pair_checks,
        'contacts': len(contacts), 'actual_diameters': len(diameters),
        'contact_isolates_retained': 1,
        'positive_normalized_stress': True,
        'core_psd_rank': stress_rank, 'core_mixed_rank': mixed_rank,
        'independent_deleted_wall_sets': len(independent),
        'deleted_wall_sets_with_pairwise_distance_at_least_two': len(sparse),
        'eligible_collective_deletion_sets': len(sparse),
        'safe_region_radius_bound': 'R-1/R < 13/42 < 1/2',
        'radius_certificate': '1 < R < 7/6; R-1/R < 13/42 < 1/2',
        'global_optimality_source': 'Bezdek--Fodor (1999), Theorem 1.1, printed p.106',
        'omitted': ['computational proof of global optimality',
                    'common-angle Boolean and hexagon claims',
                    'large-wall capacity gain', 'unbounded global family',
                    'Target C-II or Level I closure']
    }, sort_keys=True))


if __name__ == '__main__':
    main()
