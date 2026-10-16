#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
PI=D('3.141592653589793238462643383279502884197169399375105820974944')
S=D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
GAP=D('0.0021'); EPS=D('0.0017279')
CG=2*S+GAP
T0=D(4)/D(9)*(PI+S)+EPS
Q0=2*T0-PI
R0=7*PI+3*CG-D('13.5')*T0
F0=(R0-2*Q0)/2
ETA=D('0.005')
assert D('1.8212414379') < T0 < D('1.8212414380')
assert D('0.5008901') < Q0 < D('0.5008903')
assert D('3.1245659') < R0 < D('3.1245661')
assert D('1.0613926') < F0 < D('1.0613930')
assert D('1.0563926') < F0-ETA < D('1.0563930')
assert D('0.4908901') < Q0-2*ETA < D('0.4908903')
assert D('0.2454450') < Q0/2-ETA < D('0.2454452')
print('PASS weighted outer-flex near-equality arithmetic')
print('g=',GAP)
print('t21=',T0)
print('Q/D endpoint=',Q0)
print('weighted outer endpoint R=',R0)
print('sharp localized-flex floor=',F0)
print('example eta=',ETA)
print('near-branch L_OO floor=',F0-ETA)
print('near-branch exact-two-face floor=',Q0-2*ETA)
print('near-branch coherent-hinge floor=',Q0/2-ETA)
