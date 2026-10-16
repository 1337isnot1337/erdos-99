#!/usr/bin/env python3
"""Exact S1 obstruction for nine-no-root k=5,D=-1,d_root=0,p=5.

Support S1 is [0123]^3 [0124]^3 [0134]^3, so all three orientations
occur on each tetrahedral support. The LOCAL table is the resulting exact
local quotient-component table in the committed Target-C normal form.
All rank calculations below are over Q using Fraction arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

EXTERNAL = (
    "1234", "1243", "1324", "1235", "1253", "1325", "1245", "1254", "1425"
)
LOCAL = {
    "012": ((1,0),(-1,1),(0,1),(1,0),(-1,1),(0,1),(0,0),(0,0),(0,0)),
    "013": ((-1,1),(1,0),(0,-1),(0,0),(0,0),(0,0),(1,0),(-1,1),(0,1)),
    "014": ((0,0),(0,0),(0,0),(-1,1),(1,0),(0,-1),(-1,1),(1,0),(0,-1)),
    "023": ((0,-1),(-1,0),(-1,1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)),
    "024": ((0,0),(0,0),(0,0),(0,-1),(-1,0),(-1,1),(0,0),(0,0),(0,0)),
    "034": ((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,-1),(-1,0),(-1,1)),
    "123": ((1,0),(0,1),(1,-1),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)),
    "124": ((0,0),(0,0),(0,0),(1,0),(0,1),(1,-1),(0,0),(0,0),(0,0)),
    "134": ((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0),(0,1),(1,-1)),
}
TOUCHED = tuple(LOCAL)
assert len(EXTERNAL) == 9 and len(TOUCHED) == 9

EXPECTED_TOUCHED = (
    frozenset(("012", "013", "023", "123")),
    frozenset(("012", "013", "023", "123")),
    frozenset(("012", "013", "023", "123")),
    frozenset(("012", "014", "024", "124")),
    frozenset(("012", "014", "024", "124")),
    frozenset(("012", "014", "024", "124")),
    frozenset(("013", "014", "034", "134")),
    frozenset(("013", "014", "034", "134")),
    frozenset(("013", "014", "034", "134")),
)
for i in range(9):
    got = frozenset(b for b in TOUCHED if LOCAL[b][i] != (0, 0))
    assert got == EXPECTED_TOUCHED[i], (i, EXTERNAL[i], got)


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def empty_rows(block):
    vals = LOCAL[block]
    return (tuple(v[0] for v in vals), tuple(v[1] for v in vals))


assert all(rank(empty_rows(b)) == 2 for b in TOUCHED)
triple_census = Counter()
for S in combinations(TOUCHED, 3):
    triple_census[rank([row for b in S for row in empty_rows(b)])] += 1
assert triple_census == Counter({5: 28, 6: 56}), triple_census
assert min(triple_census) == 5

edges = tuple(combinations(range(7), 2))
edge_index = {e: i for i, e in enumerate(edges)}


def hrow(label):
    a, b, c = map(int, label)
    row = [0] * len(edges)
    row[edge_index[(b, c)]] = 1
    row[edge_index[(a, c)]] = -1
    row[edge_index[(a, b)]] = 1
    return tuple(row)


rank_HT = rank([hrow(b) for b in TOUCHED])
assert rank_HT == 6
max_complete = rank_HT - 5
assert max_complete == 1
min_empty = len(TOUCHED) - max_complete - 5
assert min_empty == 3
assert min_empty > 2

print("PASS: S1 is impossible in nine-no-root k=5,D=-1,d_root=0,p=5")
print("touched_blocks", len(TOUCHED))
print("rank_H_T", rank_HT)
print("triple_empty_span_rank_census", dict(sorted(triple_census.items())))
print("max_complete_blocks", max_complete)
print("min_empty_blocks", min_empty)
