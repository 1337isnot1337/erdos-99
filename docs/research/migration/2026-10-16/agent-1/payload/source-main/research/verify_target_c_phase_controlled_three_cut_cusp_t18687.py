#!/usr/bin/env python3
"""Exact constants for a phase-controlled three-cut cusp at t<=1.8687."""
from fractions import Fraction as Q
from math import isqrt


def atan_inv_bounds(q,n):
    s=Q(0)
    for k in range(n):
        term=Q(1,(2*k+1)*q**(2*k+1))
        s += term if k%2==0 else -term
    nxt=Q(1,(2*n+1)*q**(2*n+1))
    return (s,s+nxt) if n%2==0 else (s-nxt,s)


a5l,a5h=atan_inv_bounds(5,100)
a239l,a239h=atan_inv_bounds(239,30)
pi_lo,pi_hi=16*a5l-4*a239h,16*a5h-4*a239l

T=Q(18687,10000)
row_floor=Q(113,5_000_000)      # 0.0000226
col_floor=Q(1567,10000)          # 0.1567
triplet_floor=Q(112,10_000_000)  # 0.0000112, below row_floor/2
common_col_floor=Q(1305,10000)   # 0.1305, below (5/6)*col_floor
assert row_floor/2>triplet_floor
assert Q(5,6)*col_floor>common_col_floor

S=10**90
n3=isqrt(3*S*S)
sqrt3_hi=Q(n3+1,S)
Cphase_hi=pi_hi*pi_hi*sqrt3_hi*(2+sqrt3_hi)/12
lambda_coeff=Cphase_hi/(row_floor*col_floor)
assert lambda_coeff<Q(1_502_000)

# Six-times-average Markov trimming retains at least 5/6 of both shores.
row_spread_coeff=6*Q(1_502_000)
cross_defect_coeff=13*Q(1_502_000)  # g + 6lambda + 6lambda
assert row_spread_coeff==Q(9_012_000)
assert cross_defect_coeff==Q(19_526_000)

# With at most m/6 bad rows, at least m/2-O(1) consecutive row triples are all good.
# Average the two-interface finite-defect cost over those good triples.
Kglob=10*T-2*pi_lo+2
two_interface_average=2*Kglob/triplet_floor
assert two_interface_average<Q(2_573_000)
J=2_573_000
face_cap=(J-1)//5
assert face_cap==514599
clean_density=common_col_floor/Q(face_cap+1)
assert clean_density>Q(25,100_000_000)  # 2.5e-7

print('PASS phase-controlled three-cut cusp through t<=1.8687')
for k,v in [
    ('Cphase upper',Cphase_hi),
    ('average phase coefficient',lambda_coeff),
    ('good consecutive-triplet density',triplet_floor),
    ('good common-column density',common_col_floor),
    ('row/column phase-spread coefficient',row_spread_coeff),
    ('row-column defect coefficient',cross_defect_coeff),
    ('two-interface defect average',two_interface_average),
    ('rounded finite cusp',Q(J)),
    ('exceptional-face cap',Q(face_cap)),
    ('clean subladder density',clean_density),
]: print(k,'=',float(v))
