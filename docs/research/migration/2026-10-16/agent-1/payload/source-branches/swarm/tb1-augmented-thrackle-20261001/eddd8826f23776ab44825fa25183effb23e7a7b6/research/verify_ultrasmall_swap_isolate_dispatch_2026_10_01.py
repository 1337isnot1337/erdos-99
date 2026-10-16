#!/usr/bin/env python3
"""Exact finite regressions for the October 1 long-pair/isolate-dispatch report.

Encodes source unit separation, actual diameter, strict long threshold, hull
extremality, proper crossings, short-pair planarity, and one cyclic binary move.
Uses Fraction and Q(sqrt(3)); no tolerances or global optimality assertions.
Does not encode train cuts, the fixed-star extraction, KKT, or source minimality.
Universal conclusions are proved in the report, not by these finite samples.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from random import Random


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def distance2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def hull(points):
    ordered = sorted(set(points))
    halves = []
    for order in (ordered, ordered[::-1]):
        half = []
        for p in order:
            while len(half) >= 2 and cross(half[-2], half[-1], p) <= 0:
                half.pop()
            half.append(p)
        halves.append(half[:-1])
    return set(halves[0] + halves[1])


def proper_cross(a, b, c, d):
    return cross(a, b, c) * cross(a, b, d) < 0 and cross(c, d, a) * cross(c, d, b) < 0


def rational_packet(points):
    pairs = {ij: distance2(points[ij[0]], points[ij[1]]) for ij in combinations(range(len(points)), 2)}
    assert min(pairs.values()) >= 1
    diameter2 = max(pairs.values())
    long_edges = [ij for ij, value in pairs.items() if value > diameter2 - 1]
    extreme = hull(points)
    incident = {i for ij in long_edges for i in ij}
    assert all(points[i] in extreme for i in incident)
    assert len(long_edges) <= len(incident)
    for ij, kl in combinations(long_edges, 2):
        if set(ij).isdisjoint(kl):
            assert proper_cross(points[ij[0]], points[ij[1]], points[kl[0]], points[kl[1]])
        else:
            common = set(ij) & set(kl)
            v = common.pop()
            others = (set(ij) | set(kl)) - {v}
            a, b = others
            assert cross(points[v], points[a], points[b]) != 0
    short_edges = [ij for ij, value in pairs.items() if value <= F(101, 100) ** 2]
    for ij, kl in combinations(short_edges, 2):
        if set(ij).isdisjoint(kl):
            assert not proper_cross(points[ij[0]], points[ij[1]], points[kl[0]], points[kl[1]])
    for i, j in short_edges:
        for k in set(range(len(points))) - {i, j}:
            assert not (cross(points[i], points[j], points[k]) == 0 and
                        sum((points[k][axis] - points[i][axis]) *
                            (points[k][axis] - points[j][axis]) for axis in (0, 1)) < 0)
    return sum(pairs[ij] < diameter2 for ij in long_edges)


@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def lift(value):
        return value if isinstance(value, Q3) else Q3(F(value))

    def __add__(self, other):
        other = self.lift(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.lift(other)

    def __rsub__(self, other):
        return self.lift(other) + -self

    def __mul__(self, other):
        other = self.lift(other)
        return Q3(self.a * other.a + 3 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __pow__(self, power):
        assert power == 2
        return self * self

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a or self.a * self.b > 0:
            return (self.b > 0) - (self.b < 0)
        gap = self.a * self.a - 3 * self.b * self.b
        return ((gap > 0) - (gap < 0)) * ((self.a > 0) - (self.a < 0))

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __le__(self, other):
        return (self - other).sign() <= 0

    def __gt__(self, other):
        return (self - other).sign() > 0

    def __ge__(self, other):
        return (self - other).sign() >= 0


def regressions():
    rectangle = [(F(0), F(0)), (F(1), F(0)), (F(1), F(15, 8)), (F(0), F(15, 8))]
    assert max(distance2(a, b) for a, b in combinations(rectangle, 2)) == F(17, 8) ** 2
    assert distance2(rectangle[0], rectangle[3]) == F(17, 8) ** 2 - 1
    assert not proper_cross(rectangle[0], rectangle[3], rectangle[1], rectangle[2])
    rational_packet(rectangle)
    nonextreme = [(F(-1), F(0)), (F(0), F(0)), (F(1), F(0)), (F(0), F(15, 8))]
    assert nonextreme[1] not in hull(nonextreme)
    assert distance2(nonextreme[1], nonextreme[3]) == F(17, 8) ** 2 - 1
    rational_packet(nonextreme)
    square = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    assert distance2(square[0], square[2]) == distance2(square[1], square[3]) == 2
    assert proper_cross(square[0], square[2], square[1], square[3])
    for t in [F(1, 10**k) for k in range(1, 9)]:
        near_triangle = [(Q3(), Q3()), (Q3(F(1)), Q3()),
                         (Q3(F(1, 2)), Q3(F(0), (1 + t) / 2))]
        lengths = [distance2(a, b) for a, b in combinations(near_triangle, 2)]
        assert lengths[0] == Q3(F(1))
        assert lengths[1] == lengths[2] == Q3(1 + F(3, 2) * t + F(3, 4) * t * t)
        assert 1 < lengths[1]


def cyclic_dispatch():
    d = F(10)
    t = F(999, 1000)
    points = [(Q3(), Q3()), (Q3(d), Q3()), (Q3(d / 2), Q3(F(0), d / 2)),
              (Q3(F(0), t * d / 2), Q3(t * d / 2))]
    pairs = {ij: distance2(points[ij[0]], points[ij[1]]) for ij in combinations(range(4), 2)}
    assert min(pairs.values()) >= 1
    actual = {ij for ij, value in pairs.items() if value == Q3(d * d)}
    long_edges = {ij for ij, value in pairs.items() if d * d - 1 < value}
    assert actual == {(0, 1), (0, 2), (1, 2)}
    assert long_edges == actual | {(0, 3)}
    for s in [F(1, 10**k) for k in range(2, 7)]:
        assert d * d - 1 < (d - s) ** 2  # s < gamma_D, with d-s positive
        delta = (Q3(F(0), s / 2), Q3(s / 2))
        moved = [(p[0] + delta[0], p[1] + delta[1]) if i in {0, 3} else p
                 for i, p in enumerate(points)]
        after = {ij: distance2(moved[ij[0]], moved[ij[1]]) for ij in pairs}
        assert after[0, 3] == pairs[0, 3]
        assert after[0, 1] < d * d and after[0, 2] < d * d
        assert after[1, 2] == Q3(d * d)
        assert all(value < d * d for ij, value in after.items() if ij not in actual)
        assert min(after.values()) >= 1
    # Forest H on old endpoints: an inactive old-B pair can itself be long.
    cayley = F(1, 10000)
    cosine = (1 - cayley * cayley) / (1 + cayley * cayley)
    sine = 2 * cayley / (1 + cayley * cayley)
    c = (Q3(d * cosine / 2, d * sine / 2), Q3(-d * sine / 2, d * cosine / 2))
    forest_points = points[:2] + [c]
    forest_pairs = {ij: distance2(forest_points[ij[0]], forest_points[ij[1]])
                    for ij in combinations(range(3), 2)}
    assert forest_pairs[0, 1] == forest_pairs[0, 2] == Q3(d * d)
    assert d * d - 1 < forest_pairs[1, 2] < d * d


def main():
    regressions()
    cyclic_dispatch()
    rng = Random(991001)
    samples = 0
    inactive_long = 0
    for _ in range(1200):
        radius = F(rng.randrange(3, 21))
        points = []
        for _ in range(30):
            parameter = F(rng.randrange(-80, 81), rng.randrange(1, 16))
            point = (radius * (1 - parameter ** 2) / (1 + parameter ** 2),
                     radius * 2 * parameter / (1 + parameter ** 2))
            if all(distance2(point, p) >= 1 for p in points):
                points.append(point)
            if len(points) >= 9:
                break
        if len(points) >= 3:
            inactive_long += rational_packet(points)
            samples += 1
    for _ in range(800):
        points = []
        for _ in range(35):
            point = (F(rng.randrange(-12, 13), 2), F(rng.randrange(-12, 13), 2))
            if all(distance2(point, p) >= 1 for p in points):
                points.append(point)
            if len(points) >= 10:
                break
        inactive_long += rational_packet(points)
        samples += 1
    assert inactive_long > 0
    print(f"PASS: {samples} rational source packets; {inactive_long} inactive strict-long edges")
    print("PASS: sharp long/extreme/short thresholds; 8 near-triangle packets")
    print("PASS: cyclic unique-partner dispatch at 5 amplitudes; forest old-endpoint regression")
    print("Scope: finite geometry certificates, no train/KKT/global-optimality certificate")


if __name__ == "__main__":
    main()
