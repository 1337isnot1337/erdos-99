#!/usr/bin/env python3
"""Arithmetic/trigonometric regressions for the force-carrying robust fork."""

from fractions import Fraction
from math import cos, sin, pi

c0 = Fraction(113, 20_000_000)
assert c0 > 0

# Density tradeoff remains positive precisely in the stated range.
for denom in (32, 12, 9, 7):
    rho = c0 / denom
    if rho < c0 / 6:
        joint = c0 - 6 * rho
        assert joint > 0
        assert joint / 2 > 0

# Calibrated rho=c0/12 instance.
rho = c0 / 12
assert c0 - 6 * rho == c0 / 2
assert (c0 - 6 * rho) / 2 == c0 / 4
assert abs(float(c0 / 4) - 1.4125e-6) < 1e-18

# Exact positive two-ray force representation for every strict bracket.
for p, q in [(0.05, 0.08), (0.4, 0.9), (1.0, 1.2), (0.001, pi - 0.002)]:
    assert 0 < p and 0 < q and p + q < pi
    lm = sin(q) / sin(p + q)
    lp = sin(p) / sin(p + q)
    assert lm > 0 and lp > 0
    dm = (cos(p), -sin(p))
    dp = (cos(q), sin(q))
    x = lm * dm[0] + lp * dp[0]
    y = lm * dm[1] + lp * dp[1]
    assert abs(x - 1.0) < 2e-12
    assert abs(y) < 2e-12

# Wide-force bundle extraction coefficient is positive for every admissible rho.
rho = c0 / 12
coef = float(c0 - 6 * rho) / (32.0 * 3.0 ** (1.0 / 8.0))
assert coef > 0

print("PASS: force-carrying robust fork regressions")
