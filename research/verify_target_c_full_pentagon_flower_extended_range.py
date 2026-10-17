#!/usr/bin/env python3
"""Exact outward certificate for the singleton/full-pentagon-flower dichotomy at wider t."""
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


def row(T, s_claim, sig_claim, mantel_claim, nfull_claim):
    p5=C707+pil-Q(5,2)*T
    s=p5/3
    sigma=2*(tau0-s)
    mantel=sigma*sDl/2+sigma*sigma/16
    nfull=Q(5,2)*s
    assert s>s_claim
    assert sigma>sig_claim
    assert mantel>mantel_claim
    assert nfull>nfull_claim
    print('T=',float(T))
    print('  P5/D lower =',float(p5))
    print('  common singleton/full-flower floor =',float(s),'margin',float(s-s_claim))
    print('  full-flower sigma_R/D lower =',float(sigma),'margin',float(sigma-sig_claim))
    print('  full-flower Mantel deficit/D^2 lower =',float(mantel),'margin',float(mantel-mantel_claim))
    print('  full-flower terminal trains/D lower =',float(nfull),'margin',float(nfull-nfull_claim))


row(Q(47,25), Q(1179,10000), Q(1257,1000), Q(697,1000), Q(2949,10000))
row(Q(19,10), Q(1013,10000), Q(1290,1000), Q(718,1000), Q(2532,10000))
row(Q(48,25), Q(846,10000), Q(1324,1000), Q(740,1000), Q(2116,10000))
row(Q(39,20), Q(596,10000), Q(1374,1000), Q(772,1000), Q(1491,10000))
row(Q(49,25), Q(513,10000), Q(1390,1000), Q(783,1000), Q(1282,10000))
row(Q(2), Q(179,10000), Q(1457,1000), Q(826,1000), Q(449,10000))
row(Q(101,50), Q(13,10000), Q(1490,1000), Q(848,1000), Q(32,10000))

root=(pil+C707)/Q(5,2)
assert root>Q(20215,10000)
print('positive common-floor threshold lower enclosure =',float(root))
print('PASS: singleton/full-flower dichotomy extends through t<=2.02')
