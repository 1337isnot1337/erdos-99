#!/usr/bin/env python3
"""Regression checks for the sharp all-residue Horn blocker budget."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

s0 = Fraction(791, 320_000_000)
delta = s0 / 24
weighted_rhs = s0 / 8

assert delta == Fraction(791, 7_680_000_000)
assert weighted_rhs == Fraction(791, 2_560_000_000)
assert delta == weighted_rhs / 3

# UPPER localization: c = delta/(6 A_*), A_*=14/(3 sqrt(3))
# = delta * sqrt(3)/28.
c_sqrt3 = delta / 28
assert c_sqrt3 == Fraction(113, 30_720_000_000)

single6_sqrt3 = Fraction(113, 122_880_000_000)
first_all_sqrt3 = Fraction(791, 430_080_000_000)
dedup_sqrt3 = Fraction(113, 40_960_000_000)
assert c_sqrt3 / single6_sqrt3 == 4
assert c_sqrt3 / first_all_sqrt3 == 2
assert c_sqrt3 / dedup_sqrt3 == Fraction(4, 3)

getcontext().prec = 50
c_dec = (
    Decimal(c_sqrt3.numerator)
    / Decimal(c_sqrt3.denominator)
    * Decimal(3).sqrt()
)
assert abs(c_dec - Decimal("6.37115043148708e-9")) < Decimal("1e-22")

# Five class mass regression. Class L gives P_L/8 after possible lower
# cross-residue duplication; class U gives P_U/4 because repeated exact
# UPPER blockers are only O(1). Hence 8 N_L + 4 N_U >= P.
for masses in product(range(5), repeat=5):
    total = sum(masses)
    if total == 0:
        continue
    for labels in product((0, 1), repeat=5):  # 0=L, 1=U
        p_l = sum(m for m, lab in zip(masses, labels) if lab == 0)
        p_u = total - p_l
        n_l = Fraction(p_l, 8)
        n_u = Fraction(p_u, 4)
        assert 8 * n_l + 4 * n_u == total
        assert max(n_l, n_u) >= Fraction(total, 12)

# Equality point is P_L : P_U = 2 : 1.
assert Fraction(2, 3) / 8 == Fraction(1, 3) / 4 == Fraction(1, 12)

# P > (s0/2)D gives winner > (s0/24)D.
assert (s0 / 2) / 12 == delta

# LOWER downstream constants after the 4/3 density gain.
good = delta / 2
assert good == s0 / 48
Tstar = Fraction(6121, 2000)
train = good * Fraction(1609, 2500) / Tstar
assert train == Fraction(1_272_719, 117_523_200_000_000)
disjoint = train / 8
assert disjoint == Fraction(1_272_719, 940_185_600_000_000)

print("sharp all-residue Horn budget certificate: PASS")
print("delta_sharp =", float(delta))
print("weighted rhs s0/8 =", float(weighted_rhs))
print("c_sharp =", c_dec)
print("LOWER good density =", float(good))
print("LOWER fixed-train density =", float(train))
print("LOWER disjoint fixed-train density =", float(disjoint))
