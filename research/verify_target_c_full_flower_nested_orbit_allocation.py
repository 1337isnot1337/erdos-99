#!/usr/bin/env python3
"""Finite arithmetic regression for the four-near-orbit pentagon lemma.

The proof is analytic. This script exhausts sums of four exact six-ray triangular
unit vectors and checks the norm spectrum and the unit-sum closure claim used in the
nested-window argument.
"""
from itertools import product
from fractions import Fraction as Q

# Represent m*a+n*b by integer pair (m,n), |.|^2=m^2+mn+n^2.
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]

def add(xs):
    xs=list(xs)
    return sum(x for x,_ in xs),sum(y for _,y in xs)
def norm2(v):
    m,n=v
    return m*m+m*n+n*n

spectrum=set()
unit_sums=0
for idx in product(range(6), repeat=4):
    s=add(rays[i] for i in idx)
    q=norm2(s)
    spectrum.add(q)
    if q==1:
        unit_sums+=1
        assert (-s[0],-s[1]) in rays
    else:
        assert q==0 or q>=3
        assert q%3 in (0,1)

assert 2 not in spectrum
assert min(q for q in spectrum if q not in (0,1))>=3
assert unit_sums==360

# Safe rho=1/10 inequalities used in the note.
rho=Q(1,10)
assert 4*rho<Q(7,10)  # and sqrt(3)-1 > 7/10 since sqrt(3)>17/10
assert Q(17,10)**2<3
assert 4*rho<1

print('PASS full-flower nested-orbit allocation regression')
print('four-ray norm^2 spectrum =',sorted(spectrum))
print('unit four-ray sums =',unit_sums)
