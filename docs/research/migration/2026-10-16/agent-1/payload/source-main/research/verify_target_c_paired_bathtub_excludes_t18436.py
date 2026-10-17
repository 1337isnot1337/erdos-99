#!/usr/bin/env python3
"""Exact rational certificate for the paired-bathtub exclusion at t <= 1.8436."""

from fractions import Fraction as F

# Parent theorem constants.
Z = F(22069, 10000)          # total retained dominant outer mass > 2.2069
G = F(6895, 100000)          # limiting trimmed good O--O pair weight 0.06895
M = 2 * G                    # paired terminal submeasure mass per leaf
DELTA_CEIL = F(51295, 1000000)

# Cross-leaf noncrossing energy: (2-sqrt(3))*G > 0.01847.
# sqrt(3) < 1.7321 because (17321/10000)^2 > 3.
SQRT3_HI = F(17321, 10000)
assert SQRT3_HI * SQRT3_HI > 3
PAIR_ENERGY_LO = (F(2) - SQRT3_HI) * G
PAIR_SAFE = F(1847, 100000)
assert PAIR_ENERGY_LO > PAIR_SAFE

# After removing paired terminal mass M from each leaf measure, the three
# residual one-well masses have total at least Z-2M. Jensen equalizes them.
AVG = (Z - 2 * M) / 3
assert AVG == F(6437, 10000)

# f(s)=s-2 sin(s/2).  For x=s/2>0 the alternating truncation
# x - x^3/6 + x^5/120 is an upper bound for sin(x), hence the expression
# below is an exact rational lower bound for f(AVG).
x = AVG / 2
sin_hi = x - x**3 / 6 + x**5 / 120
f_lo = AVG - 2 * sin_hi
assert f_lo > 0

TOTAL_LO = 3 * f_lo + PAIR_SAFE
GAP = TOTAL_LO - DELTA_CEIL
assert GAP > F(34, 100000)  # > 0.00034

print("Z =", float(Z))
print("G =", float(G))
print("paired terminal mass M =", float(M))
print("paired-energy lower from coarse sqrt3 enclosure =", float(PAIR_ENERGY_LO))
print("safe paired energy =", float(PAIR_SAFE))
print("Jensen average residual phase mass =", float(AVG))
print("rational f(AVG) lower =", float(f_lo))
print("total outer-energy lower =", float(TOTAL_LO))
print("parent delta ceiling =", float(DELTA_CEIL))
print("contradiction gap =", float(GAP))
print("PASS: paired-bathtub constraints exclude every t <= 1.8436 survivor")
