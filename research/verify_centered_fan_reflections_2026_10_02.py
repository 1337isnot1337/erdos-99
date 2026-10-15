#!/usr/bin/env python3
"""Exact full-source fan-reflection packets over Q(sqrt(4D**2-1)).

Encodes actual diameter, unit separation, old contacts, actual fan carriers,
three independent internal leaves, every old/new pair, solo/joint lower
failure labels, and one isolate-following repair. These are nonglobal finite
packets; canonical KKT, source minimality, a large fan population, and universal
inactive-blocker repair are omitted. See the dated proof report and README.
"""
from dataclasses import dataclass
from fractions import Fraction as F

D = 100
RADICAND = 4 * D * D - 1


@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(F(x))

    def __add__(self, other):
        other = Q.of(other)
        return Q(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + -Q.of(other)

    def __rsub__(self, other):
        return Q.of(other) - self

    def __mul__(self, other):
        other = Q.of(other)
        return Q(self.a * other.a + RADICAND * self.b * other.b,
                 self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * F(1, other)

    def sign(self):
        if not self.b:
            return (self.a > 0) - (self.a < 0)
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        delta = self.a * self.a - RADICAND * self.b * self.b
        if not delta:
            return 0
        return ((self.a > 0) - (self.a < 0)) * ((delta > 0) - (delta < 0))


def sub(p, q):
    return tuple(x - y for x, y in zip(p, q))


def add(p, q):
    return tuple(x + y for x, y in zip(p, q))


def squared(p, q):
    r = sub(p, q)
    return sum((x * x for x in r), Q())


def rotation(p, sign=1):
    co = Q(F(2 * D * D - 1, 2 * D * D))
    si = Q(F(0), F(sign, 2 * D * D))
    x, y = p
    return co * x - si * y, si * x + co * y


def packet(blocked, chain=False):
    origin = Q(), Q()
    points = {"carrier": origin, 0: (Q(F(D)), Q())}
    for i in range(1, 5):
        points[i] = rotation(points[i - 1])
        points[-i] = rotation(points[-i + 1], -1)
    if blocked:
        points["isolate"] = Q(F(D) - 1 - F(1, 2 * D)), Q()
    if chain:
        assert blocked
        points["next_isolate"] = Q(F(D) - 2 - F(1, D)), Q()
    return points


SELECTED = {-2, 0, 2}


def reflected(points, selected):
    return {i: tuple(x * (1 - F(1, D * D)) for x in p)
            if i in selected else p for i, p in points.items()}


def pair_lengths(points):
    keys = list(points)
    return {(a, b): squared(points[a], points[b])
            for i, a in enumerate(keys) for b in keys[i + 1:]}


def verify(blocked, chain=False):
    old = packet(blocked, chain)
    old_lens = pair_lengths(old)
    assert all((x - 1).sign() >= 0 for x in old_lens.values())
    assert max((x - D * D).sign() for x in old_lens.values()) == 0
    contacts = {pair for pair, x in old_lens.items() if x == Q(F(1))}
    assert {frozenset(e) for e in contacts} == {frozenset((i, i + 1)) for i in range(-4, 4)}
    diameter_pairs = {pair for pair, x in old_lens.items() if x == Q(F(D * D))}
    assert len(diameter_pairs) == 9
    center = Q(F(D, 2)), Q()
    for i in SELECTED:
        midpoint = tuple(x / 2 for x in old[i])
        assert (squared(midpoint, center) - 16).sign() < 0
        assert sum(i in pair for pair in contacts) == 2

    joint = reflected(old, SELECTED)
    new_lens = pair_lengths(joint)
    assert all((new_lens[e] - old_lens[e]).sign() <= 0 for e in old_lens)
    assert all(new_lens[e] == Q(F(1)) for e in contacts)
    assert sum(x == Q(F(D * D)) for x in new_lens.values()) == 6
    for e, x in new_lens.items():
        if all(v in SELECTED for v in e):
            assert (x - 1).sign() > 0
    failed_joint = {e for e, x in new_lens.items() if (x - 1).sign() < 0}
    unary_failures = set()
    blockers = {}
    for i in SELECTED:
        solo = pair_lengths(reflected(old, {i}))
        failures = {e for e, x in solo.items() if (x - 1).sign() < 0}
        unary_failures |= failures
        blockers[i] = {e[1] if e[0] == i else e[0] for e in failures}
    assert failed_joint == unary_failures
    for i in SELECTED:
        for j in SELECTED - {i}:
            assert not (blockers[i] & blockers[j])
    if blocked:
        assert failed_joint == {(0, "isolate")}
        assert old_lens[0, "isolate"] == Q((1 + F(1, 2 * D)) ** 2)
        assert new_lens[0, "isolate"] == Q((1 - F(1, 2 * D)) ** 2)
        repaired = dict(joint)
        repaired["isolate"] = add(old["isolate"], sub(joint[0], old[0]))
        repaired_lens = pair_lengths(repaired)
        if chain:
            assert {e for e, x in repaired_lens.items() if (x - 1).sign() < 0} == {
                ("isolate", "next_isolate")}
            assert all((x - D * D).sign() <= 0 for x in repaired_lens.values())
            repaired["next_isolate"] = add(old["next_isolate"], sub(joint[0], old[0]))
            repaired_lens = pair_lengths(repaired)
        assert all((x - 1).sign() >= 0 for x in repaired_lens.values())
        assert all((x - D * D).sign() <= 0 for x in repaired_lens.values())
        assert {e for e, x in repaired_lens.items() if x == Q(F(1))} == contacts
        assert sum(x == Q(F(D * D)) for x in repaired_lens.values()) == 6
    else:
        assert not failed_joint
    # Explicit smaller same-cardinality competitor: take the first n points
    # of a 3-by-4 integer grid (diameter squared at most 13).
    assert len(old) <= 12 and 13 < D * D
    return len(old_lens)


def main():
    pairs = verify(False) + verify(True) + verify(True, True)
    # Uniform finite lens margin used in the uniqueness proof.
    assert F(28, 15) - F(1, 10) > F(7, 4)
    assert F(7, 4) ** 2 > 3
    print(f"PASS: {pairs} exact old/joint pair certificates; solo/joint "
          "factorization; distinct blocker labels; isolate repair and exact "
          "collision-transfer regression")
    print("OMITTED: global optimality/KKT; universal repair; fan extraction; Level I")


if __name__ == "__main__":
    main()
