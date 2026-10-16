#!/usr/bin/env python3
"""Regression checks for the high-t local phase/bracket fusion theorem."""

import math
from fractions import Fraction

sqrt3 = math.sqrt(3.0)
r = Fraction(817, 1250)  # 0.6536
c0 = Fraction(113, 20_000_000)
Cphase = math.pi**2 * sqrt3 * (2.0 + sqrt3) / 12.0

# ---------------------------------------------------------------------------
# 1. Exact robust-fork bookkeeping for rho=c0/4 and outer retention eta=1/2.
# ---------------------------------------------------------------------------
rho = c0 / 4
robust_union = c0 - 2 * rho
assert robust_union == c0 / 2

outer_eta = Fraction(1, 2)
robust_fused = (1 - outer_eta) * robust_union
assert robust_fused == c0 / 4
assert robust_fused == Fraction(113, 80_000_000)

one_mechanism = robust_fused / 2
assert one_mechanism == c0 / 8
assert one_mechanism == Fraction(113, 160_000_000)
assert abs(float(robust_fused) - 1.4125e-6) < 1e-18
assert abs(float(one_mechanism) - 7.0625e-7) < 1e-18

# ---------------------------------------------------------------------------
# 2. Concrete sigma=mu=0.01 flank density and local phase constants.
# ---------------------------------------------------------------------------
sigma = Fraction(1, 100)
mu = Fraction(1, 100)
parent_density = r - sigma
assert parent_density == Fraction(1609, 2500)  # 0.6436

q = float(parent_density) - (1.0 + 2.0 * float(mu)) / sqrt3
assert 0.05470 < q < 0.05471

# K = 2*Cphase/(eta*gamma*sigma).
Krob = 2.0 * Cphase / (
    float(outer_eta) * float(robust_union) * float(sigma)
)
# Algebraically this is 800*Cphase/c0.
assert abs(Krob - 800.0 * Cphase / float(c0)) < 1e-4
assert 7.5e8 < Krob < 7.54e8

# Current displayed deep-force density is 0.96*c0.
deep_density = Fraction(24, 25) * c0
assert abs(float(deep_density) - 5.424e-6) < 1e-18
deep_fused = (1 - outer_eta) * deep_density
assert deep_fused == Fraction(12, 25) * c0
assert abs(float(deep_fused) - 2.712e-6) < 1e-18

Kdeep = 2.0 * Cphase / (
    float(outer_eta) * float(deep_density) * float(sigma)
)
assert 3.8e8 < Kdeep < 3.93e8

# ---------------------------------------------------------------------------
# 3. Adjacent-interface charging multiplicity is at most two.
# A row j occurs only in interface j-1 and interface j.
# ---------------------------------------------------------------------------
for n_rows in range(2, 100):
    counts = [0] * n_rows
    for i in range(n_rows - 1):
        counts[i] += 1
        counts[i + 1] += 1
    assert max(counts) <= 2
    assert counts[0] == counts[-1] == 1
    if n_rows >= 3:
        assert all(c == 2 for c in counts[1:-1])

# The same remains true for arbitrary subfamilies of adjacent interfaces.
for n_rows in range(2, 12):
    n_interfaces = n_rows - 1
    for mask in range(1 << n_interfaces):
        counts = [0] * n_rows
        for i in range(n_interfaces):
            if (mask >> i) & 1:
                counts[i] += 1
                counts[i + 1] += 1
        assert max(counts, default=0) <= 2

# ---------------------------------------------------------------------------
# 4. Markov deletion algebra: S_i <= T and threshold K/D=T/(sigma D)
# imply at most sigma*D bad columns.  Check integer realizations around the
# rounding boundary for many toy D values.
# ---------------------------------------------------------------------------
for D in range(10, 500):
    for sigma_num in range(1, 10):
        sig = sigma_num / 20.0
        # Normalize T=1. A bad column has charge strictly greater than 1/(sig D).
        threshold = 1.0 / (sig * D)
        max_bad = math.floor(sig * D + 1e-12)
        # max_bad+1 bad columns, each strictly above threshold, necessarily exceed T.
        if max_bad + 1 > sig * D:
            lower_total = (max_bad + 1) * threshold
            assert lower_total >= 1.0 - 1e-12

# ---------------------------------------------------------------------------
# 5. Common-order flank extraction. If each of two rows has at least Q labels
# below its threshold, and each below-set is an initial segment of the same
# order, the first Q labels work simultaneously. Likewise for terminal blocks.
# ---------------------------------------------------------------------------
for M in range(4, 70):
    order = list(range(M))
    for Q in range(1, M + 1):
        for low1 in range(Q, M + 1):
            for low2 in range(Q, M + 1):
                common_prefix = set(order[:low1]).intersection(order[:low2])
                assert set(order[:Q]).issubset(common_prefix)
        for high1 in range(Q, M + 1):
            for high2 in range(Q, M + 1):
                common_suffix = set(order[-high1:]).intersection(order[-high2:])
                assert set(order[-Q:]).issubset(common_suffix)

# ---------------------------------------------------------------------------
# 6. Parameter feasibility and nearby margins.
# ---------------------------------------------------------------------------
def flank_density(sig: float, margin: float) -> float:
    return float(r) - sig - (1.0 + 2.0 * margin) / sqrt3

assert flank_density(0.01, 0.01) == q
assert flank_density(0.01, 0.05) > 0.0085
assert flank_density(0.01, 0.055) > 0.0027
assert flank_density(0.01, 0.057) > 0.0004
assert flank_density(0.01, 0.058) < 0.0

print("PASS: high-t local phase/bracket fusion regressions")
print("Cphase =", Cphase)
print("robust fused union density =", float(robust_fused))
print("one robust mechanism density =", float(one_mechanism))
print("phase-pure parent column density =", float(parent_density))
print("mu=0.01 flank density =", q)
print("Krob =", Krob)
print("deep fused exact-force density =", float(deep_fused))
print("Kdeep =", Kdeep)
