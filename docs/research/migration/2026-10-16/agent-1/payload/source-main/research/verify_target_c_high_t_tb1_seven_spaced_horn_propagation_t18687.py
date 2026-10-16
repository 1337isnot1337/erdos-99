#!/usr/bin/env python3
"""Regression checks for seven-spaced Horn propagation after the six-row bound."""

from fractions import Fraction
from itertools import combinations

s0 = Fraction(791, 320_000_000)
gamma7 = s0 / 14
assert gamma7 == Fraction(113, 640_000_000)

assert gamma7 / 2 == Fraction(113, 1_280_000_000)
assert gamma7 / 4 == Fraction(113, 2_560_000_000)
assert gamma7 / 8 == Fraction(113, 5_120_000_000)
assert gamma7 / 16 == Fraction(113, 10_240_000_000)

Tstar = Fraction(6121, 2000)
cstar7 = gamma7 / (48 * Tstar)
assert cstar7 == Fraction(113, 94_018_560_000)

lower_global_train = (gamma7 / 16) * Fraction(1609, 2500) / Tstar
assert lower_global_train == Fraction(181817, 78_348_800_000_000)

old_gamma15 = s0 / 30
assert gamma7 / old_gamma15 == Fraction(15, 7)

# Finite regression for residue thinning: one mod-7 class has at least 1/7
# of every finite coordinate set, and equal-residue coordinates are 7-spaced.
for m in range(1, 13):
    for mask in range(1, 1 << m):
        S = [i for i in range(m) if (mask >> i) & 1]
        buckets = [[x for x in S if x % 7 == r] for r in range(7)]
        best = max(buckets, key=len)
        assert 7 * len(best) >= len(S)
        for a, b in combinations(best, 2):
            assert abs(a - b) >= 7

# Six-local same-orientation support intervals from seven-spaced owners are disjoint.
for i in range(15):
    for ip in range(i + 7, 22):
        # right-oriented supports
        for j in range(i + 1, i + 7):
            for jp in range(ip + 1, ip + 7):
                A = set(range(i + 1, j + 1))
                B = set(range(ip + 1, jp + 1))
                assert A.isdisjoint(B)

        # left-oriented supports
        for j in range(max(0, i - 6), i):
            for jp in range(max(0, ip - 6), ip):
                A = set(range(j + 1, i + 1))
                B = set(range(jp + 1, ip + 1))
                assert A.isdisjoint(B)

print("seven-spaced Horn propagation certificate: PASS")
print("gamma_7 =", float(gamma7))
print("permanent LOWER density =", float(gamma7 / 4))
print("permanent UPPER density =", float(gamma7 / 8))
print("implication-forest density =", float(gamma7 / 2))
print("localized UPPER c*_7 =", float(cstar7))
print("global LOWER-train coefficient =", float(lower_global_train))
