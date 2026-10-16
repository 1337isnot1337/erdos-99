#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816')
sqrt3 = Decimal(3).sqrt()
Delta2 = pi / (Decimal(2)*sqrt3)
f_star = Delta2.sqrt() - pi/Decimal(4) + Decimal('0.00021')
new = f_star/Decimal(13)
old_fixed = Decimal('0.000512254353148848304361279055340777291303204385097877698495996')
old_diag = Decimal('0.000256127176574424152180639527670388645651602192548938849247998')
assert new > Decimal('0.0128557')
assert new/old_fixed > Decimal(25)
assert new/old_diag > Decimal(50)
prev = Decimal('-1')
for K in [23,42,100,1000,10000]:
    ell = f_star - pi/Decimal(K-3)
    c = ell/Decimal(13)
    assert c > prev
    assert c < new
    prev = c
print('PASS anchored Groemer triple matching refinement arithmetic')
print('Delta_2=', Delta2)
print('f_star=', f_star)
print('triple_matching_coefficient=f_star/13=', new)
print('improvement_vs_old_fixed=', new/old_fixed)
print('improvement_vs_old_diagonal=', new/old_diag)
