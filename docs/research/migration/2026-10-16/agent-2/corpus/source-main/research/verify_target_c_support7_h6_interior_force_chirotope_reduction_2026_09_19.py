#!/usr/bin/env python3
"""Exact certificate for the generic support-seven H6 interior-force reduction.

This verifier rebuilds the generic H6 oriented-matroid outer states from scratch,
reproduces the preceding hull-sign census, and then imposes one additional exact
necessary condition at the two reciprocal interior vertices.

For a strict closed equilateral force pentagon, the audited two-turn upper bound
says that, in cyclic force order, each force ray has exactly two other force rays
in its open left half-plane and exactly two in its open right half-plane.  If the
raw reciprocal-ray chirotope at vertex v is chi(v,a,b) and the edge signs are
s_va, s_vb, then the corresponding force determinant sign is

    chi_force(v,a,b) = s_va * s_vb * chi(v,a,b).

Hence the 2+2 half-plane balance can be checked using signs only.  At the five
non-ground hull vertices the previous local positions-2,4 theorem fixes every
incident edge sign once the ground-edge sign is known.  Thus all signs incident
to interior vertices 6 and 7 are fixed except possibly edge 67.  When 67 is
present both signs are tested, and one assignment must satisfy the 2+2 balance
at both interior vertices.

No floating point arithmetic or numerical optimization is used.
"""

from collections import Counter
from itertools import combinations, permutations, product

HULL = tuple(range(6))
NON_GROUND = tuple(range(1, 8))
HULL_NON_GROUND = tuple(range(1, 6))
INTERIOR = (6, 7)
ALL = tuple(range(8))

H6_GROUND_PATTERNS = tuple(
    tuple(int(c) for c in s)
    for s in (
        "145", "156", "234", "235", "236", "237", "245",
        "256", "345", "346", "347", "356", "456",
    )
)


def edge(a, b):
    return (a, b) if a < b else (b, a)


def hull_ray_order(i):
    return tuple((i + k) % 6 for k in range(1, 6))


def slot_chi(i, k, j):
    return 1 if hull_ray_order(i).index(j) < k else -1


SINGLE_INTERIOR_SLOTS = tuple(
    ks
    for ks in product(range(1, 5), repeat=6)
    if all(
        slot_chi(i, ks[i], j) == -slot_chi(j, ks[j], i)
        for i, j in combinations(HULL, 2)
    )
)
assert len(SINGLE_INTERIOR_SLOTS) == 26


def sorted_triple_with_parity(triple):
    a = list(triple)
    inv = sum(a[i] > a[j] for i in range(3) for j in range(i + 1, 3))
    return tuple(sorted(a)), (-1 if inv & 1 else 1)


def make_chirotope(slots6, slots7, chi_i67):
    chi = {}
    for tri in combinations(HULL, 3):
        chi[tri] = 1
    for p, slots in ((6, slots6), (7, slots7)):
        for i, j in combinations(HULL, 2):
            key, parity = sorted_triple_with_parity((i, j, p))
            chi[key] = slot_chi(i, slots[i], j) * parity
    for i in HULL:
        key, parity = sorted_triple_with_parity((i, 6, 7))
        chi[key] = chi_i67[i] * parity
    assert len(chi) == 56
    return chi


def chi_value(chi, a, b, c):
    key, parity = sorted_triple_with_parity((a, b, c))
    return parity * chi[key]


def grassmann_pluecker_ok(chi):
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


# Keep the full chirotope attached to each six-hull radial-order type.  The
# six hull orders determine it uniquely in this census.
ORDER_TYPES = {}
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
            if raws in ORDER_TYPES:
                assert ORDER_TYPES[raws] == chi
            else:
                ORDER_TYPES[raws] = chi

assert extensions_tested == 4678
assert extensions_surviving == 1848
assert len(ORDER_TYPES) == 1848
assert len({raws[0] for raws in ORDER_TYPES}) == 20


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


def local_base_signs_all(i, raw, missing):
    """Normalize the positions-2,4 local sign so edge 0i has sign +1."""
    absent = {j for j in NON_GROUND if j != i and edge(i, j) in missing}
    present = tuple(j for j in raw if j not in absent)
    assert len(absent) == 2 and len(present) == 5 and 0 in present
    base = {j: (1 if pos in (1, 3) else -1) for pos, j in enumerate(present)}
    ground_base = base[0]
    return {j: base[j] * ground_base for j in present if j != 0}


def force_rank2_balanced(chi, v, neighbors, signs):
    """Every force ray must have exactly two force rays on each open side."""
    for a in neighbors:
        left = sum(
            signs[a] * signs[b] * chi_value(chi, v, a, b) > 0
            for b in neighbors
            if b != a
        )
        if left != 2:
            return False
    return True


# Ground patterns are positions in the strict raw order at vertex 0.  Fix the
# size-three class as +; global sign reversal is normalized away.
GROUND_CASES = {}
for raws in ORDER_TYPES:
    order = raws[0]
    if order in GROUND_CASES:
        continue
    cases = []
    for pattern in H6_GROUND_PATTERNS:
        positive_positions = set(pattern)
        signs = {
            v: (1 if order.index(v) + 1 in positive_positions else -1)
            for v in NON_GROUND
        }
        cases.append((pattern, signs))
    GROUND_CASES[order] = tuple(cases)
assert len(GROUND_CASES) == 20

before = Counter()
after = Counter()
by_pattern_after = Counter()
by_67_after = Counter()
assignment_multiplicity = Counter()
missing_before = {"C7": set(), "C3+C4": set()}
missing_after = {"C7": set(), "C3+C4": set()}
order_types_after = set()

for order_index, (raws, chi) in enumerate(ORDER_TYPES.items()):
    for graph_type, missing in MISSING_GRAPHS:
        local = {
            i: local_base_signs_all(i, raws[i], missing)
            for i in HULL_NON_GROUND
        }

        # Reproduce the preceding hull-hull sign-compatibility filter.
        hull_constraints = []
        for i, j in combinations(HULL_NON_GROUND, 2):
            if edge(i, j) not in missing:
                hull_constraints.append((i, j, local[i][j] * local[j][i]))

        for pattern, ground_signs in GROUND_CASES[raws[0]]:
            if not all(
                ground_signs[i] * ground_signs[j] == required
                for i, j, required in hull_constraints
            ):
                continue

            before[graph_type] += 1
            missing_before[graph_type].add(tuple(sorted(missing)))

            # Hull vertices determine every present edge sign touching 6 or 7.
            fixed = {}
            for h in HULL_NON_GROUND:
                for v in INTERIOR:
                    if edge(h, v) in missing:
                        continue
                    fixed[edge(h, v)] = ground_signs[h] * local[h][v]

            has_67 = edge(6, 7) not in missing
            good_67 = []
            for sign_67 in ((1, -1) if has_67 else (None,)):
                good = True
                for v in INTERIOR:
                    neighbors = [0] + [
                        j
                        for j in NON_GROUND
                        if j != v and edge(v, j) not in missing
                    ]
                    assert len(neighbors) == 5
                    signs = {0: ground_signs[v]}
                    for j in neighbors:
                        if j == 0:
                            continue
                        e = edge(v, j)
                        signs[j] = sign_67 if e == edge(6, 7) else fixed[e]
                    if not force_rank2_balanced(chi, v, neighbors, signs):
                        good = False
                        break
                if good:
                    good_67.append(sign_67)

            assignment_multiplicity[(has_67, len(good_67))] += 1
            if not good_67:
                continue

            after[graph_type] += 1
            by_pattern_after["".join(map(str, pattern))] += 1
            by_67_after[(graph_type, has_67)] += 1
            missing_after[graph_type].add(tuple(sorted(missing)))
            order_types_after.add(order_index)

assert before == Counter({"C7": 208588, "C3+C4": 56356})
assert after == Counter({"C7": 10670, "C3+C4": 3504})
assert sum(after.values()) == 14174

EXPECTED_PATTERN_AFTER = {
    "145": 144,
    "156": 108,
    "234": 0,
    "235": 1770,
    "236": 3630,
    "237": 108,
    "245": 1390,
    "256": 3630,
    "345": 90,
    "346": 1390,
    "347": 144,
    "356": 1770,
    "456": 0,
}
assert {
    p: by_pattern_after[p]
    for p in EXPECTED_PATTERN_AFTER
} == EXPECTED_PATTERN_AFTER

assert by_67_after == Counter({
    ("C7", True): 7554,
    ("C7", False): 3116,
    ("C3+C4", True): 2364,
    ("C3+C4", False): 1140,
})
assert assignment_multiplicity == Counter({
    (True, 0): 144822,
    (True, 1): 9918,
    (False, 0): 105948,
    (False, 1): 4256,
})
# In particular, whenever edge 67 is present and the state survives, its sign is unique.
assert assignment_multiplicity[(True, 2)] == 0

assert {k: len(v) for k, v in missing_before.items()} == {"C7": 348, "C3+C4": 105}
assert {k: len(v) for k, v in missing_after.items()} == {"C7": 276, "C3+C4": 81}
assert len(order_types_after) == 1824

print("PASS")
print("generic H6 hull-sign survivors: 264944 = 208588 C7 + 56356 C3+C4")
print("after interior force-chirotope balance: 14174 = 10670 C7 + 3504 C3+C4")
print("eliminated: 250770")
print("surviving ground patterns: 11/13; patterns 234 and 456 are excluded")
print("surviving missing-graph embeddings: 276/360 C7 and 81/105 C3+C4")
print("surviving outer order types: 1824/1848")
print("states with edge 67 present: 9918; its sign is unique in every survivor")
