#!/usr/bin/env python3
"""Exact-rational certificate for live terminal FREE detour pinching.

Certifies for epsilon=0.00710:
* the correlated reduced feasibility function is strictly decreasing;
* every survivor must have delta>0.017609;
* a+2r<0.000282 and r<0.000141;
* universal pair-shield flex density >1.1988388040;
* signed diameter-locking incidence density >2.3976776080;
* face-count and pentagon floors;
* one-anchor corank base constant <0.15230481.

All load-bearing arithmetic is Fraction/integer-square-root/Taylor/Machin.
"""

from fractions import Fraction
from math import isqrt

Q = Fraction


def atan_inv_bounds(q: int, terms: int):
    s = Q(0)
    for k in range(terms):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * terms + 1) * q ** (2 * terms + 1))
    if terms % 2 == 0:
        return s, s + nxt
    return s - nxt, s


def sqrt_floor(x: Q, scale: int) -> Q:
    n = isqrt((x.numerator * scale * scale) // x.denominator)
    y = Q(n, scale)
    assert y * y <= x
    return y


def sqrt_ceil(x: Q, scale: int) -> Q:
    n = isqrt((x.numerator * scale * scale) // x.denominator) + 1
    y = Q(n, scale)
    assert y * y >= x
    return y


DIGITS = 90
SCALE = 10 ** DIGITS

# Machin enclosure for pi.
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo
assert pi_lo < pi_hi

# sqrt(3), Delta_2, s_2.
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
assert sqrt3_lo * sqrt3_lo < 3 < sqrt3_hi * sqrt3_hi

delta2_lo = pi_lo / (2 * sqrt3_hi)
delta2_hi = pi_hi / (2 * sqrt3_lo)
s2_lo = sqrt_floor(delta2_lo, SCALE)
s2_hi = sqrt_ceil(delta2_hi, SCALE)

g = Q(7707, 10**6)
epsilon = Q(71, 10000)              # 0.00710
five_epsilon = 5 * epsilon           # 0.0355
delta_max = Q(71, 4000)              # 0.01775
delta_cut = Q(17609, 10**6)          # 0.017609
assert delta_cut < delta_max

# rho(delta)=r_2(A0+5 epsilon-2 delta).
# Uniform outward bound on rho and the derivative factor.
C_uniform_hi = 2 * s2_hi + g + five_epsilon
radicand_uniform_lo = 8 * delta2_lo - C_uniform_hi * C_uniform_hi
assert radicand_uniform_lo > 0
sqrt_radicand_uniform_lo = sqrt_floor(radicand_uniform_lo, SCALE)
residual_uniform_hi = (C_uniform_hi - sqrt_radicand_uniform_lo) / 2
assert residual_uniform_hi < Q(44, 1000)

# F(z)=z-6 sin(z/6). Taylor gives
# F(z) >= z^3/216-z^5/155520.
# This cap covers z_delta throughout delta<=delta_max.
z_uniform_cap = Q(1567, 1000)        # 1.567
Fz_uniform_lower = (
    z_uniform_cap**3 / 216
    - z_uniform_cap**5 / 155520
)
assert Fz_uniform_lower > delta_max

# G'(delta)<0.
# -rho'=1+C/sqrt(8Delta_2-C^2).
# z_delta'=1/F'(z_delta), with F'(z)<=z^2/72.
Fp_uniform_cap = z_uniform_cap * z_uniform_cap / 72
minus_rho_prime_hi = 1 + C_uniform_hi / sqrt_radicand_uniform_lo
rho_factor_hi = 1 + residual_uniform_hi / (1 - delta_max)
positive_derivative_cap = minus_rho_prime_hi * rho_factor_hi
zprime_lower = 1 / Fp_uniform_cap
assert positive_derivative_cap < zprime_lower

# Rigorous positive G at delta_cut.
C_cut_hi = 2 * s2_hi + g + five_epsilon - 2 * delta_cut
radicand_cut_lo = 8 * delta2_lo - C_cut_hi * C_cut_hi
assert radicand_cut_lo > 0
sqrt_radicand_cut_lo = sqrt_floor(radicand_cut_lo, SCALE)
residual_cut_hi = (C_cut_hi - sqrt_radicand_cut_lo) / 2
residual_cap = Q(4003, 500000)        # 0.008006
assert residual_cut_hi < residual_cap

z_cut_cap = Q(312549, 200000)         # 1.562745
Fz_cut_lower = z_cut_cap**3 / 216 - z_cut_cap**5 / 155520
assert Fz_cut_lower > delta_cut

margin = (
    pi_lo / 2
    - residual_cap
    - z_cut_cap
    - residual_cap**2 / (2 * (1 - delta_cut))
)
assert margin > Q(12, 10**6)

# Remaining correlated defect budget.
remaining = five_epsilon - 2 * delta_cut
assert remaining == Q(141, 500000)   # 0.000282
assert remaining / 2 == Q(141, 10**6)  # 0.000141

Mstar_lo = 4 * s2_lo + 2 * g
Mstar_hi = 4 * s2_hi + 2 * g

# Pair-shield base:
# (b-f)/(2D) >= pi/2-M*/10-epsilon+delta+r/2.
pair_floor_lo = (
    pi_lo / 2
    - Mstar_hi / 10
    - epsilon
    + delta_cut
)
assert pair_floor_lo > Q(11988388, 10**7)  # 1.1988388

signed_incidence_lo = 2 * pair_floor_lo
assert signed_incidence_lo > Q(23976776, 10**7)  # 2.3976776

# Exceptional-face strip.
f_lo = (Mstar_lo - delta_max) / 5
f_hi = (Mstar_hi + 10 * epsilon - 5 * delta_cut) / 5
assert f_lo > Q(76138304, 10**8)
assert f_hi < Q(76152405, 10**8)

# P5 >= f-r; optimize with the correlated budget.
p5_lo = (Mstar_lo + 5 * delta_cut - 15 * epsilon) / 5
assert p5_lo > Q(76124204, 10**8)

# One-anchor corank base f/5.
corank_base_hi = f_hi / 5
assert corank_base_hi < Q(15230481, 10**8)

print("PASS: live terminal FREE detour pinching certified")
print("delta >", float(delta_cut))
print("G(delta_cut) margin >", float(margin))
print("a+2r <", float(remaining))
print("r <", float(remaining / 2))
print("pair-shield flex density >", float(pair_floor_lo))
print("signed diameter-incidence density >", float(signed_incidence_lo))
print("f density in (", float(f_lo), ",", float(f_hi), ")")
print("P5 density >", float(p5_lo))
print("one-anchor corank base <", float(corank_base_hi))
