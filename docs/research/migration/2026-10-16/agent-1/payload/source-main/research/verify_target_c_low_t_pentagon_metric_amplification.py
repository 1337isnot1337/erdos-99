#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
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
coarse = r - pi / Decimal(4) + Decimal('0.00021')

assert Decimal('0.4944166723') < p42 < Decimal('0.4944166725')
assert Decimal('0.4003882672') < p18585 < Decimal('0.4003882674')
assert p42 / coarse > Decimal('2.95')

vals = {
    'p42': p42,
    'V_flat_42': p42 / Decimal(5),
    'C_flat_42': p42 / Decimal(13),
    'H_eta_42': p42 / Decimal(9),
    'p18585': p18585,
    'V_flat_18585': p18585 / Decimal(5),
    'C_flat_18585': p18585 / Decimal(13),
    'H_eta_18585': p18585 / Decimal(9),
    'gain_over_coarse': p42 / coarse,
}

assert vals['V_flat_42'] > Decimal('0.0988833344')
assert vals['C_flat_42'] > Decimal('0.0380320517')
assert vals['H_eta_42'] > Decimal('0.0549351858')
assert vals['V_flat_18585'] > Decimal('0.0800776534')
assert vals['C_flat_18585'] > Decimal('0.0307990974')
assert vals['H_eta_18585'] > Decimal('0.0444875852')

print('PASS low-t pentagon metric amplification arithmetic')
for key, value in vals.items():
    print(f'{key}={value}')
