#!/usr/bin/env python3
"""Outward certificate for the high-t bounded-pentagon face floor.

Modern high-t inputs:
  tau/D >= rho + g, g=0.007707,
  tau=(q-k)+2f-2sqrt(R4),
  R4/D^2 -> Delta=pi/(2sqrt(3)),
  per(F)/D -> pi and b>=per(F),
  b+Q=2(q-k).
For t=(q-k)/D <= T this gives asymptotically
  f/D >= (rho+g-T+2sqrt(Delta))/2 =: f0,
  Q/D <= 2T-pi =: Q0.
If P5 is the number of bounded pentagonal contact faces, then
  Q >= P5+2(f-P5)=2f-P5,
so P5/D >= 2f0-Q0.
"""
from fractions import Fraction as Q
from math import factorial, isqrt


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

def cos_lower(x,n=24):
    # n even => last included k=n-1 odd, next omitted term positive; partial sum is lower.
    s=Q(0)
    for k in range(n):
        term=x**(2*k)/factorial(2*k)
        s += term if k%2==0 else -term
    return s

# Machin pi enclosure.
a5l,a5h=atan_inv_bounds(5,90)
a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
S=10**90
n3=isqrt(3*S*S)
s3l,s3h=Q(n3,S),Q(n3+1,S)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,S)

# rho=cos(rho).  A convenient certified lower bound.
rho0=Q(739085,1000000)
assert cos_lower(rho0)>rho0
g=Q(7707,1000000)

# a0=sqrt(3)/2, c0=sqrt(3)/4.  For the exceptional-face Oler payment
# A_exc-a0 Z_def >= a0 f+c0 Q >= (a0+c0)f = 3sqrt(3)f/4.
def cert(T, p5_claim, frac_claim, oler_claim):
    f0=(rho0+g-T+2*sDl)/2
    Q0=2*T-pil
    p50=2*f0-Q0
    frac0=2-Q0/f0
    oler0=Q(3,4)*s3l*f0
    assert f0>0 and Q0>0 and p50>p5_claim
    assert frac0>frac_claim
    assert oler0>oler_claim
    print('T=',float(T))
    print('  f/D    >',float(f0))
    print('  Q/D    <',float(Q0))
    print('  P5/D   >',float(p50),' claim',float(p5_claim))
    print('  P5/f   >',float(frac0),' claim',float(frac_claim))
    print('  exceptional Oler/D >',float(oler0),' claim',float(oler_claim))

cert(Q(37,20),  Q(243,1000), Q(60,100), Q(520,1000))
cert(Q(371,200), Q(228,1000), Q(57,100), Q(517,1000))
cert(Q(93,50),   Q(213,1000), Q(53,100), Q(514,1000))
print('PASS')
