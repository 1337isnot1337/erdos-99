#!/usr/bin/env python3
"""Regression checks for all-residue six-spaced Horn aggregation."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

s0 = Fraction(791, 320_000_000)
gamma6 = s0 / 12
beta = s0 / 48

assert gamma6 == Fraction(791, 3_840_000_000)
assert beta == Fraction(791, 15_360_000_000)
assert gamma6 / 4 == beta
assert beta / (gamma6 / 8) == 2

# Exact rational coefficient multiplying sqrt(3) in c_all.
# A_* = 14/(3 sqrt(3)), so beta/(6 A_*) = beta*sqrt(3)/28.
c_all_sqrt3_coeff = beta / 28
assert c_all_sqrt3_coeff == Fraction(791, 430_080_000_000)

# Compare against the single largest mod-6 class coefficient.
# c_hat6 = gamma6/(48 A_*) = gamma6*sqrt(3)/224.
c_hat6_sqrt3_coeff = gamma6 / 224
assert c_all_sqrt3_coeff == 2 * c_hat6_sqrt3_coeff

getcontext().prec = 50
sqrt3 = Decimal(3).sqrt()
c_all = (
    Decimal(c_all_sqrt3_coeff.numerator)
    / Decimal(c_all_sqrt3_coeff.denominator)
    * sqrt3
)
assert abs(c_all - Decimal("3.18557521574354e-9")) < Decimal("1e-22")

# Abstract six-class balance. Each class is labelled L or U.
# After cross-residue multiplicity <=2, L mass P_L gives >=P_L/8
# distinct blockers and U mass P_U gives >=P_U/16. Verify the
# optimized global lower bound max(P_L/8,P_U/16) >= P/24.
for masses in product(range(5), repeat=6):
    total = sum(masses)
    if total == 0:
        continue
    for labels in product((0, 1), repeat=6):  # 0=L, 1=U
        p_l = sum(m for m, lab in zip(masses, labels) if lab == 0)
        p_u = total - p_l
        best = max(Fraction(p_l, 8), Fraction(p_u, 16))
        assert best >= Fraction(total, 24)

# The 1/3 : 2/3 split is sharp for these conservative coefficients.
assert Fraction(1, 3) / 8 == Fraction(2, 3) / 16 == Fraction(1, 24)

# Multiplicity sanity: if every physical blocker pair can occur at most twice
# among classwise extractions, Q occurrences imply at least ceil(Q/2)
# distinct source pairs.
for q in range(100):
    min_distinct = (q + 1) // 2
    assert 2 * min_distinct >= q
    if min_distinct:
        assert 2 * (min_distinct - 1) < q

print("all-residue Horn aggregation certificate: PASS")
print("s0 =", float(s0))
print("gamma_6 =", float(gamma6))
print("beta_* = s0/48 =", float(beta))
print("c_all =", c_all)
print("c_all / c_hat6 = 2")
