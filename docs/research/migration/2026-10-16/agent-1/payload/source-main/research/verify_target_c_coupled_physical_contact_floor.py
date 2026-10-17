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

eta = Decimal(15) / Decimal(56)
cos_alpha = Decimal(1) - eta / Decimal(2)
sin_alpha = (Decimal(1) - cos_alpha * cos_alpha).sqrt()
Y_tooth = sqrt3 / Decimal(2) * cos_alpha - Decimal('0.5') * sin_alpha
Y_tooth_exact = (Decimal(97) * sqrt3 - Decimal(3135).sqrt()) / Decimal(224)

c_beta = Decimal(1) - sqrt3 / Decimal(2)
K = Decimal(3) + Decimal(1) / eta + Decimal(4) / c_beta
K_exact = Decimal(341) / Decimal(15) + Decimal(8) * sqrt3
physical_floor = (pi - t - K * R / Decimal(2)) / Decimal(6)

# Worst endpoint of the joint network squeeze: delta=R/2, kappa=0.
delta = R / Decimal(2)
branch_burden = pi - t - delta
ct = delta / (Decimal(2) * eta)
cl = delta / c_beta + delta / Decimal(2)
direct_floor = (branch_burden - Decimal(2) * ct - Decimal(4) * cl) / Decimal(6)

assert cos_alpha * cos_alpha - Decimal(3) / Decimal(4) == Decimal(1) / Decimal(12544)
assert cos_alpha > sqrt3 / Decimal(2)
assert abs(Y_tooth - Y_tooth_exact) < Decimal('1e-80')
assert Y_tooth > Decimal('0.5000797215')
assert abs(K - K_exact) < Decimal('1e-80')
assert R == Decimal('0.00576795')
assert abs(physical_floor - direct_floor) < Decimal('1e-80')
assert physical_floor > Decimal('0.2025300201')

print('t42 =', t)
print('R(t42) =', R)
print('eta =', eta)
print('cos(alpha_eta) =', cos_alpha)
print('cos(alpha)^2 - 3/4 =', cos_alpha * cos_alpha - Decimal(3) / Decimal(4))
print('tooth inward component >', Y_tooth)
print('c_beta =', c_beta)
print('K =', K)
print('joint worst delta =', delta)
print('joint worst kappa = 0')
print('physical contact floor =', physical_floor)
print('PASS: coupled physical-contact floor constants')
