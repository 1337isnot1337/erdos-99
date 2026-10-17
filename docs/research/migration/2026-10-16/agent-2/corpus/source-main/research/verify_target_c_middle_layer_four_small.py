#!/usr/bin/env python3
"""Exact rational certificate for the four-small adjacent-layer constant.

Adds the disjoint middle-layer loaded-terminal count to the three costs in
verify_target_c_adjacent_cut_triple_small.py. The only new global budget is
sum_i L_i <= q <= pi D.
"""

from fractions import Fraction as Q

# Exact path density and lower-center incidence from the audited triple-small theorem.
p = Q(278778993, 78216868750)
d_low = Q(9891, 62500)

# Standard outward rational enclosures already used by the parent certificate.
pi_hi = Q(355, 113)
sqrt3_hi = Q(17321, 10000)

# C_phase = pi^2 sqrt(3) (2+sqrt(3))/12, with every factor replaced outward.
C_phase_hi = pi_hi * pi_hi * sqrt3_hi * (2 + sqrt3_hi) / 12

# Parent three-cost numerator:
#   sum N_i <= 2 pi D,
#   sum D B_i <= 2D,
#   sum D(q_i+q_{i+1}) <= 2 C_phase D/d_low.
base = 2 * pi_hi + 2 + 2 * C_phase_hi / d_low
K3 = base / p

# New fourth cost L_i=number of loaded terminals in physical middle layer R_i.
# The internal layers are disjoint, so sum L_i <= q <= pi D.
K4 = (base + pi_hi) / p

assert K3 < Q(21200)
assert K4 < Q(22060)

print("PASS four-small middle-layer certificate")
print("p =", float(p))
print("C_phase upper =", float(C_phase_hi))
print("three-cost average upper =", float(K3))
print("added loaded-terminal average =", float(pi_hi / p))
print("four-cost average upper =", float(K4))
print("exact four-cost upper =", K4)
print("CONCLUSION: one internal boundary has N_i, D B_i, D phasecost_i, L_i all < 22060+o(1)")
