#!/usr/bin/env python3
"""Exact regressions for the degree-pure support-seven reciprocal reduction.

No floating point is used.  The script checks:
  * the two possible 4-regular relation-graph complements on seven vertices;
  * the collision-partition obstruction for both graph types;
  * the fully-convex H8 local 2+3 sign census;
  * reflection-orbit counts and ground sign-split counts;
  * exact signed-length certificates excluding the two H8 2+5 ground-split orbits.
"""

from collections import Counter
from itertools import combinations, permutations, product

V = tuple(range(8))
GROUND = 0
NON_GROUND = tuple(range(1, 8))
ALL_EDGES = {tuple(sorted(e)) for e in combinations(V, 2)}


def edge(a, b):
    return tuple(sorted((a, b)))


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
    # 2-regular simple graphs on seven labelled non-ground vertices are C7 or C3+C4.
    for missing in cycle_edge_sets(NON_GROUND):
        yield "C7", missing
    for tri in combinations(NON_GROUND, 3):
        tri = frozenset(tri)
        quad = frozenset(NON_GROUND) - tri
        tri_edges = frozenset(edge(a, b) for a, b in combinations(sorted(tri), 2))
        for four_cycle in cycle_edge_sets(quad):
            yield "C3+C4", frozenset(set(tri_edges) | set(four_cycle))


# ---------------------------------------------------------------------------
# Collision partitions.
# ---------------------------------------------------------------------------

def set_partitions(seq):
    seq = tuple(seq)
    if not seq:
        yield ()
        return
    x = seq[0]
    for tail in set_partitions(seq[1:]):
        yield ((x,),) + tail
        for i in range(len(tail)):
            blocks = [tuple(b) for b in tail]
            blocks[i] = tuple(sorted(blocks[i] + (x,)))
            yield tuple(blocks)


def canon_partition(partition):
    return tuple(sorted(tuple(sorted(block)) for block in partition))


def relation_from_missing(missing):
    return {
        edge(a, b)
        for a, b in combinations(NON_GROUND, 2)
        if edge(a, b) not in missing
    }


def partition_respects_no_parallel_rule(partition, relation):
    # Distinct dual-value classes A,B can have only a matching of relation edges
    # between them: otherwise one vertex sees two equal reciprocal differences and
    # hence two projectively parallel sides of one strict pentagon.
    for ia, A0 in enumerate(partition):
        A = set(A0)
        for B0 in partition[ia + 1 :]:
            B = set(B0)
            for a in A:
                if sum(edge(a, b) in relation for b in B) > 1:
                    return False
            for b in B:
                if sum(edge(a, b) in relation for a in A) > 1:
                    return False
    return True


PARTITIONS = {canon_partition(p) for p in set_partitions(NON_GROUND)}
assert len(PARTITIONS) == 877

REP_C7 = next(m for typ, m in complement_graphs() if typ == "C7")
REP_C3C4 = next(m for typ, m in complement_graphs() if typ == "C3+C4")
for missing in (REP_C7, REP_C3C4):
    relation = relation_from_missing(missing)
    good = [p for p in PARTITIONS if partition_respects_no_parallel_rule(p, relation)]
    assert len(good) == 2
    assert any(len(p) == 7 for p in good)  # all singleton classes
    assert any(len(p) == 1 for p in good)  # total collapse


# ---------------------------------------------------------------------------
# Fully convex H8 local sign census.
# ---------------------------------------------------------------------------

def raw_neighbor_order(i, missing):
    order = [(i + k) % 8 for k in range(1, 8)]
    order = [j for j in order if edge(i, j) not in missing]
    assert len(order) == 5
    return order


def sign_solutions(missing):
    reciprocal_edges = ALL_EDGES - set(missing)
    solutions = []
    for local_choice in product((2, 3), repeat=7):
        prescribed = {}
        consistent = True
        for i, positive_degree in zip(NON_GROUND, local_choice):
            order = raw_neighbor_order(i, missing)
            positive = (
                {order[1], order[3]}
                if positive_degree == 2
                else {order[0], order[2], order[4]}
            )
            for j in order:
                e = edge(i, j)
                value = j in positive
                if e in prescribed and prescribed[e] != value:
                    consistent = False
                    break
                prescribed[e] = value
            if not consistent:
                break
        if consistent:
            assert set(prescribed) == reciprocal_edges
            positive_edges = frozenset(e for e, value in prescribed.items() if value)
            solutions.append((local_choice, positive_edges))
    return reciprocal_edges, solutions


all_missing = list(complement_graphs())
assert sum(typ == "C7" for typ, _ in all_missing) == 360
assert sum(typ == "C3+C4" for typ, _ in all_missing) == 105

survivors = []
for typ, missing in all_missing:
    H, solutions = sign_solutions(missing)
    if not solutions:
        continue
    assert len(solutions) == 2
    assert solutions[0][1] == frozenset(H - set(solutions[1][1]))
    survivors.append((typ, missing, H, solutions))

assert sum(typ == "C7" for typ, *_ in survivors) == 24
assert sum(typ == "C3+C4" for typ, *_ in survivors) == 14


def reflect_vertex(i):
    return (-i) % 8


def reflect_edges(edges):
    return frozenset(edge(reflect_vertex(a), reflect_vertex(b)) for a, b in edges)


def edge_set_key(edges):
    return tuple(sorted(edges))


seen = set()
orbit_counts = Counter()
ground_split_orbits = Counter()
canonical_orbits = []
for typ, missing, _, _ in survivors:
    if missing in seen:
        continue
    reflected = reflect_edges(missing)
    orbit = {missing, reflected}
    seen.update(orbit)
    canonical = min(orbit, key=edge_set_key)
    H, solutions = sign_solutions(canonical)
    gp = sum(edge(0, i) in solutions[0][1] for i in NON_GROUND)
    smaller = min(gp, 7 - gp)
    orbit_counts[typ] += 1
    ground_split_orbits[(typ, smaller)] += 1
    canonical_orbits.append((typ, canonical, H, solutions, smaller))

assert orbit_counts == Counter({"C7": 15, "C3+C4": 8})
assert ground_split_orbits == Counter({("C7", 3): 13, ("C7", 2): 2, ("C3+C4", 3): 8})


# One further C7 3+4 reflection orbit is killed directly by the ground
# equilibrium: minority patterns {1,3,7} and {1,5,7} are reflections.
# The analytic proof is in the accompanying note; here we lock the finite census.
def ground_minority(positive):
    P = frozenset(i for i in NON_GROUND if edge(0, i) in positive)
    return P if len(P) <= 3 else frozenset(NON_GROUND) - P


projection_bad = {frozenset({1, 3, 7}), frozenset({1, 5, 7})}
projection_bad_orbits = 0
for typ, missing, _, solutions, smaller in canonical_orbits:
    if smaller != 3:
        continue
    patterns = {ground_minority(sol[1]) for sol in solutions}
    # Global sign complement does not change the minority set.
    assert len(patterns) == 1
    P = next(iter(patterns))
    reflected_P = frozenset(reflect_vertex(i) for i in P)
    if P in projection_bad or reflected_P in projection_bad:
        assert typ == "C7"
        projection_bad_orbits += 1
assert projection_bad_orbits == 1

# ---------------------------------------------------------------------------
# Two exact signed-length certificates for the H8 2+5 ground-split orbits.
# ---------------------------------------------------------------------------

def form(terms):
    out = Counter()
    for coefficient, e in terms:
        out[edge(*e)] += coefficient
    return Counter({e: c for e, c in out.items() if c})


def triangle(long_edge, side1, side2):
    # d(long) - d(side1) - d(side2) < 0 for a noncollinear triangle.
    return form(((1, long_edge), (-1, side1), (-1, side2)))


def quadrilateral(side1, side2, diag1, diag2):
    # For four cyclically ordered convex points, opposite-side sum minus
    # the two diagonals is strictly negative.
    return form(((1, side1), (1, side2), (-1, diag1), (-1, diag2)))


def add_scaled(dst, src, scale):
    for e, c in src.items():
        dst[e] += scale * c


def signed_length_form(H, positive):
    return Counter({e: (1 if e in positive else -1) for e in H})


M_A = frozenset({edge(1, 2), edge(1, 7), edge(2, 3), edge(3, 4), edge(4, 5), edge(5, 6), edge(6, 7)})
P_A = frozenset({edge(0, 3), edge(0, 5), edge(1, 4), edge(1, 6), edge(2, 5), edge(2, 7), edge(3, 6), edge(4, 7)})

M_B = frozenset({edge(1, 4), edge(1, 5), edge(2, 5), edge(2, 6), edge(3, 6), edge(3, 7), edge(4, 7)})
P_B = frozenset({edge(0, 2), edge(0, 6), edge(1, 3), edge(1, 7), edge(2, 4), edge(3, 5), edge(4, 6), edge(5, 7)})

actual_k2 = {(m, sol[0][1]) for typ, m, _, sol, k in canonical_orbits if typ == "C7" and k == 2}
assert actual_k2 == {(M_A, P_A), (M_B, P_B)}

# Case A: 6 L_A is a positive integer combination of strict negative residuals.
A_terms = [
    (6, triangle((1, 6), (0, 1), (0, 6))),
    (1, triangle((0, 3), (0, 2), (2, 3))),
    (1, triangle((0, 5), (0, 2), (2, 5))),
    (3, triangle((2, 7), (0, 2), (0, 7))),
    (1, triangle((0, 3), (0, 7), (3, 7))),
    (2, triangle((0, 5), (0, 7), (5, 7))),
    (1, triangle((2, 7), (1, 2), (1, 7))),
    (3, triangle((1, 4), (1, 3), (3, 4))),
    (2, triangle((3, 6), (1, 3), (1, 6))),
    (1, triangle((1, 7), (1, 5), (5, 7))),
    (1, triangle((2, 5), (2, 4), (4, 5))),
    (1, triangle((5, 6), (2, 5), (2, 6))),
    (1, triangle((2, 7), (2, 6), (6, 7))),
    (1, triangle((3, 6), (3, 4), (4, 6))),
    (2, triangle((3, 6), (3, 5), (5, 6))),
    (1, triangle((5, 6), (4, 5), (4, 6))),
    (2, triangle((4, 7), (4, 6), (6, 7))),
    (1, quadrilateral((1, 2), (0, 5), (0, 2), (1, 5))),
    (2, quadrilateral((1, 4), (0, 5), (0, 4), (1, 5))),
    (4, quadrilateral((0, 3), (4, 7), (0, 4), (3, 7))),
    (1, quadrilateral((2, 3), (1, 4), (1, 3), (2, 4))),
    (2, quadrilateral((4, 5), (1, 6), (1, 5), (4, 6))),
    (4, quadrilateral((3, 4), (2, 5), (2, 4), (3, 5))),
    (1, quadrilateral((3, 6), (2, 7), (2, 6), (3, 7))),
    (3, quadrilateral((2, 5), (6, 7), (2, 6), (5, 7))),
]

rhs_A = Counter()
for coefficient, residual in A_terms:
    add_scaled(rhs_A, residual, coefficient)
lhs_A = Counter({e: 6 * c for e, c in signed_length_form(ALL_EDGES - set(M_A), P_A).items()})
assert Counter({e: c for e, c in rhs_A.items() if c}) == lhs_A

# Case B: 2 L_B is a sum of fourteen strict negative residuals.
B_terms = [
    triangle((0, 2), (0, 1), (1, 2)),
    triangle((1, 3), (0, 1), (0, 3)),
    triangle((3, 5), (0, 3), (0, 5)),
    triangle((5, 7), (0, 5), (0, 7)),
    triangle((0, 6), (0, 7), (6, 7)),
    triangle((1, 3), (1, 2), (2, 3)),
    triangle((2, 4), (2, 3), (3, 4)),
    triangle((3, 5), (3, 4), (4, 5)),
    triangle((4, 6), (4, 5), (5, 6)),
    triangle((5, 7), (5, 6), (6, 7)),
    quadrilateral((2, 4), (0, 6), (0, 4), (2, 6)),
    quadrilateral((0, 2), (4, 7), (0, 4), (2, 7)),
    quadrilateral((2, 6), (1, 7), (1, 6), (2, 7)),
    quadrilateral((4, 6), (1, 7), (1, 6), (4, 7)),
]

rhs_B = Counter()
for residual in B_terms:
    add_scaled(rhs_B, residual, 1)
lhs_B = Counter({e: 2 * c for e, c in signed_length_form(ALL_EDGES - set(M_B), P_B).items()})
assert Counter({e: c for e, c in rhs_B.items() if c}) == lhs_B

print("PASS")
print("labelled H8 local-sign survivors: C7=24, C3+C4=14")
print("reflection orbits: C7=15, C3+C4=8")
print("ground split orbits before metric exclusion: C7 2+5=2, C7 3+4=13, C3+C4 3+4=8")
print("two exact 2+5 signed-length certificates: PASS")
print("ground-projection exclusion removes one further C7 3+4 reflection orbit")
print("remaining fully-convex H8 local-sign/metric orbits: 20")
