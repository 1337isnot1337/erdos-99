#!/usr/bin/env python3
"""Exact dense nonglobal family defeating minimum-cardinality cover search.

The all-k construction and population asymptotic are proved in the report.
This program verifies complete rational pair ledgers for k=4,5.
"""

if not __debug__:
    raise RuntimeError("Certificate assertions are required; run Python without -O.")

from fractions import Fraction as Q
from itertools import combinations
from math import isqrt
import json

from verify_global_joint_exchange_2026_10_12 import (
    diameter2,
    distance2,
    feasible,
    maximum_matching_cover,
    replay_matching_cover,
    point,
)


def family(k):
    assert k >= 4
    radius = k * k
    c = point(Q(radius, 2), 0)
    r = Q(radius, 2) - 4
    scale = 1 + Q(1, radius * radius)
    h = Q(isqrt(3 * radius**4) + 1, 2 * radius * radius)
    pair = [(c[0], Q(-1, 2)), (c[0], Q(1, 2))]
    interior = list(pair)
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            p = (c[0] + scale * (i + Q(j, 2)), scale * h * j)
            if distance2(p, c) <= r * r and all(distance2(p, z) > 1 for z in pair):
                interior.append(p)
    leaves = []
    for j in range(k):
        t = Q(j, radius)
        leaves.append((radius * (1 - t * t) / (1 + t * t),
                       2 * radius * t / (1 + t * t)))
    contraction = 1 - Q(1, 8 * radius)
    moved = [(contraction * x, contraction * y) for x, y in leaves]
    source = [point(0, 0)] + leaves + interior
    packet = moved + interior
    return radius, source, packet, len(interior)


def verify(k):
    radius, source, packet, interior_count = family(k)
    n, m = len(source), len(packet)
    threshold = Q(radius * radius)
    assert m == n - 1
    contacts = []
    h_edges = []
    pair_checks = 0
    for i, j in combinations(range(n), 2):
        d = distance2(source[i], source[j])
        pair_checks += 1
        assert 1 <= d <= threshold
        if d == 1:
            contacts.append((i, j))
        if d == threshold:
            h_edges.append((i, j))
    assert contacts == [(k + 1, k + 2)], "Source must have exactly one unit contact."
    assert h_edges == [(0, j) for j in range(1, k + 1)]
    assert feasible(packet, threshold)
    competitor = [source[0]] + packet
    assert len(competitor) == n and feasible(competitor, threshold)
    improved_d2 = diameter2(competitor)
    assert improved_d2 == (Q(radius) - Q(1, 8)) ** 2

    # Compute every cross pair. No upper conflict or unexpected lower conflict
    # is omitted; G must be exactly the copy/movement matching.
    adjacency = []
    for b, p in enumerate(packet):
        ns = set()
        for a, q in enumerate(source):
            d = distance2(p, q)
            pair_checks += 1
            if d < 1 or d >= threshold:
                ns.add(a)
        assert ns == {b + 1}
        adjacency.append(ns)
    source_set = set(range(n))
    min_cover = {0}
    leaf_cover = set(range(1, k + 1))
    min_witness, leaf_witness = {}, {}
    nu_min = maximum_matching_cover(adjacency, source_set - min_cover, witness=min_witness)[0]
    nu_leaf = maximum_matching_cover(adjacency, source_set - leaf_cover, witness=leaf_witness)[0]
    assert replay_matching_cover(adjacency, source_set-min_cover,
                                 json.loads(json.dumps(min_witness))) == nu_min
    assert replay_matching_cover(adjacency, source_set-leaf_cover,
                                 json.loads(json.dumps(leaf_witness))) == nu_leaf
    assert nu_min == m
    assert nu_leaf == interior_count
    assert m - len(min_cover) - nu_min == -1
    assert m - len(leaf_cover) - nu_leaf == 0
    # The star has precisely these two inclusion-minimal covers; supersets
    # cannot improve the joint cost, by the theorem's monotonicity argument.
    best_size = n + max(m - 1 - nu_min, m - k - nu_leaf)
    assert best_size == n
    # Count the additional complete packet and competitor pair ledgers.
    pair_checks += m * (m - 1) // 2 + n * (n - 1) // 2
    print(json.dumps({
        "k": k,
        "source_labels": n,
        "contact_isolated_labels": n - 2,
        "original_diameter": radius,
        "improved_diameter": str(Q(radius) - Q(1, 8)),
        "complete_pair_checks": pair_checks,
        "minimum_cover_profit": -1,
        "leaf_cover_profit": 0,
        "cross_graph": "exactly a matching",
        "full_source_certificate": "PASS",
    }, sort_keys=True))


def main():
    for k in (4, 5):
        verify(k)
    print("PASS: dense rational star family; nonglobality certified by every endpoint pair")


if __name__ == "__main__":
    main()
