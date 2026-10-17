#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 80
D = Decimal
pi = D('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
sqrt3 = D(3).sqrt()
Delta2 = pi / (D(2) * sqrt3)
s = Delta2.sqrt()
g = D('0.0021')
eps = D('0.0017279')
C146 = D(4) / D(9) * (pi + s)
t0 = C146 + eps
P = pi + D(2)*s + g - D('2.5')*t0
U = D(2)*pi + D(3)*s + D('1.5')*g - D(5)*t0
threshold = (D(2)*pi + D(3)*s + D('1.5')*g) / D(5)
weak = U / D(4)
hidden_distinct = D(3)*U / D(4)
hidden_endpoint_disjoint = U / D(9)

assert D('1.82124143795') < t0 < D('1.82124143800')
assert D('0.4952146') < P < D('0.4952148')
assert D('0.0370664') < U < D('0.0370667')
assert D('1.8286546') < threshold < D('1.8286549')
assert D('0.0092665') < weak < D('0.0092668')
assert D('0.0277997') < hidden_distinct < D('0.0278001')
assert D('0.0041184') < hidden_endpoint_disjoint < D('0.0041187')

# Coefficient identities used in the theorem, allowing Decimal sqrt roundoff.
assert abs(P - (pi + D(2)*s + g - D(5)*t0/D(2))) < D('1e-70')
# S <= 5t-2pi-2delta-2s-g, and 2L<=S, so at delta=kappa=0:
L_cap = (D(5)*t0 - D(2)*pi - D(2)*s - g) / D(2)
assert abs(U - (P - L_cap)) < D('1e-70')
assert hidden_distinct == D(3) * weak

print('PASS loaded-flat-center unloading g=0.0021 arithmetic')
print('s =', s)
print('t0 =', t0)
print('flat-center endpoint floor P =', P)
print('unloaded-center endpoint floor U =', U)
print('positive unloading window t <', threshold)
print('weak-contact branch U/4 =', weak)
print('distinct-hidden-pair branch 3U/4 =', hidden_distinct)
print('endpoint-disjoint hidden-pair fallback U/9 =', hidden_endpoint_disjoint)
