#!/usr/bin/env python3
"""Exact certificate for the repaired opposite-branch O-O dual path through t<=1.8593."""

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


def sin_bounds(x, n=20):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


a5_lo, a5_hi = atan_inv_bounds(5, 80)
a239_lo, a239_hi = atan_inv_bounds(239, 20)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10 ** 80
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo, sqrt3_hi = Q(n3, SCALE), Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C76_lo = 2 * s_lo + Q(19, 2500)

T = Q(18593, 10000)
Umax_lo = Q(9, 2) * T - 2 * pi_hi
Umax_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Umax_hi - C76_lo) / 2
assert delta_max_hi < Q(86, 1000)


def m2_bounds(Ulo, Uhi):
    xlo = 8 * Delta_lo - Uhi * Uhi
    xhi = 8 * Delta_hi - Ulo * Ulo
    assert xlo > 0
    rlo, rhi = sqrt_bounds(xlo, xhi, SCALE)
    return (Ulo + rlo) / 2, (Uhi + rhi) / 2


def bootstrap_step(z):
    Flo, _ = F_bounds(z)
    Ulo = Umax_lo - 2 * Flo
    Uhi = Umax_hi - 2 * Flo
    mlo, _ = m2_bounds(Ulo, Uhi)
    rhi = Uhi - mlo
    Slo = pi_lo - Uhi - T / 2 + mlo
    numerator_hi = delta_max_hi - Flo + rhi * rhi
    assert numerator_hi > 0
    return Slo - numerator_hi / (2 * (1 - delta_max_hi))


levels = [
    Q(0),
    Q(1957, 1000),
    Q(20634, 10000),
    Q(20807, 10000),
    Q(20837, 10000),
    Q(20842, 10000),
    Q(20843, 10000),
]

for i, z in enumerate(levels[:-1]):
    nxt = bootstrap_step(z)
    assert nxt > levels[i + 1]
    print(i, float(z), "->", float(nxt), "margin", float(nxt - levels[i + 1]))

z0 = levels[-1]
Flo, _ = F_bounds(z0)

# Use a threshold just above 1/2. Keeping delta correlated with U gives
# P_low >= z-Umax + (2-1/lambda) F(z).
lam = Q(201, 400)  # 0.5025
coeff = 2 - 1 / lam
assert coeff > 0
low_total = z0 - Umax_hi + coeff * Flo
assert low_total > Q(9, 10000)
assert low_total / 3 > Q(3, 10000)

# Opposite-branch repair.
# If both terminals used the same oriented normal branch, e_tau<=lambda implies
# sin((alpha+beta)/2) <= sqrt(lambda-lambda^2/4), hence terminal separation
# <= D*sqrt(lambda-lambda^2/4)+o(D).
# Section-157 bracing gives separation >=D*(1-delta-lambda/2)-o(D).
# Prove the latter coefficient is strictly larger using delta<=delta_max_hi.
rhs = 1 - delta_max_hi - lam / 2
lhs_sq = lam - lam * lam / 4
assert rhs > 0
assert rhs * rhs > lhs_sq

# Once opposite branches are forced, lambda<1 gives each deviation
# <pi/2 and hence two fixed disjoint terminal arcs.

# Density >0.0003 leaves one nonhub boundary with <=20943 switching rows.
pi_up = Q(355, 113)
avg_switch_up = 2 * pi_up / Q(3, 10000)
assert avg_switch_up < 20944

print("delta_max upper =", float(delta_max_hi))
print("z lower =", float(z0))
print("F(z) lower =", float(Flo))
print("opposite-branch squared margin =", float(rhs * rhs - lhs_sq))
print("correlated low-energy total >", float(low_total))
print("one-phase path density >", float(low_total / 3))
print("2*pi_up/0.0003 =", float(avg_switch_up), "< 20944")
print("PASS repaired opposite-branch dual path through t<=1.8593")
