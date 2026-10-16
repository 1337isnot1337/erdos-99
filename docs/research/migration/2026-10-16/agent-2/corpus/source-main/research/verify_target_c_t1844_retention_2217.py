#!/usr/bin/env python3
"""Exact outward certificate: t<=1.844 residual localization forces z>2.217."""
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

S=10**100
a5l,a5h=atan_inv_bounds(5,100); a239l,a239h=atan_inv_bounds(239,30)
pi_lo,pi_hi=16*a5l-4*a239h,16*a5h-4*a239l
n3=isqrt(3*S*S); s3lo,s3hi=Q(n3,S),Q(n3+1,S)
Dlo,Dhi=pi_lo/(2*s3hi),pi_hi/(2*s3lo)
slo,shi=sqrt_bounds(Dlo,Dhi,S)
C707_lo,C707_hi=2*slo+Q(7707,1_000_000),2*shi+Q(7707,1_000_000)
T=Q(461,250); c=Q(21,20)
Rt_lo=Q(9,2)*T-2*pi_hi-C707_hi
Rt_hi=Q(9,2)*T-2*pi_lo-C707_lo

# Residual-stability scope gate from the previously proved z>2.2069.
Fold_lo,_=F_bounds(Q(22069,10000))
Unet_hi=Q(9,2)*T-2*pi_lo-2*Fold_lo
assert Unet_hi<Q(1916,1000)<Q(2013,1000)

# Residual slack localization.
H=Q(9,4000)  # .00225
dH_hi=(Rt_hi-H)/2
B_H_hi=c*c*H*H/(2*(1-dH_hi))
A_H_lo=pi_lo-T/2-c*H-B_H_hi
FA_lo,_=F_bounds(A_H_lo)
loc_margin=FA_lo-dH_hi
assert loc_margin>Q(3,1_000_000)
Fp=Q(67,500)
Qx=-1/(2*Fp)+1
Qh=-1/(2*Fp)+c+c*c*Q(101,1000)/(1-Q(51,1000))
assert Qx<Q(-27,10) and Qh<Q(-5,2)

# Retained dominant mass cap Z=2.217.
Z=Q(2217,1000)
FZ_lo,FZ_hi=F_bounds(Z)
hstar_lo=Rt_lo-2*FZ_hi
hstar_hi=Rt_hi-2*FZ_lo
assert hstar_lo>H
delta_max=Rt_hi/2
assert 1-Z*Z/Q(72)/(2*(1-delta_max))>Q(96,100)
Bx=(1+c*c*H*H-FZ_lo)/(2*(1-delta_max)*(1-delta_max))
assert Bx<1
cap_hi=(Z+c*c*H*H/(2*(1-FZ_hi))-pi_lo+T/2+hstar_hi+(c-1)*H)
assert cap_hi<Q(-2,10000)

# Consequent topology/diameter-edge density.
kappa_hi=2*(Rt_hi-2*FZ_lo)
hdiam_hi=T+kappa_hi
switch_budget=2*hdiam_hi

# Optimized path density from lambda=.6404, d_low=1e-4.
A=Q(1851,2500); W=Q(53,625); NC=Q(1063,1000); lam=Q(1601,2500); dlow=Q(1,10000)
r=(lam-dlow)/NC; dtop=lam-(1-r)*NC; g=(A-lam)*W/(NC-lam); p=dtop*g/(r*NC)
assert switch_budget/p<Q(542)

# Pareto n=542 can keep beta/phase inverse-D on the same boundary.
Cphase=Q(3258689123681,612912000000)
L=Q(100_000_000_000_000)
bad=switch_budget/Q(542)+Q(2)/L+(2*Cphase/dlow)/L
pareto_margin=p-bad
assert pareto_margin>Q(1,1_000_000)

print('PASS t<=1.844 residual retention z>2.217')
print('scope U upper =',float(Unet_hi))
print('h localization margin =',float(loc_margin),'H =',float(H))
print('hstar interval =',float(hstar_lo),float(hstar_hi))
print('z-cap excess upper =',float(cap_hi))
print('F(2.217) lower =',float(FZ_lo))
print('kappa upper =',float(kappa_hi),'diameter-edge density upper =',float(hdiam_hi))
print('optimized switch threshold =',float(switch_budget/p))
print('n=542 Pareto density margin =',float(pareto_margin))
print('CONCLUSION: z>2.217 and one optimized adjacent boundary has N<542, hence N<=541.')
