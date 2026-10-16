#!/usr/bin/env python3
"""Exact scalar certificate for the terminal FREE outer-energy surplus gap.

This certifies the numerical inequalities used in
`target_c_free_terminal_outer_energy_surplus_gap_2026-09-18.md`.
The geometric inputs are the separately audited/proof-only train-phase,
outer-energy, and O--O bracing theorems cited there.
"""

from fractions import Fraction as F
from math import isqrt


def atan_inv_bounds(q: int, n: int) -> tuple[F, F]:
    """Alternating-series bounds for atan(1/q)."""
    s = F(0)
    for k in range(n):
        term = F(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = F(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo: F, hi: F, scale: int) -> tuple[F, F]:
    assert 0 <= lo <= hi
    lo_n = isqrt((lo.numerator * scale * scale) // lo.denominator)
    hi_n = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    out_lo = F(lo_n, scale)
    out_hi = F(hi_n, scale)
    assert out_lo * out_lo <= lo
    assert out_hi * out_hi >= hi
    return out_lo, out_hi


def show(x: F) -> str:
    return f"{float(x):.16g}"


# Rigorous enclosures for pi, sqrt(3), Delta_2 and sqrt(Delta_2).
DIGITS = 90
SCALE = 10**DIGITS

a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

sqrt3_n = isqrt(3 * SCALE * SCALE)
sqrt3_lo = F(sqrt3_n, SCALE)
sqrt3_hi = F(sqrt3_n + 1, SCALE)

Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)

# Claimed safe endpoint gap and consequences of surplus stability.
g = F(7707, 1_000_000)
epsilon = F(3, 2500)  # 0.0012
a_max = 5 * epsilon  # 0.006
delta_max = F(5, 2) * epsilon  # 0.003

assert a_max == F(3, 500)
assert delta_max == F(3, 1000)

# All-train atomic scalar C <= 2 s_2 + g + a_max.
C_hi = 2 * s_hi + g + a_max

# If A is total atomic train mass and M the dominant-orbit mass, then
# R=A-M <= A-4 Delta_2/A.  The right side increases with A, so C_hi and
# Delta_lo give a rigorous residual upper bound.
R_hi = C_hi - 4 * Delta_lo / C_hi
R_cap = F(683, 25_000)  # 0.02732
assert R_hi < R_cap

# Dominant-orbit terminal threshold z_0=0.87.  For
# F(z)=z-6 sin(z/6), the alternating sine upper bound gives
# F(z) >= z^3/216-z^5/155520.
z0 = F(87, 100)
Fz_lower = z0**3 / F(216) - z0**5 / F(155_520)
assert Fz_lower > delta_max

# The transport identities then force an O--O retained pair floor
# p >= pi/2-g-a-z0-2R-delta.
p_lower = pi_lo / 2 - g - a_max - z0 - 2 * R_cap - delta_max
p0 = F(3147, 5000)  # 0.6294
assert p_lower > p0

# One of three pi/3 direction sectors has retained pair mass at least p0/3.
m0 = p0 / 3
assert m0 == F(1049, 5000)  # 0.2098
assert m0 < pi_lo / 6

# For E(m)=2m-2 sin(m), alternating sine gives
# E(m) >= m^3/3-m^5/60.
Em_lower = m0**3 / F(3) - m0**5 / F(60)
assert Em_lower > delta_max

# Report the old and improved surplus constants with rigorous lower endpoints.
mu_star_lo = pi_lo / 2 + F(2, 5) * s_lo + g / 5
mu_floor_lo = mu_star_lo + epsilon

print("PASS terminal FREE outer-energy surplus gap")
print("Delta_2 lower:", show(Delta_lo))
print("s_2 lower:", show(s_lo))
print("C upper:", show(C_hi))
print("atomic residual upper:", show(R_hi))
print("declared atomic residual cap:", show(R_cap))
print("F(0.87) rational lower:", show(Fz_lower))
print("retained O-O pair lower:", show(p_lower))
print("declared retained-pair floor:", show(p0))
print("one-sector pair floor:", show(m0))
print("sector energy rational lower:", show(Em_lower))
print("available detour upper:", show(delta_max))
print("mu_* lower:", show(mu_star_lo))
print("new mu floor lower:", show(mu_floor_lo))
