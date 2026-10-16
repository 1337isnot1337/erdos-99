#!/usr/bin/env python3
"""Regression checks for quarter-power SIGNED propagation through the common-cut grid."""

# New starting exponent from the bounded-noncrossing-degree extraction.
beta = 0.25

# General row-slot tradeoff: k=n^a, pair slots n^(2a), ordered row block
# n^(1-2a), then diagonal Ramsey leaves (1/2)log_2 k chords.
for a in [0.10, 0.20, 0.25, 1 / 3, 0.40, 0.49]:
    assert 0.0 < a < 0.5
    pre_chord_exp = beta * a
    row_exp = beta * (1.0 - 2.0 * a)
    cable_log2_coeff = beta * a / 2.0
    assert pre_chord_exp > 0.0
    assert row_exp > 0.0
    assert cable_log2_coeff > 0.0

# Concrete a=1/4 form.
a = 0.25
assert abs(beta * a - 1 / 16) < 1e-15
assert abs(beta * (1 - 2 * a) - 1 / 8) < 1e-15
assert abs(beta * a / 2 - 1 / 32) < 1e-15

# Balanced a=1/3 form.
a = 1 / 3
assert abs(beta * a - 1 / 12) < 1e-15
assert abs(beta * (1 - 2 * a) - 1 / 12) < 1e-15
assert abs(beta * a / 2 - 1 / 24) < 1e-15

# Check the finite row-slot lower bound on large model values.
# H=floor(n/4), k=floor(n^a), C=k choose 2,
# rows >= (H-C)/(C+1).
for a in [0.25, 1 / 3, 0.40]:
    for exponent in [8, 10, 12]:
        n = 10**exponent
        H = n // 4
        k = int(n**a)
        C = k * (k - 1) // 2
        rows = (H - C) / (C + 1)
        assert rows > 0
        normalized = rows / (n ** (1 - 2 * a))
        assert normalized > 0.1

print("quarter-power SIGNED propagation regression checks passed")
