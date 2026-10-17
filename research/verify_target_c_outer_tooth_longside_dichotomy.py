#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C0 = Decimal(2) * s + g
C146 = Decimal(4) * (pi + s) / Decimal(9)


def branch_floor(t):
    R = Decimal('4.5') * t - Decimal(2) * pi - C0
    coupled = pi - t - Decimal(2) * R
    max_floor = coupled / Decimal(3)
    symbolic = Decimal(5) * pi + Decimal(2) * C0 - Decimal(10) * t
    assert abs(coupled - symbolic) < Decimal('1e-70')
    return R, coupled, max_floor


t42 = C146 + Decimal('0.0013751')
R42, coupled42, floor42 = branch_floor(t42)
assert abs(R42 - Decimal('0.00576795')) < Decimal('1e-70')
assert coupled42 > Decimal('1.3091681')
assert floor42 > Decimal('0.4363893')

Rbar, coupled_bar, floor_bar = branch_floor(Decimal('1.8585'))
assert floor_bar > Decimal('0.3110181')

R190, coupled190, floor190 = branch_floor(Decimal('1.90'))
assert floor190 > Decimal('0.1726848')

print('Delta2 =', Delta2)
print('C0 =', C0)
print('C146 =', C146)
print('t42 =', t42)
print('R(t42) =', R42)
print('(N2 + 2 L_>2)/D >=', coupled42)
print('max(N2,L_>2)/D >=', floor42)
print('at t=1.8585 max floor =', floor_bar)
print('at t=1.90 max floor =', floor190)
print('PASS: outer-tooth / long-side dichotomy')
