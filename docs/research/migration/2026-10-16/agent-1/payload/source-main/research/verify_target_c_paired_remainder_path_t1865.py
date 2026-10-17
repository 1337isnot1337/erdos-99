#!/usr/bin/env python3
"""Exact outward certificate for the paired-remainder O-O path through t<=1.865."""
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


a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**110
n3=isqrt(3*SCALE*SCALE)
s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,SCALE)
C76lo=2*sDl+Q(19,2500)

T=Q(373,200) # 1.865
U0lo=Q(9,2)*T-2*pih
U0hi=Q(9,2)*T-2*pil
dmax=(U0hi-C76lo)/2
assert dmax<Q(99,1000)
assert U0hi<Q(211,100)
assert 5*U0hi*U0hi<32*Dl

# Corrected retained-mass feasibility on 0<=z<=z0, delta<=dmax.
rmax=Q(21,20)
omd=Q(9,10)
assert 1+rmax*rmax<4*omd*omd
Gd_lower=-6*(1+rmax)/(2*omd*omd)
assert Gd_lower>-Q(77,10)
z0=Q(10369,5000) # 2.0738
assert z0*z0/72<Q(1,16)
Gz_lower=1-Q(1,16)/(2*omd)
assert Gz_lower>Q(24,25)
assert Q(24,25)-Q(77,10)*Q(1,16)>0
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

# Physical opposite-branch margin.
lam=Q(2453,5000) # 0.4906
brace=1-dmax-lam/2
same_sq=lam-lam*lam/4
assert brace>0
assert brace*brace>same_sq

# Paired-remainder bathtub at the adverse endpoint.
# P >= z-U0+2 delta+kappa/2.  For the lower bound below:
# - low-mass functional increases with P because lambda>2-sqrt(3);
# - after P is replaced by its floor, it increases with z and kappa;
# - it decreases with delta (lambda<1/2) and with U0.
# Hence set t=T, z=z0, kappa=0, delta=dmax.
P0=z0-U0hi+2*dmax
assert P0>0
assert 2*P0<z0
rem0=z0-2*P0
Frem_lo,Frem_hi=F_bounds(rem0)
assert lam>2-s3h
low=P0-(dmax-Frem_lo)/lam
assert low>Q(11,1000)
phase=low/3
assert phase>Q(36,10000)
avg=2*Q(355,113)/Q(36,10000)
assert avg<1746

print('PASS paired-remainder path through t<=1.865')
print('U0 upper =',float(U0hi))
print('delta max =',float(dmax))
print('H(2.0738) outward upper =',float(H_hi))
print('geometry squared margin =',float(brace*brace-same_sq))
print('pair-weight floor =',float(P0))
print('residual occurrence mass =',float(rem0))
print('residual bathtub floor =',float(Frem_lo))
print('low-energy pair floor =',float(low))
print('one-phase path floor =',float(phase))
print('switch-count average upper using .0036 =',float(avg))
