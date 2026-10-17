#!/usr/bin/env python3
"""Exact outward certificate for the coupled adaptive O-O path through t<=1.86248."""

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


def sin_bounds(x,n=28):
    s=Q(0)
    for k in range(n):
        term=x**(2*k+1)/factorial(2*k+1)
        s += term if k%2==0 else -term
    nxt=x**(2*n+1)/factorial(2*n+1)
    return (s,s+nxt) if n%2==0 else (s-nxt,s)


def F_bounds(z):
    slo,shi=sin_bounds(z/6)
    return z-6*shi,z-6*slo


SCALE=10**110
a5l,a5h=atan_inv_bounds(5,110)
a239l,a239h=atan_inv_bounds(239,35)
pi_lo,pi_hi=16*a5l-4*a239h,16*a5h-4*a239l
n3=isqrt(3*SCALE*SCALE)
s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Delta_lo,Delta_hi=pi_lo/(2*s3h),pi_hi/(2*s3l)
sDelta_lo,_=sqrt_bounds(Delta_lo,Delta_hi,SCALE)
C76_lo=2*sDelta_lo+Q(19,2500)
n2=isqrt(2*SCALE*SCALE)
sqrt2_hi=Q(n2+1,SCALE)

T=Q(23281,12500)           # 1.86248
z0=Q(209123,100000)        # 2.09123
A0=Q(5857,10000)

U0_lo=Q(9,2)*T-2*pi_hi
U0_hi=Q(9,2)*T-2*pi_lo
delta_max_hi=(U0_hi-C76_lo)/2
assert delta_max_hi<Q(93,1000)
assert U0_hi<Q(21,10)
assert 5*U0_hi*U0_hi<32*Delta_lo

omd=Q(907,1000)
rmax=Q(21,20)
assert 1-delta_max_hi>omd
Gdelta_lower=-6*(1+rmax)/(2*omd*omd)
assert Gdelta_lower>-Q(38,5)
assert z0*z0/72<Q(1,16)
Gz_lower=1-Q(1,16)/(2*omd)
assert Gz_lower>Q(24,25)
assert Q(24,25)-Q(38,5)*Q(1,16)>0

F_lo,F_hi=F_bounds(z0)
U_lo,U_hi=U0_lo-2*F_hi,U0_hi-2*F_lo
x_lo,x_hi=8*Delta_lo-U_hi*U_hi,8*Delta_hi-U_lo*U_lo
assert x_lo>0
root_lo,_=sqrt_bounds(x_lo,x_hi,SCALE)
m_lo=(U_lo+root_lo)/2
r_hi=U_hi-m_lo
p_hi=r_hi*r_hi/(2*(1-F_hi))
S_lo=pi_lo-U_hi-T/2+m_lo
H_hi=z0+p_hi-S_lo
assert H_hi<-Q(7,1000000)

assert rmax<4*omd
Gdelta_upper=Q(1,1)/(2*omd*omd)-2
A=Q(139,100)
assert Gdelta_upper<-A

assert A0+sqrt2_hi<2
lambda_min=A0-Q(93,1000)
assert lambda_min>Q(49,100)
assert A0<1
qprime_lower=2-Q(1,1)/lambda_min-Q(93,1000)/(lambda_min*lambda_min)
assert qprime_lower>-Q(21,50)
assert A+qprime_lower>Q(9,10)

assert F_hi<Q(43,1000)
q0_lo=2*F_lo-F_hi/(A0-F_hi)
low_total_lo=z0-U0_hi+q0_lo
assert low_total_lo>Q(1,125000)  # > 0.000008

phase_floor=Q(13,5000000)        # 0.0000026 < (0.000008)/3
assert Q(1,125000)/3>phase_floor
avg_switch_hi=2*Q(355,113)/phase_floor
assert avg_switch_hi<2416610

print('PASS: coupled adaptive O-O path through t<=1.86248')
for name,val in [
 ('U0 upper',U0_hi),('delta max',delta_max_hi),('F(z0)',F_lo),
 ('H(z0) outward upper',H_hi),('G_delta upper coarse',Gdelta_upper),
 ('lambda minimum',lambda_min),('q prime lower',qprime_lower),
 ('q(F(z0)) lower',q0_lo),('low-energy pair mass lower',low_total_lo),
 ('one-phase path floor',phase_floor),('switch-count average upper',avg_switch_hi),
]: print(name,'=',float(val))
