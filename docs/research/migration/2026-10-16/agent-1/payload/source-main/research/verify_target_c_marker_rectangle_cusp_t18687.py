#!/usr/bin/env python3
"""Exact auxiliary constants for the marker-classified rectangle cusp through t<=1.8687."""
from fractions import Fraction as Q

# Parent joint-cusp theorem supplies these certified rounded constants.
J=1_109_000
col_floor=Q(783,10_000)  # >0.0783 D common ordered columns

# Since N+L<J, there are at most J-1 diameter-endpoint/terminal defect objects.
# Mark at most two internal column slabs per object to handle ties on a column curve.
marked=2*(J-1)
runs=marked+1
clean_coeff=col_floor/runs
safe=Q(7,200_000_000)  # 3.5e-8
assert clean_coeff>safe

print('PASS: marker rectangle cusp auxiliary constants through t<=1.8687')
print('max defect objects =',J-1)
print('max marked internal slabs =',marked)
print('run denominator =',runs)
print('clean-run coefficient =',float(clean_coeff))
print('safe clean-run floor =',float(safe))
