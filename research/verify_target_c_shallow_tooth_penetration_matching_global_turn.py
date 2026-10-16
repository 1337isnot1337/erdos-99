#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
sqrt14 = Decimal(14).sqrt()
sqrt42 = Decimal(42).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C146 = Decimal(4) * (pi + s) / Decimal(9)
t42 = C146 + Decimal('0.0013751')
R42 = Decimal('4.5') * (t42 - C146) - g
delta = R42 / Decimal(2)
tooth_floor = (pi - t42 - Decimal(2) * R42) / Decimal(3)

eta = Decimal(4) / Decimal(15)
cos_alpha = Decimal(13) / Decimal(15)
sin_alpha = Decimal(2) * sqrt14 / Decimal(15)
tangent_cap = (Decimal(13) + Decimal(2) * sqrt42) / Decimal(30)
tangent_margin = cos_alpha - tangent_cap
Y = (Decimal(13) * sqrt3 - Decimal(2) * sqrt14) / Decimal(30)
matching = tooth_floor - delta / eta
endpoint_population = Decimal(2) * matching
internal_edge_floor = Decimal(2) * matching
attachment_edge_floor = Decimal(2) * matching
combined_edge_floor = Decimal(4) * matching
loaded_neighbor_margin = Decimal('0.5') + tangent_margin

eta0 = Decimal(2) - sqrt3
assert eta < eta0
assert tangent_margin > Decimal('0.00128')
assert Decimal(2) * tangent_margin > Decimal('0.00256')
assert Y > Decimal('0.5011115')
assert matching > Decimal('0.4255744656')
assert endpoint_population > Decimal('0.8511489312')
assert combined_edge_floor > Decimal('1.7022978624')
assert loaded_neighbor_margin > Decimal('0.50128')
assert sin_alpha < Decimal('0.5')

print('eta0 =', eta0)
print('eta =', eta)
print('cos(alpha_eta) =', cos_alpha)
print('sin(alpha_eta) =', sin_alpha)
print('tangent cap =', tangent_cap)
print('per-side tangent margin =', tangent_margin)
print('two-side tangent margin =', Decimal(2) * tangent_margin)
print('inward component floor =', Y)
print('matching/D >=', matching)
print('distinct matching endpoints/D >=', endpoint_population)
print('internal edge incidence floor/D >=', internal_edge_floor)
print('attachment edge floor/D >=', attachment_edge_floor)
print('combined edge floor/D >=', combined_edge_floor)
print('loaded-neighbor contradiction margin =', loaded_neighbor_margin)
print('PASS: widened penetration matching constants')
