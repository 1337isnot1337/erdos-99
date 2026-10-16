#!/usr/bin/env python3
"""Exact outward certificate for the modern all-train pentagon sea through T=1.8623.

Inputs:
 C=(T_train-q/2)/D >= C707:=2sqrt(Delta2)+0.007707,
 T_train-q=2f-k,
 t=(q-k)/D <= endpoint,
 b+Q=2(q-k), b>=per(F), per(F)/D->pi.
Thus
 f/D >= C707/2-t/4+o(1),
 Q/D <= 2t-pi+o(1),
 P5/D >= 2f/D-Q/D >= pi+C707-(5/2)t+o(1).
Each pentagon has five stopped-train terminal face-side occurrences, so at least
(5/2)P5 distinct all-stopped trains touch a pentagon.
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

a5l,a5h=atan_inv_bounds(5,90); a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
S=10**90
n3=isqrt(3*S*S); s3l,s3h=Q(n3,S),Q(n3+1,S)
Dl,Dh=pil/(2*s3h),pih/(2*s3l); sDl,sDh=sqrt_bounds(Dl,Dh,S)
g=Q(7707,1000000)
C707_lo=2*sDl+g

def cert(T, f_claim, p5_claim, frac_claim, train_claim, oler_claim):
    f0=C707_lo/2-T/4
    Q0=2*T-pil
    p50=2*f0-Q0
    frac0=2-Q0/f0
    ntrain0=Q(5,2)*p50
    oler0=Q(3,4)*s3l*f0
    assert f0>f_claim
    assert p50>p5_claim
    assert frac0>frac_claim
    assert ntrain0>train_claim
    assert oler0>oler_claim
    print('T=',float(T))
    print('  f/D >',float(f0),' Q/D <',float(Q0))
    print('  P5/D >',float(p50),' P5/f >',float(frac0))
    print('  all stopped trains touching pentagons/D >',float(ntrain0))
    print('  exceptional Oler/D >',float(oler0))

cert(Q(37,20),       Q(493,1000), Q(428,1000), Q(86,100), Q(107,100), Q(640,1000))
cert(Q(371,200),     Q(492,1000), Q(416,1000), Q(84,100), Q(104,100), Q(639,1000))
cert(Q(93,50),       Q(491,1000), Q(403,1000), Q(82,100), Q(100,100), Q(638,1000))
cert(Q(18623,10000), Q(490,1000), Q(398,1000), Q(81,100), Q(99,100),  Q(637,1000))
print('PASS')
