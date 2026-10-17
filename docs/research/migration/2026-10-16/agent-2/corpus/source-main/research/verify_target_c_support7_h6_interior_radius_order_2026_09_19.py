#!/usr/bin/env python3
"""Finite certificate for the generic-H6 interior radial-order restriction.

The geometric lemma is proved in the companion note. This verifier checks the
finite reduction of the 7! strict radius-order cones for every pair of ground
slots occupied by reciprocal interior vertices 6 and 7.

No floating point arithmetic is used.
"""

from collections import Counter
from itertools import permutations
from math import factorial

LABELS = tuple(range(1, 8))
assert factorial(7) == 5040


def permitted(order, s6, s7):
    """Whether a strict ascending-radius order obeys both interior max bounds."""
    pos = {v: k for k, v in enumerate(order)}
    for v, s in ((6, s6), (7, s7)):
        # rho_v < max(rho_s,rho_{s+1}): v may not occur after both endpoints.
        if pos[v] > pos[s] and pos[v] > pos[s + 1]:
            return False
    return True


counts = {}
for s6 in range(1, 5):
    for s7 in range(1, 5):
        counts[(s6, s7)] = sum(
            permitted(order, s6, s7)
            for order in permutations(LABELS)
        )

expected = {
    (1, 1): 2520, (1, 2): 2352, (1, 3): 2240, (1, 4): 2240,
    (2, 1): 2352, (2, 2): 2520, (2, 3): 2352, (2, 4): 2240,
    (3, 1): 2240, (3, 2): 2352, (3, 3): 2520, (3, 4): 2352,
    (4, 1): 2240, (4, 2): 2240, (4, 3): 2352, (4, 4): 2520,
}
assert counts == expected
assert Counter(counts.values()) == Counter({2240: 6, 2352: 6, 2520: 4})

for (s6, s7), count in counts.items():
    d = abs(s6 - s7)
    if d == 0:
        assert count * 2 == 5040
    elif d == 1:
        assert count * 15 == 7 * 5040
    else:
        assert count * 9 == 4 * 5040

# Each one-interior restriction alone retains exactly 2/3 of strict orders.
for v in (6, 7):
    for s in range(1, 5):
        kept = 0
        for order in permutations(LABELS):
            pos = {x: k for k, x in enumerate(order)}
            if not (pos[v] > pos[s] and pos[v] > pos[s + 1]):
                kept += 1
        assert kept == 3360
        assert kept * 3 == 2 * 5040

print("PASS: generic-H6 interior radial-order finite certificate")
print("strict radius orders before H6 interiority: 5040")
print("permitted counts by slot distance: 0 -> 2520, 1 -> 2352, 2/3 -> 2240")
