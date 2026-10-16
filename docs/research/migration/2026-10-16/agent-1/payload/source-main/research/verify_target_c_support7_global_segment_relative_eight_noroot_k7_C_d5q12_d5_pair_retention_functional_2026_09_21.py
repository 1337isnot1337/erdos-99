#!/usr/bin/env python3
"""Pair-retention functional obstruction for k=7 C:(5,12,12), d6=5.

The sole remaining profile in the current eight-no-root split is

    C: D=-1, p=12, (d_v,q,s)=(5,12,12),

and its only unresolved six-row shadow has d6=5.  For a committed good
p-retaining pair deletion the six-row shadow has D6=3.  Replacement-functional
accounting forces at least ten selected singleton replacements whose six-row
functionals contribute at least ten dimensions modulo the canonical relation
column span.

Restore either deleted cycle.  The established seven-row alternatives are

    d7=4 with singleton capacity >=10, or
    d7=5 with singleton capacity >=11.

Every six-row singleton selected by an actual eight-row target must remain
compatible in both one-cycle restorations.  Thus the selected six-row set is a
subset of the intersection of the singleton sets retained by the two good
seven-row lifts.  Functional rank is monotone under taking subsets.  Therefore
an actual target requires some pair of good one-cycle lifts whose retained
intersection still contributes at least ten functional dimensions.

This verifier exhausts the exact 325955-representative six-row augmentation
cover, every synchronized d6=5 state of singleton capacity at least ten whose
full compatible singleton span already reaches the necessary extra rank ten,
and every pair of qualifying one-cycle lifts.  It deliberately does NOT impose
the full eight-row compatibility condition: this is an over-approximation.  If
even that larger family has retained-intersection extra rank at most nine,
then no actual eight-row target can exist.

Seven-row profiles are updated incrementally from the six-row profile.  The
optional --crosscheck flag recomputes the corresponding full block profiles
and asserts equality of candidate coefficient lines, complete sets, and
singleton capacities.  This is intended for small validation ranges.

All ranks use P=2^127-1.  Lucas-Lehmer primality plus the observed Hadamard
bound certifies every functional-rank decision over Q.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
FUNC_PATH = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_d5_capacity10_functional_2026_09_21.py"
EXT_PATH = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_C_d5q12_d3_pair_extension_2026_09_21.py"

spec = importlib.util.spec_from_file_location("e99_C_d5_pair_retention_func", FUNC_PATH)
D5 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(D5)

spec = importlib.util.spec_from_file_location("e99_C_d5_pair_retention_ext", EXT_PATH)
E = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(E)

B, S, R = D5.B, D5.S, D5.R
assert E.R.P == R.P
STATE_INDEX = {1: 0, 2: 1, 4: 2}


def extended_block_profile(old_values, xy):
    """Extend one six-row block profile by one exact quotient coordinate."""
    values = old_values if old_values is not None else ((0, 0),) * 6
    x, y = xy
    xrow = tuple(v[0] for v in values) + (x,)
    yrow = tuple(v[1] for v in values) + (y,)
    px = S.primitive_line(xrow)
    py = S.primitive_line(yrow)
    if px is None:
        empty = py
    elif py is None or px == py:
        empty = px
    else:
        empty = None

    singles = []
    for lx, ly in R.LOCAL:
        singles.append(
            S.primitive_line(
                tuple(lx * v[1] - ly * v[0] for v in values)
                + (lx * y - ly * x,)
            )
        )
    return empty, tuple(singles)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--cover-cache",
        help="optional pickle containing (keys, six_augmentation_cover, local_cycle_info)",
    )
    ap.add_argument("--cover-start", type=int, default=0)
    ap.add_argument("--cover-end", type=int)
    ap.add_argument(
        "--crosscheck",
        action="store_true",
        help="recompute seven-row block profiles and assert incremental equality",
    )
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert max(sum(x * x for x in row) for row in S.COMPLETE_T) == 12
    assert R.P * R.P > 12 ** 15

    keys, cover, info = B.load_cover(args.cover_cache)
    info = tuple(
        tuple((block, int(x), int(y)) for block, x, y in cycle)
        for cycle in info
    )
    local_to_global, _ = S.local_cycle_data(keys)
    assert len(cover) == 325955

    start = args.cover_start
    end = len(cover) if args.cover_end is None else args.cover_end
    assert 0 <= start <= end <= len(cover)

    all_cycles = set(range(105))
    rank_cache = {}

    def deficiency(complete_set):
        complete_set = tuple(sorted(complete_set))
        cached = rank_cache.get(complete_set)
        if cached is not None:
            return cached
        value = len(complete_set) - R.rank_mod(
            [S.COMPLETE_T[block] for block in complete_set]
        )
        rank_cache[complete_set] = value
        return value

    synchronized_states = 0
    functional_witness_states = 0
    seven_threshold_lifts = 0
    seven_d4_lifts = 0
    seven_d5_lifts = 0
    lift_last_coordinate = Counter()
    pair_lifts = 0
    pair_intersection_sizes = Counter()
    pair_extra_census = Counter()
    rank_tested_pairs = 0
    max_pair_retained_count = 0
    max_pair_retained_extra = 0
    threshold_pair_examples = []
    crosschecks = 0
    max_functional_norm2 = 0
    max_functional_width = 0
    max_singleton_multiplicity = 0

    for cover_index, ext6 in enumerate(cover[start:end], start=start):
        values6, lines6, empty6, singles6 = S.block_profile(ext6, info)
        ext6_global = tuple(local_to_global[i] for i in ext6)
        values6_blocks = set(values6)

        for line6 in lines6:
            if sum(x != 0 for x in line6) < 2:
                continue
            synchronized_states += 1

            complete6 = tuple(
                sorted(block for block in values6 if empty6[block] != line6)
            )
            rank6 = R.rank_mod([S.COMPLETE_T[block] for block in complete6])
            if len(complete6) - rank6 != 5:
                continue

            singleton_state6 = {}
            for block in complete6:
                options = tuple(
                    (1, 2, 4)[i]
                    for i, local_line in enumerate(singles6[block])
                    if local_line is None or local_line == line6
                )
                max_singleton_multiplicity = max(
                    max_singleton_multiplicity, len(options)
                )
                if options:
                    assert len(options) == 1
                    singleton_state6[block] = options[0]
            if len(singleton_state6) < 10:
                continue

            touched6 = tuple(sorted(values6))
            complete6_set = set(complete6)
            canonical_states6 = tuple(
                7 if block in complete6_set else 0 for block in touched6
            )
            rows6 = D5.F.relation_rows_line(
                ext6_global, touched6, canonical_states6, line6
            )
            assert R.rank_mod(rows6) == rank6
            transposed6 = [
                tuple(rows6[j][k] for j in range(len(rows6)))
                for k in range(15)
            ]
            assert D5.F.rank_mod_rows(transposed6) == rank6

            complete_index6 = {block: i for i, block in enumerate(complete6)}
            functionals = {
                block: D5.F.singleton_functional(
                    ext6_global,
                    block,
                    state,
                    line6,
                    complete_index6,
                    len(complete6),
                )
                for block, state in singleton_state6.items()
            }
            functional_rows = transposed6 + list(functionals.values())
            extra6 = D5.F.rank_mod_rows(functional_rows) - rank6
            if extra6 < 10:
                continue
            functional_witness_states += 1

            max_functional_width = max(max_functional_width, len(rows6))
            for row in functional_rows:
                max_functional_norm2 = max(
                    max_functional_norm2, sum(x * x for x in row)
                )

            empty_blocks = {
                block for block in values6 if empty6[block] == line6
            }
            generator_blocks = {
                block
                for block in values6
                if empty6[block] == line6
                or any(local_line == line6 for local_line in singles6[block])
            }
            zero_line = line6 + (0,)
            good = []

            for cycle in all_cycles.difference(ext6):
                cycle_map = {block: (x, y) for block, x, y in info[cycle]}
                cycle_blocks = set(cycle_map)
                profiles = {
                    block: extended_block_profile(values6.get(block), xy)
                    for block, xy in cycle_map.items()
                }

                candidates = set()
                if generator_blocks - cycle_blocks:
                    candidates.add(zero_line)
                for block in cycle_blocks & values6_blocks:
                    empty7, singles7 = profiles[block]
                    if empty6[block] == line6 and empty7 is not None:
                        candidates.add(empty7)
                    for i, local6 in enumerate(singles6[block]):
                        if local6 == line6 and singles7[i] is not None:
                            candidates.add(singles7[i])
                candidates = {
                    line7
                    for line7 in candidates
                    if S.primitive_line(line7[:6]) == line6
                }

                if args.crosscheck:
                    values7_ref, lines7_ref, empty7_ref, singles7_ref = B.block_profile(
                        ext6 + (cycle,), info
                    )
                    expected = {
                        line7
                        for line7 in lines7_ref
                        if S.primitive_line(line7[:6]) == line6
                    }
                    assert candidates == expected, (
                        cover_index,
                        ext6,
                        line6,
                        cycle,
                        candidates,
                        expected,
                    )

                for line7 in candidates:
                    added = set(cycle_blocks - values6_blocks)
                    for block in empty_blocks:
                        empty7 = (
                            profiles[block][0]
                            if block in cycle_blocks
                            else zero_line
                        )
                        if empty7 != line7:
                            added.add(block)
                    complete7 = complete6_set | added

                    cap7 = 0
                    for block in complete7:
                        if block in cycle_blocks:
                            singleton_lines7 = profiles[block][1]
                            compatible = any(
                                local_line is None or local_line == line7
                                for local_line in singleton_lines7
                            )
                        else:
                            compatible = any(
                                local_line is None
                                or (local_line == line6 and zero_line == line7)
                                for local_line in singles6[block]
                            )
                        cap7 += compatible

                    if args.crosscheck:
                        complete_ref = {
                            block
                            for block in values7_ref
                            if empty7_ref[block] != line7
                        }
                        cap_ref = sum(
                            any(
                                local_line is None or local_line == line7
                                for local_line in singles7_ref[block]
                            )
                            for block in complete_ref
                        )
                        assert complete7 == complete_ref, (
                            cover_index,
                            cycle,
                            line7,
                            complete7,
                            complete_ref,
                        )
                        assert cap7 == cap_ref, (
                            cover_index,
                            cycle,
                            line7,
                            cap7,
                            cap_ref,
                        )
                        crosschecks += 1

                    d7 = deficiency(complete7)
                    if d7 == 4 and cap7 >= 10:
                        seven_d4_lifts += 1
                    elif d7 == 5 and cap7 >= 11:
                        seven_d5_lifts += 1
                    else:
                        continue
                    seven_threshold_lifts += 1
                    lift_last_coordinate[line7[-1]] += 1

                    retained = []
                    for block, state in singleton_state6.items():
                        index = STATE_INDEX[state]
                        if block in cycle_blocks:
                            local_line = profiles[block][1][index]
                            compatible = local_line is None or local_line == line7
                        else:
                            local_line = singles6[block][index]
                            compatible = local_line is None or (
                                local_line == line6 and zero_line == line7
                            )
                        if compatible:
                            retained.append(block)
                    good.append((cycle, line7, frozenset(retained)))

            for (cycle_a, line_a, retained_a), (
                cycle_b,
                line_b,
                retained_b,
            ) in combinations(good, 2):
                if cycle_a == cycle_b:
                    continue
                pair_lifts += 1
                retained = retained_a & retained_b
                retained_count = len(retained)
                pair_intersection_sizes[retained_count] += 1
                max_pair_retained_count = max(
                    max_pair_retained_count, retained_count
                )
                if retained_count < 10:
                    continue

                rank_tested_pairs += 1
                extra = (
                    D5.F.rank_mod_rows(
                        transposed6 + [functionals[block] for block in retained]
                    )
                    - rank6
                )
                pair_extra_census[(retained_count, extra)] += 1
                max_pair_retained_extra = max(max_pair_retained_extra, extra)
                if extra >= 10 and len(threshold_pair_examples) < 50:
                    threshold_pair_examples.append(
                        (
                            cover_index,
                            ext6,
                            line6,
                            cycle_a,
                            line_a,
                            cycle_b,
                            line_b,
                            retained_count,
                            extra,
                        )
                    )

    assert max_singleton_multiplicity <= 1
    if max_functional_width:
        assert R.P * R.P > max_functional_norm2 ** max_functional_width

    print("six_augmentation_cover", len(cover))
    print("cover_range", (start, end))
    print("synchronized_states", synchronized_states)
    print("functional_witness_states", functional_witness_states)
    print("seven_threshold_lifts", seven_threshold_lifts)
    print("seven_d4_lifts", seven_d4_lifts)
    print("seven_d5_lifts", seven_d5_lifts)
    print("lift_last_coordinate", dict(sorted(lift_last_coordinate.items())))
    print("pair_lifts", pair_lifts)
    print("pair_intersection_sizes", dict(sorted(pair_intersection_sizes.items())))
    print("rank_tested_pairs", rank_tested_pairs)
    print("pair_extra_census", dict(sorted(pair_extra_census.items())))
    print("max_pair_retained_count", max_pair_retained_count)
    print("max_pair_retained_extra", max_pair_retained_extra)
    print("required_pair_retained_extra", 10)
    print("threshold_pair_examples", threshold_pair_examples)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_singleton_multiplicity", max_singleton_multiplicity)
    print("max_row_norm_squared", max_functional_norm2)
    print("max_functional_width", max_functional_width)
    print(
        "hadamard_exact_rank_bound",
        (not max_functional_width)
        or R.P * R.P > max_functional_norm2 ** max_functional_width,
    )
    print("incremental_profile_crosschecks", crosschecks)

    if threshold_pair_examples:
        raise SystemExit(
            "FAIL: a pair of good lifts retains singleton-functional extra rank >=10"
        )
    print(
        "PASS: no pair of good lifts retains the required singleton-functional extra rank 10"
    )


if __name__ == "__main__":
    main()
