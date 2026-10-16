#!/usr/bin/env python3
"""Exact-rational certificate for the terminal FREE t-gap 0.00659.

The mathematical note proves the geometric implications. This script certifies only
its scalar/algebraic part with rational arithmetic:

  * outward enclosures for pi, sqrt(3), Delta_2 and sqrt(Delta_2);
  * the two-bin residual cap r < 0.04111 at epsilon = 0.00659;
  * F(1.5286) > delta_max = 0.016475 using an alternating Taylor bound;
  * monotonicity of the joint retention/incidence margin on the feasible z interval;
  * a positive rational contradiction margin > 2.27e-4;
  * the reported terminal t and chamber-interface constants.

No floating-point quantity is load-bearing.
"""

from fractions import Fraction
from math import isqrt

Q = Fraction


def atan_inv_bounds(q: int, terms: int):
    """Alternating-series enclosure for atan(1/q)."""
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

# Machin: pi = 16 atan(1/5) - 4 atan(1/239).
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo
assert pi_lo < pi_hi

# sqrt(3) and Delta_2 = pi/(2 sqrt(3)).
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
assert sqrt3_lo * sqrt3_lo < 3 < sqrt3_hi * sqrt3_hi

delta2_lo = pi_lo / (2 * sqrt3_hi)
delta2_hi = pi_hi / (2 * sqrt3_lo)
s2_lo = sqrt_floor(delta2_lo, SCALE)
s2_hi = sqrt_ceil(delta2_hi, SCALE)
assert s2_lo * s2_lo <= delta2_lo
assert s2_hi * s2_hi >= delta2_hi

# Safe gap and stability box.
g = Q(7707, 10**6)
epsilon = Q(659, 100000)  # 0.00659
a_max = 5 * epsilon         # train-slack excess
delta_max = Q(5, 2) * epsilon  # outer directional-energy/detour budget
assert delta_max == Q(659, 40000)

# The all-train scalar is C = 2 sqrt(Delta_2) + g + a.
# r_2(C) = (C - sqrt(8 Delta_2 - C^2))/2 is increasing on the live box.
C_hi = 2 * s2_hi + g + a_max
radicand_lo = 8 * delta2_lo - C_hi * C_hi
assert radicand_lo > 0
sqrt_radicand_lo = sqrt_floor(radicand_lo, SCALE)
residual_hi = (C_hi - sqrt_radicand_lo) / 2
residual_cap = Q(4111, 100000)  # 0.04111
assert residual_hi < residual_cap

# F(z)=z-6 sin(z/6). For x=z/6, sin x <= x-x^3/6+x^5/120,
# hence F(z) >= z^3/216-z^5/155520.
z0 = Q(7643, 5000)  # 1.5286
Fz0_lower = z0**3 / 216 - z0**5 / 155520
assert Fz0_lower > delta_max

# H(z)=pi/2-r-z-[r^2+delta-F(z)]/[2(1-delta)].
# H'(z)=-1+F'(z)/[2(1-delta)]. On 0<=z<=z0,
# F'(z)=1-cos(z/6)<=z^2/72 <= z0^2/72 < 1/30,
# so H'<0 throughout the entire stability box.
Fp_cap = z0 * z0 / 72
assert Fp_cap < Q(1, 30)
assert Q(1, 30) / (2 * (1 - delta_max)) < 1

# Since every energetically feasible z has z<z0, decreasing H implies
# H(z)>H(z0). At z0, F(z0)>delta, so it is enough to certify the still
# weaker lower bound obtained by replacing delta-F(z0) with zero.
margin = (
    pi_lo / 2
    - residual_cap
    - z0
    - residual_cap**2 / (2 * (1 - delta_max))
)
assert margin > Q(227, 10**6)  # > 0.000227

# Reported floor. mu_* = pi/2 + (2/5)sqrt(Delta_2) + g/5.
t_floor_lo = pi_lo / 2 + Q(2, 5) * s2_lo + g / 5 + epsilon
t_report = Q(1959852849, 10**9)  # 1.959852849, safe truncated decimal
assert t_floor_lo > t_report

# The matched terminal chamber-interface relation is H_ch/D >= t + gamma_g,
# gamma_g = 2 sqrt(Delta_2) - pi/2 + g.
gamma_lo = 2 * s2_lo - pi_hi / 2 + g
chamber_floor_lo = t_floor_lo + gamma_lo
chamber_report = Q(2301389, 10**6)  # 2.301389
assert chamber_floor_lo > chamber_report

# Multiplying by sqrt(3)/4 gives the raw inactive-chamber Oler surplus.
oler_floor_lo = sqrt3_lo * chamber_floor_lo / 4
oler_report = Q(99653, 100000)  # 0.99653
assert oler_floor_lo > oler_report

print("PASS: terminal FREE t-gap 0.00659 certified")
print("epsilon =", float(epsilon))
print("delta_max =", float(delta_max))
print("a_max =", float(a_max))
print("two-bin residual upper <", float(residual_cap))
print("F(1.5286) lower =", float(Fz0_lower))
print("joint contradiction margin >", float(margin))
print("t floor >", float(t_floor_lo))
print("chamber-interface floor >", float(chamber_floor_lo))
print("Oler chamber surplus floor >", float(oler_floor_lo))
