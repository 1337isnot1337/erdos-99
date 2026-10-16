#!/usr/bin/env python3
"""Regression checks for the high-t exact-antipodal stress-balance theorem."""

import math

c = 0.4143
s = math.sqrt(1.0 - c * c)
side_fraction = c / (1.0 + c)
transverse_fraction = c / 2.0
reaction_inverse = 1.0 / s

assert 0.2929 < side_fraction < 0.2930
assert 0.2071 < transverse_fraction < 0.2072
assert 0.9101 < s < 0.9102
assert 1.0987 < reaction_inverse < 1.0988

# Aggregate feasibility. Transverse cancellation with individual magnitudes in
# [c,1] requires c B+ <= B- and c B- <= B+. Verify the resulting side-mass floor
# on a dense ratio mesh.
for k in range(100_001):
    ratio = 1e-5 + (1.0 / c - 1e-5) * k / 100_000
    bp = ratio / (1.0 + ratio)
    bm = 1.0 / (1.0 + ratio)
    feasible = c * bp <= bm + 1e-12 and c * bm <= bp + 1e-12
    if feasible:
        assert bp >= side_fraction - 2e-6
        assert bm >= side_fraction - 2e-6
        # Since T >= c*max(B+,B-), every feasible aggregate has T >= c/2 B.
        assert c * max(bp, bm) >= transverse_fraction - 1e-12

# Host transverse margin bounds the absolute axial component of every unit ray.
for t in [c, 0.5, 0.7, 0.9, 0.999]:
    axial = math.sqrt(max(0.0, 1.0 - t * t))
    assert axial <= s + 1e-15

print("PASS: high-t exact-antipodal stress-balance regressions")
print("host transverse component floor =", c)
print("each-side stress fraction floor =", side_fraction)
print("each-side transverse moment fraction floor =", transverse_fraction)
print("axial component ceiling =", s)
print("stress/reaction inverse factor =", reaction_inverse)
