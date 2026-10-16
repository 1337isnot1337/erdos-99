#!/usr/bin/env python3
"""Exact constant checks for the direct one-sign exact-swap witness injection theorem."""
from fractions import Fraction as Q
import math

s0 = Q(791, 320_000_000)

# One-sign strong-TB1 branch size and direct metric pigeonhole.
total_witness = s0 / 2
metric_floor = s0 / 4
assert total_witness == Q(791, 640_000_000)
assert metric_floor == Q(791, 1_280_000_000)

# Latest Oler path-capacity UPPER localization: delta/(6 A_*),
# A_*=14/(3 sqrt(3)), hence rational coefficient delta/28 before sqrt(3).
upper_coeff = metric_floor / 28
assert upper_coeff == Q(113, 5_120_000_000)

# LOWER winner: support depth one and injective owners imply support-row overlap <=2.
# Retain the low-defect half and average the >0.6436D pure columns over all trains.
good_lower = metric_floor / 2
assert good_lower == s0 / 8
assert good_lower == Q(791, 2_560_000_000)
pure = Q(1609, 2500)  # 0.6436
Tstar = Q(6121, 2000)
threaded = good_lower * pure / Tstar
assert threaded == Q(1_272_719, 19_587_200_000_000)

# At most two chosen LOWER blockers use one support row.
distinct_rows = threaded / 2
assert distinct_rows == Q(1_272_719, 39_174_400_000_000)

print("direct exact-swap witness injection certificate: PASS")
print("total distinct witness floor = s0/2 =", total_witness, "=", float(total_witness))
print("one-metric floor = s0/4 =", metric_floor, "=", float(metric_floor))
print("UPPER localization coefficient =", upper_coeff, "* sqrt(3) =", float(upper_coeff) * math.sqrt(3.0))
print("good LOWER density = s0/8 =", good_lower, "=", float(good_lower))
print("fixed-train threading coefficient =", threaded, "=", float(threaded))
print("pairwise-distinct-row fixed-train coefficient =", distinct_rows, "=", float(distinct_rows))
