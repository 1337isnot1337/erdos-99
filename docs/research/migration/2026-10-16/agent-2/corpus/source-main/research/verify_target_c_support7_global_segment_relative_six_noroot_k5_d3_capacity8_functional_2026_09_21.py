#!/usr/bin/env python3
"""Exact d6=3 singleton-functional obstruction for k=7 C:(5,12,12).

The remaining all-singleton eight-no-root profile is

    C: D=-1, p=12, (d_v,q,s)=(5,12,12).

A committed good p-retaining pair deletion gives a synchronized six-row k=5
shadow with defect D6=3.  In the d6=3 subcase the replacement-functional
inequality is

    D6 >= 6 + p + 3*d6 - 3*s_f,

where s_f is the extra rank, modulo the canonical relation-column span, of the
selected compatible singleton replacement functionals.  Thus a realization
would require s_f >= 8, and in particular singleton capacity at least eight.

This verifier exhausts the exact S7 six-row augmentation cover and every
synchronized rank-one virtual-canonical state with d6=3 and singleton capacity
at least eight.  It computes the span of all compatible singleton replacement
functionals.  There are exactly 324 such states.  Their (capacity, extra-rank)
census is

    (8,3): 19, (8,4): 97, (9,4): 144, (10,4): 64.

Hence the exact maximum extra rank is four, far below the required eight.  The
d6=3 side of C:(5,12,12) is therefore impossible; the larger two-cycle
pair-extension search is not needed for this subcase.

All ranks are computed modulo P=2^127-1.  Lucas-Lehmer certifies P prime.  The
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
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_d4_capacity9_functional_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_k7_C_d3_functional_base", BASE)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)
B, S, R = F.B, F.S, F.R
MOD = R.P

EXPECTED_CENSUS = {
    (8, 3): 19,
    (8, 4): 97,
    (9, 4): 144,
    (10, 4): 64,
}


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
    candidate_states = 0
    threshold_survivors = 0
    witnesses = []
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
            if len(complete) - rank_complete != 3:
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
            if capacity < 8:
                continue

            candidate_states += 1
            touched = tuple(sorted(values))
            complete_set = set(complete)
            states = tuple(7 if block in complete_set else 0 for block in touched)
            rows = F.relation_rows_line(ext_global, touched, states, line)
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert F.rank_mod_rows(transposed) == rank_complete

            complete_index = {block: i for i, block in enumerate(complete)}
            functionals = [
                F.singleton_functional(
                    ext_global, block, state, line, complete_index, len(complete)
                )
                for block, state in singleton_state
            ]
            extra = F.rank_mod_rows(transposed + functionals) - rank_complete
            census[(capacity, extra)] += 1
            max_extra = max(max_extra, extra)
            if extra >= 8:
                threshold_survivors += 1
                if len(witnesses) < 20:
                    witnesses.append((ext_local, line, capacity, extra))

            max_width = max(max_width, len(rows))
            for row in transposed + functionals:
                max_norm2 = max(max_norm2, sum(x * x for x in row))

    assert max_singleton_multiplicity <= 1
    if max_width:
        assert MOD * MOD > max_norm2 ** max_width

    branch_C_D8 = -1
    branch_C_p = 12
    shadow_D6 = branch_C_D8 + 4
    shadow_d6 = 3
    required_extra = (6 + branch_C_p + 3 * shadow_d6 - shadow_D6 + 2) // 3
    assert shadow_D6 == 3
    assert required_extra == 8
    assert max_extra < required_extra
    assert threshold_survivors == 0

    if start == 0 and end == len(cover):
        assert synchronized_states == 1751870
        assert candidate_states == 324
        assert dict(sorted(census.items())) == EXPECTED_CENSUS
        assert max_extra == 4
        assert max_norm2 == 31
        assert max_width == 19
        assert max_singleton_multiplicity == 1

    print("PASS: C:(5,12,12) d6=3 singleton-functional obstruction")
    print("cover_range", (start, end))
    print("synchronized_states", synchronized_states)
    print("candidate_census", dict(sorted(census.items())))
    print("candidate_count", candidate_states)
    print("max_extra_rank", max_extra)
    print("required_extra_rank", required_extra)
    print("threshold_survivor_count", threshold_survivors)
    print("survivor_examples", witnesses)
    print("max_singleton_multiplicity", max_singleton_multiplicity)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", (not max_width) or MOD * MOD > max_norm2 ** max_width)


if __name__ == "__main__":
    main()
