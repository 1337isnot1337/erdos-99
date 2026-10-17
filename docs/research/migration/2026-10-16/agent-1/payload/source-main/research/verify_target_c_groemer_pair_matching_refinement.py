#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2) * sqrt3)
f_star = Delta2.sqrt() - pi/Decimal(4) + Decimal('0.00021')
coeff = f_star / Decimal(9)
old_fixed = Decimal('0.000512254353148848304361279055340777291303204385097877698495996')
old_diag = Decimal('0.000256127176574424152180639527670388645651602192548938849247998')
assert coeff > Decimal('0.0185694')
assert coeff / old_fixed > Decimal(36)
assert coeff / old_diag > Decimal(72)
prev = Decimal('-1')
for K in [23, 42, 100, 1000, 10000]:
    ell = f_star - pi/Decimal(K-3)
    c = ell/Decimal(9)
    assert c > prev
    assert c < coeff
    prev = c
print('PASS Groemer pair-level matching refinement arithmetic')
print('Delta_2=', Delta2)
print('f_star=', f_star)
print('new_matching_coefficient=f_star/9=', coeff)
print('improvement_vs_old_fixed=', coeff/old_fixed)
print('improvement_vs_old_diagonal=', coeff/old_diag)
