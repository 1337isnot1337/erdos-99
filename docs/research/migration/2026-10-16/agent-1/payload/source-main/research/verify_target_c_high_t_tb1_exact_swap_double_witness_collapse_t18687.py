#!/usr/bin/env python3
"""Regression checks for repeated exact-swap blocker collapse."""

from fractions import Fraction

# Exact algebra identities behind ED.15 and ED.22.
for ai in range(1, 8):
    for aj in range(1, 8):
        qi = Fraction(ai, 17)
        qj = Fraction(aj, 19)
        H = qi * qj / (qi + qj)

        for a_num in range(1, 8):
            A = Fraction(a_num, 23)
            lower_gap = A * (1 / qi + 1 / qj) / 2 + (qi + qj) / 2
            assert 2 * H * lower_gap == A + qi * qj

        for b_num in range(1, 8):
            B = Fraction(b_num, 29)
            upper_gap = B * (1 / qi + 1 / qj) / 2 - (qi + qj) / 2
            assert 2 * H * upper_gap == B - qi * qj

# Scaling sanity. If q_i,q_j,d = O(D^-1), then:
# LOWER: ell=O(1) => 2 ell d H = O(D^-2).
# UPPER: ell=O(D) => 2 ell d H = O(D^-1), hence B=O(D^-1)
# and (D-ell)=B/(D+ell)=O(D^-2).
for D in (100, 1000, 10000):
    qi = Fraction(3, D)
    qj = Fraction(5, D)
    d = Fraction(7, D)
    H = qi * qj / (qi + qj)

    lower_rhs = 2 * Fraction(2, 1) * d * H
    assert lower_rhs * D * D == Fraction(105, 2)

    upper_rhs = 2 * D * d * H + qi * qj
    # D * upper_rhs remains bounded; the q_i q_j term vanishes after scaling.
    assert upper_rhs * D < 27

# Direction scaling sanity for UPPER: q/ell=O(D^-2), d=O(D^-1).
for D in (100, 1000, 10000):
    q = Fraction(3, D)
    d = Fraction(7, D)
    ell = D - Fraction(1, D)
    normalized_bound = q / (2 * ell) + d
    assert normalized_bound * D < 8

print("exact-swap double-witness collapse certificate: PASS")
