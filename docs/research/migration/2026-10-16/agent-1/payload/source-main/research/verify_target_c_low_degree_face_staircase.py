#!/usr/bin/env python3
from fractions import Fraction as Q
from math import isqrt

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

a5l,a5h=atan_inv_bounds(5,90)
a239l,a239h=atan_inv_bounds(239,25)
pil,pih=16*a5l-4*a239h,16*a5h-4*a239l
SCALE=10**100
n3=isqrt(3*SCALE*SCALE)
s3l,s3h=Q(n3,SCALE),Q(n3+1,SCALE)
Dl,Dh=pil/(2*s3h),pih/(2*s3l)
sDl,_=sqrt_bounds(Dl,Dh,SCALE)
C=2*sDl+Q(7707,1000000)

def lowface_floor(r,T):
    f0=C/2-T/4
    q0=2*T-pil
    return ((r-3)*f0-q0)/(r-4)

def threshold_lower(r):
    return (2*(r-3)*C+4*pil)/(r+5)

assert threshold_lower(5)>Q(20215,10000)
assert threshold_lower(6)>Q(21854,10000)
assert threshold_lower(7)>Q(23220,10000)
assert threshold_lower(10)>Q(26225,10000)
assert threshold_lower(15)>Q(29230,10000)
assert threshold_lower(22)>Q(31568,10000)

rows=[
    (6,Q(21,10),Q(1175,10000)),
    (6,Q(109,50),Q(75,10000)),
    (7,Q(11,5),Q(1220,10000)),
    (7,Q(23,10),Q(220,10000)),
    (10,Q(5,2),Q(766,10000)),
    (22,Q(3),Q(588,10000)),
]
for r,T,claim in rows:
    val=lowface_floor(r,T)
    assert val>claim,(r,T,float(val),float(claim))

univ=(Q(19)*C/2-Q(23)*pih/4)/18
assert univ>Q(57,10000)
assert Q(5,2)*univ>Q(142,10000)

print('PASS low-degree exceptional-face staircase')
print('C707 lower =',float(C))
for r in [5,6,7,10,15,22]:
    print('threshold r<=',r,'>',float(threshold_lower(r)))
for r,T,_ in rows:
    print('floor F_{<=%d}/D at t<=%.6f > %.12f'%(r,float(T),float(lowface_floor(r,T))))
print('universal F_{<=22}/D at t<=pi >',float(univ))
print('universal trains touching degree<=22 faces/D >',float(Q(5,2)*univ))
