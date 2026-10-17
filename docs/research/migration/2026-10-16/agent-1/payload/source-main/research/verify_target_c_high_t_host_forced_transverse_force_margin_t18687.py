#!/usr/bin/env python3
"""Regression checks for the high-t host-forced transverse force margin."""

import math
from fractions import Fraction as Q

# Coupled-path terminal-energy threshold.
a = Q(5857, 10000)
c = 1 - float(a)
theta = math.acos(c)
gamma = math.asin(c)

assert abs((math.pi / 2 - theta) - gamma) < 1e-15
assert abs(math.sin(gamma) - c) < 1e-15
assert 0.42717 < gamma < 0.42718
assert 24.475 < math.degrees(gamma) < 24.476
assert abs(2 * math.sin(gamma) - 0.8286) < 1e-15

# The projective lower margin survives any collection of o(1) angular errors.
for eps in [1e-2, 1e-3, 1e-4, 1e-6]:
    lower = math.pi / 2 - theta - 3 * eps
    assert 0 < lower < gamma
    assert math.sin(lower) < c
    if eps <= 1e-4:
        assert math.sin(lower) > 0.4139

# If a diameter midpoint is eD from the near-disk center, the endpoint radial
# line differs from the diameter line by at most asin(e/(1/2-e)), which tends
# to zero with e.
prev = None
for e in [1e-1, 1e-2, 1e-3, 1e-4, 1e-6]:
    ratio = e / (0.5 - e)
    angle = math.asin(min(1.0, ratio))
    if prev is not None:
        assert angle < prev
    prev = angle
assert prev < 3e-6

# Removing the old axis-near deletion improves the displayed parameterized
# deep-force density from 90% to 92% of c0 for the same rho/eta choices.
c0 = Q(113, 20_000_000)
rho = c0 / Q(100, 1)
eta = c0 / Q(50, 1)
old_delta = c0 / Q(100, 1)
new_lambda = c0 - 6 * rho - eta
old_lambda = c0 - 6 * rho - eta - 2 * old_delta
assert new_lambda == Q(23, 25) * c0
assert old_lambda == Q(9, 10) * c0
assert abs(float(new_lambda) - 5.198e-6) < 1e-18
assert abs(float(old_lambda) - 5.085e-6) < 1e-18
assert new_lambda > old_lambda

# Exact-force coefficient algebra. If each lifted force ray has projective
# distance at least gamma from the reaction axis, then sin(p),sin(q)>=c.
# Since sin(p+q)<=1, both compressed positive coefficients are at least
# c |G|/D. Check a finite mesh of the admissible lifted cone.
for pdeg in range(25, 156, 5):
    p = math.radians(pdeg)
    if min(p, math.pi - p) + 1e-12 < gamma:
        continue
    for qdeg in range(25, 156, 5):
        q = math.radians(qdeg)
        if min(q, math.pi - q) + 1e-12 < gamma:
            continue
        if p + q >= math.pi:
            continue
        denom = math.sin(p + q)
        assert denom > 0
        assert math.sin(p) / denom >= c - 1e-12
        assert math.sin(q) / denom >= c - 1e-12

print("PASS: host-forced transverse force-margin regressions")
print("theta* deg =", math.degrees(theta))
print("gamma* deg =", math.degrees(gamma))
print("sin gamma* =", math.sin(gamma))
print("dipole slope coefficient =", 2 * math.sin(gamma))
print("old displayed density =", float(old_lambda))
print("new displayed density =", float(new_lambda))
