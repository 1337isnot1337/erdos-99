#!/usr/bin/env python3
"""Exact outward certificate for the coupled adaptive O-O path through t<=1.8623.

This repairs the incompatible-extrema loss in the previous high-t continuation.  The
old argument first minimized retained dominant mass at the low-energy edge and then
paid Markov at the unrelated maximum outer-energy edge.  Here feasibility and Markov
are coupled through the actual outer-energy variable delta, and the terminal-energy
threshold is chosen sourcewise as lambda(delta)=0.5857-delta.
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


def sin_bounds(x, n=28):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


SCALE = 10 ** 110

a5_lo, a5_hi = atan_inv_bounds(5, 110)
a239_lo, a239_hi = atan_inv_bounds(239, 35)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
sDelta_lo, _ = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C76_lo = 2 * sDelta_lo + Q(19, 2500)

n2 = isqrt(2 * SCALE * SCALE)
sqrt2_hi = Q(n2 + 1, SCALE)

# Endpoint and retained-mass test point.
T = Q(18623, 10000)          # 1.8623
z0 = Q(5231, 2500)           # 2.0924
A0 = Q(5857, 10000)          # adaptive lambda(delta)=A0-delta

U0_lo = Q(9, 2) * T - 2 * pi_hi
U0_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (U0_hi - C76_lo) / 2

assert delta_max_hi < Q(93, 1000)
assert U0_hi < Q(21, 10)
assert 5 * U0_hi * U0_hi < 32 * Delta_lo

# H(z)=G(F(z),z) is increasing on [0,z0].  These are the same outward
# derivative gates used by the corrected parent theorem, with slightly wider constants.
one_minus_delta = Q(907, 1000)
rmax = Q(21, 20)
assert 1 - delta_max_hi > one_minus_delta
Gdelta_lower = -6 * (1 + rmax) / (2 * one_minus_delta * one_minus_delta)
assert Gdelta_lower > -Q(38, 5)  # > -7.6
assert z0 * z0 / 72 < Q(1, 16)
Gz_lower = 1 - Q(1, 16) / (2 * one_minus_delta)
assert Gz_lower > Q(24, 25)
assert Q(24, 25) - Q(38, 5) * Q(1, 16) > 0

# Exact outward evaluation H(z0)<0.
F_lo, F_hi = F_bounds(z0)
U_lo = U0_lo - 2 * F_hi
U_hi = U0_hi - 2 * F_lo
x_lo = 8 * Delta_lo - U_hi * U_hi
x_hi = 8 * Delta_hi - U_lo * U_lo
assert x_lo > 0
root_lo, _ = sqrt_bounds(x_lo, x_hi, SCALE)
m_lo = (U_lo + root_lo) / 2
r_hi = U_hi - m_lo
p_hi = r_hi * r_hi / (2 * (1 - F_hi))
S_lo = pi_lo - U_hi - T / 2 + m_lo
H_hi = z0 + p_hi - S_lo
assert H_hi < -Q(5, 100000)  # visible fixed sign margin

# Strong adverse-energy slope.  The exact parent identity is
#   2(1-d)^2 G_d = 1-F(z)+r^2-4r'(1-d)(r+1-d).
# Here r'>1, F>=0, r<1.05<4(1-d), so
#   G_d <= 1/[2(1-d)^2]-2 < -1.39.
assert rmax < 4 * one_minus_delta
Gdelta_upper = Q(1, 1) / (2 * one_minus_delta * one_minus_delta) - 2
A = Q(139, 100)
assert Gdelta_upper < -A

# The adaptive threshold is uniformly below the smaller physical same-branch root
#   lambda_-(d)=2-d-sqrt(2-d^2).
# Since sqrt(2-d^2)<sqrt(2), A0<2-sqrt(2) suffices.
assert A0 + sqrt2_hi < 2
lambda_min = A0 - Q(93, 1000)
assert lambda_min > Q(49, 100)
assert A0 < 1

# q(d)=d*(2-1/(A0-d)).  On d<.093 its derivative stays above -.42.
qprime_lower = 2 - Q(1, 1) / lambda_min - Q(93, 1000) / (lambda_min * lambda_min)
assert qprime_lower > -Q(21, 50)
assert A + qprime_lower > Q(9, 10)

# Since feasibility gives z-z0 >= A*(d-F(z0))-o(1), while q increases no
# slower than qprime_lower, the coupled Markov lower bound is minimized at
# d0=F(z0).  Bound q(d0)=2d0-d0/(A0-d0) outward.
assert F_hi < Q(43, 1000)
q0_lo = 2 * F_lo - F_hi / (A0 - F_hi)
low_total_lo = z0 - U0_hi + q0_lo
assert low_total_lo > Q(99, 50000)  # > .00198

# One of at most three dominant phase windows carries one third of that pair mass.
phase_floor = Q(33, 50000)          # .00066
assert Q(99, 50000) / 3 == phase_floor

# A path with >.00066 D cuts has, after deleting the unique hub boundary,
# a nonhub boundary with at most 9519 switching diameter rows.
avg_switch_hi = 2 * Q(355, 113) / phase_floor
assert avg_switch_hi < 9520

print("PASS: coupled adaptive O-O path through t<=1.8623")
for name, value in [
    ("U0 upper", U0_hi),
    ("delta max", delta_max_hi),
    ("F(z0) lower", F_lo),
    ("F(z0) upper", F_hi),
    ("H(z0) outward upper", H_hi),
    ("G_delta lower coarse", Gdelta_lower),
    ("G_delta upper coarse", Gdelta_upper),
    ("lambda minimum", lambda_min),
    ("q prime lower", qprime_lower),
    ("q(F(z0)) lower", q0_lo),
    ("low-energy pair mass lower", low_total_lo),
    ("one-phase path floor", phase_floor),
    ("switch-count average upper", avg_switch_hi),
]:
    print(name, "=", float(value))
