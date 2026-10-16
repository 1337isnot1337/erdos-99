#!/usr/bin/env python3
"""Regression checks for the adjacent high-t circumcenter flank ladder."""

import math

r = 0.6536
sqrt3 = math.sqrt(3.0)


def q(mu: float) -> float:
    return r - (1.0 + 2.0 * mu) / sqrt3


mu_star = (sqrt3 * r - 1.0) / 2.0
assert 0.06603 < mu_star < 0.06604
assert abs(q(mu_star)) < 1e-14
assert q(0.0) > 0.07624
assert 0.01851 < q(0.05) < 0.01852
assert 0.00696 < q(0.06) < 0.00698
assert 0.00119 < q(0.065) < 0.00120
assert 0.0 < q(0.066) < 4.0e-5
assert q(0.0661) < 0.0

# Common-prefix/common-suffix extraction: two ordered rows, each with at least Q
# labels below/above its threshold, share the first/last Q labels respectively.
for M in range(8, 60):
    order = list(range(M))
    for Q in range(1, M // 2 + 1):
        for low1 in range(Q, M - Q + 1):
            for low2 in range(Q, M - Q + 1):
                assert set(order[:Q]).issubset(set(order[:low1]))
                assert set(order[:Q]).issubset(set(order[:low2]))
        for high1 in range(Q, M - Q + 1):
            for high2 in range(Q, M - Q + 1):
                # A terminal segment of length at least Q always contains the
                # same final Q labels of the common order.
                assert set(order[-Q:]).issubset(set(order[-high1:]))
                assert set(order[-Q:]).issubset(set(order[-high2:]))

# Exact set identity behind the common-neighborhood estimate.
for gi in range(1, 30):
    for gj in range(1, 30):
        max_inter = min(gi, gj)
        for inter in range(max_inter + 1):
            sym = gi + gj - 2 * inter
            recovered = (gi + gj - sym) // 2
            assert recovered == inter

# Source-wide diameter midpoint error is o(D), so the local location-angle
# threshold tends to 2*mu.
def midpoint_error_ratio(D: float) -> float:
    eta = 3.0 ** 0.25 * math.sqrt(D)
    L = math.sqrt(D * eta + eta * eta)
    return L / D

mu = 0.06
prev = None
for D in [1e8, 1e10, 1e12, 1e14, 1e16]:
    err = midpoint_error_ratio(D)
    if prev is not None:
        assert err < prev
    prev = err
    rhs = 2.0 * mu - 2.0 * err
    assert rhs < 0.12
assert 0.117 < 0.12 - 2.0 * midpoint_error_ratio(1e12) < 0.118
assert 0.119 < 0.12 - 2.0 * midpoint_error_ratio(1e16) < 0.120

# The limiting angular separation corresponding to the mu=0.06 specialization.
angle = math.asin(0.12)
assert 0.1202 < angle < 0.1204
assert 6.89 < math.degrees(angle) < 6.90

print('PASS: adjacent high-t circumcenter flank-ladder regressions')
print('mu_star =', mu_star)
print('q(0) =', q(0.0))
print('q(0.05) =', q(0.05))
print('q(0.06) =', q(0.06))
print('q(0.065) =', q(0.065))
print('q(0.066) =', q(0.066))
print('arcsin(0.12) degrees =', math.degrees(angle))
print('D=1e12 location-angle sine floor =', 0.12 - 2.0 * midpoint_error_ratio(1e12))
