#!/usr/bin/env python3
"""Regression checks for simultaneous deep-window / force-bundle disjoint extraction."""

from fractions import Fraction
from math import pow

c = Fraction(113, 5_000_000)
kappa = 4.0 * pow(3.0, 1.0 / 8.0)
base_density = c / 32
leading = float(base_density) / (4.0 * kappa)
expected = float(c) / (512.0 * pow(3.0, 1.0 / 8.0))

assert abs(leading - expected) < 1e-20
assert leading > 0.0

# Conflict-degree formula: 4 Delta(H) endpoint conflicts + 4r index-window conflicts.
for D, r in [(10**8, 3), (10**12, 100), (10**16, 10000)]:
    Delta = kappa * D ** 0.75
    degree_cap = 4.0 * Delta + 4.0 * r
    centers = float(base_density) * D
    greedy_lb = centers / (degree_cap + 1.0)
    assert greedy_lb > 0.0

# A proximity graph on integer centers with conflict distance <=2r has degree <=4r.
def proximity_degree(centers, r):
    centers = sorted(centers)
    best = 0
    for x in centers:
        deg = sum(1 for y in centers if y != x and abs(x-y) <= 2*r)
        best = max(best, deg)
    return best

for r in (0, 1, 3, 9):
    centers = list(range(100))
    assert proximity_degree(centers, r) <= 4*r

# Growing-depth examples with r=o(D^(3/4)) leave the degree term asymptotically dominant.
ratios = []
for k in (10, 100, 1000, 10000):
    D = float(k**8)
    r = float(k**3)
    ratios.append(r / D**0.75)
assert all(ratios[i+1] < ratios[i] for i in range(len(ratios)-1))
assert ratios[-1] < 1e-8

print("PASS: disjoint deep exact-force braid regressions")
print(f"base_center_density={float(base_density):.12g}")
print(f"diameter_degree_constant_kappa={kappa:.12g}")
print(f"D_quarter_extraction_constant={leading:.12g}")
