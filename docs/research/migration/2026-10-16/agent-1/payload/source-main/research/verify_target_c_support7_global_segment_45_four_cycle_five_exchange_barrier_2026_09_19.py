#!/usr/bin/env python3
"""Exact five-outsider exchange barrier for the Target-C 45-four-cycle test.

This extends verify_target_c_support7_global_segment_45_four_cycle_exchange_barrier_2026_09_19.py.
That verifier rules out 44-cycle replacements using at most four cycles outside
its selected 45-cycle family F. Here we rule out exactly five outside cycles.
Together the two verifiers prove that any sufficient 44-cycle family chosen
from the 210 undirected simple K8 four-cycles must use at least six cycles
outside F, and therefore omit at least seven members of F.

The candidate enumeration uses F_251 only as an exact indexing device. The
compact quotient residuals are integer vectors with entries in {-1,0,1}. Every
4x4 minor therefore has absolute value at most 16 by Hadamard, and every 3x3
minor has absolute value < 6. Thus ranks 2 and 3 over F_251 agree with the
rational ranks on the enumerated candidates. Final compensation tests use
exact integer arithmetic, with Fraction only in the small two-block rank test.

Optional --start/--stop split the deterministic candidate ledger for bounded
reruns. A full run additionally checks the global totals.
"""

from argparse import ArgumentParser
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
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
E5 = set()
for mask in FLATS.values():
    class_ids = [i for i in range(len(CLASS_ITEMS)) if (mask >> i) & 1]
    cycle_ids = sorted(e for ci in class_ids for e in CLASS_ITEMS[ci][1])
    if len(cycle_ids) < 5:
        continue
    capacity_hist[len(cycle_ids)] += 1
    E5.update(combinations(cycle_ids, 5))

assert capacity_hist == Counter({5: 76950, 6: 30800, 8: 1140, 7: 900})
assert len(E5) == 332250
E5 = sorted(E5)


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def det3(M):
    a, b, c = M
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def determinant(M):
    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return det2(M)
    assert len(M) == 3
    return det3(M)


def mod_basis(E):
    basis = []
    pivot_rows = []
    for idx in range(5):
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
    Bvec = [RES[E[j]] for j in basis]
    M = [[Bvec[j][q] for j in range(r)] for q in pivot_rows]
    D = determinant(M)
    assert D and D % P

    relations = []
    for j in range(5):
        if j in basis:
            continue
        w = RES[E[j]]
        nums = []
        for k in range(r):
            Mk = [row[:] for row in M]
            for i, q in enumerate(pivot_rows):
                Mk[i][k] = w[q]
            nums.append(determinant(Mk))
        alpha = [0] * 5
        alpha[j] = D
        for k, b in enumerate(basis):
            alpha[b] -= nums[k]
        assert all(
            D * w[q] == sum(nums[k] * Bvec[k][q] for k in range(r))
            for q in range(N)
        )
        relations.append(tuple(alpha))
    assert len(relations) == 5 - r
    return r, relations


def h_rows(E, relations):
    return [
        [sum(alpha[t] * F2[E[t]][k] for t in range(5)) for k in range(45)]
        for alpha in relations
    ]


G = (1, -1, -1)


def proportional_on_mask(h, block, mask):
    positions = [i for i in range(3) if (mask >> i) & 1]
    i0 = positions[0]
    coeff = h[3 * block + i0] * G[i0]
    if any(h[3 * block + i] != coeff * G[i] for i in positions):
        return None
    return coeff


def rank3_compensation(H):
    good = []
    for block in range(15):
        coeff = []
        for h in H:
            c = proportional_on_mask(h, block, 0b111)
            if c is None:
                break
            coeff.append(c)
        else:
            good.append((block, coeff))
    for (a, u), (b, v) in combinations(good, 2):
        if u[0] * v[1] - u[1] * v[0]:
            return a, b
    return None


def exact_row_rank(rows):
    A = [[Fraction(x) for x in row] for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, m) if A[i][col]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        q = A[r][col]
        for j in range(col, n):
            A[r][j] /= q
        for i in range(r + 1, m):
            if not A[i][col]:
                continue
            q = A[i][col]
            for j in range(col, n):
                A[i][j] -= q * A[r][j]
        r += 1
    return r


def rank2_full_block_compensation(H):
    for a, b in combinations(range(15), 2):
        R = list(range(3 * a, 3 * a + 3)) + list(range(3 * b, 3 * b + 3))
        Hr = [[h[k] for k in R] for h in H]
        rh = exact_row_rank(Hr)
        ta = [1, -1, -1, 0, 0, 0]
        tb = [0, 0, 0, 1, -1, -1]
        if exact_row_rank(Hr + [ta, tb]) == rh:
            return a, b
    return None


def rank2_three_block_compensation(H):
    for a, b, c in permutations(range(15), 3):
        if len({a, b, c}) != 3:
            continue
        for omitted_b in range(3):
            mask_b = 0b111 ^ (1 << omitted_b)
            for one_c in range(3):
                mask_c = 1 << one_c
                coeff = []
                for h in H:
                    ca = proportional_on_mask(h, a, 0b111)
                    cb = proportional_on_mask(h, b, mask_b)
                    cc = proportional_on_mask(h, c, mask_c)
                    if ca is None or cb is None or cc is None:
                        break
                    coeff.append([ca, cb, cc])
                else:
                    if det3(coeff):
                        return ("3+2+1", a, b, c, omitted_b, one_c)

    for a, b, c in combinations(range(15), 3):
        for omitted_a in range(3):
            mask_a = 0b111 ^ (1 << omitted_a)
            for omitted_b in range(3):
                mask_b = 0b111 ^ (1 << omitted_b)
                for omitted_c in range(3):
                    mask_c = 0b111 ^ (1 << omitted_c)
                    coeff = []
                    for h in H:
                        ca = proportional_on_mask(h, a, mask_a)
                        cb = proportional_on_mask(h, b, mask_b)
                        cc = proportional_on_mask(h, c, mask_c)
                        if ca is None or cb is None or cc is None:
                            break
                        coeff.append([ca, cb, cc])
                    else:
                        if det3(coeff):
                            return ("2+2+2", a, b, c, omitted_a, omitted_b, omitted_c)
    return None


parser = ArgumentParser()
parser.add_argument("--start", type=int, default=0)
parser.add_argument("--stop", type=int, default=None)
args = parser.parse_args()
start = args.start
stop = len(E5) if args.stop is None else args.stop
assert 0 <= start <= stop <= len(E5)

rank_counter = Counter()
rank3_pair_checks = 0
rank2_full_checks = 0
rank2_three_block_checks = 0

for E in E5[start:stop]:
    r, relations = exact_kernel_relations(E)
    rank_counter[r] += 1
    H = h_rows(E, relations)
    if r == 3:
        rank3_pair_checks += 105
        assert rank3_compensation(H) is None
        continue

    assert r == 2
    rank2_full_checks += 105
    assert rank2_full_block_compensation(H) is None
    rank2_three_block_checks += 15 * 14 * 13 * 3 * 3 + 455 * 27
    assert rank2_three_block_compensation(H) is None

if start == 0 and stop == len(E5):
    assert rank_counter == Counter({3: 332130, 2: 120})
    assert rank3_pair_checks == 332130 * 105
    assert rank2_full_checks == 120 * 105 == 12600
    assert rank2_three_block_checks == 120 * 36855 == 4422600

print("PASS: five-outsider 44-cycle exchange barrier")
print(f"candidate ledger: {len(E5)} exact rank<=3 five-outsider sets")
print(f"checked slice: [{start}, {stop})")
print(f"exact quotient ranks in slice: {dict(rank_counter)}")
print(f"rank-3 two-block checks represented: {rank3_pair_checks}")
print(f"rank-2 full/full checks: {rank2_full_checks}")
print(f"rank-2 three-block checks: {rank2_three_block_checks}")
if start == 0 and stop == len(E5):
    print("conclusion: any sufficient 44-cycle family must use >=6 external cycles")
