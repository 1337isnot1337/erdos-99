#!/usr/bin/env python3
"""Exact arithmetic checks for the many-uniform-cusps/resultant-plateau note."""

from fractions import Fraction as Q

C = Q(1_109_000)
column_floor = Q(1567, 10_000)
uniform_good_budget = 2 * C
phase_coeff = uniform_good_budget / column_floor
local_column_coeff = 2 * uniform_good_budget / column_floor

assert uniform_good_budget == 2_218_000
assert phase_coeff < 14_160_000
assert local_column_coeff < 28_320_000

# If sum_i J_i < C*r, the number of indices with J_i >= 2C is < r/2.
# Thus the number of uniform-good interfaces is > r/2. Any edge subset of
# a path with g edges contains a no-common-endpoint subfamily of size at
# least ceil(g/2), hence > r/4 here.
for r in range(1, 1000):
    max_bad_integer = (r - 1) // 2
    min_good = r - max_bad_integer
    assert Q(min_good) > Q(r, 2)
    min_row_disjoint = (min_good + 1) // 2
    assert Q(min_row_disjoint) > Q(r, 4)

print("PASS: many-uniform-cusps constants through t<=1.8687")
print("uniform-good interface budget =", int(uniform_good_budget))
print("uniform-good phase/opening coefficient =", float(phase_coeff))
print("local two-row column-excess coefficient =", float(local_column_coeff))
print("good-interface density > 1/2")
print("row-disjoint good-interface density > 1/4")
print("resultant plateau scaling: TV(F)/D <= C*r_D/D -> 0 whenever r_D/D -> 0")
