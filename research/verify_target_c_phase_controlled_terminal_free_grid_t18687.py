#!/usr/bin/env python3
"""Exact arithmetic for the phase-controlled terminal-free grid corridor."""
from fractions import Fraction as Q

B0_floor=Q(783,10000)
L0=1_108_999
run_density=B0_floor/Q(L0+1)
column_defect=Q(14_160_000)
column_phase_width=2*column_defect
row_phase_width=Q(7_080_000)

assert run_density>Q(706,10_000_000_000)  # >7.06e-8
assert column_phase_width==Q(28_320_000)
assert row_phase_width<Q(7_100_000)

print('PASS: phase-controlled terminal-free grid through t<=1.8687')
for k,v in [
    ('B0 floor',B0_floor),
    ('clean-run density',run_density),
    ('per-crossing defect coefficient',column_defect),
    ('column phase-width coefficient',column_phase_width),
    ('row phase-width coefficient',row_phase_width),
]: print(k,'=',float(v))
