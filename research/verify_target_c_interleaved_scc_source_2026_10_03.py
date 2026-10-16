#!/usr/bin/env python3
"""Exact source-geometry regression for the open-cell interleaved SCC route.

Assumes Euclidean layer cuts and assigned positive diameter weights, not actual
contact-train co-embedding or vertex KKT equilibrium. Checks every source pair,
all actual diameters, chord intersections, open-cell signs, SCCs, exact positive
cut resultants, divergence, phase-width bounds, and cut derivative rank.
Arithmetic is in Q(sqrt(6),sqrt(21)); signs use rational isolating intervals.
Does not prove global optimality, a complete contact shore, C-II, or Level I.
The report supplies the analytic homothetic family and its no-go scope.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import isqrt


class A:
    """Four exact coefficients in basis 1,sqrt(6),sqrt(21),sqrt(126)."""

    def __init__(self, value=0):
        self.c = value.c if isinstance(value, A) else (
            tuple(F(x) for x in value) if isinstance(value, tuple)
            else (F(value), F(0), F(0), F(0)))

    def __add__(self, other):
        other = A(other)
        return A(tuple(x + y for x, y in zip(self.c, other.c)))

    __radd__ = __add__

    def __neg__(self):
        return A(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + -A(other)

    def __rsub__(self, other):
        return A(other) + -self

    def __mul__(self, other):
        other = A(other)
        result = [F(0)] * 4
        for i in range(4):
            for j in range(4):
                factor = (6 if i & j & 1 else 1) * (21 if i & j & 2 else 1)
                result[i ^ j] += self.c[i] * other.c[j] * factor
        return A(tuple(result))

    __rmul__ = __mul__

    def __truediv__(self, rational):
        return A(tuple(x / F(rational) for x in self.c))

    def __eq__(self, other):
        return self.c == A(other).c

    def bounds(self, digits=12):
        scale = 10 ** digits
        lo = hi = self.c[0]
        for coefficient, radicand in zip(self.c[1:], (6, 21, 126)):
            root = isqrt(radicand * scale * scale)
            lower, upper = F(root, scale), F(root + 1, scale)
            lo += coefficient * (lower if coefficient >= 0 else upper)
            hi += coefficient * (upper if coefficient >= 0 else lower)
        return lo, hi

    def sign(self):
        if all(x == 0 for x in self.c):
            return 0
        for digits in (12, 24, 48, 96):
            lower, upper = self.bounds(digits)
            if lower > 0:
                return 1
            if upper < 0:
                return -1
        raise AssertionError('nonzero algebraic sign was not isolated')


def add(v, w):
    return tuple(a + b for a, b in zip(v, w))


def sub(v, w):
    return tuple(a - b for a, b in zip(v, w))


def times(a, v):
    return tuple(a * x for x in v)


def dot(v, w):
    return sum(a * b for a, b in zip(v, w))


def cross(v, w):
    return v[0] * w[1] - v[1] * w[0]


def det(matrix):
    n = len(matrix)
    value = A(0)
    for order in permutations(range(n)):
        inversions = sum(order[i] > order[j] for i in range(n) for j in range(i + 1, n))
        term = A((-1) ** inversions)
        for i in range(n):
            term *= matrix[i][order[i]]
        value += term
    return value


def main():
    root6, root21 = A((0, 1, 0, 0)), A((0, 0, 1, 0))
    U, V = 2 * root21, 4 * root6
    points = {
        'a': (0, 0), 'b': (6, 8), 'p': (0, 8), 'q': (6, 0),
        'c': (2, U - V), 'd': (4, U), 'cp': (2, U), 'dp': (4, U - V),
        'L': (-2, 4), 'R': (8, 4), 'Rp': (F(318, 41), F(254, 41)),
        'zt': (3, U - V / 2 + 5), 'zb': (3, U - V / 2 - 5),
    }
    points = {name: tuple(A(x) for x in xy) for name, xy in points.items()}
    layer = {'L': 0, 'a': 1, 'p': 1, 'c': 2, 'cp': 2, 'zt': 3, 'zb': 3,
             'd': 4, 'dp': 4, 'b': 5, 'q': 5, 'R': 6, 'Rp': 6}
    expected = {frozenset(edge) for edge in (
        ('a', 'b'), ('a', 'd'), ('p', 'q'), ('q', 'cp'), ('c', 'd'),
        ('cp', 'dp'), ('L', 'R'), ('L', 'Rp'), ('zt', 'zb'))}
    actual = set()
    distances = []
    inactive = []
    for a, b in combinations(points, 2):
        r = sub(points[b], points[a])
        distance_sq = dot(r, r)
        distances.append(distance_sq)
        assert (distance_sq - F(201, 200) ** 2).sign() > 0
        assert (distance_sq - 100).sign() <= 0
        if distance_sq == 100:
            actual.add(frozenset((a, b)))
        else:
            inactive.append(distance_sq)
            assert (distance_sq - F(199, 20) ** 2).sign() < 0
    assert actual == expected
    minimum, maximum_inactive = 50 - 20 * root6, 50 + 20 * root6
    assert minimum in distances and maximum_inactive in inactive
    assert all((value - minimum).sign() >= 0 for value in distances)
    assert all((maximum_inactive - value).sign() >= 0 for value in inactive)
    # Every source point is an actual diameter endpoint, but contact-isolated.
    assert set.union(*(set(edge) for edge in actual)) == set(points)

    # All disjoint actual diameter chords cross properly (exact thrackle check).
    for first, second in combinations(actual, 2):
        if first & second:
            continue
        a, b = sorted(first)
        c, d = sorted(second)
        ab, cd = sub(points[b], points[a]), sub(points[d], points[c])
        assert cross(ab, sub(points[c], points[a])).sign() * cross(ab, sub(points[d], points[a])).sign() < 0
        assert cross(cd, sub(points[a], points[c])).sign() * cross(cd, sub(points[b], points[c])).sign() < 0

    # The two actual wall chords are a common star at L and bound the cell J.
    wall0, wall1 = (A(10), A(0)), (A(F(400, 41)), A(F(90, 41)))
    e = (A(F(399, 401)), A(F(40, 401)))
    assert dot(e, e) == 1
    assert cross(wall0, e).sign() > 0 and cross(e, wall1).sign() > 0
    rows, directed = [], []
    for edge in sorted(actual, key=lambda edge: sorted(edge)):
        a, b = sorted(edge, key=lambda name: (layer[name], name))
        r = sub(points[b], points[a])
        lo, hi = layer[a], layer[b]
        if r[0].sign() < 0 or (r[0].sign() == 0 and r[1].sign() < 0):
            projective = times(-1, r)
        else:
            projective = r
        # No other direction lies between wall directions.
        if edge not in {frozenset(('L', 'R')), frozenset(('L', 'Rp'))}:
            assert not (cross(wall0, projective).sign() > 0 and
                        cross(projective, wall1).sign() > 0)
        beta = F(1) if a == 'L' else F(1, 100)
        rows.append((lo, hi, r, beta))
        if lo < hi:
            sign = cross(e, r).sign()
            assert sign != 0
            directed.append((lo, hi) if sign > 0 else (hi, lo))
    assert sorted(directed) == sorted(((0, 6), (6, 0), (1, 5), (5, 1),
                                      (1, 4), (5, 2), (2, 4), (4, 2)))

    reach = [{i} for i in range(7)]
    for a, b in directed:
        reach[a].add(b)
    for k in range(7):
        for i in range(7):
            if k in reach[i]:
                reach[i] |= reach[k]
    sccs = {frozenset(j for j in range(7) if j in reach[i] and i in reach[j])
            for i in range(7)}
    assert sccs == {frozenset((0, 6)), frozenset((1, 5)), frozenset((2, 4)), frozenset((3,))}
    assert all(not (b in {1, 5} and a not in {1, 5}) for a, b in directed)
    assert all(not (a in {2, 4} and b not in {2, 4}) for a, b in directed)
    assert (1, 4) in directed and (5, 2) in directed
    lower_host = {'a', 'c', 'zb', 'dp', 'q'}
    upper_host = {'p', 'cp', 'zt', 'd', 'b'}
    for component in ({1, 5}, {2, 4}):
        packet = {name for edge in actual
                  if all(layer[name] in component for name in edge)
                  for name in edge}
        assert len(packet & lower_host) == len(component)
        assert len(packet & upper_host) == len(component)
        assert len(packet) == 2 * len(component)

    base = add(wall0, wall1)
    cuts = []
    for i in range(1, 7):
        resultant = (A(0), A(0))
        low_flow = high_flow = A(0)
        for lo, hi, r, beta in rows:
            if lo < i <= hi:
                resultant = add(resultant, times(beta, r))
                flow = beta * cross(e, r)
                if flow.sign() > 0:
                    low_flow += flow
                else:
                    high_flow -= flow
        assert low_flow.sign() > 0 and high_flow.sign() > 0
        assert cross(wall0, resultant).sign() > 0
        assert cross(resultant, wall1).sign() > 0
        assert low_flow - high_flow == cross(e, resultant)
        cuts.append(resultant)
    targets = (base, add(base, (A(F(16, 100)), U / 100)),
               add(base, (A(F(24, 100)), A(0))),
               add(base, (A(F(24, 100)), A(0))),
               add(base, (A(F(16, 100)), -U / 100)), base)
    assert cuts == list(targets)

    # For arbitrary homothety s>=1, walls contribute s*base and every old
    # beta=1/(100s) contributes the same bounded correction as above.
    # Each correction has norm<1/4; normalized phase spread is <1/(19s).
    assert (dot(base, base) - 19 ** 2).sign() > 0
    for correction in (sub(target, base) for target in targets):
        assert (dot(correction, correction) - F(1, 16)).sign() < 0

    # Scale each derivative column by its positive cut mass. The entries
    # become cross(r_h,R_i), without introducing another square root.
    matrix = [[cross(r, cuts[i-1]) if lo < i <= hi else A(0)
               for i in range(1, 7)] for lo, hi, r, beta in rows]
    assert all(row[0] == row[5] and row[2] == row[3] for row in matrix)
    nonzero_minor = False
    for indexes in combinations(range(len(matrix)), 4):
        minor = [[matrix[j][i] for i in (0, 1, 2, 4)] for j in indexes]
        if det(minor).sign() != 0:
            nonzero_minor = True
            break
    assert nonzero_minor  # Together with the two column identities: rank=4.
    print('PASS: all 78 source pairs; exactly 9 actual diameters; all disjoint chords cross;')
    print('common-star open cell; noninterval source/sink SCCs; all 6 positive cut resultants;')
    print('strict inactive-pair margins; exact divergence; homothetic phase bound; derivative rank 4.')
    print('REGRESSION ONLY: no actual unit contacts, vertex KKT stress, or global optimality.')


if __name__ == '__main__':
    main()
