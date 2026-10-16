#!/usr/bin/env python3
"""Exact source regression for the scope of rhombus swap immunity.

Encoded: all 21 original source distances, the full unit-contact graph, two
actual O-O contact cutsets, an exact binary finite phase transposition, and
both boundary rhombus short diagonals. Arithmetic is Q(sqrt(3)).
Omitted: global optimality, KKT equilibrium, strict moving-diameter decrease,
quadratic core population, and full-span diameter witnesses. No global
minimum-diameter claim follows. Universal source-face proofs are in the report.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


@dataclass(frozen=True)
class Q3:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def cast(x):
        return x if isinstance(x, Q3) else Q3(F(x))

    def __add__(self, other):
        q = self.cast(other)
        return Q3(self.a + q.a, self.b + q.b)

    __radd__ = __add__

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __sub__(self, other):
        return self + -self.cast(other)

    def __rsub__(self, other):
        return self.cast(other) - self

    def __mul__(self, other):
        q = self.cast(other)
        return Q3(self.a*q.a + 3*self.b*q.b,
                  self.a*q.b + self.b*q.a)

    __rmul__ = __mul__

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if self.a >= 0 and self.b > 0:
            return 1
        if self.a <= 0 and self.b < 0:
            return -1
        d = self.a*self.a - 3*self.b*self.b
        assert d, "sqrt(3) is irrational"
        return ((d > 0) - (d < 0)) * ((self.a > 0) - (self.a < 0))


def plus(p, q):
    return tuple(a+b for a, b in zip(p, q))


def minus(p, q):
    return tuple(a-b for a, b in zip(p, q))


def norm2(p):
    return sum(a*a for a in p)


def rotate(p, c, s):
    return (c*p[0]-s*p[1], s*p[0]+c*p[1])


EXPECTED = {(0, 1), (0, 2), (1, 3), (2, 3),
            (3, 4), (3, 5), (4, 6), (5, 6)}
LOWER = {(0, 1), (2, 3)}
UPPER = {(3, 4), (5, 6)}
LAYERS = (0, 1, 0, 1, 2, 1, 2)


def check(t):
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    u = (Q3(F(1)), Q3())
    base = (Q3(F(1, 2)), Q3(F(0), F(1, 2)))
    v = rotate(base, c, s)
    w = rotate(rotate(u, c, s), c, s)
    a = rotate(rotate(v, c, s), c, s)
    p = plus(u, v)
    points = [(Q3(), Q3()), u, v, p, plus(p, w),
              plus(p, a), plus(plus(p, w), a)]
    assert all(norm2(x) == Q3(F(1)) for x in (u, v, w, a))
    contacts = set()
    for i, j in combinations(range(7), 2):
        d = (norm2(minus(points[i], points[j])) - 1).sign()
        assert d >= 0, (t, "old overlap", i, j)
        if not d:
            contacts.add((i, j))
    assert contacts == EXPECTED, (t, contacts)
    assert not any(all(tuple(sorted(e)) in contacts for e in
                       ((i, j), (j, k), (i, k)))
                   for i, j, k in combinations(range(7), 3))
    lower = {e for e in contacts if (LAYERS[e[0]] >= 1)
             != (LAYERS[e[1]] >= 1)}
    upper = {e for e in contacts if (LAYERS[e[0]] >= 2)
             != (LAYERS[e[1]] >= 2)}
    assert lower == LOWER and upper == UPPER
    delta = minus(w, u)
    moved = [plus(p, delta) if LAYERS[i] == 1 else p
             for i, p in enumerate(points)]
    for i, j in contacts:
        assert norm2(minus(moved[i], moved[j])) == Q3(F(1))
    assert (norm2(minus(points[1], points[2]))-1).sign() > 0
    assert (norm2(minus(moved[1], moved[2]))-1).sign() < 0
    assert (norm2(minus(moved[4], moved[5]))-1).sign() > 0
    assert (norm2(delta)-F(1, 10_000)).sign() < 0
    # The v-train's contacts 02 and 13 have one end outside M and
    # one physical terminal contact edge entirely inside M.
    assert LAYERS[0] == LAYERS[2] == 0
    assert LAYERS[1] == LAYERS[3] == 1


def cyclic_alternate(edge, other):
    a, b = sorted(edge)
    c, d = other
    return (a < c < b) != (a < d < b)


def check_boundary(m, n):
    """Integer endpoint pattern; no Euclidean source realization asserted.

    Independent checks: same-shore noncrossing, all cross-shore alternation,
    and every open boundary arc carrying a perimeter pair of layer labels.
    These finite checks audit the formula; the universal proof is topological.
    """
    a_edges = [(i, 2*m+n-1-i) for i in range(m)]
    b_edges = [(m+j, 2*m+2*n-1-j) for j in range(n)]
    assert not any(cyclic_alternate(e, f)
                   for e, f in combinations(a_edges, 2))
    assert not any(cyclic_alternate(e, f)
                   for e, f in combinations(b_edges, 2))
    assert all(cyclic_alternate(e, f) for e in a_edges for f in b_edges)
    a = b = 0
    for index in range(2*m+2*n):
        if index < m:
            a += 1
        elif index < m+n:
            b += 1
        elif index < 2*m+n:
            a -= 1
        else:
            b -= 1
        assert a in (0, m) or b in (0, n)
        if 0 < a < m:
            assert b in (0, n)
        if 0 < b < n:
            assert a in (0, m)
    assert a == b == 0


def check_face_dispatch(t):
    """Actual contact ring and its formerly isolated bounded-face point.

    No KKT or diameter improvement encoded. The endpoint is feasible after
    face dispatch; keeping the isolate fixed gives an exact overlap.
    """
    c, s = (1-t*t)/(1+t*t), 2*t/(1+t*t)
    u, w = (Q3(F(1)), Q3()), (Q3(c), Q3(s))
    grid = [(i, j) for i in range(7) for j in range(7)
            if not (2 <= i <= 4 and 2 <= j <= 4)]
    core = [(Q3(F(i)), Q3(F(j))) if i < 6 else
            (Q3(F(5))+w[0], Q3(F(j))+w[1]) for i, j in grid]
    z = (Q3(F(1)+t/10, F(1, 2)), Q3(F(7, 2)))
    points = core + [z]
    assert len(core) == 40
    contacts = set()
    for i, j in combinations(range(41), 2):
        diff = (norm2(minus(points[i], points[j]))-1).sign()
        assert diff >= 0, (t, "ring source overlap", i, j)
        if not diff:
            contacts.add((i, j))
    expected = {(i, j) for i, j in combinations(range(40), 2)
                if sum(abs(a-b) for a, b in zip(grid[i], grid[j])) == 1}
    assert contacts == expected and len(contacts) == 60
    label = [int(1 <= i <= 5) for i, _ in grid] + [1]
    lower = {e for e in contacts if (grid[e[0]][0] >= 1)
             != (grid[e[1]][0] >= 1)}
    upper = {e for e in contacts if (grid[e[0]][0] >= 6)
             != (grid[e[1]][0] >= 6)}
    assert len(lower) == len(upper) == 7
    assert all(grid[i][0] == 0 and grid[j][0] == 1 for i, j in lower)
    assert all(grid[i][0] == 5 and grid[j][0] == 6 for i, j in upper)
    delta = minus(w, u)
    moved = [plus(p, delta) if label[i] else p
             for i, p in enumerate(points)]
    left = grid.index((1, 3))
    assert (norm2(minus(moved[left], z))-1).sign() < 0
    for i, j in combinations(range(41), 2):
        diff = (norm2(minus(moved[i], moved[j]))-1).sign()
        assert diff >= 0, (t, "dispatched overlap", i, j)
        if (i, j) in contacts:
            assert diff == 0
    # Every core vertex on the sixteen-edge central boundary moves, exactly
    # as the geometrically assigned isolate does.
    face = [i for i, (x, y) in enumerate(grid)
            if ((x in (1, 5) and 1 <= y <= 5) or
                (y in (1, 5) and 1 <= x <= 5))]
    assert len(face) == 16 and all(label[i] for i in face)


def main():
    for k in range(1, 101):
        check(F(1, 1000*k))
    print("PASS: 100 exact seven-point source packets; 2100 old distances;")
    print("800 preserved contacts; 100 lower-cut rhombus overlaps;")
    print("100 upper-cut rhombi retain strict short-diagonal feasibility.")
    for m in range(1, 17):
        for n in range(1, 17):
            check_boundary(m, n)
    print("256 integer complete-crosscut patterns; 8704 perimeter-only boundary arcs.")
    for k in range(1, 21):
        check_face_dispatch(F(1, 1000*k))
    print("20 exact 41-point face-dispatch repairs; 16400 initial pair checks;")
    print("1200 old contacts preserved and all 16400 endpoint pairs feasible.")
    print("Arithmetic: Q(sqrt(3)); global optimality and KKT omitted.")


if __name__ == "__main__":
    main()
