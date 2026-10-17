#!/usr/bin/env python3
"""Exact arithmetic for the degree-5/6 residual near-contact matching extension."""
from fractions import Fraction as Q
from math import isqrt


def atan_inv_bounds(q,n):
    s=Q(0)
    for k in range(n):
        term=Q(1,(2*k+1)*q**(2*k+1))
        s += term if k%2==0 else -term
    nxt=Q(1,(2*n+1)*q**(2*n+1))
    return (s,s+nxt) if n%2==0 else (s-nxt,s)


def sqrt_bounds(lo,hi,scale):
    a=isqrt((lo.numerator*scale*scale)//lo.denominator)
    b=isqrt((hi.numerator*scale*scale)//hi.denominator)
    return Q(a,scale),Q(b+1,scale)


a5l,a5h=atan_inv_bounds(5,90)
a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**100
n3=isqrt(3*SCALE*SCALE)
s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,_=sqrt_bounds(Dl,Dh,SCALE)
C707=2*sDl+Q(7707,1000000)


def f56_floor(T):
    return (Q(3)*C707/Q(2)+pil-Q(11)*T/Q(4))/Q(2)

threshold=(Q(6)*C707+Q(4)*pil)/Q(11)
assert threshold>Q(21854,10000)

rows=[
    (Q(2,1),        Q(283,10000)),
    (Q(41,20),      Q(206,10000)),
    (Q(21,10),      Q(130,10000)),
    (Q(43,20),      Q(53,10000)),
    (Q(109,50),     Q(8,10000)),
    (Q(10927,5000), Q(1,100000)),
]
for T,claim in rows:
    F=f56_floor(T)
    M=F/Q(9)
    assert F>0
    assert M>claim,(T,float(F),float(M),float(claim))
    print('T=',float(T),'F56/D >',float(F),'matching/D >',float(M),'claim',float(claim))

print('F<=6 positivity threshold >',float(threshold))
print('PASS low-degree residual near-contact extension')
