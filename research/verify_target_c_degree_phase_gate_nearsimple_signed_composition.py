#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 100

S15 = Decimal('1.1543116921171727469')
outer_repetition_surplus = Decimal('0.0459365399110338116')
simple_outer = S15 - outer_repetition_surplus
half_cubic = S15 / Decimal(2)
edge_floor_if_low_cubic = Decimal('1.5') * S15

assert simple_outer > Decimal('1.1083751522')
assert half_cubic > Decimal('0.5771558460')
assert edge_floor_if_low_cubic > Decimal('1.7314675381')

print('S15/D >=', S15)
print('outer repetition surplus/D <=', outer_repetition_surplus)
print('simple-outer straight vertices/D >=', simple_outer)
print('half cubic split =', half_cubic)
print('all-extra edges if V3<S15/2 =', edge_floor_if_low_cubic)
print('PASS: near-simple signed degree/phase-gate composition constants')
