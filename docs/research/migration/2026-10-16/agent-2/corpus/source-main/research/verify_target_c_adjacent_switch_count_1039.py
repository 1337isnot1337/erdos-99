#!/usr/bin/env python3
"""Exact certificate: t<=1.844 retained-mass/defect ledger forces N<1039+o(1)."""
from fractions import Fraction as Q
from math import factorial,isqrt

def atan_inv_bounds(q,n):
    s=Q(0)
    for k in range(n):
        term=Q(1,(2*k+1)*q**(2*k+1))
        s += term if k%2==0 else -term
    nxt=Q(1,(2*n+1)*q**(2*n+1))
    return (s,s+nxt) if n%2==0 else (s-nxt,s)

def sqrt_bounds(lo,hi,S):
    a=isqrt((lo.numerator*S*S)//lo.denominator)
    b=isqrt((hi.numerator*S*S)//hi.denominator)+1
    return Q(a,S),Q(b,S)

def sin_bounds(x,n=30):
    s=Q(0)
    for k in range(n):
        term=x**(2*k+1)/factorial(2*k+1)
        s += term if k%2==0 else -term
    nxt=x**(2*n+1)/factorial(2*n+1)
    return (s,s+nxt) if n%2==0 else (s-nxt,s)

def F_lower(z):
    _,shi=sin_bounds(z/6)
    return z-6*shi

S=10**100
a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pi_lo=16*a5l-4*a239h
pi_hi=16*a5h-4*a239l
n3=isqrt(3*S*S)
s3lo,s3hi=Q(n3,S),Q(n3+1,S)
Dlo,Dhi=pi_lo/(2*s3hi),pi_hi/(2*s3lo)
slo,shi=sqrt_bounds(Dlo,Dhi,S)
C707_lo=2*slo+Q(7707,1_000_000)

T=Q(461,250)  # 1.844
Rt_hi=Q(9,2)*T-2*pi_lo-C707_lo
Z=Q(22069,10000)
delta_lo=F_lower(Z)

# Section-171 residual envelope:
# 2 delta + kappa/2 + h_res = R_t, with h_res>=0.
kappa_hi=2*(Rt_hi-2*delta_lo)
assert kappa_hi>0

# q-k=h_H-s_Z=tD and s_Z<=k=kappa D.
hdiam_hi=T+kappa_hi
switch_budget=2*hdiam_hi

# Audited adjacent-backbone constants.
p=Q(278778993,78216868750)
d_low=Q(9891,62500)
C_phase_up=Q(3258689123681,612912000000)

# Count-focused Pareto thresholds.
N=Q(1039)
L=Q(100_000_000_000)
bad_count=switch_budget/N
bad_beta=Q(2)/L
bad_phase=(2*C_phase_up/d_low)/L
bad_total=bad_count+bad_beta+bad_phase
margin=p-bad_total

assert kappa_hi<Q(73,10000)
assert hdiam_hi<Q(18513,10000)
assert switch_budget/p<Q(1039)
assert margin>0

print('PASS adjacent switch count N<1039+o(1)')
print('F(2.2069) lower =',float(delta_lo))
print('R_t upper =',float(Rt_hi))
print('kappa upper =',float(kappa_hi))
print('diameter edge density upper =',float(hdiam_hi))
print('switch budget density upper =',float(switch_budget))
print('count-only threshold =',float(switch_budget/p))
print('bad density from count =',float(bad_count))
print('bad density from multiplier =',float(bad_beta))
print('bad density from phase =',float(bad_phase))
print('union-bound density margin =',float(margin))
print('CONCLUSION: eventually N<=1038; D*B,D*phasegap<1e11+o(1).')
