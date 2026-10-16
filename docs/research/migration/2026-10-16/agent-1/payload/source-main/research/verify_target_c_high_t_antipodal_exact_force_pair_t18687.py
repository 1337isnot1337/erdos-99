#!/usr/bin/env python3
"""Regression checks for the exact-antipodal force-pair theorem."""

from fractions import Fraction
from math import cos, sin, pi


def close(a: float, b: float, eps: float = 2e-12) -> bool:
    return abs(a - b) <= eps


# Exact two-ray bracketing identity, sampled over a range of strict cones.
for p, q in [
    (0.01, 0.02),
    (0.2, 0.7),
    (0.9, 1.1),
    (1.4, 1.6),
    (0.001, pi - 0.002),
]:
    assert p > 0 and q > 0 and p + q < pi
    cm = sin(q) / sin(p + q)
    cp = sin(p) / sin(p + q)
    assert cm > 0 and cp > 0
    dm = (cos(p), -sin(p))
    dp = (cos(q), sin(q))
    x = cm * dm[0] + cp * dp[0]
    y = cm * dm[1] + cp * dp[1]
    assert close(x, 1.0)
    assert close(y, 0.0)

# Density/extraction constant inherited from the EA-dominant fork.
c1 = Fraction(791, 320_000_000)
assert c1 > 0
# AF.6 coefficient is c1/(16*3^(1/8)); verify its numerical positivity only.
coef = float(c1) / (16.0 * (3.0 ** (1.0 / 8.0)))
assert 1.3e-7 < coef < 1.4e-7

# A constant-phase block with one-sided scalar differences telescopes exactly.
A = [100.0, 91.0, 74.0, 60.0]
variation = sum(abs(A[j] - A[j + 1]) for j in range(len(A) - 1))
assert close(variation, abs(A[0] - A[-1]))

print("PASS: exact-antipodal force-pair and phase-block monotonicity regressions")
