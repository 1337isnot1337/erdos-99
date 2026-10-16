#!/usr/bin/env python3
"""Exact arithmetic certificate for correlated low-energy O-O path through t<=1.8623."""

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

T = Q(18623, 10000)
Umax_lo = Q(9, 2) * T - 2 * pi_hi
Umax_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Umax_hi - C76_lo) / 2
assert Q(0) < delta_max_hi < Q(93, 1000)
assert delta_max_hi < 1


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
    p_hi = numerator_hi / (2 * (1 - delta_max_hi))
    return Slo - p_hi


levels = [
    Q(0),
    Q(1933, 1000),
    Q(20379, 10000),
    Q(20549, 10000),
    Q(20578, 10000),
    Q(20583, 10000),
    Q(20584, 10000),
]

for i, z in enumerate(levels[:-1]):
    nxt = bootstrap_step(z)
    assert nxt > levels[i + 1]
    print(
        i,
        float(z),
        "->",
        float(nxt),
        "target",
        float(levels[i + 1]),
        "margin",
        float(nxt - levels[i + 1]),
    )

z0 = levels[-1]
Flo, _ = F_bounds(z0)
Uhi = Umax_hi - 2 * Flo
pair_floor = z0 - Uhi
assert pair_floor > Q(415, 10000)

# Correlated low-energy bound with lambda=.99:
# P_low >= z-U-delta/lambda
#       >= z-Umax+(2-1/lambda)F(z).
lam = Q(99, 100)
coeff = 2 - 1 / lam
assert coeff > 0
low_total = z0 - Umax_hi + coeff * Flo
assert low_total > Q(9, 10000)
low_phase = low_total / 3
assert low_phase > Q(3, 10000)

# Terminal-arc gap: 2 asin(.01)>.02.
# Path density >.0003 gives one nonhub switch boundary with <=20943 rows.
pi_up = Q(355, 113)
avg_switch_up = 2 * pi_up / Q(3, 10000)
assert avg_switch_up < 20944

print("delta_max upper =", float(delta_max_hi))
print("z lower =", float(z0))
print("F(z) lower =", float(Flo))
print("dominant O-O pair floor =", float(pair_floor))
print("correlated low-energy total floor =", float(low_total))
print("one-phase path density floor =", float(low_phase))
print("2*pi_up/0.0003 =", float(avg_switch_up), "< 20944")
print("PASS correlated low-energy dual path through t<=1.8623")
