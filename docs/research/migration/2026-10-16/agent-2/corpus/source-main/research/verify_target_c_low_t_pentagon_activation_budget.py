#!/usr/bin/env python3
"""Non-load-bearing regression for the low-t pentagon activation budget."""
from decimal import Decimal, getcontext
import math

getcontext().prec = 70

# Local endpoint calculus.
sqrt3f = math.sqrt(3.0)
a0f = sqrt3f / 2.0

def F(s):
    return 0.25 * s * math.sqrt(4.0 - s * s)

def Fp(s):
    return (2.0 - s * s) / (2.0 * math.sqrt(4.0 - s * s))

def S(x, y):
    return 4.0 * x * x * y * y - (x * x + y * y - 1.0) ** 2

def G(x, y):
    return 0.25 * math.sqrt(S(x, y))

def Gx(x, y):
    return x * (y * y - x * x + 1.0) / (2.0 * math.sqrt(S(x, y)))

def Gy(x, y):
    return y * (x * x - y * y + 1.0) / (2.0 * math.sqrt(S(x, y)))

def rho(x, y):
    return (F(x) + G(x, y) + F(y)) / a0f - 1.5

def rhox(x, y):
    return (Fp(x) + Gx(x, y)) / a0f

def rhoy(x, y):
    return (Fp(y) + Gy(x, y)) / a0f

assert abs(rho(1.0, 1.0)) < 1e-15
assert abs(rhox(1.0, 1.0) - 2.0 / 3.0) < 1e-15
assert abs(rhoy(1.0, 1.0) - 2.0 / 3.0) < 1e-15

# Regression only; theorem uses continuity, not this grid.
min_px = 10.0
min_py = 10.0
c = 3.0 / 5.0
min_margin = 10.0
for i in range(41):
    x = 1.0 + 0.01 * i / 40.0
    for j in range(41):
        y = 1.0 + 0.01 * j / 40.0
        min_px = min(min_px, rhox(x, y))
        min_py = min(min_py, rhoy(x, y))
        min_margin = min(min_margin, rho(x, y) - c * ((x - 1.0) + (y - 1.0)))
assert min_px > 0.64
assert min_py > 0.64
assert min_margin > -1e-14

# Low-t constants.
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
r = Delta2.sqrt()
C0 = Decimal(2) * r + Decimal('0.00042')
C146 = Decimal(4) / Decimal(9) * (pi + r)
t42 = C146 + Decimal('0.0013751')

def p_floor(t):
    return pi + C0 - Decimal(5) * t / Decimal(2)

p42 = p_floor(t42)
p18585 = p_floor(Decimal('1.8585'))
H42 = p42 / Decimal(9)
T42 = p42 / Decimal(13)
H18585 = p18585 / Decimal(9)
T18585 = p18585 / Decimal(13)
activation_coeff = Decimal(5) / Decimal(6)

assert Decimal('0.4944166723') < p42 < Decimal('0.4944166725')
assert Decimal('0.0549351858') < H42 < Decimal('0.0549351859')
assert Decimal('0.0380320517') < T42 < Decimal('0.0380320518')
assert Decimal('0.0444875852') < H18585 < Decimal('0.0444875853')
assert Decimal('0.0307990974') < T18585 < Decimal('0.0307990976')
assert activation_coeff == Decimal(5) / Decimal(6)

print('PASS low-t pentagon activation budget regression')
print(f'endpoint_gradient={rhox(1,1):.15f}')
print(f'sampled_min_partials={min_px:.15f},{min_py:.15f}')
print(f'sampled_c35_margin={min_margin:.15e}')
print('p42=', p42)
print('H42=', H42)
print('T42=', T42)
print('activation_coeff=', activation_coeff)
