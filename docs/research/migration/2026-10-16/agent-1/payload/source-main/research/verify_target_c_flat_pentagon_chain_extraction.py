#!/usr/bin/env python3
from decimal import Decimal, getcontext
getcontext().prec=70
D=Decimal
PI=D('3.141592653589793238462643383279502884197169399375105820974944')
SQ=D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
f=SQ-PI/4+D('0.00021')
assert f>D('0.16712464346650') and f<D('0.16712464346652')
print('PASS flat-pentagon chain extraction arithmetic')
print('f_star=',f)
print('distinct_flat_center_floor_if_X_sublinear=f_star/5=',f/D(5))
print('vertex_disjoint_chain_floor_if_X_sublinear=f_star/13=',f/D(13))
print('unweighted_center_tradeoff_threshold=f_star/6=',f/D(6))
print('unweighted_chain_tradeoff_threshold=f_star/14=',f/D(14))
# Incidence constants: one source vertex is on at most five bounded contact-face sectors.
MAX_FACE_OCC_AT_VERTEX=5
CENTER_MULT=MAX_FACE_OCC_AT_VERTEX
PATH_CONFLICT=3*(MAX_FACE_OCC_AT_VERTEX-1)
assert CENTER_MULT==5
assert PATH_CONFLICT==12
assert PATH_CONFLICT+1==13
