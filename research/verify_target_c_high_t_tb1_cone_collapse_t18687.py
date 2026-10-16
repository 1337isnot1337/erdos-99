#!/usr/bin/env python3
"""Regression checks for the high-t TB1 cone-collapse theorem."""

import math

c = 0.4143
gamma = math.asin(c)
C = 31.4e6

assert 0.42717 < gamma < 0.42718
assert abs(math.sin(gamma) - c) < 1e-15

# Once the common projective phase window is smaller than gamma, the
# small-ordinary-angle branch min(theta, pi-theta)=theta is incompatible with
# the host-strong lower bound theta >= 2 gamma-o(1). The surviving branch is
# theta=pi-O(1/D).
for D in [1e9, 1e10, 1e12]:
    omega = C / D
    assert omega < gamma

    theta_small = omega
    assert theta_small < 2 * gamma

    theta_large = math.pi - omega
    assert abs(min(theta_large, math.pi - theta_large) - omega) < 1e-14

    # For a=(1,0), b=(cos(theta),sin(theta)), the unit opening cone has angular
    # interval [theta-pi/2, pi/2], hence width pi-theta.
    left = theta_large - math.pi / 2
    right = math.pi / 2
    assert abs((right - left) - omega) < 1e-14

# If a local opening direction differs from a common opening axis by O(1/D),
# a D-sized blocker dot product changes by only O(1); after division by D the
# host lower margin still converges to 0.4143.
for D in [1e9, 1e10, 1e12]:
    eps = C / D
    normalized_lower = c - eps
    assert normalized_lower < c
    if D >= 1e12:
        assert normalized_lower > 0.41426

threshold = C / gamma
assert 73e6 < threshold < 74e6

print("PASS: high-t TB1 cone-collapse regressions")
print("gamma* radians =", gamma)
print("gamma* degrees =", math.degrees(gamma))
print("C/gamma* =", threshold)
for D in [1e9, 1e10, 1e12]:
    print(
        "D", D,
        "opening-width upper rad", C / D,
        "common-axis normalized blocker floor", c - C / D,
    )
