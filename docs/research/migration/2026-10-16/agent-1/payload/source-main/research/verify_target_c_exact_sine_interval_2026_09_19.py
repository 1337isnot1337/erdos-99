#!/usr/bin/env python3
"""Exact rational enclosures for sin(pi*x) on rational intervals.

This is a reusable proof utility for Target C law-of-sines cycle exclusions.
All arithmetic used for certificate decisions is fractions.Fraction. No
floating-point value is used in an assertion.
"""
from fractions import Fraction as F
from math import factorial


def atan_partial(x, nterms):
    return sum(
        ((-1) ** k) * x ** (2 * k + 1) / F(2 * k + 1)
        for k in range(nterms)
    )


def atan_bounds(x, even_terms=12):
    """Alternating-series bounds for atan(x), 0<x<1."""
    assert F(0) < x < F(1)
    assert even_terms >= 2 and even_terms % 2 == 0
    lo = atan_partial(x, even_terms)
    hi = atan_partial(x, even_terms + 1)
    assert lo < hi
    return lo, hi


def pi_bounds():
    """Machin: pi/4 = 4 atan(1/5) - atan(1/239)."""
    a_lo, a_hi = atan_bounds(F(1, 5), 12)
    b_lo, b_hi = atan_bounds(F(1, 239), 6)
    # Exact tangent check for the Machin identity: tan(4a)=120/119,
    # tan(b)=1/239, and tan(4a-b)=1 because numerator=denominator.
    t4a = F(120, 119)
    tb = F(1, 239)
    assert t4a - tb == 1 + t4a * tb
    lo = 4 * (4 * a_lo - b_hi)
    hi = 4 * (4 * a_hi - b_lo)
    assert lo < hi
    # Coarse classical bounds are checked only as exact rational sanity tests.
    assert F(333, 106) < lo
    assert hi < F(355, 113)
    return lo, hi


PI_LO, PI_HI = pi_bounds()


def sin_partial(y, nterms):
    return sum(
        ((-1) ** k) * y ** (2 * k + 1) / F(factorial(2 * k + 1))
        for k in range(nterms)
    )


def sin_positive_bounds(y_lo, y_hi, even_terms=10):
    """Bound sin(y) for 0<=y_lo<=y<=y_hi<=pi/2.

    S_even is a lower bound and S_odd is an upper bound because the sine
    series alternates with decreasing term magnitudes on [0,pi/2].
    """
    assert F(0) <= y_lo <= y_hi <= PI_HI / 2
    assert (PI_HI / 2) ** 2 < 6  # first sine-term ratio < 1; later ratios are smaller
    assert even_terms >= 2 and even_terms % 2 == 0
    lo = sin_partial(y_lo, even_terms)
    hi = sin_partial(y_hi, even_terms + 1)
    assert lo <= hi
    return lo, hi


def sin_pi_point_bounds(q):
    """Exact rational enclosure of sin(pi*q), for rational 0<=q<=1."""
    q = F(q)
    assert F(0) <= q <= F(1)
    q = min(q, 1 - q)
    if q == 0:
        return F(0), F(0)
    y_lo = q * PI_LO
    y_hi = q * PI_HI
    return sin_positive_bounds(y_lo, y_hi)


def sin_pi_interval_bounds(lo, hi):
    """Enclose sin(pi*x) for every x in rational interval [lo,hi] subset [0,1]."""
    lo, hi = F(lo), F(hi)
    assert F(0) <= lo <= hi <= F(1)
    half = F(1, 2)

    if hi <= half:
        mn_lo, _ = sin_pi_point_bounds(lo)
        _, mx_hi = sin_pi_point_bounds(hi)
        return mn_lo, mx_hi
    if lo >= half:
        mn_lo, _ = sin_pi_point_bounds(hi)
        _, mx_hi = sin_pi_point_bounds(lo)
        return mn_lo, mx_hi

    l_lo, _ = sin_pi_point_bounds(lo)
    r_lo, _ = sin_pi_point_bounds(hi)
    return min(l_lo, r_lo), F(1)


def product_ratio_bounds(numerators, denominators):
    """Rational enclosure for product sin(pi*a)/sin(pi*b).

    Each input item is a closed rational interval (lo,hi). Intervals must stay
    inside (0,1), so denominator sine lower bounds are positive.
    """
    assert len(numerators) == len(denominators)
    n_bounds = [sin_pi_interval_bounds(*iv) for iv in numerators]
    d_bounds = [sin_pi_interval_bounds(*iv) for iv in denominators]
    assert all(lo > 0 for lo, _ in d_bounds)

    lower = F(1)
    upper = F(1)
    for (nl, nu), (dl, du) in zip(n_bounds, d_bounds):
        lower *= nl / du
        upper *= nu / dl
    return lower, upper


# Basic exact special-angle checks. The enclosures need not hit the algebraic
# values exactly; they only need to contain them tightly enough for proof use.
lo6, hi6 = sin_pi_point_bounds(F(1, 6))
assert lo6 < F(1, 2) < hi6
lo2, hi2 = sin_pi_point_bounds(F(1, 2))
assert lo2 < F(1) < hi2

# Reproduce the quantitative H7b orbit-115 contradiction using only rational
# interval endpoints from the committed affine certificates. Open endpoints
# may be safely replaced by their closures for a strict >1 lower certificate.
orb115_num = ((F(5, 9), F(47, 69)), (F(1, 5), F(1, 3)), (F(5, 21), F(1, 3)))
orb115_den = ((F(0), F(4, 21)), (F(0), F(1, 15)), (F(0), F(1, 3)))
# Zero lower endpoints are harmless for denominators because only denominator
# upper bounds enter the lower product. Compute the lower product directly.
def lower_ratio_with_zero_den(num, den):
    out = F(1)
    for n_iv, d_iv in zip(num, den):
        nl, _ = sin_pi_interval_bounds(*n_iv)
        _, du = sin_pi_interval_bounds(*d_iv)
        assert du > 0
        out *= nl / du
    return out


orb115_lower = lower_ratio_with_zero_den(orb115_num, orb115_den)
assert orb115_lower > 1

# Orbit 146: the first two sine ratios are interval-certified; the third ratio
# is >1 by the already exact same-triangle angle-order certificate a62>a26.
orb146_num = ((F(1, 3), F(5, 9)), (F(2, 9), F(1, 3)))
orb146_den = ((F(0), F(1, 6)), (F(0), F(1)))
orb146_lower = lower_ratio_with_zero_den(orb146_num, orb146_den)
assert orb146_lower > 1

# A generic H6/H7 search can now prove any cycle product impossible whenever
# this rational lower bound exceeds one (or the corresponding upper bound is
# below one), without relying on decimal transcendental evaluation.
print("PASS: exact rational sine interval engine")
width = PI_HI - PI_LO
print("pi interval width numerator digits / denominator digits:", len(str(width.numerator)), len(str(width.denominator)))
print("orbit 115 rational cycle lower bound > 1:", orb115_lower > 1)
print("orbit 146 rational partial-cycle lower bound > 1:", orb146_lower > 1)
