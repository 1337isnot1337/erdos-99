#!/usr/bin/env python3
"""Exact finite checks for strict near-diameter capacity; not global optimality.

Encoded: unit separation, full diameter, extreme hull vertices, segment crossings,
strict near-diameter threshold, strict Gabriel cutoff. All grid arithmetic is
integer arithmetic in coordinates scaled by 2. The analytical universal proofs
are in the accompanying report. Omitted: KKT, optimality, train embedding and
the rooted endpoint hypothesis. Passing is a regression check, not a theorem
about every global minimizer.
"""

from itertools import combinations
from fractions import Fraction


def norm2(p, q):
    return sum((a - b) ** 2 for a, b in zip(p, q))


def turn(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    ordered = sorted(points)
    chains = []
    for order in (ordered, ordered[::-1]):
        chain = []
        for p in order:
            while len(chain) >= 2 and turn(chain[-2], chain[-1], p) <= 0:
                chain.pop()
            chain.append(p)
        chains.append(chain)
    return set(chains[0][:-1] + chains[1][:-1])


def proper_cross(a, b, c, d):
    return turn(a, b, c) * turn(a, b, d) < 0 and turn(c, d, a) * turn(c, d, b) < 0


def check(points, unit2):
    edges = list(combinations(range(len(points)), 2))
    squared = {e: norm2(points[e[0]], points[e[1]]) for e in edges}
    assert min(squared.values()) >= unit2
    diameter2 = max(squared.values())
    extreme = hull(points)
    near_d = [e for e in edges if squared[e] > diameter2 - unit2]
    assert all(points[i] in extreme for e in near_d for i in e)
    assert len(near_d) <= len(extreme)
    for e, f in combinations(near_d, 2):
        if set(e).isdisjoint(f):
            assert proper_cross(*(points[i] for i in e + f))
    short = [e for e in edges if squared[e] < 2 * unit2]
    for e in short:
        p, q = (points[i] for i in e)
        for z in (points[i] for i in range(len(points)) if i not in e):
            assert sum((z[k] - p[k]) * (z[k] - q[k]) for k in (0, 1)) > 0
    for e, f in combinations(short, 2):
        if set(e).isdisjoint(f):
            assert not proper_cross(*(points[i] for i in e + f))
    return len(near_d) - sum(s == diameter2 for s in squared.values())


def sharp_regressions():
    points = [(0, 0), (0, 1), (0, -1), (3, 0)]
    assert max(norm2(p, q) for p, q in combinations(points, 2)) == 10
    assert (0, 0) not in hull(points)
    assert norm2(points[0], points[3]) == 9
    check(points, 1)
    rectangle = [(0, 0), (3, 0), (3, 1), (0, 1)]
    assert max(norm2(p, q) for p, q in combinations(rectangle, 2)) == 10
    assert norm2(rectangle[0], rectangle[1]) == norm2(rectangle[2], rectangle[3]) == 9
    assert not proper_cross(*rectangle)
    check(rectangle, 1)
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    assert proper_cross(square[0], square[2], square[1], square[3])
    assert norm2(square[0], square[2]) == norm2(square[1], square[3]) == 2
    check(square, 1)
    # Linear planar near-unit witnesses, with an exact inverse-diameter margin.
    for r in (2, 3, 10, 50):
        height = 1 + Fraction(1, 10 * r)
        family = [(3 * j, y) for j in range(r) for y in (0, height)]
        diameter2 = max(norm2(p, q) for p, q in combinations(family, 2))
        assert diameter2 <= (3 * r) ** 2
        assert 2 * 3 * r * (height - 1) < 1
        assert min(norm2(p, q) for p, q in combinations(family, 2)) > 1
        check(family, 1)
    # Unit triangular rhombus, in the exact basis with Gram matrix [[1,1/2],[1/2,1]].
    rhombus = [(0, 0), (1, 0), (0, 1), (1, -1)]
    def triangular_norm(p, q):
        a, b = p[0] - q[0], p[1] - q[1]
        return a * a + a * b + b * b
    assert triangular_norm(rhombus[0], rhombus[1]) == 1
    assert triangular_norm(rhombus[2], rhombus[3]) == 3
    assert all(triangular_norm(p, q) >= 1 for p, q in combinations(rhombus, 2))


def main():
    sharp_regressions()
    grid = list(combinations([(i, j) for i in range(6) for j in range(6)], 4))
    eligible = inactive = packets_with_inactive = 0
    for points in grid:
        if any(norm2(p, q) < 4 for p, q in combinations(points, 2)):
            continue
        eligible += 1
        count = check(points, 4)
        inactive += count
        packets_with_inactive += count > 0
    print(f"PASS: {eligible} unit-separated four-point half-grid packets; "
          f"{packets_with_inactive} packets with {inactive} strict inactive near-diameter edges")
    print("PASS: sharp extremality/crossing/Gabriel regressions and four exact linear-witness families")
    print("Not encoded: KKT, train geometry, rooted endpoint, or global optimality.")


if __name__ == '__main__':
    main()
