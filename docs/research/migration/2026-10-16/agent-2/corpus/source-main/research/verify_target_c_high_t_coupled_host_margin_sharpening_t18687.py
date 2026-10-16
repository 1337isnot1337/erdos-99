#!/usr/bin/env python3
"""Regression checks for the coupled high-t host-margin sharpening."""

import math

z0 = 2.0477
d0 = z0 - 6 * math.sin(z0 / 6)
c = 0.4143 + d0
gamma = math.asin(c)
theta = math.acos(c)

assert 0.03951 < d0 < 0.03953
assert 0.45381 < c < 0.45383
assert abs(gamma + theta - math.pi / 2) < 1e-15
assert 26.98 < math.degrees(gamma) < 27.00
assert 63.00 < math.degrees(theta) < 63.02
assert 126.00 < 2 * math.degrees(theta) < 126.04

slope = 2 * c
side_fraction = c / (1 + c)
transverse_fraction = c / 2
axial_ceiling = math.sqrt(1 - c * c)
stress_factor = 1 / axial_ceiling

assert 0.90763 < slope < 0.90765
assert 0.31215 < side_fraction < 0.31217
assert 0.22690 < transverse_fraction < 0.22692
assert 0.89108 < axial_ceiling < 0.89110
assert 1.12220 < stress_factor < 1.12223

# Every displayed host-derived constant strictly improves the coarse c=0.4143
# version used before the coupled detour lower bound was fed back into lambda.
coarse = 0.4143
assert c > coarse
assert slope > 2 * coarse
assert side_fraction > coarse / (1 + coarse)
assert transverse_fraction > coarse / 2
assert axial_ceiling < math.sqrt(1 - coarse * coarse)
assert stress_factor > 1 / math.sqrt(1 - coarse * coarse)

print("PASS: coupled high-t host-margin sharpening regressions")
print("d0 =", d0)
print("host transverse floor =", c)
print("host margin degrees =", math.degrees(gamma))
print("dipole slope coefficient =", slope)
print("each-side stress fraction =", side_fraction)
print("transverse moment fraction =", transverse_fraction)
print("axial component ceiling =", axial_ceiling)
print("stress/reaction factor =", stress_factor)
