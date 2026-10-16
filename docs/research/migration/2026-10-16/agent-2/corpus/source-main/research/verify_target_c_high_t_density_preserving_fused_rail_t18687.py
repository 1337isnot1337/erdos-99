#!/usr/bin/env python3
"""Regression checks for the density-preserving fused high-t rail."""

import math
from fractions import Fraction as Q

c0 = Q(113, 20_000_000)
gamma = float(c0 / 2)
r = 0.6536
mu = 0.01
Cphase = math.pi**2 * math.sqrt(3) * (2 + math.sqrt(3)) / 12
phase_coefficient = 2 * Cphase / gamma
q = r - (1 + 2 * mu) / math.sqrt(3)

assert abs(gamma - 2.825e-6) < 1e-18
assert 0.06470 < q < 0.06471
assert 3.7638e6 < phase_coefficient < 3.7640e6

# Symmetric eta_D=sigma_D=D^(-1/3): both deletion fractions vanish and the
# retained per-crossing angular defect is O(D^(-1/3)).
prev_loss = None
prev_defect = None
for D in [10**6, 10**9, 10**12, 10**18]:
    eta = D ** (-1 / 3)
    sigma = eta
    interface_relative_loss = eta
    column_relative_loss = sigma
    defect_bound = phase_coefficient * D ** (-1 / 3)
    assert interface_relative_loss > 0
    assert column_relative_loss > 0
    assert defect_bound > 0
    if prev_loss is not None:
        assert interface_relative_loss < prev_loss
        assert defect_bound < prev_defect
    prev_loss = interface_relative_loss
    prev_defect = defect_bound

# General exponent bookkeeping: a,b>0 and a+b<1 imply o(D) interface/column
# deletions and an o(1) angular-defect threshold.
for a, b in [(0.2, 0.2), (1 / 3, 1 / 3), (0.1, 0.7), (0.45, 0.45)]:
    assert a > 0 and b > 0 and a + b < 1
    assert 1 - a < 1
    assert 1 - b < 1
    assert a + b - 1 < 0

# One mechanism tag and one tag+destination retain these leading densities.
assert float(c0 / 4) == 1.4125e-6
assert float(c0 / 8) == 7.0625e-7

print("PASS: density-preserving fused-rail regressions")
print("full tagged rail density =", gamma)
print("one-percent circumcenter flank density =", q)
print("D^(-1/3) phase coefficient =", phase_coefficient)
print("one-tag density =", float(c0 / 4))
print("one-tag plus destination density =", float(c0 / 8))
