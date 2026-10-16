#!/usr/bin/env python3
"""Constant/exponent checks for the near-quarter-power reflection crossing braid."""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
import math

getcontext().prec = 70

# Parameter chosen close to the exact braid-coefficient optimum, but rational.
eta = Q(3, 26)
s_min = 2 - eta
assert s_min == Q(49, 26)

# Reflection slack C=2*sqrt(eta-eta^2/4).
C2 = 4 * eta - eta * eta
assert C2 == Q(303, 676)
assert 1 - C2 == Q(373, 676)

# Existing shallow-tooth count and outer-detour coefficient.
N2 = Decimal("0.4363893718701161781")
dout = Decimal("0.002883975")
eta_dec = Decimal(3) / Decimal(26)
u = N2 - dout / eta_dec
assert u > Decimal("0.4113949218701")

# With w=D^-1/4 log D, one normal bin has leading capacity
# [1/(2*s_min)] D^(3/4) log D = 13/49 times that scale.
bin_lead = Q(1, 1) / (2 * s_min)
assert bin_lead == Q(13, 49)

# Winning quadrant (1/4), then one residue class modulo 3.
braid_coeff = u * Decimal(49) / Decimal(156)
assert braid_coeff > Decimal("0.1292201998181")

# Exponent/scale checks.
assert Q(3, 4) < 1
for D in (1e16, 1e24, 1e32):
    w = D ** (-1 / 4) * math.log(D)
    direction_error = D ** (-1 / 4)
    central_radius = D ** (3 / 4)
    intersection_scale = central_radius / math.sin(w)
    assert direction_error / w < 1
    assert intersection_scale / D < 1

print("near-quarter reflection crossing-braid certificate: PASS")
print("eta =", eta, "; minimum base length =", s_min)
print("C^2 =", C2, "; 1-C^2 =", 1-C2)
print("upper-blocked density floor =", u)
print("normal-bin leading coefficient =", bin_lead)
print("D^(1/4)/log(D) braid coefficient =", braid_coeff)
