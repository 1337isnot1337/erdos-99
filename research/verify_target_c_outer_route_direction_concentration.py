#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('4.5') * (t - C146) - g
delta = R / Decimal(2)
branch_floor = (pi - t - Decimal(2) * R) / Decimal(3)

eta = Decimal(1) / Decimal(15)
penetration = (branch_floor - delta / eta) / Decimal(2)

one_minus_cos_beta = Decimal(1) - sqrt3 / Decimal(2)
bad_angle_occ = delta / one_minus_cos_beta
tangent_edges = (branch_floor - bad_angle_occ) / Decimal(2)
unified = min(penetration, tangent_edges)

assert branch_floor > Decimal('0.4363893718')
assert bad_angle_occ < Decimal('0.0215262825')
assert tangent_edges > Decimal('0.2074315447')
assert penetration > Decimal('0.1965648734')
assert unified == penetration

print('t42 =', t)
print('detour density <=', delta)
print('tooth/long-side branch floor =', branch_floor)
print('1-cos(pi/6) =', one_minus_cos_beta)
print('bad angle occurrences/D <=', bad_angle_occ)
print('distinct near-tangent edges/D >=', tangent_edges)
print('distinct penetration edges/D >=', penetration)
print('unified physical-edge density >=', unified)
print('PASS: outer-route direction concentration constants')
