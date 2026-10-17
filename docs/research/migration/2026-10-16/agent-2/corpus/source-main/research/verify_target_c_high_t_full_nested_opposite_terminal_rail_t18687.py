#!/usr/bin/env python3
"""Regression checks for the full opposite-or-terminal nested rail."""

from fractions import Fraction as Q
from itertools import combinations_with_replacement
from decimal import Decimal, getcontext

getcontext().prec = 60

# Topological model: after orienting births in increasing interface order and
# deleting the same-host piece, the allowed partner segment consists of the
# far terminal piece (constant label m), followed by the opposite host with
# labels decreasing toward the hub. Any weakly order-preserving partner map,
# including repeated partner positions, therefore has nonincreasing labels.
for m in range(3, 10):
    for k in range(1, m):
        # Three slots model arbitrary multiplicity/positions inside T_m.
        labels = [m, m, m] + list(range(m - 1, k - 1, -1))
        assert all(a >= b for a, b in zip(labels, labels[1:]))
        for n in range(1, min(7, len(labels) + 1)):
            for idxs in combinations_with_replacement(range(len(labels)), n):
                seq = [labels[j] for j in idxs]
                assert all(a >= b for a, b in zip(seq, seq[1:]))

# Unconditional one-bar fork.
s0 = Q(791, 320_000_000)
full_nested = s0 / 2
one_piece = s0 / 4
assert full_nested == Q(791, 640_000_000)
assert one_piece == Q(791, 1_280_000_000)
assert full_nested == 3 * (s0 / 6)

D = Decimal
root8_3 = D(3) ** (D(1) / D(8))
full_disjoint = (D(s0.numerator) / D(s0.denominator)) / (D(8) * root8_3)
assert D('2.69336e-7') < full_disjoint < D('2.69339e-7')

# Current deep exact-force parameter choice.
lam = Q(5085, 1_000_000_000)
assert lam / 2 == Q(25425, 10_000_000_000)
deep_full_disjoint = (D(lam.numerator) / D(lam.denominator)) / (D(4) * root8_3)
assert D('1.10812e-6') < deep_full_disjoint < D('1.10814e-6')

print('PASS: full opposite-or-terminal nested rail regressions')
print('unconditional full nested density =', float(full_nested))
print('unconditional one-piece density =', float(one_piece))
print('unconditional full disjoint coefficient =', full_disjoint)
print('deep 90% full nested density =', float(lam))
print('deep 90% one-piece density =', float(lam / 2))
print('deep full disjoint coefficient =', deep_full_disjoint)
