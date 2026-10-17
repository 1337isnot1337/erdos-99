#!/usr/bin/env python3
"""Finite arithmetic/combinatorial regression for the universal outer manifold."""
from decimal import Decimal, getcontext
from itertools import product
getcontext().prec=80
D=Decimal
PI=D('3.1415926535897932384626433832795028841971693993751058209749445923078164')
S=D('0.9523128068639573458338104262565569008230510550118582389446084732508783')
T21=D(4)/D(9)*(PI+S)+D('0.0017279')
coef=D('1.5')*PI-D(2)*T21
assert D('1.06990') < coef < D('1.06992')
# Raw dimension LOO+sum(r-2)_+ dominates b/2-f for all small endpoint distributions.
for f in range(0,6):
    for rs in product(range(0,8), repeat=f):
        lob=sum(rs)
        priv=sum(max(r-2,0) for r in rs)
        for loo in range(0,8):
            b=2*loo+lob
            dman=loo+priv
            assert D(dman) >= D(b)/2-D(f)
# Eliminate f using f<=Q and b+Q=2(q-k).
for b in range(0,24):
    for Q in range(0,24):
        if (b+Q)%2:
            continue
        qmk=(b+Q)//2
        for f in range(Q+1):
            assert D(b)/2-D(f)-1 >= D(3)*D(b)/2-D(2*qmk)-1
print('PASS universal outer-supported finite-manifold regression')
print('t21=',T21)
print('zero-detour normalized non-Euclidean floor=',coef)
