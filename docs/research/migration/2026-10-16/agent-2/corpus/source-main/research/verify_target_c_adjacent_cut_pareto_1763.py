#!/usr/bin/env python3
"""Exact certificate for the near-optimal count-focused Pareto refinement."""
from fractions import Fraction as Q

p = Q(278778993, 78216868750)
d_low = Q(9891, 62500)
pi_up = Q(355, 113)
C_phase_up = Q(3258689123681, 612912000000)

N_MAX = Q(1763)
L_MAX = Q(300_000_000)

bad_switch_count = 2*pi_up/N_MAX
bad_switch_weight = Q(2)/L_MAX
bad_phase = (2*C_phase_up/d_low)/L_MAX
bad_total = bad_switch_count + bad_switch_weight + bad_phase
margin = p - bad_total

assert margin > Q(3, 100_000_000)

print('PASS near-optimal switching-count Pareto refinement')
print('path boundary density lower =', float(p))
print('bad density from N>=1763 =', float(bad_switch_count))
print('bad density from D*B>=3e8 =', float(bad_switch_weight))
print('bad density from D*phasegap>=3e8 =', float(bad_phase))
print('total bad density upper =', float(bad_total))
print('density margin =', float(margin))
print('count-only limiting ratio 2*pi_up/p =', float(2*pi_up/p))
print('CONCLUSION: N<1763+o(1), so eventually N<=1762; D*B,D*phasegap<3e8+o(1).')
