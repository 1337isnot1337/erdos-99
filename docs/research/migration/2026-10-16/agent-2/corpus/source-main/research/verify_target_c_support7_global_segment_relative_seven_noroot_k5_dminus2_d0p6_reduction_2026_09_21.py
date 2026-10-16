#!/usr/bin/env python3
"""Arithmetic checker for the seven-no-root D=-2,k=5,d=0,p=6 reduction.

Inputs already certified elsewhere in the repository:
  * six-row synchronized k=4 containment: D >= 6+p+3d-3q;
  * five-row repaired k=3 containment: D >= 5+p+3d-3q;
  * synchronized six-row d=1 virtual states have at most three
    canonical-complete blocks admitting a compatible singleton;
  * five-row d=1 virtual states have the same capacity upper bound three;
  * D=-2 all-depth deletion bounds preserve coefficient rank under one- and
    two-coordinate punctures.
This script checks only the arithmetic consequences used in the reduction.
"""

P = 6
D6 = 0
D5 = 2
CAP_D1 = 3


def six_lower(d, q):
    return 6 + P + 3 * d - 3 * q


def five_lower(d, q):
    return 5 + P + 3 * d - 3 * q


def min_singleton_replacements(p, q):
    """Minimum singleton replacements among q changed complete blocks.

    Each changed canonical-complete block is nonempty incomplete, hence costs
    one (singleton) or two (pair) rows. Other incomplete blocks, if any, cost
    at least one. Minimize singleton replacements subject to total incomplete
    cost p.
    """
    best = None
    for singleton_repl in range(q + 1):
        pair_repl = q - singleton_repl
        replacement_cost = singleton_repl + 2 * pair_repl
        if replacement_cost > p:
            continue
        leftover = p - replacement_cost
        if leftover >= 0:
            best = (
                singleton_repl
                if best is None
                else min(best, singleton_repl)
            )
    return best


# Six-row defect-zero shadow possibilities before the d=1 capacity obstruction.
six_possible = []
for d in range(1, 8):
    for q in range(P + 1):
        if six_lower(d, q) <= D6:
            six_possible.append((d, q))
assert six_possible == [(1, 5), (1, 6), (2, 6)], six_possible

# The d=1 possibilities need at least 4 or 6 singleton replacements among
# canonical-complete blocks, both exceeding the exact capacity three.
assert min_singleton_replacements(P, 5) == 4
assert min_singleton_replacements(P, 6) == 6
six_after_capacity = [
    (d, q)
    for d, q in six_possible
    if not (d == 1 and min_singleton_replacements(P, q) > CAP_D1)
]
assert six_after_capacity == [(2, 6)], six_after_capacity

# Pair deletion: d5 is between 1 and the six-row d6=2. The d=1 case needs at
# least q=4; since all six actual incomplete blocks are now known singletons,
# that would require at least four singleton-compatible complete blocks, above
# the exact five-row d=1 capacity three. Thus d5=2. Then q5>=5.
five_d1_q = [q for q in range(P + 1) if five_lower(1, q) <= D5]
assert five_d1_q == [4, 5, 6]
assert min(five_d1_q) == 4 > CAP_D1
five_d2_q = [q for q in range(P + 1) if five_lower(2, q) <= D5]
assert five_d2_q == [5, 6]

print("PASS: seven-no-root D=-2,k=5,d=0,p=6 reduction arithmetic")
print("six_shadow_candidates_before_capacity", six_possible)
print("six_shadow_candidates_after_d1_capacity", six_after_capacity)
print("minimum_singletons_for_d1_q5", min_singleton_replacements(P, 5))
print("minimum_singletons_for_d1_q6", min_singleton_replacements(P, 6))
print("five_shadow_d1_possible_q", five_d1_q)
print("five_shadow_d2_possible_q", five_d2_q)
