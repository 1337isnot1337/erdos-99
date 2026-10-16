#!/usr/bin/env python3
"""Arithmetic/combinatorial checks for the sharp five-row k=2,p=3 reduction.

The mathematical input is the already-certified five-row k=2 slack-two
containment theorem. This script checks the equality arithmetic and the
seven-coordinate touch-support consequences used by the companion note.
"""
from itertools import combinations

# Low-singleton-generated case. The previous theorem gives
# D >= 5 + p + 3*d - 3*q, with d>=1 and q<=p.
p = 3
solutions = []
for d in range(1, 8):
    for q in range(0, p + 1):
        lb = 5 + p + 3 * d - 3 * q
        if lb <= 2:
            solutions.append((d, q, lb))
assert solutions == [(1, 3, 2)]

# If q=3 canonical-complete blocks become incomplete while p=3 total rows
# are selected on incomplete blocks, all three changed blocks must be
# singletons. The only positive integer partition of 3 into >=3 parts is
# 1+1+1.
parts = []
for a in range(1, 4):
    for b in range(a, 4):
        for c in range(b, 4):
            if a + b + c == 3:
                parts.append((a, b, c))
assert parts == [(1, 1, 1)]

# In the complementary case, P is not obtainable with <=2 singleton blocks.
# Any p=3 realization therefore must have at least three singleton blocks;
# again the only possible cost pattern is 1+1+1, so no two-row pair can occur.
# Enumerate the possible p=3 incomplete-state cost multisets (costs 1 or 2).
cost_patterns = set()
for n1 in range(4):
    for n2 in range(3):
        if n1 + 2 * n2 == 3:
            cost_patterns.add((n1, n2))
assert cost_patterns == {(3, 0), (1, 1)}
assert [pat for pat in cost_patterns if pat[0] >= 3] == [(3, 0)]

# Seven-row consequence: for any two nonempty touch supports S,T in [7],
# there is a two-coordinate deletion that leaves both blocks touched.
U = tuple(range(7))
pairs = tuple(combinations(U, 2))
subsets = []
for mask in range(1, 1 << 7):
    subsets.append(frozenset(i for i in U if (mask >> i) & 1))
for S in subsets:
    for T in subsets:
        assert any(
            not S.issubset(frozenset(D)) and not T.issubset(frozenset(D))
            for D in pairs
        )

# A block remains touched after every two-coordinate deletion iff it is
# touched by at least three of the seven no-root rows.
for S in subsets:
    survives_all = all(not S.issubset(frozenset(D)) for D in pairs)
    assert survives_all == (len(S) >= 3)

print("PASS: sharp five-row k=2,p=3 singleton reduction arithmetic")
print("low_generated_equality", {"d": 1, "q": 3, "p": 3})
print("sharp_incomplete_cost_pattern", "three singletons")
print("seven_row_singleton_touch_minimum", 3)
