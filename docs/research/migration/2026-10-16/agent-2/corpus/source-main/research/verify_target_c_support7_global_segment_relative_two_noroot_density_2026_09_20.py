#!/usr/bin/env python3
"""Exact two-no-root rank-density barrier for the Target-C four-cycle system.

Let M be the 85-dimensional span of the 210 simple K8 four-cycle rows modulo
automatic side-triangle rows, let T be the 15-dimensional ground-root star
space, and let Q=M/T.  The companion normal-form verifier proves that the 105
four-cycles containing root 0 split in Q into 35 independent rank-two local
blocks of three columns, while every four-cycle avoiding root 0 is supported on
exactly the four blocks corresponding to the triangular faces of its four-set.

This verifier proves the following restricted global rank-density inequality:

    3 * (r_M(A) - r_Q(A)) <= |A|

for every four-cycle family A containing at most two cycles that avoid root 0.
Consequently a sufficient family with relative rank 15 and at most two no-root
cycles has at least 45 rows.  In particular, every hypothetical sufficient
44-row family must contain at least three no-root four-cycles.

All ranks used to reject the only potentially violating local configurations
are computed over Q with Fraction arithmetic.  Finite-field arithmetic is not
used by this verifier for a proof decision.
"""

from fractions import Fraction
from itertools import combinations, permutations

VERTICES = tuple(range(8))
SEGMENTS = tuple(combinations(VERTICES, 2))
SEGMENT_INDEX = {e: i for i, e in enumerate(SEGMENTS)}
LINE_EDGES = []
LINE_EDGE_INDEX = {}
for i, j in combinations(range(len(SEGMENTS)), 2):
    if set(SEGMENTS[i]) & set(SEGMENTS[j]):
        LINE_EDGE_INDEX[(i, j)] = len(LINE_EDGES)
        LINE_EDGES.append((i, j))
assert len(SEGMENTS) == 28 and len(LINE_EDGES) == 168


def seg(a, b):
    return SEGMENT_INDEX[tuple(sorted((a, b)))]


def line_cycle(segment_ids):
    row = [0] * len(LINE_EDGES)
    ids = list(segment_ids)
    for x, y in zip(ids, ids[1:] + ids[:1]):
        if x < y:
            row[LINE_EDGE_INDEX[(x, y)]] += 1
        else:
            row[LINE_EDGE_INDEX[(y, x)]] -= 1
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

# One orientation representative of each undirected simple K8 four-cycle.
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
assert len(SIDE) == 56 and len(GROUND) == 15 and len(FOUR) == 210


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
        self.rows[pivot] = [x / q for x in r]
        return True

    @property
    def rank(self):
        return len(self.rows)


class RationalCoordinateBasis:
    def __init__(self, vectors):
        self.rows = {}
        self.dimension = len(vectors)
        for idx, row in enumerate(vectors):
            r = list(row)
            coeff = [Fraction(0)] * self.dimension
            coeff[idx] = Fraction(1)
            for pivot in sorted(self.rows):
                if r[pivot]:
                    q = r[pivot]
                    b, bc = self.rows[pivot]
                    r = [x - q * y for x, y in zip(r, b)]
                    coeff = [x - q * y for x, y in zip(coeff, bc)]
            pivot = next((i for i, x in enumerate(r) if x), None)
            assert pivot is not None
            q = r[pivot]
            r = [x / q for x in r]
            coeff = [x / q for x in coeff]
            self.rows[pivot] = (r, coeff)

    def coordinates(self, row):
        r = list(row)
        coeff = [Fraction(0)] * self.dimension
        for pivot in sorted(self.rows):
            if r[pivot]:
                q = r[pivot]
                b, bc = self.rows[pivot]
                r = [x - q * y for x, y in zip(r, b)]
                coeff = [x + q * y for x, y in zip(coeff, bc)]
        assert not any(r)
        return coeff


def exact_rank(rows):
    basis = {}
    for row in rows:
        r = [Fraction(x) for x in row]
        for pivot in sorted(basis):
            if r[pivot]:
                q = r[pivot]
                b = basis[pivot]
                r = [x - q * y for x, y in zip(r, b)]
        pivot = next((i for i, x in enumerate(r) if x), None)
        if pivot is None:
            continue
        q = r[pivot]
        basis[pivot] = [x / q for x in r]
    return len(basis)


# Build an exact M = Q (+) T coordinate system.  The first 70 coordinates are
# two chosen root-0 columns from each of the 35 local Q blocks; the last 15 are
# the ground-star basis of T.
side = RationalBasis(SIDE)
M_residual = [side.reduce(row) for row in FOUR]
T_residual = [side.reduce(row) for row in GROUND]
assert RationalBasis(T_residual).rank == 15

BLOCK_LABELS = list(combinations(range(1, 8), 3))
BLOCKS = []
for face in BLOCK_LABELS:
    ids = tuple(i for i, d in enumerate(DESC) if set(d) == {0, *face})
    assert len(ids) == 3
    BLOCKS.append(ids)
SECTION_IDS = [e for block in BLOCKS for e in block[:2]]
assert len(SECTION_IDS) == 70

coord_basis = RationalCoordinateBasis(
    [M_residual[e] for e in SECTION_IDS] + T_residual
)
COORD = [coord_basis.coordinates(row) for row in M_residual]
assert all(x.denominator == 1 for c in COORD for x in c)
assert {int(x) for c in COORD for x in c} <= {-2, -1, 0, 1, 2}
QCOORD = [tuple(int(x) for x in c[:70]) for c in COORD]
MCOORD = [tuple(int(x) for x in c) for c in COORD]
assert exact_rank(MCOORD) == 85
assert exact_rank(QCOORD) == 70

# Exact block normal form: the three root-0 columns in every block are
# (1,0), (0,1), and (1,-1) in Q.  Different blocks have disjoint support.
LOCAL = ((1, 0), (0, 1), (1, -1))
for b, ids in enumerate(BLOCKS):
    for j, e in enumerate(ids):
        support = [(QCOORD[e][2 * h], QCOORD[e][2 * h + 1]) for h in range(35)]
        assert support[b] == LOCAL[j]
        assert all(v == (0, 0) for h, v in enumerate(support) if h != b)

NO_ROOT = [i for i, d in enumerate(DESC) if 0 not in d]
assert len(NO_ROOT) == 105
BLOCK_INDEX = {face: i for i, face in enumerate(BLOCK_LABELS)}
QCOMP = {}
for e in NO_ROOT:
    comp = tuple((QCOORD[e][2 * b], QCOORD[e][2 * b + 1]) for b in range(35))
    touched = {b for b, v in enumerate(comp) if v != (0, 0)}
    expected = {
        BLOCK_INDEX[tuple(face)]
        for face in combinations(sorted(set(DESC[e])), 3)
    }
    assert touched == expected
    assert len(touched) == 4
    QCOMP[e] = comp

# Root-0 block states.  p counts selected columns in an incomplete block.
# A full block has cost 3 but contributes one local Q-kernel direction, so its
# 3-cost cancels against 3 times that potential relative direction.
STATES = []
for mask in range(8):
    chosen = [j for j in range(3) if (mask >> j) & 1]
    cost = len(chosen)
    complete = mask == 7
    if cost == 0:
        kind, line, p = 0, None, 0
    elif cost == 1:
        kind, line, p = 1, LOCAL[chosen[0]], 1
    else:
        kind, line, p = 2, None, 0 if complete else 2
    STATES.append((mask, cost, complete, kind, line, p))


def residual_rank(externals, touched, state_tuple):
    """Exact rank in Q modulo the chosen root-0 block spans."""
    rows = [[] for _ in externals]
    for b, state_id in zip(touched, state_tuple):
        _mask, _cost, _complete, kind, line, _p = STATES[state_id]
        vals = [QCOMP[e][b] for e in externals]
        if kind == 2:
            continue
        if kind == 0:
            for row, (x, y) in zip(rows, vals):
                row.extend((x, y))
        else:
            lx, ly = line
            for row, (x, y) in zip(rows, vals):
                row.append(lx * y - ly * x)
    return exact_rank(rows)


def selected_local_rows(externals, touched, state_tuple):
    selected = list(externals)
    for b, state_id in zip(touched, state_tuple):
        mask = STATES[state_id][0]
        ids = BLOCKS[b]
        selected.extend(ids[j] for j in range(3) if (mask >> j) & 1)
    return selected


def state_tuples_with_p_at_most(block_count, limit):
    current = []

    def rec(pos, p):
        if pos == block_count:
            yield tuple(current)
            return
        for state_id, state in enumerate(STATES):
            np = p + state[5]
            if np > limit:
                continue
            current.append(state_id)
            yield from rec(pos + 1, np)
            current.pop()

    yield from rec(0, 0)


def actual_defect(externals, touched, state_tuple):
    selected = selected_local_rows(externals, touched, state_tuple)
    m_rank = exact_rank([MCOORD[e] for e in selected])
    q_rank = exact_rank([QCOORD[e] for e in selected])
    delta = m_rank - q_rank
    return len(selected) - 3 * delta, m_rank, q_rank, selected


# All no-root columns are one S_7 orbit.
def cycle_key(desc):
    d = list(desc)
    return tuple(sorted(tuple(sorted((d[i], d[(i + 1) % 4]))) for i in range(4)))


KEY_TO_ID = {cycle_key(DESC[e]): e for e in NO_ROOT}
KEY = {e: cycle_key(DESC[e]) for e in NO_ROOT}
PERMS = list(permutations(range(1, 8)))


def map_key(key, pmap):
    return tuple(sorted(tuple(sorted((pmap[a], pmap[b]))) for a, b in key))


def orbit_of_tuple(items):
    out = set()
    keys = [KEY[e] for e in items]
    for perm in PERMS:
        pmap = {i + 1: perm[i] for i in range(7)}
        image = tuple(sorted(KEY_TO_ID[map_key(key, pmap)] for key in keys))
        out.add(image)
    return out


one_orbit = orbit_of_tuple((NO_ROOT[0],))
assert len(one_orbit) == 105

# t=1.  For local Q-kernel dimension K=c+k,
# |A_local|-3K = 1+p-3k.  A violation can occur only for k=1 and p<=1.
one_rep = min(NO_ROOT)
one_touched = sorted(b for b, v in enumerate(QCOMP[one_rep]) if v != (0, 0))
one_potential = 0
one_actual_min = None
for states in state_tuples_with_p_at_most(4, 1):
    c = sum(STATES[s][2] for s in states)
    p = sum(STATES[s][5] for s in states)
    k = 1 - residual_rank((one_rep,), one_touched, states)
    crude_defect = 1 + p - 3 * k
    if crude_defect >= 0:
        continue
    one_potential += 1
    defect, _mr, _qr, _selected = actual_defect((one_rep,), one_touched, states)
    assert defect >= 0
    one_actual_min = defect if one_actual_min is None else min(one_actual_min, defect)
assert one_potential == 5
assert one_actual_min == 2

# t=2.  Classify all C(105,2)=5460 unordered no-root pairs into S_7 orbits.
remaining = set(combinations(NO_ROOT, 2))
pair_orbits = []
while remaining:
    rep = min(remaining)
    orbit = orbit_of_tuple(rep)
    assert orbit <= remaining
    pair_orbits.append((rep, orbit))
    remaining -= orbit
assert not remaining
assert len(pair_orbits) == 7
assert sorted(len(orbit) for _rep, orbit in pair_orbits) == [105, 315, 630, 630, 1260, 1260, 1260]
assert sum(len(orbit) for _rep, orbit in pair_orbits) == 5460

pair_records = []
pair_potential = 0
pair_actual_min = None
for rep, orbit in pair_orbits:
    touched = sorted(
        b
        for b in range(35)
        if any(QCOMP[e][b] != (0, 0) for e in rep)
    )
    assert len(touched) in (4, 7, 8)
    tested = 0
    potential = 0
    for states in state_tuples_with_p_at_most(len(touched), 3):
        tested += 1
        c = sum(STATES[s][2] for s in states)
        p = sum(STATES[s][5] for s in states)
        k = 2 - residual_rank(rep, touched, states)
        # |A_local|-3K = 2+p-3k.  If this is nonnegative then
        # delta<=K already proves the desired inequality, so only negative
        # cases need an exact M-rank calculation.
        crude_defect = 2 + p - 3 * k
        if crude_defect >= 0:
            continue
        potential += 1
        pair_potential += 1
        defect, _mr, _qr, _selected = actual_defect(rep, touched, states)
        assert defect >= 0
        pair_actual_min = defect if pair_actual_min is None else min(pair_actual_min, defect)
    pair_records.append((len(orbit), len(touched), tested, potential))

assert pair_potential == 1684
assert pair_actual_min == 2
assert sorted(pair_records) == sorted([
    (1260, 7, 36080, 185),
    (1260, 8, 103168, 315),
    (315, 8, 103168, 315),
    (630, 8, 103168, 315),
    (1260, 8, 103168, 315),
    (105, 4, 1072, 13),
    (630, 7, 36080, 226),
])

# Prepare the next finite layer without using it in the theorem above.  The
# C(105,3)=187460 unordered no-root triples have only 77 S_7 orbits.
remaining_triples = set(combinations(NO_ROOT, 3))
triple_orbits = []
triple_touched_counts = []
while remaining_triples:
    rep = min(remaining_triples)
    orbit = orbit_of_tuple(rep)
    assert orbit <= remaining_triples
    touched = sum(
        any(QCOMP[e][b] != (0, 0) for e in rep)
        for b in range(35)
    )
    triple_orbits.append((rep, orbit))
    triple_touched_counts.append(touched)
    remaining_triples -= orbit
assert len(triple_orbits) == 77
assert sum(len(orbit) for _rep, orbit in triple_orbits) == 187460
assert min(triple_touched_counts) == 4
assert max(triple_touched_counts) == 12

print("PASS: relative four-cycle density for at most two no-root cycles")
print("M_rank", 85)
print("T_rank", 15)
print("Q_rank", 70)
print("root0_blocks", 35)
print("no_root_cycles", 105)
print("one_no_root_orbits", 1)
print("one_no_root_potential_negative_states", one_potential)
print("one_no_root_min_exact_defect", one_actual_min)
print("two_no_root_pair_orbits", len(pair_orbits))
print("two_no_root_orbit_sizes", sorted(len(o) for _r, o in pair_orbits))
print("two_no_root_potential_negative_states", pair_potential)
print("two_no_root_min_exact_defect", pair_actual_min)
print("three_no_root_orbits_for_next_layer", len(triple_orbits))
print("three_no_root_touched_block_range", (min(triple_touched_counts), max(triple_touched_counts)))
print("corollary_min_no_root_cycles_in_any_sufficient_44_family", 3)
