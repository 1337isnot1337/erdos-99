#!/usr/bin/env python3
"""Exact/asymptotic certificate for fixed-slack reflection-blocker degree and matching."""
from fractions import Fraction as Q
from decimal import Decimal, getcontext
import math

# Reflection slack from eta=15/56 geometry: C = sqrt(3135)/56.
C2 = Q(3135, 56 * 56)
assert C2 == Q(3135, 3136)
gap2 = 1 - C2
assert gap2 == Q(1, 3136)
# Hence sqrt(1-C^2)=1/56 exactly.

# Fixed-slack near-diameter degree leading coefficient.
lead_degree = 448 * (3 ** (1 / 8))

# Existing coupled shallow-apex floor.
getcontext().prec = 70
eta = Decimal(15) / Decimal(56)
T42 = Decimal("1.8208886379794447")
R42 = Decimal("0.00576795")
PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
SQ3 = Decimal(3).sqrt()
K = Decimal(3) + Decimal(1) / eta + Decimal(8) * (Decimal(2) + SQ3)
u0 = (PI - T42 - (K / 2) * R42) / Decimal(5)
assert u0 > Decimal("0.24303602415")

lead_dec = Decimal(448) * (Decimal(3) ** (Decimal(1) / Decimal(8)))
matching_coeff = u0 / (Decimal(2) * lead_dec)
assert matching_coeff > Decimal("0.0002364408355")

# Finite-D regression of the fixed-slack star bound.
C = math.sqrt(3135) / 56
for D in (1e6, 1e8, 1e10, 1e12):
    eta_D = 3 ** 0.25 * math.sqrt(D)
    L = math.sqrt(D * eta_D + eta_D * eta_D + D * C / 2)
    theta = 2 * math.asin(4 * L / (D - C))
    sep = 2 * math.asin(math.sqrt(1 - C * C) / (2 * D))
    degree_bound = 1 + theta / sep
    ratio = degree_bound / D ** 0.75
    assert 0 < ratio < 700

print("tooth reflection blocker matching certificate: PASS")
print("C^2 =", C2, "; 1-C^2 =", gap2)
print("degree leading coefficient = 448*3^(1/8) =", lead_degree)
print("forced-apex floor =", u0)
print("matching D^(1/4) coefficient =", matching_coeff)
