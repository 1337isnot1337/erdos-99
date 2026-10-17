from fractions import Fraction
import math

# Regression certificate for
# target_c_high_t_tb1_superdiameter_inactive_thrackle_t18687_2026-09-17.md
#
# The convex-hull / four-turn superdiameter-thrackle lemma is proved in the
# companion note.  This script checks the exact threshold arithmetic, the
# chosen TB1 slack parameter, the density losses, and the matching constant.

S0 = Fraction(791, 320_000_000)
TAU_STAR = Fraction(1, 128_000_000)
K_SWAP = 31_400_000

assert S0 / 16 == Fraction(791, 5_120_000_000)
assert abs(float(S0 / 16) - 1.544921875e-7) < 1e-20

# 31.4e6 * tau_* = 0.2453125 < 1/4.
thin_constant = Fraction(K_SWAP, 1) * TAU_STAR
assert thin_constant == Fraction(157, 640)
assert float(thin_constant) == 0.2453125
assert thin_constant < Fraction(1, 4)

# Sharp metric threshold.  For D>1,
# sqrt(D^2-1) < D - 1/(2D) < D - 1/(4D).
# The first inequality follows by squaring the positive quantities:
# (D-1/(2D))^2 = D^2-1+1/(4D^2).
for D in [2, 3, 10, 100, 1000, 10**6]:
    threshold = math.sqrt(D * D - 1)
    assert threshold < D - 1 / (2 * D)
    assert D - 1 / (2 * D) < D - 1 / (4 * D)

# Sharpness: a 1 x sqrt(D^2-1) rectangle has diameter D.
for D in [2, 10, 100, 1000]:
    long_side = math.sqrt(D * D - 1)
    assert abs(math.hypot(1, long_side) - D) < 1e-12 * D

# Existing near-diameter degree bound is
# Delta <= (8*3^(1/8)+o(1)) D^(3/4).
# Greedy matching from an (s0/16-o(1))D edge family loses asymptotically
# another factor 2*8*3^(1/8).
matching_coefficient = float(S0) / (256 * (3 ** (1 / 8)))
assert abs(matching_coefficient - 8.416787895648718e-9) < 1e-20

# Four-turn contradiction arithmetic used in the proof:
# if X^2 > D^2-1 and Y^2 >= 1 while |X+Y| <= D, then X.Y < 0.
# Check exact rational samples strictly on the long side of the threshold.
for D in [10, 100, 1000]:
    D2 = Fraction(D * D, 1)
    x2 = D2 - 1 + Fraction(1, 1000)
    for y2 in [Fraction(1, 1), Fraction(3, 2), Fraction(5, 1)]:
        upper_dot = (D2 - x2 - y2) / 2
        assert upper_dot < 0

print("PASS: TB1 superdiameter inactive-thrackle certificate")
print("tau_* =", float(TAU_STAR))
print("31.4e6*tau_* =", float(thin_constant))
print("s0/16 =", float(S0 / 16))
print("matching coefficient =", matching_coefficient)
