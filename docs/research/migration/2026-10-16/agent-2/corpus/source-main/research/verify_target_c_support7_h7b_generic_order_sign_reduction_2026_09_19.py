#!/usr/bin/env python3
"""Exact certificate for the generic interior-ground support-seven H7b reduction.

This file repairs the certificate referenced by
`target_c_support7_h7b_generic_order_sign_reduction_2026-09-19.md`.
It uses standard-library integer/Fraction arithmetic only.

It checks the 57 admissible ground-ray slot vectors, all labelled C7/C3+C4
missing graphs, the local 2+3 force-sign consistency census, the D7/global-sign
quotient to 184 generic H7b order/sign orbits, and eight exact signed-distance
certificates.  The latter reduce 184 to 176 orbits (112 C7 + 64 C3+C4).
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

HULL = tuple(range(1, 8))
ALL_VERTICES = tuple(range(8))
DIST_EDGES = tuple(combinations(ALL_VERTICES, 2))
DIST_INDEX = {e: k for k, e in enumerate(DIST_EDGES)}


def edge(a, b):
    return tuple(sorted((a, b)))


def ray_order(i):
    return tuple(((i - 1 + t) % 7) + 1 for t in range(1, 7))


def chi_from_slot(i, j, k):
    pos = ray_order(i).index(j) + 1
    return 1 if pos <= k else -1


SLOT_VECTORS = []
for ks in product(range(1, 6), repeat=7):
    if all(
        chi_from_slot(i, j, ks[i - 1]) == -chi_from_slot(j, i, ks[j - 1])
        for i, j in combinations(HULL, 2)
    ):
        SLOT_VECTORS.append(tuple(ks))
assert len(SLOT_VECTORS) == 57


def canonical_cycle(cycle):
    cycle = tuple(cycle)
    images = []
    for seq in (cycle, cycle[::-1]):
        for k in range(len(seq)):
            images.append(seq[k:] + seq[:k])
    return min(images)


def cycle_edge_sets(nodes):
    nodes = tuple(nodes)
    a = min(nodes)
    rest = tuple(x for x in nodes if x != a)
    seen = set()
    for p in permutations(rest):
        cyc = canonical_cycle((a,) + p)
        if cyc in seen:
            continue
        seen.add(cyc)
        yield frozenset(edge(cyc[i], cyc[(i + 1) % len(cyc)]) for i in range(len(cyc)))


def complement_graphs():
    for missing in cycle_edge_sets(HULL):
        yield "C7", missing
    for tri in combinations(HULL, 3):
        tri = frozenset(tri)
        quad = frozenset(HULL) - tri
        tri_edges = frozenset(edge(a, b) for a, b in combinations(sorted(tri), 2))
        for four_cycle in cycle_edge_sets(quad):
            yield "C3+C4", frozenset(set(tri_edges) | set(four_cycle))


MISSING_GRAPHS = list(complement_graphs())
assert Counter(t for t, _ in MISSING_GRAPHS) == Counter({"C7": 360, "C3+C4": 105})


def local_raw(i, k, missing):
    order = ray_order(i)
    raw = order[:k] + (0,) + order[k:]
    absent = {j for j in HULL if edge(i, j) in missing}
    out = tuple(r for r in raw if r not in absent)
    assert len(out) == 5
    return out


def base_signs(i, k, missing):
    raw = local_raw(i, k, missing)
    plus = {raw[1], raw[3]}
    return {r: (1 if r in plus else -1) for r in raw}


def solve_edge_signs(missing, slots):
    relation = [e for e in combinations(HULL, 2) if e not in missing]
    base = {i: base_signs(i, slots[i - 1], missing) for i in HULL}
    adj = {i: [] for i in HULL}
    for i, j in relation:
        parity = 0 if base[i][j] == base[j][i] else 1
        adj[i].append((j, parity))
        adj[j].append((i, parity))
    assignment = {1: 0}
    stack = [1]
    while stack:
        u = stack.pop()
        for w, parity in adj[u]:
            value = assignment[u] ^ parity
            if w in assignment:
                if assignment[w] != value:
                    return None
            else:
                assignment[w] = value
                stack.append(w)
    assert len(assignment) == 7
    signs = {}
    for i in HULL:
        multiplier = -1 if assignment[i] else 1
        for r, s in base[i].items():
            e = edge(i, r)
            value = s * multiplier
            if e in signs:
                assert signs[e] == value
            else:
                signs[e] = value
    assert len(signs) == 21
    return signs


VALID_STATES = []
for typ, missing in MISSING_GRAPHS:
    for slots in SLOT_VECTORS:
        signs = solve_edge_signs(missing, slots)
        if signs is not None:
            VALID_STATES.append((typ, missing, slots, signs))
assert len(VALID_STATES) == 2166
assert Counter(t for t, *_ in VALID_STATES) == Counter({"C7": 1368, "C3+C4": 798})
assert 2 * len(VALID_STATES) == 4332


def rot_vertex(i, r):
    return ((i - 1 + r) % 7) + 1


def ref_vertex(i, r):
    return ((r - (i - 1)) % 7) + 1


def transform_state(missing, slots, signs, kind, r, complement):
    f = (lambda i: rot_vertex(i, r)) if kind == "rot" else (lambda i: ref_vertex(i, r))
    m2 = frozenset(edge(f(a), f(b)) for a, b in missing)
    k2 = [None] * 7
    for i in HULL:
        ni = f(i)
        k2[ni - 1] = slots[i - 1] if kind == "rot" else 6 - slots[i - 1]
    s2 = {}
    for (a, b), sig in signs.items():
        aa = 0 if a == 0 else f(a)
        bb = 0 if b == 0 else f(b)
        s2[edge(aa, bb)] = -sig if complement else sig
    positive = tuple(sorted(e for e, sig in s2.items() if sig > 0))
    return tuple(sorted(m2)), tuple(k2), positive


def canonical_key(missing, slots, signs):
    return min(
        transform_state(missing, slots, signs, kind, r, complement)
        for kind in ("rot", "ref")
        for r in range(7)
        for complement in (False, True)
    )


ORBIT_MEMBERS = defaultdict(list)
for state in VALID_STATES:
    typ, missing, slots, signs = state
    ORBIT_MEMBERS[canonical_key(missing, slots, signs)].append(state)
assert len(ORBIT_MEMBERS) == 184
assert Counter(v[0][0] for v in ORBIT_MEMBERS.values()) == Counter({"C7": 120, "C3+C4": 64})
ORBIT_KEYS = tuple(sorted(ORBIT_MEMBERS))
ORBIT_INDEX = {key: i for i, key in enumerate(ORBIT_KEYS)}


def vec():
    return [Fraction(0) for _ in DIST_EDGES]


def add_term(out, coefficient, e):
    out[DIST_INDEX[edge(*e)]] += Fraction(coefficient)


def triangle_residual(long_edge, side1, side2):
    out = vec()
    add_term(out, 1, long_edge)
    add_term(out, -1, side1)
    add_term(out, -1, side2)
    return out


def quadrilateral_residual(kind, a, b, c, d):
    out = vec()
    if kind == "Q1":
        for coefficient, e in ((1, (a,b)), (1, (c,d)), (-1, (a,c)), (-1, (b,d))):
            add_term(out, coefficient, e)
    elif kind == "Q2":
        for coefficient, e in ((1, (a,d)), (1, (b,c)), (-1, (a,c)), (-1, (b,d))):
            add_term(out, coefficient, e)
    else:
        raise ValueError(kind)
    return out


def negative_type_residual(coeffs):
    assert len(coeffs) == 8 and sum(coeffs) == 0 and any(coeffs)
    out = vec()
    for i, j in combinations(range(8), 2):
        add_term(out, 2 * coeffs[i] * coeffs[j], (i, j))
    return out


def residual(desc):
    kind = desc[0]
    if kind == "T":
        return triangle_residual(*desc[1:])
    if kind in ("Q1", "Q2"):
        return quadrilateral_residual(*desc)
    if kind == "N":
        return negative_type_residual(desc[1])
    raise ValueError(desc)


def add_scaled(dst, src, scale):
    scale = Fraction(scale)
    for k, value in enumerate(src):
        dst[k] += scale * value


def signed_trace(missing, signs):
    out = vec()
    present = {edge(0, i) for i in HULL} | {e for e in combinations(HULL, 2) if e not in missing}
    assert present == set(signs)
    for e in present:
        add_term(out, signs[e], e)
    return out


def signs_from_positive(missing, positive):
    present = {edge(0, i) for i in HULL} | {e for e in combinations(HULL, 2) if e not in missing}
    positive = {edge(*e) for e in positive}
    assert positive <= present
    return {e: (1 if e in positive else -1) for e in present}


TRACE_CASES = [
    {
        "slots": (1, 1, 5, 5, 4, 3, 2),
        "missing": ((1,2),(1,7),(2,3),(3,4),(4,5),(5,6),(6,7)),
        "positive": ((0,5),(0,7),(1,3),(1,5),(2,4),(2,6),(3,6),(4,7)),
        "cert": [
            (Fraction(226,525), ('T',(1,4),(0,1),(0,4))), (Fraction(73,525), ('T',(0,6),(0,1),(1,6))),
            (Fraction(113,525), ('T',(2,6),(0,2),(0,6))), (Fraction(3,35), ('T',(0,7),(0,2),(2,7))),
            (Fraction(8,105), ('T',(0,5),(0,3),(3,5))), (Fraction(3,35), ('T',(3,7),(0,3),(0,7))),
            (Fraction(467,1050), ('Q2',1,2,4,5)), (Fraction(233,1050), ('Q2',1,2,6,7)),
            (Fraction(124,175), ('Q1',1,3,4,7)), (Fraction(68,75), ('Q1',1,5,6,7)),
            (Fraction(4,75), ('Q2',1,5,6,7)), (Fraction(323,525), ('Q2',3,4,5,6)),
            (Fraction(299,525), ('Q2',4,5,6,7)), (Fraction(4,105), ('N',(-1,-1,0,1,1,0,0,0))),
            (Fraction(73,2100), ('N',(-1,-1,1,1,0,0,1,-1))), (Fraction(29,700), ('N',(-1,0,0,1,0,0,1,-1))),
            (Fraction(1,70), ('N',(-1,0,0,1,0,1,-1,0))), (Fraction(1,210), ('N',(-1,0,0,1,0,1,0,-1))),
            (Fraction(47,700), ('N',(-1,0,0,1,1,-1,0,0))), (Fraction(1,30), ('N',(-1,0,1,0,1,-1,0,0))),
            (Fraction(43,210), ('N',(-1,0,1,0,1,-1,1,-1))), (Fraction(22,525), ('N',(-1,0,1,0,1,0,0,-1))),
            (Fraction(29,1050), ('N',(-1,1,-1,1,0,-1,1,0))), (Fraction(1,210), ('N',(-1,1,-1,1,1,0,-1,0))),
            (Fraction(113,1050), ('N',(-1,1,0,1,-1,0,1,-1))), (Fraction(17,210), ('N',(-1,1,0,1,0,-1,0,0))),
            (Fraction(1,420), ('N',(-1,1,1,-1,1,-1,0,0))), (Fraction(34,525), ('N',(-1,1,1,0,0,-1,1,-1))),
        ],
    },
    {
        "slots": (1,3,5,4,3,3,2),
        "missing": ((1,2),(1,7),(2,3),(3,4),(4,5),(5,6),(6,7)),
        "positive": ((0,4),(0,7),(1,3),(1,5),(2,5),(2,6),(3,6),(4,7)),
        "cert": [
            (Fraction(1,2), ('T',(2,6),(0,2),(0,6))), (Fraction(1,5), ('T',(3,5),(0,3),(0,5))),
            (Fraction(1,10), ('T',(2,5),(2,3),(3,5))), (Fraction(1,4), ('Q2',1,2,5,7)),
            (Fraction(7,20), ('Q2',1,3,4,5)), (Fraction(1,10), ('Q1',1,3,4,7)),
            (Fraction(3,10), ('Q1',1,3,5,7)), (Fraction(1,4), ('Q2',1,3,6,7)),
            (Fraction(13,20), ('Q1',1,5,6,7)), (Fraction(1,4), ('Q1',2,3,4,5)),
            (Fraction(1,20), ('Q2',2,3,4,5)), (Fraction(1,2), ('Q2',3,4,5,6)),
            (Fraction(1,20), ('N',(-1,0,0,1,0,-1,1,0))), (Fraction(7,40), ('N',(-1,0,1,0,-1,1,1,-1))),
            (Fraction(1,40), ('N',(-1,0,1,0,0,0,1,-1))), (Fraction(1,20), ('N',(-1,0,1,1,-1,0,1,-1))),
            (Fraction(1,8), ('N',(-1,1,-1,1,0,0,0,0))), (Fraction(3,40), ('N',(-1,1,0,0,0,1,-1,0))),
            (Fraction(3,40), ('N',(-1,1,0,1,-1,0,1,-1))), (Fraction(1,20), ('N',(-1,1,0,1,-1,1,-1,0))),
            (Fraction(1,40), ('N',(-1,1,0,1,-1,1,0,-1))), (Fraction(1,40), ('N',(-1,1,0,1,0,0,0,-1))),
            (Fraction(1,8), ('N',(-1,1,1,0,-1,1,0,-1))),
        ],
    },
    {
        "slots": (3,3,3,3,3,3,3),
        "missing": ((1,2),(1,7),(2,3),(3,4),(4,5),(5,6),(6,7)),
        "positive": ((1,4),(1,5),(2,5),(2,6),(3,6),(3,7),(4,7)),
        "cert": [
            (Fraction(73,124), ('T',(1,4),(0,1),(0,4))), (Fraction(26,31), ('T',(1,5),(0,1),(0,5))),
            (Fraction(63,124), ('T',(2,5),(0,2),(0,5))), (Fraction(55,124), ('T',(2,6),(0,2),(0,6))),
            (Fraction(7,62), ('T',(2,7),(0,2),(0,7))), (Fraction(43,124), ('T',(4,7),(0,4),(0,7))),
            (Fraction(55,124), ('Q1',1,2,3,7)), (Fraction(2,31), ('Q2',1,5,6,7)),
            (Fraction(1,62), ('Q1',2,3,4,5)), (Fraction(53,124), ('Q2',3,4,5,6)),
            (Fraction(1,31), ('Q1',4,5,6,7)), (Fraction(15,496), ('N',(-1,-1,-1,1,1,-1,1,1))),
            (Fraction(19,124), ('N',(-1,-1,0,1,0,-1,1,1))), (Fraction(1,496), ('N',(-1,-1,1,0,-1,1,1,0))),
            (Fraction(1,124), ('N',(-1,-1,1,0,0,0,1,0))), (Fraction(13,124), ('N',(-1,-1,1,1,-1,0,1,0))),
            (Fraction(29,496), ('N',(-1,-1,1,1,-1,1,1,-1))), (Fraction(11,248), ('N',(-1,0,-1,0,1,1,0,0))),
            (Fraction(21,248), ('N',(-1,0,-1,1,1,-1,0,1))), (Fraction(1,31), ('N',(-1,0,1,0,-1,1,1,-1))),
            (Fraction(3,62), ('N',(-1,1,-1,0,1,0,-1,1))), (Fraction(29,496), ('N',(-1,1,-1,1,1,-1,-1,1))),
            (Fraction(1,124), ('N',(-1,1,0,1,-1,-1,0,1))), (Fraction(1,496), ('N',(-1,1,1,0,-1,1,-1,0))),
            (Fraction(3,124), ('N',(-1,1,1,0,-1,1,0,-1))), (Fraction(1,496), ('N',(-1,1,1,1,-1,-1,-1,1))),
        ],
    },
]

COMMON_MISSING = ((1,4),(1,5),(2,5),(2,6),(3,6),(3,7),(4,7))
COMMON_POSITIVE = ((1,3),(1,6),(2,4),(2,7),(3,5),(4,6),(5,7))
COMMON_SLOTS = [(2,2,2,4,4,4,3),(2,2,3,4,4,3,3),(2,3,2,4,3,4,3),(2,3,3,4,3,3,3),(3,3,3,3,3,3,3)]
COMMON_CERT = [(Fraction(1,2), d) for d in [
    ('T',(1,3),(0,1),(0,3)), ('T',(1,6),(0,1),(0,6)), ('T',(2,4),(0,2),(0,4)),
    ('T',(2,7),(0,2),(0,7)), ('T',(3,5),(0,3),(0,5)), ('T',(4,6),(0,4),(0,6)),
    ('T',(5,7),(0,5),(0,7)), ('T',(1,3),(1,2),(2,3)), ('T',(2,7),(1,2),(1,7)),
    ('T',(1,6),(1,7),(6,7)), ('T',(2,4),(2,3),(3,4)), ('T',(3,5),(3,4),(4,5)),
    ('T',(4,6),(4,5),(5,6)), ('T',(5,7),(5,6),(6,7)),
]]
for slots in COMMON_SLOTS:
    TRACE_CASES.append({"slots":slots,"missing":COMMON_MISSING,"positive":COMMON_POSITIVE,"cert":COMMON_CERT})

TRACE_ORBIT_INDICES = set()
for case in TRACE_CASES:
    missing = frozenset(edge(*e) for e in case["missing"])
    signs = signs_from_positive(missing, case["positive"])
    slots = tuple(case["slots"])
    matches = [s for s in VALID_STATES if s[1] == missing and s[2] == slots and s[3] == signs]
    assert len(matches) == 1
    lhs = signed_trace(missing, signs)
    rhs = vec()
    for coefficient, desc in case["cert"]:
        coefficient = Fraction(coefficient)
        assert coefficient > 0
        add_scaled(rhs, residual(desc), coefficient)
    assert rhs == lhs
    TRACE_ORBIT_INDICES.add(ORBIT_INDEX[canonical_key(missing, slots, signs)])

assert len(TRACE_ORBIT_INDICES) == 8
assert all(ORBIT_MEMBERS[ORBIT_KEYS[i]][0][0] == "C7" for i in TRACE_ORBIT_INDICES)
remaining = [i for i in range(184) if i not in TRACE_ORBIT_INDICES]
assert Counter(ORBIT_MEMBERS[ORBIT_KEYS[i]][0][0] for i in remaining) == Counter({"C7":112,"C3+C4":64})
print("PASS: 57 slots; 4332 labelled sign states; 184 generic H7b orbits; 8 exact trace exclusions; 176 remain (112 C7 + 64 C3+C4).")