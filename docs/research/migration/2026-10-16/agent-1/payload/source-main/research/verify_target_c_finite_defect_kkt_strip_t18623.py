#!/usr/bin/env python3
"""Exact certificate for the joint finite-defect/KKT strip at t<=1.8623."""

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

# Exceptional-degree budget: f<=Q and Q/D<=2t-pi.
Q_upper=2*T-pi_lo

# Exact stopped-train ledger gives 2*T_train/D=2t+4f/D.
terminal_upper=2*T+4*Q_upper

# Interval support: total switching-row count <=2|H|<=2pi D.
switch_upper=2*pi_hi

# Positive relative-interior KKT stress is normalized by sum beta_h=1, and every
# diameter interval starts/stops at most twice, so sum_i B_i<=2.  The averaged cost
# uses D*B_i and therefore contributes at most 2D globally.
kkt_scaled_upper=Q(2)

complexity=terminal_upper+switch_upper+kkt_scaled_upper
ratio=complexity/path

assert Q_upper<Q(584,1000)
assert terminal_upper<Q(6057,1000)
assert switch_upper<Q(6284,1000)
assert ratio<21727

print('PASS: finite-defect KKT strip through t<=1.8623')
for k,v in [
    ('Q upper',Q_upper),('terminal occurrence upper',terminal_upper),
    ('switch-count upper',switch_upper),('D*B global upper',kkt_scaled_upper),
    ('combined complexity',complexity),('average ratio',ratio),
    ('margin to 21727',Q(21727)-ratio),
]: print(k,'=',float(v))
