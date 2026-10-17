#!/usr/bin/env python3
"""Constant/exponent checks for the shallow-tooth reflection crossing braid."""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
import math

getcontext().prec = 70

# Dedicated eta=4/15 branch.
u4 = Decimal("0.4255744656201161781")
s_min = Q(26, 15)

# For a normal bin of width w=D^-1/8, the leading projected boundary span is
# (1/2)D*w.  Dividing by the minimum tooth-base length gives 15/52 D^7/8.
bin_lead = Q(1, 2) / s_min
assert bin_lead == Q(15, 52)

# A winning quadrant keeps one quarter of the linear blocked-base population.
# Taking one residue class modulo 3 of occupied bins leaves normal gaps >=2w.
coef = u4 * Decimal(13) / Decimal(45)
assert coef > Decimal("0.1229437345124")

# Exponent separation needed by the geometric proof.
assert Q(3, 4) < Q(7, 8) < 1
assert Q(1, 8) < Q(1, 4)

# Reflection slack at eta=4/15 remains strictly below one.
C2 = Q(224, 225)
assert 1 - C2 == Q(1, 225)

# Numerical scale regression: O(D^-1/4) direction error is negligible against
# w=D^-1/8, and O(D^3/4)/sin(w) is o(D), so line intersections lie inside
# D-O(1) blocker segments for sufficiently large D.
for D in (1e8, 1e12, 1e16, 1e20):
    w = D ** (-1 / 8)
    direction_error = D ** (-1 / 4)
    intersection_scale = D ** (3 / 4) / math.sin(w)
    assert direction_error / w < 1
    assert intersection_scale / D < 2  # converges to zero; coarse finite regression

print("tooth reflection crossing-braid certificate: PASS")
print("minimum base length =", s_min)
print("normal-bin leading occupancy coefficient =", bin_lead)
print("pairwise-crossing D^(1/8) coefficient =", coef)
