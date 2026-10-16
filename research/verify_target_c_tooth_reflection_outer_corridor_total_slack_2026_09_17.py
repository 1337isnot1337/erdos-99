#!/usr/bin/env python3
"""Arithmetic/regression checks for the FREE outer-corridor total-slack theorem.

The proof of the activation-time telescope is symbolic and is recorded in the
corresponding research note. This script checks its quantitative consequences and
finite synthetic instances of the exact slack inequality.
"""

import math
import random

HSTAR = math.sqrt(303.0) / 52.0
CSTAR = 3.0 ** 0.125

assert 0.3347 < HSTAR < 0.3348
assert abs(CSTAR - 1.147202690439877) < 1e-15


def matching_coeff(K: float) -> float:
    return 0.25 - HSTAR / (2.0 * K)


def slab_matching_coeff(delta: float, K: float) -> float:
    return 0.5 * (delta - HSTAR / K)


# The first useful fixed threshold can be K=1 because 1 > 2 h_*.
assert 1.0 > 2.0 * HSTAR
assert matching_coeff(1.0) > 0.08262
assert abs(matching_coeff(1.0) - 0.08262600783144988) < 1e-15

# A quarter-depth slab has a positive K=2 matching coefficient.
assert 2.0 > HSTAR / 0.25
assert slab_matching_coeff(0.25, 2.0) > 0.04131
assert abs(slab_matching_coeff(0.25, 2.0) - 0.04131300391572494) < 1e-15

# Synthetic activation chains. For first-contact vectors c_j of unit length and
# activation gaps tau_j, the original edge is c_j + tau_j N, hence its excess
# above one is at most tau_j. Activation gaps telescope to the final join time.
rng = random.Random(99)
for _ in range(200):
    m = rng.randint(1, 200)
    raw = [rng.random() for _ in range(m)]
    final_time = rng.uniform(1e-4, HSTAR)
    scale = final_time / sum(raw)
    taus = [x * scale for x in raw]
    angles = [rng.uniform(-math.pi / 2, math.pi / 2) for _ in range(m)]
    slacks = []
    for tau, theta in zip(taus, angles):
        # N=(1,0), c=(cos theta,sin theta), and cos(theta)>=0 is consistent
        # with first-contact monotonicity.
        dx = math.cos(theta) + tau
        dy = math.sin(theta)
        length = math.hypot(dx, dy)
        slack = length - 1.0
        assert slack >= -1e-14
        assert slack <= tau + 1e-14
        slacks.append(max(0.0, slack))
    assert sum(taus) <= HSTAR + 1e-14
    assert sum(slacks) <= final_time + 1e-12

# Finite sanity check for the near-half chain length. With omega=log D, the new
# exact ledger gives leading coefficient 1/2 without division by 1+h_*.
for D in (1e8, 1e10, 1e12, 1e14, 1e16):
    omega = math.log(D)
    lower = (
        D / 2.0
        - CSTAR * D ** 0.75
        - omega * math.sqrt(D)
        - 2.0 * math.sqrt(D)  # conservative placeholder for the O(sqrt D) root term
        - HSTAR
        - D ** (-1.0 / 3.0)
    )
    assert lower > 0.35 * D
    assert lower / D < 0.5

# Markov + parity extraction: if total slack is <= t_D, the number of edges
# above K/D is at most t_D D/K. The asymptotic coefficients below must be positive.
for K in (1.0, 2.0, 4.0, 10.0):
    if K > 2.0 * HSTAR:
        assert matching_coeff(K) > 0.0

for delta, K in ((0.25, 2.0), (0.10, 4.0), (0.40, 1.0)):
    assert K > HSTAR / delta
    assert slab_matching_coeff(delta, K) > 0.0

print("FREE outer-corridor total-slack certificate: PASS")
print(f"h_*={HSTAR:.15f}")
print(f"K=1 matching coefficient={matching_coeff(1.0):.15f}")
print(f"quarter-depth K=2 layer coefficient={slab_matching_coeff(0.25, 2.0):.15f}")
