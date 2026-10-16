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


def main():
    for k in range(1, 101):
        check(F(1, 1000*k))
    print("PASS: 100 exact seven-point source packets; 2100 old distances;")
    print("800 preserved contacts; 100 lower-cut rhombus overlaps;")
    print("100 upper-cut rhombi retain strict short-diagonal feasibility.")
    print("Arithmetic: Q(sqrt(3)); global optimality and KKT omitted.")


if __name__ == "__main__":
    main()
