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

c_beta = Decimal(1) - sqrt3 / Decimal(2)
delta = R / Decimal(2)
kappa = Decimal(0)
x_B = pi + delta - t - kappa
bad_edge_occurrences = delta / c_beta
straight_occurrences = x_B - Decimal(2) * bad_edge_occurrences
distinct_straight_vertices = straight_occurrences - delta
outer_vertices = pi - Decimal(2) * delta / c_beta
outer_walk = pi + delta
outer_defect = outer_walk - outer_vertices
outer_vertex_fraction = outer_vertices / outer_walk

assert R == Decimal('0.00576795')
assert delta == Decimal('0.002883975')
assert straight_occurrences > Decimal('1.2805354256')
assert distinct_straight_vertices > Decimal('1.2776514506')
assert outer_vertices > Decimal('3.0985400886')
assert outer_defect < Decimal('0.0459365400')
assert outer_vertex_fraction > Decimal('0.9853913559')

print('t42 =', t)
print('R(t42) =', R)
print('delta_worst =', delta)
print('x_B/D >=', x_B)
print('bad edge occurrences/D <=', bad_edge_occurrences)
print('straight occurrences/D >=', straight_occurrences)
print('distinct straight unloaded vertices/D >=', distinct_straight_vertices)
print('distinct outer vertices/D >=', outer_vertices)
print('outer walk length/D <=', outer_walk)
print('(b-V_out)/D <=', outer_defect)
print('V_out/b >=', outer_vertex_fraction)
print('PASS: outer-walk near-simplicity constants')
