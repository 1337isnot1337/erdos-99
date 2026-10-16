#!/usr/bin/env python3
"""Regression checks for the unconditional near-maximal-aperture corridor."""

from fractions import Fraction
from math import asin, sin

c = Fraction(113, 5_000_000)
nu = c / 2
c_f = float(c)
nu_f = float(nu)

z0 = 20477 / 10000
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)

assert c == Fraction(113, 5_000_000)
assert nu == Fraction(113, 10_000_000)
assert c_f == 2.26e-5
assert nu_f == 1.13e-5
assert c_f < gammaH / 1000

# Fixed-epsilon algebra:
# rho_eps=(1-eps)c, narrow density <=rho_eps/2=(1-eps)nu,
# so parent density nu leaves eps*nu.
for p in range(1, 100):
    eps = p / 100
    rho = (1 - eps) * c_f
    wide_floor = nu_f - rho / 2
    assert abs(wide_floor - eps * nu_f) < 2e-18
    assert 0 < rho < gammaH

# Exact finite narrow-capacity bound uses delta_D >= 1/D.
for D in (10, 100, 10_000, 1_000_000):
    delta = 2 * asin(1 / (2 * D))
    assert delta >= 1 / D
    for eps in (0.1, 0.5, 0.9):
        rho = (1 - eps) * c_f
        exact_cap = rho / (2 * delta) + 1
        coarse_cap = rho * D / 2 + 1
        assert exact_cap <= coarse_cap + 1e-12

# Hole-free block packing on the wide suffix.
def run_lengths(mask, n):
    out = []
    q = 0
    for i in range(n):
        if (mask >> i) & 1:
            q += 1
        elif q:
            out.append(q)
            q = 0
    if q:
        out.append(q)
    return out

for n in range(1, 13):
    for mask in range(1 << n):
        W = mask.bit_count()
        H = n - W
        runs = run_lengths(mask, n)
        for m in range(1, n + 2):
            K = sum(q // m for q in runs)
            assert K * m >= W - (H + 1) * (m - 1)

# Limiting diagonal constants as epsilon -> 0.
diamond = 0.5 * sin(c_f / 2)
endpoint = sin(c_f / 2)
compression = 2 / sin(c_f)

assert 5.649e-6 < diamond < 5.651e-6
assert 1.129e-5 < endpoint < 1.131e-5
assert 88_000 < compression < 89_000

# The limiting aperture and disk radius are exactly twice the previous
# parent-threshold values to first order, with the strict sine ratio just below 2.
old_diamond = 0.5 * sin(nu_f / 2)
assert diamond > 1.9999999999 * old_diamond
assert diamond < 2 * old_diamond

print("PASS: unconditional near-maximal-aperture corridor regressions")
print(f"c={c_f:.15g}")
print(f"nu={nu_f:.15g}")
print(f"cH={cH:.15g}")
print(f"gammaH={gammaH:.15g}")
print(f"limiting_diamond_radius_coeff={diamond:.15g}")
print(f"limiting_endpoint_separation_coeff={endpoint:.15g}")
print(f"limiting_compression_factor={compression:.15g}")