#!/usr/bin/env python3
"""Exact arithmetic certificate for the t<=1.855 low-energy O-O dual-path extraction.

The numerical claims proved here are the scope-safe energy envelope, the resulting
weighted-Markov mass, and the adjacent switch-count threshold. The two-arc ->
dual-path step is topological and is proved in the companion markdown note.
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


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator * scale * scale) // lo.denominator)
    b = isqrt((hi.numerator * scale * scale) // hi.denominator)
    return Q(a, scale), Q(b + 1, scale)


a5_lo, a5_hi = atan_inv_bounds(5, 90)
a239_lo, a239_hi = atan_inv_bounds(239, 25)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10 ** 90
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, _ = sqrt_bounds(Delta_lo, Delta_hi, SCALE)

# Corrected matched atomic floor C_76 = 2 sqrt(Delta_2) + 0.0076.
C76_lo = 2 * s_lo + Q(19, 2500)

T = Q(371, 200)  # 1.855
Umax_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Umax_hi - C76_lo) / 2

# Safe outer directional-energy ceiling used by the theorem.
assert delta_max_hi < Q(761, 10000)  # 0.0761

# Existing staircase theorem: total retained dominant O-O pair weight >0.14 D.
P = Q(14, 100)

# Select trains whose two-terminal pair energy is <= 0.9.
lam = Q(9, 10)
low_total = P - Q(761, 10000) / lam
low_phase = low_total / 3

assert low_total == Q(499, 9000)
assert low_phase == Q(499, 27000)
assert low_phase > Q(23, 1250)  # 0.0184

# A path of density >0.0184 has one internal boundary with at most 341
# switching diameter intervals. Use the standard outward pi bound 355/113.
pi_up = Q(355, 113)
path_floor = Q(23, 1250)
avg_switch_up = 2 * pi_up / path_floor
assert avg_switch_up < 342
assert avg_switch_up > 341

print("PASS high-t low-energy O-O dual-path arithmetic")
print("delta_max_hi =", float(delta_max_hi))
print("delta margin to 0.0761 =", float(Q(761, 10000) - delta_max_hi))
print("low-energy total retained pair weight >", low_total, "=", float(low_total))
print("one phase low-energy pair weight >", low_phase, "=", float(low_phase))
print("margin above 0.0184 =", float(low_phase - Q(23, 1250)))
print("terminal-arc gap: pi - 2 arccos(0.1) = 2 arcsin(0.1) > 0.2 radians")
print("2*pi_up/0.0184 =", float(avg_switch_up), "< 342, hence an integer switch count <=341")
