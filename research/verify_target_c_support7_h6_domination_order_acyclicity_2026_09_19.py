#!/usr/bin/env python3
"""Exact order-level audit for all H6 interior-domination branch atoms.

Every domination branch compares a segment from a root to an interior target
against a segment from the same root to a hull endpoint.  The number of
interior endpoints therefore drops by exactly one along the forced
shorter-to-longer comparison.  This script checks the complete finite family of
possible atomic comparisons and the universal three-level scalar realization.
"""
from itertools import combinations

HULL = frozenset(range(6))
INTERIOR = frozenset((6, 7))
VERTICES = tuple(range(8))
SEGMENTS = tuple(combinations(VERTICES, 2))


def seg(a, b):
    assert a != b
    return tuple(sorted((a, b)))


def interior_count(edge):
    return sum(v in INTERIOR for v in edge)


def universal_length(edge):
    # HH=3, HI=2, II=1.  Only order matters.
    return 3 - interior_count(edge)


atoms = []
for target in INTERIOR:
    for root in VERTICES:
        if root == target:
            continue
        target_edge = seg(root, target)
        for endpoint in HULL:
            if endpoint == root:
                continue
            endpoint_edge = seg(root, endpoint)
            atoms.append((root, target, endpoint, target_edge, endpoint_edge))

assert len(SEGMENTS) == 28
assert atoms

levels = set()
for root, target, endpoint, target_edge, endpoint_edge in atoms:
    a = interior_count(target_edge)
    b = interior_count(endpoint_edge)
    assert a == b + 1, (root, target, endpoint, target_edge, endpoint_edge, a, b)
    assert universal_length(target_edge) < universal_length(endpoint_edge)
    levels.add((a, b))

assert levels == {(1, 0), (2, 1)}

# The actual H6 theorem contributes fourteen clauses: twelve with a hull root
# and one target in {6,7}, and two with the other interior point as root.  Each
# clause chooses one of two hull endpoints.  Since every possible atomic choice
# is already satisfied by the same universal assignment, every one of the
# 2^14 actual branch products is order-feasible, independent of the cell's
# bracketing edges.
assert 2 ** 14 == 16384

print("PASS: H6 domination branch atoms are universally order-acyclic")
print("segment levels: II=1, HI=2, HH=3")
print("atomic level transitions (target -> chosen endpoint):", sorted(levels, reverse=True))
print("actual domination branch products covered:", 2 ** 14)
