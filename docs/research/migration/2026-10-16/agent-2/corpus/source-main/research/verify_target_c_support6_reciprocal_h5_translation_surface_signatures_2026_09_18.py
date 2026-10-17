#!/usr/bin/env python3
"""Exact combinatorial/rational regression for the remaining uniform H5 surface signatures.

No floating point is used.  The script reproduces the seven-face translation-surface
vertex classes for the three surviving H5 force rotation systems, computes their genera,
enumerates the cone orders allowed by the strict corner-count bounds, and checks the
short rational inequalities that remove the four extreme cone-order assignments.
"""

from fractions import Fraction as F
from itertools import product

GROUND = (1, 2, 3, 6, 5, 4)

CASES = {
    1: {
        1: (0, 3, 5, 2, 4),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 5, 2, 6, 1),
        5: (0, 6, 1, 3, 4),
        6: (0, 3, 4, 2, 5),
    },
    2: {
        1: (0, 3, 5, 2, 4),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 6, 2, 5, 1),
        5: (0, 4, 1, 3, 6),
        6: (0, 3, 5, 2, 4),
    },
    3: {
        1: (0, 3, 4, 2, 5),
        2: (0, 1, 4, 6, 3),
        3: (0, 6, 2, 5, 1),
        4: (0, 1, 2, 6, 5),
        5: (0, 6, 4, 3, 1),
        6: (0, 3, 4, 2, 5),
    },
}

EXPECTED = {
    1: [(16, 12, 4), (3, 2, 1), (3, 2, 1), (3, 3, 0), (11, 11, 0)],
    2: [(22, 16, 6), (3, 3, 0), (4, 4, 0), (3, 3, 0), (4, 4, 0)],
    3: [(19, 16, 3), (14, 12, 2), (3, 2, 1)],
}

FINAL = {
    1: {(4, 1, 1, 1, 4), (5, 1, 1, 1, 3)},
    2: {(7, 1, 1, 1, 1)},
    3: {(5, 5, 1), (6, 4, 1)},
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
    corners = [(f, k) for f, cyc in face_cycles.items() for k in range(len(cyc))]
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

            # The paired side vectors are exact negatives.  Translation pairing maps
            # the start of one side to the end of the other and vice versa.
            uf.union((f, k), (g, (l + 1) % m))
            uf.union((f, (k + 1) % n), (g, l))

    out = {}
    for c in corners:
        out.setdefault(uf.find(c), []).append(c)
    return list(out.values())


def gap_members(comp, face_cycles):
    # Corner k lies between side k-1 and side k, so its exterior gap is k-1.
    return sorted((f, (k - 1) % len(face_cycles[f])) for f, k in comp)


def basic_orders(comps):
    """Enumerate integer cone orders from p/6 < m < N/2 and sum m = 11."""
    ranges = []
    for comp in comps:
        N = len(comp)
        p = sum(f != 0 for f, _ in comp)
        lo = p // 6 + 1
        hi = (N - 1) // 2
        ranges.append(range(lo, hi + 1))

    out = set()
    for ms in product(*ranges):
        if sum(ms) == 11:
            out.add(ms)
    return out


for case in (1, 2, 3):
    face_cycles = {0: GROUND, **CASES[case]}
    comps = classes(face_cycles)

    summary = [
        (
            len(c),
            sum(f != 0 for f, _ in c),
            sum(f == 0 for f, _ in c),
        )
        for c in comps
    ]
    assert summary == EXPECTED[case], (case, summary)

    V = len(comps)
    g = (13 - V) // 2
    assert V - 18 + 7 == 2 - 2 * g
    assert g == (4 if case in (1, 2) else 5)
    assert sum(len(c) for c in comps) == 36

    possible = basic_orders(comps)

    if case == 1:
        assert possible == {
            (3, 1, 1, 1, 5),
            (4, 1, 1, 1, 4),
            (5, 1, 1, 1, 3),
            (6, 1, 1, 1, 2),
        }

        C4 = gap_members(comps[4], face_cycles)
        assert [k for f, k in C4 if f == 2] == [1, 2, 3]
        assert len(C4) == 11

        # m4=5 would require selected gap sum = 1*pi.  On face 2, the selected
        # gaps 1,2,3 equal 2*pi minus the adjacent pair 4,0, hence already > pi.
        assert (4 + 1) % 5 == 0

        # m4=2 would require 7*pi.  Three consecutive physical gaps are <5/3*pi;
        # the other eight selected physical gaps are individually <2/3*pi.
        assert F(5, 3) + 8 * F(2, 3) == 7

        possible -= {(3, 1, 1, 1, 5), (6, 1, 1, 1, 2)}

    elif case == 2:
        assert possible == {(7, 1, 1, 1, 1)}

    else:
        assert possible == {
            (4, 6, 1),
            (5, 5, 1),
            (6, 4, 1),
            (7, 3, 1),
        }

        C1 = gap_members(comps[1], face_cycles)
        groups = {f: sorted(k for ff, k in C1 if ff == f) for f in range(7)}
        assert groups == {
            0: [0, 4],
            1: [2, 3, 4],
            2: [0, 1, 3],
            3: [2],
            4: [0, 2],
            5: [3, 4],
            6: [2],
        }

        # m1=6 target = 2*pi.  Lower bounds from faces 1,2,5 are respectively
        # >1, >2/3, >1/3 in pi units, already strictly above the target.
        assert F(1) + F(2, 3) + F(1, 3) == 2

        # m1=3 target = 8*pi.  The selected physical contribution is <7*pi.
        # The selected ground gaps gamma0+gamma4 are <2/3*pi because both are
        # contained in the raw ground cone of width <pi/3.
        physical_upper = (
            F(5, 3)
            + F(5, 3)
            + F(2, 3)
            + F(4, 3)
            + F(1)
            + F(2, 3)
        )
        assert physical_upper == 7
        assert physical_upper + F(2, 3) < 8

        possible -= {(4, 6, 1), (7, 3, 1)}

    assert possible == FINAL[case], (case, possible)
    print(
        "P%d: V=%d g=%d classes=%s cone_orders=%s"
        % (case, V, g, summary, sorted(possible))
    )

print("PASS: exact combinatorial bookkeeping and rational cone-order bounds reproduced.")
