#!/usr/bin/env python3
"""Certificate for the modern high-t recipient-waste / pentagon-rhombus dichotomy.

Use safe tau0=0.7467921 from the hostile-audited modern chamber theorem and
2 tau = rho_rec + sigma_R.
If rho_rec<tau0 D, then sigma_R>tau0 D.  With T=B4/2 and
sigma_R=2T-4sqrt(R4), the Mantel deficit M=T^2/4-R4 satisfies exactly
  M = sigma_R*sqrt(R4)/2 + sigma_R^2/16.

Recipient waste also bounds unused exceptional-face occurrences.  If I5 is the number
of strict-rhombus/pentagon boundary incidences, then
  I5 >= (4f+Q-rho_rec) - [boundary capacity of degree>=6 faces].
The latter capacity is at most 6(Q-f), so
  I5 > 10f-5Q-tau0 = 5(2f-Q)-tau0.
Insert the high-t pentagon lower staircase p5(T)=2f0-Q0.
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

def cos_lower(x,n=24):
    s=Q(0)
    for k in range(n):
        term=x**(2*k)/factorial(2*k)
        s += term if k%2==0 else -term
    return s

a5l,a5h=atan_inv_bounds(5,90)
a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
S=10**90
n3=isqrt(3*S*S)
s3l,s3h=Q(n3,S),Q(n3+1,S)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,sDh=sqrt_bounds(Dl,Dh,S)
rho0=Q(739085,1000000)
assert cos_lower(rho0)>rho0
g=Q(7707,1000000)
tau0=Q(7467921,10000000)

# Exact deficit identity M = sigma*sqrt(R4)/2 + sigma^2/16.
mantel0=tau0*sDl/2 + tau0*tau0/16
assert mantel0>Q(390,1000)
print('Mantel deficit / D^2 >',float(mantel0),'safe > 0.390')

def cert(T, incidence_claim, touching_claim):
    f0=(rho0+g-T+2*sDl)/2
    Q0=2*T-pil
    p50=2*f0-Q0
    I50=5*p50-tau0
    # A pentagon has at most five rhombus-bordering edge occurrences.
    touch0=I50/5
    assert I50>incidence_claim
    assert touch0>touching_claim
    print('T=',float(T),'P5/D >',float(p50),'I5/D >',float(I50),'touching pentagons/D >',float(touch0))

cert(Q(37,20),  Q(468,1000), Q(93,1000))
cert(Q(371,200), Q(393,1000), Q(78,1000))
cert(Q(93,50),   Q(318,1000), Q(63,1000))
print('PASS')
