#!/usr/bin/env python3
"""Exact six-outsider exchange barrier for the Target-C 45-four-cycle test.

This extends the exact zero-through-five-outsider exchange barriers.  It proves
that no sufficient 44-cycle family chosen from all 210 undirected simple K8
four-cycles can use exactly six cycles outside the selected 45-cycle family F.
Consequently any sufficient 44-cycle family, if one exists, uses at least seven
external cycles and omits at least eight members of F.

Candidate enumeration uses F_251 only as an exact indexing device.  The compact
quotient residuals are integer vectors with entries in {-1,0,1}; every 4x4
minor therefore has absolute value at most 16 by Hadamard, and every 3x3 minor
has absolute value below 6.  Hence rank <= 3 over F_251 is equivalent to rank
<= 3 over Q here.  Kernel and compensation checks are exact integer/rational
arithmetic.  Optional --start/--stop split the deterministic candidate ledger.
"""

from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import runpy

BASE_NAME = "verify_target_c_support7_global_segment_45_four_cycle_exchange_barrier_2026_09_19.py"
B = runpy.run_path(str(Path(__file__).with_name(BASE_NAME)))

OUTSIDE = B["OUTSIDE"]
CLASS_ITEMS = B["CLASS_ITEMS"]
COMPACT_DIRS = B["COMPACT_DIRS"]
NONZERO_COLS = B["NONZERO_COLS"]
GROUND_FCOORD = B["GROUND_FCOORD"]

P = 251
N = len(NONZERO_COLS)
assert N == 59
assert len(OUTSIDE) == 165
assert len(CLASS_ITEMS) == 105
assert max(abs(x) for v in COMPACT_DIRS for x in v) == 1

CYCLE_TO_CLASS = {}
for ci, (_key, ids) in enumerate(CLASS_ITEMS):
    for e in ids:
        assert e not in CYCLE_TO_CLASS
        CYCLE_TO_CLASS[e] = ci
assert len(CYCLE_TO_CLASS) == 165

RES = []
F2 = []
for e, item in enumerate(OUTSIDE):
    ci = CYCLE_TO_CLASS[e]
    full_key = CLASS_ITEMS[ci][0]
    pivot = next(i for i, x in enumerate(full_key) if x)
    lam = item["residual"][pivot] / full_key[pivot]
    assert lam in (1, -1)
    assert all(item["residual"][i] == lam * full_key[i] for i in range(len(full_key)))
    RES.append(tuple(int(lam * x) for x in COMPACT_DIRS[ci]))
    f2 = tuple(int(2 * x) for x in item["fcoord"])
    assert all(Fraction(x, 2) == y for x, y in zip(f2, item["fcoord"]))
    F2.append(f2)

MOD_CLASS_DIRS = [tuple(x % P for x in v) for v in COMPACT_DIRS]


def canonical_mod_span_three(a, b, c):
    rows = [list(MOD_CLASS_DIRS[a]), list(MOD_CLASS_DIRS[b]), list(MOD_CLASS_DIRS[c])]
    r = 0
    for col in range(N):
        pivot = next((i for i in range(r, 3) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        q = rows[r][col]
        if q != 1:
            inv = pow(q, P - 2, P)
            for j in range(col, N):
                rows[r][j] = rows[r][j] * inv % P
        for i in range(3):
            if i == r or not rows[i][col]:
                continue
            q = rows[i][col]
            for j in range(col, N):
                rows[i][j] = (rows[i][j] - q * rows[r][j]) % P
        r += 1
        if r == 3:
            break
    return bytes([r]) + b"".join(bytes(rows[i]) for i in range(r))


FLATS = {}
for a, b, c in combinations(range(len(CLASS_ITEMS)), 3):
    key = canonical_mod_span_three(a, b, c)
    mask = (1 << a) | (1 << b) | (1 << c)
    FLATS[key] = FLATS.get(key, 0) | mask

capacity_hist = Counter()
E6 = set()
for mask in FLATS.values():
    class_ids = [i for i in range(len(CLASS_ITEMS)) if (mask >> i) & 1]
    cycle_ids = sorted(e for ci in class_ids for e in CLASS_ITEMS[ci][1])
    if len(cycle_ids) < 5:
        continue
    capacity_hist[len(cycle_ids)] += 1
    if len(cycle_ids) >= 6:
        E6.update(combinations(cycle_ids, 6))

assert capacity_hist == Counter({5: 76950, 6: 30800, 8: 1140, 7: 900})
assert len(E6) == 66980
E6 = sorted(E6)


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det3(m):
    a, b, c = m
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def det4(m):
    total = 0
    for j in range(4):
        minor = [[m[i][k] for k in range(4) if k != j] for i in range(1, 4)]
        total += (-1 if j % 2 else 1) * m[0][j] * det3(minor)
    return total


def determinant(m):
    if len(m) == 2:
        return det2(m)
    if len(m) == 3:
        return det3(m)
    if len(m) == 4:
        return det4(m)
    raise AssertionError("unsupported determinant size")


def mod_basis(E):
    basis = []
    pivot_rows = []
    for idx in range(len(E)):
        v = RES[E[idx]]
        if not basis:
            q = next(i for i, x in enumerate(v) if x % P)
            basis.append(idx)
            pivot_rows.append(q)
            continue
        r = len(basis)
        A = [
            [RES[E[basis[j]]][pivot_rows[i]] % P for j in range(r)]
            + [v[pivot_rows[i]] % P]
            for i in range(r)
        ]
        for col in range(r):
            pivot = next(i for i in range(col, r) if A[i][col])
            A[col], A[pivot] = A[pivot], A[col]
            inv = pow(A[col][col], P - 2, P)
            for j in range(col, r + 1):
                A[col][j] = A[col][j] * inv % P
            for i in range(r):
                if i == col or not A[i][col]:
                    continue
                q = A[i][col]
                for j in range(col, r + 1):
                    A[i][j] = (A[i][j] - q * A[col][j]) % P
        coeff = [A[j][r] for j in range(r)]
        bad = None
        for q in range(N):
            if (v[q] - sum(coeff[j] * RES[E[basis[j]]][q] for j in range(r))) % P:
                bad = q
                break
        if bad is not None:
            basis.append(idx)
            pivot_rows.append(bad)
            assert len(basis) <= 3
    return basis, pivot_rows


def exact_kernel_relations(E):
    basis, pivot_rows = mod_basis(E)
    r = len(basis)
    assert r in (2, 3)
    bvec = [RES[E[j]] for j in basis]
    M = [[bvec[j][q] for j in range(r)] for q in pivot_rows]
    D = determinant(M)
    assert D and D % P

    relations = []
    for j in range(len(E)):
        if j in basis:
            continue
        w = RES[E[j]]
        nums = []
        for k in range(r):
            Mk = [row[:] for row in M]
            for i, q in enumerate(pivot_rows):
                Mk[i][k] = w[q]
            nums.append(determinant(Mk))
        alpha = [0] * len(E)
        alpha[j] = D
        for k, b in enumerate(basis):
            alpha[b] -= nums[k]
        assert all(sum(alpha[t] * RES[E[t]][q] for t in range(len(E))) == 0 for q in range(N))
        relations.append(tuple(alpha))
    assert len(relations) == len(E) - r
    return r, relations


def h_rows(E, relations):
    return [
        [sum(alpha[t] * F2[E[t]][k] for t in range(len(E))) for k in range(45)]
        for alpha in relations
    ]


G = (1, -1, -1)


def coeff_on_mask(H, block, mask):
    positions = [i for i in range(3) if (mask >> i) & 1]
    i0 = positions[0]
    out = []
    for h in H:
        coeff = h[3 * block + i0] * G[i0]
        if any(h[3 * block + i] != coeff * G[i] for i in positions):
            return None
        out.append(coeff)
    return tuple(out)


def det_columns(cols):
    n = len(cols)
    return determinant([[cols[j][i] for j in range(n)] for i in range(n)])


def cross3(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot3(a, b):
    return sum(x * y for x, y in zip(a, b))


def primitive3(v):
    from math import gcd
    g = 0
    for x in v:
        g = gcd(g, abs(x))
    if not g:
        return None
    q = tuple(x // g for x in v)
    first = next(x for x in q if x)
    return tuple(-x for x in q) if first < 0 else q


def span_rank3(vectors):
    u = next((v for v in vectors if any(v)), None)
    if u is None:
        return 0, None
    for v in vectors:
        n = cross3(u, v)
        if any(n):
            if any(dot3(n, w) for w in vectors):
                return 3, None
            return 2, n
    return 1, None


def rank3_compensation(H):
    # For 3+3+1, fix the singleton block c.  The two full-block
    # coefficient vectors may be chosen from any two other blocks.  Their
    # existence is characterized just by the rank of the full-block vectors
    # outside c, avoiding enumeration of all 4095 patterns.
    full = {}
    doubles = {b: [] for b in range(15)}
    singles = {b: [] for b in range(15)}
    for block in range(15):
        c = coeff_on_mask(H, block, 0b111)
        if c is not None:
            full[block] = c
        for omitted in range(3):
            mask = 0b111 ^ (1 << omitted)
            c = coeff_on_mask(H, block, mask)
            if c is not None:
                doubles[block].append(c)
        for pos in range(3):
            c = coeff_on_mask(H, block, 1 << pos)
            assert c is not None
            singles[block].append(c)

    for singleton_block in range(15):
        fvec = [v for b, v in full.items() if b != singleton_block]
        r, normal = span_rank3(fvec)
        if r < 2:
            continue
        for w in singles[singleton_block]:
            if not any(w):
                continue
            if r == 3 or dot3(normal, w):
                return ("3+3+1", singleton_block)

    # For 3+2+2, quotient the double-block coefficient vectors by the
    # full-block vector u.  A block contributes quotient rank 0, 1, or 2.
    # Success requires two distinct double blocks with independent quotient
    # directions.  Cross(u,v) is an exact projective key for a nonzero
    # quotient direction.
    for full_block, u in full.items():
        if not any(u):
            continue
        states = []
        for block in range(15):
            if block == full_block:
                continue
            keys = set()
            for v in doubles[block]:
                key = primitive3(cross3(u, v))
                if key is not None:
                    keys.add(key)
            if keys:
                states.append((block, keys))
        if len(states) < 2:
            continue
        if any(len(keys) >= 2 for _b, keys in states):
            return ("3+2+2", full_block)
        directions = {next(iter(keys)) for _b, keys in states}
        if len(directions) >= 2:
            return ("3+2+2", full_block)
    return None


def exact_row_rank(rows):
    # Fraction-free integer elimination.  Dividing each updated row by its
    # content preserves its rational row span while controlling coefficient
    # growth.
    from math import gcd
    A = [list(map(int, row)) for row in rows]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if A[i][col]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        for i in range(r + 1, m):
            if not A[i][col]:
                continue
            a, b = A[r][col], A[i][col]
            g = gcd(abs(a), abs(b))
            ma, mb = b // g, a // g
            A[i] = [mb * x - ma * y for x, y in zip(A[i], A[r])]
            content = 0
            for x in A[i][col:]:
                content = gcd(content, abs(x))
            if content > 1:
                A[i] = [x // content for x in A[i]]
        r += 1
    return r


def target_row(R, block):
    return [G[k % 3] if k // 3 == block else 0 for k in R]


def rank2_t3_compensation(H):
    for blocks in combinations(range(15), 3):
        for single_index in range(3):
            single_block = blocks[single_index]
            full_blocks = [x for x in blocks if x != single_block]
            for pos in range(3):
                R = sorted(
                    [3 * x + i for x in full_blocks for i in range(3)]
                    + [3 * single_block + pos]
                )
                Hr = [[h[k] for k in R] for h in H]
                rh = exact_row_rank(Hr)
                if exact_row_rank(Hr + [target_row(R, x) for x in blocks]) == rh:
                    return ("3+3+1", blocks, single_block, pos)

        for full_block in blocks:
            double_blocks = [x for x in blocks if x != full_block]
            for omitted_a in range(3):
                for omitted_b in range(3):
                    R = [3 * full_block + i for i in range(3)]
                    R += [3 * double_blocks[0] + i for i in range(3) if i != omitted_a]
                    R += [3 * double_blocks[1] + i for i in range(3) if i != omitted_b]
                    R.sort()
                    Hr = [[h[k] for k in R] for h in H]
                    rh = exact_row_rank(Hr)
                    if exact_row_rank(Hr + [target_row(R, x) for x in blocks]) == rh:
                        return ("3+2+2", blocks, full_block, omitted_a, omitted_b)
    return None


def rank2_t4_compensation(H):
    full = []
    double = []
    single = []
    for block in range(15):
        c = coeff_on_mask(H, block, 0b111)
        if c is not None:
            full.append((block, 0b111, c))
        for omitted in range(3):
            mask = 0b111 ^ (1 << omitted)
            c = coeff_on_mask(H, block, mask)
            if c is not None:
                double.append((block, mask, c))
        for pos in range(3):
            mask = 1 << pos
            c = coeff_on_mask(H, block, mask)
            assert c is not None
            single.append((block, mask, c))

    for f in full:
        for d in double:
            if d[0] == f[0]:
                continue
            for s1, s2 in combinations(single, 2):
                if len({f[0], d[0], s1[0], s2[0]}) < 4:
                    continue
                if det_columns((f[2], d[2], s1[2], s2[2])):
                    return ("3+2+1+1", f, d, s1, s2)

    for d1, d2, d3 in combinations(double, 3):
        if len({d1[0], d2[0], d3[0]}) < 3:
            continue
        for s in single:
            if s[0] in (d1[0], d2[0], d3[0]):
                continue
            if det_columns((d1[2], d2[2], d3[2], s[2])):
                return ("2+2+2+1", d1, d2, d3, s)
    return None


parser = ArgumentParser()
parser.add_argument("--start", type=int, default=0)
parser.add_argument("--stop", type=int, default=None)
args = parser.parse_args()
start = args.start
stop = len(E6) if args.stop is None else args.stop
assert 0 <= start <= stop <= len(E6)

rank_counter = Counter()
rank3_patterns_represented = 0
rank2_t3_patterns = 0
rank2_t4_patterns_represented = 0

for E in E6[start:stop]:
    r, relations = exact_kernel_relations(E)
    rank_counter[r] += 1
    H = h_rows(E, relations)
    if r == 3:
        rank3_patterns_represented += 16380
        assert rank3_compensation(H) is None
        continue

    assert r == 2
    rank2_t3_patterns += 16380
    assert rank2_t3_compensation(H) is None
    rank2_t4_patterns_represented += 884520
    assert rank2_t4_compensation(H) is None

if start == 0 and stop == len(E6):
    assert rank_counter == Counter({3: 66960, 2: 20})
    assert rank3_patterns_represented == 66960 * 16380 == 1_096_804_800
    assert rank2_t3_patterns == 20 * 16380 == 327_600
    assert rank2_t4_patterns_represented == 20 * 884520 == 17_690_400

print("PASS: six-outsider 44-cycle exchange barrier")
print(f"candidate ledger: {len(E6)} exact rank<=3 six-outsider sets")
print(f"checked slice: [{start}, {stop})")
print(f"exact quotient ranks in slice: {dict(rank_counter)}")
print(f"rank-3 removal patterns represented: {rank3_patterns_represented}")
print(f"rank-2 three-block checks: {rank2_t3_patterns}")
print(f"rank-2 four-block patterns represented: {rank2_t4_patterns_represented}")
if start == 0 and stop == len(E6):
    print("conclusion: any sufficient 44-cycle family must use >=7 external cycles")
