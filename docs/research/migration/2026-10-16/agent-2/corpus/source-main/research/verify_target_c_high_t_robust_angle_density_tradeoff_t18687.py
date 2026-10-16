#!/usr/bin/env python3
"""Exact arithmetic regressions for the robust high-t angle/density tradeoff."""

from fractions import Fraction

c0 = Fraction(113, 20_000_000)


def total_density(rho: Fraction) -> Fraction:
    return c0 - 6 * rho


def winning_density(rho: Fraction) -> Fraction:
    return total_density(rho) / 2


# The fixed-angle theorem is the rho=c0/32 specialization.
rho32 = c0 / 32
assert total_density(rho32) == Fraction(13, 16) * c0
assert winning_density(rho32) == Fraction(13, 32) * c0
assert abs(float(rho32) - 1.765625e-7) < 1e-20
assert abs(float(winning_density(rho32)) - 2.2953125e-6) < 1e-18

# Linear angle*density calibration. For f(rho)=rho(c0-6rho)/2,
# the unique positive critical point is rho=c0/12 and it is a maximum.
rho12 = c0 / 12
assert total_density(rho12) == c0 / 2
assert winning_density(rho12) == c0 / 4
assert abs(float(rho12) - 4.708333333333333e-7) < 1e-20
assert abs(float(winning_density(rho12)) - 1.4125e-6) < 1e-18

# Quadratic angle^2*density calibration. For
# g(rho)=rho^2(c0-6rho)/2, the positive critical point is c0/9.
rho9 = c0 / 9
assert total_density(rho9) == c0 / 3
assert winning_density(rho9) == c0 / 6
assert abs(float(rho9) - 6.277777777777778e-7) < 1e-20
assert abs(float(winning_density(rho9)) - 9.416666666666666e-7) < 1e-18

# All displayed choices lie in the theorem's positive-density interval.
for rho in (rho32, rho12, rho9):
    assert 0 < rho < c0 / 6
    assert total_density(rho) > 0

# Direct finite-difference verification of the two claimed maximizers on a
# fine rational grid around the critical points. This is only a regression;
# the report proves them by differentiation.
def f1(rho: Fraction) -> Fraction:
    return rho * winning_density(rho)


def f2(rho: Fraction) -> Fraction:
    return rho * rho * winning_density(rho)

step = c0 / 100_000
for center, f in ((rho12, f1), (rho9, f2)):
    for k in range(-20, 21):
        rho = center + k * step
        if 0 < rho < c0 / 6:
            assert f(rho) <= f(center)

# The general density bookkeeping is exactly the parent c0 density minus
# 4*rho for boundary-near TB1 bars and 2*rho for narrow antipodal pairs.
for q in (24, 32, 48, 96):
    rho = c0 / q
    assert total_density(rho) == c0 - 4 * rho - 2 * rho

print("PASS: robust high-t angle/density tradeoff regressions")
print(f"c0={float(c0):.12g}")
print(f"rho32={float(rho32):.12g}, winner32={float(winning_density(rho32)):.12g}")
print(f"rho12={float(rho12):.12g}, winner12={float(winning_density(rho12)):.12g}")
print(f"rho9={float(rho9):.12g}, winner9={float(winning_density(rho9)):.12g}")
