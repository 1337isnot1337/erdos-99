#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 90
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C0 = Decimal(2) * s + g
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('4.5') * (t - C146) - g

c_beta = Decimal(1) - sqrt3 / Decimal(2)
delta = R / Decimal(2)
kappa = Decimal(0)
x_B = pi + delta - t - kappa
bad_edge_occurrences = delta / c_beta
straight_occurrences = x_B - Decimal(2) * bad_edge_occurrences
transverse_edges = (straight_occurrences - delta) / Decimal(2)
closed_form = (pi - t - R / c_beta) / Decimal(2)

assert R == Decimal('0.00576795')
assert delta == Decimal('0.002883975')
assert x_B > Decimal('1.3235879906')
assert bad_edge_occurrences < Decimal('0.0215262825')
assert straight_occurrences > Decimal('1.2805354256')
assert abs(transverse_edges - closed_form) < Decimal('1e-80')
assert transverse_edges > Decimal('0.6388257253')

print('t42 =', t)
print('R(t42) =', R)
print('1-cos(pi/6) =', c_beta)
print('joint worst delta =', delta)
print('joint worst kappa =', kappa)
print('x_B/D >=', x_B)
print('bad edge occurrences/D <=', bad_edge_occurrences)
print('straight internal occurrences/D >=', straight_occurrences)
print('distinct transverse contacts/D >=', transverse_edges)
print('transverse component > 1/2')
print('PASS: global outer straight-event penetration constants')
