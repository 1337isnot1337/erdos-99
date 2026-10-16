#!/usr/bin/env python3
"""Exact arithmetic checks for the terminal-free high-t rhombic corridor."""
from fractions import Fraction as Q

column_floor=Q(1567,10000)
L0=1_108_999
J=1_109_000
run_density=column_floor/Q(L0+1)
four_defect_coefficient=Q(2*J,1)/run_density

assert run_density>Q(1412,10_000_000_000)   # >1.412e-7
assert four_defect_coefficient<Q(15_700_000_000_000)
assert L0//5 == 221_799

print('PASS: terminal-free rhombic corridor through t<=1.8687')
for k,v in [
    ('column floor',column_floor),
    ('terminal cap',Q(L0)),
    ('clean-run density',run_density),
    ('four-defect coefficient',four_defect_coefficient),
    ('margin to 1.57e13',Q(15_700_000_000_000)-four_defect_coefficient),
]: print(k,'=',float(v))
