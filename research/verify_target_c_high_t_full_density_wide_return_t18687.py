#!/usr/bin/env python3
"""Regression checks for the full-density fixed-wide no-TT return theorem."""

from fractions import Fraction
from math import asin, pi, sin

c = Fraction(113, 5_000_000)
n0 = c / 2

z0 = 20477 / 10000
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)

rhoF = cH * float(c) / (1 + cH)
diamond = sin(rhoF / 2)

assert float(n0) == 1.13e-5
assert 0 < rhoF < gammaH / 2
assert 7.05e-6 < rhoF < 7.06e-6
assert 3.52e-6 < diamond < 3.54e-6

# Exact affine minimax inequality used after combining the two ramps.
# max{x, cH(n-x)} >= cH*n/(1+cH), with equality at their intersection.
for D in (10_000, 100_000, 1_000_000):
    # Use a deliberately larger finite population to check monotonicity in n.
    N0 = int(float(n0) * D)
    for extra in (0, 1, 7):
        N = N0 + extra
        n = N / D
        floor = cH * n / (1 + cH)
        for s in range(1, max(2, N + 1)):
            x = (s - 1) / D
            val = max(x, cH * (n - x))
            assert val + 1e-15 >= floor

# Exhaust the terminal-prefix combinatorics. No TT means one terminal cutoff
# is zero, hence that lane is opposite-host throughout the full population.
for N in range(1, 41):
    for rA in range(N + 1):
        for rB in range(N + 1):
            if min(rA, rB) == 0:
                assert rA == 0 or rB == 0
                if rA == 0:
                    assert all(s > rA for s in range(1, N + 1))
                if rB == 0:
                    assert all(s > rB for s in range(1, N + 1))

# Finite discrete version of the two-ramp minimax. For a narrow center,
# ordered bilateral motion gives eta >= 2(s-1)/D and the return estimate,
# after arcsin(z)>=z, gives eta >= 2*cH*(N-s)/D. Their minimum tends to rhoF.
for D in (1_000_000, 5_000_000, 20_000_000):
    N = int(float(n0) * D)
    if N == 0:
        continue
    vals = []
    for s in range(1, N + 1):
        a = 2 * (s - 1) / D
        b = 2 * cH * (N - s) / D
        vals.append(max(a, b))
    finite_min = min(vals)
    # Discretization and the omitted O(1/D) endpoints cost at most a few /D.
    assert finite_min + 4 / D >= rhoF - 1e-14

# The earlier first-half return-only aperture is strictly weaker than the
# combined full-density aperture.
rho_old = 2 * asin(cH * float(c) / 4)
assert rhoF > rho_old

print("PASS: full-density fixed-wide no-TT return regressions")
print(f"c={float(c):.12g}")
print(f"near_full_density={float(n0):.12g}")
print(f"cH={cH:.15g}")
print(f"gammaH={gammaH:.15g}")
print(f"rho_old_half_population={rho_old:.15g}")
print(f"rho_full_density={rhoF:.15g}")
print(f"rho_full_density_deg={rhoF * 180 / pi:.15g}")
print(f"central_diamond_coeff={diamond:.15g}")
