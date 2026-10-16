#!/usr/bin/env python3
"""Regression checks for the THIN ROW-UNIQUE order-stabilization note."""

import itertools
import math


def largest_block(H, marked_rows, marked_gaps):
    """Rows are 0..H-1, gaps are 0..H-2 between j and j+1."""
    best = cur = 0
    for j in range(H):
        if j in marked_rows:
            cur = 0
            continue
        if j > 0 and (j - 1) in marked_gaps:
            cur = 0
        cur += 1
        best = max(best, cur)
    return best


# Exhaust the row/gap slot combinatorics for small H and mark budgets C.
for H in range(1, 9):
    slots = [("r", j) for j in range(H)] + [("g", j) for j in range(H - 1)]
    for C in range(0, min(4, len(slots)) + 1):
        lower = (H - C) / (C + 1)
        for chosen in itertools.combinations(slots, C):
            rows = {j for kind, j in chosen if kind == "r"}
            gaps = {j for kind, j in chosen if kind == "g"}
            assert largest_block(H, rows, gaps) + 1e-12 >= lower

# Diagonal Ramsey bound used in RS.6-RS.7.
for K in range(2, 10000):
    r = math.floor(0.5 * math.log2(K)) + 1
    assert math.comb(2 * r - 2, r - 1) <= K
    assert 4 ** (r - 1) <= K

# Polylogarithmic loss preserves the half exponent.
prev = 0.0
for D in [10.0**20, 10.0**40, 10.0**80, 10.0**160]:
    H = D ** 0.5
    K = math.log(D)
    C = K * K
    reduced = (H - C) / (C + 1.0)
    exponent = math.log(reduced) / math.log(D)
    assert exponent > 0.32
    assert exponent > prev
    prev = exponent

print("THIN ROW-UNIQUE order-stabilization regression checks passed")
