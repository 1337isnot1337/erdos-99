#!/usr/bin/env python3
"""Exact outward certificate for the paired-remainder bathtub exclusion t<=1.84370.

New ingredient relative to the hostile-audited t<=1.84365 theorem:
a trimmed good O-O pair submeasure in each leaf uses exactly 2G terminal-occurrence
mass.  The unused retained occurrence measure therefore has mass at least A-2G
and pays an additional one-well bathtub cost f(A-2G).  The two leaf remainders
are disjoint, so both costs add to the existing cross-leaf pair energy.
"""
from fractions import Fraction as Q
from math import factorial, isqrt


def atan_inv_bounds(q, n):
    s = Q(0)
    for k in range(n):
        term = Q(1, (2*k+1)*q**(2*k+1))
        s += term if k % 2 == 0 else -term
    nxt = Q(1, (2*n+1)*q**(2*n+1))
    return (s, s+nxt) if n % 2 == 0 else (s-nxt, s)


def sqrt_bounds(lo, hi, scale):
    a = isqrt((lo.numerator*scale*scale)//lo.denominator)
    b = isqrt((hi.numerator*scale*scale)//hi.denominator)+1
    return Q(a,scale), Q(b,scale)


def sin_bounds(x, n=30):
    s = Q(0)
    for k in range(n):
        term = x**(2*k+1)/factorial(2*k+1)
        s += term if k % 2 == 0 else -term
    nxt = x**(2*n+1)/factorial(2*n+1)
    return (s,s+nxt) if n % 2 == 0 else (s-nxt,s)


def F_bounds(z):
    slo,shi=sin_bounds(z/6)
    return z-6*shi, z-6*slo


def phase_energy_bounds(z):
    slo,shi=sin_bounds(z/2)
    return z-2*shi, z-2*slo


SCALE=10**100
a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pi_lo,pi_hi=16*a5l-4*a239h,16*a5h-4*a239l
n3=isqrt(3*SCALE*SCALE)
sqrt3_lo,sqrt3_hi=Q(n3,SCALE),Q(n3+1,SCALE)
K_lo,K_hi=Q(2)/sqrt3_hi,Q(2)/sqrt3_lo
Delta_lo,Delta_hi=pi_lo/(2*sqrt3_hi),pi_hi/(2*sqrt3_lo)
s_lo,s_hi=sqrt_bounds(Delta_lo,Delta_hi,SCALE)
rcrit_lo,_=sqrt_bounds(Q(20,29),Q(20,29),SCALE)
C707_lo,C707_hi=2*s_lo+Q(7707,1_000_000),2*s_hi+Q(7707,1_000_000)

T=Q(18437,10000)       # 1.84370
c=Q(21,20)             # 1.05
H=Q(13,20000)          # 0.00065
Rt_lo=Q(9,2)*T-2*pi_hi-C707_hi
Rt_hi=Q(9,2)*T-2*pi_lo-C707_lo

# 0. Residual-stability scope gate, inherited from the t<=1.844 phase theorem.
F1848_lo,_=F_bounds(Q(231,125))
assert F1848_lo > Q(29,1000)
Unet_scope_hi=Q(9,2)*T-2*pi_lo-2*F1848_lo
assert Unet_scope_hi < Q(1957,1000) < Q(2013,1000)

# 1. Residual slack localization h<0.00065.
dH_hi=(Rt_hi-H)/2
assert 0<dH_hi<Q(51,1000)
B_H_hi=c*c*H*H/(2*(1-dH_hi))
A_H_lo=pi_lo-T/2-c*H-B_H_hi
FA_H_lo,_=F_bounds(A_H_lo)
loc_margin=FA_H_lo-dH_hi
assert loc_margin > Q(2,1_000_000)

Fprime_cap=Q(67,500)
Qx_upper=-1/(2*Fprime_cap)+1
Qh_upper=-1/(2*Fprime_cap)+c+c*c*Q(101,1000)/(1-Q(51,1000))
assert Qx_upper<Q(-27,10)
assert Qh_upper<Q(-5,2)

# 2. Dominant-orbit box.
WBAR=Q(1912984,1_000_000)  # 1.912984
assert C707_hi+H < WBAR
RMAX=c*H
E0=Q(90689955,100000000)   # 0.90689955
assert Delta_lo-RMAX*RMAX/4 > E0

delta_max_hi=Rt_hi/2
assert delta_max_hi<Q(51,1000)

# 3. Retained dominant outer mass z>2.21904.
Z=Q(27738,12500)           # 2.21904
FZ_lo,FZ_hi=F_bounds(Z)
Fprime_Z_hi=Z*Z/Q(72)
assert 1-Fprime_Z_hi/(2*(1-delta_max_hi)) > Q(96,100)
B_x_hi=(1+c*c*H*H-FZ_lo)/(2*(1-delta_max_hi)*(1-delta_max_hi))
assert B_x_hi<1

# Boundary delta=F(Z): h*=Rt-2F(Z) lies strictly inside 0<h<H.
hstar_lo=Rt_lo-2*FZ_hi
hstar_hi=Rt_hi-2*FZ_lo
assert hstar_lo>0
assert hstar_hi < H-Q(2,1_000_000)

# Along the boundary x=h*-h, the capped survivor excess increases with h,
# so h=h*,x=0 is adverse.  It is still negative.
cap_excess_hi=(
    Z+c*c*hstar_hi*hstar_hi/(2*(1-FZ_hi))
    -pi_lo+T/2+c*hstar_hi
)
assert cap_excess_hi < Q(-2,100000)
assert delta_max_hi > FZ_hi+Q(18,100000)

# 4. Phasewise one-well convexity: every z_i>0.6904.
A=Q(863,1250)              # 0.6904
OTHER=(Z-A)/2
assert A<Z/3
fA_lo,_=phase_energy_bounds(A)
fO_lo,_=phase_energy_bounds(OTHER)
phase_margin=fA_lo+2*fO_lo-delta_max_hi
assert phase_margin > Q(2,1_000_000)

# 5. Both leaf train masses are <0.5436 by correlated strong capacity.
U0=Q(1359,2500)            # 0.5436
CLOW=WBAR-2*U0
CHI=Q(523,500)             # 1.046
alpha=Q(1,10)
assert CLOW>U0

# Generic center capacity excludes both tails.
assert CLOW<WBAR/2
assert CLOW*(WBAR-CLOW) < E0-Q(9,1000)
assert CHI>WBAR/2
assert CHI*(WBAR-CHI) < E0-Q(3,100000)

# Strong physical pair branch is valid non-circularly on the original configuration.
# Since z_V>A and every train contributes at most two retained outer occurrences,
# V>A/2. Hence C+U=W-V<WBAR-A/2. On the contradiction branch U>=U0,
# the larger-leaf excess ratio is bounded before any U->U0 replacement.
ratio_hi=(WBAR-A/2-K_lo)/U0
assert CHI<K_lo
assert ratio_hi<rcrit_lo


def cap(C):
    V=WBAR-C-U0
    AA=1-V/C
    BB=1-U0/C
    x=alpha*(C+U0-K_hi)**2
    y=alpha*(C+V-K_hi)**2
    return C*(U0+V)-AA*x-BB*y


def cap_prime(C):
    V=WBAR-C-U0
    AA=1-V/C
    BB=1-U0/C
    eU=C+U0-K_hi
    eV=C+V-K_hi
    x=alpha*eU*eU
    y=alpha*eV*eV
    AAp=(WBAR-U0)/(C*C)
    BBp=U0/(C*C)
    return WBAR-2*C-AAp*x-AA*(2*alpha*eU)-BBp*y


Dconst=(K_hi*K_hi*WBAR+4*K_hi*U0*U0-4*K_hi*U0*WBAR-U0*U0*WBAR+U0*WBAR*WBAR)
assert (1+2*alpha)*CLOW**3-alpha*Dconst > CLOW**3
c0=Q(9301,10000)           # 0.9301
assert CLOW<c0<CHI
f0=cap(c0); fp0=cap_prime(c0)
cap_upper=f0+fp0*fp0/4
leaf_cap_margin=E0-cap_upper
assert leaf_cap_margin > Q(4,1_000_000)

# 6. Common-center good O-O weight.
# Generic center capacity also forces C>U0, so the denominator C-U0 used
# in the adverse bad-weight bound is strictly positive.
assert U0<WBAR/2
assert U0*(WBAR-U0) < E0-Q(1,10)

PAIR=A-U0
assert PAIR==Q(367,2500)   # 0.1468
BAD=Q(49,1250)             # 0.0392
disc=(BAD-2*WBAR)**2-8*(2*E0-BAD*U0)
assert disc<Q(-3,10000)
GOOD=PAIR-BAD
assert GOOD==Q(269,2500)   # 0.1076

# 7. New paired-remainder bathtub ledger.
# Trim each good leaf family to pair weight GOOD.  Its paired terminal
# submeasure has occurrence mass exactly 2*GOOD and is dominated by the
# selected retained occurrence measure.  The remainder therefore has mass
# at least A-2*GOOD and still obeys the one-well density cap.
REM=A-2*GOOD
assert REM==Q(594,1250)    # 0.4752
fREM_lo,_=phase_energy_bounds(REM)

SQRT3_UP=Q(17321,10000)
assert SQRT3_UP*SQRT3_UP>3
ALT_COST_LO=2-SQRT3_UP     # 0.2679
leaf_cross_energy_lo=ALT_COST_LO*GOOD

# center bathtub + cross-leaf pair energy + both leaf remainder bathtubs.
final_energy_lo=fA_lo+leaf_cross_energy_lo+2*fREM_lo
final_margin=final_energy_lo-delta_max_hi
assert final_margin > Q(8,10000)

print('PASS: paired-remainder bathtub excludes full-core Type-II t<=1.84370')
for name,val in [
    ('scope_U_hi',Unet_scope_hi),
    ('loc_margin',loc_margin),
    ('WBAR',WBAR),('E0',E0),
    ('hstar_lo',hstar_lo),('hstar_hi',hstar_hi),
    ('cap_excess_hi',cap_excess_hi),
    ('phase_margin',phase_margin),
    ('U0',U0),('ratio_hi',ratio_hi),('leaf_cap_margin',leaf_cap_margin),
    ('PAIR',PAIR),('BAD',BAD),('GOOD',GOOD),('bad_disc',disc),
    ('REM',REM),('center_energy_lo',fA_lo),
    ('leaf_cross_energy_lo',leaf_cross_energy_lo),
    ('two_remainder_energy_lo',2*fREM_lo),
    ('delta_max_hi',delta_max_hi),('final_margin',final_margin),
]:
    print(name,'=',float(val))
