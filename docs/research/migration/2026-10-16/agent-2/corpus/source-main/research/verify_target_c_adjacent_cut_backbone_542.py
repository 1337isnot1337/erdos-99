#!/usr/bin/env python3
"""Exact certificate for a <=542-edge adjacent switching set.

Inputs already proved on main:
  * weighted smallest-leaf center degree > .7404 D;
  * retained smallest-leaf O-O pair weight > .0848 D;
  * total center trains < 1.063 D;
  * total adjacent switch-count budget < 3.702519852 D + o(D), from SW1039;
  * sum B_i <= 2 and the global phase-defect budget.

We retune the common-center path parameters before averaging switches.  The longer
path plus the improved global diameter-edge budget leaves a positive-density set of
boundaries with integer N_i <= 542.  A second average over that set preserves
B_i,Q_i=O(1/D) on the same boundary.
"""
from fractions import Fraction as Q

D_AVG = Q(7404, 10000)
P_PAIR = Q(848, 10000)
N_CENTER = Q(1063, 1000)

LAMBDA = Q(64033, 100000)
R_TOP = Q(60237, 100000)

C_PHASE_UP = Q(3258689123681, 612912000000)
SWITCH_TOTAL_UP = Q(3702519852, 10**9)

G = (D_AVG - LAMBDA) * P_PAIR / (N_CENTER - LAMBDA)
D_TOP = LAMBDA - (1 - R_TOP) * N_CENTER
D_LOW = LAMBDA - R_TOP * N_CENTER
P_PATH = D_TOP * G / (R_TOP * N_CENTER)

assert G > 0 and D_TOP > 0 and D_LOW > 0

# Count-bad means N_i >= 543.  Since sum N_i < SWITCH_TOTAL_UP D + o(D),
# the count-bad boundary density is at most SWITCH_TOTAL_UP/543.
BAD_COUNT_DENSITY = SWITCH_TOTAL_UP / Q(543)
COUNT_GOOD_DENSITY = P_PATH - BAD_COUNT_DENSITY
assert COUNT_GOOD_DENSITY > Q(5, 1_000_000)

# On all path boundaries:
#   sum D B_i <= 2D,
#   sum D Q_i <= (2 C_phase / D_LOW) D + o(D).
# Average only over the positive-density count-good boundaries.
PHASE_COEFF = 2 * C_PHASE_UP / D_LOW
COMBINED_COEFF = Q(2) + PHASE_COEFF
SAFE_COMBINED = Q(180_000_000_000)
assert SAFE_COMBINED * COUNT_GOOD_DENSITY > COMBINED_COEFF

print('PASS optimized common-center backbone: <=542 switching rows')
print('good-leaf density =', G, '=', float(G))
print('top-neighbor density =', D_TOP, '=', float(D_TOP))
print('lower-phase neighbor density =', D_LOW, '=', float(D_LOW))
print('path density =', P_PATH, '=', float(P_PATH))
print('switch total density upper =', SWITCH_TOTAL_UP, '=', float(SWITCH_TOTAL_UP))
print('count-bad density N>=543 =', BAD_COUNT_DENSITY, '=', float(BAD_COUNT_DENSITY))
print('count-good density =', COUNT_GOOD_DENSITY, '=', float(COUNT_GOOD_DENSITY))
print('phase budget coefficient =', PHASE_COEFF, '=', float(PHASE_COEFF))
print('combined safe constant =', SAFE_COMBINED)
print('combined averaging margin =',
      SAFE_COMBINED * COUNT_GOOD_DENSITY - COMBINED_COEFF,
      '=', float(SAFE_COMBINED * COUNT_GOOD_DENSITY - COMBINED_COEFF))
print('CONCLUSION: same adjacent boundary has N_i<=542 and')
print('D*(B_i+Q_i) < 1.8e11 + o(1).')
