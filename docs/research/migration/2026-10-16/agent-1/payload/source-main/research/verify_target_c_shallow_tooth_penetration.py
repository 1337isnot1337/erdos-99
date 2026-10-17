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
delta = R / Decimal(2)
branch_floor = (pi - t - Decimal(2) * R) / Decimal(3)

eta = Decimal('0.02')
cos_alpha = Decimal(1) - eta / Decimal(2)
sin_alpha = (Decimal(1) - cos_alpha * cos_alpha).sqrt()
Y = sqrt3 / Decimal(2) * cos_alpha - Decimal('0.5') * sin_alpha
cos_pi_12 = (Decimal(2) + sqrt3).sqrt() / Decimal(2)

bad_allowance = delta / eta
shallow = branch_floor - bad_allowance
apices = shallow / Decimal(2)
penetration_edges = apices / Decimal(2)

assert cos_alpha > cos_pi_12
assert branch_floor > Decimal('0.4363893')
assert bad_allowance < Decimal('0.144199')
assert shallow > Decimal('0.2921906')
assert apices > Decimal('0.1460953')
assert penetration_edges > Decimal('0.0730476')
assert Y > Decimal('0.7868314')

print('t42 =', t)
print('detour density <=', delta)
print('tooth branch density >=', branch_floor)
print('eta =', eta)
print('bad tooth allowance <=', bad_allowance)
print('shallow teeth/D >=', shallow)
print('distinct shallow apices/D >=', apices)
print('distinct penetration edges/D >=', penetration_edges)
print('inward normal component >', Y)
print('cos(alpha_eta) =', cos_alpha)
print('cos(pi/12) =', cos_pi_12)
print('PASS: shallow-tooth penetration')
