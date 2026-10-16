#!/usr/bin/env python3
"""Exact scalar certificate for the terminal FREE quantitative incidence gap.

The geometric inputs are the separately audited/proof-only modules cited in
`target_c_free_terminal_quantitative_incidence_surplus_gap_2026-09-18.md`.
This script certifies only the scalar enclosures used by that composition.
"""

from fractions import Fraction as F
from math import isqrt


def atan_inv_bounds(q: int, n: int) -> tuple[F, F]:
    s = F(0)
    for k in range(n):
        term = F(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = F(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_floor(q: F, scale: int) -> F:
    n = isqrt((q.numerator * scale * scale) // q.denominator)
    out = F(n, scale)
    assert out * out <= q
    return out


def sqrt_ceil(q: F, scale: int) -> F:
    n = isqrt((q.numerator * scale * scale) // q.denominator) + 1
    out = F(n, scale)
    assert out * out >= q
    return out


def show(x: F) -> str:
    return f"{float(x):.16g}"


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
s_lo = sqrt_floor(Delta_lo, SCALE)
s_hi = sqrt_ceil(Delta_hi, SCALE)

g = F(7707, 1_000_000)
epsilon = F(129, 20_000)  # 0.00645
a_max = 5 * epsilon  # 0.03225
delta_max = F(5, 2) * epsilon  # 0.016125

assert a_max == F(129, 4000)
assert delta_max == F(129, 8000)

# C <= 2*s_2+g+a_max.
C_hi = 2 * s_hi + g + a_max

# Two-bin residual r(C)=(C-sqrt(8 Delta_2-C^2))/2.
# Lower-bound the square root to upper-bound r.
radicand_lo = 8 * Delta_lo - C_hi * C_hi
assert radicand_lo > 0
sqrt_radicand_lo = sqrt_floor(radicand_lo, SCALE)
residual_hi = (C_hi - sqrt_radicand_lo) / 2
residual_cap = F(101, 2500)  # 0.0404
assert residual_hi < residual_cap

# Dominant retained outer mass: F(z)=z-6 sin(z/6).
# The alternating sine upper bound gives
# F(z)>=z^3/216-z^5/155520.
z0 = F(1519, 1000)
Fz_lower = z0**3 / F(216) - z0**5 / F(155_520)
assert Fz_lower > delta_max

# Shared retention: z+p >= pi/2-r.
p_lower = pi_lo / 2 - residual_cap - z0
p0 = F(113, 10_000)  # 0.0113
assert p_lower > p0

# Conservative complement-incidence inequality:
# p(1-delta)-e_c/2 <= r^2/2, with e_c<=delta.
incidence_lhs = p0 * (1 - delta_max) - delta_max / 2
incidence_rhs = residual_cap * residual_cap / 2
assert incidence_lhs > incidence_rhs

mu_star_lo = pi_lo / 2 + F(2, 5) * s_lo + g / 5
mu_floor_lo = mu_star_lo + epsilon

print("PASS terminal FREE quantitative incidence surplus gap")
print("epsilon:", show(epsilon))
print("a upper:", show(a_max))
print("detour upper:", show(delta_max))
print("C upper:", show(C_hi))
print("residual upper:", show(residual_hi))
print("residual cap:", show(residual_cap))
print("F(1.519) rational lower:", show(Fz_lower))
print("retained complement pair lower:", show(p_lower))
print("declared pair floor:", show(p0))
print("incidence demand lower:", show(incidence_lhs))
print("residual incidence capacity upper:", show(incidence_rhs))
print("incidence margin:", show(incidence_lhs - incidence_rhs))
print("new mu floor lower:", show(mu_floor_lo))
