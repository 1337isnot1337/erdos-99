#!/usr/bin/env python3
"""Regression checks for the growing high-t dense cusp ladder."""

import math

r0 = 0.6536
H = 1_109_000
mu = 0.01
q = r0 - (1 + 2 * mu) / math.sqrt(3)

assert 0.06470 < q < 0.06471

# Balanced choice R_D=D^(1/3), sigma_D=D^(-1/3):
# R_D/D -> 0, sigma_D -> 0, and R_D/(sigma_D D)=D^(-1/3) -> 0.
prev_r_rel = None
prev_sigma = None
prev_defect = None
for D in [10**9, 10**12, 10**15, 10**18]:
    R = D ** (1 / 3)
    sigma = D ** (-1 / 3)
    r_rel = R / D
    defect = H * R / (sigma * D)

    assert r_rel > 0
    assert sigma > 0
    assert defect > 0
    assert abs(defect - H * D ** (-1 / 3)) / defect < 1e-12
    assert R / (sigma * D) < 1

    if prev_r_rel is not None:
        assert r_rel < prev_r_rel
        assert sigma < prev_sigma
        assert defect < prev_defect

    prev_r_rel = r_rel
    prev_sigma = sigma
    prev_defect = defect

# A fixed hub interface belongs to at most R length-R windows.  For R=o(D)
# this removes only o(D) windows from a linearly long row block.
for D in [10**9, 10**12, 10**15]:
    R = D ** (1 / 3)
    assert R / D < 1e-5

# General exponent bookkeeping: R_D=D^a, sigma_D=D^-b with
# a,b>0 and a+b<1 gives o(D) hub/column losses and o(1) defect.
for a, b in [(0.2, 0.2), (1 / 3, 1 / 3), (0.4, 0.2), (0.1, 0.7)]:
    assert 0 < a < 1
    assert 0 < b < 1 - a
    assert a - 1 < 0
    assert -b < 0
    assert a + b - 1 < 0

print("PASS: growing high-t dense-cusp-ladder regressions")
print("one-percent circumcenter flank density =", q)
print("balanced depth exponent = 1/3")
print("balanced defect coefficient =", H)
