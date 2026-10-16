#!/usr/bin/env python3
"""Exact constant checks after one-row LOWER classification and full blocker dedup."""
from fractions import Fraction as Q
import math

s0 = Q(791, 320_000_000)

# The current sharp all-residue theorem supplies p_r/4 blockers of the selected
# metric type in each valid residue system. One-row LOWER nonrepetition removes
# the final cross-system multiplicity-two loss; UPPER repetition is already O(1).
sourcewide_sum_floor = s0 / 8
metric_floor = s0 / 16
assert sourcewide_sum_floor == Q(791, 2_560_000_000)
assert metric_floor == Q(791, 5_120_000_000)

# Flexible-scale UPPER localization: delta/(6 A_*), A_*=14/(3 sqrt(3)).
upper_coeff = metric_floor / 28
assert upper_coeff == Q(113, 20_480_000_000)

# GLOBAL LOWER: support depth one and injective owners imply row overlap <= 2.
# Keep the low-cost half, then average the >0.6436D pure columns over all trains.
good_lower = metric_floor / 2
assert good_lower == s0 / 32
assert good_lower == Q(791, 10_240_000_000)
pure = Q(1609, 2500)
Tstar = Q(6121, 2000)
threaded = good_lower * pure / Tstar
assert threaded == Q(1_272_719, 78_348_800_000_000)

# Interval overlap <=2, so one of two colors is pairwise disjoint.
disjoint = threaded / 2
assert disjoint == Q(1_272_719, 156_697_600_000_000)

print("one-row Horn propagation certificate: PASS")
print("N_L+N_U floor = s0/8 =", sourcewide_sum_floor, "=", float(sourcewide_sum_floor))
print("equal-density metric floor = s0/16 =", metric_floor, "=", float(metric_floor))
print("UPPER localization coefficient =", upper_coeff, "* sqrt(3) =", float(upper_coeff) * math.sqrt(3.0))
print("good LOWER density = s0/32 =", good_lower, "=", float(good_lower))
print("fixed-train threading coefficient =", threaded, "=", float(threaded))
print("pairwise-disjoint fixed-train coefficient =", disjoint, "=", float(disjoint))
