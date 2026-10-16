#!/usr/bin/env python3
"""Regression checks for the TT-prefix / return-suffix aperture tradeoff."""

from fractions import Fraction
from math import asin, pi, sin

c = Fraction(113, 5_000_000)
n0 = c / 2

z0 = 20477 / 10000
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)

# Discrete minimax identity:
# min_j max(2(j-1), 2(L-j)+1) = L.
for L in range(1, 500):
    vals = [max(2 * (j - 1), 2 * (L - j) + 1) for j in range(1, L + 1)]
    assert min(vals) == L

# Terminal cutoffs: M=min(rA,rB), and one lane is nonterminal/opposite-host
# at every center of the suffix M+1..N.
for N in range(1, 80):
    for rA in range(N + 1):
        for rB in range(N + 1):
            M = min(rA, rB)
            L = N - M
            assert M + L == N
            if L:
                if rA == M:
                    assert all(s > rA for s in range(M + 1, N + 1))
                if rB == M:
                    assert all(s > rB for s in range(M + 1, N + 1))

# Finite C67 scaling. delta_D >= 1/D and D*delta_D -> 1.
for D in (100, 1_000, 100_000, 10_000_000):
    delta = 2 * asin(1 / (2 * D))
    assert delta >= 1 / D
    assert D * delta > 1
    if D >= 100_000:
        assert abs(D * delta - 1) < 1e-10

# No-TT asymptotic aperture and its central-diamond coefficient.
rho_no_tt = float(n0)
diamond = sin(rho_no_tt / 2)
assert rho_no_tt == 1.13e-5
assert 5.64e-6 < diamond < 5.66e-6
assert rho_no_tt < gammaH / 2

# Compare against the preceding host-projection minimax floor.
rho_projection = cH * float(c) / (1 + cH)
assert rho_no_tt > rho_projection

# Density-scale tradeoff arithmetic: theta+ell=n.
for q in range(101):
    theta = float(n0) * q / 100
    ell = float(n0) - theta
    assert abs(theta + ell - float(n0)) < 1e-18
    # TT span increment is 2 theta; return suffix aperture is ell.
    assert 2 * theta >= 0
    assert ell >= 0

print("PASS: TT-prefix / return-suffix aperture tradeoff regressions")
print(f"c={float(c):.12g}")
print(f"near_full_density={float(n0):.12g}")
print(f"cH={cH:.15g}")
print(f"gammaH={gammaH:.15g}")
print(f"no_TT_gap_floor={rho_no_tt:.15g}")
print(f"no_TT_gap_floor_deg={rho_no_tt * 180 / pi:.15g}")
print(f"no_TT_central_diamond_coeff={diamond:.15g}")
print(f"previous_projection_floor={rho_projection:.15g}")
