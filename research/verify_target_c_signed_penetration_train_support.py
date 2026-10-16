#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')

Tmax = Decimal(5) * t - Decimal(2) * pi
TRmin = Decimal(2) * s + Decimal('0.0004')
Smax = Tmax - TRmin

Eall = Decimal('1.1543116921171727469')
Esimp = Decimal('1.1083751522061389353')
Er_all = Eall - Smax
Er_simp = Esimp - Smax
half = Er_simp / Decimal(2)
train_floor = half / Decimal(2)

assert Smax < Decimal('0.9162322690')
assert Er_all > Decimal('0.2380794231')
assert Er_simp > Decimal('0.1921428832')
assert half > Decimal('0.0960714416')
assert train_floor > Decimal('0.0480357208')

print('t42 =', t)
print('T/D <=', Tmax)
print('T_R/D >=', TRmin)
print('S/D <=', Smax)
print('all penetration rhombic-train edges/D >=', Er_all)
print('simple penetration rhombic-train edges/D >=', Er_simp)
print('terminal/internal half floor/D >=', half)
print('distinct terminal-hit trains/D >=', train_floor)
print('PASS: signed penetration train-support constants')
