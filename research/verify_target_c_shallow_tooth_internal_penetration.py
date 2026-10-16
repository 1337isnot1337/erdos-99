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
t42 = C146 + Decimal('0.0013751')

# AG42 / low-t topology-network endpoint.
R42 = Decimal('4.5') * (t42 - C146) - g
delta_max = R42 / Decimal(2)

# Tooth branch of N2 + 2 L_{>2} >= pi - t - 2R.
tooth_branch = (pi - t42 - Decimal(2) * R42) / Decimal(3)

eta = Decimal('0.06')
cos_alpha = Decimal(1) - eta / Decimal(2)
sin_alpha = (Decimal(1) - cos_alpha * cos_alpha).sqrt()
cos_pi_12 = (Decimal(2) + sqrt3).sqrt() / Decimal(2)
sin_pi_12 = (Decimal(2) - sqrt3).sqrt() / Decimal(2)
eta0 = Decimal(2) * (Decimal(1) - cos_pi_12)

# Markov loss from the exact metric tooth-detour sum.
shallow_internal = tooth_branch - delta_max / eta

# Edge normal component from the triangle-free third-neighbor geometry.
Y_eta = sqrt3 / Decimal(2) * cos_alpha - sin_alpha / Decimal(2)
normal_flux = shallow_internal * Y_eta
absolute_depth_floor = sqrt3 / Decimal(2)

# Count-only endpoint as eta increases to eta0 from below.
count_supremum = tooth_branch - delta_max / eta0

assert R42 == Decimal('0.00576795')
assert delta_max == Decimal('0.002883975')
assert eta < eta0
assert cos_alpha > cos_pi_12
assert sin_alpha < sin_pi_12
assert tooth_branch > Decimal('0.4363893')
assert shallow_internal > Decimal('0.3883231')
assert Y_eta > Decimal('0.7184921')
assert normal_flux > Decimal('0.27900712')
assert absolute_depth_floor > Decimal('0.8660254')
assert count_supremum > Decimal('0.3940702')

print('C146 =', C146)
print('t42 =', t42)
print('R(t42) =', R42)
print('d_out/D <=', delta_max)
print('tooth-branch N2/D >=', tooth_branch)
print('eta0 =', eta0)
print('eta =', eta)
print('cos(alpha_eta) =', cos_alpha)
print('cos(pi/12) =', cos_pi_12)
print('sin(alpha_eta) =', sin_alpha)
print('sin(pi/12) =', sin_pi_12)
print('distinct internal penetration edges/D >=', shallow_internal)
print('local inward normal component >', Y_eta)
print('local-normal penetration flux/D >', normal_flux)
print('inner endpoint depth >', absolute_depth_floor)
print('count supremum as eta -> eta0- =', count_supremum)
print('PASS: shallow-tooth internal penetration constants')
