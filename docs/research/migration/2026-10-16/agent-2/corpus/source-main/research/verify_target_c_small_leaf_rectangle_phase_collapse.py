#!/usr/bin/env python3
"""Exact coarse constants for the small-leaf rectangle phase-collapse corollary.

Uses safe rational upper bounds
    pi < 355/113,
    sqrt(3) < 17321/10000,
together with the already-certified rectangle shore densities
    a > 0.003 D,
    b > 0.35 D.

For a complete phase-pure product A x B, the canonical angular-defect budget is
    S_AB < C_phase D,
    C_phase = pi^2 sqrt(3)(2+sqrt(3))/12.
Thus the mean product defect is < C_phase/(0.003*0.35*D), and the standard
half-shore Markov trim makes every retained crossing defect at most five times
that mean.  This script certifies the convenient round bound 25320/D.
"""

from fractions import Fraction as F

PI_UP = F(355, 113)
SQRT3_UP = F(17321, 10000)
assert SQRT3_UP * SQRT3_UP > 3

C_UP = PI_UP * PI_UP * SQRT3_UP * (2 + SQRT3_UP) / 12
A_MIN = F(3, 1000)
B_MIN = F(35, 100)
DEFECT_COEFF_UP = 5 * C_UP / (A_MIN * B_MIN)

assert C_UP < F(5317, 1000)
assert DEFECT_COEFF_UP < 25320

print("C_phase upper =", C_UP, "=", float(C_UP))
print("5*C_phase/(0.003*0.35) upper =", DEFECT_COEFF_UP,
      "=", float(DEFECT_COEFF_UP))
print("PASS: half-sized subgrid has every angular defect < 25320/D")
print("shore densities after half trim: >0.0015D and >0.175D")
