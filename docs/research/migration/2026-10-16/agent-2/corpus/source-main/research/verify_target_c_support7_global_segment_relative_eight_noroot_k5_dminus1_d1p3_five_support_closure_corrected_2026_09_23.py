#!/usr/bin/env python3
"""Dimension-correct audit of the m=5 eight-no-root k=5,p=3 closure.

The earlier verifier imported relation_rows_int from a four-cycle base module.
That helper hard-codes a four-coordinate nullspace and is not valid for an
eight-cycle ext tuple. This audit repeats the same census with the nullspace
dimension set to len(ext)=8. The closure result and all published counts remain
unchanged.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd, lcm
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
OLD = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_five_support_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("five_support_old", OLD)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)
R = F.R


def primitive_int(v):
    scale = 1
    for x in v:
        scale = lcm(scale, x.denominator)
    a = [int(x * scale) for x in v]
    g = 0
    for x in a:
        g = gcd(g, abs(x))
    if g:
        a = [x // g for x in a]
    for x in a:
        if x:
            if x < 0:
                a = [-y for y in a]
            break
    return tuple(a)


def nullspace_int(key, n):
    pivots = [next(i for i, x in enumerate(row) if x) for row in key]
    free = [j for j in range(n) if j not in pivots]
    out = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = 1
        for row, p in zip(key, pivots):
            v[p] = -row[f]
        out.append(primitive_int(v))
    return out


def relation_rows_int8(ext, touched, states, constraint_key):
    rows = []
    for b, s in zip(touched, states):
        if R.STATES[s][2]:
            ids = R.BLOCKS[b]
            rows.append([
                R.MCOORD[ids[0]][70 + j]
                - R.MCOORD[ids[1]][70 + j]
                - R.MCOORD[ids[2]][70 + j]
                for j in range(15)
            ])

    for alpha in nullspace_int(constraint_key, len(ext)):
        tv = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
            for j in range(15)
        ]
        for b, s in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][b][0] for i, e in enumerate(ext))
            vy = sum(alpha[i] * R.QCOMP[e][b][1] for i, e in enumerate(ext))
            beta = R.solve_local_coeffs_int(R.STATES[s][0], (-vx, -vy))
            ids = R.BLOCKS[b]
            for j0, q in enumerate(beta):
                if q:
                    for jj in range(15):
                        tv[jj] += q * R.MCOORD[ids[j0]][70 + jj]
        rows.append(tv)
    return rows


def main():
    assert R.lucas_lehmer_127()
    reps = F.five_support_cycle_orbits()
    singleton_sets = F.singleton_triples()

    candidate_count = 0
    rank_three_count = 0
    generalized_weight_count = 0
    relation_rank_census = Counter()
    max_norm2 = 0

    for ext in reps:
        local_rows = {
            (b, d): F.singleton_row(ext, b, d)
            for b in F.TOUCHED
            for d in F.LOCAL
        }
        for singleton_blocks in singleton_sets:
            for directions in product(F.LOCAL, repeat=3):
                candidate_count += 1
                rows = tuple(
                    local_rows[(b, d)]
                    for b, d in zip(singleton_blocks, directions)
                )
                if R.exact_rank(rows) != 3:
                    continue
                rank_three_count += 1
                d1, d2, d3 = F.generalized_weights(rows)
                if not (d1 >= 2 and d2 >= 4 and d3 >= 5):
                    continue
                generalized_weight_count += 1

                constraint_key = R.rowspace_key(rows)
                singletons = dict(zip(singleton_blocks, directions))
                states = tuple(
                    F.DIR_MASK[singletons[b]] if b in singletons else 7
                    for b in F.TOUCHED
                )
                rel_rows = relation_rows_int8(ext, F.TOUCHED, states, constraint_key)
                for row in rel_rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
                rank = R.rank_mod(rel_rows)
                relation_rank_census[rank] += 1
                assert rank == 6

    assert candidate_count == 127710
    assert rank_three_count == 118838
    assert generalized_weight_count == 36106
    assert dict(relation_rank_census) == {6: 36106}
    assert max_norm2 == 84
    assert R.P * R.P > max_norm2 ** 15

    print("PASS: corrected eight-no-root k=5,p=3 five-support closure")
    print("candidate_count", candidate_count)
    print("rank_three_count", rank_three_count)
    print("generalized_weight_count", generalized_weight_count)
    print("relation_rank_census", dict(relation_rank_census))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
