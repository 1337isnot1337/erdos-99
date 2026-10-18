#!/usr/bin/env python3
"""Exact rational checks for the numerical margins in the Target B GPI audit.

This verifies only displayed constants. It does not verify the geometric or
combinatorial lemmas used by GPI or MCP2.
"""

from fractions import Fraction as Q


def atan_partial(x: Q, terms: int) -> Q:
    """Return the first `terms` terms of the alternating arctan series."""
    return sum(
        (Q(-1) ** k) * x ** (2 * k + 1) / (2 * k + 1)
        for k in range(terms)
    )


# Machin's identity is pi/4 = 4 atan(1/5) - atan(1/239).
# An even number of terms gives a lower bound; an odd number gives an upper bound.
# Thus this is an exact rational lower bound for pi.
pi_lower = 16 * atan_partial(Q(1, 5), 8) - 4 * atan_partial(Q(1, 239), 3)
assert pi_lower > Q(314159, 100000)

sqrt3_upper = Q(1732051, 1000000)
sqrt_mu0_upper = Q(89443, 10000000)
mu0 = Q(8, 100000)
assert sqrt3_upper**2 > 3
assert sqrt_mu0_upper**2 > mu0

c_upper = 2 * sqrt3_upper / pi_lower
gamma0_lower = Q(3, 4) - c_upper / 2
unique_max_loss_upper = 4 * sqrt3_upper * (3 * sqrt_mu0_upper + mu0)
assert unique_max_loss_upper < Q(1865, 10000) < gamma0_lower
assert gamma0_lower > Q(198, 1000)

# The contradiction hypothesis gives 1-s < 5e-13*tau <= 5e-13.
u = Q(5, 10**13)
delta_coefficient = Q(4, 10**17)
assert delta_coefficient / mu0 == Q(5, 10**13)
assert Q(5, 10**13) + delta_coefficient < Q(6, 10**13)
assert 2 * u / (1 - u) < Q(3, 10**12)

# epsilon_bal < 1e-12 implies epsilon_bal**(1/4) < 1e-3 and
# sqrt(epsilon_bal) < 1e-6, so the displayed grid loss is < 0.00601.
grid_loss_cap = 6 * Q(1, 1000) + 4 * Q(1, 10**6)
assert grid_loss_cap < Q(601, 100000)

diameter_lower = (
    3
    - 4 * sqrt3_upper * Q(601, 100000)
    - 2 * sqrt3_upper * Q(3, 10**12)
    - Q(1, 10**10)
)
assert diameter_lower > Q(295, 100)

# Since s > 1-u and s,t <= 1, the lattice upper bound is at most
# 2c/(1-u)^2 + o(1), with a strict gap below 2.21.
lattice_upper = 2 * c_upper / (1 - u) ** 2
assert lattice_upper < Q(221, 100)

print("PASS: pi lower bound from exact Machin-series rationals")
print("PASS: unique-max loss < 0.1865 < gamma_0")
print("PASS: balancing, deletion, and grid-loss thresholds")
print("PASS: GPI diameter lower bound > 2.95 and lattice upper bound < 2.21")
print("Scope: numerical margins only; no geometric or graph proof is encoded.")
