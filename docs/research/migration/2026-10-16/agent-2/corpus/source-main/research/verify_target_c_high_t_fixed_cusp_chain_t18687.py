#!/usr/bin/env python3
"""Exact constant certificate for the fixed-length high-t cusp-chain theorem."""

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
base_cusp = Q(1_109_000)

scale = 10**90
sqrt3_hi = Q(isqrt(3 * scale * scale) + 1, scale)
Cphase_hi = pi_hi * pi_hi * sqrt3_hi * (2 + sqrt3_hi) / 12

Kfinite = 10 * T - 2 * pi_lo + 2
Kangular = 2 * Cphase_hi
Ktotal = Kfinite + Kangular

# This strict margin is the sliding-window engine: the mean J-budget per
# internal rectangle interface is below 1,108,000, so some fixed length-r
# window has total J-budget below 1,109,000*r after excluding O(r) windows.
assert Ktotal / row_floor < 1_108_000
assert Ktotal < base_cusp * row_floor

phase_base = base_cusp / column_floor
chain_column_base = 2 * base_cusp / column_floor
assert phase_base < 7_080_000
assert chain_column_base < 14_160_000

print("PASS: fixed-length high-t cusp-chain constants through t<=1.8687")
print("joint budget coefficient =", float(Ktotal))
print("joint average coefficient =", float(Ktotal / row_floor))
print("run-extraction margin =", float(base_cusp * row_floor - Ktotal))
print("per-interface phase coefficient per r =", float(phase_base))
print("chain column-defect coefficient per r =", float(chain_column_base))

for r in (1, 2, 3, 5, 10):
    M_r = base_cusp * r
    print(
        f"r={r}: interface_budget={int(M_r)}, "
        f"phase_coeff<{float(phase_base * r):.6f}, "
        f"chain_column_coeff<{float(chain_column_base * r):.6f}, "
        f"total_switch_budget<{int(base_cusp * r)}"
    )
