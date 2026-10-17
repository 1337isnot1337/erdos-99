#!/usr/bin/env python3
"""Constants and elementary angle check for the corrected robust blocker fork."""

from fractions import Fraction as Q
from math import cos, pi, sin

c0 = Q(113, 20_000_000)  # corrected parent: |E|+|U| > c0 D-o(D)
gamma = c0 / 32
near_capacity = 4 * gamma
combined_density = c0 - near_capacity
fork_density = combined_density / 2

assert gamma == Q(113, 640_000_000)
assert near_capacity == c0 / 8 == Q(113, 160_000_000)
assert combined_density == 7 * c0 / 8 == Q(791, 160_000_000)
assert fork_density == 7 * c0 / 16 == Q(791, 320_000_000)
assert float(c0) == 0.00000565
assert float(gamma) == 0.0000001765625
assert float(near_capacity) == 0.00000070625
assert float(combined_density) == 0.00000494375
assert float(fork_density) == 0.000002471875
assert gamma > 0
assert gamma < Q(1, 1_000_000)

# A projective ball of radius 2*gamma has arc length 4*gamma. With pairwise
# direction separation >=1/D, its finite packing capacity is <=1+4*gamma*D.
for D in (1, 10, 10**3, 10**6, 10**9):
    cap = Q(1) + near_capacity * D
    assert cap == Q(1) + c0 * D / 8

# Elementary robust-angle inequality used in SB.21--SB.22. For any
# non-antipodal cone angle theta and a TB1 direction t at least gamma from
# both rays, every opening tangent angle s lies within pi/2-gamma of t.
g = float(gamma)
for theta in (0.1, 0.7, 1.4, 2.0, 2.8, pi - 1e-5):
    if theta <= 2 * g:
        continue
    for ti in range(101):
        t = g + (theta - 2 * g) * ti / 100.0
        lo = theta - pi / 2.0
        hi = pi / 2.0
        for si in range(101):
            s = lo + (hi - lo) * si / 100.0
            assert abs(t - s) <= pi / 2.0 - g + 2e-15
            assert cos(t - s) + 2e-15 >= sin(g)

print("PASS: corrected exact-antipodal / strong-TB1 density fork")
print("parent E+U density =", float(c0))
print("gamma =", float(gamma))
print("boundary-near TB1 capacity coefficient =", float(near_capacity))
print("E+strong-TB1 density =", float(combined_density))
print("one-side fork density =", float(fork_density))
print("sin(gamma) =", sin(g))
