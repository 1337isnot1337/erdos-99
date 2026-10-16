#!/usr/bin/env python3
"""Arithmetic regression for WO145 rhombic flat-center unloading."""
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
S = D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
G = D('0.00145')
EPS = D('0.0015914')
T = D(4) / D(9) * (PI + S) + EPS
L = T + 2 * G
PFLAT = PI + 2 * S + G - D('2.5') * T
TCEIL = 5 * T - 2 * PI
TRLOW = 2 * S + (T + 2 * G) / 4
SUP = TCEIL - TRLOW
ULOADED = PFLAT - SUP / 2
H4 = ULOADED / 9
E3 = ULOADED / 4
TPOS = D(8) / D(39) * (2 * PI + 3 * S + D(5) * G / 4)

assert D('1.82110') < T < D('1.82111')
assert D('1.82400') < L < D('1.82401')
assert D('0.49490') < PFLAT < D('0.49491')
assert D('2.82233') < TCEIL < D('2.82235')
assert D('2.36062') < TRLOW < D('2.36064')
assert D('0.46170') < SUP < D('0.46172')
assert D('0.26404') < ULOADED < D('0.26406')
assert D('0.02933') < H4 < D('0.02935')
assert D('0.06601') < E3 < D('0.06602')
assert D('1.87526') < TPOS < D('1.87528')

print('PASS: WO145 rhombic flat-center unloading arithmetic')
print('t145 =', T)
print('lossless train defect =', L)
print('flat-center floor =', PFLAT)
print('total-train ceiling =', TCEIL)
print('rhombic-train floor =', TRLOW)
print('singleton ceiling =', SUP)
print('unloaded flat-center floor =', ULOADED)
print('hidden-pair floor =', H4)
print('low-stress-contact floor =', E3)
print('algebraic positivity threshold =', TPOS)
