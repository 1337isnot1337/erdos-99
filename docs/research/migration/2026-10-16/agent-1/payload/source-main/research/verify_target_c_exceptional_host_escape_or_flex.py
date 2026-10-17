#!/usr/bin/env python3
"""Finite algebra and high-t rows for exceptional-host boundary-or-flex theorem."""
from fractions import Fraction as QF
from math import isqrt

# Finite identity regression: K=4F+q=2Eint+Eboundary implies
# Eint-2F=(q-Eboundary)/2 whenever the endpoint count is integral.
for F in range(1,30):
    for q in range(0,50):
        K=4*F+q
        for Ebd in range(K+1):
            if (K-Ebd)%2: continue
            Eint=(K-Ebd)//2
            lhs=QF(Eint-2*F)
            rhs=QF(q-Ebd,2)
            assert lhs==rhs

def atan_inv_bounds(q,n):
    s=QF(0)
    for k in range(n):
        term=QF(1,(2*k+1)*q**(2*k+1))
        s += term if k%2==0 else -term
    nxt=QF(1,(2*n+1)*q**(2*n+1))
    return (s,s+nxt) if n%2==0 else (s-nxt,s)

def sqrt_bounds(lo,hi,scale):
    a=isqrt((lo.numerator*scale*scale)//lo.denominator)
    b=isqrt((hi.numerator*scale*scale)//hi.denominator)
    return QF(a,scale),QF(b+1,scale)

a5l,a5h=atan_inv_bounds(5,90); a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**90
n3=isqrt(3*SCALE*SCALE); s3l,s3h=QF(n3,SCALE),QF(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l); sDl,sDh=sqrt_bounds(Dl,Dh,SCALE)
C707=2*sDl+QF(7707,1000000)

def row(T,p_claim,outer_claim,flex_claim):
    p=pil+C707-QF(5,2)*T
    outer=p/2
    flex=p/4
    assert p>p_claim and outer>outer_claim and flex>flex_claim
    print('T=',float(T),'Q/D>=P5/D>',float(p),'BO-trains/D>',float(outer),'flex/D>',float(flex))

row(QF(47,25), QF(3539,10000), QF(1769,10000), QF(884,10000))
row(QF(19,10), QF(3039,10000), QF(1519,10000), QF(759,10000))
row(QF(48,25), QF(2539,10000), QF(1269,10000), QF(634,10000))
row(QF(49,25), QF(1539,10000), QF(769,10000), QF(384,10000))
row(QF(2,1), QF(539,10000), QF(269,10000), QF(134,10000))
row(QF(201,100), QF(289,10000), QF(144,10000), QF(72,10000))
row(QF(101,50), QF(39,10000), QF(19,10000), QF(9,10000))
print('PASS exceptional-host boundary-or-flex theorem')
