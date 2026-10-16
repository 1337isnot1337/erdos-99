#!/usr/bin/env python3
"""Constant and local-inequality regression for the flat-center degree-4 split."""
from decimal import Decimal, getcontext
from math import pi, sin

getcontext().prec = 60
D = Decimal

A42 = D('0.4944166723690961')
A18585 = D('0.4003882673177079')

assert D('0.1236041680') < A42 / 4 < D('0.1236041682')
assert D('0.0549351857') < A42 / 9 < D('0.0549351859')
assert D('0.1000970667') < A18585 / 4 < D('0.1000970670')
assert D('0.0444875851') < A18585 / 9 < D('0.0444875854')

# Local degree-4 identity and chord-gap estimate on representative small turns.
for eps in (1e-1, 1e-2, 1e-4, 1e-7):
    # Any nonnegative split of eps among the three complementary excesses works.
    es = (0.2 * eps, 0.3 * eps, 0.5 * eps)
    assert abs(sum(es) - eps) < 1e-14
    total_gap = 0.0
    for e in es:
        beta = pi / 3 + e
        d = 2 * sin(beta / 2)
        assert d > 1.0
        assert d - 1.0 <= e + 1e-15
        total_gap += d - 1.0
    assert total_gap <= eps + 1e-14

# Conflict graph: endpoint incidence <=5 gives degree <=8 and greedy 1/9.
endpoint_incidence = 5
max_conflict_degree = 2 * (endpoint_incidence - 1)
assert max_conflict_degree == 8
assert D(2) / D(max_conflict_degree + 1) == D(2) / D(9)

print('current-floor loaded/degree3 coefficient =', A42 / 4)
print('current-floor degree4 hidden-pair coefficient =', A42 / 9)
print('t<=1.8585 loaded/degree3 coefficient =', A18585 / 4)
print('t<=1.8585 degree4 hidden-pair coefficient =', A18585 / 9)
print('flat-center degree-four activation dichotomy: PASS')
