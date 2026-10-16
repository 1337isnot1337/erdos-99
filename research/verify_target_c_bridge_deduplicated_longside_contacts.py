#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 80

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt2 = Decimal(2).sqrt()
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')
C146 = Decimal(4) * (pi + s) / Decimal(9)
t42 = C146 + Decimal('0.0013751')
R42 = Decimal('4.5') * (t42 - C146) - g
delta = R42 / Decimal(2)
longside = (pi - t42 - Decimal(2) * R42) / Decimal(3)
bridge = delta / Decimal(2)

# beta = pi/8: cos(pi/8)=sqrt(2+sqrt(2))/2.
cos_pi_8 = (Decimal(2) + sqrt2).sqrt() / Decimal(2)
one_minus_cos_pi_8 = Decimal(1) - cos_pi_8
bad_pi_8 = delta / one_minus_cos_pi_8
E_pi_8 = longside - bad_pi_8 - bridge

# beta = pi/6.
cos_pi_6 = sqrt3 / Decimal(2)
one_minus_cos_pi_6 = Decimal(1) - cos_pi_6
bad_pi_6 = delta / one_minus_cos_pi_6
E_pi_6 = longside - bad_pi_6 - bridge

# Companion tooth/internal branch at eta=1/15.
eta = Decimal(1) / Decimal(15)
E_internal = longside - delta / eta
uniform_floor = min(E_internal, E_pi_8)

assert R42 == Decimal('0.00576795')
assert delta == Decimal('0.002883975')
assert bridge == Decimal('0.0014419875')
assert E_pi_8 > Decimal('0.39706039')
assert E_pi_6 > Decimal('0.41342110')
assert E_internal > Decimal('0.39312974')
assert E_pi_8 > E_internal
assert uniform_floor == E_internal

print('t42 =', t42)
print('d_out/D <=', delta)
print('long-side floor =', longside)
print('outer bridges/D <=', bridge, '+ o(1)')
print('1-cos(pi/8) =', one_minus_cos_pi_8)
print('bad pi/8 occurrences/D <=', bad_pi_8)
print('distinct pi/8 near-tangent edges/D >=', E_pi_8)
print('distinct pi/6 near-tangent edges/D >=', E_pi_6)
print('companion internal tooth edges/D >=', E_internal)
print('branch-uniform physical-edge floor =', uniform_floor)
print('PASS: bridge-deduplicated long-side constants')
