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
t = C146 + Decimal('0.0013751')

R = Decimal('4.5') * (t - C146) - g
delta_max = R / Decimal(2)
kappa_max = Decimal(2) * R

phi_min = C0 / Decimal(2) - t / Decimal(4)
qminusf_max = Decimal(9) * t / Decimal(4) - pi - C0 / Decimal(2)
p5_min = pi + C0 - Decimal('2.5') * t
rank_pent_min = Decimal(2) * p5_min - kappa_max
nonpent_endpoint_max = Decimal(6) * qminusf_max
pentagon_touching_trains_min = Decimal('2.5') * p5_min

B_min = Decimal(5) * phi_min
B_max = Decimal(10) * t - Decimal(5) * pi
T_min = (pi + B_min) / Decimal(2)
T_max = Decimal(5) * t - Decimal(2) * pi

edge_density_min = t / (t + kappa_max)
forest_avg_component_min = t / kappa_max

A_DF = Decimal('12.19736577709914')
F_loc_min = (A_DF - Decimal(6) * t - Decimal(2) * kappa_max) / Decimal(4)
N_loc_min = A_DF / Decimal(2) - Decimal(3) * t - Decimal(2) * kappa_max
local_pent_min = F_loc_min - qminusf_max

assert abs(delta_max - qminusf_max) < Decimal('1e-70')
assert abs(kappa_max - Decimal('0.01153590')) < Decimal('1e-70')
assert rank_pent_min > Decimal('0.97729')
assert nonpent_endpoint_max < Decimal('0.017304')
assert pentagon_touching_trains_min > Decimal('1.23604')
assert B_min > Decimal('2.48650')
assert B_max < Decimal('2.50093')
assert T_min > Decimal('2.81404')
assert T_max < Decimal('2.82127')
assert edge_density_min > Decimal('0.99370')
assert forest_avg_component_min > Decimal('157.8')
assert F_loc_min > Decimal('0.31224')
assert N_loc_min > Decimal('0.61294')
assert local_pent_min > Decimal('0.30935')

print('Delta2 =', Delta2)
print('C0 =', C0)
print('C146 =', C146)
print('t42 =', t)
print('R(t42) =', R)
print('delta/D <=', delta_max)
print('k/D <=', kappa_max)
print('pentagon closure rank / D >=', rank_pent_min)
print('nonpentagon bounded endpoints / D <=', nonpent_endpoint_max)
print('trains touching pentagons / D >=', pentagon_touching_trains_min)
print('B/D in [', B_min, ',', B_max, ']')
print('T/D in [', T_min, ',', T_max, ']')
print('h/q >=', edge_density_min)
print('forest average component size >=', forest_avg_component_min)
print('common-cap F_loc/D >=', F_loc_min)
print('common-cap N(S_D)/D >=', N_loc_min)
print('common-cap local pentagons/D >=', local_pent_min)
print('PASS: low-t topology/network squeeze')
