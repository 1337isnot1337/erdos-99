#!/usr/bin/env python3
"""Exact exchange barrier for the 45-four-cycle Target-C metric test.

Let F be the 45 simple K8 four-cycles used by
verify_target_c_support7_global_segment_45_four_cycle_metric_test_2026_09_19.py.
Modulo the 56 automatic triangle-side cycles, F is a basis of a 45-dimensional
space W/SIDE and the fifteen ground-root metric cycles occupy fifteen disjoint
three-coordinate blocks, one for each pair 2 <= i < j <= 7.

This verifier proves the following finite statement over Q:

    Any 44-element family chosen from all 210 undirected simple K8 four-cycles
    that spans the fifteen ground-root metric cycles modulo SIDE must contain
    at least five cycles outside F.

Equivalently, no 44-cycle complete metric test is obtainable from F by
introducing only 0, 1, 2, 3, or 4 external simple four-cycles.

The proof is exact. It uses fractions.Fraction for the W decomposition and
integer determinant tests for the final 1,266,300 four-outsider cases. There is
no floating-point arithmetic and no optimization solver.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, lcm

V = tuple(range(8))
SEGMENTS = tuple(combinations(V, 2))
SIDX = {e: i for i, e in enumerate(SEGMENTS)}

LEDGES = []
LIDX = {}
for i, j in combinations(range(len(SEGMENTS)), 2):
    if set(SEGMENTS[i]) & set(SEGMENTS[j]):
        LIDX[(i, j)] = len(LEDGES)
        LEDGES.append((i, j))
assert len(SEGMENTS) == 28
assert len(LEDGES) == 168


def seg(a, b):
    return SIDX[tuple(sorted((a, b)))]


def line_cycle(segment_vertices):
    row = [0] * len(LEDGES)
    seq = list(segment_vertices)
    for x, y in zip(seq, seq[1:] + seq[:1]):
        if x < y:
            row[LIDX[(x, y)]] += 1
        else:
            row[LIDX[(y, x)]] -= 1
    return row


def k8_cycle(vertices):
    vs = list(vertices)
    return line_cycle([
        seg(vs[i], vs[(i + 1) % len(vs)])
        for i in range(len(vs))
    ])


def side_triangle(a, b, c):
    return line_cycle((seg(a, b), seg(b, c), seg(a, c)))


def star_triangle(a, b, c, d):
    return line_cycle((seg(a, b), seg(a, c), seg(a, d)))


SIDE = [side_triangle(*t) for t in combinations(V, 3)]
GROUND = [
    star_triangle(0, 1, i, j)
    for i, j in combinations(range(2, 8), 2)
]

FOUR = []
FOUR_DESC = []
for i, j in combinations(range(2, 8), 2):
    desc = ((0, 1, i, j), (0, 1, j, i), (0, i, 1, j))
    rows = [k8_cycle(c) for c in desc]
    FOUR.extend(rows)
    FOUR_DESC.extend(desc)

    c1, c2, c3 = rows
    rhs = [
        -side_triangle(0, 1, i)[k]
        + side_triangle(0, 1, j)[k]
        - side_triangle(0, i, j)[k]
        - side_triangle(1, i, j)[k]
        + c1[k] - c2[k] - c3[k]
        for k in range(len(LEDGES))
    ]
    lhs = [2 * z for z in star_triangle(0, 1, i, j)]
    assert rhs == lhs

assert len(SIDE) == 56
assert len(GROUND) == 15
assert len(FOUR) == 45


class ExactRowBasis:
    """Independent exact row basis with coordinates in the input rows."""

    def __init__(self, rows):
        self.nbase = len(rows)
        self.basis = {}
        for k, row0 in enumerate(rows):
            row = [Fraction(x) for x in row0]
            rep = [Fraction(0)] * self.nbase
            rep[k] = Fraction(1)
            self._insert(row, rep)

    def _insert(self, row, rep):
        for pivot in sorted(self.basis):
            if row[pivot]:
                q = row[pivot]
                brow, brep = self.basis[pivot]
                row = [x - q * y for x, y in zip(row, brow)]
                rep = [x - q * y for x, y in zip(rep, brep)]
        pivot = next((i for i, x in enumerate(row) if x), None)
        if pivot is None:
            raise AssertionError("input rows are not independent")
        q = row[pivot]
        row = [x / q for x in row]
        rep = [x / q for x in rep]
        self.basis[pivot] = (row, rep)

    def decompose(self, row0):
        """Return (basis coefficients, residual outside the row span)."""
        row = [Fraction(x) for x in row0]
        coeff = [Fraction(0)] * self.nbase
        for pivot in sorted(self.basis):
            if row[pivot]:
                q = row[pivot]
                brow, brep = self.basis[pivot]
                row = [x - q * y for x, y in zip(row, brow)]
                coeff = [x + q * y for x, y in zip(coeff, brep)]
        return coeff, row


W_ROWS = SIDE + FOUR
W = ExactRowBasis(W_ROWS)
assert len(W.basis) == 101

GROUND_FCOORD = []
for block, g in enumerate(GROUND):
    coeff, residual = W.decompose(g)
    assert not any(residual)
    fc = tuple(coeff[56:])
    expected = [Fraction(0)] * 45
    expected[3 * block:3 * block + 3] = (
        Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2)
    )
    assert list(fc) == expected
    GROUND_FCOORD.append(fc)

ALL_FOUR = []
seen_rows = []
for vertices in combinations(V, 4):
    a = min(vertices)
    rest = [x for x in vertices if x != a]
    for perm in permutations(rest):
        if perm[0] >= perm[-1]:
            continue
        desc = (a,) + perm
        row = k8_cycle(desc)
        if any(row == q or all(x == -y for x, y in zip(row, q)) for q in seen_rows):
            continue
        seen_rows.append(row)
        ALL_FOUR.append((desc, row))
assert len(ALL_FOUR) == 210


def same_unoriented(row, other):
    return row == other or all(x == -y for x, y in zip(row, other))


OUTSIDE = []
for desc, row in ALL_FOUR:
    if any(same_unoriented(row, f) for f in FOUR):
        continue
    coeff, residual = W.decompose(row)
    assert any(residual)
    OUTSIDE.append({
        "desc": desc,
        "row": row,
        "fcoord": tuple(coeff[56:]),
        "residual": tuple(residual),
    })
assert len(OUTSIDE) == 165


def primitive_integer_vector(vec):
    den = 1
    for x in vec:
        den = lcm(den, x.denominator)
    vals = [int(x * den) for x in vec]
    g = 0
    for x in vals:
        g = gcd(g, abs(x))
    if g:
        vals = [x // g for x in vals]
    first = next((x for x in vals if x), 0)
    if first < 0:
        vals = [-x for x in vals]
    return tuple(vals)


RESIDUAL_CLASS = {}
for idx, item in enumerate(OUTSIDE):
    key = primitive_integer_vector(item["residual"])
    assert any(key)
    RESIDUAL_CLASS.setdefault(key, []).append(idx)

class_sizes = Counter(len(v) for v in RESIDUAL_CLASS.values())
assert class_sizes == Counter({1: 45, 2: 60})


def proportional_to_ground_block(vec, block):
    a, b, c = vec[3 * block:3 * block + 3]
    return a != 0 and b == -a and c == -a


pair_checks = 0
for ids in RESIDUAL_CLASS.values():
    if len(ids) != 2:
        continue
    i, j = ids
    zi = OUTSIDE[i]["residual"]
    zj = OUTSIDE[j]["residual"]
    pivot = next(k for k, x in enumerate(zj) if x)
    lam = zi[pivot] / zj[pivot]
    assert all(x == lam * y for x, y in zip(zi, zj))
    h = tuple(
        x - lam * y
        for x, y in zip(OUTSIDE[i]["fcoord"], OUTSIDE[j]["fcoord"])
    )
    for block in range(15):
        pair_checks += 1
        assert not proportional_to_ground_block(h, block)
assert pair_checks == 60 * 15 == 900

CLASS_ITEMS = list(RESIDUAL_CLASS.items())
DIRECTIONS = [key for key, _ids in CLASS_ITEMS]
NONZERO_COLS = sorted({i for v in DIRECTIONS for i, x in enumerate(v) if x})
COMPACT_DIRS = [tuple(v[i] for i in NONZERO_COLS) for v in DIRECTIONS]


def canonical_rank_two_span(v1, v2):
    rows = [[Fraction(x) for x in v1], [Fraction(x) for x in v2]]
    r = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(r, 2) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        q = rows[r][col]
        rows[r] = [x / q for x in rows[r]]
        for i in range(2):
            if i == r or not rows[i][col]:
                continue
            q = rows[i][col]
            rows[i] = [x - q * y for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == 2:
            break
    if r < 2:
        return None
    return tuple(tuple(x for x in row) for row in rows)


RANK2_FLATS = {}
for i, j in combinations(range(len(COMPACT_DIRS)), 2):
    key = canonical_rank_two_span(COMPACT_DIRS[i], COMPACT_DIRS[j])
    if key is not None:
        RANK2_FLATS.setdefault(key, set()).update((i, j))

E4_CANDIDATES = set()
for ids in RESIDUAL_CLASS.values():
    for E in combinations(ids, 4):
        E4_CANDIDATES.add(tuple(sorted(E)))
for class_indices in RANK2_FLATS.values():
    cycle_indices = sorted(
        idx
        for ci in class_indices
        for idx in CLASS_ITEMS[ci][1]
    )
    for E in combinations(cycle_indices, 4):
        E4_CANDIDATES.add(tuple(sorted(E)))
assert len(E4_CANDIDATES) == 2010


def exact_nullspace_columns(columns):
    """Nullspace of a list of equal-length column vectors over Q."""
    m = len(columns)
    n = len(columns[0])
    matrix = [
        [Fraction(columns[j][i]) for j in range(m)]
        for i in range(n)
        if any(columns[j][i] for j in range(m))
    ]
    pivot_cols = []
    r = 0
    for col in range(m):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        q = matrix[r][col]
        matrix[r] = [x / q for x in matrix[r]]
        for i in range(len(matrix)):
            if i == r or not matrix[i][col]:
                continue
            q = matrix[i][col]
            matrix[i] = [x - q * y for x, y in zip(matrix[i], matrix[r])]
        pivot_cols.append(col)
        r += 1
    free_cols = [c for c in range(m) if c not in pivot_cols]
    basis = []
    for free in free_cols:
        x = [Fraction(0)] * m
        x[free] = Fraction(1)
        for row_idx in reversed(range(len(pivot_cols))):
            pc = pivot_cols[row_idx]
            x[pc] = -sum(matrix[row_idx][j] * x[j] for j in free_cols)
        basis.append(tuple(x))
    return basis, len(pivot_cols)


def primitive_row(vec):
    return list(primitive_integer_vector(tuple(Fraction(x) for x in vec)))


def restricted_rows_independent(a, b):
    for i, j in combinations(range(len(a)), 2):
        if a[i] * b[j] - a[j] * b[i]:
            return True
    return False


def det3(a, b, c, i, j, k):
    return (
        a[i] * (b[j] * c[k] - b[k] * c[j])
        - a[j] * (b[i] * c[k] - b[k] * c[i])
        + a[k] * (b[i] * c[j] - b[j] * c[i])
    )


def in_span_of_two(a, b, target):
    return all(
        det3(a, b, target, i, j, k) == 0
        for i, j, k in combinations(range(len(a)), 3)
    )


REMOVED5 = []
for full_block in range(15):
    full = tuple(range(3 * full_block, 3 * full_block + 3))
    for partial_block in range(15):
        if partial_block == full_block:
            continue
        partial = range(3 * partial_block, 3 * partial_block + 3)
        for two in combinations(partial, 2):
            R = tuple(sorted(full + two))
            REMOVED5.append((R, full_block, partial_block))
assert len(REMOVED5) == 630
assert len({R for R, _a, _b in REMOVED5}) == 630

four_outsider_checks = 0
rank_counter = Counter()
for E in sorted(E4_CANDIDATES):
    residuals = [OUTSIDE[e]["residual"] for e in E]
    null_basis, quotient_rank = exact_nullspace_columns(residuals)
    rank_counter[quotient_rank] += 1
    assert quotient_rank == 2
    assert len(null_basis) == 2

    H = []
    for alpha in null_basis:
        h = [
            sum(alpha[t] * OUTSIDE[E[t]]["fcoord"][k] for t in range(4))
            for k in range(45)
        ]
        H.append(primitive_row(h))

    for R, block_a, block_b in REMOVED5:
        four_outsider_checks += 1
        h1 = [H[0][k] for k in R]
        h2 = [H[1][k] for k in R]
        if not restricted_rows_independent(h1, h2):
            continue
        t1 = primitive_row([GROUND_FCOORD[block_a][k] for k in R])
        t2 = primitive_row([GROUND_FCOORD[block_b][k] for k in R])
        assert not (
            in_span_of_two(h1, h2, t1)
            and in_span_of_two(h1, h2, t2)
        )

assert rank_counter == Counter({2: 2010})
assert four_outsider_checks == 2010 * 630 == 1_266_300

print("PASS: 45-four-cycle exchange barrier")
print("simple undirected K8 four-cycles: 210")
print("selected four-cycles: 45")
print("external four-cycles: 165")
print("exact external projective classes: 105 = 45 singletons + 60 pairs")
print("two-outsider/full-block checks: 900")
print("external rank<=2 four-sets: 2010")
print("four-outsider/removed-five checks: 1266300")
print("conclusion: any sufficient 44-cycle family must use >=5 external cycles")
