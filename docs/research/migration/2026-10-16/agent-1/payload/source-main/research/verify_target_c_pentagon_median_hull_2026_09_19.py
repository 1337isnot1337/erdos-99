#!/usr/bin/env python3
"""Exact verifier for the median-threshold convex hull of one physical gap-order cone."""

from fractions import Fraction as F
from itertools import combinations

N = 5
SUM_ROW = (F(1),) * N
SUM_RHS = F(2)
ORDER = (0, 2, 3, 4, 1)  # increasing ranks in the representative physical order cone
RANK = {k: r for r, k in enumerate(ORDER)}


def branch_constraints(median_low):
    """Closed rational relaxation for one side of x_3 = 2/5."""
    cons = []
    # Turn-simplex q_k >= 1/3, written A x <= b.
    for k in range(5):
        r = [F(0)] * N
        r[k] -= 1
        r[(k + 1) % 5] -= 1
        r[(k + 3) % 5] += 1
        cons.append((tuple(r), F(-1, 3), ("Q", k)))

    # Representative physical order x0 <= x2 <= x3 <= x4 <= x1.
    for a, b in zip(ORDER, ORDER[1:]):
        r = [F(0)] * N
        r[a] += 1
        r[b] -= 1
        cons.append((tuple(r), F(0), ("O", a, b)))

    # Nonnegativity. It is redundant physically but makes boundedness explicit.
    for k in range(5):
        r = [F(0)] * N
        r[k] -= 1
        cons.append((tuple(r), F(0), ("N", k)))

    # Exact 2/5 secants. Ranks 1,2 are low; ranks 4,5 are high.
    # The median uses the side chosen for this branch.
    for k in range(5):
        rank = RANK[k]
        use_low = rank <= 1 or (rank == 2 and median_low)
        r = [F(0)] * N
        if use_low:
            # x_{k+2}+x_{k+3} <= 2/3 + x_k/3.
            r[k] -= F(1, 3)
            r[(k + 2) % 5] += 1
            r[(k + 3) % 5] += 1
            cons.append((tuple(r), F(2, 3), ("SL", k)))
        else:
            # x_{k+2}+x_{k+3} <= 1/2 + 3 x_k/4.
            r[k] -= F(3, 4)
            r[(k + 2) % 5] += 1
            r[(k + 3) % 5] += 1
            cons.append((tuple(r), F(1, 2), ("SH", k)))

    r = [F(0)] * N
    if median_low:
        r[3] = 1
        cons.append((tuple(r), F(2, 5), ("MEDIAN_LOW",)))
    else:
        r[3] = -1
        cons.append((tuple(r), F(-2, 5), ("MEDIAN_HIGH",)))
    return tuple(cons)


def solve_square(rows, rhs):
    n = len(rows)
    assert n == len(rhs) and all(len(r) == n for r in rows)
    a = [list(map(F, r)) + [F(b)] for r, b in zip(rows, rhs)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if a[r][c]), None)
        if pivot is None:
            return None
        a[c], a[pivot] = a[pivot], a[c]
        p = a[c][c]
        a[c] = [z / p for z in a[c]]
        for r in range(n):
            if r == c or not a[r][c]:
                continue
            q = a[r][c]
            a[r] = [u - q * v for u, v in zip(a[r], a[c])]
    return tuple(a[i][-1] for i in range(n))


def enumerate_vertices(cons):
    verts = set()
    for active in combinations(range(len(cons)), N - 1):
        rows = [SUM_ROW] + [cons[i][0] for i in active]
        rhs = [SUM_RHS] + [cons[i][1] for i in active]
        x = solve_square(rows, rhs)
        if x is None:
            continue
        if all(sum(a * y for a, y in zip(r, x)) <= b for r, b, _ in cons):
            verts.add(x)
    return frozenset(verts)


def affine_rank(points):
    points = list(points)
    if len(points) <= 1:
        return 0
    base = points[0]
    mat = [[p[j] - base[j] for j in range(N - 1)] for p in points[1:]]
    # We project away x4 because all points satisfy sum x=2.
    rank = 0
    col = 0
    while rank < len(mat) and col < N - 1:
        pivot = next((r for r in range(rank, len(mat)) if mat[r][col]), None)
        if pivot is None:
            col += 1
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        p = mat[rank][col]
        mat[rank] = [z / p for z in mat[rank]]
        for r in range(len(mat)):
            if r == rank or not mat[r][col]:
                continue
            q = mat[r][col]
            mat[r] = [u - q * v for u, v in zip(mat[r], mat[rank])]
        rank += 1
        col += 1
    return rank


LOW = branch_constraints(True)
HIGH = branch_constraints(False)
LOW_VERTS = enumerate_vertices(LOW)
HIGH_VERTS = enumerate_vertices(HIGH)
UNION_VERTS = LOW_VERTS | HIGH_VERTS
assert len(LOW_VERTS) == 11
assert len(HIGH_VERTS) == 13
assert len(UNION_VERTS) == 17

# Two new branch-free inequalities, in representative labels.
# H1: 5 x0 + 4 x1 - x2 - 3 x3 <= 2.
H1 = ((F(5), F(4), F(-1), F(-3), F(0)), F(2), "H1")
# H2: 9 x0 + 9 x1 + x2 - 4 x3 <= 6.
H2 = ((F(9), F(9), F(1), F(-4), F(0)), F(6), "H2")

# Direct exact Farkas identities for H1/H2 in both median branches.
def by_label(cons):
    return {lab: (r, b) for r, b, lab in cons}


L = by_label(LOW)
H = by_label(HIGH)


def check_identity(target, const, pieces, eq_mult=F(0)):
    rr = [F(0)] * N
    bb = F(0)
    for mult, (r, b) in pieces:
        assert mult >= 0
        for j, z in enumerate(r):
            rr[j] += mult * z
        bb += mult * b
    for j in range(N):
        rr[j] += eq_mult * SUM_ROW[j]
    bb += eq_mult * SUM_RHS
    assert tuple(rr) == tuple(target)
    assert bb == const


# Low-median branch:
# H1 = (1/3) O23 + SL2 + 5 SL3 - SUM.
check_identity(H1[0], H1[1], [
    (F(1, 3), L[("O", 2, 3)]),
    (F(1), L[("SL", 2)]),
    (F(5), L[("SL", 3)]),
], eq_mult=F(-1))
# H2 = O23 + 9 SL3.
check_identity(H2[0], H2[1], [
    (F(1), L[("O", 2, 3)]),
    (F(9), L[("SL", 3)]),
])

# High-median branch:
# H1 = O02 + 4 SH3.
check_identity(H1[0], H1[1], [
    (F(1), H[("O", 0, 2)]),
    (F(4), H[("SH", 3)]),
])
# H2 = O34 + 8 SH3 + SUM.
check_identity(H2[0], H2[1], [
    (F(1), H[("O", 3, 4)]),
    (F(8), H[("SH", 3)]),
], eq_mult=F(1))

# Claimed exact convex hull. The original Q/order/common-secant facets below,
# plus H1/H2, define the convex hull of the two median branches.
# We include a redundant nonnegativity family so boundedness is explicit.
COMMON = []
# Keep all five turn-simplex inequalities in the branch-free description.
for k in range(5):
    r = [F(0)] * N
    r[k] -= 1
    r[(k + 1) % 5] -= 1
    r[(k + 3) % 5] += 1
    COMMON.append((tuple(r), F(-1, 3), ("Q", k)))
for a, b in zip(ORDER, ORDER[1:]):
    r = [F(0)] * N
    r[a] += 1
    r[b] -= 1
    COMMON.append((tuple(r), F(0), ("O", a, b)))
for k in range(5):
    r = [F(0)] * N
    r[k] -= 1
    COMMON.append((tuple(r), F(0), ("N", k)))
# Four branch-determined exact 2/5 secants: ranks 1,2 low and 4,5 high.
for k in range(5):
    rank = RANK[k]
    if rank == 2:
        continue
    r = [F(0)] * N
    if rank <= 1:
        r[k] -= F(1, 3)
        r[(k + 2) % 5] += 1
        r[(k + 3) % 5] += 1
        COMMON.append((tuple(r), F(2, 3), ("SL", k)))
    else:
        r[k] -= F(3, 4)
        r[(k + 2) % 5] += 1
        r[(k + 3) % 5] += 1
        COMMON.append((tuple(r), F(1, 2), ("SH", k)))
COMMON = tuple(COMMON)
COMMON_VERTS = enumerate_vertices(COMMON)
# H1 and H2 are genuinely new relative to the common branch-independent layer.
assert max(sum(a * y for a, y in zip(H1[0], x)) for x in COMMON_VERTS) > H1[1]
assert max(sum(a * y for a, y in zip(H2[0], x)) for x in COMMON_VERTS) > H2[1]

HULL_CONS = tuple(COMMON + (H1, H2))
HULL_VERTS = enumerate_vertices(HULL_CONS)
assert all(sum(a * y for a, y in zip(r, x)) <= b for x in UNION_VERTS for r, b, _ in HULL_CONS)
assert HULL_VERTS <= UNION_VERTS
assert len(HULL_VERTS) == 11

# Each novel inequality is a genuine facet of the four-dimensional hull.
for r, b, name in (H1, H2):
    on = [x for x in HULL_VERTS if sum(a * y for a, y in zip(r, x)) == b]
    assert affine_rank(on) == 3, (name, len(on), affine_rank(on))

# Rank-form equivalents, where a<=b<=c<=d<=e are the five ordered gaps:
# H1 <=> 5 b + 7 c + 4 d >= 6 + a.
# H2 <=> 8 b + 13 c + 9 d >= 12.
for x in UNION_VERTS:
    a, b, c, d, e = (x[i] for i in ORDER)
    lhs1 = 5 * b + 7 * c + 4 * d
    lhs2 = 8 * b + 13 * c + 9 * d
    assert lhs1 >= 6 + a
    assert lhs2 >= 12

print("PASS")
print("low-branch vertices:", len(LOW_VERTS))
print("high-branch vertices:", len(HIGH_VERTS))
print("branch-vertex union:", len(UNION_VERTS))
print("convex-hull extreme vertices:", len(HULL_VERTS))
print("new exact hull facets:")
print("  5*x_min + 4*x_max - x_second - 3*x_median <= 2")
print("  9*x_min + 9*x_max + x_second - 4*x_median <= 6")
print("equivalently:")
print("  5*x_second + 7*x_median + 4*x_second_largest >= 6 + x_min")
print("  8*x_second + 13*x_median + 9*x_second_largest >= 12")
