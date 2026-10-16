#!/usr/bin/env python3
"""Exact constants for terminal-free high-t rhombic subladders."""
from fractions import Fraction as Q

# Coarse finite-defect strip through t<=1.8687:
# common transverse family > 0.6536 D-o(D), terminal occurrences <= 70954.
common_coarse = Q(6536, 10000)
L_coarse = 70954
coarse_run = common_coarse / (L_coarse + 1)
assert coarse_run > Q(92, 10_000_000)  # 9.2e-6

# Phase-collapsed joint cusp through t<=1.8687:
# retained ordered common columns > 0.0783 D-o(D), terminal occurrences <= 1,108,999.
common_phase = Q(783, 10000)
L_phase = 1_108_999
phase_run = common_phase / (L_phase + 1)
assert phase_run > Q(7, 100_000_000)  # 7e-8

print("PASS terminal-free rhombic subladder constants")
print("coarse clean-run coefficient =", float(coarse_run), coarse_run)
print("margin over 9.2e-6 =", float(coarse_run - Q(92,10_000_000)))
print("phase clean-run coefficient =", float(phase_run), phase_run)
print("margin over 7e-8 =", float(phase_run - Q(7,100_000_000)))
