#!/usr/bin/env python3
"""Exact arithmetic certificate for same-host diameter exclusion and sharpened densities."""

from fractions import Fraction as Q
from decimal import Decimal, getcontext

getcontext().prec = 60

# Adaptive threshold ceiling a=0.5857. If theta0=acos(1-a), then
# sin(theta0)^2 = 1-(1-a)^2. A rational 0.911 upper bound leaves
# a fixed macroscopic gap from diameter length.
a = Q(5857, 10000)
c0 = 1 - a
sin2 = 1 - c0 * c0
assert c0 == Q(4143, 10000)
assert sin2 == Q(82835551, 100000000)
assert sin2 < Q(911, 1000) ** 2

# Unconditional fork density and improved two-piece physical pigeonhole.
s0 = Q(791, 320_000_000)
mu_old = s0 / 6
mu_new = s0 / 4
assert mu_new == Q(791, 1_280_000_000)
assert mu_new > mu_old

# Numerical endpoint-disjoint coefficient s0/(16*3^(1/8)).
D = Decimal
root8_3 = D(3) ** (D(1) / D(8))
coeff = (D(s0.numerator) / D(s0.denominator)) / (D(16) * root8_3)
assert D('1.34668e-7') < coeff < D('1.34670e-7')

# Current 90%-density deep exact-force choice.
lam = Q(5085, 1_000_000_000)  # 5.085e-6
mu_deep_old = lam / 3
mu_deep_new = lam / 2
assert mu_deep_old == Q(1695, 1_000_000_000)
assert mu_deep_new == Q(25425, 10_000_000_000)
assert mu_deep_new > mu_deep_old

deep_coeff = (D(lam.numerator) / D(lam.denominator)) / (D(8) * root8_3)
assert D('5.54064e-7') < deep_coeff < D('5.54067e-7')

print('PASS: same-host diameter exclusion constants and two-piece densities')
print('1-a =', float(c0))
print('sin(theta0)^2 =', float(sin2))
print('sin(theta0) < 0.911')
print('old unconditional physical density =', float(mu_old))
print('new unconditional physical density =', float(mu_new))
print('new unconditional disjoint coefficient =', coeff)
print('old deep physical density =', float(mu_deep_old))
print('new deep physical density =', float(mu_deep_new))
print('new deep disjoint coefficient =', deep_coeff)
