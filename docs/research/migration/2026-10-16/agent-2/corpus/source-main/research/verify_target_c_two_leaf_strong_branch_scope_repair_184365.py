#!/usr/bin/env python3
"""Exact scope repair for the strong center/leaf pair branch at t<=1.84365.

The original 1.84364/1.84365 certificates checked the strong-branch ratio after
replacing the larger leaf U by its contradiction threshold U0.  That check is not
logically sufficient because, for C<K, (C+U-K)_+/U increases with U.  The phasewise
retained-mass theorem supplies the missing independent control V>A/2, hence
C+U=W-V <= Wbar-A/2.  This certificate checks the resulting non-circular ratio.
"""

from fractions import Fraction as Q
from math import isqrt

SCALE = 10**100
n3 = isqrt(3*SCALE*SCALE)
sqrt3_lo = Q(n3, SCALE)
sqrt3_hi = Q(n3+1, SCALE)
K_lo = Q(2)/sqrt3_hi

nr = isqrt(Q(20,29).numerator*SCALE*SCALE//Q(20,29).denominator)
rcrit_lo = Q(nr, SCALE)

# Current hostile-audited 1.84365 box.
WBAR = Q(1912711, 1_000_000)
A = Q(351, 500)       # every retained phase occurrence mass > .702
VMIN = A/2            # because z_V <= 2V
U0 = Q(663, 1250)     # contradiction hypothesis U >= .5304

# For the larger leaf U:
#   C+U = W-V <= WBAR-VMIN,
#   U >= U0,
#   K >= K_lo.
# Therefore (C+U-K)_+/U is at most this quantity.
ratio_hi = (WBAR-VMIN-K_lo)/U0
assert ratio_hi > 0
assert ratio_hi < Q(768,1000)
assert ratio_hi < rcrit_lo

# In the main physical-pair interval C<1.0443<K.  For fixed C<K,
# r(L)=(C+L-K)_+/L is nondecreasing in L, so V<=U makes the V ratio no larger.
CHI = Q(10443, 10000)
assert CHI < K_lo

# The same repair also covers the hostile-audited 1.84364 theorem.
W64 = Q(956329, 500000)  # 1.912658
A64 = Q(1409, 2000)      # .7045
V64 = A64/2
U64 = Q(66,125)          # .528
ratio64_hi = (W64-V64-K_lo)/U64
assert ratio64_hi < Q(769,1000)
assert ratio64_hi < rcrit_lo

print('PASS: non-circular strong-pair scope repair')
print('1.84365 ratio upper =', float(ratio_hi))
print('1.84364 ratio upper =', float(ratio64_hi))
print('strong threshold lower =', float(rcrit_lo))
