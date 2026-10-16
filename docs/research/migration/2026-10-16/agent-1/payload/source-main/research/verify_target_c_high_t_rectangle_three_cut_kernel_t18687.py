#!/usr/bin/env python3
"""Exact constants for a three-cut kernel embedded in the high-t rectangle at t<=1.8687."""
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
row_floor=Q(113,5_000_000)  # 0.0000226
col_floor=Q(1567,10000)      # 0.1567 oriented common columns
S=10**90
n3=isqrt(3*S*S)
sqrt3_hi=Q(n3+1,S)
Cphase_hi=pi_hi*pi_hi*sqrt3_hi*(2+sqrt3_hi)/12
Kglob=10*T-2*pi_lo+2
# Triple cost E_i=(C_i+C_{i+1})+(S_i+2S_{i+1}+S_{i+2}).
Ktriple=2*Kglob+4*Cphase_hi
avg=Ktriple/row_floor
print('Kglob',float(Kglob))
print('Cphase',float(Cphase_hi))
print('Ktriple',float(Ktriple))
print('average',float(avg))
# deliberately safe integer
J=Q(2_216_000)
assert avg < J
# exceptional union count and multiplier mass are individually <= J (asymptotically)
# phase-gap sum <= (S1+2S2+S3)/|B+| <= J/(col_floor D)
phase_sum_coeff=J/col_floor
assert phase_sum_coeff < Q(14_142_000)
# Markov on x_b = defects across all three row crossings: sum_b x_b = S1+S2+S3 <= J.
# Half columns then have each individual defect <= 2J/(col_floor D).
three_row_col_coeff=2*J/col_floor
assert three_row_col_coeff < Q(28_284_000)
print('margin',float(J-avg))
print('phase sum coeff',float(phase_sum_coeff))
print('half-column 3-row defect coeff',float(three_row_col_coeff))
print('PASS')
