#!/usr/bin/env python3
"""Regression checks for ordered bilateral narrow-force-pair capacity."""

from fractions import Fraction
from math import asin, sin

c0 = Fraction(113, 20_000_000)
c = Fraction(113, 5_000_000)
p0 = Fraction(2599, 960_000_000)

# If eta increases by at least 2*delta along an ordered bilateral family,
# eta < rho can occur on at most rho/(2 delta)+1 indices.
# Exhaust finite integer models with delta normalized to 1.
for n in range(1, 9):
    # Minimal possible boundary distances under opposite lane order.
    a = [i for i in range(n)]
    b = [i for i in range(n)]
    eta = [a[i] + b[i] for i in range(n)]
    for rho in range(1, 18):
        N = sum(x < rho for x in eta)
        assert N <= rho / 2 + 1
        # Narrow set is an initial segment.
        seen_wide = False
        for x in eta:
            if x >= rho:
                seen_wide = True
            if seen_wide:
                assert x >= rho

# More general increasing lane increments >=1.
for a_step in (1, 2, 3):
    for b_step in (1, 2, 4):
        eta = [3 + (a_step + b_step) * i for i in range(12)]
        for rho in range(1, 40):
            N = sum(x < rho for x in eta)
            assert N <= rho / 2 + 1

# New robust fork: subtract rho/2 instead of rho.
# One-power product rho*(c0-rho/2)/2 is maximized at rho=c0.
rho1 = c0
pop1 = (c0 - rho1 / 2) / 2
assert pop1 == c0 / 4
prod1 = rho1 * pop1
assert prod1 == c0 * c0 / 4

# Previous one-arc theorem: rho=c0/2, same population c0/4.
old_rho1 = c0 / 2
old_pop1 = (c0 - old_rho1) / 2
old_prod1 = old_rho1 * old_pop1
assert old_pop1 == c0 / 4
assert prod1 == 2 * old_prod1

# Square-weighted product is maximized at rho=4c0/3.
rho2 = 4 * c0 / 3
pop2 = (c0 - rho2 / 2) / 2
assert pop2 == c0 / 6
prod2 = rho2 * rho2 * pop2
assert prod2 == Fraction(8, 27) * c0**3

# Previous one-arc square optimum was rho=2c0/3 at the same population.
old_rho2 = 2 * c0 / 3
old_pop2 = (c0 - old_rho2) / 2
old_prod2 = old_rho2 * old_rho2 * old_pop2
assert old_pop2 == c0 / 6
assert prod2 == 4 * old_prod2

# Fixed-depth loss improves from m*rho to m*rho/2.
for r in range(20):
    m = 2 * r + 1
    rho = Fraction(1, 10_000_000)
    eta0 = Fraction(1, 100_000_000)
    etar = Fraction(1, 100_000_000)
    old = c / 2 - eta0 - etar - m * rho
    new = c / 2 - eta0 - etar - m * rho / 2
    assert new - old == m * rho / 2

# At the existing adjacent-double-cell aperture rho*=p0/8,
# narrow interfaces cost only p0/16 D and spoil at most p0/8 D cells.
rhostar = p0 / 8
narrow = rhostar / 2
spoiled = 2 * narrow
remain = p0 - spoiled
assert remain == 7 * p0 / 8

# TT block baseline: opposite lane order forces ordinary separation at the
# first cell to be at least 2*gamma + 2(M-1)*delta.
z0 = 2.0477
d0 = z0 - 6 * sin(z0 / 6)
cH = 0.4143 + d0
gammaH = asin(cH)
for D in (10_000, 100_000, 1_000_000):
    delta = 2 * asin(1 / (2 * D))
    for M in (1, 2, 5, 20):
        lower = 2 * gammaH + 2 * (M - 1) * delta
        assert lower >= 2 * gammaH
        if M > 1:
            assert lower > 2 * gammaH

# Near-full TT regime if TT is the winning c/6 block.
theta = float(c) / 6
span = 2 * gammaH + 2 * theta
chord = sin(gammaH + theta)
assert span > 2 * gammaH
assert chord > cH

print("PASS: ordered bilateral narrow-force-pair capacity regressions")
print(f"c0={float(c0):.12g}")
print(f"rho_linear={float(rho1):.12g} population={float(pop1):.12g} product={float(prod1):.12g}")
print(f"rho_square={float(rho2):.12g} population={float(pop2):.12g} product={float(prod2):.12g}")
print(f"double_cell_retention={float(remain):.12g}")
print(f"gamma_H={gammaH:.12g} two_gamma_H={2*gammaH:.12g}")
print(f"near_full_TT_span={span:.12g} chord_ratio={chord:.12g}")