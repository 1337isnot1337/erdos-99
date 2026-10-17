#!/usr/bin/env python3
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

a5l,a5h=atan_inv_bounds(5,90); a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**90
n3=isqrt(3*SCALE*SCALE); s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,SCALE)
C707=2*sDl+Q(7707,1000000)

def row(T,p_claim,e_claim,f_claim):
    p=pil+C707-Q(5,2)*T
    esc=p/2
    flex=p/4
    assert p>p_claim and esc>e_claim and flex>f_claim
    print('T=',float(T),'P5/D>',float(p),'escape/D>',float(esc),'flex/D asymptotic>',float(flex))

row(Q(47,25), Q(3539,10000), Q(1769,10000), Q(884,10000))
row(Q(19,10), Q(3039,10000), Q(1519,10000), Q(759,10000))
row(Q(48,25), Q(2539,10000), Q(1269,10000), Q(634,10000))
row(Q(49,25), Q(1539,10000), Q(769,10000), Q(384,10000))
row(Q(2,1), Q(539,10000), Q(269,10000), Q(134,10000))
row(Q(201,100), Q(289,10000), Q(144,10000), Q(72,10000))
row(Q(101,50), Q(39,10000), Q(19,10000), Q(9,10000))
print('PASS pentagon-sea escape-or-flex rows')
