#!/usr/bin/env python3
"""Outward Decimal regression for the double-unit / flat-center overlap theorem."""
from decimal import Decimal as D, getcontext
getcontext().prec = 80
pi = D('3.14159265358979323846264338327950288419716939937510')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2)*sqrt3)
s = Delta2.sqrt()
g = D('0.0021')
C21 = D(2)*s + g
C146 = D(4)/D(9)*(pi+s)
t21 = C146 + D('0.0017279')

def burden(t):
    return D(5)*pi + D(3)*C21 - D(23)*t/D(2)

xmax = D(9)*t21/D(4) - pi - C21/D(2)
R21 = D('4.5')*t21 - D(2)*pi - C21
delta21 = R21/D(2)
H21 = burden(t21)
Hbar = burden(D('1.8585'))
tcrit = (D(5)*pi + D(3)*C21)/(D(23)/D(2))
assert D('0.0028377749999999999999999') < xmax < D('0.0028377750000000000000001')
assert D('0.0056755499999999999999998') < R21 < D('0.0056755500000000000000002')
assert D('0.0028377749999999999999999') < delta21 < D('0.0028377750000000000000001')
assert D('0.48386357') < H21 < D('0.48386358')
assert D('0.16128785') < H21/D(3) < D('0.16128787')
assert D('0.05539010') < Hbar < D('0.05539012')
assert D('0.01846336') < Hbar/D(3) < D('0.01846338')
assert D('1.8633165') < tcrit < D('1.8633166')
eta = D('0.06')
Hpen = H21 + (D(2)-D(1)/eta)*delta21
assert D('0.44224287') < Hpen < D('0.44224288')
assert D('0.07370714') < Hpen/D(6) < D('0.07370715')
# Algebraic coefficient check after replacing x by its low-t upper bound.
t,d,k = D('1.83'),D('0.004'),D('0.002')
xub = D(9)*t/D(4)-pi-C21/D(2)-d-k/D(4)
lhs = D(2)*t+D(2)*k-pi-D(4)*d-D(6)*xub
rhs = D(5)*pi+D(3)*C21-D(23)*t/D(2)+D(2)*d+D(7)*k/D(2)
assert abs(lhs-rhs) < D('1e-70')
print('PASS double-unit / flat-center overlap constants')
print('C21=', C21)
print('t21=', t21)
print('xmax(t21)=', xmax)
print('delta21=', delta21)
print('endpoint burden=', H21)
print('endpoint three-way max floor=', H21/D(3))
print('t=1.8585 burden=', Hbar)
print('positive until t<', tcrit)
print('eta=.06 contact-converted burden=', Hpen)
print('eta=.06 weighted max floor=', Hpen/D(6))
