#!/usr/bin/env python3
"""Constant checks for the high-t localized two-bar ladder theorem at t<=1.8687."""

from fractions import Fraction as Q

# Inputs already certified by the high-t rectangle joint-cusp theorem.
J = Q(1_109_000)
column_floor = Q(1567, 10_000)  # |B_+|/D > 0.1567-o(1)
retained_column_floor = Q(783, 10_000)  # safe |B_0|/D > 0.0783-o(1)

phase_coeff = J / column_floor
pair_defect_coeff = 2 * J / column_floor

assert phase_coeff < 7_080_000
assert pair_defect_coeff < 14_160_000
assert retained_column_floor == Q(783, 10_000)

# The two-bar localization theorem gives eta <= epsilon and
# endpoint separation <= 2D sin(eta/2) <= D eta. Thus the same
# coefficient controls the absolute endpoint-cluster separation.
endpoint_cluster_coeff = Q(7_080_000)
assert phase_coeff < endpoint_cluster_coeff

print("PASS: high-t localized two-bar ladder constants through t<=1.8687")
print("joint-cusp phase coefficient =", float(phase_coeff))
print("safe phase coefficient =", float(endpoint_cluster_coeff))
print("safe pair-defect coefficient =", float(pair_defect_coeff))
print("retained common-column density =", float(retained_column_floor))
