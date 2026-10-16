#!/usr/bin/env python3
"""Exact finite cap checks. No KKT, train extraction, or optimality certificate."""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt


def sqdist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def turn(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    sides = []
    for seq in (points, points[::-1]):
        side = []
        for p in seq:
            while len(side) >= 2 and turn(side[-2], side[-1], p) <= 0:
                side.pop()
            side.append(p)
        sides.append(side[:-1])
    return sides[0] + sides[1]


def cap_threshold(d2, l2):
    # 2L/D >= 3-L^2-L^2/D^2, with both sides nonnegative before squaring.
    residue = 3 - l2 - l2 / d2
    return residue <= 0 or 4 * l2 / d2 >= residue**2


def finite_grid():
    grid = [(F(x, 2), F(y, 2)) for x in range(5) for y in range(5)]
    packets = caps = 0
    for size in (4, 5):
        for points in combinations(grid, size):
            distances = {(i, j): sqdist(points[i], points[j])
                         for i, j in combinations(range(size), 2)}
            if min(distances.values()) < 1:
                continue
            d2 = max(distances.values())
            loaded = {i for edge, length in distances.items() if length == d2 for i in edge}
            boundary = hull(points[i] for i in loaded)
            if len(boundary) < 3:
                continue
            packets += 1
            for a, b in zip(boundary, boundary[1:] + boundary[:1]):
                if any(turn(a, b, z) < 0 for z in points):
                    caps += 1
                    assert cap_threshold(d2, sqdist(a, b)), (points, a, b)
    assert caps > 0, "Finite universe must include nonempty loaded caps."
    return packets, caps


@dataclass(frozen=True)
class Interval:
    lo: F
    hi: F

    @staticmethod
    def point(x):
        return Interval(F(x), F(x))

    def __add__(self, other):
        if not isinstance(other, Interval):
            other = self.point(other)
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Interval) else -F(other))

    def __mul__(self, other):
        if not isinstance(other, Interval):
            other = self.point(other)
        bounds = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return Interval(min(bounds), max(bounds))

    def __truediv__(self, denominator):
        assert denominator > 0
        return self * F(1, denominator)

    def square(self):
        high = max(self.lo**2, self.hi**2)
        low = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return Interval(F(low), high)

    def sqrt(self):
        assert self.lo >= 0
        scale = 1 << 128
        low = isqrt(self.lo.numerator * scale**2 // self.lo.denominator)
        high = isqrt(self.hi.numerator * scale**2 // self.hi.denominator) + 1
        return Interval(F(low, scale), F(high, scale))


def radical_regressions():
    count = 0
    for diameter in list(range(10, 65)) + [100, 1000, 10000]:
        d = F(diameter)
        l = Interval.point(3).sqrt() + 1 / d
        r = F(1) + F(1, 100) / d
        height = (Interval.point(d**2) - ((l + d) / 2).square()).sqrt()
        top = (Interval.point(r**2) - (l / 2).square()).sqrt()
        assert l.lo > 1 and l.hi < 2
        assert top.lo > 0
        assert (Interval.point(d**2) - l * d).lo > 1
        cross_top = (height + top).square() + d**2 / 4
        assert cross_top.lo > 1 and cross_top.hi < d**2
        # ac,bd,cd have exact squared length D^2 by their defining formulas.
        assert r > 1
        assert 3 * r**2 < l.square().lo
        count += 1
    return count


def rational_regressions():
    count = 0
    for t in (F(2, 7), F(27, 100), F(269, 1000), F(268, 1000), F(26795, 100000)):
        kappa = 4 * t / (1 + t**2) - 1
        assert kappa > 0
        l = F(7, 4)
        d = l / kappa
        height = d * (1 - t**2) / (1 + t**2)
        points = [(-l / 2, F(0)), (l / 2, F(0)),
                  (d / 2, -height), (-d / 2, -height), (F(0), F(1, 2))]
        distances = {(i, j): sqdist(points[i], points[j]) for i, j in combinations(range(5), 2)}
        assert min(distances.values()) > 1
        assert {e for e, x in distances.items() if x == d**2} == {(0, 2), (1, 3), (2, 3)}
        assert max(distances.values()) == d**2
        assert cap_threshold(d**2, l**2)
        apex_height = (d + l) * l / (4 * height)
        assert apex_height > F(1, 2)
        # Squared bound on the two equal tangent-triangle apex sides.
        side2 = l**2 / 4 + apex_height**2
        if l <= d / 4:
            assert side2 * 39 <= 16 * l**2
        assert hull(points[:4]) == [points[3], points[2], points[1], points[0]]
        count += 1
    return count


def quadrilateral_pocket_regression():
    count = 0
    for diameter in (10, 30, 100, 300, 1000, 10000):
        d = F(diameter)
        t = F(1, 100 * diameter)
        cosine, sine = (1 - t**2) / (1 + t**2), 2 * t / (1 + t**2)
        v = ((1 - 4 * t**2) / (1 + 4 * t**2), 4 * t / (1 + 4 * t**2))
        l = 1 + 2 * sine
        height = Interval.point(d**2 - (d + l)**2 / 4).sqrt()
        points = [(-sine, F(0)), (F(0), -cosine), (F(1), -cosine),
                  (1 + sine, F(0))]
        # Coordinates rotated from a=(cos,-sin), x=0, y=(0,1), b=(cos,1+sin).
        # Add actual loaded partners c,d on the inward side of the near-unit base.
        points += [(F(1, 2) + d / 2, -height), (F(1, 2) - d / 2, -height)]
        intervals = [(Interval.point(x), y if isinstance(y, Interval) else Interval.point(y))
                     for x, y in points]
        actual_h = {(0, 4), (3, 5), (4, 5)}
        contacts = {(0, 1), (1, 2), (2, 3)}
        for i, j in combinations(range(6), 2):
            distance = sum_interval_squares(intervals[i], intervals[j])
            if (i, j) in actual_h:
                continue  # Exact by H^2=D^2-(D+L)^2/4.
            if (i, j) in contacts:
                assert distance.lo == distance.hi == 1
            else:
                assert distance.lo > 1 and distance.hi < d**2
        # After replacing the first side by v, the closing pair overlaps exactly.
        old_a = (cosine, -sine)
        old_b = (cosine, 1 + sine)
        assert sqdist(old_a, old_b) > 1
        assert sqdist(v, old_b) < 1
        assert sqdist(v, (F(0), F(1))) > 1
        # In original coordinates, old ac=(H,-(D+L)/2); both Delta signs shorten it.
        dx, dy = v[0] - cosine, v[1] + sine
        change = height * (2 * dx) + (-(d + l) * dy + dx**2 + dy**2)
        assert change.hi < 0
        moved = list(intervals)
        moved[0] = (Interval.point(v[1]), Interval.point(v[0] - cosine))
        for i, j in combinations(range(6), 2):
            if (i, j) in {(3, 5), (4, 5)} | contacts:
                continue
            distance = sum_interval_squares(moved[i], moved[j])
            assert distance.hi < d**2
            if (i, j) == (0, 3):
                assert distance.hi < 1
            else:
                assert distance.lo > 1
        count += 1
    return count


def sum_interval_squares(a, b):
    return (a[0] - b[0]).square() + (a[1] - b[1]).square()


def face_colors():
    packets = survivors = 0
    for size in range(3, 11):
        for colors in product((0, 1), repeat=size):
            packets += 1
            crossing = {i for i in range(size) if colors[i] != colors[(i + 1) % size]}
            if not crossing:
                assert len(set(colors)) == 1
                survivors += 1
    assert survivors == 16
    # Explicit I-end / outer-end boundary: dropping completeness loses monochromy.
    colors = (0, 0, 0, 1, 1)
    assert {i for i in range(5) if colors[i] != colors[(i + 1) % 5]} == {2, 4}
    return packets, survivors


def constants():
    # tau_D>3/2 for D>=6 reduces to this decreasing rational expression at D=6.
    assert F(3, 6) + F(9, 4 * 6**2) < F(3, 4)
    assert 4 * F(19, 12)**2 < 11
    assert F(125, 27) < 5
    assert F(216**2, 39) < 35**2
    # Exact isosceles pocket formula: closing-angle cosine squared is L^2/4.
    for t in (F(5, 3), F(19, 11), F(71, 41), F(265, 153), F(989, 571)):
        w = ((1 - t**2) / (1 + t**2), 2 * t / (1 + t**2))
        closing = (1 + w[0], w[1])
        l2 = sqdist(closing, (F(0), F(0)))
        assert l2 > 1
        assert closing[0]**2 / l2 == l2 / 4


def host_blocks(counts, corners):
    word = []
    for group, count in enumerate(counts):
        for index in range(count):
            if index:
                word.append(None)  # An actual loaded anchor inside this host.
            word.append((group, index))
        if corners & (1 << group):
            word.append(None)
    marker = word.index(None)
    word = word[marker + 1:] + word[:marker + 1]
    blocks = []
    current = []
    for token in word:
        if token is None:
            if current:
                blocks.append(tuple(current))
            current = []
        else:
            current.append(token)
    assert not current
    return blocks


def pocket_end_census():
    words = exemptions = 0
    for ma, mb in product(range(2, 5), repeat=2):
        for corners in range(16):
            blocks = host_blocks((ma, mb, ma, mb), corners)
            words += 1
            assert all(len(block) <= 2 for block in blocks)
            assert all(len({group % 2 for group, _ in block}) == len(block) for block in blocks)
            assert sum(len(block) == 2 for block in blocks) <= 4
            ends = tuple(token for block in blocks for token in block)
            for count in range(5):
                for selected in combinations(ends, count):
                    free = set(selected)
                    occupied = sum(bool(set(block) - free) for block in blocks)
                    assert occupied >= 2 * (ma + mb) - 8
                    exemptions += 1
    blocks = host_blocks((3, 3, 3, 3), 0)
    free = {(group, 1) for group in range(4)}
    occupied = sum(bool(set(block) - free) for block in blocks)
    assert occupied == 4 == 12 - 8
    gap_packets = 0
    for m in range(1, 11):
        for steps in product((0, 1), repeat=m - 1):
            a, b = 0, m
            edges = [(a, b)]
            for step in steps:
                a += step
                b -= 1 - step
                edges.append((a, b))
            anchors = {k: set() for k in range(m + 1)}
            for a, b in edges:
                for side in (0, 1):
                    anchors[a].add(side)
                    anchors[b].add(1 - side)
            assert all(anchors[k] == {0, 1} for k in range(1, m))
            gap_packets += 1
    return words, exemptions, gap_packets


def main():
    packets, caps = finite_grid()
    print(f"PASS rational finite grid: {packets} loaded-hull packets, {caps} nonempty caps")
    print(f"PASS rational five-point empty-cap regressions: {rational_regressions()}")
    print(f"PASS 128-bit rational radical enclosures: {radical_regressions()} sharpness packets")
    print(f"PASS three-contact pocket overlap regressions: {quadrilateral_pocket_regression()}")
    packets, survivors = face_colors()
    print(f"PASS exhaustive binary face incidence: {packets} colorings, {survivors} monochrome survivors")
    constants()
    words, exemptions, gaps = pocket_end_census()
    print(f"PASS cyclic host words: {words} words, {exemptions} exemption packets, {gaps} paired gap trees")
    print("PASS exact constants; no source KKT, train extraction, or global-optimality claim")


if __name__ == "__main__":
    main()
