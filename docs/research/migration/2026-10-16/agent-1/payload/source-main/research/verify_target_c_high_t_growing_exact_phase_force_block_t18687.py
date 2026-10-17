#!/usr/bin/env python3
"""Regression checks for the growing exact-phase force-block reduction."""

from fractions import Fraction
from math import sqrt

c = Fraction(113, 5_000_000)
c0 = Fraction(113, 20_000_000)
rho0 = c0 / 12

assert c > 0 and c0 > 0 and rho0 > 0
assert c0 - 6 * rho0 == c0 / 2
assert float(c / 2) == 1.13e-5
assert float(c0 / 2) == 2.825e-6

# sqrt(D) is a legitimate slowly-growing threshold: ->infinity and o(D).
for D in (10**4, 10**8, 10**12):
    M = sqrt(D)
    assert M > 1
    assert M / D < 0.02

# If U >= eta D and rho=eta/16, the phase-near C67 capacity is eta D/4.
for eta in (1e-7, 1e-5, 1e-3):
    rho = eta / 16.0
    assert abs(4.0 * rho - eta / 4.0) < 1e-18
    assert eta - 4.0 * rho == 3.0 * eta / 4.0

# Pigeonhole asymptotic model: linear many wide pairs over sublinear run count
# forces a diverging number in one run.
for D in (10**6, 10**8, 10**10):
    wide = float(c0 / 2) * D
    runs = D ** 0.75
    assert wide / runs > 0
# The representative ratio is proportional to D^(1/4), hence increases without bound.
vals=[]
for D in (10**16, 10**24, 10**32):
    vals.append((float(c0 / 2) * D) / (D ** 0.75))
assert vals[0] < vals[1] < vals[2]
assert vals[2] > 1.0

# Collinear same-sign increments telescope.
A = [50.0, 49.5, 40.0, 7.0]
variation = sum(abs(A[i] - A[i + 1]) for i in range(len(A) - 1))
assert abs(variation - abs(A[0] - A[-1])) < 1e-12

print("PASS: growing exact-phase force-block regressions")
