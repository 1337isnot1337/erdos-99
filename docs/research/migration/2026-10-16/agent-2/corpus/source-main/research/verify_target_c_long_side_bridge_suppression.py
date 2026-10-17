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
long_side_floor = (pi - t - Decimal(2) * R) / Decimal(3)

one_minus_cos_beta = Decimal(1) - sqrt3 / Decimal(2)
bad_edge_occurrences = delta / one_minus_cos_beta
straight_occurrences = long_side_floor - Decimal(2) * bad_edge_occurrences
transverse_edges = (straight_occurrences - delta) / Decimal(10)

assert long_side_floor > Decimal('0.4363893718')
assert bad_edge_occurrences < Decimal('0.0215262825')
assert straight_occurrences > Decimal('0.3933368069')
assert transverse_edges > Decimal('0.0390452831')

print('t42 =', t)
print('outer detour density <=', delta)
print('long-side density >=', long_side_floor)
print('bad edge occurrences/D <=', bad_edge_occurrences)
print('near-straight internal occurrences/D >=', straight_occurrences)
print('2*loaded-degree-two-events/D <=', delta, 'by bridge suppression')
print('distinct transverse edges/D >=', transverse_edges)
print('transverse component > 1/2')
print('PASS: long-side bridge suppression constants')
