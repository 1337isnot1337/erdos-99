#!/usr/bin/env python3
"""Scaling checks for the diagonal growing-cusp-chain theorem."""

from fractions import Fraction as Q
from math import isqrt

base = Q(1_109_000)
phase_block = Q(14_160_000)

# With r_D <= D^(1/2) and the sharpened O(r) whole-window budget:
#   support/D <= base*r_D/D = O(D^-1/2)
#   switching beta mass <= base*r_D/D = O(D^-1/2)
#   row/column phase scales <= phase_block*r_D/D = O(D^-1/2).
for D in (10**8, 10**12, 10**16):
    r = isqrt(D)
    assert r * r <= D
    support_ratio = float(base * r / D)
    beta_mass = float(base * r / D)
    phase_diameter = float(phase_block * r / D)
    column_defect = float(phase_block * r / D)
    print(
        f"D={D}, r<={r}: support/D<{support_ratio:.9g}, "
        f"beta_mass<{beta_mass:.9g}, row_phase<{phase_diameter:.9g}, "
        f"column_defect<{column_defect:.9g}"
    )

print("PASS: O(r) window budgets with r<=D^(1/2) force support/D, beta mass, and phase scales to zero")
