#!/usr/bin/env python3
"""Exact constant certificate for the high-t three-row clustered cusp at t<=1.8687."""

from fractions import Fraction as Q
from math import isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


a5l, a5h = atan_inv_bounds(5, 100)
a239l, a239h = atan_inv_bounds(239, 30)
pi_lo, pi_hi = 16 * a5l - 4 * a239h, 16 * a5h - 4 * a239l

T = Q(18687, 10000)
row_floor = Q(113, 5_000_000)   # 0.0000226 consecutive rectangle rows
col_floor = Q(1567, 10000)      # 0.1567 consistently oriented common columns

S = 10 ** 90
n3 = isqrt(3 * S * S)
sqrt3_hi = Q(n3 + 1, S)
Cphase_hi = pi_hi * pi_hi * sqrt3_hi * (2 + sqrt3_hi) / 12

# Existing global finite-defect/KKT budget for one interface:
#   sum_i (N_i + L_i + D B_i) <= (10T - 2pi + 2) D + o(D).
Kglob = 10 * T - 2 * pi_lo + 2

# For three consecutive rows, a sliding triple contains two interfaces,
# three row angular-defect sums, and two outer-walk gap terms.
# Summed over all triples:
#   interface cost <= 2 Kglob D,
#   angular cost   <= 3 Cphase D,
#   outer-gap cost <= 2 b <= 4 pi D.
Ktriple = 2 * Kglob + 3 * Cphase_hi + 4 * pi_hi
average = Ktriple / row_floor

J = Q(2_537_000)
assert average < J

# Consequences against the common oriented column shore.
phase_pair = J / col_floor
three_row_half_column_defect = 2 * J / col_floor
assert phase_pair < 16_200_000
assert three_row_half_column_defect < 32_381_000

print("PASS: high-t three-row clustered cusp through t<=1.8687")
for k, v in [
    ("one-interface global coefficient", Kglob),
    ("phase coefficient", Cphase_hi),
    ("triple-window coefficient", Ktriple),
    ("limiting triple average", average),
    ("margin to 2,537,000", J - average),
    ("pair row-phase coefficient", phase_pair),
    ("half-column three-row defect coefficient", three_row_half_column_defect),
]:
    print(k, "=", float(v))
