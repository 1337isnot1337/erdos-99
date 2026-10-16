#!/usr/bin/env python3
"""Exact-rational certificate for the live universal flex reservoir.

No floating-point inequality is load-bearing. The script certifies:
  * with epsilon=0.00710 and c=0.31805, retained complement mass p<=c
    forces outer detour delta>0.00852;
  * the correlated k=3 fan lower bound then exceeds c whenever L_O/D<c;
  * without the energy feedback, the direct universal coefficient already
    exceeds 0.30956.
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
five_epsilon = 5 * epsilon         # 0.0355
c = Q(6361, 20000)                 # 0.31805
delta_cut = Q(213, 25000)          # 0.00852

# rho(delta)=r_2(2s_2+g+5eps-2delta).  For
# Phi_c(delta)=F(pi/2-rho(delta)-c)-delta,
# Phi_c'=F'(x)*(-rho')-1.  A uniform rational upper bound proves Phi_c'<0.
C_uniform_hi = 2 * s2_hi + g + five_epsilon
rad_uniform_lo = 8 * delta2_lo - C_uniform_hi * C_uniform_hi
assert rad_uniform_lo > 0
sqrt_rad_uniform_lo = sqrt_floor(rad_uniform_lo, SCALE)
minus_rho_prime_hi = 1 + C_uniform_hi / sqrt_rad_uniform_lo
Fp_hi = (pi_hi / 2) ** 2 / 72
assert minus_rho_prime_hi * Fp_hi < 1

# Prove Phi_c(delta_cut)>0.  Upper-bound rho and lower-bound the retained
# dominant mass x.  The alternating Taylor bound
# F(x)>=x^3/216-x^5/155520 is rigorous on this range.
C_cut_hi = 2 * s2_hi + g + five_epsilon - 2 * delta_cut
rad_cut_lo = 8 * delta2_lo - C_cut_hi * C_cut_hi
assert rad_cut_lo > 0
sqrt_rad_cut_lo = sqrt_floor(rad_cut_lo, SCALE)
rho_cut_hi = (C_cut_hi - sqrt_rad_cut_lo) / 2
x_cut_lo = pi_lo / 2 - rho_cut_hi - c
assert x_cut_lo > 0
assert x_cut_lo * x_cut_lo < 432
F_cut_lo = x_cut_lo**3 / 216 - x_cut_lo**5 / 155520
phi_margin = F_cut_lo - delta_cut
assert phi_margin > Q(17, 10**7)   # >1.7e-6

# k=3 fan constant.  p_*=M_*/5 and A_3=(pi-2p_*)/3.
# For a lower bound on A_3 use pi_lo and pstar_hi.
Mstar_hi = 4 * s2_hi + 2 * g
pstar_hi = Mstar_hi / 5
A3_lo = (pi_lo - 2 * pstar_hi) / 3

# Correlated stability gives
# Y_3/D >= A_3 -(2/3)ell +(5/3)delta -3epsilon.
# At ell<c and delta>delta_cut the limiting lower endpoint is:
fan_lower = A3_lo - Q(2, 3) * c + Q(5, 3) * delta_cut - 3 * epsilon
fan_margin = fan_lower - c
assert fan_margin > Q(58, 10**6)   # >5.8e-5

# Context: even without dominant-energy feedback, the direct Y_3/O-O handoff
# has coefficient (3/5)(A_3-3epsilon)>0.30956.
direct_c_lo = Q(3, 5) * (A3_lo - 3 * epsilon)
assert direct_c_lo > Q(30956, 100000)

print("PASS live universal flex reservoir certified")
print("epsilon =", float(epsilon))
print("universal flex coefficient c =", float(c))
print("detour cut =", float(delta_cut))
print("Phi_c(delta_cut) rigorous lower margin =", float(phi_margin))
print("fan lower endpoint =", float(fan_lower))
print("fan margin above c =", float(fan_margin))
print("direct coefficient without energy feedback >", float(direct_c_lo))
