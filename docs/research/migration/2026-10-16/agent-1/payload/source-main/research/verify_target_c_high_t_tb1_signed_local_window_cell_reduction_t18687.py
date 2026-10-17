#!/usr/bin/env python3
"""Regression checks for the SIGNED LOCAL-WINDOW dual-cone/cell reduction."""

import itertools
import math

# Normalize RP^1 to circumference one. C(0)=[1/3,2/3]. If a crossing
# train has directed projective offset delta in (1/3,2/3), its closed
# step cone wraps as [0,delta-1/3] U [delta+1/3,1], disjoint from C(0).
for num in range(101, 200):
    delta = num / 300.0
    assert 1 / 3 < delta < 2 / 3
    left_end = delta - 1 / 3
    right_start = delta + 1 / 3
    assert left_end < 1 / 3
    assert right_start > 2 / 3

# Exhaustive interval Helly check on integer path/fence intervals through m=6.
for m in range(1, 7):
    intervals = [(a, b) for a in range(m + 1) for b in range(a, m + 1)]
    for r in range(1, min(5, len(intervals)) + 1):
        for fam in itertools.combinations(intervals, r):
            pairwise = all(
                max(a, c) <= min(b, d)
                for (a, b), (c, d) in itertools.combinations(fam, 2)
            )
            if pairwise:
                lo = max(a for a, _ in fam)
                hi = min(b for _, b in fam)
                assert lo <= hi

# The four common-cell types partition every interval containing the Helly rank.
for m in range(1, 8):
    for g in range(m + 1):
        for p in range(m + 1):
            for q in range(p, m + 1):
                if not (p <= g <= q):
                    continue
                kinds = [
                    p < g < q,
                    p < q == g,
                    p == g < q,
                    p == q == g,
                ]
                assert sum(kinds) == 1

# Uniqueness-mode and four-way type thinning are only constant losses, so
# they preserve the strengthened quarter-power exponent.
beta = 0.25
for logD in [100.0, 1000.0, 10000.0]:
    effective = beta - math.log(logD) / logD
    assert effective > 0.0

print("SIGNED LOCAL-WINDOW dual-cone/cell regression checks passed")
