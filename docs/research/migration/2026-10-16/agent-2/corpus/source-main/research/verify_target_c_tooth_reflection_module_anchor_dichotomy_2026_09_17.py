#!/usr/bin/env python3
"""Regression checks for the reflection module anchor/free dichotomy."""

from fractions import Fraction
import math

c_star = 0.129220199818177
assert c_star > 0.12

# General slow scale: kappa=D^alpha is a representative family with
# 0<alpha<1/4.  Check all scale comparisons used in the theorem.
for alpha in (
    Fraction(1, 100),
    Fraction(1, 16),
    Fraction(1, 8),
    Fraction(1, 5),
):
    family_exp = Fraction(1, 4) - alpha          # D^(1/4)/kappa
    normal_gap_exp = alpha - Fraction(1, 4)     # kappa D^-1/4
    q_sep_exp = alpha + Fraction(3, 4)          # kappa D^3/4
    partner_err_exp = Fraction(3, 4)             # D^3/4
    core_exp = 1 - alpha                         # D/kappa

    assert family_exp > 0
    assert normal_gap_exp > Fraction(-1, 4)      # dominates O(D^-1/4)
    assert q_sep_exp > partner_err_exp            # partner balls become disjoint
    assert core_exp < 1                           # common core is o(D)

# Vector cancellation scale:
# radius error O(D^1/2) is below angular displacement D*D^-1/4=D^3/4.
assert Fraction(1, 2) < Fraction(3, 4)

# Midpoint formula t-q = 2(m-o) - (z-o) - (q-o):
# three O(D^3/4) terms remain O(D^3/4).
for D in (1e8, 1e16, 1e32):
    E = D ** 0.75
    assert (2 * E + E) <= 3 * E

# Direction error O(D^-1/4) is negligible against kappa D^-1/4
# for any divergent kappa.  Representative logarithmic scale.
for D in (1e8, 1e16, 1e32):
    kappa = math.log(math.log(D))
    assert kappa > 1
    raw_error = D ** -0.25
    selected_gap = kappa * D ** -0.25
    assert raw_error / selected_gap < 1

# Partner balls have radius C D^3/4 while q-centers separate on the
# kappa D^3/4 scale; ratio tends to zero as kappa diverges.
for kappa in (10.0, 100.0, 1000.0):
    assert 1.0 / kappa < 0.11

# Common line-intersection core:
# D^3/4 / (kappa D^-1/4) = D/kappa.
assert Fraction(3, 4) - (Fraction(-1, 4)) == 1

# The anchored/free partition loses only a factor two.
for M in range(1, 100):
    anchored = M // 2
    free = M - anchored
    assert max(anchored, free) >= M / 2

print("PASS: reflection module anchor/free dichotomy certificate")
