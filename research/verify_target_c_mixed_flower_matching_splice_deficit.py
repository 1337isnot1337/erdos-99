#!/usr/bin/env python3
"""Finite combinatorial regression for the mixed matching-splice deficit theorem."""
from fractions import Fraction as Q

# Greedy matching bound in a loopless multigraph of maximum degree two:
# every selected edge deletes at most three edges. Check the algebraic consequence
# symbolically over a large finite integer box.
for T in range(2,200):
    for L in range(0,T+1):
        P=(L+2)//3  # ceil(L/3), safe lower matching size
        if 2*P>T:
            # Such L/P pairs cannot occur for a matching on T train vertices.
            continue
        r=P
        s=T-2*P
        edge_cap=Q(s*s,4)+r*s+Q(r*(r-1),2)
        closed=Q(T*T,4)-Q(P*P,2)-Q(P,2)
        assert edge_cap==closed
        assert edge_cap<=Q(T*T,4)-Q(P*P,2)
        assert Q(P*P,2)>=Q(L*L,18)

# Current full-flower coarse numeric row: (0.1327)^2/72 > 0.0002445.
M=Q(1327,10000)
assert M*M/Q(72)>Q(2445,10_000_000)

print('PASS mixed flower matching-splice combinatorial regression')
print('current-row deficit floor >',float(M*M/Q(72)))
