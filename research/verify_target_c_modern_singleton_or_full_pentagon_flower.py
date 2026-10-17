#!/usr/bin/env python3
"""Outward certificate for the singleton-or-fully-rhombic-pentagon dichotomy.

At a fixed t endpoint the modern all-train theorem gives
  P5/D >= p5(T) = pi + C707 - (5/2)T.
If F5 is the number of pentagons all five of whose sides border strict rhombi and S is
the singleton stopped-train count, then every pentagon outside F5 uses at least one
singleton face-side occurrence, while one singleton edge has only two face sides:
  P5-F5 <= 2S.
Balancing at s=p5/3 gives either S/D>=s or F5/D>=s.
In the F5 branch S<sD, rho_rec=2S<2sD and
  sigma_R = 2tau-rho_rec > 2(tau0-s)D.
The exact Mantel identity gives a corresponding quadratic deficit.
"""
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

def cert(T,bal_claim, sigma_claim, mantel_claim, train_claim):
    p5=pil+C707-Q(5,2)*T
    s=p5/3
    sigma=2*(tau0-s)
    mantel=sigma*sDl/2+sigma*sigma/16
    ntrain=Q(5,2)*s
    assert s>bal_claim
    assert sigma>sigma_claim
    assert mantel>mantel_claim
    assert ntrain>train_claim
    print('T=',float(T))
    print('  P5/D >',float(p5))
    print('  balanced S-or-Ffull floor >',float(s))
    print('  Ffull branch sigma_R/D >',float(sigma))
    print('  Ffull branch Mantel deficit/D^2 >',float(mantel))
    print('  Ffull branch trains touching full flowers/D >',float(ntrain))

cert(Q(37,20),       Q(142,1000),  Q(1207,1000), Q(666,1000), Q(357,1000))
cert(Q(371,200),     Q(138,1000),  Q(1215,1000), Q(671,1000), Q(347,1000))
cert(Q(18593,10000), Q(135,1000),  Q(1223,1000), Q(675,1000), Q(338,1000))
cert(Q(93,50),       Q(1346,10000),Q(1224,1000), Q(676,1000), Q(3366,10000))
cert(Q(1861,1000),   Q(1338,10000),Q(1225,1000), Q(677,1000), Q(3345,10000))
cert(Q(18623,10000), Q(1327,10000),Q(1228,1000), Q(679,1000), Q(3317,10000))
print('PASS')
