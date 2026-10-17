#!/usr/bin/env python3
"""Regression checks for all-residue Horn UPPER deduplication."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product

s0 = Fraction(791, 320_000_000)
gamma6 = s0 / 12
old_all = s0 / 48
delta = s0 / 32
sum_floor = s0 / 16

assert gamma6 == Fraction(791, 3_840_000_000)
assert old_all == Fraction(791, 15_360_000_000)
assert delta == Fraction(791, 10_240_000_000)
assert sum_floor == Fraction(791, 5_120_000_000)
assert delta / old_all == Fraction(3, 2)

# c_dedup = delta/(6 A_*), A_*=14/(3 sqrt(3)) = delta*sqrt(3)/28.
c_sqrt3 = delta / 28
assert c_sqrt3 == Fraction(113, 40_960_000_000)

# Single-class six-spaced coefficient has sqrt(3) coefficient 113/122880e9.
c_hat6_sqrt3 = Fraction(113, 122_880_000_000)
assert c_sqrt3 / c_hat6_sqrt3 == 3

# First all-residue coefficient was 791/430080e9 times sqrt(3).
c_all_sqrt3 = Fraction(791, 430_080_000_000)
assert c_sqrt3 / c_all_sqrt3 == Fraction(3, 2)

getcontext().prec = 50
c_dec = (
    Decimal(c_sqrt3.numerator)
    / Decimal(c_sqrt3.denominator)
    * Decimal(3).sqrt()
)
assert abs(c_dec - Decimal("4.77836282361531e-9")) < Decimal("1e-22")

# Abstract class-mass check after UPPER deduplication:
# N_L >= P_L/8, N_U >= P_U/8, hence N_L+N_U >= P/8
# and max(N_L,N_U) >= P/16.
for masses in product(range(5), repeat=6):
    total = sum(masses)
    if total == 0:
        continue
    for labels in product((0, 1), repeat=6):  # 0=L, 1=U
        p_l = sum(m for m, lab in zip(masses, labels) if lab == 0)
        p_u = total - p_l
        n_l = Fraction(p_l, 8)
        n_u = Fraction(p_u, 8)
        assert n_l + n_u == Fraction(total, 8)
        assert max(n_l, n_u) >= Fraction(total, 16)

# If P>(s0/2)D, P/8 gives the s0/16 sum floor, and P/16 the s0/32 dichotomy floor.
assert (s0 / 2) / 8 == sum_floor
assert (s0 / 2) / 16 == delta

print("all-residue UPPER dedup certificate: PASS")
print("sum floor s0/16 =", float(sum_floor))
print("equal-type floor s0/32 =", float(delta))
print("c_dedup =", c_dec)
print("c_dedup / c_hat6 = 3")
print("c_dedup / c_all = 3/2")
