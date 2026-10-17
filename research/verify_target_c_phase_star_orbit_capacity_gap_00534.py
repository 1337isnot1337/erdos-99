#!/usr/bin/env python3
"""Exact rational certificate for corrected phase-star gap g=0.00534."""
from fractions import Fraction as F
from math import isqrt


def atan_inv_bounds(q, n):
    s = F(0)
    for k in range(n):
        term = F(1, (2*k+1)*q**(2*k+1))
        s += term if k % 2 == 0 else -term
    nxt = F(1, (2*n+1)*q**(2*n+1))
    return (s, s+nxt) if n % 2 == 0 else (s-nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator*scale*scale)//lo.denominator)
    b = isqrt((hi.numerator*scale*scale)//hi.denominator)
    return F(a,scale), F(b+1,scale)


a5l,a5h = atan_inv_bounds(5,80)
a239l,a239h = atan_inv_bounds(239,20)
pi_lo,pi_hi = 16*a5l-4*a239h, 16*a5h-4*a239l
S = 10**70
n3 = isqrt(3*S*S)
s3l,s3h = F(n3,S),F(n3+1,S)
Klo,Khi = F(2)/s3h,F(2)/s3l
Dlo,Dhi = pi_lo/(2*s3h),pi_hi/(2*s3l)
sl,sh = sqrt_bounds(Dlo,Dhi,S)
alpha = F(2,29)
g = F(534,100000)
Alo,Ahi = 2*sl+g,2*sh+g
Mlo = 4*Dlo/Ahi
residual_slope_hi = (Ahi-Mlo)/2

# High-center scope split.
assert Ahi/2 < Klo
high_center_capacity_hi = Klo*(Ahi-Klo)
assert high_center_capacity_hi < Dlo-F(3,100)
assert Klo-residual_slope_hi > F(1)

# Low-center optimizer lies in (W/3,W/2) subset (0,K).
r_edge_hi = F(2,3)*Ahi-Klo
left_derivative_lo = Mlo/3-alpha*(F(9)/Mlo)*r_edge_hi*r_edge_hi
assert left_derivative_lo > F(3,5)
assert F(2,3)*Mlo > Khi
assert 2*Klo > F(2,3)*Ahi

r_slope_hi = F(3,4)*Ahi-Klo
net_slope_lo = Mlo/3-alpha*r_slope_hi-residual_slope_hi
assert net_slope_lo > F(3,5)

# Strong-concavity endpoint certificate.
c0 = F(94049,100000)
assert Ahi/3 < c0 < Alo/2 < Klo
qlo,qhi = 3-Ahi/c0,3-Alo/c0
rlo,rhi = (Alo+c0)/2-Khi,(Ahi+c0)/2-Klo
phi_hi = c0*(Ahi-c0)-alpha*qlo*rlo*rlo
pc_lo = Alo-2*c0-alpha*(Ahi/(c0*c0)*rhi*rhi+qhi*rhi)
pc_hi = Ahi-2*c0-alpha*(Alo/(c0*c0)*rlo*rlo+qlo*rlo)
pc_abs = max(abs(pc_lo),abs(pc_hi))
psi_hi = phi_hi+pc_abs*pc_abs/4
margin = Dlo-psi_hi
assert margin > F(92,10_000_000)

print('PASS corrected phase-star gap g=0.00534')
print('A upper =',float(Ahi))
print('M lower =',float(Mlo))
print('high-center margin =',float(Dlo-high_center_capacity_hi))
print('left derivative lower =',float(left_derivative_lo))
print('net M slope lower =',float(net_slope_lo))
print('endpoint capacity margin =',float(margin))
