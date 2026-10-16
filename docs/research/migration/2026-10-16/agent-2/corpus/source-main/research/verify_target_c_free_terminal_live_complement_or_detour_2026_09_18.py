#!/usr/bin/env python3
"""Exact-rational certificate for the live complement-train/detour split.

No floating-point inequality is load-bearing. The script certifies:
  * monotonicity of Phi(delta)=F(pi/2-rho(delta)-0.01)-delta;
  * Phi(0.01725)>0 by rational Machin/square-root/Taylor bounds;
  * the remaining correlated defect budget a+2r<=0.001;
  * the displayed exceptional-face and pentagon constants.
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

# Rigorous pi enclosure from Machin's formula.
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo
assert pi_lo < pi_hi

# sqrt(3), Delta_2, s_2.
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
delta2_lo = pi_lo / (2 * sqrt3_hi)
delta2_hi = pi_hi / (2 * sqrt3_lo)
s2_lo = sqrt_floor(delta2_lo, SCALE)
s2_hi = sqrt_ceil(delta2_hi, SCALE)

g = Q(7707, 10**6)
epsilon = Q(71, 10000)            # 0.00710
delta_max = Q(71, 4000)           # 0.01775
delta_cut = Q(69, 4000)           # 0.01725
eta = Q(1, 100)                    # retained complement threshold 0.01
five_epsilon = 5 * epsilon         # 0.0355

# rho(delta)=r_2(2s_2+g+5eps-2delta). It is decreasing in delta.
# For Phi(delta)=F(pi/2-rho(delta)-eta)-delta,
# Phi'=F'(x)*(-rho')-1.
# Uniformly bound -rho' and F'(x) to prove Phi'<0.
C_uniform_hi = 2 * s2_hi + g + five_epsilon
rad_uniform_lo = 8 * delta2_lo - C_uniform_hi * C_uniform_hi
assert rad_uniform_lo > 0
sqrt_rad_uniform_lo = sqrt_floor(rad_uniform_lo, SCALE)
minus_rho_prime_hi = 1 + C_uniform_hi / sqrt_rad_uniform_lo

# x<=pi/2 and F'(x)=1-cos(x/6)<=x^2/72.
Fp_hi = (pi_hi / 2) ** 2 / 72
assert minus_rho_prime_hi * Fp_hi < 1

# At delta_cut, upper-bound rho, hence lower-bound x.
C_cut_hi = 2 * s2_hi + g + five_epsilon - 2 * delta_cut
rad_cut_lo = 8 * delta2_lo - C_cut_hi * C_cut_hi
assert rad_cut_lo > 0
sqrt_rad_cut_lo = sqrt_floor(rad_cut_lo, SCALE)
rho_cut_hi = (C_cut_hi - sqrt_rad_cut_lo) / 2
x_cut_lo = pi_lo / 2 - rho_cut_hi - eta
assert x_cut_lo > 0

# sin y <= y-y^3/6+y^5/120 gives
# F(x)=x-6sin(x/6) >= x^3/216-x^5/155520.
# This polynomial is increasing throughout the present range.
assert x_cut_lo * x_cut_lo < 432
F_cut_lo = x_cut_lo**3 / 216 - x_cut_lo**5 / 155520
margin = F_cut_lo - delta_cut
assert margin > Q(13, 10**7)      # >1.3e-6

# Since Phi is strictly decreasing, Phi(delta_cut)>0 implies a survivor with
# p<=0.01 must have delta>delta_cut.
remaining_budget = five_epsilon - 2 * delta_cut
assert remaining_budget == Q(1, 1000)
r_max = remaining_budget / 2
assert r_max == Q(1, 2000)

# Exceptional-face constants. Use outward bounds on M_*=4s_2+2g.
Mstar_lo = 4 * s2_lo + 2 * g
Mstar_hi = 4 * s2_hi + 2 * g

f_lower = (Mstar_lo - delta_max - r_max) / 5
f_upper = (Mstar_hi + 2 * remaining_budget - delta_cut) / 5
p5_lower = f_lower - r_max

assert f_lower > Q(761283, 10**6)
assert f_upper < Q(761884, 10**6)
assert p5_lower > Q(760783, 10**6)

print("PASS live complement-train / detour split certified")
print("epsilon =", float(epsilon))
print("delta_max =", float(delta_max))
print("complement threshold =", float(eta))
print("detour cut =", float(delta_cut))
print("Phi(delta_cut) rigorous lower margin =", float(margin))
print("remaining a+2r budget =", float(remaining_budget))
print("r max =", float(r_max))
print("f lower >", float(f_lower))
print("f upper <", float(f_upper))
print("P5 lower >", float(p5_lower))
