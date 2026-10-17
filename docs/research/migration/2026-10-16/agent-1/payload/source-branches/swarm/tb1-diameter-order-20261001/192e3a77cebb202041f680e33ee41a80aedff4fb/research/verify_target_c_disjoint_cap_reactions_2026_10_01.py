#!/usr/bin/env python3
"""Exact regressions for the disjoint-cap reaction theorem.

Encoded: rational quadratic-field coordinates, every source distance/contact/
diameter, exact individual row swaps, and circular interval packing on a finite
angular mesh. Omitted: global optimality, positive KKT, mixed rigidity, and the
existence of an extracted swap family. The tooth packets deliberately violate
positive KKT: each tooth cap has contacts across its cut and no diameter across
it. The universal cap theorem has an analytical proof in the report.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = q(other)
        return Q3(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -q(other)

    def __mul__(self, other):
        other = q(other)
        return Q3(self.a * other.a + 3 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def sign(self):
        if self.a == 0:
            return (self.b > 0) - (self.b < 0)
        if self.b == 0 or (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        d = self.a * self.a - 3 * self.b * self.b
        return ((d > 0) - (d < 0)) * ((self.a > 0) - (self.a < 0))


def q(x):
    return x if isinstance(x, Q3) else Q3(F(x))


def add(p, v):
    return tuple(x + y for x, y in zip(p, v))


def sub(p, v):
    return tuple(x - y for x, y in zip(p, v))


def norm2(p, v):
    d = sub(p, v)
    return sum(x * x for x in d)


def rotate(p, c, s):
    return (c * p[0] - s * p[1], s * p[0] + c * p[1])


def tooth_packet(r):
    # phi=2 atan(t), v has angle 2phi, sigma has angle pi/3+phi,
    # b has angle pi/3+3phi. All coordinates lie in Q(sqrt(3)).
    t = F(1, 10000 * r)
    c, s = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
    u = (q(1), q(0))
    v = rotate(rotate(u, c, s), c, s)
    sigma = rotate((q(F(1, 2)), Q3(F(0), F(1, 2))), c, s)
    b = rotate(rotate(sigma, c, s), c, s)
    origin = (q(0), q(0))
    assert all(norm2(origin, w) == q(1) for w in (u, v, sigma, b))
    rows = [w for _ in range(r) for w in (u, u, v, v)]
    positions = [origin]
    for w in rows:
        positions.append(add(positions[-1], w))
    points = []
    grid = {}
    for i, p in enumerate(positions):
        for j in range(3):
            grid[i, j] = len(points)
            points.append(add(p, tuple(j * x for x in b)))
    teeth = []
    modules = []
    for k in range(r):
        i = 4 * k + 1  # the second u-row, preceded by another u-row
        low, high = sub(positions[i], sigma), sub(positions[i + 1], sigma)
        teeth.append((len(points), len(points) + 1, grid[i, 0], grid[i + 1, 0]))
        points.extend((low, high))
        modules.append({grid[i + 1, j] for j in range(3)} | {teeth[-1][1]})
    pairs = list(combinations(range(len(points)), 2))
    squared = {e: norm2(points[e[0]], points[e[1]]) for e in pairs}
    assert all((d - 1).sign() >= 0 for d in squared.values())
    contacts = {e for e, d in squared.items() if d == q(1)}
    for a, b0, c0 in combinations(range(len(points)), 3):
        assert not {(a, b0), (a, c0), (b0, c0)} <= contacts
    diameter2 = q(0)
    for d in squared.values():
        if (d - diameter2).sign() > 0:
            diameter2 = d
    diameters = {e for e, d in squared.items() if d == diameter2}
    loaded = {i for e in diameters for i in e}
    delta = sub(v, u)
    # s_swap <= 1/(2D), using an exact squared comparison.
    assert (4 * diameter2 * norm2(delta, origin) - 1).sign() < 0
    for k, module in enumerate(modules):
        moved = [add(p, delta) if j in module else p for j, p in enumerate(points)]
        assert all(norm2(moved[a], moved[b0]) == q(1) for a, b0 in contacts)
        assert all(norm2(moved[a], moved[b0]) == diameter2 for a, b0 in diameters)
        low, high, anchor_low, anchor_high = teeth[k]
        blocker = tuple(sorted((anchor_low, high)))
        assert (squared[blocker] - 1).sign() > 0
        assert (norm2(moved[anchor_low], moved[high]) - 1).sign() < 0
        cap = {low, high}
        crossing_contacts = {e for e in contacts if len(cap & set(e)) == 1}
        assert crossing_contacts == {tuple(sorted((low, anchor_low))),
                                     tuple(sorted((high, anchor_high)))}
        assert not cap & loaded
        assert not module & loaded  # the required changed-diameter hypothesis fails
    print(f"PASS: r={r}, {len(points)} points, {len(contacts)} unit contacts, "
          f"{len(diameters)} diameters, {r} exact rhombus blockers; no cap KKT")


def interval_mesh():
    # Circle length 24, projective period 12, separation delta=2.
    # Reaction marks are in the interiors of two opposite width-W windows.
    # Broad normal spans are >=12; all other witness intervals have length >=2.
    # Enumerate every circular cut, every pair of window starts/widths, and find
    # the maximum disjoint-interval count by exact weighted interval scheduling.
    packets = 0
    for cut in range(24):
        for start in range(12):
            for width in range(1, 6):
                marks = {(2 * start + j) % 48 for j in range(2 * width + 1)}
                marks |= {(x + 24) % 48 for x in tuple(marks)}
                ending = {i: [] for i in range(25)}
                for left in range(24):
                    for right in range(left + 2, 25):
                        broad = right - left >= 12
                        has_mark = any((2 * cut + x) % 48 in marks
                                       for x in range(2 * left + 1, 2 * right))
                        if broad or has_mark:
                            ending[right].append(left)
                best = [0] * 25
                for right in range(1, 25):
                    best[right] = max([best[right - 1]] +
                                      [1 + best[left] for left in ending[right]])
                assert best[24] <= 2 * (width // 2) + 6
                packets += 1
    print(f"PASS: {packets} exact circular normal-span interval packets")


def alternating_supports():
    packets = 0
    for r in range(1, 11):
        phases = [i % 2 for i in range(2 * r)]
        for left in range(2 * r):
            for right in range(left, 2 * r):
                support = set(range(left, right + 1))
                for forbidden in (0, 1):
                    if any(phases[i] == forbidden for i in support):
                        continue
                    assert len(support) == 1
                    packets += 1
    print(f"PASS: {packets} alternating selected-cut supports")


if __name__ == "__main__":
    for count in (2, 3, 5, 10):
        tooth_packet(count)
    interval_mesh()
    alternating_supports()
