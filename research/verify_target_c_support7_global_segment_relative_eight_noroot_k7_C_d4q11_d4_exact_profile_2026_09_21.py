#!/usr/bin/env python3
"""Exactify the d6=4 functional witnesses for k=7 C:(4,11,10).

The remaining eight-no-root profile is

    D=-1, p=12, (d_v,q,s)=(4,11,10),

with ten singleton changed blocks and one pair changed block.  The committed
good-pair reduction supplies a p-retaining synchronized six-row shadow.  The
d6=3 side is already closed, so this verifier treats d6=4.

For d6=4 the six-row containment bound forces at least nine changed canonical-
complete blocks.  If the global pair block is not one of them, at least nine
singleton replacements occur and the committed d4 singleton-functional theorem
excludes the state.  Hence every unresolved state has the pair block among the
six-row complete blocks and at least eight compatible singleton replacements.
The committed singleton-plus-pair audit shows that the corresponding replacement
functionals must gain at least nine relative directions.

This verifier keeps only those exact six-row d6=4/capacity>=8 states and exact
(pair block, pair state) choices whose singleton-plus-pair functional span can
gain at least nine directions.  It then restores every pair of deleted no-root
cycles through the already-forced seven-row d7=4/capacity>=9 shadows.  A pair
of one-row lifts determines a candidate eight-row coefficient line, but the
block involving both restored cycles can impose an additional compatibility
condition, so only candidate lines that occur in the full eight-row block
profile are retained.  The target then requires global d8=4/capacity>=10 and
exhausts the actual global root profile: exactly ten singleton blocks and the
retained pair block/state.  Each actual profile is checked against the exact
global constraint line and reranked directly.

A state with D=|A|-3*delta(A)<=-1 would survive all necessary conditions for the
target branch and is therefore reported as a counterexample candidate.  If the
full scan has none, the d6=4 side of C:(4,11,10) is closed.

All modular ranks use P=2^127-1.  Lucas-Lehmer certifies P prime, and the script
checks a Hadamard bound for every direct relation-rank computation, so those
ranks equal the ranks over Q.
"""

from collections import Counter
from itertools import combinations, product
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
FUNC_PATH = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_d4_capacity8_singleton_pair_functional_2026_09_21.py"
EXT_PATH = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d4q11_d3_pair_extension_2026_09_21.py"

spec = importlib.util.spec_from_file_location("e99_C_d4q11_d4_functional", FUNC_PATH)
D4 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(D4)

spec = importlib.util.spec_from_file_location("e99_C_d4q11_extension", EXT_PATH)
E = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(E)

B, S, R = D4.B, D4.S, D4.R
assert E.R.P == R.P


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
    ap.add_argument("--cover-start", type=int, default=0)
    ap.add_argument("--cover-end", type=int)
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert R.P * R.P > 12 ** 15

    keys, cover, info = B.load_cover(args.cover_cache)
    local_to_global, _ = S.local_cycle_data(keys)
    assert len(cover) == 325955

    start = args.cover_start
    end = len(cover) if args.cover_end is None else args.cover_end
    assert 0 <= start <= end <= len(cover)

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

    all_cycles = set(range(105))
    synchronized_states = 0
    d4_capacity_ge8 = Counter()
    functional_witness_states = 0
    viable_pair_choice_census = Counter()
    seven_row_lift_multiplicity = Counter()
    pair_cycle_count = 0
    pair_line_count = 0
    compatible_pair_line_count = 0
    incompatible_pair_line_count = 0
    structural_global_d4 = 0
    structural_capacity = Counter()
    pair_choice_survivors = 0
    singleton_choice_census = Counter()
    actual_state_tests = 0
    exact_constraint_line_tests = 0
    defect_census = Counter()
    bad = []
    max_norm2 = 0
    max_relation_rows = 0
    max_functional_norm2 = 0
    max_functional_width = 0
    max_singleton_multiplicity = 0

    for cover_index, ext6 in enumerate(cover[start:end], start=start):
        values6, lines6, empty6, singles6 = S.block_profile(ext6, info)
        ext6_global = tuple(local_to_global[i] for i in ext6)

        for line6 in lines6:
            if sum(x != 0 for x in line6) < 2:
                continue
            synchronized_states += 1

            complete6 = tuple(
                sorted(block for block in values6 if empty6[block] != line6)
            )
            rank6 = len(complete6) - deficiency(complete6)
            if len(complete6) - rank6 != 4:
                continue

            singleton_state6 = {}
            for block in complete6:
                options = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singles6[block])
                    if local_line is None or local_line == line6
                )
                max_singleton_multiplicity = max(max_singleton_multiplicity, len(options))
                if options:
                    assert len(options) == 1
                    singleton_state6[block] = options[0]
            cap6 = len(singleton_state6)
            if cap6 < 8:
                continue
            d4_capacity_ge8[cap6] += 1

            touched6 = tuple(sorted(values6))
            complete6_set = set(complete6)
            canonical_states6 = tuple(
                7 if block in complete6_set else 0 for block in touched6
            )
            rows6 = D4.F.relation_rows_line(
                ext6_global, touched6, canonical_states6, line6
            )
            assert R.rank_mod(rows6) == rank6
            transposed6 = [
                tuple(rows6[j][k] for j in range(len(rows6)))
                for k in range(15)
            ]
            assert D4.F.rank_mod_rows(transposed6) == rank6

            c6 = len(complete6)
            complete_index6 = {block: i for i, block in enumerate(complete6)}
            singleton_functionals = {
                block: D4.replacement_functional(
                    ext6_global, block, state, line6, complete_index6, c6
                )
                for block, state in singleton_state6.items()
            }
            functional_rows = transposed6 + list(singleton_functionals.values())
            for row in functional_rows:
                max_functional_norm2 = max(
                    max_functional_norm2, sum(x * x for x in row)
                )
            max_functional_width = max(max_functional_width, len(rows6))
            singleton_extra = D4.F.rank_mod_rows(functional_rows) - rank6
            if singleton_extra < 8:
                continue

            viable_pairs = []
            for pair_block in complete6:
                others = [
                    vec for block, vec in singleton_functionals.items()
                    if block != pair_block
                ]
                for pair_state in (3, 5, 6):
                    pair_vec = D4.replacement_functional(
                        ext6_global,
                        pair_block,
                        pair_state,
                        line6,
                        complete_index6,
                        c6,
                    )
                    max_functional_norm2 = max(
                        max_functional_norm2, sum(x * x for x in pair_vec)
                    )
                    extra = (
                        D4.F.rank_mod_rows(transposed6 + others + [pair_vec])
                        - rank6
                    )
                    if extra >= 9:
                        viable_pairs.append((pair_block, pair_state, pair_vec))

            if not viable_pairs:
                continue
            functional_witness_states += 1
            viable_pair_choice_census[len(viable_pairs)] += 1

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
                    if capacity(complete7, line7, singles7) < 9:
                        continue
                    found.append(line7)
                if found:
                    unique = tuple(dict.fromkeys(found))
                    good[cycle] = unique
                    seven_row_lift_multiplicity[len(unique)] += 1

            for a, b in combinations(sorted(good), 2):
                pair_cycle_count += 1
                lines8_for_pair = set()
                for line7_a in good[a]:
                    for line7_b in good[b]:
                        lines8_for_pair.add(E.combine(line6, line7_a, line7_b))
                pair_line_count += len(lines8_for_pair)
                ext8 = ext6 + (a, b)
                ext8_global = tuple(local_to_global[i] for i in ext8)

                for line8 in lines8_for_pair:
                    values8, lines8, empty8, singles8 = B.block_profile(ext8, info)
                    if line8 not in lines8:
                        incompatible_pair_line_count += 1
                        continue
                    compatible_pair_line_count += 1
                    complete8 = tuple(
                        sorted(block for block in values8 if empty8[block] != line8)
                    )
                    if deficiency(complete8) != 4:
                        continue
                    cap8 = capacity(complete8, line8, singles8)
                    if cap8 < 10:
                        continue
                    structural_global_d4 += 1
                    structural_capacity[cap8] += 1

                    singleton_options = {}
                    for block in complete8:
                        options = tuple(
                            (1, 2, 4)[i]
                            for i, local_line in enumerate(singles8[block])
                            if local_line is None or local_line == line8
                        )
                        max_singleton_multiplicity = max(
                            max_singleton_multiplicity, len(options)
                        )
                        if options:
                            singleton_options[block] = options

                    touched8 = tuple(sorted(values8))
                    position8 = {block: i for i, block in enumerate(touched8)}
                    target_line_key = R.rowspace_key((line8,))
                    complete8_set = set(complete8)

                    for pair_block, pair_state, pair_vec6 in viable_pairs:
                        if pair_block not in complete8_set:
                            continue
                        eligible_singletons = tuple(
                            block
                            for block in sorted(singleton_options)
                            if block != pair_block
                        )
                        if len(eligible_singletons) < 10:
                            continue
                        pair_choice_survivors += 1

                        choose_count = 0
                        for singleton_blocks in combinations(eligible_singletons, 10):
                            choose_count += 1
                            for singleton_states in product(
                                *(singleton_options[block] for block in singleton_blocks)
                            ):
                                selected_six_functionals = []
                                selected_six_count = 0
                                for block, state in zip(singleton_blocks, singleton_states):
                                    if singleton_state6.get(block) == state:
                                        selected_six_count += 1
                                        selected_six_functionals.append(
                                            singleton_functionals[block]
                                        )
                                if selected_six_count < 8:
                                    continue
                                six_extra = (
                                    D4.F.rank_mod_rows(
                                        transposed6
                                        + selected_six_functionals
                                        + [pair_vec6]
                                    )
                                    - rank6
                                )
                                if six_extra < 9:
                                    continue

                                states = [
                                    7 if block in complete8_set else 0
                                    for block in touched8
                                ]
                                for block, state in zip(
                                    singleton_blocks, singleton_states
                                ):
                                    states[position8[block]] = state
                                states[position8[pair_block]] = pair_state

                                incomplete_cost = sum(
                                    R.STATES[state][1]
                                    for state in states
                                    if state != 7
                                )
                                assert incomplete_cost == 12
                                actual_state_tests += 1

                                key = constraint_key(ext8_global, touched8, states)
                                if key != target_line_key:
                                    continue
                                exact_constraint_line_tests += 1

                                rows = relation_rows(
                                    ext8_global, touched8, states, line8
                                )
                                max_relation_rows = max(max_relation_rows, len(rows))
                                for row in rows:
                                    max_norm2 = max(
                                        max_norm2, sum(x * x for x in row)
                                    )
                                delta = R.rank_mod(rows)
                                defect = 8 + incomplete_cost - 3 * delta
                                defect_census[defect] += 1
                                if defect <= -1 and len(bad) < 20:
                                    bad.append(
                                        (
                                            cover_index,
                                            ext8,
                                            line8,
                                            pair_block,
                                            pair_state,
                                            tuple(zip(singleton_blocks, singleton_states)),
                                            defect,
                                        )
                                    )
                        singleton_choice_census[choose_count] += 1

    if max_functional_width:
        assert R.P * R.P > max_functional_norm2 ** max_functional_width
    if max_relation_rows:
        assert R.P * R.P > max_norm2 ** 15

    print("completed C:(4,11,10) d6=4 exact-profile scan")
    print("cover_range", (start, end))
    print("synchronized_states", synchronized_states)
    print("d4_capacity_ge8", dict(sorted(d4_capacity_ge8.items())))
    print("functional_witness_states", functional_witness_states)
    print("viable_pair_choice_census", dict(sorted(viable_pair_choice_census.items())))
    print("seven_row_lift_multiplicity", dict(sorted(seven_row_lift_multiplicity.items())))
    print("pair_cycle_count", pair_cycle_count)
    print("pair_line_count", pair_line_count)
    print("compatible_pair_line_count", compatible_pair_line_count)
    print("incompatible_pair_line_count", incompatible_pair_line_count)
    print("structural_global_d4", structural_global_d4)
    print("structural_capacity", dict(sorted(structural_capacity.items())))
    print("pair_choice_survivors", pair_choice_survivors)
    print("singleton_choice_census", dict(sorted(singleton_choice_census.items())))
    print("actual_state_tests", actual_state_tests)
    print("exact_constraint_line_tests", exact_constraint_line_tests)
    print("defect_census", dict(sorted(defect_census.items())))
    print("D_le_minus1_count", sum(count for d, count in defect_census.items() if d <= -1))
    print("bad_examples", bad)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_singleton_multiplicity", max_singleton_multiplicity)
    print("max_functional_row_norm_squared", max_functional_norm2)
    print("max_functional_width", max_functional_width)
    print("functional_hadamard_exact_rank_bound", (not max_functional_width) or R.P * R.P > max_functional_norm2 ** max_functional_width)
    print("max_relation_row_norm_squared", max_norm2)
    print("max_relation_row_count", max_relation_rows)
    print("hadamard_exact_rank_bound", (not max_relation_rows) or R.P * R.P > max_norm2 ** 15)

    if bad:
        raise AssertionError("found C:(4,11,10) d6=4 exact-profile candidate")
    print("PASS: no C:(4,11,10) d6=4 exact-profile candidate")


if __name__ == "__main__":
    main()
