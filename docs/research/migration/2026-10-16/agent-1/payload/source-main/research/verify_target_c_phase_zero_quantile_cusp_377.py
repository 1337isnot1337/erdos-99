#!/usr/bin/env python3
"""Exact arithmetic certificate for the phase-zero/center-quantile 377-row cusp.

Uses hostile-audited t<=1.844 inputs:
  weighted smallest-leaf center degree average A=.7404,
  retained smallest-leaf O-O pair weight P=.0848,
  total center train density N<=1.063.

Choose good degree threshold lambda=.532 and split actual center trains into equal
lower/upper phase blocks.  Phase-zero localization splits the good retained pair mass
into at most two laminar chains.  The larger chain has density p=g/2.  The global
diameter interval endpoint budget then leaves positive density of boundaries with at
most 377 switching rows.  Global angular defect and KKT switching variation retain
inverse-D phase and beta costs on one such boundary.
"""
from fractions import Fraction as F

A = F(1851, 2500)          # .7404
P = F(53, 625)             # .0848
N = F(1063, 1000)          # 1.063
LAM = F(133, 250)           # .532
R = F(1, 2)

# Weighted good-pair mass from the audited thresholding lemma.
G = (A - LAM) * P / (N - LAM)
PATH = G / 2
DLOW = LAM - R * N
DTOP = LAM - (1 - R) * N

assert G == F(55226, 1659375)
assert PATH == F(27613, 1659375)
assert DLOW == F(1, 2000)
assert DTOP == DLOW
assert DLOW > 0

# Count-bad means N_i >= 378, so its boundary density is <= 2*pi/378.
PI_UP = F(355, 113)
COUNT_BAD_UP = 2 * PI_UP / 378
RHO = PATH - COUNT_BAD_UP
assert COUNT_BAD_UP == F(355, 21357)
assert RHO == F(72524, 3937696875)
assert RHO > 0

# Standard outward upper enclosure already used by current adjacent-cut certificates.
CPHASE_UP = F(3258689123681, 612912000000)

# sum_i D Q_i <= (2*Cphase/d_low)D + o(D)
# sum_i D B_i <= 2D
TOTAL_COST_COEFF = 2 + 2 * CPHASE_UP / DLOW
Q0 = F(1_160_000_000, 1)
assert TOTAL_COST_COEFF / RHO < Q0

# Non-load-bearing architecture diagnostic: lambda -> N/2+ gives the largest path
# density in this two-marker + 50/50-quantile architecture.
PMAX = (A - N / 2) * P / N
assert PMAX > 2 * PI_UP / 378

print("PASS phase-zero quantile cusp arithmetic")
print("good retained pair density >", G, "=", float(G))
print("one laminar good-chain density >", PATH, "=", float(PATH))
print("lower/top center-neighbor density >", DLOW, "=", float(DLOW))
print("N_i>=378 boundary density <", COUNT_BAD_UP, "=", float(COUNT_BAD_UP))
print("N_i<=377 boundary density >", RHO, "=", float(RHO))
print("phase+beta total cost coefficient <", float(TOTAL_COST_COEFF))
print("same-boundary inverse-D constant <", float(TOTAL_COST_COEFF / RHO))
print("safe Q0 =", int(Q0))
print("architecture max path density =", float(PMAX))
print("PASS: <=377 is rigorously reachable in this architecture")
