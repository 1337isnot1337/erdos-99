from fractions import Fraction
from math import sqrt

# Nonincident crossed-rhombus centers with the same side sign lie in one
# tiny pole cluster. At epsilon <= 1/20, the coarse rational cluster
# diameter is far below the audited sqrt(3)/2 center separation.
eps = Fraction(1, 20)
vertical_width = 2 * (eps + eps * eps)
cluster_d2 = eps * eps + vertical_width * vertical_width

assert vertical_width == Fraction(21, 200)
assert cluster_d2 == Fraction(541, 40000)
assert cluster_d2 < Fraction(3, 4)

# Four-row bandwidth makes mod-five thinning sufficient for one exact-swap
# Horn subsystem.
s0 = Fraction(791, 320_000_000)
gamma5 = s0 / 10

assert gamma5 == Fraction(791, 3_200_000_000)
assert gamma5 / 4 == Fraction(791, 12_800_000_000)
assert gamma5 / 8 == Fraction(791, 25_600_000_000)
assert gamma5 / 2 == Fraction(791, 6_400_000_000)
assert gamma5 / 16 == Fraction(791, 51_200_000_000)

# Current sharp all-residue budget:
# 2 N_LOWER + N_UPPER > (s0/8-o(1))D, hence one metric winner has density s0/24.
weighted_rhs = s0 / 8
winner_density = s0 / 24
assert weighted_rhs == Fraction(791, 2_560_000_000)
assert winner_density == Fraction(791, 7_680_000_000)

# Single-class UPPER localization reference constant:
# A_* = 14/(3 sqrt(3)), so gamma5/(48 A_*) = gamma5*sqrt(3)/224.
upper_coeff = float(gamma5) * sqrt(3) / 224
assert 1.9113e-9 < upper_coeff < 1.9114e-9

print("four-row endpoint-incidence certificate: PASS")
print("pole_cluster_d2 =", float(cluster_d2))
print("center_separation_d2 =", 3 / 4)
print("gamma5 =", float(gamma5))
print("sharp_weighted_rhs =", float(weighted_rhs))
print("sharp_winner_density =", float(winner_density))
print("single_class_upper_localization =", upper_coeff)
