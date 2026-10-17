#!/usr/bin/env python3
"""Arithmetic row checks for the full-flower escape-or-flex research candidate.

Preserved from research/c2-flower-high-t-sol-20260915 at exact tip
7de4cdc3e9aa0cac5b278c2ccc17158bd8d66bdb. This checks the rational numeric
rows only; it does not certify the geometric/rank statement in the report.

If F is the number of fully rhombic pentagons, Eesc is the number of complete
non-singleton trains with exactly one terminal face in the flower set, and Eint has
both terminal faces in the set, then 5F=2Eint+Eesc. The internal-train columns of the
face-closure matrix have support only on the 2F flower rows, so their train-rate kernel
has dimension at least Eint-2F=(F-Eesc)/2. Modulo global rotation this leaves at least
(F-Eesc)/2-1 non-Euclidean contact-flex dimensions.

At threshold Eesc=F/2, either Eesc>=F/2 or non-Euclidean flex dimension >=F/4-1.
This script combines that exact structural statement with the certified high-t flower
floors from verify_target_c_singleton_full_flower_extended_range.py.
"""
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

def row(T, flower_claim, esc_claim, flex_claim):
    p5=pil+C707-Q(5,2)*T
    flower=p5/3
    esc=flower/2
    flex=flower/4
    assert flower>flower_claim
    assert esc>esc_claim
    assert flex>flex_claim
    print('T=',float(T),'F/D>',float(flower),'escape/D>',float(esc),'flex/D asymptotic>',float(flex))

row(Q(47,25), Q(1179,10000), Q(589,10000), Q(294,10000))
row(Q(19,10), Q(1013,10000), Q(506,10000), Q(253,10000))
row(Q(48,25), Q(846,10000), Q(423,10000), Q(211,10000))
row(Q(49,25), Q(513,10000), Q(256,10000), Q(128,10000))
row(Q(2,1), Q(179,10000), Q(89,10000), Q(44,10000))
row(Q(201,100), Q(96,10000), Q(48,10000), Q(24,10000))
row(Q(101,50), Q(13,10000), Q(6,10000), Q(3,10000))
print('PASS full-flower escape-or-flex rows')
