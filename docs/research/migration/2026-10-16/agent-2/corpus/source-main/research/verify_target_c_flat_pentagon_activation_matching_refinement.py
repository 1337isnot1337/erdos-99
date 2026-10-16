#!/usr/bin/env python3
"""Arithmetic and finite conflict-count regression for the activation matching refinement."""
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
r = Delta2.sqrt()
C0 = D(2) * r + D('0.00042')
C146 = D(4) * (pi + r) / D(9)
t42 = C146 + D('0.0013751')


def A(t):
    return pi + C0 - D(5) * t / D(2)


a42 = A(t42)
a18585 = A(D('1.8585'))

# Sector arithmetic for the new conflict denominators.
# Hidden chord: center incidence <=2, shoulder incidence <=3.
chord_conflict_degree = (2 - 1) + (3 - 1)
assert chord_conflict_degree == 3
assert chord_conflict_degree + 1 == 4

# Tooth/flat-chain: center contributes <=3 conflicts; the other two vertices <=4 each.
tooth_conflict_degree = 3 + 4 + 4
assert tooth_conflict_degree == 11
assert tooth_conflict_degree + 1 == 12

h42 = a42 / D(4)
t42_floor = a42 / D(12)
h18585 = a18585 / D(4)
t18585_floor = a18585 / D(12)

assert D('0.4944166723') < a42 < D('0.4944166725')
assert D('0.1236041680') < h42 < D('0.1236041682')
assert D('0.0412013893') < t42_floor < D('0.0412013895')
assert D('0.1000970667') < h18585 < D('0.1000970670')
assert D('0.0333656888') < t18585_floor < D('0.0333656891')

# Safe c=3/5 activation budget and median-gap coefficient.
c = D(3) / D(5)
activation_coeff = D(1) / (D(2) * c)
assert activation_coeff == D(5) / D(6)
median_coeff_42 = D(20) / (D(3) * a42)
assert D('13.48') < median_coeff_42 < D('13.49')
median_count_42 = a42 / D(8)
assert D('0.0618020') < median_count_42 < D('0.0618022')

print('PASS flat-pentagon activation matching refinement')
print('A(t42)=', a42)
print('H_act/D at t42 >=', h42)
print('T_act/D and C_flat/D at t42 >=', t42_floor)
print('H_act/D at 1.8585 >=', h18585)
print('T_act/D and C_flat/D at 1.8585 >=', t18585_floor)
print('c=3/5 total-gap coefficient =', activation_coeff)
print('t42 median-gap coefficient <', median_coeff_42)
