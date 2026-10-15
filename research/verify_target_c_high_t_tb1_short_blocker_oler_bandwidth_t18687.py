#!/usr/bin/env python3
"""Regression checks for the six-row Oler short-blocker bandwidth theorem."""

from fractions import Fraction
import math

# Exact limiting Oler cap at L=1.
limit = 1.0 + (14.0 + 5.0 * math.pi) / (3.0 * math.sqrt(3.0))
assert 6.71 < limit < 6.72 < 7.0

# Rational envelope used in the proof.
# sqrt(3) > 265/153 because 3*153^2 - 265^2 = 2.
assert 3 * 153 * 153 - 265 * 265 == 2

# With pi < 22/7:
# 14/(3 sqrt(3)) < 714/265,
# 1 + 5 pi/(3 sqrt(3)) < 1493/371.
coef = Fraction(714, 265)
const = Fraction(1493, 371)

# If L <= 1 + K/D and D > 10K, then L < 11/10.
cap = coef * Fraction(11, 10) + const
assert cap == Fraction(64814, 9275)
assert Fraction(7, 1) - cap == Fraction(111, 9275)
assert cap < 7

print("six-row Oler bandwidth certificate: PASS")
print("limiting Oler cap =", limit)
print("explicit D>10K cap <", float(cap))
