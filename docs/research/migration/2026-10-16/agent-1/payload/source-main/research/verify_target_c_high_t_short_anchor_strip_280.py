#!/usr/bin/env python3
"""Exact arithmetic certificate for the high-t short-anchor strip.

The live t<=1.855 low-energy O-O path has safe density p=0.0184=23/1250.
For its nonhub internal strips:

    sum outer-hull strip arclength <= per(K) <= pi D,
    sum switching KKT variation B_i <= 2.

Hence some nonhub strip has

    ell_i + D B_i <= ((pi+2)/p) + o(1).

The rational enclosure pi < 355/113 puts the coefficient below 280.
A perimeter-only averaging gives ell_i<171+o(1).  A three-currency optional
check also records ell_i + D B_i + N_i <621+o(1), using sum N_i<=2 pi D.
"""
from fractions import Fraction as F

P = F(23, 1250)          # 0.0184
PI_UP = F(355, 113)

ARC = PI_UP / P
JOINT = (PI_UP + 2) / P
TRIPLE = (3 * PI_UP + 2) / P

assert ARC == F(443750, 2599)
assert JOINT == F(726250, 2599)
assert TRIPLE == F(1613750, 2599)

assert ARC < 171
assert JOINT < 280
assert TRIPLE < 621

print("PASS high-t short-anchor strip arithmetic")
print("path density =", P, "=", float(P))
print("perimeter-only coefficient <", ARC, "=", float(ARC))
print("perimeter+beta coefficient <", JOINT, "=", float(JOINT))
print("perimeter+beta+switch-count coefficient <", TRIPLE, "=", float(TRIPLE))
print("safe same-strip anchor/reaction constant = 280")
