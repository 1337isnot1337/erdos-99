#!/usr/bin/env python3
"""Exact combinatorial/rational regression for the P1 H(3,3) exclusion.

The analytic adjacent-two-turn lower lemma is proved in the companion note. This
script independently reconstructs the P1 translation-surface corner classes from
its force cycles, checks the two cone equations used by the proof, and verifies the
exact rational lower-bound arithmetic. No floating point is used.
"""

from fractions import Fraction as F

GROUND = (1, 2, 3, 6, 5, 4)
P1 = {
    1: (0, 3, 5, 2, 4),
    2: (0, 1, 4, 6, 3),
    3: (0, 6, 2, 5, 1),
    4: (0, 5, 2, 6, 1),
    5: (0, 6, 1, 3, 4),
    6: (0, 3, 4, 2, 5),
}


def edge(a, b):
    return tuple(sorted((a, b)))


class UF:
    def __init__(self, xs):
        self.p = {x: x for x in xs}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[b] = a


def classes(face_cycles):
    corners = [
        (f, k)
        for f, cyc in face_cycles.items()
        for k in range(len(cyc))
    ]
    uf = UF(corners)
    seen = set()

    for f, cyc in face_cycles.items():
        n = len(cyc)
        for k, g in enumerate(cyc):
            e = edge(f, g)
            if e in seen:
                continue
            seen.add(e)
            other = face_cycles[g]
            l = other.index(f)
            m = len(other)
            uf.union((f, k), (g, (l + 1) % m))
            uf.union((f, (k + 1) % n), (g, l))

    out = {}
    for c in corners:
        out.setdefault(uf.find(c), []).append(c)
    return list(out.values())


def gaps(comp, face_cycles):
    # Corner k lies between side k-1 and side k, so its exterior gap is k-1.
    return sorted(
        (f, (k - 1) % len(face_cycles[f]))
        for f, k in comp
    )


face_cycles = {0: GROUND, **P1}
comps = classes(face_cycles)
summary = [
    (
        len(c),
        sum(f != 0 for f, _ in c),
        sum(f == 0 for f, _ in c),
    )
    for c in comps
]
assert summary == [
    (16, 12, 4),
    (3, 2, 1),
    (3, 2, 1),
    (3, 3, 0),
    (11, 11, 0),
]

# For signature (4,1,1,1,4), C3 and C4 have exactly these selected gaps.
C3 = gaps(comps[3], face_cycles)
C4 = gaps(comps[4], face_cycles)
assert C3 == [(1, 1), (3, 3), (5, 2)]
assert C4 == [
    (1, 2),
    (2, 1), (2, 2), (2, 3),
    (3, 2),
    (4, 1), (4, 2),
    (5, 1), (5, 3),
    (6, 2), (6, 3),
]

# A cone class with N corners and cone order m has selected exterior-gap sum
# (N-2m)*pi.  Thus C3 targets 1*pi and C4 targets 3*pi.
assert F(len(comps[3]) - 2 * 1) == 1
assert F(len(comps[4]) - 2 * 4) == 3

# The companion proof lower-bounds the six groups in C4, in units of pi:
#   d12+d32 > 1/3+d52,
#   face-2 triple > 1,
#   face-4 adjacent pair > 2/3,
#   d51+d53 > 1-d52,
#   face-6 adjacent pair > 2/3.
# The d52 terms cancel exactly.
lower = F(1, 3) + F(1) + F(2, 3) + F(1) + F(2, 3)
assert lower == F(11, 3)
assert lower > F(3)

print("P1 classes:", summary)
print("C3 gaps:", C3, "target=1*pi")
print("C4 gaps:", C4, "target=3*pi")
print("strict C4 lower:", lower, "* pi")
print("PASS: exact P1 H(3,3) cone bookkeeping gives 11/3*pi > 3*pi")
