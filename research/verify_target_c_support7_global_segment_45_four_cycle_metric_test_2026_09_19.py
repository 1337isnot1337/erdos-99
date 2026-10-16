#!/usr/bin/env python3
"""Exact certificate for a 45-four-cycle complete reciprocal metric test.

On the complete generic angular system, the existing 15 ground-root star-cycle
log-sine equations are sufficient for common reciprocal metric compatibility.
For every pair 2 <= i < j <= 7, this verifier gives an integer cycle-chain
identity expressing twice the ground-root star cycle S_0(1,i,j) as four
automatic triangle-side cycles plus three cross-root four-cycles on the K4
{0,1,i,j}. Hence vanishing of the 45 listed four-cycle sums implies all fifteen
ground-root equations.

Only integer graph-chain arithmetic and exact modular rank are used here.
"""
from itertools import combinations

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


def rank_mod_prime(rows, p=1_000_000_007):
    a = [[x % p for x in row] for row in rows]
    m = len(a)
    n = len(a[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], p - 2, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(m):
            if i == r or a[i][c] == 0:
                continue
            q = a[i][c]
            a[i] = [(x - q * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


SIDE = [side_triangle(*t) for t in combinations(V, 3)]
GROUND = [
    star_triangle(0, 1, i, j)
    for i, j in combinations(range(2, 8), 2)
]
assert len(SIDE) == 56
assert len(GROUND) == 15
assert rank_mod_prime(SIDE) == 56
assert rank_mod_prime(GROUND) == 15
assert rank_mod_prime(SIDE + GROUND) == 71

FOUR = []
for i, j in combinations(range(2, 8), 2):
    c1 = k8_cycle((0, 1, i, j))
    c2 = k8_cycle((0, 1, j, i))
    c3 = k8_cycle((0, i, 1, j))
    FOUR.extend((c1, c2, c3))

    # Oriented chain identity:
    # 2 S_0(1,i,j)
    #   = -T_01i + T_01j - T_0ij - T_1ij
    #     + C_01ij - C_01ji - C_0i1j.
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

assert len(FOUR) == 45
assert len({tuple(row) for row in FOUR}) == 45

# These 45 are independent even after adjoining the 56 side triangles. This is
# not a global minimality theorem, but it verifies that the displayed family has
# no linear redundancy relative to the automatic side identities.
assert rank_mod_prime(SIDE + FOUR) == 101

# The fifteen ground-root equations lie in the span of SIDE + FOUR, as certified
# constructively by the identities above. The rank equality is an independent
# exact guard on that containment.
assert rank_mod_prime(SIDE + FOUR + GROUND) == 101

print("PASS: 45-four-cycle complete-metric reduction")
print("automatic triangle-side cycles: 56")
print("selected cross-root four-cycles: 45")
print("ground-root target cycles: 15")
print("rank(side + four): 101")
print("rank(side + four + ground): 101")
