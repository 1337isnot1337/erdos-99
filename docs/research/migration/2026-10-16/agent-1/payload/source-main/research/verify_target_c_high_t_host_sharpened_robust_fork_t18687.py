#!/usr/bin/env python3
"""Regression checks for the host-sharpened high-t robust fork."""

import math
from fractions import Fraction as Q

c0 = Q(113, 20_000_000)
gamma = math.asin(0.4143)
assert 0.42717 < gamma < 0.42718
assert abs(math.sin(gamma) - 0.4143) < 1e-15

# New robust combined density c0-2*rho is positive exactly for rho<c0/2.
assert c0 - 2 * (c0 / Q(2, 1)) == 0
assert c0 - 2 * (c0 / Q(3, 1)) > 0

# Linear angle-density product rho(c0-2rho)/2 is maximized at c0/4;
# the quadratic product is maximized at c0/3.
def linear_product(rho):
    return float(rho * (c0 - 2 * rho) / 2)


def quadratic_product(rho):
    return float(rho * rho * (c0 - 2 * rho) / 2)


rho_linear = c0 / Q(4, 1)
rho_quadratic = c0 / Q(3, 1)
assert linear_product(rho_linear) > linear_product(c0 / Q(5, 1))
assert linear_product(rho_linear) > linear_product(c0 * Q(3, 10))
assert quadratic_product(rho_quadratic) > quadratic_product(c0 / Q(4, 1))
assert quadratic_product(rho_quadratic) > quadratic_product(c0 * Q(2, 5))
assert (c0 - 2 * rho_linear) / 2 == c0 / Q(4, 1)
assert (c0 - 2 * rho_quadratic) / 2 == c0 / Q(6, 1)

# With the old displayed rho/eta choices, removing the 4*rho TB1 loss and
# 2*delta axis-near loss improves the deep-force coefficient 90% -> 96%.
rho = c0 / Q(100, 1)
eta = c0 / Q(50, 1)
new_density = c0 - 2 * rho - eta
old_density = c0 - 6 * rho - eta - 2 * (c0 / Q(100, 1))
assert new_density == Q(24, 25) * c0
assert old_density == Q(9, 10) * c0
assert abs(float(new_density) - 5.424e-6) < 1e-18
assert abs(float(old_density) - 5.085e-6) < 1e-18

# The host-forced TB1 margin is a fixed macroscopic constant, independent of
# the tiny rho scales used for the exact-antipodal pair-gap extraction.
assert math.sin(gamma) > float(c0) * 70_000

print("PASS: host-sharpened robust-fork regressions")
print("c0 =", float(c0))
print("host TB1 sine margin =", math.sin(gamma))
print("linear-product rho =", float(rho_linear), "side density =", float(c0 / Q(4, 1)))
print("quadratic-product rho =", float(rho_quadratic), "side density =", float(c0 / Q(6, 1)))
print("old displayed deep density =", float(old_density))
print("new displayed deep density =", float(new_density))
