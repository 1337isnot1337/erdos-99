#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
PI=D('3.141592653589793238462643383279502884197169399375105820974944')
SQ=D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
fstar=SQ-PI/4+D('0.00021')
assert fstar > D('0.16712464346650')
assert fstar < D('0.16712464346652')
print('PASS global pentagon two-window escape arithmetic')
print('f_star=',fstar)
print('unweighted_threshold=f_star/3=',fstar/D(3))
print('off_window_floor_if_degree_excess_sublinear=f_star/2=',fstar/D(2))
