#!/usr/bin/env python3
"""Exact finite certificate for the short relative dependencies in the K8
four-cycle metric system used by Target C.

The computation works with integer cycle-flow vectors on L(K8).  Modular
rank is used only as an independence certificate: a nonzero minor mod p is
also a nonzero integer minor.  Every asserted dependence is separately
checked over Q with Fraction arithmetic.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

P = 1_000_003
VERTICES = tuple(range(8))
GROUND_ROOT = 0

segments = list(combinations(VERTICES, 2))
segment_index = {e: i for i, e in enumerate(segments)}
line_edges = []
line_edge_index = {}
for i, j in combinations(range(len(segments)), 2):
    if set(segments[i]) & set(segments[j]):
        line_edge_index[(i, j)] = len(line_edges)
        line_edges.append((i, j))
assert len(segments) == 28
assert len(line_edges) == 168


def seg(a, b):
    return segment_index[tuple(sorted((a, b)))]


def line_cycle(segment_ids):
    row = [0] * len(line_edges)
    ids = list(segment_ids)
    for x, y in zip(ids, ids[1:] + ids[:1]):
        if x < y:
            row[line_edge_index[(x, y)]] += 1
        else:
            row[line_edge_index[(y, x)]] -= 1
    return row


def k8_cycle(vs):
    vs = list(vs)
    return line_cycle([seg(vs[i], vs[(i + 1) % len(vs)]) for i in range(len(vs))])


def side_triangle(a, b, c):
    return line_cycle([seg(a, b), seg(b, c), seg(a, c)])


def star_triangle(r, a, b, c):
    return line_cycle([seg(r, a), seg(r, b), seg(r, c)])


SIDE = [side_triangle(*t) for t in combinations(VERTICES, 3)]
GROUND = [star_triangle(0, 1, i, j) for i, j in combinations(range(2, 8), 2)]
assert len(SIDE) == 56
assert len(GROUND) == 15

# One orientation representative of every undirected simple K8 four-cycle.
FOUR = []
DESC = []
seen = set()
for vertex_set in combinations(VERTICES, 4):
    a = min(vertex_set)
    rest = [x for x in vertex_set if x != a]
    for perm in permutations(rest):
        if perm[0] >= perm[-1]:
            continue
        d = (a,) + perm
        row = k8_cycle(d)
        key = min(tuple(row), tuple(-x for x in row))
        if key in seen:
            continue
        seen.add(key)
        FOUR.append(row)
        DESC.append(d)
assert len(FOUR) == 210


class ModBasis:
    def __init__(self, rows=()):
        self.rows = {}
        for row in rows:
            self.add(row)

    def reduce(self, row):
        r = [x % P for x in row]
        for pivot in sorted(self.rows):
            if r[pivot]:
                q = r[pivot]
                b = self.rows[pivot]
                r = [(x - q * y) % P for x, y in zip(r, b)]
        return r

    def add(self, row):
        r = self.reduce(row)
        pivot = next((i for i, x in enumerate(r) if x), None)
        if pivot is None:
            return False
        inv = pow(r[pivot], P - 2, P)
        r = [(x * inv) % P for x in r]
        self.rows[pivot] = r
        return True

    @property
    def rank(self):
        return len(self.rows)


class RationalBasis:
    def __init__(self, rows=()):
        self.rows = {}
        for row in rows:
            assert self.add(row)

    def reduce(self, row):
        r = [Fraction(x) for x in row]
        for pivot in sorted(self.rows):
            if r[pivot]:
                q = r[pivot]
                b = self.rows[pivot]
                r = [x - q * y for x, y in zip(r, b)]
        return r

    def add(self, row):
        r = self.reduce(row)
        pivot = next((i for i, x in enumerate(r) if x), None)
        if pivot is None:
            return False
        q = r[pivot]
        r = [x / q for x in r]
        self.rows[pivot] = r
        return True


side_basis = ModBasis(SIDE)
ground_basis = ModBasis(SIDE + GROUND)
all_basis = ModBasis(SIDE + FOUR)

# These modular ranks are exact over Q.  SIDE and SIDE+GROUND have as many
# rows as their modular ranks.  SIDE+FOUR consists of cycle flows on connected
# L(K8), whose rational cycle-space dimension is 168-28+1 = 141.
assert side_basis.rank == 56
assert ground_basis.rank == 71
assert all_basis.rank == 141
assert len(line_edges) - len(segments) + 1 == 141

# M = span(FOUR+SIDE)/span(SIDE), rank 85.
# Q = M/T, where T is the 15-dimensional ground star space, rank 70.
M = [side_basis.reduce(row) for row in FOUR]
Q = [ground_basis.reduce(row) for row in FOUR]
assert ModBasis(M).rank == 85
assert ModBasis(Q).rank == 70


def compress(vectors):
    cols = sorted({j for v in vectors for j, x in enumerate(v) if x % P})
    return [tuple(v[j] % P for j in cols) for v in vectors]


QC = compress(Q)


def projective_key(v):
    pivot = next((i for i, x in enumerate(v) if x), None)
    if pivot is None:
        return None
    inv = pow(v[pivot], P - 2, P)
    return tuple((x * inv) % P for x in v)


projective = {}
for i, v in enumerate(QC):
    key = projective_key(v)
    assert key is not None
    projective.setdefault(key, []).append(i)
assert len(projective) == 210
assert all(len(ids) == 1 for ids in projective.values())


def span2_key(a, b):
    rows = [list(a), list(b)]
    rr = 0
    n = len(a)
    for col in range(n):
        pivot = next((i for i in range(rr, 2) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rr], rows[pivot] = rows[pivot], rows[rr]
        inv = pow(rows[rr][col], P - 2, P)
        rows[rr] = [(x * inv) % P for x in rows[rr]]
        for i in range(2):
            if i != rr and rows[i][col]:
                q = rows[i][col]
                rows[i] = [(x - q * y) % P for x, y in zip(rows[i], rows[rr])]
        rr += 1
        if rr == 2:
            break
    assert rr == 2
    return tuple(tuple(row) for row in rows)


# Every dependent triple is visible as a three-point rank-two flat.  Because
# pairwise independence was certified mod P, this catches all 3-circuits.
flats = {}
for i, j in combinations(range(210), 2):
    key = span2_key(QC[i], QC[j])
    flats.setdefault(key, set()).update((i, j))
flat_sizes = Counter(len(s) for s in flats.values())
assert flat_sizes == Counter({2: 21840, 3: 35})
triples = [tuple(sorted(s)) for s in flats.values() if len(s) == 3]
assert len(triples) == 35

# The 35 triples are exactly the three four-cycles on each four-set
# {0,a,b,c}.  They are pairwise disjoint and cover 105 elements.
expected = []
for abc in combinations(range(1, 8), 3):
    U = {0, *abc}
    ids = tuple(i for i, d in enumerate(DESC) if set(d) == U)
    assert len(ids) == 3
    expected.append(tuple(sorted(ids)))
assert set(triples) == set(expected)
participation = Counter(i for tri in triples for i in tri)
assert len(participation) == 105
assert set(participation.values()) == {1}

# Modular dependence is not used to assert rational dependence.  Check the
# actual integer relation -C0+C1+C2 in SIDE+GROUND exactly over Q.
rational_ground = RationalBasis(SIDE + GROUND)
for tri in expected:
    a, b, c = tri
    relation = [-FOUR[a][j] + FOUR[b][j] + FOUR[c][j] for j in range(168)]
    assert all(x == 0 for x in rational_ground.reduce(relation))

# Stronger root-0 normal form.  The 105 four-cycles containing root 0 already
# span M (rank 85) and Q (rank 70).  Their Q-kernel therefore has dimension
# 35.  The 35 disjoint exact triple relations above are independent as
# coordinate relations, hence form the entire Q-kernel on these 105 columns.
root0 = [i for i, d in enumerate(DESC) if 0 in d]
assert len(root0) == 105
assert ModBasis([M[i] for i in root0]).rank == 85
assert ModBasis([Q[i] for i in root0]).rank == 70
assert len(root0) - 70 == 35

# Consequence: a subset of the root-0 columns has quotient nullity equal to
# the number of complete local triples it contains.  In particular 44 root-0
# columns can contain at most floor(44/3)=14 relative kernel directions, so
# they cannot capture all dim(T)=15 target directions.
assert 44 // 3 == 14

print("PASS: relative four-cycle 3-circuit structure")
print("M_rank", 85)
print("T_rank", 15)
print("Q_rank", 70)
print("four_cycles", 210)
print("projective_Q_points", 210)
print("rank2_flats_size2", flat_sizes[2])
print("rank2_flats_size3", flat_sizes[3])
print("three_circuit_elements", len(participation))
print("root0_four_cycles", len(root0))
print("root0_Q_kernel_dimension", len(root0) - 70)
print("root0_kernel_local_triples", len(expected))
print("max_complete_local_triples_in_44_root0_cycles", 44 // 3)

# Tetrahedral normal form for cycles avoiding root 0.  The 35 local block
# spans above form a direct sum in Q (35*2 = 70).  Every no-root four-cycle
# has one nonzero component in each of the four blocks indexed by the
# 3-subsets of its four vertices, and no component in any other block.
# Find a +-1 representative and exactify it over Q.
block_by_vertices = {}
for tri in expected:
    U = tuple(sorted(set(DESC[tri[0]]) - {0}))
    block_by_vertices[U] = tri
assert len(block_by_vertices) == 35

no0 = [i for i, d in enumerate(DESC) if 0 not in d]
assert len(no0) == 105
four_face_representations = {}
for e in no0:
    U = tuple(sorted(set(DESC[e])))
    faces = [tuple(x for x in U if x != omitted) for omitted in U]
    blocks = [block_by_vertices[tuple(sorted(face))] for face in faces]
    target = QC[e]
    found = None
    # 3^4 choices of local projective point, then 2^4 signs.
    for choices in product(*blocks):
        vecs = [QC[i] for i in choices]
        for signs in product((-1, 1), repeat=4):
            if all(sum(s * v[j] for s, v in zip(signs, vecs)) % P == target[j]
                   for j in range(len(target))):
                found = tuple(zip(choices, signs))
                break
        if found is not None:
            break
    assert found is not None
    # All four blocks are distinct and every selected Q vector is nonzero.
    assert len({tuple(sorted(set(DESC[i]) - {0})) for i, _ in found}) == 4
    # Exact rational Q equality: the difference is in SIDE+GROUND.
    difference = list(FOUR[e])
    for i, sign in found:
        difference = [x - sign * y for x, y in zip(difference, FOUR[i])]
    assert all(x == 0 for x in rational_ground.reduce(difference))
    four_face_representations[e] = found

print("no0_four_cycles", len(no0))
print("no0_exact_four_face_representations", len(four_face_representations))
print("no0_root0_representation_support", 4)
