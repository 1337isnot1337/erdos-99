#!/usr/bin/env python3
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944')
SQ = D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
C0 = 2 * SQ + D('0.00042')
t42 = D(4) / D(9) * (PI + SQ) + D('0.0013751')

def x_upper(t):
    return D(9) * t / D(4) - PI - C0 / D(2)

def weighted_floor(t):
    return PI - 6 * x_upper(t)

assert D('0.00288397499999') < x_upper(t42) < D('0.00288397500001')
assert D('1.04142') < weighted_floor(t42) / 3 < D('1.04144')
assert D('0.87217') < weighted_floor(D('1.8585')) / 3 < D('0.87219')
assert PI / 3 > D('1.04719')

print('PASS outer/flat-pentagon train gate arithmetic')
print('t42=', t42)
print('X_upper_at_t42=', x_upper(t42))
print('weighted_floor_at_t42=', weighted_floor(t42))
print('max_floor_at_t42=', weighted_floor(t42) / 3)
print('max_floor_at_1.8585=', weighted_floor(D('1.8585')) / 3)
print('low_X_limit_pi_over_3=', PI / 3)
