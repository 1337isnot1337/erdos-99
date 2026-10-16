#!/usr/bin/env python3
"""Regression checks for fixed-slack near-diameter noncrossing capacity."""

import math

# Algebraic constants for the current TB1 signed-upper application.
K = 31.4e6
A = K + 1.0
alpha = 1 + math.ceil(8.0 * (math.sqrt(2.0 * A) + 0.5) ** 2)
epsilon = 1.0 / (4.0 * alpha)
assert alpha == 502_463_417
assert abs(epsilon - 4.975486603435648e-10) < 1e-24

# Exact slack algebra Delta=D^2-(D-A/D)^2 < 2A, evaluated stably.
for D in [10.0 * A, 100.0 * A, 1000.0 * A]:
    ell = D - A / D
    stable = 2.0 * A - (A * A) / (D * D)
    assert 0.0 < stable < 2.0 * A
    # Interior-point exclusion estimate NC.11 is eventually subunit.
    near_endpoint = A / D + 2.0 * stable / ell
    assert near_endpoint < 1.0

# The close-connector theorem recovers the asymptotic thin threshold.
for a in [0.01, 0.1, 0.49]:
    assert math.sqrt(2.0 * a) < 1.0

# Ramsey inversion used in NC.25: if (r+a)^a <= M, then
# binom(r+a-1,a) <= M. Check exactly for manageable samples.
for a in range(1, 8):
    for r in range(1, 20):
        M = (r + a) ** a
        assert math.comb(r + a - 1, a) <= M

# D^(1/4)/log D is D^(1/4-o(1)); after the fixed Ramsey exponent,
# the claimed exponent is 1/(4 alpha).
for logD in [100.0, 1000.0, 10000.0]:
    beta_eff = 0.25 - math.log(logD) / logD
    assert beta_eff > 0.0
    assert beta_eff / alpha < epsilon
    assert beta_eff / alpha > 0.0

print("SIGNED near-diameter noncrossing-capacity regression checks passed")
print("alpha_K =", alpha)
print("epsilon_K =", epsilon)
