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
A = Decimal(2) / c - Decimal(1)
new_floor = (pi - t - A * R / Decimal(2)) / Decimal(2)
old_floor = (pi - t - R / c) / Decimal(2)

assert R == Decimal('0.00576795')
assert abs(A - (Decimal(7) + Decimal(4) * sqrt3)) < Decimal('1e-90')
assert new_floor - old_floor == R / Decimal(4)
assert new_floor > Decimal('0.6402677128')

print('t42 =', t)
print('R(t42) =', R)
print('c = 1-sqrt(3)/2 =', c)
print('delta coefficient = 2/c-1 =', A)
print('old global floor =', old_floor)
print('new bridge-free global floor =', new_floor)
print('gain = R/4 =', R / Decimal(4))
print('PASS: bridge-free global straight-event floor')
