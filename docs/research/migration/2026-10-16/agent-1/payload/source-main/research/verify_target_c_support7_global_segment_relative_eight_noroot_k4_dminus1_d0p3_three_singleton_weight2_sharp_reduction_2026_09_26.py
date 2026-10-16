#!/usr/bin/env python3
from itertools import combinations

coords = tuple(range(8))
pairs = tuple(combinations(coords, 2))

def disjoint_family(fam):
    return all(set(a).isdisjoint(b) for a, b in combinations(fam, 2))

for r in range(1, 6):
    found = any(disjoint_family(f) for f in combinations(pairs, r))
    assert found == (r <= 4)

matching = ((0, 1), (2, 3), (4, 5), (6, 7))
assert disjoint_family(matching)

def survives_all_sharp_triples(touch, M):
    touch = set(touch)
    M = set(M)
    return all(touch - (M | {j}) for j in set(coords) - M)

for M in matching:
    for r in range(9):
        for touch in combinations(coords, r):
            assert survives_all_sharp_triples(touch, M) == (
                len(set(touch) - set(M)) >= 2
            )

pair_indices = tuple(range(4))
for r in range(1, 5):
    for active in combinations(pair_indices, r):
        active = set(active)
        avoids_all = all(
            not active.issubset({i, k})
            for i in pair_indices
            for k in pair_indices
            if i != k
        )
        assert avoids_all == (len(active) >= 3)

vectors = tuple(range(16))
def span(gens):
    out = {0}
    for g in gens:
        out |= {x ^ g for x in tuple(out)}
    return frozenset(out)

subspaces = {
    span(gens)
    for r in range(5)
    for gens in combinations(vectors[1:], r)
}
for U in subspaces:
    active = set()
    for x in U:
        for i in pair_indices:
            if (x >> i) & 1:
                active.add(i)
    support = (
        set().union(*(set(matching[i]) for i in active))
        if active else set()
    )
    assert all(
        set(m).issubset(support) or set(m).isdisjoint(support)
        for m in matching
    )

print("PASS: k4 p3 weight-two sharp-shadow reduction")
print("max_disjoint_weight2_lines", 4)
print("perfect_matching_singleton_quotient_pair_support_min", 3)
print("perfect_matching_empty_support_is_union_of_pairs", True)
