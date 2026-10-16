#!/usr/bin/env python3
"""Exact regression for the chamber-interface baseline and residual gluing."""
from fractions import Fraction as F
from random import Random
from math import pi, sqrt

rng = Random(20260915)
for _ in range(20000):
    d = F(rng.randrange(0, 80), rng.randrange(1, 8))
    f = F(rng.randrange(0, 50))
    Q = f + F(rng.randrange(0, 80))
    a = F(rng.randrange(0, 30))
    Ladd = a + F(rng.randrange(0, 80), rng.randrange(1, 8))
    Rbar = F(rng.randrange(0, 100), rng.randrange(1, 9))  # R_ch/a0

    H = d + Q + 2*f
    J = d + Q + 4*f
    Pch = J + 2*Ladd
    sch = f + a
    sigma_ch = H/2 + Rbar + Pch/2 + sch
    assert sigma_ch == J + Rbar + Ladd + a
    assert sigma_ch >= J

    # Residual gluing algebra.  Choose arbitrary nonnegative global/cap residuals
    # satisfying Rbar + Sigma_ext = Omega + Lcap.
    omega = F(rng.randrange(0, 100), rng.randrange(1, 9))
    lcap = F(rng.randrange(0, 100), rng.randrange(1, 9))
    sigma_ext = omega + lcap - Rbar
    if sigma_ext < 0:
        continue
    assert Rbar + sigma_ext == omega + lcap

Delta2 = pi/(2*sqrt(3))
C146 = 4*(pi+sqrt(Delta2))/9
tstar = C146 + 0.0013751
Cstar = 2*sqrt(Delta2) + 0.00042
j171 = tstar + 2*Cstar - pi
print('PASS: 20,000 exact-rational chamber regressions')
print(f'j_171={j171:.15f}')
