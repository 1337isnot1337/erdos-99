#!/usr/bin/env python3
from decimal import Decimal, getcontext
import math

getcontext().prec = 60
rho = Decimal('0.73908513321516064165531208767387340401341175890076')
pi = Decimal('3.14159265358979323846264338327950288419716939937510')
sqrt3 = Decimal(3).sqrt()
delta2 = pi / (2 * sqrt3)
s2 = delta2.sqrt()
a0 = sqrt3 / 2
c0 = sqrt3 / 4
eta = Decimal('0.00042')

j = 2*rho + 4*s2 - pi + 2*eta
h = 3*j/5
pop = pi/2 + 3*j/10
beta = c0*h
ch_slack = 4*j/5
rh_def = 3*j/10

assert Decimal('2.1466687') < j < Decimal('2.1466690')
assert Decimal('1.2880012') < h < Decimal('1.2880014')
assert Decimal('2.2147968') < pop < Decimal('2.2147971')
assert Decimal('0.5577208') < beta < Decimal('0.5577211')
assert Decimal('1.7173349') < ch_slack < Decimal('1.7173352')
assert Decimal('0.6440005') < rh_def < Decimal('0.6440008')
assert abs(beta - a0*rh_def) < Decimal('1e-50')
assert abs(Decimal(str(math.cos(float(rho)))) - rho) < Decimal('1e-15')

# Exact algebraic coefficients used in the proof.
# H >= 3J/5 follows from 5H-3J = 2(d+Q-f) >= 0.
for d in range(0, 20):
    for f in range(0, 20):
        for extra in range(0, 20):
            Q = f + extra
            J = Decimal(d + 4*f + Q)
            H = Decimal(d + 2*f + Q)
            assert 5*H >= 3*J

# P_out - (b-P_F) = 2(P_F-q+a) >= 0 when P_F>=q, a>=0.
for q in range(0, 20):
    for extra_p in range(0, 10):
        P = q + extra_p
        for a in range(0, 10):
            assert 2*Decimal(P-q+a) >= 0

print('j_* =', j)
print('h_* =', h)
print('population coefficient =', pop)
print('chamber surplus coefficient =', beta)
print('chamber Oler-slack coefficient =', ch_slack)
print('absolute rhombus deficit coefficient =', rh_def)
print('correlated interface/population consequences: PASS')
