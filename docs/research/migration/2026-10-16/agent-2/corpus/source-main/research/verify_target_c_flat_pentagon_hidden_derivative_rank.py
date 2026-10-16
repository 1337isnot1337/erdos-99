#!/usr/bin/env python3
"""Arithmetic/combinatorial regression for flat-pentagon hidden-derivative rank."""
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
PI = D('3.141592653589793238462643383279502884197169399375105820974944592307816406')
SQRT3 = D(3).sqrt()
A = SQRT3 / D(2)
# Equality-model 4x4 minor is a^3.
minor = A ** 3
assert abs(minor - D(3) * SQRT3 / D(8)) < D('1e-70')
assert minor > D('0.64')

# Component combinatorics: n-1 = 5s-e-1 with e bounded by simplicity and degree 5.
for s in range(1, 1001):
    emax = min(s * (s - 1) // 2, (5 * s) // 2)
    rank = 5 * s - emax - 1
    assert D(rank) >= D(7) * D(s) / D(3)

DELTA2 = PI / (D(2) * SQRT3)
R = DELTA2.sqrt()
C0 = D(2) * R + D('0.00042')
T42 = D(4) / D(9) * (PI + R) + D('0.0013751')

def P(t):
    return PI + C0 - D(5) * t / D(2)

def Qcap(t):
    return D(2) * t - PI

def RH(t):
    direct = D(7) * P(t) / D(3) - D(2) * Qcap(t)
    expanded = D(13) * PI / D(3) + D(7) * C0 / D(3) - D(59) * t / D(6)
    assert abs(direct - expanded) < D('1e-70')
    return direct

floor = RH(T42)
root = (D(26) * PI + D(14) * C0) / D(59)
assert D('0.15326') < floor < D('0.15328')
assert D('1.836') < root < D('1.837')
assert RH(D('1.83')) > 0
assert RH(D('1.84')) < 0
print('PASS flat-pentagon hidden-derivative rank regression')
print('local_minor=', minor)
print('Delta2=', DELTA2)
print('C0=', C0)
print('t42=', T42)
print('pentagon_floor_at_t42=', P(T42))
print('Q_cap_at_t42=', Qcap(T42))
print('hidden_rank_floor_at_t42=', floor)
print('positive_rank_until_t=', root)
