#!/usr/bin/env python3
"""Exact rational interval certificate for the EFAQ uniform perimeter cap.

Proves P_r(X) < 3.010 for every X^2 in [0.4524, 0.5476],
which contains the Target C interval [sin(rho)^2, rho^2].

Only Python standard-library integer/rational arithmetic is used. Square roots
are enclosed outward by integer square roots at a fixed rational scale.
"""

from fractions import Fraction
from math import isqrt

SCALE = 10**18
BINS = 1000


def sqrt_bounds(x: Fraction):
    """Return rational lo <= sqrt(x) < hi with denominator SCALE."""
    assert x >= 0
    floor_scaled_sq = (x.numerator * SCALE * SCALE) // x.denominator
    a = isqrt(floor_scaled_sq)
    lo = Fraction(a, SCALE)
    hi = Fraction(a + 1, SCALE)
    assert lo * lo <= x
    assert hi * hi > x
    return lo, hi


# EFAQ constants for r=24/25.
r2 = Fraction(576, 625)
sqrt481_lo, sqrt481_hi = sqrt_bounds(Fraction(481, 1))
k_lo = Fraction(96, 625) * sqrt481_lo  # lower bound for 4*r*h

# Deliberately enlarge [sin(rho)^2, rho^2] using 0.739<rho<0.740.
T_LO = Fraction(4524, 10000)  # 1 - 0.74^2
T_HI = Fraction(5476, 10000)  # 0.74^2
TARGET = Fraction(301, 100)    # 3.010


def perimeter_upper(t_lo: Fraction, t_hi: Fraction):
    # z=sqrt(t(1-t)) is concave, so its minimum on an interval is at an endpoint.
    z2_lo = min(t_lo * (1 - t_lo), t_hi * (1 - t_hi))
    z_lo, _ = sqrt_bounds(z2_lo)

    # EFAQ.3/EFAQ.4 with t=X^2 and z=XY:
    # q^2 = 576/625 + 1348/625*t - (96*sqrt(481)/625)*z
    # s^2 = 1777/625 - 1152/625*t - (96*sqrt(481)/625)*z.
    # Use monotonic endpoint choices and lower bounds in the subtracted product.
    q2_hi = (
        Fraction(576, 625)
        + Fraction(1348, 625) * t_hi
        - k_lo * z_lo
    )
    s2_hi = (
        Fraction(1777, 625)
        - Fraction(1152, 625) * t_lo
        - k_lo * z_lo
    )
    _, q_hi = sqrt_bounds(q2_hi)
    _, s_hi = sqrt_bounds(s2_hi)

    # 1+r = 49/25.
    return Fraction(49, 25) + q_hi + s_hi


max_upper = Fraction(0, 1)
max_bin = -1
span = T_HI - T_LO
for i in range(BINS):
    lo = T_LO + span * i / BINS
    hi = T_LO + span * (i + 1) / BINS
    upper = perimeter_upper(lo, hi)
    if upper > max_upper:
        max_upper = upper
        max_bin = i

assert max_upper < TARGET, (max_upper, max_bin)

print("CERTIFIED")
print("bins:", BINS)
print("t interval:", T_LO, T_HI)
print("max bin:", max_bin)
print("exact max upper numerator:", max_upper.numerator)
print("exact max upper denominator:", max_upper.denominator)
print("max upper decimal:", format(float(max_upper), ".15f"))
print("target:", float(TARGET))
print("rational margin positive:", TARGET - max_upper)
