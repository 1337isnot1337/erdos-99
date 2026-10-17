#!/usr/bin/env python3
"""Arithmetic/regression checks for truncation-free OP charge and full matching activation."""

import math

h = math.sqrt(303.0) / 52.0
c = 0.129220199818177
delta = 2.0 * (1.0 - math.cos(c / 2.0))

assert 0.3347 < h < 0.3348
assert 0.00417 < delta < 0.00418


def coeffs(K: float, J: float):
    assert K > h and J > h
    alpha = 1.0 - h / K
    nu = 1.0 + delta * alpha / 4.0
    mu = nu - h / J
    matching = mu / 2.0
    old_coloring_activation = matching / 6.0
    full_activation_contacts = matching
    full_activation_endpoints = mu
    return (
        alpha,
        nu,
        mu,
        matching,
        old_coloring_activation,
        full_activation_contacts,
        full_activation_endpoints,
    )

alpha1, nu1, *_ = coeffs(1.0, 400.0)
assert abs(nu1 - 1.0006940263328101) < 1e-14

(alpha400, nu400, mu400, m400, old400, new400, endpoints400) = coeffs(400.0, 400.0)
assert abs(alpha400 - 0.9991631300391572) < 1e-14
assert abs(nu400 - 1.0010423801908050) < 1e-14
assert abs(mu400 - 1.0002055102299623) < 1e-14
assert abs(m400 - 0.5001027551149811) < 1e-14
assert abs(old400 - 0.08335045918583019) < 1e-14
assert abs(new400 - 0.5001027551149811) < 1e-14
assert abs(endpoints400 - 1.0002055102299623) < 1e-14
assert abs(new400 / old400 - 6.0) < 1e-14

nu_inf = 1.0 + delta / 4.0
m_inf = nu_inf / 2.0
area_inf = math.sqrt(3.0) * nu_inf / 2.0
area400 = math.sqrt(3.0) * nu400 / 2.0

assert abs(nu_inf - 1.0010432532581182) < 1e-14
assert abs(m_inf - 0.5005216266290591) < 1e-14
assert abs(area_inf - 0.8669288876085498) < 1e-14
assert abs(area400 - 0.8669281315100774) < 1e-14
assert 0.0 < area_inf - area400 < 1e-6

# Contact-count combinatorics in FA-SAT. If an iteration newly resolves s>=1
# matching endpoints, it creates at least max(1,s-1) contacts, which is >= s/2.
for s in range(1, 10000):
    assert max(1, s - 1) + 1e-15 >= s / 2.0

# Dynamic-programming regression: over every possible sequence of batch sizes
# resolving N endpoints, the minimum guaranteed new-contact count is ceil(N/2).
# We only need even N=2m, for which this equals m.
max_n = 200
best = [10**9] * (max_n + 1)
best[0] = 0
for n in range(1, max_n + 1):
    for s in range(1, n + 1):
        best[n] = min(best[n], best[n - s] + max(1, s - 1))
for m in range(1, max_n // 2 + 1):
    assert best[2 * m] == m

print("half-plus truncation-free OP/full-activation certificate: PASS")
print(f"h_* = {h:.15f}")
print(f"delta_* = {delta:.15f}")
print(f"nu_1 = {nu1:.15f}")
print(f"nu_400 = {nu400:.15f}")
print(f"mu_400 = {mu400:.15f}")
print(f"new-contact coefficient K=J=400 = {new400:.15f}")
print(f"activated-endpoint coefficient K=J=400 = {endpoints400:.15f}")
print(f"nu_inf = {nu_inf:.15f}")
print(f"new-contact envelope = {m_inf:.15f}")
print(f"sublinear-Z_ext H_out coefficient at K=400 = {area400:.15f}")
