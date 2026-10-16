#!/usr/bin/env python3
"""Regression checks for the fixed-accuracy linear tagged-ladder tradeoff."""

import math

M = 9_000_000
r0 = 0.6536
q0 = r0 - 1.02 / math.sqrt(3)

assert 0.06470 < q0 < 0.06471

for eps in [0.01, 0.02, 0.05, 0.06]:
    alpha = eps * eps / M
    common_density = r0 - eps - eps * eps
    flank_density = q0 - eps - eps * eps
    phase_spread = eps * eps / (r0 - eps * eps)

    assert alpha > 0
    assert common_density > 0
    assert flank_density > 0
    assert phase_spread > 0

    if eps == 0.01:
        assert abs(alpha - 1.1111111111111111e-11) < 1e-25
        assert abs(common_density - 0.6435) < 1e-15
        assert 0.05460 < flank_density < 0.05461
        assert 0.0001530 < phase_spread < 0.0001531

# One mechanism tag and one physical destination retain one quarter of the
# already linear tagged group.
assert (1 / 2) * (1 / 2) == 1 / 4

print("PASS: fixed-accuracy linear tagged-ladder regressions")
print("q0 =", q0)
print("eps=.01 tagged density =", 0.01**2 / M)
print("eps=.01 common-column density =", r0 - 0.01 - 0.01**2)
print("eps=.01 flank density =", q0 - 0.01 - 0.01**2)
print("eps=.01 all-row phase spread =", 0.01**2 / (r0 - 0.01**2))
