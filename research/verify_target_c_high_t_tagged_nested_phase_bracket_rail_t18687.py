#!/usr/bin/env python3
"""Regression checks for the tagged nested rail with fused local ladders."""

import math
from fractions import Fraction

c0 = Fraction(113, 20_000_000)
r = Fraction(817, 1250)  # 0.6536
sigma = Fraction(1, 100)
mu = Fraction(1, 100)
outer_eta = Fraction(1, 2)
sqrt3 = math.sqrt(3.0)
Cphase = math.pi**2 * sqrt3 * (2.0 + sqrt3) / 12.0

# Parent full tagged rail after one birth-host choice.
parent_rail = c0 / 2
assert parent_rail == Fraction(113, 40_000_000)
assert abs(float(parent_rail) - 2.825e-6) < 1e-18

# Half-retention under local phase/bracket averaging.
fused_rail = (1 - outer_eta) * parent_rail
assert fused_rail == c0 / 4
assert fused_rail == Fraction(113, 80_000_000)
assert abs(float(fused_rail) - 1.4125e-6) < 1e-18

# One mechanism tag, or one physical destination, costs one further factor two.
one_split = fused_rail / 2
assert one_split == c0 / 8
assert one_split == Fraction(113, 160_000_000)
assert abs(float(one_split) - 7.0625e-7) < 1e-18

# Fixing both physical destination and mechanism costs two factors two.
two_splits = fused_rail / 4
assert two_splits == c0 / 16
assert two_splits == Fraction(113, 320_000_000)
assert abs(float(two_splits) - 3.53125e-7) < 1e-18

# Local fused-ladder dimensions.
parent_columns = r - sigma
assert parent_columns == Fraction(1609, 2500)  # 0.6436
q = float(parent_columns) - (1.0 + 2.0 * float(mu)) / sqrt3
assert 0.0547027 < q < 0.0547028

K = 2.0 * Cphase / (
    float(outer_eta) * float(parent_rail) * float(sigma)
)
assert abs(K - 800.0 * Cphase / float(c0)) < 1e-4
assert 7.52e8 < K < 7.54e8

# Optional fixed-gap robust refinement on the already fused rail.
rho = c0 / 16
robust_after_narrow = fused_rail / 2 - rho
assert robust_after_narrow == c0 / 16
assert robust_after_narrow == two_splits

# More generally, if a fused rail has density F and at most 2*rho narrow EA
# positions, then max(TB1, wide-EA) >= F/2-rho.
for F_num in range(10, 80):
    F = Fraction(F_num, 1000)
    for rho_num in range(0, F_num // 2):
        rr = Fraction(rho_num, 2000)
        lower = F / 2 - rr
        if lower < 0:
            continue
        # Sweep all rational TB1 densities on a fine grid. EA_total is the rest;
        # wide EA is worst-case EA_total-2rho, truncated at zero.
        for t_num in range(F_num + 1):
            T = Fraction(t_num, 1000)
            if T > F:
                continue
            E = F - T
            Ew = max(Fraction(0), E - 2 * rr)
            assert max(T, Ew) >= lower

# Subsequence thinning preserves strict order and strict nesting. Model supports
# as intervals [birth, death] with strictly increasing births and nonincreasing
# deaths. Any increasing-index subsequence retains both properties.
for n in range(2, 30):
    births = list(range(n))
    deaths = list(reversed(range(n, 2 * n)))
    # I_s = {birth_s+1,...,death_s}; these are strictly nested.
    supports = [set(range(b + 1, d + 1)) for b, d in zip(births, deaths)]
    for s in range(n - 1):
        assert supports[s] > supports[s + 1]
    # Check many deterministic thinnings.
    masks = [1, (1 << n) - 1]
    if n <= 15:
        masks.extend(range(1, 1 << n, max(1, (1 << n) // 97)))
    else:
        masks.extend([
            sum(1 << j for j in range(n) if j % k == 0)
            for k in range(2, 8)
        ])
    for mask in masks:
        idx = [j for j in range(n) if (mask >> j) & 1]
        for a, b in zip(idx, idx[1:]):
            assert births[a] < births[b]
            assert deaths[a] > deaths[b]
            assert supports[a] > supports[b]

# Common-order flank intersection for the two adjacent rows.
for M in range(5, 80):
    order = list(range(M))
    for Q in range(1, M + 1):
        # It is enough to check extremal initial/suffix lengths Q and M and a
        # mid value; arbitrary lengths obey the same monotonicity.
        lengths = sorted(set([Q, (Q + M) // 2, M]))
        for a in lengths:
            for b in lengths:
                assert set(order[:Q]).issubset(
                    set(order[:a]).intersection(order[:b])
                )
                assert set(order[-Q:]).issubset(
                    set(order[-a:]).intersection(order[-b:])
                )

print("PASS: tagged nested phase/bracket rail regressions")
print("parent tagged rail density =", float(parent_rail))
print("fused nested rail density =", float(fused_rail))
print("one destination or one tag density =", float(one_split))
print("destination + tag density =", float(two_splits))
print("phase-pure parent column density =", float(parent_columns))
print("mu=0.01 flank density =", q)
print("phase coefficient K =", K)
print("rho=c0/16 robust density =", float(robust_after_narrow))
