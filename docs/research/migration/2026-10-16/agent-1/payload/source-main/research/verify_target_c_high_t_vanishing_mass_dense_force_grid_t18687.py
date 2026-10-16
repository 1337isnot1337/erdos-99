#!/usr/bin/env python3
"""Regression checks for the dense-grid vanishing-mass force corridor."""

import math
from fractions import Fraction as Q

c = Q(113, 5_000_000)
C = 1_109_000
r0 = 0.6536
q0 = r0 - 1.02 / math.sqrt(3.0)

assert 0.06470 < q0 < 0.06471

for n in [10, 100, 1000]:
    m = 2 * n + 1
    rho = c / (80 * n * m)
    T0 = 41 * n
    Tr = 41 * m * n

    # One admissible explicit diagonal scale. The proof may choose D still larger.
    D = (2.0 * n / float(rho)) ** 4
    assert D ** 0.25 * float(rho) > n

    # Total adjacent crossing-family loss across the whole m-interface block.
    topology_cost = m * Tr * C
    assert topology_cost / D < 1.0 / n

    # A single exact-phase center row has defect sum < T0*C. Markov at
    # sigma=sqrt(T0*C/D) deletes only sigma*D=o(D) columns and makes every
    # surviving defect <=sigma on every exact-co-phased row.
    sigma = math.sqrt((T0 * C) / D)
    assert sigma < 1.0 / n
    deleted_fraction = (T0 * C) / (sigma * D)
    assert abs(deleted_fraction - sigma) < 1e-15

    # The common circumcenter flank coefficient remains positive.
    assert r0 - deleted_fraction - 1.02 / math.sqrt(3.0) > 0

print("PASS: dense-grid vanishing-mass force-corridor regressions")
print("near-full common-column density =", r0)
print("common +/-0.01D flank density =", q0)
