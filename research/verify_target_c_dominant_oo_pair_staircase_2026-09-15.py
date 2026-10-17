#!/usr/bin/env python3
"""Exact rational certificate for the dominant O-O pair-weight staircase.

Uses the hostile-audited corrected matched atomic floor g=0.0076 and the existing
restored-incidence bootstrap. All asserted inequalities use Fraction arithmetic plus
outward enclosures for pi, square roots, and sin.
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
    b = isqrt((hi.numerator*scale*scale)//hi.denominator)
    return Q(a, scale), Q(b+1, scale)


def sin_bounds(x, n=24):
    s = Q(0)
    for k in range(n):
        term = x**(2*k+1)/factorial(2*k+1)
        s += term if k % 2 == 0 else -term
    nxt = x**(2*n+1)/factorial(2*n+1)
    return (s, s+nxt) if n % 2 == 0 else (s-nxt, s)


def F_bounds(z):
    slo, shi = sin_bounds(z/6)
    return z-6*shi, z-6*slo


a5_lo,a5_hi = atan_inv_bounds(5,90)
a239_lo,a239_hi = atan_inv_bounds(239,25)
pi_lo,pi_hi = 16*a5_lo-4*a239_hi,16*a5_hi-4*a239_lo

SCALE = 10**90
n3 = isqrt(3*SCALE*SCALE)
sqrt3_lo,sqrt3_hi = Q(n3,SCALE),Q(n3+1,SCALE)
Delta_lo,Delta_hi = pi_lo/(2*sqrt3_hi),pi_hi/(2*sqrt3_lo)
s_lo,s_hi = sqrt_bounds(Delta_lo,Delta_hi,SCALE)
C76_lo = 2*s_lo + Q(19,2500)


def certify(T, levels, pair_floor):
    Umax_lo = Q(9,2)*T - 2*pi_hi
    Umax_hi = Q(9,2)*T - 2*pi_lo
    delta_max_hi = (Umax_hi-C76_lo)/2
    assert Q(0) < delta_max_hi < 1

    def m2_bounds(Ulo,Uhi):
        xlo = 8*Delta_lo-Uhi*Uhi
        xhi = 8*Delta_hi-Ulo*Ulo
        assert xlo > 0
        a,b = sqrt_bounds(xlo,xhi,SCALE)
        return (Ulo+a)/2,(Uhi+b)/2

    def step(z):
        Flo,_ = F_bounds(z)
        Ulo = Umax_lo-2*Flo
        Uhi = Umax_hi-2*Flo
        mlo,_ = m2_bounds(Ulo,Uhi)
        rhi = Uhi-mlo
        Slo = pi_lo-Uhi-T/2+mlo
        p_hi = (delta_max_hi-Flo+rhi*rhi)/(2*(1-delta_max_hi))
        return Slo-p_hi,Flo,Uhi

    for i,z in enumerate(levels[:-1]):
        nxt,_,_ = step(z)
        assert nxt > levels[i+1]
        print(float(T), 'bootstrap', i, 'margin =', float(nxt-levels[i+1]))

    z = levels[-1]
    Flo,_ = F_bounds(z)
    Uhi = Umax_hi-2*Flo
    pair = z-Uhi
    assert pair > pair_floor
    print(float(T), 'z lower =', float(z), 'U upper =', float(Uhi),
          'O-O pair floor =', float(pair), 'claimed >', float(pair_floor))


certify(
    Q(461,250),  # 1.844
    [Q(0),Q(20721,10000),Q(21851,10000),Q(22034,10000),Q(22065,10000),Q(22070,10000)],
    Q(29,100),
)

certify(
    Q(37,20),  # 1.850
    [Q(0),Q(20285,10000),Q(21391,10000),Q(21570,10000),Q(21601,10000)],
    Q(21,100),
)

certify(
    Q(371,200),  # 1.855
    [Q(0),Q(19908,10000),Q(20991,10000),Q(21167,10000),Q(21197,10000)],
    Q(14,100),
)

print('PASS: dominant O-O pair staircase 0.29 / 0.21 / 0.14')
