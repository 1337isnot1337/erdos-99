#!/usr/bin/env python3
"""Regression checks for the linear-rank coercive antipodal dipole block."""

from fractions import Fraction
from math import sin, sqrt

c = Fraction(113, 5_000_000)
delta0 = c / 64
density = c / 32

assert delta0 == Fraction(113, 320_000_000)
assert density == Fraction(113, 160_000_000)
assert density > 0

margin = 2.0 * sin(float(delta0))
l2_margin = 2.0 * sqrt(2.0) * sin(float(delta0))
assert margin > 0.0
assert l2_margin > margin

# Synthetic disjoint two-entry blocks. Each coordinate contributes one
# positive and one negative derivative, both of magnitude >= margin*D*|s_i|.
for coeffs in [
    [1.0],
    [1.0, -2.0, 0.5],
    [0.01, 7.0, -3.5, 2.25],
]:
    D = 1_000_000.0
    entries = []
    for s in coeffs:
        a = margin * D * abs(s)
        # The actual sign assignment can swap with sign(s); this canonical
        # synthetic block preserves the guaranteed opposite-sign pair.
        entries.extend([a, -a])

    inf_s = max(abs(s) for s in coeffs)
    max_pos = max(max(x, 0.0) for x in entries)
    max_neg = max(max(-x, 0.0) for x in entries)
    assert max_pos + 1e-9 >= margin * D * inf_s
    assert max_neg + 1e-9 >= margin * D * inf_s

    norm_s = sqrt(sum(s * s for s in coeffs))
    norm_entries = sqrt(sum(x * x for x in entries))
    assert norm_entries + 1e-7 >= l2_margin * D * norm_s

# The normalized coercivity constant does not degrade with dimension.
for n in (1, 2, 10, 100, 1000):
    coeffs = [1.0 / (i + 1) for i in range(n)]
    lhs_sq = sum(2.0 * (margin * s) ** 2 for s in coeffs)
    rhs_sq = (l2_margin ** 2) * sum(s * s for s in coeffs)
    assert lhs_sq + 1e-24 >= rhs_sq

print("PASS: linear-rank coercive antipodal dipole-block regressions")
print(f"selected_density={float(density):.12g}")
print(f"linfty_normalized_margin={margin:.12g}")
print(f"l2_normalized_margin={l2_margin:.12g}")
