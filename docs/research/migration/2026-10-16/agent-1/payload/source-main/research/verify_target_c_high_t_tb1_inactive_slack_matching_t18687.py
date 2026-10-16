#!/usr/bin/env python3
"""Regression checks for the TB1 inactive-slack matching theorem."""

from fractions import Fraction
from math import asin, pi, sin, sqrt

S0 = Fraction(791, 320_000_000)
KAPPA = 31.4e6

# Density arithmetic.
assert abs(float(S0 / 8) - 3.08984375e-7) < 1e-20
assert abs(float(S0 / 88) - 2.8089488636363635e-8) < 1e-20
near_diam_matching_coeff = float(S0) / (128 * 3 ** (1 / 8))
assert abs(near_diam_matching_coeff - 1.6833575791297435e-8) < 1e-20

# Near-unit degree-six threshold. The proof uses the deliberately loose bound
# 2 q + 2(1+q) sin(pi/7) < 1. It holds whenever q is below q_crit, and
# q_D=O(1/D) eventually is.
s = sin(pi / 7)
assert 2 * s < 1
q_crit = (1 - 2 * s) / (2 + 2 * s)
assert 0.046 < q_crit < 0.047
for q in [1e-6, 1e-4, 1e-2, 0.04]:
    assert 2 * q + 2 * (1 + q) * s < 1

# Near-diameter midpoint/degree leading constants. For very large D,
# L'_D / D^(3/4) -> 3^(1/8) and (Theta'_D/delta'_D)/D^(3/4)
# -> 8*3^(1/8).
lead_midpoint = 3 ** (1 / 8)
lead_degree = 8 * lead_midpoint
for D in [10**12, 10**16, 10**20]:
    q = KAPPA / D
    assert q < 1
    eta = 3 ** (1 / 4) * sqrt(D)
    L = sqrt(D * eta + eta * eta + D * q / 2)
    assert L / D ** 0.75 > lead_midpoint
    theta = 2 * asin(4 * L / (D - q))
    delta = 2 * asin(sqrt(1 - q * q) / (2 * D))
    normalized_degree = (theta / delta) / D ** 0.75
    assert normalized_degree > lead_degree
    # Numerical convergence is rapid; a generous envelope prevents this
    # regression from depending on floating-point last digits.
    assert normalized_degree < lead_degree + 1e-3

# Greedy matching denominators used in the theorem.
# Delta<=6 => an edge meets at most 2*6-1=11 edges including itself.
assert 2 * 6 - 1 == 11
# Near-diameter asymptotic: E >= (s0/8)D and Delta <=
# (8*3^(1/8)+o(1))D^(3/4), hence E/(2 Delta) has coefficient below.
assert abs(
    (float(S0) / 8) / (16 * 3 ** (1 / 8))
    - near_diam_matching_coeff
) < 1e-20

print("PASS: high-t TB1 inactive-slack matching regressions")
print("near-unit type density =", float(S0 / 8))
print("near-unit matching density =", float(S0 / 88))
print("near-diameter matching D^(1/4) coefficient =", near_diam_matching_coeff)
print("near-unit q threshold =", q_crit)
print("midpoint leading coefficient =", lead_midpoint)
print("near-diameter degree leading coefficient =", lead_degree)
