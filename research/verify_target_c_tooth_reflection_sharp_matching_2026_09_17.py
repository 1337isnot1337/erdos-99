#!/usr/bin/env python3
"""Sharp fixed-slack matching constants for the eta=4/15 tooth branch."""
from fractions import Fraction as Q
from decimal import Decimal, getcontext
import math

# Dedicated reflection/perimeter choice eta=4/15.
# h_eta=2*sqrt(14)/15, so the blocker slack is C=2h_eta=4*sqrt(14)/15.
C2 = Q(16 * 14, 15 * 15)
assert C2 == Q(224, 225)
gap2 = 1 - C2
assert gap2 == Q(1, 225)
# Therefore sqrt(1-C^2)=1/15 exactly.

# Fixed-slack star degree leading coefficient from the general theorem.
lead_degree = 120 * (3 ** (1 / 8))

# Existing eta=4/15 perimeter-collapse tooth population.
getcontext().prec = 70
N2 = Decimal("0.4363893718701161781")
dout = Decimal("0.002883975")
eta = Decimal(4) / Decimal(15)
u4 = N2 - dout / eta
assert abs(u4 - Decimal("0.4255744656201161781")) < Decimal("1e-30")

lead_dec = Decimal(120) * (Decimal(3) ** (Decimal(1) / Decimal(8)))
matching_coeff = u4 / (Decimal(2) * lead_dec)
assert matching_coeff > Decimal("0.0015456962879")

# The dedicated choice improves the previous eta=15/56 matching coefficient by >6.5x.
u_old = Decimal("0.2430360241576561830")
lead_old = Decimal(448) * (Decimal(3) ** (Decimal(1) / Decimal(8)))
old_coeff = u_old / (Decimal(2) * lead_old)
assert matching_coeff / old_coeff > Decimal("6.53")

# Finite-D regression of the exact eta=4/15 fixed-slack degree formula.
C = 4 * math.sqrt(14) / 15
for D in (1e6, 1e8, 1e10, 1e12):
    eta_D = 3 ** 0.25 * math.sqrt(D)
    L = math.sqrt(D * eta_D + eta_D * eta_D + D * C / 2)
    theta = 2 * math.asin(4 * L / (D - C))
    sep = 2 * math.asin(math.sqrt(1 - C * C) / (2 * D))
    degree_bound = 1 + theta / sep
    ratio = degree_bound / D ** 0.75
    assert 0 < ratio < 200

print("sharp tooth reflection matching certificate: PASS")
print("C^2 =", C2, "; 1-C^2 =", gap2)
print("degree leading coefficient = 120*3^(1/8) =", lead_degree)
print("blocked-apex floor =", u4)
print("matching D^(1/4) coefficient =", matching_coeff)
print("improvement factor over eta=15/56 =", matching_coeff / old_coeff)
