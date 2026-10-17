#!/usr/bin/env python3
"""Exact outward arithmetic certificate for the g=0.0076 residual-coupled floor t>=1.84355.

The symbolic branch arguments are in
`target_c_g0076_residual_floor_184355_2026-09-15.md` and inherit the hostile-audited
strong/fallback/high-center phase-star capacities. This script certifies the new
bootstrap, residual-stability constants, and final corner sign.
"""

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


def sin_bounds(x, n=24):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


# Exact pi and algebraic enclosures.
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
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)

C76_lo = 2 * s_lo + Q(19, 2500)
C76_hi = 2 * s_hi + Q(19, 2500)
T = Q(36871, 20000)  # 1.84355

Umax_lo = Q(9, 2) * T - 2 * pi_hi
Umax_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Umax_hi - C76_lo) / 2


def m2_bounds(Ulo, Uhi):
    xlo = 8 * Delta_lo - Uhi * Uhi
    xhi = 8 * Delta_hi - Ulo * Ulo
    rlo, rhi = sqrt_bounds(xlo, xhi, SCALE)
    return (Ulo + rlo) / 2, (Uhi + rhi) / 2


def bootstrap_step(z):
    Flo, _ = F_bounds(z)
    Ulo = Umax_lo - 2 * Flo
    Uhi = Umax_hi - 2 * Flo
    mlo, _ = m2_bounds(Ulo, Uhi)
    rhi = Uhi - mlo
    Slo = pi_lo - Uhi - T / 2 + mlo
    p_hi = (delta_max_hi - Flo + rhi * rhi) / (2 * (1 - delta_max_hi))
    return Slo - p_hi, Flo, Uhi, rhi, p_hi


# Generic restored-incidence bootstrap. Each threshold is rounded down.
z_levels = [
    Q(0),
    Q(20753, 10000),
    Q(21885, 10000),
    Q(22068, 10000),
    Q(22099, 10000),
    Q(22104, 10000),
]

for i, z in enumerate(z_levels[:-1]):
    nxt, *_ = bootstrap_step(z)
    assert nxt > z_levels[i + 1]
    print(f"bootstrap {i} margin =", float(nxt - z_levels[i + 1]))

# The last bootstrap level localizes every putative survivor to U<1.9135.
Flo, _ = F_bounds(z_levels[-1])
U_hi = Umax_hi - 2 * Flo
U_bar = Q(3827, 2000)  # 1.9135
assert U_hi < U_bar

# Generic two-bin residual bound on the localized window.
mlo, _ = m2_bounds(U_bar, U_bar)
r2_hi = U_bar - mlo
assert r2_hi < Q(9, 1000)

# Distance above the hostile-audited g=.0076 endpoint.
h_hi = U_bar - C76_lo
assert h_hi < Q(128, 100000)  # 0.00128

# Strong-branch residual stability. The hostile audit gives Q1'(W)>.5968;
# hence the one-orbit strong capacity has derivative >.5968 as well.
strong_slope = Q(373, 625)  # 0.5968
stability_factor = 1 / (1 - Q(9, 1000) / (4 * strong_slope))
assert stability_factor < Q(251, 250)  # 1.004

# When U replaces C76 in the residual-square term, the extra capacity is at most
# h*R/2. This is negligible compared with the audited fallback/high-center margins.
extra_residual_capacity = Q(9, 1000) * Q(128, 100000) / 2
assert extra_residual_capacity < Q(6, 1_000_000)

# A dominant orbit below the original M0 domain is impossible even under generic
# Mantel capacity. Use outward bounds for M0=4 Delta/C76 and U=1.9135.
M0_hi = 4 * Delta_hi / C76_lo
generic_low_mass_capacity_hi = (M0_hi * M0_hi + (U_bar - M0_hi) ** 2) / 4
assert generic_low_mass_capacity_hi < Delta_lo - Q(7, 1000)

# Final weak corner h=x=0. Feasibility would require
# delta >= F(pi-t/2). The exact outward sign is reversed at t=1.84355.
S_corner_lo = pi_lo - T / 2
F_corner_lo, _ = F_bounds(S_corner_lo)
delta_corner_hi = (Q(9, 2) * T - 2 * pi_lo - C76_lo) / 2
corner_margin_lo = F_corner_lo - delta_corner_hi
assert corner_margin_lo > Q(13, 1_000_000)

# Coarse domain checks used in the derivative reduction.
assert delta_max_hi < Q(51, 1000)

print("U upper after bootstrap =", float(U_hi))
print("generic residual upper =", float(r2_hi))
print("h upper =", float(h_hi))
print("residual stability factor =", float(stability_factor))
print("extra fallback residual capacity =", float(extra_residual_capacity))
print("generic low-mass capacity margin =", float(Delta_lo - generic_low_mass_capacity_hi))
print("corner F lower =", float(F_corner_lo))
print("corner delta upper =", float(delta_corner_hi))
print("corner contradiction margin =", float(corner_margin_lo))
print("PASS: g=.0076 residual coupling forces t >= 1.84355")
