#!/usr/bin/env python3
"""Exact combinatorial checks for the degree-pure support-seven reciprocal reduction.

No floating point arithmetic is used. Verifies the two 4-regular relation graph types,
coincidence bootstrap, collinear-subset restrictions, and the complete convex-H8 local
sign-consistency census.
"""

from collections import Counter
from itertools import combinations, permutations, product


def edge(a, b):
    return tuple(sorted((a, b)))


def graph_from_missing_cycles(cycles):
    missing = set()
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            missing.add(edge(a, b))
    return set(combinations(range(7), 2)) - missing, missing


CANONICAL = {
    "C7": [list(range(7))],
    "C3+C4": [[0, 1, 2], [3, 4, 5, 6]],
}


def bootstrap(relation, seed):
    active = set(seed)
    while True:
        add = {
            v
            for v in range(7)
            if v not in active
            and sum(edge(v, w) in relation for w in active) >= 2
        }
        if not add:
            return frozenset(active)
        active |= add


for name, cycles in CANONICAL.items():
    relation, missing = graph_from_missing_cycles(cycles)
    assert len(relation) == 14
    assert len(missing) == 7
    assert all(
        sum(edge(v, w) in relation for w in range(7) if w != v) == 4
        for v in range(7)
    )
    assert all(
        sum(edge(v, w) in missing for w in range(7) if w != v) == 2
        for v in range(7)
    )
    for seed in combinations(range(7), 2):
        assert bootstrap(relation, seed) == frozenset(range(7)), (name, seed)

# A collinear non-ground set must induce relation degree at most one.
expected_triples = {"C7": 7, "C3+C4": 5}
expected_quads = {"C7": 0, "C3+C4": 1}
for name, cycles in CANONICAL.items():
    relation, _ = graph_from_missing_cycles(cycles)
    goodsets = {}
    for size in (3, 4, 5):
        good = []
        for vertices in combinations(range(7), size):
            if max(
                sum(edge(v, w) in relation for w in vertices if w != v)
                for v in vertices
            ) <= 1:
                good.append(vertices)
        goodsets[size] = good
    assert len(goodsets[3]) == expected_triples[name]
    assert len(goodsets[4]) == expected_quads[name]
    assert len(goodsets[5]) == 0
    if name == "C3+C4":
        assert goodsets[4] == [(3, 4, 5, 6)]


def canonical_cycle(seq):
    seq = tuple(seq)
    variants = []
    for orientation in (seq, tuple(reversed(seq))):
        for k in range(len(seq)):
            variants.append(orientation[k:] + orientation[:k])
    return min(variants)


# Enumerate every labelled 2-factor on non-ground hull labels 1,...,7.
non_ground = tuple(range(1, 8))
factors = set()
for p in permutations(non_ground):
    c = canonical_cycle(p)
    if p != c:
        continue
    factors.add(
        ("C7", frozenset(edge(c[i], c[(i + 1) % 7]) for i in range(7)))
    )

for tri_tuple in combinations(non_ground, 3):
    tri = set(tri_tuple)
    quad = tuple(v for v in non_ground if v not in tri)
    tri_edges = frozenset(combinations(sorted(tri), 2))
    quad_cycles = set()
    for p in permutations(quad):
        c = canonical_cycle(p)
        if p != c:
            continue
        quad_cycles.add(
            frozenset(edge(c[i], c[(i + 1) % 4]) for i in range(4))
        )
    for qedges in quad_cycles:
        factors.add(
            ("C3+C4", frozenset(set(tri_edges) | set(qedges)))
        )

assert len(factors) == 465
assert sum(t == "C7" for t, _ in factors) == 360
assert sum(t == "C3+C4" for t, _ in factors) == 105


def ray_order(i, missing):
    """Cyclic raw-ray order at hull vertex i, with missing edges deleted."""
    out = []
    for d in range(1, 8):
        j = (i + d) % 8
        if edge(i, j) in missing:
            continue
        out.append(j)
    assert len(out) == 5
    return out


survivors = []
by_type = Counter()
ground_minority = Counter()
for typ, missing in factors:
    present = set(combinations(range(8), 2)) - set(missing)
    assert len(present) == 21
    orders = {i: ray_order(i, missing) for i in non_ground}
    for bits in product((0, 1), repeat=7):
        signs = {}
        consistent = True
        for i, bit in zip(non_ground, bits):
            order = orders[i]
            minority = {order[1], order[3]}
            for j in order:
                sign = (
                    (1 if j in minority else -1)
                    if bit
                    else (-1 if j in minority else 1)
                )
                e = edge(i, j)
                if e in signs and signs[e] != sign:
                    consistent = False
                    break
                signs[e] = sign
            if not consistent:
                break
        if not consistent:
            continue
        assert set(signs) == present
        positives = sum(signs[edge(0, j)] > 0 for j in non_ground)
        minority_count = min(positives, 7 - positives)
        survivors.append((typ, missing, bits, signs, minority_count))
        by_type[typ] += 1
        ground_minority[minority_count] += 1

assert len(survivors) == 76
assert by_type == Counter({"C7": 48, "C3+C4": 28})
assert ground_minority == Counter({3: 72, 2: 4})

factor_multiplicity = Counter((typ, missing) for typ, missing, *_ in survivors)
assert len(factor_multiplicity) == 38
assert set(factor_multiplicity.values()) == {2}

# Convenience quotient by global sign reversal and hull reflection fixing vertex 0.
def reflect_edge(e):
    return edge((-e[0]) % 8, (-e[1]) % 8)


def reflect_missing(missing):
    return frozenset(reflect_edge(e) for e in missing)


def reflect_bits(bits):
    out = [None] * 7
    for old, bit in zip(non_ground, bits):
        new = (-old) % 8
        out[new - 1] = bit
    return tuple(out)


def key(typ, missing, bits):
    return typ, tuple(sorted(missing)), tuple(bits)


all_keys = {
    key(typ, missing, bits)
    for typ, missing, bits, _, _ in survivors
}
seen = set()
orbit_reps = []
for k in sorted(all_keys):
    if k in seen:
        continue
    typ, missing_tuple, bits = k
    missing = frozenset(missing_tuple)
    reflected = reflect_missing(missing)
    reflected_bits = reflect_bits(bits)
    orbit = {
        key(typ, missing, bits),
        key(typ, missing, tuple(1 - x for x in bits)),
        key(typ, reflected, reflected_bits),
        key(typ, reflected, tuple(1 - x for x in reflected_bits)),
    } & all_keys
    seen |= orbit
    orbit_reps.append(min(orbit))

assert seen == all_keys
assert len(orbit_reps) == 23
assert Counter(rep[0] for rep in orbit_reps) == Counter(
    {"C7": 15, "C3+C4": 8}
)

print("PASS: support-seven reciprocal reduction")
print("coincidence bootstrap: 42/42 seed-pair checks reach all seven vertices")
print("H8 labelled 2-factors:", len(factors))
print("H8 edge-consistent sign assignments:", len(survivors))
print("H8 surviving labelled missing factors:", len(factor_multiplicity))
print("H8 reflection/global-sign orbits:", len(orbit_reps))
print("H8 ground minority counts:", dict(sorted(ground_minority.items())))
