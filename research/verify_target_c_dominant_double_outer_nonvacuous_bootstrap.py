#!/usr/bin/env python3
"""Exact rational certificate for dominant O-O pair weight on t<=1.844."""

from fractions import Fraction as Q
from math import factorial, isqrt


def atan_inv_bounds(q: int, n: int):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2 * k + 1) * q ** (2 * k + 1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2 * n + 1) * q ** (2 * n + 1))
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def sqrt_bounds(lo: Q, hi: Q, scale: int):
    nlo = isqrt((lo.numerator * scale * scale) // lo.denominator)
    nhi = isqrt((hi.numerator * scale * scale) // hi.denominator)
    return Q(nlo, scale), Q(nhi + 1, scale)


def sin_bounds(x: Q, n: int = 24):
    s = Q(0)
    for k in range(n):
        term = x ** (2 * k + 1) / factorial(2 * k + 1)
        s += term if k % 2 == 0 else -term
    nxt = x ** (2 * n + 1) / factorial(2 * n + 1)
    return (s, s + nxt) if n % 2 == 0 else (s - nxt, s)


def F_bounds(z: Q):
    slo, shi = sin_bounds(z / 6)
    return z - 6 * shi, z - 6 * slo


# Exact enclosures for pi, sqrt(3), Delta2, and C71.
a5_lo, a5_hi = atan_inv_bounds(5, 80)
a239_lo, a239_hi = atan_inv_bounds(239, 20)
pi_lo = 16 * a5_lo - 4 * a239_hi
pi_hi = 16 * a5_hi - 4 * a239_lo

SCALE = 10 ** 80
n3 = isqrt(3 * SCALE * SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3 + 1, SCALE)
Delta_lo = pi_lo / (2 * sqrt3_hi)
Delta_hi = pi_hi / (2 * sqrt3_lo)
s_lo, s_hi = sqrt_bounds(Delta_lo, Delta_hi, SCALE)
C71_lo = 2 * s_lo + Q(71, 10000)
C71_hi = 2 * s_hi + Q(71, 10000)

T = Q(1844, 1000)
Ubase_lo = Q(9, 2) * T - 2 * pi_hi
Ubase_hi = Q(9, 2) * T - 2 * pi_lo
delta_max_hi = (Ubase_hi - C71_lo) / 2
assert delta_max_hi < Q(52, 1000)


def m2_bounds(Ulo: Q, Uhi: Q):
    xlo = 8 * Delta_lo - Uhi * Uhi
    xhi = 8 * Delta_hi - Ulo * Ulo
    assert xlo > 0
    rlo, rhi = sqrt_bounds(xlo, xhi, SCALE)
    return (Ulo + rlo) / 2, (Uhi + rhi) / 2


def bootstrap_step(z: Q):
    Flo, _ = F_bounds(z)
    Ulo = Ubase_lo - 2 * Flo
    Uhi = Ubase_hi - 2 * Flo
    assert Ulo > C71_lo

    mlo, _ = m2_bounds(Ulo, Uhi)
    rhi = Uhi - mlo
    Slo = pi_lo - Uhi - T / 2 + mlo

    numerator_hi = delta_max_hi - Flo + rhi * rhi
    assert numerator_hi > 0
    p_hi = numerator_hi / (2 * (1 - delta_max_hi))
    return Slo - p_hi, Flo, Uhi, rhi, Slo, p_hi


levels = [
    Q(0),
    Q(20720, 10000),
    Q(21850, 10000),
    Q(22033, 10000),
    Q(22064, 10000),
    Q(22069, 10000),
]

for i, z in enumerate(levels[:-1]):
    nxt, *_ = bootstrap_step(z)
    assert nxt > levels[i + 1]
    print(
        f"round {i}: z >= {float(z):.4f} -> {float(nxt):.15f} "
        f"> {float(levels[i + 1]):.4f}"
    )

z = levels[-1]
Flo, _ = F_bounds(z)
Uhi = Ubase_hi - 2 * Flo
pair_floor = z - Uhi

assert pair_floor > Q(29, 100)

print('C71 lower =', float(C71_lo))
print('delta_max upper =', float(delta_max_hi))
print('F(2.2069) lower =', float(Flo))
print('dominant-train mass upper =', float(Uhi))
print('dominant O-O pair floor =', float(pair_floor))
print('PASS: >0.29 D dominant train pair weight for every survivor with t<=1.844')
