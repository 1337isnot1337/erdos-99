#!/usr/bin/env python3
"""Exact certificate for the optimized common-center adjacent-cut backbone.

The existing triple-small construction leaves two free rational parameters:

* lambda: the center-degree threshold defining good smallest-leaf O-O trains;
* r: the top center-phase fraction used to choose one center train gamma.

Retuning those parameters makes the gamma-crossed good-leaf path almost twice as
long as in the original certificate.  The global switching-count budget then forces
an internal boundary with at most 920 actual diameter rows whose interval incidence
changes there.  On the positive-density set of such count-good boundaries, a second
averaging step keeps both switching beta mass and adjacent phase gap O(1/D).

All arithmetic below is exact Fraction arithmetic.  The only transcendental inputs
are the same outward rational upper bounds already used in the parent certificate.
"""

from fractions import Fraction as Q

# Audited parent inputs.
D_AVG = Q(7404, 10000)      # weighted center degree > .7404 D
P_PAIR = Q(848, 10000)      # retained smallest-leaf O-O pair weight > .0848 D
N_CENTER = Q(1063, 1000)    # total center train count < 1.063 D

# New path parameters.
LAMBDA = Q(64033, 100000)   # .64033
R_TOP = Q(60237, 100000)    # .60237

# Outward transcendental bounds used in the existing triple-small certificate.
PI_UP = Q(355, 113)
C_PHASE_UP = Q(3258689123681, 612912000000)

# Weighted thresholding: good-leaf retained weight, hence distinct good-leaf count.
G = (D_AVG - LAMBDA) * P_PAIR / (N_CENTER - LAMBDA)

# Every good leaf has this many neighbors in the top r block and in the
# complementary lower-phase block, respectively.
D_TOP = LAMBDA - (1 - R_TOP) * N_CENTER
D_LOW = LAMBDA - R_TOP * N_CENTER

assert G > 0
assert D_TOP > 0
assert D_LOW > 0

# Averaging good-leaf/top-block incidence gives one center train gamma crossing
# more than P_PATH*D distinct good leaves.
P_PATH = D_TOP * G / (R_TOP * N_CENTER)

# A boundary with N_i >= 921 is count-bad.  Since sum_i N_i <= 2*pi*D,
# count-bad boundaries have density at most this number.
COUNT_BAD_DENSITY = 2 * PI_UP / Q(921)
COUNT_GOOD_DENSITY = P_PATH - COUNT_BAD_DENSITY

# The phase argument gives sum_i D Q_i <= PHASE_COEFF*D+o(D), while the KKT
# interval budget gives sum_i D B_i <= 2D.  Average their sum only over the
# positive-density count-good boundaries.
PHASE_COEFF = 2 * C_PHASE_UP / D_LOW
COMBINED_COEFF = Q(2) + PHASE_COEFF
SAFE_COMBINED = Q(460_000_000_000)

assert COUNT_GOOD_DENSITY > Q(2, 1_000_000)
assert SAFE_COMBINED * COUNT_GOOD_DENSITY > COMBINED_COEFF

print("PASS optimized adjacent-cut backbone / 920-row cusp certificate")
print("good-leaf density G =", G, "=", float(G))
print("top-neighbor density =", D_TOP, "=", float(D_TOP))
print("lower-phase neighbor density =", D_LOW, "=", float(D_LOW))
print("gamma-path density P_PATH =", P_PATH, "=", float(P_PATH))
print("2*pi_up/921 =", COUNT_BAD_DENSITY, "=", float(COUNT_BAD_DENSITY))
print("count-good boundary density =", COUNT_GOOD_DENSITY,
      "=", float(COUNT_GOOD_DENSITY))
print("phase budget coefficient =", PHASE_COEFF, "=", float(PHASE_COEFF))
print("combined DB + DQ safe bound =", SAFE_COMBINED)
print("combined averaging margin =",
      SAFE_COMBINED * COUNT_GOOD_DENSITY - COMBINED_COEFF,
      "=", float(SAFE_COMBINED * COUNT_GOOD_DENSITY - COMBINED_COEFF))
print("CONCLUSION: for sufficiently large D, one adjacent boundary has")
print("  N_i <= 920")
print("  D*B_i + D*Q_i < 4.6e11 + o(1)")
print("hence B_i,Q_i = O(1/D) on the same <=920-row switching set.")
