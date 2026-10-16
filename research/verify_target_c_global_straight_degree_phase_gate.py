#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt2 = Decimal(2).sqrt()
sqrt3 = Decimal(3).sqrt()
sqrt6 = Decimal(6).sqrt()

Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C0 = Decimal(2) * s + g
C146 = Decimal(4) * (pi + s) / Decimal(9)
t = C146 + Decimal('0.0013751')
R = Decimal('4.5') * (t - C146) - g

# beta = pi/12 = 15 degrees.
# cos(pi/12) = (sqrt(6)+sqrt(2))/4.
c15 = Decimal(1) - (sqrt6 + sqrt2) / Decimal(4)
A = Decimal(2) / c15 - Decimal(1)

# The network squeeze is 2*delta + kappa/2 <= R.
# Since A/2 > 2, the straight-vertex lower bound is minimized at
# delta=R/2, kappa=0.
delta = R / Decimal(2)
kappa = Decimal(0)
x_B = pi + delta - t - kappa
bad_edge_occurrences = delta / c15
straight_occurrences = x_B - Decimal(2) * bad_edge_occurrences
closed_form = pi - t - A * R / Decimal(2)

extra_transverse_component = sqrt2 / Decimal(2)
all_extra_edge_floor = straight_occurrences / Decimal(2)
half_cubic_floor = straight_occurrences / Decimal(2)
half_degree4_edge_floor = Decimal(3) * straight_occurrences / Decimal(4)
tradeoff_rhs = Decimal(2) * straight_occurrences

assert R == Decimal('0.00576795')
assert delta == Decimal('0.002883975')
assert A / Decimal(2) > Decimal(2)
assert abs(straight_occurrences - closed_form) < Decimal('1e-90')
assert straight_occurrences > Decimal('1.1543116921')
assert all_extra_edge_floor > Decimal('0.5771558460')
assert half_cubic_floor > Decimal('0.5771558460')
assert half_degree4_edge_floor > Decimal('0.8657337690')
assert tradeoff_rhs > Decimal('2.3086233842')
assert extra_transverse_component > Decimal('0.7071067811')

print('t42 =', t)
print('R(t42) =', R)
print('c15 = 1-cos(pi/12) =', c15)
print('A = 2/c15 - 1 =', A)
print('joint worst delta =', delta)
print('joint worst kappa =', kappa)
print('x_B/D >=', x_B)
print('bad edge occurrences/D <=', bad_edge_occurrences)
print('distinct pi/12-straight vertices/D >=', straight_occurrences)
print('baseline all-extra physical edges/D >=', all_extra_edge_floor)
print('half-split cubic vertices/D >=', half_cubic_floor)
print('half-split degree-4 branch edges/D >=', half_degree4_edge_floor)
print('2 E_all/D + V3/D >=', tradeoff_rhs)
print('every extra transverse component >', extra_transverse_component)
print('PASS: global straight degree/phase-gate constants')
