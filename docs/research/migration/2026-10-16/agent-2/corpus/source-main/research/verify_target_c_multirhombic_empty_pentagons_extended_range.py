#!/usr/bin/env python3
"""Exact outward certificate for the extended multi-rhombic pentagon thresholds."""
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


a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
S=10**100
n3=isqrt(3*S*S)
s3l,s3h=Q(n3,S),Q(n3+1,S)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,S)
C707=2*sDl+Q(7707,1000000)
tau0=Q(7467921,10000000)


def values(T):
    f=C707/2-T/4
    q=2*T-pil
    p5=2*f-q
    i5=5*p5-tau0
    x2=(i5-q)/4
    x3=(i5-2*q)/3
    return f,q,p5,i5,x2,x3

for T,c2,c3 in [
    (Q(373,200), Q(1518,10000), Q(111,10000)), # 1.865
    (Q(188,100), Q(1011,10000), Q(-1,1)),       # 1.880, X3 not claimed
    (Q(19,10), Q(286,10000), Q(-1,1)),          # 1.900
    (Q(381,200), Q(104,10000), Q(-1,1)),        # 1.905
    (Q(1907,1000), Q(32,10000), Q(-1,1)),       # 1.907
]:
    f,q,p5,i5,x2,x3=values(T)
    assert x2>c2
    if c3>=0:
        assert x3>c3
    print('T=',float(T),'X2=',float(x2),'X3=',float(x3))

x2_root=(5*C707+6*pil-tau0)/Q(29,2)
x3_root=(5*C707+7*pil-tau0)/Q(33,2)
assert x2_root>Q(19078,10000)
assert x3_root>Q(18670,10000)
print('X2 positivity threshold lower enclosure =',float(x2_root))
print('X3 positivity threshold lower enclosure =',float(x3_root))
print('PASS')
