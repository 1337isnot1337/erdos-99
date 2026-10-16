#!/usr/bin/env python3
"""Exact constant check for the common-transverse ladder at t<=1.8623."""

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


S=10**100
a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pi_lo,pi_hi=16*a5l-4*a239h,16*a5h-4*a239l
n3=isqrt(3*S*S)
s3l,s3h=Q(n3,S),Q(n3+1,S)
Delta_lo,Delta_hi=pi_lo/(2*s3h),pi_hi/(2*s3l)
sDelta_lo,_=sqrt_bounds(Delta_lo,Delta_hi,S)
C76_lo=2*sDelta_lo+Q(19,2500)

T=Q(18623,10000)
U0_hi=Q(9,2)*T-2*pi_lo
delta_max_hi=(U0_hi-C76_lo)/2
A0=Q(5857,10000)

# Every adaptively selected boundary O-O train has e_tau<=A0-delta.
# Audited train-length/terminal-energy tradeoff:
#   r_tau/D >= 1-delta-e_tau/2-o(1),
# where r_tau is the number of strict rhombi traversed by tau.
length_floor=1-A0/2-delta_max_hi/2

assert delta_max_hi<Q(93,1000)
assert length_floor>Q(6608,10000)

print('PASS: common transverse ladder through t<=1.8623')
for k,v in [
    ('delta max',delta_max_hi),
    ('rhombi/crossing-neighbor floor',length_floor),
    ('margin over .6608',length_floor-Q(6608,10000)),
]:
    print(k,'=',float(v))
