#!/usr/bin/env python3
"""Exact six-row d=4 singleton-functional obstruction for eight-no-root k=7.

The only surviving branch-A profile in the eight-no-root k=7 layer is

    D=-2, p=11, (d_v,q,s)=(4,11,11).

The committed good-pair reduction supplies a p-retaining synchronized six-row
k=5 shadow. Deficiency two is already excluded. The committed branch-A
pair-extension verifier excludes the d6=3 side. If the remaining shadow had
virtual-canonical deficiency d6=4, then its defect is

    D6 = -2 + 4 = 2,

and all 11 selected incomplete root rows are singletons. The established
replacement-functional accounting gives

    D6 >= 6 + p + 3*d6 - 3*s,

where s is the extra rank, modulo the canonical relation-column span, of the
compatible singleton replacement functionals. Thus d6=4 would require s>=9.
In particular the virtual-canonical state must have singleton capacity at
least 9.

This verifier exhausts the exact S7 six-row augmentation cover and every
synchronized rank-one virtual-canonical state with d6=4 and singleton capacity
at least 9. It computes the span of all compatible singleton replacement
functionals. The exact maximum extra rank is 8, so no such shadow can realize
D6=2. Together with the committed d6=3 pair obstruction, this closes branch A.

All ranks are computed modulo P=2^127-1. Lucas-Lehmer certifies P prime. The
largest squared row norm and functional width encountered are checked against
P^2 by Hadamard's inequality, so the modular ranks equal the rational ranks.
"""

from collections import Counter
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
if HERE.name != "research":
    HERE = HERE / "research"
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_d3_cap9_extension_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_k7_A_d4_functional_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)
S, R = B.S, B.R
MOD = R.P

EXPECTED_CENSUS = {
    (9, 4): 204,
    (9, 5): 4568,
    (9, 6): 7911,
    (9, 7): 746,
    (9, 8): 107,
    (10, 5): 2738,
    (10, 6): 8373,
    (10, 7): 1348,
    (10, 8): 463,
    (11, 5): 1366,
    (11, 6): 7985,
    (11, 7): 1426,
    (11, 8): 1121,
    (12, 5): 132,
    (12, 6): 6458,
    (12, 7): 552,
    (12, 8): 1472,
    (13, 6): 2797,
    (13, 8): 936,
    (14, 6): 366,
    (14, 8): 396,
}


def rank_mod_rows(rows):
    if not rows:
        return 0
    a = [[int(x) % MOD for x in row] for row in rows]
    nr = len(a)
    nc = len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pv = a[rank][col]
        for i in range(rank + 1, nr):
            q = a[i][col]
            if q:
                a[i] = [(pv * x - q * y) % MOD for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def relation_rows_line(ext_global, touched, states, line):
    rows = [S.COMPLETE_T[b] for b, state in zip(touched, states) if state == 7]
    line_key = R.rowspace_key((line,))
    alphas = R.nullspace_int(line_key, 6)
    assert len(alphas) == 5
    for alpha in alphas:
        tvec = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext_global))
            for j in range(15)
        ]
        for block, state in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][block][0] for i, e in enumerate(ext_global))
            vy = sum(alpha[i] * R.QCOMP[e][block][1] for i, e in enumerate(ext_global))
            beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
            ids = R.BLOCKS[block]
            for local_index, coefficient in enumerate(beta):
                if coefficient:
                    for j in range(15):
                        tvec[j] += coefficient * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tuple(tvec))
    return rows


def singleton_functional(ext_global, block, state, line, complete_index, c):
    out = [0] * (c + 5)
    out[complete_index[block]] = 1
    line_key = R.rowspace_key((line,))
    for i, alpha in enumerate(R.nullspace_int(line_key, 6)):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext_global))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext_global))
        beta_complete = R.solve_local_coeffs_int(7, (-vx, -vy))
        beta_singleton = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [beta_singleton[j] - beta_complete[j] for j in range(3)]
        lam = diff[0]
        assert diff == [lam, -lam, -lam]
        out[c + i] = -lam
    return tuple(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--cover-cache",
        help="optional pickle containing (keys, six_augmentation_cover, local_cycle_info)",
    )
    parser.add_argument("--cover-start", type=int, default=0)
    parser.add_argument("--cover-end", type=int)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert MOD * MOD > 12 ** 15

    keys, cover, info = B.load_cover(args.cover_cache)
    local_to_global, _ = S.local_cycle_data(keys)
    assert len(cover) == 325955

    start = args.cover_start
    end = len(cover) if args.cover_end is None else args.cover_end
    assert 0 <= start <= end <= len(cover)

    rank_cache = {}
    census = Counter()
    synchronized_states = 0
    max_extra = 0
    max_norm2 = 0
    max_width = 0
    max_singleton_multiplicity = 0

    for ext_local in cover[start:end]:
        values, lines, empty_line, singleton_lines = S.block_profile(ext_local, info)
        ext_global = tuple(local_to_global[i] for i in ext_local)
        for line in lines:
            if sum(x != 0 for x in line) < 2:
                continue
            synchronized_states += 1
            complete = tuple(sorted(block for block in values if empty_line[block] != line))
            rank_complete = rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([S.COMPLETE_T[block] for block in complete])
                rank_cache[complete] = rank_complete
            if len(complete) - rank_complete != 4:
                continue

            singleton_state = []
            for block in complete:
                options = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singleton_lines[block])
                    if local_line is None or local_line == line
                )
                max_singleton_multiplicity = max(max_singleton_multiplicity, len(options))
                if options:
                    assert len(options) == 1
                    singleton_state.append((block, options[0]))
            capacity = len(singleton_state)
            if capacity < 9:
                continue

            touched = tuple(sorted(values))
            complete_set = set(complete)
            states = tuple(7 if block in complete_set else 0 for block in touched)
            rows = relation_rows_line(ext_global, touched, states, line)
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert rank_mod_rows(transposed) == rank_complete

            complete_index = {block: i for i, block in enumerate(complete)}
            functionals = [
                singleton_functional(
                    ext_global, block, state, line, complete_index, len(complete)
                )
                for block, state in singleton_state
            ]
            extra = rank_mod_rows(transposed + functionals) - rank_complete
            census[(capacity, extra)] += 1
            max_extra = max(max_extra, extra)

            max_width = max(max_width, len(rows))
            for row in transposed + functionals:
                max_norm2 = max(max_norm2, sum(x * x for x in row))

    if max_width:
        assert MOD * MOD > max_norm2 ** max_width
    assert max_extra <= 8
    assert max_singleton_multiplicity <= 1

    if start == 0 and end == len(cover):
        assert synchronized_states == 1751870
        assert dict(sorted(census.items())) == EXPECTED_CENSUS
        assert sum(census.values()) == 51465
        assert max_extra == 8
        assert max_norm2 == 42
        assert max_width == 23
        assert max_singleton_multiplicity == 1

    branch_A_D8 = -2
    branch_A_p = 11
    shadow_D6 = branch_A_D8 + 4
    shadow_d6 = 4
    required_extra = (6 + branch_A_p + 3 * shadow_d6 - shadow_D6 + 2) // 3
    assert shadow_D6 == 2
    assert required_extra == 9
    assert max_extra < required_extra

    print("PASS: six-no-root k5 d4/capacity>=9 singleton-functional obstruction")
    print("cover_range", (start, end))
    print("synchronized_states", synchronized_states)
    print("candidate_census", dict(sorted(census.items())))
    print("candidate_count", sum(census.values()))
    print("max_extra_rank", max_extra)
    print("branch_A_required_extra_rank", required_extra)
    print("max_singleton_multiplicity", max_singleton_multiplicity)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", (not max_width) or MOD * MOD > max_norm2 ** max_width)


if __name__ == "__main__":
    main()
