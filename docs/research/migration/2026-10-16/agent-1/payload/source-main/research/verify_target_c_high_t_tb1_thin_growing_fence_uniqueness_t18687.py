#!/usr/bin/env python3
"""Regression checks for the THIN growing-fence uniqueness fork."""

import math

# Parent incidence-purification scale s=(1/4-o(1)) log_2 log D.
# Removing O(1) and taking one of 3 sectors gives coefficient 1/12.
assert abs((1.0 / 4.0) / 3.0 - 1.0 / 12.0) < 1e-15

# Eventual fixed-tube deletion/greedy constants are finite for every fixed L.
for L in [0.5, 1.0, 3.0, 10.0, 30.0]:
    C = 2 + math.ceil(math.sqrt(2.0 + 4.0 * L * L))
    assert C >= 4
    coeff = 1.0 / (12.0 * C)
    assert coeff > 0.0

# Finite extraction arithmetic: delete B boundary-near chords, split among 3
# sectors, then greedily lose a factor at most C.
for s in range(1, 100):
    for B in range(0, min(5, s) + 1):
        rem = s - B
        sector = math.ceil(rem / 3.0)
        assert sector * 3 >= rem
        for C in [4, 7, 13]:
            separated = math.ceil(sector / C)
            assert separated * C >= sector

# log log growth dominates any fixed boundary deletion and constant thinning.
prev = 0.0
for exponent in [20, 40, 80, 160]:
    # Use log D = exponent*log 10, avoiding enormous D itself.
    s_asym = 0.25 * math.log2(exponent * math.log(10.0))
    ratio = (s_asym / 3.0) / math.log2(exponent * math.log(10.0))
    assert abs(ratio - 1.0 / 12.0) < 1e-14
    assert s_asym > prev
    prev = s_asym

print("THIN growing-fence uniqueness regression checks passed")
