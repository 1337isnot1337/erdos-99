#!/usr/bin/env python3
"""Exact constants for the Caratheodory sparse-resultant adjacent-cut profile.

Inputs are the already-audited high-phase adjacent-cut path constants:
  * path length m > p D - o(D),
  * sum_j q_j <= C_phase/d_low + o(1).

The theorem itself uses Caratheodory in R^(2m): after preserving normalization,
the selected-cut resultant vector has a nonnegative actual-diameter representation
supported on at most 2m+1 rows.  Every row has interval support, so the sparse
representation has at most 4m+2 internal switch events.

For a fixed k>=4, the exact counting identity leaves asymptotic boundary density
(k-3)/(k+1) with at most k sparse switching rows.  Combining the sparse switch-weight
budget <=2 with the phase-offset budget gives the constants certified below.
"""
from fractions import Fraction as Q

# Exact/outward constants from verify_target_c_adjacent_cut_triple_small.py.
p = Q(278778993, 78216868750)
d_low = Q(9891, 62500)
C_phase_up = Q(3258689123681, 612912000000)
Q_phase = C_phase_up / d_low

SAFE = {
    4: Q(97500),
    5: Q(58500),
    6: Q(45500),
    7: Q(39000),
    8: Q(35000),
}

for k, cap in SAFE.items():
    good_coeff = Q(k - 3, k + 1)
    Ck = 2 * (Q_phase + 1) / (good_coeff * p)
    assert Ck < cap
    print(
        f"k={k}: exact asymptotic constant < {float(Ck):.12f}; "
        f"safe {int(cap)}; slack {float(cap-Ck):.12f}"
    )

# Finite algebra used before taking the source limit:
#   G_k >= (m-1) - (4m+2)/(k+1)
#       = ((k-3)m-(k+3))/(k+1).
for k in SAFE:
    for m in range(8, 500):
        rhs = Q((k - 3) * m - (k + 3), k + 1)
        direct = Q(m - 1) - Q(4 * m + 2, k + 1)
        assert rhs == direct

print("path-density lower p =", float(p))
print("phase-sum upper C_phase/d_low =", float(Q_phase))
print("PASS: Caratheodory sparse-resultant Pareto profile")
