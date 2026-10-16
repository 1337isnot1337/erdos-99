#!/usr/bin/env python3
"""Exact certificate for the finite-complexity nonhub strip at t<=1.8623."""

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

T=Q(18623,10000)
path=Q(33,50000)  # .00066

# Q/D <= 2t-pi, f<=Q, and 2*T_train=2tD+4f.
Q_upper=2*T-pi_lo
terminal_upper=2*T+4*Q_upper

# Each actual diameter interval starts/stops at most twice and |H|<=pi D.
switch_upper=2*pi_hi
complexity=terminal_upper+switch_upper
ratio=complexity/path

assert Q_upper<Q(584,1000)
assert terminal_upper<Q(6057,1000)
assert switch_upper<Q(6284,1000)
assert ratio<18697

print('PASS: finite terminal/switch strip through t<=1.8623')
for k,v in [
    ('pi lower',pi_lo),('pi upper',pi_hi),('Q upper',Q_upper),
    ('terminal occurrence upper',terminal_upper),('switch upper',switch_upper),
    ('combined complexity',complexity),('average ratio',ratio),
    ('margin to 18697',Q(18697)-ratio),
]:
    print(k,'=',float(v))
