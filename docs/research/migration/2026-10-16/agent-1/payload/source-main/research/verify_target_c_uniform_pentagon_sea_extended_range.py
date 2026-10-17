#!/usr/bin/env python3
"""Exact outward certificate for the uniform all-train pentagon sea at wider t endpoints."""
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


def row(T, p5_claim, n5_claim, i5_claim=None):
    f0=C707/2-T/4
    Q0=2*T-pil
    p50=2*f0-Q0
    n50=Q(5,2)*p50
    assert p50>p5_claim
    assert n50>n5_claim
    print('T=',float(T))
    print('  f/D lower =',float(f0))
    print('  Q/D upper =',float(Q0))
    print('  P5/D lower =',float(p50),'margin',float(p50-p5_claim))
    print('  N5/D lower =',float(n50),'margin',float(n50-n5_claim))
    if i5_claim is not None:
        i50=5*p50-tau0
        assert i50>i5_claim
        print('  Branch-R I5/D lower =',float(i50),'margin',float(i50-i5_claim))
        print('  Branch-R rhombic trains/D lower =',float(i50/2))
        print('  Branch-R touched pentagons/D lower =',float(i50/5))


row(Q(47,25), Q(3539,10000), Q(8848,10000), Q(10228,10000))
row(Q(19,10), Q(3039,10000), Q(7598,10000), Q(7728,10000))
row(Q(48,25), Q(2539,10000), Q(6348,10000), Q(5228,10000))
row(Q(39,20), Q(1789,10000), Q(4473,10000), Q(1478,10000))
row(Q(49,25), Q(1539,10000), Q(3848,10000), Q(228,10000))
row(Q(2), Q(539,10000), Q(1348,10000))
row(Q(101,50), Q(39,10000), Q(98,10000))

p5_root=(pil+C707)/Q(5,2)
i5_root=(pil+C707-tau0/5)/Q(5,2)
assert p5_root>Q(20215,10000)
assert i5_root>Q(19618,10000)
print('P5 positivity threshold lower enclosure =',float(p5_root))
print('Branch-R I5 positivity threshold lower enclosure =',float(i5_root))
print('PASS: uniform all-train pentagon consequences extend well beyond 1.8623')
