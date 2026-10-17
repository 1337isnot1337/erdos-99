#!/usr/bin/env python3
"""Exact constant certificate for the high-t rectangle joint cusp at t<=1.8687."""

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
row_floor=Q(113,5_000_000)   # 0.0000226 consecutive rectangle rows
col_floor=Q(1567,10000)       # 0.1567 consistently oriented common columns

S=10**90
n3=isqrt(3*S*S)
sqrt3_hi=Q(n3+1,S)
Cphase_hi=pi_hi*pi_hi*sqrt3_hi*(2+sqrt3_hi)/12

# Global sum of N_i+L_i+D B_i is bounded by (10T-2pi+2)D+o(D).
Kglob=10*T-2*pi_lo+2

# If S_i is the angular-defect sum of row i over the oriented common columns,
# then sum_i(S_i+S_{i+1})<2 Cphase D.
Kangular=2*Cphase_hi
Ktotal=Kglob+Kangular
average=Ktotal/row_floor
assert average<1_108_000

# The theorem rounds to 1,109,000 to absorb deletion of O(1) indices and o(1).
J=Q(1_109_000)
phase_gap_coefficient=J/col_floor
half_column_pair_defect_coefficient=2*J/col_floor
assert phase_gap_coefficient<7_080_000
assert half_column_pair_defect_coefficient<14_160_000

print('PASS: high-t rectangle joint cusp through t<=1.8687')
for k,v in [
    ('global finite-defect coefficient',Kglob),
    ('two-row angular coefficient',Kangular),
    ('combined coefficient',Ktotal),
    ('limiting joint average',average),
    ('margin to 1,108,000',Q(1_108_000)-average),
    ('rounded cusp constant',J),
    ('row phase-gap coefficient',phase_gap_coefficient),
    ('half-column pair-defect coefficient',half_column_pair_defect_coefficient),
]:
    print(k,'=',float(v))
