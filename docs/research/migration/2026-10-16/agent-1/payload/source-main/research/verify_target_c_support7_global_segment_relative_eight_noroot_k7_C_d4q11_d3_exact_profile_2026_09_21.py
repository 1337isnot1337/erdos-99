#!/usr/bin/env python3
"""Exactify the d6=3 extension survivors for k=7 C:(4,11,10).

The structural extension scan for the eight-no-root profile

    D=-1, p=12, (d_v,q,s)=(4,11,10)

starts from every synchronized six-row rank-one state with d6=3 and singleton
capacity at least seven, restores the two deleted no-root cycles through
seven-row d7=4/capacity>=9 shadows, and retains global d8=4 states with
singleton capacity at least ten.  That structural screen has survivors, so
capacity alone does not close the d6=3 side.

This verifier exactifies every structural survivor against the actual root-row
profile: ten singleton incomplete blocks and one pair incomplete block, total
root-incomplete cost p=12.  Every compatible singleton orientation, every
candidate pair block, and each of its three two-row pair states is tested.  It
recomputes the exact external constraint line and then the relative T-rank of
the actual family.  None has defect D=|A|-3*delta(A) <= -1; in fact every
actual profile tested has D=17.

Ranks are computed modulo P=2^127-1.  Lucas-Lehmer certifies P prime.  The
largest squared relation-row norm and the row count encountered are checked by
Hadamard's inequality, making each modular rank decision exact over Q.
"""

from collections import Counter
from itertools import combinations, product
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d3_pair_extension_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_C_d4q11_d3_exact_base", BASE)
E = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(E)
B, S, R = E.B, E.S, E.R

EXPECTED_BASE = {7: 78, 8: 116, 9: 144, 10: 64}


def relation_rows(ext_global, touched, states, line):
    rows = [S.COMPLETE_T[b] for b, state in zip(touched, states) if state == 7]
    line_key = R.rowspace_key((line,))
    alphas = R.nullspace_int(line_key, len(ext_global))
    assert len(alphas) == len(ext_global) - 1
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


def constraint_key(ext_global, touched, states):
    rows = []
    for block, state in zip(touched, states):
        rows.extend(R.local_constraint_key(ext_global, block, state))
    return R.rowspace_key(tuple(rows))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--cover-cache",
        help="optional pickle containing (keys, six_augmentation_cover, local_cycle_info)",
    )
    ap.add_argument("--base-start", type=int, default=0)
    ap.add_argument("--base-end", type=int)
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert R.P * R.P > 12 ** 15

    keys, cover, info = B.load_cover(args.cover_cache)
    local_to_global, _ = S.local_cycle_data(keys)
    rank_cache = {}

    def deficiency(complete_set):
        complete_set = tuple(complete_set)
        cached = rank_cache.get(complete_set)
        if cached is not None:
            return cached
        value = len(complete_set) - R.rank_mod(
            [S.COMPLETE_T[block] for block in complete_set]
        )
        rank_cache[complete_set] = value
        return value

    def capacity(complete_set, line, singleton_lines):
        return sum(
            any(local is None or local == line for local in singleton_lines[block])
            for block in complete_set
        )

    base_states = []
    base_capacity = Counter()
    synchronized_states = 0
    for ext6 in cover:
        values6, lines6, empty6, singles6 = S.block_profile(ext6, info)
        for line6 in lines6:
            if sum(x != 0 for x in line6) < 2:
                continue
            synchronized_states += 1
            complete6 = tuple(
                sorted(block for block in values6 if empty6[block] != line6)
            )
            if deficiency(complete6) != 3:
                continue
            cap6 = capacity(complete6, line6, singles6)
            if cap6 < 7:
                continue
            base_states.append((tuple(ext6), line6))
            base_capacity[cap6] += 1

    assert synchronized_states == 1751870
    assert dict(sorted(base_capacity.items())) == EXPECTED_BASE
    assert len(base_states) == 402

    start = args.base_start
    end = len(base_states) if args.base_end is None else args.base_end
    assert 0 <= start <= end <= len(base_states)

    all_cycles = set(range(105))
    structural_survivors = 0
    singleton_option_multiplicity = Counter()
    pair_block_candidate_count = Counter()
    actual_state_tests = 0
    exact_constraint_line_tests = 0
    defect_census = Counter()
    bad = []
    max_norm2 = 0
    max_relation_rows = 0

    for base_index, (ext6, line6) in enumerate(base_states[start:end], start=start):
        good = {}
        for cycle in sorted(all_cycles.difference(ext6)):
            ext7 = ext6 + (cycle,)
            values7, lines7, empty7, singles7 = B.block_profile(ext7, info)
            found = []
            for line7 in lines7:
                if S.primitive_line(line7[:6]) != line6:
                    continue
                complete7 = tuple(
                    sorted(block for block in values7 if empty7[block] != line7)
                )
                if deficiency(complete7) != 4:
                    continue
                if capacity(complete7, line7, singles7) >= 9:
                    found.append(line7)
            assert len(found) <= 1
            if found:
                good[cycle] = found[0]

        for a, b in combinations(sorted(good), 2):
            line8 = E.combine(line6, good[a], good[b])
            ext8 = ext6 + (a, b)
            values8, lines8, empty8, singles8 = B.block_profile(ext8, info)
            assert line8 in lines8
            complete8 = tuple(
                sorted(block for block in values8 if empty8[block] != line8)
            )
            if deficiency(complete8) != 4:
                continue
            if capacity(complete8, line8, singles8) < 10:
                continue

            structural_survivors += 1
            singleton_options = {}
            for block in complete8:
                options = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singles8[block])
                    if local_line is None or local_line == line8
                )
                if options:
                    singleton_options[block] = options
                    singleton_option_multiplicity[len(options)] += 1

            assert len(singleton_options) == 10
            singleton_blocks = tuple(sorted(singleton_options))
            pair_blocks = tuple(block for block in complete8 if block not in singleton_options)
            pair_block_candidate_count[len(pair_blocks)] += 1

            ext_global = tuple(local_to_global[i] for i in ext8)
            touched = tuple(sorted(values8))
            position = {block: i for i, block in enumerate(touched)}
            target_line_key = R.rowspace_key((line8,))

            for singleton_states in product(
                *(singleton_options[block] for block in singleton_blocks)
            ):
                for pair_block in pair_blocks:
                    for pair_state in (3, 5, 6):
                        states = [7 if block in complete8 else 0 for block in touched]
                        for block, state in zip(singleton_blocks, singleton_states):
                            states[position[block]] = state
                        states[position[pair_block]] = pair_state

                        incomplete_cost = sum(
                            R.STATES[state][1] for state in states if state != 7
                        )
                        assert incomplete_cost == 12
                        actual_state_tests += 1

                        key = constraint_key(ext_global, touched, states)
                        if key != target_line_key:
                            continue
                        exact_constraint_line_tests += 1

                        rows = relation_rows(ext_global, touched, states, line8)
                        max_relation_rows = max(max_relation_rows, len(rows))
                        for row in rows:
                            max_norm2 = max(max_norm2, sum(x * x for x in row))
                        delta = R.rank_mod(rows)
                        defect = 8 + sum(R.STATES[state][1] for state in states) - 3 * delta
                        defect_census[defect] += 1
                        if defect <= -1 and len(bad) < 20:
                            bad.append(
                                (
                                    base_index,
                                    ext8,
                                    line8,
                                    pair_block,
                                    pair_state,
                                    tuple(zip(singleton_blocks, singleton_states)),
                                    defect,
                                )
                            )

    if max_relation_rows:
        assert R.P * R.P > max_norm2 ** 15
    assert not bad

    if start == 0 and end == len(base_states):
        assert structural_survivors == 924
        assert dict(sorted(singleton_option_multiplicity.items())) == {1: 9240}
        assert dict(sorted(pair_block_candidate_count.items())) == {7: 594, 8: 330}
        assert actual_state_tests == 20394
        assert exact_constraint_line_tests == 20394
        assert dict(sorted(defect_census.items())) == {17: 20394}
        assert max_norm2 == 24
        assert max_relation_rows == 14

    print("PASS: C:(4,11,10) d6=3 structural survivors fail exact profile")
    print("six_augmentation_cover", len(cover))
    print("base_d3_capacity_ge7", dict(sorted(base_capacity.items())))
    print("base_state_count", len(base_states))
    print("base_range", (start, end))
    print("structural_survivors", structural_survivors)
    print("singleton_option_multiplicity", dict(sorted(singleton_option_multiplicity.items())))
    print("pair_block_candidate_count", dict(sorted(pair_block_candidate_count.items())))
    print("actual_state_tests", actual_state_tests)
    print("exact_constraint_line_tests", exact_constraint_line_tests)
    print("defect_census", dict(sorted(defect_census.items())))
    print("D_le_minus1_count", sum(count for d, count in defect_census.items() if d <= -1))
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_relation_row_norm_squared", max_norm2)
    print("max_relation_row_count", max_relation_rows)
    print("hadamard_exact_rank_bound", (not max_relation_rows) or R.P * R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
