#!/usr/bin/env python3
"""Sanity checker for the Profile A kernel-incidence closure.

This checks only the finite combinatorial endgame after the linear-algebra
lemmas have been proved in the accompanying note.
"""
from itertools import combinations

N_SINGLETONS = 7
N_PUNCTURES = 7

# Seven-row quotient dimension and each synchronized six-row child dimension.
s7 = 7 - 2 + 2
s6 = 6 - 2 + 2
assert s7 == 7
assert s6 == 6
assert s7 - s6 == 1

# In Profile A each six-row child keeps exactly five of the seven global
# singleton replacement blocks, so exactly two singleton blocks disappear.
assert N_SINGLETONS - 5 == 2

# If all seven singleton source classes are nonzero, a missing pair {a,b}
# forces both classes into the one-dimensional puncture kernel. Distinct
# puncture kernels therefore force the missing pairs to be vertex-disjoint.
# The maximum number of pairwise disjoint two-subsets of seven labels is 3.
labels = range(N_SINGLETONS)
pairs = list(combinations(labels, 2))
max_matching = 0
for mask in range(1 << len(pairs)):
    # Avoid exploring the entire 2^21 space once the trivial upper bound is met.
    if max_matching == N_SINGLETONS // 2:
        break
    used = set()
    size = 0
    ok = True
    for i, pair in enumerate(pairs):
        if not (mask >> i) & 1:
            continue
        if used.intersection(pair):
            ok = False
            break
        used.update(pair)
        size += 1
    if ok:
        max_matching = max(max_matching, size)
assert max_matching == 3
assert max_matching < N_PUNCTURES

# If one singleton source class vanishes in the seven-row quotient, that block
# cannot survive any six-row child: otherwise one of the child's exactly six
# surviving actual classes would be zero, contradicting rank six. Hence every
# missing pair contains the zero block. Distinct puncture kernels then require
# distinct nonzero partners, giving at most six punctures.
max_distinct_star_edges = N_SINGLETONS - 1
assert max_distinct_star_edges == 6
assert max_distinct_star_edges < N_PUNCTURES

# Two zero singleton classes are impossible before the incidence argument:
# seven singleton classes plus the pair span a seven-dimensional quotient, and
# the pair survives, so with two zero singletons there are at most six nonzero
# generators.
max_nonzero_generators_with_two_zero_singletons = (N_SINGLETONS - 2) + 1
assert max_nonzero_generators_with_two_zero_singletons == 6
assert max_nonzero_generators_with_two_zero_singletons < s7

print("profile_a_kernel_incidence_check passed")
print("s7", s7)
print("s6", s6)
print("kernel_dimension", s7 - s6)
print("max_distinct_kernels_all_singletons_nonzero", max_matching)
print("max_distinct_kernels_one_zero_singleton", max_distinct_star_edges)
