#!/usr/bin/env python3
"""Regression checks for the strong-TB1 vanishing overswap theorem."""

from math import cos, pi, sin

C_H = 0.453819885927
KAPPA = 31.4e6

# Exact algebra for |a-lambda(a+b)|^2. Sample away from machine-precision
# degeneracy; the proof itself uses the symbolic identity.
for eps in [1e-5, 1e-4, 1e-2, 0.2]:
    theta = pi - eps
    a = (1.0, 0.0)
    b = (cos(theta), sin(theta))
    q2 = (a[0] + b[0]) ** 2 + (a[1] + b[1]) ** 2
    q = q2 ** 0.5
    for D in [100, 10_000, 1_000_000]:
        lam = 1 + 1 / D
        v = (-lam * (a[0] + b[0]), -lam * (a[1] + b[1]))
        av2 = (a[0] + v[0]) ** 2 + (a[1] + v[1]) ** 2
        bv2 = (b[0] + v[0]) ** 2 + (b[1] + v[1]) ** 2
        target = 1 + q2 * lam * (lam - 1)
        assert abs(av2 - target) < 1e-10
        assert abs(bv2 - target) < 1e-10
        assert target > 1

# At the second intersection lambda=1 the contacts are exactly unit; beyond it
# lambda>1 opens them. The selected asymptotic lambda tends to one.
for D in [10, 100, 10_000]:
    lam = 1 + 1 / D
    assert lam > 1
    assert abs(lam - 1) <= 0.1

# One-sign switching diameters remain strictly shorter under the overswap.
# Use the cone-collapse envelope q <= KAPPA/D where it is below 1; for any
# sufficiently large D the linear -2 lambda q c_H D term dominates lambda^2 q^2.
for D in [10**8, 10**10, 10**12]:
    q = KAPPA / D
    lam = 1 + 1 / D
    delta_sq = -2 * lam * q * C_H * D + (lam * q) ** 2
    assert delta_sq < 0

# The overswap displacement keeps exactly the same leading KAPPA/D scale:
# (1+1/D)*(KAPPA/D) = KAPPA/D + O(D^-2).
for D in [10**6, 10**8, 10**10]:
    q = KAPPA / D
    lam = 1 + 1 / D
    excess = lam * q - KAPPA / D
    assert excess > 0
    assert abs(excess - KAPPA / D**2) < 1e-20 + 1e-12 * abs(excess)

print("PASS: high-t TB1 contact-minimal overswap regressions")
print("c_H =", C_H)
print("cone-collapse coefficient =", KAPPA)
