#!/usr/bin/env python3
"""Regression checks for exact diameter support-normal order."""

import math
import random

# Exact support-normal inequality for a model diameter pair. Whenever z lies
# within both radius-D endpoint disks, each diameter vector supports the lens
# at its own endpoint.
D = 1.0
x = (0.5, 0.0)
y = (-0.5, 0.0)
for _ in range(50_000):
    z = (random.uniform(-0.5, 0.5), random.uniform(-0.86, 0.86))
    if math.dist(z, x) <= D + 1e-12 and math.dist(z, y) <= D + 1e-12:
        dot_x = (x[0] - y[0]) * (z[0] - x[0]) + (x[1] - y[1]) * (z[1] - x[1])
        dot_y = (y[0] - x[0]) * (z[0] - y[0]) + (y[1] - x[1]) * (z[1] - y[1])
        assert dot_x <= 1e-12
        assert dot_y <= 1e-12

# Coupled-path host normal interval is strictly shorter than a semicircle.
c = 0.4143
theta = math.acos(c)
gamma = math.pi / 2 - theta
assert 2 * theta < math.pi
assert abs(gamma - math.asin(c)) < 1e-15
assert 24.475 < math.degrees(gamma) < 24.476

# C67 direction separation turns a linear number of exact ordered diameter
# normals into a fixed destination normal span asymptotic to lambda radians.
for lam in [1e-6, 1e-4, 0.01, 0.1]:
    for scale in [1e5, 1e7, 1e9]:
        M = int(lam * scale)
        if M < 2:
            continue
        span = (M - 1) * 2 * math.asin(1 / (2 * scale))
        assert span <= lam + 1e-8
        if scale >= 1e9:
            assert span > lam - 2e-8

print("PASS: exact diameter-normal order regressions")
print("host normal half-width degrees =", math.degrees(theta))
print("transverse margin degrees =", math.degrees(gamma))
print("host full normal width degrees =", 2 * math.degrees(theta))
