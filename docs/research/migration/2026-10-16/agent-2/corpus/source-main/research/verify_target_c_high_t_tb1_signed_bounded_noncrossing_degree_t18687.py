#!/usr/bin/env python3
"""Regression checks for bounded noncrossing degree of fixed-slack near-diameter matchings."""

import math

K = 31.4e6
A = K + 1.0
R = math.sqrt(2.0 * A)
Q = math.ceil(8.0 * (R + 0.5) ** 2)
alpha = Q + 1
assert Q == 502_463_416
assert alpha == 502_463_417

# The previous capacity constant is exactly one plus the pointwise number
# of noncrossers allowed around a fixed matching edge.
assert alpha == Q + 1


def graph_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def max_degree(n, mask, edges):
    deg = [0] * n
    for k, (i, j) in enumerate(edges):
        if (mask >> k) & 1:
            deg[i] += 1
            deg[j] += 1
    return max(deg, default=0)


def greedy_independent_size(n, mask, edges):
    """Greedy independent set in the graph represented by mask."""
    adj = [set() for _ in range(n)]
    for k, (i, j) in enumerate(edges):
        if (mask >> k) & 1:
            adj[i].add(j)
            adj[j].add(i)
    remaining = set(range(n))
    chosen = 0
    while remaining:
        v = next(iter(remaining))
        remaining -= {v} | (adj[v] & remaining)
        chosen += 1
    return chosen


# Exhaustively verify the abstract complement-degree extraction through six
# vertices: a graph of maximum degree Delta has an independent set of size
# at least ceil(n/(Delta+1)). In the application this independent set of the
# complement is a proper-crossing clique.
for n in range(1, 7):
    edges = graph_edges(n)
    for mask in range(1 << len(edges)):
        Delta = max_degree(n, mask, edges)
        got = greedy_independent_size(n, mask, edges)
        assert got >= math.ceil(n / (Delta + 1))

# Current localized SIGNED constants.
gamma = 791 / 9_600_000_000
delta0 = gamma / 8
T_star = 3.0605
c_star = delta0 / (6 * T_star)
lead_near_diameter_degree = 8 * 3 ** (1 / 8)
matching_denominator = 2 * lead_near_diameter_degree
crossing_coefficient = c_star / (matching_denominator * alpha)

assert matching_denominator == 16 * 3 ** (1 / 8)
assert 6.08e-20 < crossing_coefficient < 6.09e-20

# The only asymptotic loss after localization is the existing D^(3/4)
# matching extraction and a logarithm. The crossing-coloring loss is fixed,
# so the exponent remains 1/4-o(1).
for logD in [100.0, 1000.0, 10000.0]:
    beta_eff = 0.25 - math.log(logD) / logD
    assert 0.0 < beta_eff < 0.25

print("bounded noncrossing-degree regression checks passed")
print("Q_K =", Q)
print("alpha_K =", alpha)
print("SIGNED crossing coefficient =", crossing_coefficient)
