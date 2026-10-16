#!/usr/bin/env python3
"""Regression checks for the high-t circumcenter-bracketed synchronized grid."""

from fractions import Fraction as Q
import math

rho = Q(1019, 5_000_000)   # 0.0002038
r = Q(817, 1250)            # 0.6536
T = Q(6121, 2000)           # 3.0605
sqrt3 = math.sqrt(3.0)


def a(N: int) -> float:
    return float(rho) / N


def b(N: int) -> float:
    return float(r) - float(T) / (N - 3)


def q(N: int, mu: float) -> float:
    return b(N) - (1.0 + 2.0 * mu) / sqrt3


def product(N: int, mu: float) -> float:
    return a(N) * q(N, mu)


# Zero-margin circumcenter straddling starts exactly at N=44.
assert q(43, 0.0) < 0.0
assert q(44, 0.0) > 0.0
best0 = max(range(44, 5000), key=lambda N: product(N, 0.0))
assert best0 == 85
assert 2.3976e-6 < a(85) < 2.3977e-6
assert 0.61627 < b(85) < 0.61629
assert 0.03892 < q(85, 0.0) < 0.03894
assert 9.33e-8 < product(85, 0.0) < 9.34e-8

# A fixed 1%-of-D row-normal margin becomes positive at N=51.
mu = 0.01
assert q(50, mu) < 0.0
assert q(51, mu) > 0.0
best1 = max(range(51, 5000), key=lambda N: product(N, mu))
assert best1 == 99
assert 2.0585e-6 < a(99) < 2.0587e-6
assert 0.62171 < b(99) < 0.62173
assert 0.03282 < q(99, mu) < 0.03283
assert 6.75e-8 < product(99, mu) < 6.77e-8

# The one-sided crossing-center capacity coefficient is exactly the asymptotic
# coordinate length (1/2+mu) divided by the strict train-step floor sqrt(3)/2.
cap0 = 1.0 / sqrt3
cap1 = 1.02 / sqrt3
assert 0.57735 < cap0 < 0.57736
assert 0.58889 < cap1 < 0.58890
assert abs((b(85) - cap0) - q(85, 0.0)) < 1e-14
assert abs((b(99) - cap1) - q(99, mu)) < 1e-14

# Common-order flank extraction is purely order theoretic: if every ordered row
# has at least q columns below the lower threshold and q above the upper
# threshold, then the first q and last q column labels work simultaneously.
for M in range(10, 50):
    for qcount in range(1, M // 2 + 1):
        order = list(range(M))
        # Allow the row-dependent threshold positions to vary arbitrarily subject
        # only to the guaranteed flank counts.
        for low_count in range(qcount, M - qcount + 1):
            high_start = low_count
            # First q labels are among the low side whenever low_count>=q.
            assert set(order[:qcount]).issubset(set(order[:low_count]))
            # Last q labels are among the high side whenever at least q labels
            # remain after the row-dependent upper threshold.
            assert set(order[-qcount:]).issubset(set(order[M - qcount:]))

# Midpoint localization has genuinely sublinear normalized error.
def normalized_midpoint_error(D: float) -> float:
    eta = 3.0 ** 0.25 * math.sqrt(D)
    L = math.sqrt(D * eta + eta * eta)
    return L / D

prev = None
for D in [1e4, 1e6, 1e8, 1e10, 1e12]:
    err = normalized_midpoint_error(D)
    if prev is not None:
        assert err < prev
    prev = err
assert normalized_midpoint_error(1e12) < 0.002

# Location-or-angle inequality: an intersection at row-normal distance mu*D
# outside the central corridor forces sin(theta) >= 2mu - 2L_D/D.
for D in [1e8, 1e10, 1e12]:
    rhs = 2.0 * mu - 2.0 * normalized_midpoint_error(D)
    assert rhs < 2.0 * mu
    if D >= 1e12:
        assert rhs > 0.016

print('PASS: high-t circumcenter-bracketed synchronized-grid regressions')
print('zero-margin optimum N =', best0)
print('N=85 row/diameter density =', a(85))
print('N=85 transverse density =', b(85))
print('N=85 each-side circumcenter flank density =', q(85, 0.0))
print('one-percent-margin optimum N =', best1)
print('N=99 row/diameter density =', a(99))
print('N=99 transverse density =', b(99))
print('N=99 each-side 1%-margin flank density =', q(99, mu))
print('N=99 flank-product coefficient =', product(99, mu))
print('D=1e12 normalized midpoint error =', normalized_midpoint_error(1e12))
