#!/usr/bin/env python3
"""Exact finite certificate for the generic support-seven H6 outer sign reduction.

Scope: a degree-pure support-seven reciprocal H6 configuration with no collinear
triple of reciprocal points.  The verifier uses only integer/sign combinatorics.
Every actual generic H6 realization induces one of the enumerated rank-3 uniform
chirotopes, so failure of the local sign conditions is a rigorous obstruction.
The surviving outer cells are not claimed geometrically realizable.
"""
from collections import Counter
from itertools import combinations, permutations, product

HULL = tuple(range(6))          # convex hexagon, ground is 0
NON_GROUND = tuple(range(1, 8))
HULL_NON_GROUND = tuple(range(1, 6))
ALL = tuple(range(8))
INTERIOR = (6, 7)

H6_GROUND_PATTERNS = tuple(
    tuple(int(c) for c in s)
    for s in (
        "145", "156", "234", "235", "236", "237", "245",
        "256", "345", "346", "347", "356", "456",
    )
)
assert len(H6_GROUND_PATTERNS) == 13


def edge(a, b):
    return (a, b) if a < b else (b, a)


def hull_ray_order(i):
    """Other hull vertices in CCW ray order inside the hull angle at i."""
    return tuple((i + k) % 6 for k in range(1, 6))


def slot_chi(i, k, j):
    """chi(i,j,p) when interior ray p is inserted after k hull rays."""
    return 1 if hull_ray_order(i).index(j) < k else -1


# Every strict interior point has one of these six-vertex insertion patterns.
SINGLE_INTERIOR_SLOTS = tuple(
    ks
    for ks in product(range(1, 5), repeat=6)
    if all(
        slot_chi(i, ks[i], j) == -slot_chi(j, ks[j], i)
        for i, j in combinations(HULL, 2)
    )
)
assert len(SINGLE_INTERIOR_SLOTS) == 26
for ks in SINGLE_INTERIOR_SLOTS:
    # Boundary neighbors bracket a strict interior ray at every hull vertex.
    assert all(slot_chi(i, ks[i], (i + 1) % 6) == 1 for i in HULL)
    assert all(slot_chi(i, ks[i], (i - 1) % 6) == -1 for i in HULL)


def sorted_triple_with_parity(triple):
    a = list(triple)
    inv = sum(a[i] > a[j] for i in range(3) for j in range(i + 1, 3))
    return tuple(sorted(a)), (-1 if inv & 1 else 1)


def make_chirotope(slots6, slots7, chi_i67):
    """Store chi(a,b,c) for ascending triples a<b<c."""
    chi = {}
    for tri in combinations(HULL, 3):
        chi[tri] = 1
    for p, slots in ((6, slots6), (7, slots7)):
        for i, j in combinations(HULL, 2):
            value = slot_chi(i, slots[i], j)  # chi(i,j,p)
            key, parity = sorted_triple_with_parity((i, j, p))
            chi[key] = value * parity
    for i in HULL:
        key, parity = sorted_triple_with_parity((i, 6, 7))
        chi[key] = chi_i67[i] * parity
    assert len(chi) == 56
    assert set(chi.values()) == {-1, 1}
    return chi


def chi_value(chi, a, b, c):
    key, parity = sorted_triple_with_parity((a, b, c))
    return parity * chi[key]


def grassmann_pluecker_ok(chi):
    """Uniform rank-3 chirotope axiom, checked on every x and four-set."""
    for x in ALL:
        rest = tuple(v for v in ALL if v != x)
        for a, b, c, d in combinations(rest, 4):
            values = (
                chi_value(chi, x, a, b) * chi_value(chi, x, c, d),
                -chi_value(chi, x, a, c) * chi_value(chi, x, b, d),
                chi_value(chi, x, a, d) * chi_value(chi, x, b, c),
            )
            if values[0] == values[1] == values[2]:
                return False
    return True


def raw_order(i, slots6, slots7, chi_i67):
    base = hull_ray_order(i)
    k6, k7 = slots6[i], slots7[i]
    out = []
    for index, vertex in enumerate(base, 1):
        out.append(vertex)
        if k6 == index and k7 == index:
            out.extend((6, 7) if chi_i67[i] > 0 else (7, 6))
        elif k6 == index:
            out.append(6)
        elif k7 == index:
            out.append(7)
    assert len(out) == 7 and set(out) == set(ALL) - {i}
    return tuple(out)


# Enumerate every uniform rank-3 chirotope extension compatible with the convex
# hexagon and two strict interior points.  This is an outer combinatorial envelope:
# realizability is not assumed.
raw_order_types = set()
extensions_tested = 0
extensions_surviving = 0
for slots6 in SINGLE_INTERIOR_SLOTS:
    for slots7 in SINGLE_INTERIOR_SLOTS:
        forced = [
            1 if slots6[i] < slots7[i] else -1 if slots6[i] > slots7[i] else 0
            for i in HULL
        ]
        free = tuple(i for i in HULL if forced[i] == 0)
        for free_signs in product((1, -1), repeat=len(free)):
            chi_i67 = forced[:]
            for i, sign in zip(free, free_signs):
                chi_i67[i] = sign
            extensions_tested += 1
            chi = make_chirotope(slots6, slots7, chi_i67)
            if not grassmann_pluecker_ok(chi):
                continue
            extensions_surviving += 1
            raws = tuple(raw_order(i, slots6, slots7, chi_i67) for i in HULL)
            # Cross-check the raw radial orders against every hull-based chirotope sign.
            for i in HULL:
                for a, b in combinations(raws[i], 2):
                    assert chi_value(chi, i, a, b) == 1
            raw_order_types.add(raws)

assert extensions_tested == 4678
assert extensions_surviving == 1848
assert len(raw_order_types) == 1848
raw_order_types = tuple(sorted(raw_order_types))
assert len({raws[0] for raws in raw_order_types}) == 20


def canonical_cycle(seq):
    seq = tuple(seq)
    return min(
        orient[k:] + orient[:k]
        for orient in (seq, tuple(reversed(seq)))
        for k in range(len(seq))
    )


def cycle_edge_sets(nodes):
    nodes = tuple(nodes)
    first = min(nodes)
    rest = tuple(v for v in nodes if v != first)
    seen = set()
    for perm in permutations(rest):
        cycle = canonical_cycle((first,) + perm)
        if cycle in seen:
            continue
        seen.add(cycle)
        yield frozenset(
            edge(cycle[i], cycle[(i + 1) % len(cycle)])
            for i in range(len(cycle))
        )


def missing_graphs():
    for missing in cycle_edge_sets(NON_GROUND):
        yield "C7", missing
    for tri in combinations(NON_GROUND, 3):
        tri = frozenset(tri)
        quad = tuple(v for v in NON_GROUND if v not in tri)
        tri_edges = frozenset(edge(a, b) for a, b in combinations(sorted(tri), 2))
        for four_cycle in cycle_edge_sets(quad):
            yield "C3+C4", frozenset(set(tri_edges) | set(four_cycle))


MISSING_GRAPHS = tuple(missing_graphs())
assert Counter(t for t, _ in MISSING_GRAPHS) == Counter({"C7": 360, "C3+C4": 105})
for _, missing in MISSING_GRAPHS:
    assert len(missing) == 7
    assert all(sum(edge(v, w) in missing for w in NON_GROUND if w != v) == 2 for v in NON_GROUND)

# Ground patterns are positions in the strict raw order at vertex 0.  Fix the
# size-three class as +; global sign reversal is already normalized away.
ground_signs_by_order = {}
for raws in raw_order_types:
    order = raws[0]
    if order in ground_signs_by_order:
        continue
    signed = []
    for pattern in H6_GROUND_PATTERNS:
        positive_positions = set(pattern)
        signs = {v: (1 if order.index(v) + 1 in positive_positions else -1) for v in NON_GROUND}
        assert sum(1 for v in NON_GROUND if signs[v] > 0) == 3
        signed.append((pattern, signs))
    ground_signs_by_order[order] = tuple(signed)
assert len(ground_signs_by_order) == 20


def local_hull_base_signs(i, raw, missing):
    """Normalize the local positions-2,4 sign so edge 0i has sign +1."""
    absent = {j for j in NON_GROUND if j != i and edge(i, j) in missing}
    present = tuple(j for j in raw if j not in absent)
    assert len(absent) == 2 and len(present) == 5 and 0 in present
    base = {j: (1 if pos in (1, 3) else -1) for pos, j in enumerate(present)}
    ground_base = base[0]
    return {j: base[j] * ground_base for j in present if j in HULL_NON_GROUND}


counts = Counter()
pattern_survivors = Counter()
surviving_c7_missing = set()
surviving_c34_missing = set()
order_types_with_survivor = set()

for order_index, raws in enumerate(raw_order_types):
    ground_cases = ground_signs_by_order[raws[0]]
    for graph_type, missing in MISSING_GRAPHS:
        local = {i: local_hull_base_signs(i, raws[i], missing) for i in HULL_NON_GROUND}
        # For a present hull-hull relation edge ij, local complementation at i and j
        # is fixed by the corresponding ground-edge signs.  Eliminating those two
        # local complement bits gives s_0i*s_0j = normalized_i(j)*normalized_j(i).
        constraints = []
        for i, j in combinations(HULL_NON_GROUND, 2):
            if edge(i, j) not in missing:
                constraints.append((i, j, local[i][j] * local[j][i]))
        for pattern, ground_signs in ground_cases:
            ok = all(
                ground_signs[i] * ground_signs[j] == required
                for i, j, required in constraints
            )
            counts[(graph_type, ok)] += 1
            if not ok:
                continue
            pattern_survivors[pattern] += 1
            order_types_with_survivor.add(order_index)
            if graph_type == "C7":
                surviving_c7_missing.add(tuple(sorted(missing)))
            else:
                surviving_c34_missing.add(tuple(sorted(missing)))

assert counts == Counter({
    ("C7", False): 8440052,
    ("C3+C4", False): 2466164,
    ("C7", True): 208588,
    ("C3+C4", True): 56356,
})
assert sum(counts.values()) == 1848 * 465 * 13 == 11171160
assert counts[("C7", True)] + counts[("C3+C4", True)] == 264944
assert len(order_types_with_survivor) == 1848
assert len(surviving_c7_missing) == 348
assert len(surviving_c34_missing) == 105

EXPECTED_PATTERN_COUNTS = {
    "145": 3694,
    "156": 19678,
    "234": 10924,
    "235": 18556,
    "236": 67914,
    "237": 19678,
    "245": 10256,
    "256": 67914,
    "345": 2900,
    "346": 10256,
    "347": 3694,
    "356": 18556,
    "456": 10924,
}
assert {
    "".join(map(str, pattern)): count for pattern, count in pattern_survivors.items()
} == EXPECTED_PATTERN_COUNTS
assert sum(EXPECTED_PATTERN_COUNTS.values()) == 264944

all_c7_missing = {
    tuple(sorted(missing)) for typ, missing in MISSING_GRAPHS if typ == "C7"
}
excluded_c7_missing = all_c7_missing - surviving_c7_missing
EXPECTED_EXCLUDED_C7 = {
    tuple(edge(int(token[0]), int(token[1])) for token in line.split())
    for line in (
        "12 14 26 35 37 47 56",
        "12 14 27 35 36 46 57",
        "13 15 24 26 37 47 56",
        "13 15 24 27 36 46 57",
        "13 16 25 27 34 47 56",
        "13 16 25 27 37 45 46",
        "13 17 25 26 34 46 57",
        "13 17 25 26 36 45 47",
        "14 16 23 27 35 47 56",
        "14 17 23 26 35 46 57",
        "15 16 24 27 35 37 46",
        "15 17 24 26 35 36 47",
    )
}
assert excluded_c7_missing == EXPECTED_EXCLUDED_C7

# The obvious H6 relabeling symmetry fixes ground 0, reflects the hull
# (1,2,3,4,5) <-> (5,4,3,2,1), and may exchange the two interior labels 6,7.
# The twelve fully excluded labelled C7 embeddings form three classes.
def transform_missing(missing, reflect=False, swap_interiors=False):
    mp = {i: i for i in NON_GROUND}
    if reflect:
        hull_reflection = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 6, 7: 7}
        mp = {i: hull_reflection[mp[i]] for i in NON_GROUND}
    if swap_interiors:
        interior_swap = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 7, 7: 6}
        mp = {i: interior_swap[mp[i]] for i in NON_GROUND}
    return tuple(sorted(edge(mp[a], mp[b]) for a, b in missing))

seen = set()
excluded_symmetry_classes = []
for missing in sorted(excluded_c7_missing):
    if missing in seen:
        continue
    orbit = {
        transform_missing(missing, reflect, swap)
        for reflect in (False, True)
        for swap in (False, True)
    } & excluded_c7_missing
    seen |= orbit
    excluded_symmetry_classes.append(orbit)
assert sorted(len(orbit) for orbit in excluded_symmetry_classes) == [4, 4, 4]

print("PASS")
print("single-interior slot vectors:", len(SINGLE_INTERIOR_SLOTS))
print("uniform chirotope extensions tested:", extensions_tested)
print("generic H6 outer order types:", len(raw_order_types))
print("ground raw orders:", len(ground_signs_by_order))
print("labelled outer cells before local sign compatibility: 11171160")
print("local-sign survivors: 264944 = 208588 C7 + 56356 C3+C4")
print("C7 missing-graph embeddings with a survivor: 348/360")
print("C3+C4 missing-graph embeddings with a survivor: 105/105")
print("C7 embeddings excluded for every outer order type and every H6 ground pattern: 12")
print("excluded C7 symmetry classes under hull reflection and interior swap: 3")
for missing in sorted(excluded_c7_missing):
    print(" ", " ".join(f"{a}{b}" for a, b in missing))
print("survivors by ground pattern:")
for pattern in sorted(EXPECTED_PATTERN_COUNTS):
    print(" ", pattern, EXPECTED_PATTERN_COUNTS[pattern])
