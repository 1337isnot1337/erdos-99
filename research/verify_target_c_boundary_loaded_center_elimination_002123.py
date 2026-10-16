#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
sqrt3 = D(3).sqrt()
s = (pi/(D(2)*sqrt3)).sqrt()
g = D('0.002123')
C146 = D(4)/D(9)*(pi+s)
t23 = C146 + D('0.0017327')
B = D(6)*pi + D(7)*s + D(7)*g/D(2) - D(14)*t23
tcrit = (D(6)*pi + D(7)*s + D(7)*g/D(2))/D(14)

assert D('0.0257286') < B < D('0.0257289')
assert D('0.0128642') < B/D(2) < D('0.0128645')
assert D('1.8230839') < tcrit < D('1.8230841')

C_g = D(2)*s + g
boundary = D(5)*pi + D(3)*C_g - D(23)*t23/D(2)
loaded_cap = D(5)*t23/D(2) - pi - s - g/D(2)
assert abs((boundary-loaded_cap)-B) < D('1e-70')

U = D(2)*pi + D(3)*s + D(3)*g/D(2) - D(5)*t23
weak = U/D(2)
assert D('0.0185384') < weak < D('0.0185387')

print('PASS boundary loaded-center elimination g=0.002123 arithmetic')
print('s =', s)
print('t23 =', t23)
print('N2+E_in endpoint floor =', B)
print('max(N2,E_in) endpoint floor =', B/D(2))
print('pure-burden positivity window t <', tcrit)
print('simultaneous weak-contact floor =', weak)
