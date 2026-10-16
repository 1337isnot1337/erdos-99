#!/usr/bin/env python3
"""Exact d6=3 extension scan for the remaining k=7 profile C:(4,11,10).

The current eight-no-root k=7 reduction leaves branch C with

    D=-1, p=12, (d_v,q,s)=(4,11,10)

and the all-singleton profile (5,12,12).  For (4,11,10), the committed good
pair-shadow reduction supplies a p-retaining synchronized six-row k=5 shadow.
If that shadow has deficiency d6=3, the containment inequality forces at least
8 changed virtual-complete blocks.  Since the global row budget contains ten
singleton blocks and one pair block, the six-row shadow has singleton capacity
at least 7.

For either one-cycle intermediate seven-row shadow, D7=1 and p=12.  Deficiency
2 is already excluded by the exact seven-row capacity bound.  Deficiency 3 is
excluded by the committed six-to-seven theorem: no six-row d=3/capacity>=6
state extends to a seven-row d=3/capacity>=7 state.  Thus each intermediate
shadow must have d7=4.  The seven-row containment inequality then forces at
least 10 changed virtual-complete blocks, hence singleton capacity at least 9
(the one pair block can account for at most one of those ten blocks).

This scan starts from every exact six-row d=3/capacity>=7 state, enumerates all
restriction-compatible seven-row d=4/capacity>=9 lifts for each remaining
cycle, combines every pair of one-cycle lifts into the corresponding eight-row
coefficient line, and records global d8=4 states and their singleton capacity.
If no global state has singleton capacity at least 10, the d6=3 side of
C:(4,11,10) is closed.

Complete-set ranks are exact over Q by the existing 2^127-1 Lucas-Lehmer and
Hadamard certificate.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
import argparse
import contextlib
import importlib.util
import io
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k7_d3_cap9_extension_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_C_d4q11_d3_pair_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)
S, R = B.S, B.R

EXPECTED_BASE = {7: 78, 8: 116, 9: 144, 10: 64}


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
            if capacity6 < 7:
                continue
            base_states.append((tuple(ext6), line6))
            base_capacity[capacity6] += 1

    assert synchronized_states == 1751870
    assert dict(sorted(base_capacity.items())) == EXPECTED_BASE
    assert len(base_states) == 402

    start = args.base_start
    end = len(base_states) if args.base_end is None else args.base_end
    assert 0 <= start <= end <= len(base_states)

    all_cycles = set(range(105))
    extension_multiplicity = Counter()
    pair_cycle_count = 0
    pair_line_count = 0
    global_d4 = 0
    global_d4_capacity = Counter()
    survivors = []

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
                if deficiency(complete7) != 4:
                    continue
                capacity7 = sum(
                    any(local is None or local == line7 for local in singles7[block])
                    for block in complete7
                )
                if capacity7 >= 9:
                    found.append(line7)
            if found:
                unique = tuple(dict.fromkeys(found))
                good[cycle] = unique
                extension_multiplicity[len(unique)] += 1

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
                assert line8 in lines8
                if deficiency(complete8) != 4:
                    continue
                global_d4 += 1
                global_d4_capacity[capacity8] += 1
                if capacity8 >= 10:
                    survivors.append((base_index, ext6, line6, a, b, line8, capacity8))

    print("PASS: completed C:(4,11,10) d6=3 exact extension scan")
    print("six_augmentation_cover", len(cover))
    print("synchronized_six_row_states", synchronized_states)
    print("base_d3_capacity_ge7", dict(sorted(base_capacity.items())))
    print("base_state_count", len(base_states))
    print("base_range", (start, end))
    print("seven_row_lift_multiplicity", dict(sorted(extension_multiplicity.items())))
    print("pair_cycle_count", pair_cycle_count)
    print("pair_line_count", pair_line_count)
    print("global_d4", global_d4)
    print("global_d4_capacity", dict(sorted(global_d4_capacity.items())))
    print("global_d4_capacity_ge10", len(survivors))
    print("survivor_examples", survivors[:10])
    print("unique_complete_sets_ranked", len(rank_cache))
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)


if __name__ == "__main__":
    main()
