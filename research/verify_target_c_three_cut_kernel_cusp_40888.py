#!/usr/bin/env python3
"""Exact outward certificate: optimize the canonical three-cut kernel cusp to 40888."""
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
    b = isqrt((hi.numerator * scale * scale) // hi.denominator) + 1
    return Q(a, scale), Q(b, scale)


def sin_bounds(x, n=30):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_lower(z):
    _, shi = sin_bounds(z / 6)
    return z - 6 * shi


# Audited 0.7404 fan inputs and fixed rational path thresholds.
A = Q(1851, 2500)
P = Q(53, 625)
N = Q(1063, 1000)
lam = Q(13553, 20000)  # .67765
r = Q(9713, 20000)     # .48565

g = (A - lam) * P / (N - lam)
d_top = lam - (1 - r) * N
d_low = lam - r * N
p = d_top * g / (r * N)
assert A > lam and d_top > 0 and d_low > 0 and p > 0

# Current exact q/D upper from the matched atomic envelope plus z>2.217.
SCALE = 10**100
a5_lo, a5_hi = atan_inv_bounds(5, 100)
a239_lo, a239_hi = atan_inv_bounds(239, 30)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C707_lo = 2 * s_lo + Q(7707, 1_000_000)

T = Q(461, 250)
Rt_hi = Q(9, 2) * T - 2 * pi_lo - C707_lo
delta_lo = F_lower(Q(2217, 1000))
kappa_hi = 2 * (Rt_hi - 2 * delta_lo)
q_hi = T + kappa_hi
switch_budget = 2 * q_hi
assert q_hi < Q(184855, 100000)
assert switch_budget < Q(36971, 10000)

# Standard outward angular-defect bound.
pi_up = Q(355, 113)
sqrt3_up = Q(17321, 10000)
C_phase_up = pi_up * pi_up * sqrt3_up * (2 + sqrt3_up) / 12

K = (switch_budget + 2 + 2 * C_phase_up / d_low) / p
K3 = 2 * K
assert K3 < Q(40888)
assert Q(40888) - K3 > Q(4, 5)
assert Q(42400) - K3 > Q(1512)

print("PASS canonical three-cut kernel cusp <40888")
print("lambda =", float(lam), "r =", float(r))
print("good-leaf density =", float(g))
print("d_top =", float(d_top), "d_low =", float(d_low))
print("path density =", float(p))
print("q/D upper =", float(q_hi))
print("switch budget density =", float(switch_budget))
print("one-boundary constant =", float(K))
print("three-cut two-boundary constant =", float(K3))
print("margin to 40888 =", float(Q(40888) - K3))
