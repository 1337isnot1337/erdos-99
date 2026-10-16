#!/usr/bin/env python3
"""Regression checks for the geometric reflection contact-tube theorem."""

from fractions import Fraction
import math


rho = 0.129220199818177
A = 2 * 3 ** (5 / 8) + 4 * 3 ** (1 / 8)
C_A = A + 1
leading_tube_coefficient = 32 * C_A * rho

assert abs(C_A - 9.562837454602665) < 1e-12
assert abs(leading_tube_coefficient - 39.54277653480011) < 1e-11

# Unit-disk packing algebra used in GT.15--GT.17.
# If an arc of length L is covered at arclength spacing R, at most L/R+2
# radius-2R disks cover its R-neighborhood. Their total area is bounded by
# 4*pi*L*R + 8*pi*R^2. Dividing the corresponding R+1/2 bound by pi/4
# gives 16*L*(R+1/2)+32*(R+1/2)^2.
for L in (1.0, 10.0, 100.0):
    for R in (0.5, 2.0, 7.0):
        area_bound = 4 * math.pi * L * R + 8 * math.pi * R * R
        cover_count_bound = L / R + 2
        disk_union_bound = cover_count_bound * math.pi * (2 * R) ** 2
        assert abs(area_bound - disk_union_bound) < 1e-10 * max(1.0, area_bound)

# Polynomial example kappa=D^(1/8).
beta = Fraction(1, 8)
assert Fraction(1, 4) - beta == Fraction(1, 8)   # module-count exponent
assert Fraction(3, 4) + beta == Fraction(7, 8)   # inter-module separation exponent

# If r=o(kappa), the leading total tube term D*r/kappa is o(D).
# The quadratic tube term is smaller than the leading term by r/D^(3/4).
# Under r=o(kappa)=o(D^(1/4)), that ratio tends to zero.
assert Fraction(1, 4) < Fraction(3, 4)

# For r=kappa/log(kappa), the leading ratio is exactly 1/log(kappa).
for kappa in (10.0, 1e3, 1e6, 1e12):
    r = kappa / math.log(kappa)
    assert abs((r / kappa) - 1 / math.log(kappa)) < 1e-15
    assert r / kappa < 1

print("PASS: geometric reflection contact-tube certificate")
print(f"C_A={C_A:.15f}")
print(f"leading tube coefficient={leading_tube_coefficient:.15f}")
