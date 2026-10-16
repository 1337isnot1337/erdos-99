#!/usr/bin/env python3
"""Exact outward certificate extending corrected joint-feasibility O-O path to t<=1.86177."""
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
def sin_bounds(x,n=24):
    s=Q(0)
    for k in range(n):
        term=x**(2*k+1)/factorial(2*k+1)
        s += term if k%2==0 else -term
    nxt=x**(2*n+1)/factorial(2*n+1)
    return (s,s+nxt) if n%2==0 else (s-nxt,s)
def F_bounds(z):
    slo,shi=sin_bounds(z/6)
    return z-6*shi,z-6*slo

a5l,a5h=atan_inv_bounds(5,90); a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**100
n3=isqrt(3*SCALE*SCALE); s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,_=sqrt_bounds(Dl,Dh,SCALE)
C76=2*sDl+Q(19,2500)

T=Q(186177,100000)
U0lo=Q(9,2)*T-2*pih
U0hi=Q(9,2)*T-2*pil
dmax=(U0hi-C76)/2
assert dmax<Q(92,1000)
assert U0hi<Q(2095,1000)
assert 5*U0hi*U0hi<32*Dl
rmax=Q(21,20)
omd=Q(9087,10000)
assert 1+rmax*rmax<4*omd*omd
Gd_lower=-6*(1+rmax)/(2*omd*omd)
assert Gd_lower>-Q(757,100)
z0=Q(104803,50000)
assert z0*z0/72<Q(1,16)
Gz_lower=1-Q(1,16)/(2*omd)
assert Gz_lower>Q(24,25)
assert Q(24,25)-Q(757,100)*Q(1,16)>0
Flo,Fhi=F_bounds(z0)
Ulo=U0lo-2*Fhi
Uhi=U0hi-2*Flo
xlo=8*Dl-Uhi*Uhi
xhi=8*Dh-Ulo*Ulo
assert xlo>0
rootlo,_=sqrt_bounds(xlo,xhi,SCALE)
mlo=(Ulo+rootlo)/2
rhi=Uhi-mlo
p_hi=rhi*rhi/(2*(1-Fhi))
S_lo=pil-Uhi-T/2+mlo
H_hi=z0+p_hi-S_lo
assert H_hi<0
lam=Q(9949,20000)
brace=1-dmax-lam/2
same_sq=lam-lam*lam/4
assert brace>0
assert brace*brace>same_sq
coef=2-1/lam
assert coef<0
low_total=z0-U0hi+dmax*coef
assert low_total>Q(33,100000)
low_phase=low_total/3
assert low_phase>Q(11,100000)
avg=2*Q(355,113)/Q(11,100000)
assert avg<57120
print('PASS corrected joint-feasibility path through t<=1.86177')
print('U0 upper =',float(U0hi))
print('delta max =',float(dmax))
print('H(2.09606) outward upper =',float(H_hi))
print('geometry squared margin =',float(brace*brace-same_sq))
print('total low-energy pair floor =',float(low_total))
print('one-phase path floor =',float(low_phase))
print('switch-count average upper using .00011 =',float(avg))
