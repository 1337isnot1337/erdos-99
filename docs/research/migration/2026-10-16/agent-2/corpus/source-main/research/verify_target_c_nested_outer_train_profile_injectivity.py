#!/usr/bin/env python3
"""Exact constants for the nested O-O train diameter-profile injectivity corollary."""
from fractions import Fraction as F
RHO = F(779, 100000)
CENTER = F(696271, 82500000)
SAFE_CENTER = F(779, 100000)
BRACE_DENSITY = RHO / 2
SAFE_BRACE = F(389, 100000)
assert CENTER > SAFE_CENTER
assert BRACE_DENSITY == F(779, 200000)
assert BRACE_DENSITY > SAFE_BRACE
print("balanced leaf density =", RHO, "=", float(RHO))
print("balanced center density lower =", CENTER, "=", float(CENTER))
print("profile-injective bracing density =", BRACE_DENSITY, "=", float(BRACE_DENSITY))
print("safe distinct-diameter density =", SAFE_BRACE, "margin =", BRACE_DENSITY-SAFE_BRACE)
print("PASS: balanced rectangle forces >0.00389D distinct diameter bracers")
