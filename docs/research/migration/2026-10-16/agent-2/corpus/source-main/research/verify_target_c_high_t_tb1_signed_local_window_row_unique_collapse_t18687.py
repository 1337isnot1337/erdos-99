#!/usr/bin/env python3
"""Finite checks for ROW-UNIQUE local-window collapse to COMMON-CUT."""

# Every closed region interval [p,q] containing g, except the singleton
# [g,g], supports at least one boundary cut tau_g or tau_{g+1}.
for m in range(1, 10):
    for g in range(m + 1):
        for p in range(m + 1):
            for q in range(p, m + 1):
                if not (p <= g <= q):
                    continue
                if p == q == g:
                    continue
                supports_left = g >= 1 and p < g <= q
                supports_right = g < m and p <= g < q
                assert supports_left or supports_right

# If both endpoint region indices equal g, every allowed owner coordinate is
# g. Injective ownership therefore permits at most one such blocker.
for multiplicity in range(2, 8):
    possible_owner_sets = [{3} for _ in range(multiplicity)]
    possible_owners = set().union(*possible_owner_sets)
    assert len(possible_owners) == 1 < multiplicity

print("ROW-UNIQUE local-window common-cut collapse checks passed")
