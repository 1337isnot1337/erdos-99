#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s = Delta2.sqrt()
g = D('0.002123')
eps = D('0.0017327')
C146 = D(4) / D(9) * (pi + s)
t0 = C146 + eps
P = pi + D(2)*s + g - D('2.5')*t0
U = D(2)*pi + D(3)*s + D('1.5')*g - D(5)*t0
weak_count = U / D(2)
threshold = (D(2)*pi + D(3)*s + D('1.5')*g) / D(5)

assert D('1.82124623795') < t0 < D('1.82124623801')
assert D('0.4952256') < P < D('0.4952258')
assert D('0.0370769') < U < D('0.0370772')
assert D('0.0185384') < weak_count < D('0.0185387')
assert D('1.8286615') < threshold < D('1.8286618')

for u3, u4 in [(D(1),D(0)),(D(0),D(1)),(D(7),D(11)),(D(100),D(100))]:
    occurrences = u3 + D(2)*u4
    distinct_floor = occurrences / D(2)
    assert distinct_floor >= (u3+u4)/D(2)

eps_flat = pi / D(12)
assert (pi/D(3) - eps_flat) > 0

print('PASS loaded-flat-center weak-contact collapse g=0.002123 arithmetic')
print('s =', s)
print('t0 =', t0)
print('flat-center endpoint floor P =', P)
print('unloaded-center endpoint floor U =', U)
print('distinct weak-contact floor U/2 =', weak_count)
print('positive unloading window t <', threshold)
