#!/usr/bin/env python3
"""Regression checks for the growing fully loaded force corridor."""

import math

C = 1_109_000
b = 0.1567
grid_coeff = C / b
assert 7.077e6 < grid_coeff < 7.078e6

# Model the diagonal construction by D_k=k^8 and rho_k=1/k.
# The proof is qualitative/diagonal; these exact model values check the scale
# relations used after the thresholds D_k are enlarged as necessary.
prev_narrow = None
for k in range(16, 80):
    D = k**8
    rho = 1.0 / k
    L = D**0.75

    # rho D^(1/4) -> infinity; here it equals k exactly.
    assert abs(rho * D**0.25 - k) < 1e-9 * k

    # Eventually the midpoint error is below the wide-pair separation scale.
    assert 2 * L <= 0.5 * D * math.sin(rho / 2)

    radius = 0.5 * D * math.sin(rho / 2) - L
    assert radius > 0
    assert radius / D**0.75 > 1
    assert radius / D < 0.1

    crossing_ratio = (1 + 2 / math.sin(rho)) * L / D
    assert crossing_ratio < 0.2

    same_side_cap = 2 * math.pi / math.sin(rho / 2)
    assert same_side_cap / D < 1e-6

    narrow_fraction = 3.0 / k
    if prev_narrow is not None:
        assert narrow_fraction < prev_narrow
    prev_narrow = narrow_fraction

# Longest-run combinatorics: G good positions split by B bad positions have a
# good run of length at least ceil(G/(B+1)).  Use very large k because the
# shore density itself is about 1.13e-5.
def longest_run_lower(good: int, bad: int) -> int:
    return (good + bad) // (bad + 1)

alpha_num = 113
alpha_den = 10_000_000
prev = 0
for k in [500_000, 1_000_000, 2_000_000, 4_000_000]:
    D = k**8
    # Conservative model: actual proof has o(D) + 3D/k + O(k).
    bad = 4 * D // k + 51 * k
    good = max(0, alpha_num * D // alpha_den - bad)
    run = longest_run_lower(good, bad)
    assert run > prev
    prev = run
assert prev > 1

c_H = 0.453819885927
assert 0.9076 < 2 * c_H < 0.9077

print("PASS: growing fully loaded force-corridor scale regressions")
print(f"slow-good grid coefficient = {grid_coeff:.6f}")
print(f"sharpened two-sided dipole slope coefficient = {2*c_H:.12f}")
print(f"model final longest-run lower bound = {prev}")
