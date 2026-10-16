#!/usr/bin/env python3
"""Exact arithmetic certificate for the t<=1.844 smallest-leaf rectangle.

The first draft incorrectly treated an arbitrary pairwise noncrossing leaf family
as a global linear stack.  The audited topology only guarantees that its complement
dual is a tree.  The corrected proof first extracts one long center crossing path in
that tree and uses it as a backbone.  Every other center crossing path intersects the
backbone in an interval, so one can then do consecutive-block averaging safely.

Previously certified asymptotic constants:

    P_V > 0.0848             retained smallest-leaf O--O pair weight / D
    weighted average center degree > 0.73 D
    center phase size < 1.063 D
    each retained pair weight <= 1

Safe conclusions certified here:

    good leaf trains (degree > 0.57 D): > 0.0275 D
    one center-path backbone:          > 0.014746 D leaf tracks
    complete rectangle:               > 0.003 D leaf tracks
                                       x > 0.35 D center trains

All load-bearing arithmetic is exact Fraction arithmetic.
"""

from fractions import Fraction as F

P_MIN = F(53, 625)       # 0.0848
AVG = F(73, 100)         # 0.73
L = F(57, 100)           # 0.57 good-cut degree threshold
C_MAX = F(1063, 1000)    # 1.063 center-train density ceiling

GOOD_SAFE = F(11, 400)   # 0.0275
ALPHA = F(3, 1000)       # 0.003 leaf density in final block
BETA = F(7, 20)          # 0.35 common center density

# Weighted averaging: if G is normalized total weight of leaf cuts with degree
# > L D, then AVG*P < L(P-G)+C_MAX*G.
GOOD_EXACT = (AVG - L) * P_MIN / (C_MAX - L)

# Among m >= GOOD_SAFE D good leaf tracks, total center/leaf incidence exceeds
# L*m*D and there are at most C_MAX*D center trains.  Hence one center train
# crosses at least BACKBONE_SAFE*D good leaf tracks.  Those crossed leaf tracks
# are a path in the complement dual tree.
BACKBONE_SAFE = L * GOOD_SAFE / C_MAX

# Every center crossing path meets the selected backbone in an interval.  For
# r=ALPHA D consecutive backbone edges, block averaging gives one block with
# common center density at least
#     L - ALPHA*C_MAX/BACKBONE_SAFE
# up to o(1).
COMMON_SAFE = L - ALPHA * C_MAX / BACKBONE_SAFE

assert GOOD_EXACT > GOOD_SAFE
assert BACKBONE_SAFE > ALPHA
assert COMMON_SAFE > BETA

print("GOOD_EXACT =", GOOD_EXACT, "=", float(GOOD_EXACT))
print("GOOD_EXACT-GOOD_SAFE =", GOOD_EXACT - GOOD_SAFE,
      "=", float(GOOD_EXACT - GOOD_SAFE))
print("BACKBONE_SAFE =", BACKBONE_SAFE, "=", float(BACKBONE_SAFE))
print("COMMON_SAFE =", COMMON_SAFE, "=", float(COMMON_SAFE))
print("COMMON_SAFE-BETA =", COMMON_SAFE - BETA,
      "=", float(COMMON_SAFE - BETA))
print("ALPHA/BACKBONE_SAFE =", ALPHA / BACKBONE_SAFE,
      "=", float(ALPHA / BACKBONE_SAFE))
print("PASS: >0.003D leaf cuts x >0.35D common center trains")
