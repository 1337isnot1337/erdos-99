#!/usr/bin/env python3
"""Exact outward certificate extending singleton/full-flower dichotomy to t<=2.02."""
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
SCALE=10**90
n3=isqrt(3*SCALE*SCALE)
s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,SCALE)
C707=2*sDl+Q(7707,1000000)
tau0=Q(7467921,10000000)

def cert(T, s_claim, sigma_claim, mantel_claim, n_claim):
    p5=pil+C707-Q(5,2)*T
    s=p5/3
    sigma=2*(tau0-s)
    mantel=sigma*sDl/2+sigma*sigma/16
    nfull=Q(5,2)*s
    assert p5>0
    assert s>s_claim
    assert sigma>sigma_claim
    assert mantel>mantel_claim
    assert nfull>n_claim
    print('T =',float(T))
    print('  P5/D >',float(p5))
    print('  max(S,Ffull)/D >',float(s))
    print('  Ffull branch sigma_R/D >',float(sigma))
    print('  Ffull branch Mantel deficit/D^2 >',float(mantel))
    print('  Ffull-terminal trains/D >',float(nfull))

cert(Q(47,25), Q(1179,10000), Q(1257,1000), Q(697,1000), Q(2949,10000))
cert(Q(19,10), Q(1013,10000), Q(1290,1000), Q(718,1000), Q(2532,10000))
cert(Q(48,25), Q(846,10000), Q(1324,1000), Q(740,1000), Q(2116,10000))
cert(Q(49,25), Q(513,10000), Q(1390,1000), Q(783,1000), Q(1282,10000))
cert(Q(2,1),   Q(179,10000), Q(1457,1000), Q(826,1000), Q(449,10000))
cert(Q(201,100), Q(96,10000), Q(1474,1000), Q(837,1000), Q(241,10000))
cert(Q(101,50), Q(13,10000), Q(1490,1000), Q(848,1000), Q(327,100000))

threshold=Q(2,5)*(pil+C707)
assert threshold>Q(20215,10000)
print('pentagon/flower positivity threshold >',float(threshold))
print('PASS singleton/full-flower extension through t<=2.02')
