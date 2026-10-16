#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100

pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
s = Delta2.sqrt()
g = Decimal('0.00042')

C146 = Decimal(4) * (pi + s) / Decimal(9)
t42 = C146 + Decimal('0.0013751')
R = Decimal('4.5') * (t42 - C146) - g

# beta = pi/6.
cos_beta = sqrt3 / Decimal(2)
c_beta = Decimal(1) - cos_beta

# Joint split-route inequality:
#   d_out >= c_beta A_beta + 2 cos(beta) r.
# Since 2 cos(beta) > c_beta, A_beta+r <= d_out/c_beta.
assert Decimal(2) * cos_beta > c_beta

normalized_detour_coeff = Decimal(1) / c_beta - Decimal(1)
expected_coeff = Decimal(3) + Decimal(2) * sqrt3
assert abs(normalized_detour_coeff - expected_coeff) < Decimal('1e-90')

floor = pi - t42 - normalized_detour_coeff * R / Decimal(2)

# Compare against the already merged signed arbitrary-walk floor.
old_coeff = Decimal(2) / c_beta - Decimal(1)
old_floor = pi - t42 - old_coeff * R / Decimal(2)

assert R == Decimal('0.00576795')
assert floor > Decimal('1.3020617081')
assert floor > old_floor

print('C146 =', C146)
print('t42 =', t42)
print('R(t42) =', R)
print('c_beta = 1-sqrt(3)/2 =', c_beta)
print('2 cos(beta) =', Decimal(2) * cos_beta)
print('normalized joint detour coefficient =', normalized_detour_coeff)
print('old signed arbitrary-walk floor =', old_floor)
print('convex joint-energy floor =', floor)
print('gain =', floor - old_floor)
print('PASS: convex-route joint energy floor')
