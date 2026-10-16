#!/usr/bin/env python3
"""Exact arithmetic certificate for the t<=1.8436 two-leaf common-center energy bridge."""

from fractions import Fraction as Q

W = Q(239057, 125000)       # 1.912456
E = Q(90689967, 100000000)  # 0.90689967
U = Q(513, 1000)            # certified upper bound for both leaf masses
P = Q(103, 1000)            # retained O-O pair weight lower bound in each leaf
BAD = Q(681, 20000)         # 0.03405 total low-center-degree O-O weight

# Generic center capacity forces C>U, so all denominators used in the proof are positive.
assert U * (W - U) < E

# If x,y are the two center/leaf missing crossing masses, the hostile-audited
# correlation gives x+y <= h/(1-U/C), where h=C(W-C)-E.  The total retained O-O
# weight on trains of center degree at most C D/2 is at most 2(x+y)/C, hence at most
# 2h/(C-U).  Prove this is < BAD for every real C by a negative discriminant.
#
#   BAD(C-U) - 2[C(W-C)-E] > 0.
#
# The left side is a quadratic with leading coefficient 2.
disc = (BAD - 2 * W) ** 2 - 8 * (2 * E - BAD * U)
assert disc < 0

GOOD = P - BAD
assert GOOD > Q(689, 10000)  # >0.0689 in each leaf phase

# Rational enclosure sqrt(3)<1.7321, hence 2-sqrt(3)>0.2679.
SQRT3_UP = Q(17321, 10000)
assert SQRT3_UP * SQRT3_UP > 3
L_LO = 2 - SQRT3_UP

# Every high-center-degree U/O-O train and V/O-O train shares a center neighbor.
# Triangle-freeness makes the two leaf trains noncrossing; the endpoint-alternation
# theorem then charges e_tau+e_sigma >= 2-sqrt(3)-o(1).  Summing the complete weighted
# product gives E_U+E_V >= (2-sqrt(3))*min(G_U,G_V)-o(1).
energy_lo = L_LO * GOOD
assert energy_lo > Q(1847, 100000)  # >0.01847

print("PASS two-leaf common-center energy bridge")
print("bad-weight discriminant =", float(disc))
print("good O-O weight per leaf >", float(GOOD))
print("2-sqrt(3) lower =", float(L_LO))
print("leaf pair-energy lower =", float(energy_lo))
