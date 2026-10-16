#!/usr/bin/env python3
"""Exact constant certificate for the high-t complete rectangle through t<=1.8687."""

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
path=Q(1019,5_000_000)      # 0.0002038, certified one-window path floor
blocks=9
row_floor=Q(113,5_000_000)  # 0.0000226
assert path/blocks>row_floor

# Every selected path train has e_tau<=0.5857-delta and delta<0.107.
# The audited train-length inequality gives
#   r_tau/D >= 1-delta-e_tau/2 >= 1-.5857/2-delta/2.
degree_floor=Q(817,1250)     # 0.6536
assert 1-Q(5857,10000)/2-Q(107,1000)/2>degree_floor

# Exact stopped-train ledger: T_tr/D<=5T-2pi+o(1).
train_upper=5*T-2*pi_lo
assert train_upper<Q(6121,2000)  # <3.0605

# Partition the selected path into nine equal consecutive blocks. Each arbitrary
# complete train crosses a contiguous interval of the selected path, hence has at
# most one right endpoint. One block contains at most T_tr/9 right endpoints.
common_floor=Q(3134,10000)
assert degree_floor-train_upper/blocks>common_floor

# After deleting o(D) orientation-ambiguous columns, split the remaining common
# transversals between the two oriented crossing branches.
column_floor=Q(1567,10000)
assert common_floor/2>=column_floor

product_floor=row_floor*column_floor
assert product_floor>Q(347,100_000_000)

# Global angular-defect constant; used by the companion phase-collapse theorem.
S=10**90
n3=isqrt(3*S*S)
sqrt3_hi=Q(n3+1,S)
Cphase_hi=pi_hi*pi_hi*sqrt3_hi*(2+sqrt3_hi)/12
average_constant=Cphase_hi/product_floor
uniform_constant=5*average_constant
assert uniform_constant<7_700_000

trim_row=row_floor/2
trim_col=column_floor/2
assert trim_row>Q(56,5_000_000)  # >0.0000112
assert trim_col>Q(783,10000)     # >0.0783

print('PASS: high-t complete rectangle and phase constants through t<=1.8687')
for k,v in [
    ('pi lower',pi_lo),('path floor',path),('row floor',row_floor),
    ('degree floor',degree_floor),('complete train upper',train_upper),
    ('common transverse floor before sign split',common_floor),
    ('oriented column floor',column_floor),('rectangle product floor',product_floor),
    ('Cphase upper',Cphase_hi),('average defect constant',average_constant),
    ('uniform five-times constant',uniform_constant),
    ('trimmed row floor',trim_row),('trimmed column floor',trim_col),
]:
    print(k,'=',float(v))
