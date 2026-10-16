#!/usr/bin/env python3
"""Exact arithmetic certificate for the phase-zero laminar O--O backbone.

Inputs are existing hostile-audited t<=1.844 constants:
  A = .7404   weighted average center degree / D
  P = .0848   retained smallest-leaf O--O pair weight / D
  N = 1.063   total center-train count / D

Singleton stopped trains have zero strict-rhombus train-crossing degree. Hence the
non-singleton retained pair weight is at least A*P/N. Section-157 phase-zero
localization splits all but o(D) of that weight into two nested normal-arc classes,
so one laminar non-singleton chain has at least half of it.
"""
from fractions import Fraction as F

A = F(1851, 2500)       # .7404
P = F(53, 625)          # .0848
N = F(1063, 1000)       # 1.063

NS = A * P / N
CHAIN = NS / 2
SAFE_CHAIN = F(59, 2000)       # .0295
SAFE_SWITCH = F(59, 4000)      # .01475

assert NS == F(196206, 3321875)
assert CHAIN == F(98103, 3321875)
assert CHAIN > SAFE_CHAIN
assert SAFE_CHAIN / 2 == SAFE_SWITCH

# KKT interval-row total-variation consequences on a chain of density SAFE_CHAIN.
# sum B_i <= 2, sum N_i <= 2*pi*D; for an exact rational safe simultaneous
# support/multiplier corollary we use pi < 355/113.
PI_UP = F(355, 113)
B_AVG = F(2, 1) / SAFE_CHAIN
N_AVG_UP = 2 * PI_UP / SAFE_CHAIN
COMBINED_AVG_UP = (2 * PI_UP + 2) / SAFE_CHAIN

assert B_AVG < 68
assert N_AVG_UP < 214
assert COMBINED_AVG_UP < 281

print("PASS phase-zero laminar backbone arithmetic")
print("non-singleton pair density >", NS, "=", float(NS))
print("one zero-class chain density >", CHAIN, "=", float(CHAIN))
print("safe chain density =", SAFE_CHAIN, "=", float(SAFE_CHAIN))
print("safe switching-boundary density =", SAFE_SWITCH, "=", float(SAFE_SWITCH))
print("average DB_i ceiling <", float(B_AVG))
print("average N_i ceiling <", float(N_AVG_UP))
print("average N_i + D B_i ceiling <", float(COMBINED_AVG_UP))
