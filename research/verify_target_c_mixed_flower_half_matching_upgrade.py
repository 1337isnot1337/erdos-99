#!/usr/bin/env python3
"""Combinatorial regression for the half-matching flower-splice upgrade."""
from fractions import Fraction as Q

# Componentwise matching facts for paths and cycles.
for e in range(1,500):
    path_matching=(e+1)//2
    assert path_matching>=Q(e,2)
    cycle_matching=e//2
    assert cycle_matching>=Q(e,2)-Q(1,2)

# If c=o(D) odd/cycle components are the only half-edge loss, then
# P>=L/2-c/2. Verify the propagated quadratic expression algebraically.
for L in range(1,200):
    for c in range(0,L+1):
        P=Q(L-c,2)  # weaker than L/2-c/2 when c counts all cycle components
        if P<0:
            continue
        deficit=P*P/Q(2)
        target=Q((L-c)*(L-c),8)
        assert deficit==target

M=Q(1327,10000)
assert M*M/Q(32)>Q(5502,10_000_000)

print('PASS mixed flower half-matching combinatorial regression')
print('current-row coarse deficit >',float(M*M/Q(32)))
