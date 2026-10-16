#!/usr/bin/env python3
"""Arithmetic regression for q-k amplified bridge-subtracted train split.

Checks constants and exact scalar identities only. It does not prove the geometric
AG42, Section-171, or bridge-isoperimetric inputs.
"""
from decimal import Decimal, getcontext
getcontext().prec = 70
PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164')
SQRT3 = Decimal(3).sqrt()
DELTA = PI/(Decimal(2)*SQRT3)
S = DELTA.sqrt()
T_STAR = Decimal(4)*(PI+S)/Decimal(9) + Decimal('0.0013751')
L = T_STAR + Decimal('0.00084')
THREE = L/Decimal(3)
SE = L/Decimal(6)
M3 = THREE*(Decimal(4)*S+THREE/Decimal(2))/Decimal(8)
HALF = L/Decimal(2)
M2 = HALF*(Decimal(4)*S+HALF/Decimal(2))/Decimal(8)
OLD = Decimal('1.47901026643032128331062417534774680802682351780152')

assert L > OLD
assert abs(L-(T_STAR+Decimal('0.00084'))) < Decimal('1e-60')
assert abs(Decimal(2)*SE-THREE) < Decimal('1e-60')
assert abs(Decimal(2)*HALF-L) < Decimal('1e-60')

print('PASS q-k amplified bridge-subtracted train split')
for name,value in [
    ('Delta_2',DELTA),('sqrt_Delta_2',S),('t_star',T_STAR),
    ('old_bridge_currency',OLD),('new_bridge_currency',L),
    ('three_way_threshold',THREE),('S_E_threshold',SE),
    ('Mantel_three_way_branch',M3),('two_block_threshold',HALF),
    ('Mantel_two_block_branch',M2),
]: print(f'{name}={value}')
