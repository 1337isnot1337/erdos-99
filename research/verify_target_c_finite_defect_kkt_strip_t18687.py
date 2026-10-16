#!/usr/bin/env python3
"""Exact certificate propagating the finite-defect/KKT strip to t<=1.8687."""
from fractions import Fraction as Q


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
path=Q(203,1000000)
Q_upper=2*T-pi_lo
terminal_upper=2*T+4*Q_upper
switch_upper=2*pi_hi
kkt_scaled_upper=Q(2)
complexity=terminal_upper+switch_upper+kkt_scaled_upper
ratio=complexity/path

assert Q_upper<Q(596,1000)
assert terminal_upper<Q(6121,1000)
assert switch_upper<Q(6284,1000)
assert complexity<Q(14404,1000)
assert ratio<70955

print('PASS: finite-defect KKT strip through t<=1.8687')
for k,v in [
    ('Q upper',Q_upper),
    ('terminal occurrence upper',terminal_upper),
    ('switch-count upper',switch_upper),
    ('D*B global upper',kkt_scaled_upper),
    ('combined complexity',complexity),
    ('path floor',path),
    ('average ratio',ratio),
    ('margin to 70955',Q(70955)-ratio),
]: print(k,'=',float(v))
