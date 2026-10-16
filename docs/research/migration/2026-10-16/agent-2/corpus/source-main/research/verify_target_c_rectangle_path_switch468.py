#!/usr/bin/env python3
"""Exact certificate: Pareto rectangle + light leaf trimming gives N<468+o(1)."""
from fractions import Fraction as Q
from math import factorial,isqrt

def atan_inv_bounds(q,n):
    s=Q(0)
    for k in range(n):
        term=Q(1,(2*k+1)*q**(2*k+1)); s += term if k%2==0 else -term
    nxt=Q(1,(2*n+1)*q**(2*n+1)); return (s,s+nxt) if n%2==0 else (s-nxt,s)
def sqrt_bounds(lo,hi,S):
    a=isqrt((lo.numerator*S*S)//lo.denominator); b=isqrt((hi.numerator*S*S)//hi.denominator)+1
    return Q(a,S),Q(b,S)
def sin_bounds(x,n=30):
    s=Q(0)
    for k in range(n):
        term=x**(2*k+1)/factorial(2*k+1); s += term if k%2==0 else -term
    nxt=x**(2*n+1)/factorial(2*n+1); return (s,s+nxt) if n%2==0 else (s-nxt,s)
def F_bounds(z):
    slo,shi=sin_bounds(z/6); return z-6*shi,z-6*slo

# Pareto rectangle exact constants.
s0=Q(627,42520)
d0=Q(57,100)
n0=Q(1063,1000)
alpha=n0/s0
rho=Q(1581,200000)      # .007905 < rho_max
eta=Q(1,2000)           # discard at most .05% of leaves by Markov
center=d0-alpha*rho
rho_max=d0/alpha
p=(1-eta)*rho
assert rho<rho_max and center>0

# Global angular-defect upper constant.  Product decomposition gives
# average leaf offset <= C_phase/(rho*center*D); after eta-trimming every
# retained leaf has offset <= this divided by eta.
Cphase=Q(3258689123681,612912000000)
phase_constant=Cphase/(rho*center*eta)

# Current exact switch budget from t<=1.844 z>2.217.
S=10**100
a5l,a5h=atan_inv_bounds(5,100); a239l,a239h=atan_inv_bounds(239,30)
pi_lo=16*a5l-4*a239h; pi_hi=16*a5h-4*a239l
n3=isqrt(3*S*S); s3lo,s3hi=Q(n3,S),Q(n3+1,S)
Dlo,Dhi=pi_lo/(2*s3hi),pi_hi/(2*s3lo)
slo,shi=sqrt_bounds(Dlo,Dhi,S)
C707_lo=2*slo+Q(7707,1_000_000)
T=Q(461,250)
Rt_hi=Q(9,2)*T-2*pi_lo-C707_lo
FZ_lo,_=F_bounds(Q(2217,1000))
kappa_hi=2*(Rt_hi-2*FZ_lo)
hdiam_hi=T+kappa_hi
switch_budget=2*hdiam_hi

# On the retained phase-close path only count and KKT switch mass need averaging.
N=Q(468)
L=Q(10**12)
bad_count=switch_budget/N
bad_beta=Q(2)/L
bad_total=bad_count+bad_beta
margin=p-bad_total

assert p>Q(79,10000)
assert switch_budget/p<Q(468)
assert margin>Q(1,1_000_000)

print('PASS rectangle-path adjacent switch count N<468+o(1)')
print('rho_max =',float(rho_max),'rho =',float(rho),'center density =',float(center))
print('trim fraction =',float(eta),'retained path density =',float(p))
print('leaf phase constant =',float(phase_constant))
print('switch budget density =',float(switch_budget))
print('count-only threshold =',float(switch_budget/p))
print('bad count density =',float(bad_count),'bad beta density =',float(bad_beta))
print('union-bound margin =',float(margin))
print('CONCLUSION: eventually N<=467; switching beta and leaf phase gap are O(1/D).')
