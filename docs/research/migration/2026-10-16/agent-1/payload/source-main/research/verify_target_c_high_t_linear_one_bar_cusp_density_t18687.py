#!/usr/bin/env python3
"""Exact constants for the corrected high-t linear local-obstruction fork.

This certifies the global budget extraction and the non-antipodal opening-width
constant. Geometry separating exact-antipodal, TB1, and non-antipodal TB2
interfaces is proved in the companion note.
"""

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
row_floor = Q(113, 5_000_000)  # 0.0000226
column_floor = Q(1567, 10000)  # 0.1567
C = Q(1_109_000)
M = 4 * C

scale = 10**90
sqrt3_hi = Q(isqrt(3 * scale * scale) + 1, scale)
Cphase_hi = pi_hi * pi_hi * sqrt3_hi * (2 + sqrt3_hi) / 12
Ktotal = 10 * T - 2 * pi_lo + 2 + 2 * Cphase_hi

# Existing fixed-chain strict margin.
assert Ktotal < C * row_floor

# The larger hub side has asymptotic density row_floor/2. Interfaces with
# J>=4C have density below row_floor/4, leaving row_floor/4 good density.
side_density = row_floor / 2
good_density = row_floor / 4
fork_half_density = good_density / 2
assert side_density == Q(113, 10_000_000)
assert good_density == Q(113, 20_000_000)
assert fork_half_density == Q(113, 40_000_000)
assert float(good_density) == 0.00000565
assert float(fork_half_density) == 0.000002825

# Local non-antipodal opening and two-row retained-column constants.
phase_coeff = M / column_floor
column_coeff = 2 * M / column_floor
assert phase_coeff < 28_310_000
assert column_coeff < 56_620_000

print("PASS: corrected linear high-t obstruction-fork constants through t<=1.8687")
print("joint budget coefficient =", float(Ktotal))
print("C*row_floor margin =", float(C * row_floor - Ktotal))
print("hub-side density =", float(side_density))
print("linear-good density =", float(good_density))
print("half-fork density =", float(fork_half_density))
print("linear-good threshold =", int(M))
print("non-antipodal opening coefficient <", float(phase_coeff))
print("two-row retained-column coefficient <", float(column_coeff))
