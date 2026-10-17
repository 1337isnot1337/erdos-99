#!/usr/bin/env python3
"""Exact d6=3 pair-extension audit for k=7 C:(5,12,12).

The remaining all-singleton eight-no-root k=7 profile is

    C: D=-1, p=12, (d_v,q,s)=(5,12,12).

A committed good p-retaining pair deletion gives a synchronized six-row k=5
shadow with D6=3.  In the d6=3 subcase, replacement accounting forces at
least eight compatible singleton blocks.  Restoring either deleted cycle gives
a seven-row shadow of deficiency four or five.  The established containment
bounds force singleton capacity at least ten when d7=4 and at least eleven
when d7=5.  The global eight-row state must have d8=5 and singleton capacity
at least twelve.

This verifier exhausts every exact six-row d6=3/capacity>=8 state, every
restriction-compatible seven-row lift meeting the corresponding d7/capacity
threshold, and every compatible pair of one-cycle lifts.  A pair of one-cycle
lifts determines a candidate eight-row coefficient line, but the block involving
both restored cycles can impose an additional compatibility condition.  The
candidate is therefore retained only when it is an actual line of the full
eight-row block profile.  A successful run with zero global d8=5/capacity>=12
survivors certifies that the d6=3 side is impossible.

Complete-set ranks are exact over Q by the existing P=2^127-1
Lucas-Lehmer/Hadamard certificate.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io
import math

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_d3_cap9_extension_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_k7_C_d5_pair_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)
S, R = B.S, B.R

EXPECTED_BASE = {8: 116, 9: 144, 10: 64}


def combine(line6, line7_a, line7_b):
    """Recover the primitive eight-row line determined by two seven-row lifts."""
    pivot = next(i for i, x in enumerate(line6) if x)
    scale_a = Fraction(line7_a[pivot], line6[pivot])
    scale_b = Fraction(line7_b[pivot], line6[pivot])
    assert scale_a and scale_b
    assert all(Fraction(line7_a[i], 1) == scale_a * line6[i] for i in range(6))
    assert all(Fraction(line7_b[i], 1) == scale_b * line6[i] for i in range(6))
    vector = [Fraction(x, 1) for x in line6]
    vector.append(Fraction(line7_a[6], 1) / scale_a)
    vector.append(Fraction(line7_b[6], 1) / scale_b)
    denominator = 1
    for x in vector:
        denominator = math.lcm(denominator, x.denominator)
    return S.primitive_line(tuple(int(x * denominator) for x in vector))


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

    _keys, cover, info = B.load_cover(args.cover_cache)
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

    def profile(ext, line):
        values, lines, empty_line, singleton_lines = B.block_profile(ext, info)
        complete = tuple(sorted(block for block in values if empty_line[block] != line))
        capacity = sum(
            any(local is None or local == line for local in singleton_lines[block])
            for block in complete
        )
        return complete, capacity, lines

    base_states = []
    base_capacity = Counter()
    synchronized_states = 0
    for ext6 in cover:
        values6, lines6, empty6, singles6 = S.block_profile(ext6, info)
        for line6 in lines6:
            if sum(x != 0 for x in line6) < 2:
                continue
            synchronized_states += 1
            complete6 = tuple(sorted(block for block in values6 if empty6[block] != line6))
            if deficiency(complete6) != 3:
                continue
            capacity6 = sum(
                any(local is None or local == line6 for local in singles6[block])
                for block in complete6
            )
            if capacity6 < 8:
                continue
            base_states.append((tuple(ext6), line6))
            base_capacity[capacity6] += 1

    assert synchronized_states == 1751870
    assert dict(sorted(base_capacity.items())) == EXPECTED_BASE
    assert len(base_states) == 324

    start = args.base_start
    end = len(base_states) if args.base_end is None else args.base_end
    assert 0 <= start <= end <= len(base_states)

    all_cycles = set(range(105))
    seven_d4 = 0
    seven_d5 = 0
    seven_lift_multiplicity = Counter()
    pair_cycle_count = 0
    pair_line_count = 0
    compatible_pair_line_count = 0
    incompatible_pair_line_count = 0
    global_d5 = 0
    global_d5_capacity = Counter()
    survivor_count = 0
    survivor_examples = []

    for base_index, (ext6, line6) in enumerate(base_states[start:end], start=start):
        good = {}
        for cycle in sorted(all_cycles.difference(ext6)):
            ext7 = ext6 + (cycle,)
            values7, lines7, empty7, singles7 = B.block_profile(ext7, info)
            found = []
            for line7 in lines7:
                if S.primitive_line(line7[:6]) != line6:
                    continue
                complete7 = tuple(sorted(block for block in values7 if empty7[block] != line7))
                d7 = deficiency(complete7)
                capacity7 = sum(
                    any(local is None or local == line7 for local in singles7[block])
                    for block in complete7
                )
                if d7 == 4 and capacity7 >= 10:
                    seven_d4 += 1
                    found.append(line7)
                elif d7 == 5 and capacity7 >= 11:
                    seven_d5 += 1
                    found.append(line7)
            if found:
                unique = tuple(dict.fromkeys(found))
                good[cycle] = unique
                seven_lift_multiplicity[len(unique)] += 1

        for a, b in combinations(sorted(good), 2):
            pair_cycle_count += 1
            lines8_for_pair = set()
            for line7_a in good[a]:
                for line7_b in good[b]:
                    lines8_for_pair.add(combine(line6, line7_a, line7_b))
            pair_line_count += len(lines8_for_pair)
            ext8 = ext6 + (a, b)
            for line8 in lines8_for_pair:
                complete8, capacity8, lines8 = profile(ext8, line8)
                if line8 not in lines8:
                    incompatible_pair_line_count += 1
                    continue
                compatible_pair_line_count += 1
                if deficiency(complete8) != 5:
                    continue
                global_d5 += 1
                global_d5_capacity[capacity8] += 1
                if capacity8 >= 12:
                    survivor_count += 1
                    if len(survivor_examples) < 20:
                        survivor_examples.append(
                            (base_index, ext6, line6, a, b, line8, capacity8)
                        )

    print("six_augmentation_cover", len(cover))
    print("synchronized_six_row_states", synchronized_states)
    print("base_d3_capacity_ge8", dict(sorted(base_capacity.items())))
    print("base_state_count", len(base_states))
    print("base_range", (start, end))
    print("seven_d4_threshold_lifts", seven_d4)
    print("seven_d5_threshold_lifts", seven_d5)
    print("seven_lift_multiplicity", dict(sorted(seven_lift_multiplicity.items())))
    print("pair_cycle_count", pair_cycle_count)
    print("pair_line_count", pair_line_count)
    print("compatible_pair_line_count", compatible_pair_line_count)
    print("incompatible_pair_line_count", incompatible_pair_line_count)
    print("global_d5", global_d5)
    print("global_d5_capacity", dict(sorted(global_d5_capacity.items())))
    print("global_d5_capacity_ge12", survivor_count)
    print("survivor_examples", survivor_examples)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)

    if survivor_count:
        raise SystemExit("FAIL: d6=3 pair-extension survivors exist")
    print("PASS: no d6=3 shadow extends to global d8=5/capacity>=12")


if __name__ == "__main__":
    main()
