#!/usr/bin/env python3
"""Exact certificate for the Pareto adjacent-cut refinement.

Using the already-audited path density p, total switch-count budget 2*pi*D,
total scaled switching-weight budget 2D, and total scaled phase-gap budget
(2*C_phase/d_low)D, a union bound finds one internal boundary satisfying all
three thresholds simultaneously.
"""
from fractions import Fraction as Q

# Audited exact constants from verify_target_c_adjacent_cut_triple_small.py.
p = Q(278778993, 78216868750)
d_low = Q(9891, 62500)
pi_up = Q(355, 113)
C_phase_up = Q(3258689123681, 612912000000)

N_MAX = Q(1800)
L_MAX = Q(1_000_000)

bad_switch_count = (2*pi_up)/N_MAX
bad_switch_weight = Q(2)/L_MAX
bad_phase = (2*C_phase_up/d_low)/L_MAX
bad_total = bad_switch_count + bad_switch_weight + bad_phase
margin = p - bad_total

assert margin > Q(4, 1_000_000)

print('PASS adjacent-cut Pareto refinement')
print('path boundary density lower =', float(p))
print('bad density from N>=1800 =', float(bad_switch_count))
print('bad density from D*B>=1e6 =', float(bad_switch_weight))
print('bad density from D*phasegap>=1e6 =', float(bad_phase))
print('total bad density upper =', float(bad_total))
print('density margin =', float(margin))
print('CONCLUSION: same adjacent boundary has N<1800, D*B<1e6, D*phasegap<1e6 (up to o(1)).')
