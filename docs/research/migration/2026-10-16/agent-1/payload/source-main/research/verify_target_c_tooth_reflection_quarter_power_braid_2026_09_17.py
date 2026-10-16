#!/usr/bin/env python3
"""Asymptotic constant checks for the eta=4/15 reflection quarter-power braid."""
from decimal import Decimal, getcontext
from fractions import Fraction as Q
import math

getcontext().prec = 80

u4 = Decimal("0.4255744656201161781")

b = Decimal(3) ** (Decimal(1) / Decimal(8))
s = Decimal(3) ** (Decimal(5) / Decimal(8))
A = 2*s + 4*b
B = 8*b

K = Decimal(14)
assert 2*K - 2*A > B
assert 2*K - 2*A > 4*b

assert float(3 ** (1/8)) < 6/5
assert float(3 ** (5/8)) < 21/10
assert 2*Q(21,10) + 8*Q(6,5) < 14

C_K = (Decimal(15) / Decimal(26)) * (2*s + K/2)
coef = (u4 / Decimal(12)) / C_K
coef_formula = Decimal(13) * u4 / (Decimal(90) * (2*s + K/2))
assert abs(coef - coef_formula) < Decimal("1e-60")
assert coef > Decimal("0.00560")

G = 2*K - 2*A
intersection_ratio = 2*b/G
assert intersection_ratio < Decimal("0.25")

old_matching = Decimal("0.001545696287901749")
assert coef / old_matching > Decimal("3.6")

C2 = Q(224, 225)
assert 1 - C2 == Q(1, 225)

for D in (10**12, 10**16, 10**20, 10**24):
    Df = float(D)
    etaD = 3**0.25 * math.sqrt(Df)
    Rp = Df/2 + etaD
    Rm = Df/2 - 2*etaD
    S = math.sqrt(Rp*Rp - Rm*Rm)
    C = 4*math.sqrt(14)/15
    L = math.sqrt(Df*etaD + etaD*etaD + Df*C/2)
    w = 14 * Df**(-0.25)
    base_rad = math.atan(S/(Rm-1))
    block_rad = 2*math.asin(2*L/(Df-C))
    star = 2*math.asin(4*L/(Df-C))
    chord_gap = 2*w - 2*(base_rad + block_rad)
    assert chord_gap > star
    dist_ratio = (2*L/math.sin(chord_gap))/Df
    assert dist_ratio < 0.30

print("tooth reflection quarter-power crossing-braid certificate: PASS")
print("3^(1/8) =", b)
print("3^(5/8) =", s)
print("direction-error coefficient A =", A)
print("shared-endpoint star coefficient B =", B)
print("K =", K, "; selected chord-gap coefficient =", G)
print("bin-cap coefficient C_K =", C_K)
print("D^(1/4) crossing-braid coefficient =", coef)
print("intersection displacement limsup / D <=", intersection_ratio)
print("improvement over prior arbitrary matching coefficient =", coef / old_matching)
