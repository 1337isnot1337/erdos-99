#!/usr/bin/env python3
"""Exact outward certificate for the g=0.0077 residual-coupled floor t>=1.843577."""

from fractions import Fraction as Q
from math import factorial, isqrt


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


def sin_bounds(x, n=26):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10**100
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
K_lo = Q(2) / sqrt3_hi
K_hi = Q(2) / sqrt3_lo
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C77_lo = 2 * s_lo + Q(77, 10000)
C77_hi = 2 * s_hi + Q(77, 10000)


def m2_bounds(Ulo, Uhi):
    xlo = 8 * Delta_lo - Uhi * Uhi
    xhi = 8 * Delta_hi - Ulo * Ulo
    assert xlo > 0
    rlo, rhi = sqrt_bounds(xlo, xhi, SCALE)
    return (Ulo + rlo) / 2, (Uhi + rhi) / 2


Ubar = Q(2013, 1000)
m_lo, _ = m2_bounds(Ubar, Ubar)
generic_residual_hi = Ubar - m_lo
assert generic_residual_hi < Q(112, 1000)

strong_slope_lo = m_lo / 3 - Q(1, 10) * (3 * C77_hi / 4 - K_lo)
fallback_slope_lo = m_lo / 2 - Q(4, 29) * (C77_hi - K_lo)
high_center_slope_lo = K_lo
assert strong_slope_lo > Q(596, 1000)
assert fallback_slope_lo > Q(84, 100)
assert high_center_slope_lo > Q(115, 100)

stability_factor = 1 / (1 - Q(112, 1000) / (4 * Q(596, 1000)))
assert stability_factor < Q(21, 20)

T = Q(1843577, 1000000)
Umax_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Umax_hi - C77_lo) / 2
h_max_hi = Umax_hi - C77_lo
assert Umax_hi < Ubar
assert delta_max_hi < Q(51, 1000)
assert h_max_hi < Q(101, 1000)

Fprime_cap = Q(67, 500)
c = Q(21, 20)
Qx_upper = -1 / (2 * Fprime_cap) + 1
Qh_upper = (
    -1 / (2 * Fprime_cap)
    + c
    + c * c * Q(101, 1000) / (1 - Q(51, 1000))
)
assert Qx_upper < Q(-27, 10)
assert Qh_upper < Q(-5, 2)

S_corner_lo = pi_lo - T / 2
F_corner_lo, _ = F_bounds(S_corner_lo)
delta_corner_hi = (Q(9, 2) * T - 2 * pi_lo - C77_lo) / 2
corner_margin_lo = F_corner_lo - delta_corner_hi
assert corner_margin_lo > Q(13, 10_000_000)

T2 = Q(921789, 500000)  # 1.843578
S2_hi = pi_hi - T2 / 2
_, F2_hi = F_bounds(S2_hi)
delta2_lo = (Q(9, 2) * T2 - 2 * pi_hi - C77_hi) / 2
fail_margin_hi = F2_hi - delta2_lo
assert fail_margin_hi < 0

print("PASS g=0.0077 residual-coupled floor t>=1.843577")
print("generic residual upper at U=2.013 =", float(generic_residual_hi))
print("strong branch slope lower =", float(strong_slope_lo))
print("fallback branch slope lower =", float(fallback_slope_lo))
print("high-center branch slope lower =", float(high_center_slope_lo))
print("residual stability factor =", float(stability_factor))
print("Umax upper =", float(Umax_hi))
print("delta max upper =", float(delta_max_hi))
print("h max upper =", float(h_max_hi))
print("Q_x upper =", float(Qx_upper))
print("Q_h upper =", float(Qh_upper))
print("corner contradiction margin =", float(corner_margin_lo))
print("1.843578 corner margin upper =", float(fail_margin_hi))
