#!/usr/bin/env python3
"""Exact outward certificate for the modern singleton / rhombic-pentagon split at T=1.8623."""
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
SCALE=10**90
n3=isqrt(3*SCALE*SCALE); s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l); sDl,sDh=sqrt_bounds(Dl,Dh,SCALE)
g=Q(7707,1000000); C707=2*sDl+g
tau0=Q(7467921,10000000)
T=Q(18623,10000)
f0=C707/2-T/4
Q0=2*T-pil
p50=2*f0-Q0
# RW: rho_rec=2S >= tau0 D.
singleton0=tau0/2
# RP: rho_rec<tau0D, sigma>tau0D, I5 >= 5(2f-Q)-rho.
I50=5*p50-tau0
rhombic_pent_train0=I50/2
touch_pent0=I50/5
touch_fraction0=touch_pent0/p50
mantel0=tau0*sDl/2+tau0*tau0/16
assert singleton0>Q(373,1000)
assert I50>Q(1244,1000)
assert rhombic_pent_train0>Q(622,1000)
assert touch_pent0>Q(248,1000)
assert touch_fraction0>Q(62,100)
assert mantel0>Q(390,1000)
print('RW singleton trains /D >=',float(singleton0))
print('RP I5/D >',float(I50))
print('RP non-singleton rhombic trains touching pentagons /D >',float(rhombic_pent_train0))
print('RP distinct pentagons touching rhombi /D >',float(touch_pent0))
print('RP fraction of pentagons touching rhombi >',float(touch_fraction0))
print('RP Mantel deficit /D^2 >',float(mantel0))
print('PASS')
