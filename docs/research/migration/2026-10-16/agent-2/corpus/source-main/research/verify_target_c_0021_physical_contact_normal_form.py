#!/usr/bin/env python3
"""High-precision arithmetic regression for the g=0.0021 physical-contact normal form."""
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
pi = D('3.14159265358979323846264338327950288419716939937510')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s = Delta2.sqrt()
g = D('0.0021')
C0 = D(2) * s + g
C146 = D(4) * (pi + s) / D(9)
t = C146 + D('0.0017279')
R = D('4.5') * t - D(2) * pi - C0
delta = R / D(2)
F = (pi - t - D(2) * R) / D(3)

eta = D(4) / D(15)
tooth = (F - delta / eta) / D(2)
Y = (D(13) * sqrt3 - D(2) * D(14).sqrt()) / D(30)

c = D(1) - sqrt3 / D(2)
long_side = (F - delta * (D(1) + D(2) / c)) / D(10)

assert R == D('0.00567555')
assert delta == D('0.002837775')
assert F > D('0.43633337187011617')
assert tooth > D('0.21284585781005808')
assert Y > D('0.50111152416158406')
assert long_side > D('0.03911327149483210')

print('PASS g=0.0021 physical-contact normal form')
print('Delta2 =', Delta2)
print('sqrt(Delta2) =', s)
print('C0 =', C0)
print('C146 =', C146)
print('t21 =', t)
print('R(t21) =', R)
print('delta_max =', delta)
print('branch_floor =', F)
print('tooth_contact_floor =', tooth)
print('tooth_inward_component =', Y)
print('long_side_transverse_floor =', long_side)
