#!/usr/bin/env python3
"""Regression checks for dense phase-pure circumcenter-bracketed fixed cusp chains."""

import math
from fractions import Fraction

T = Fraction(18687, 10000)
c = Fraction(113, 5_000_000)  # 0.0000226 row-block density
H = 1_109_000
r0 = Fraction(817, 1250)  # 0.6536
sigma = Fraction(1, 100)
mu = Fraction(1, 100)
sqrt3 = math.sqrt(3.0)
Cphase = math.pi**2 * sqrt3 * (2.0 + sqrt3) / 12.0

# ---------------------------------------------------------------------------
# 1. The augmented full-row defect charge uses exactly the same global
#    constant as the existing fixed-cusp-chain theorem.
# ---------------------------------------------------------------------------
Kglobal = 10.0 * float(T) - 2.0 * math.pi + 2.0 + 2.0 * Cphase
ratio = Kglobal / float(c)
assert ratio < 1_108_000
assert H > 1_108_000
assert H - ratio > 1_000

# Every row defect F_j can enter at most the two adjacent-interface charges
# J_{j-1}^{full}, J_j^{full}.
for n_rows in range(2, 100):
    multiplicity = [0] * n_rows
    for i in range(n_rows - 1):
        multiplicity[i] += 1
        multiplicity[i + 1] += 1
    assert max(multiplicity) <= 2
    assert multiplicity[0] == multiplicity[-1] == 1
    if n_rows > 2:
        assert all(x == 2 for x in multiplicity[1:-1])

# ---------------------------------------------------------------------------
# 2. Intersection loss lemma.
# If |G_j triangle G_{j+1}| <= L_j, then the running intersection loses at
# most sum L_j elements from G_0. Exhaust small set systems.
# ---------------------------------------------------------------------------
for universe_size in range(1, 7):
    subsets = [set(i for i in range(universe_size) if (mask >> i) & 1)
               for mask in range(1 << universe_size)]
    for g0 in subsets:
        for g1 in subsets:
            L0 = len(g0.symmetric_difference(g1))
            inter1 = g0 & g1
            assert len(inter1) >= len(g0) - L0
            for g2 in subsets:
                L1 = len(g1.symmetric_difference(g2))
                inter2 = inter1 & g2
                assert len(inter2) >= len(g0) - L0 - L1

# A deterministic longer-chain version with arbitrary additions/removals.
for n in range(2, 30):
    universe = set(range(4 * n))
    families = [set(range(2 * n))]
    losses = []
    for j in range(n - 1):
        prev = families[-1]
        # Remove up to j+1 old elements and add the same number of new ones.
        rem = set(sorted(prev)[: min(j + 1, len(prev))])
        add = set(range(2 * n + 2 * j, min(4 * n, 2 * n + 2 * j + len(rem))))
        nxt = (prev - rem) | add
        losses.append(len(prev.symmetric_difference(nxt)))
        families.append(nxt)
    common = set.intersection(*families)
    assert len(common) >= len(families[0]) - sum(losses)

# ---------------------------------------------------------------------------
# 3. Column Markov deletion over the whole chain.
# Total chain defect < H*R and threshold H*R/(sigma*D) leave < sigma D bad
# columns. Check the integer boundary for a range of toy D,R.
# ---------------------------------------------------------------------------
for R in range(1, 15):
    total = H * R
    for D in range(20, 400):
        threshold = total / (float(sigma) * D)
        max_allowed = math.floor(float(sigma) * D + 1e-12)
        # max_allowed+1 strictly-bad columns necessarily exceed the budget.
        if max_allowed + 1 > float(sigma) * D:
            assert (max_allowed + 1) * threshold >= total - 1e-7

# ---------------------------------------------------------------------------
# 4. Concrete common-ladder and flank constants.
# ---------------------------------------------------------------------------
parent_density = r0 - sigma
assert parent_density == Fraction(1609, 2500)  # 0.6436
q = float(parent_density) - (1.0 + 2.0 * float(mu)) / sqrt3
assert 0.0547027 < q < 0.0547028

for R in [1, 2, 3, 5, 10, 25, 100]:
    KR = H * R / float(sigma)
    assert KR == 110_900_000 * R

# The retained density remains above the exact one-sided circumdisk capacity.
assert float(parent_density) > 1.0 / sqrt3

# ---------------------------------------------------------------------------
# 5. Common-order flank extraction across arbitrarily many rows.
# If every row has at least Q below-threshold crossings and below-sets are
# initial segments of one common order, then the same first Q columns work on
# every row. Likewise for terminal segments.
# ---------------------------------------------------------------------------
for M in range(4, 80):
    order = list(range(M))
    for rows in range(1, 8):
        for Q in range(1, M + 1):
            # Use several extremal/midpoint initial lengths >= Q.
            choices = sorted(set([Q, (Q + M) // 2, M]))
            lengths = [choices[(j * 2 + rows) % len(choices)] for j in range(rows)]
            prefix_intersection = set(order)
            suffix_intersection = set(order)
            for ell in lengths:
                prefix_intersection &= set(order[:ell])
                suffix_intersection &= set(order[-ell:])
            assert set(order[:Q]).issubset(prefix_intersection)
            assert set(order[-Q:]).issubset(suffix_intersection)

# ---------------------------------------------------------------------------
# 6. Fixed-R finite loss and a model diagonal R_D -> infinity slowly enough
# that H R_D = o(D), while the per-crossing phase defect O(R_D/D) -> 0.
# ---------------------------------------------------------------------------
for D in [10**6, 10**8, 10**10, 10**12]:
    R = max(1, int(D ** 0.25))
    assert H * R / D < H * D ** (-0.75) + H / D
    assert R / D <= D ** (-0.75)

print("PASS: dense phase-bracket fixed cusp-chain regressions")
print("Cphase =", Cphase)
print("global augmented cost constant =", Kglobal)
print("global constant / row density =", ratio)
print("phase-pure common-column density =", float(parent_density))
print("mu=0.01 common flank density =", q)
print("K_R coefficient =", H / float(sigma))
