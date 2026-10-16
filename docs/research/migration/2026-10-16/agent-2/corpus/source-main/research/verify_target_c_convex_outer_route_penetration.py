#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('4.5') * (t - C146) - g
c = Decimal(1) - sqrt3 / Decimal(2)
coeff = Decimal(1) / c
floor = pi - t - coeff * R / Decimal(2)
old_signed = pi - t - (Decimal(2) / c - Decimal(1)) * R / Decimal(2)

assert R == Decimal('0.00576795')
assert abs(coeff - (Decimal(4) + Decimal(2) * sqrt3)) < Decimal('1e-90')
assert floor > Decimal('1.2991777331')
assert floor > old_signed

print('t42 =', t)
print('R(t42) =', R)
print('c = 1-sqrt(3)/2 =', c)
print('convex-route detour coefficient = 1/c =', coeff)
print('old signed arbitrary-walk floor =', old_signed)
print('convex-route signed floor =', floor)
print('gain =', floor - old_signed)
print('PASS: convex outer-route penetration constants')
