#!/usr/bin/env python3
"""Exact certificate: optimize adjacent good-leaf path density for count-focused cusp reduction."""
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

# Optimized good-leaf path constants from the same audited fan inputs.
A=Q(1851,2500)       # .7404 weighted average center degree
W=Q(53,625)          # .0848 retained O-O weight
NC=Q(1063,1000)      # center train upper density
lam=Q(1601,2500)     # .6404
d_low=Q(1,10000)     # .0001
r=(lam-d_low)/NC     # lambda-r*N_C=d_low exactly
d_top=lam-(1-r)*NC
g=(A-lam)*W/(NC-lam)
p=d_top*g/(r*NC)
assert r>Q(1,2) and r<lam/NC
assert d_top>0 and d_low>0 and g>0 and p>0

# Exact current diameter-edge density upper from matched atomic envelope + z>2.2069.
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
T=Q(461,250)
Rt_hi=Q(9,2)*T-2*pi_lo-C707_lo
delta_lo=F_lower(Q(22069,10000))
kappa_hi=2*(Rt_hi-2*delta_lo)
hdiam_hi=T+kappa_hi
switch_budget=2*hdiam_hi

# Pareto union bound on the optimized path.
C_phase_up=Q(3258689123681,612912000000)
N=Q(543)
L=Q(100_000_000_000_000)
bad_count=switch_budget/N
bad_beta=Q(2)/L
bad_phase=(2*C_phase_up/d_low)/L
bad_total=bad_count+bad_beta+bad_phase
margin=p-bad_total

assert p>Q(68,10000)
assert switch_budget/p<Q(543)
assert margin>0

print('PASS optimized adjacent backbone N<543+o(1)')
print('lambda =',float(lam),'r =',float(r))
print('d_top =',float(d_top),'d_low =',float(d_low))
print('good leaf density =',float(g))
print('optimized path density =',float(p))
print('diameter edge density upper =',float(hdiam_hi))
print('switch budget density upper =',float(switch_budget))
print('count-only threshold =',float(switch_budget/p))
print('bad count density =',float(bad_count))
print('bad beta density =',float(bad_beta))
print('bad phase density =',float(bad_phase))
print('union-bound margin =',float(margin))
print('CONCLUSION: eventually N<=542; switching beta and phase gap remain O(1/D).')
