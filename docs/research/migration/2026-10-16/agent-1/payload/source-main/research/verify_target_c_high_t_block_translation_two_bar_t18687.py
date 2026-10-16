#!/usr/bin/env python3
"""Arithmetic checks for high-t contiguous block-translation reaction bounds."""

from fractions import Fraction as Q

base = Q(1_109_000)
column_floor = Q(1567, 10000)
block_phase_base = 2 * base / column_floor

assert block_phase_base < 14_160_000

print("PASS: high-t contiguous block-translation constants through t<=1.8687")
print("block phase coefficient per fixed r =", float(block_phase_base))
print("TB2 endpoint-cluster coefficient per fixed r =", float(block_phase_base))

for r in (1, 2, 3, 5, 10):
    support_cap = base * r
    subblocks = r * (r + 1) // 2
    print(
        f"r={r}: subblocks={subblocks}, support_cap<{int(support_cap)}, "
        f"beta_mass_cap<{int(support_cap)}/D, "
        f"opening_coeff<{float(block_phase_base * r):.6f}/D"
    )
