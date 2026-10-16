#!/usr/bin/env python3
"""Exact d6=3 side of branch A in the eight-no-root k=7 layer.

The surviving branch-A profile is (d_v,q,s)=(4,11,11). A selected
p-retaining good pair shadow must pass through a six-row state of either
(d6=3, singleton capacity >=8) or (d6=4, capacity >=9). This verifier treats
the d6=3 side. Both one-cycle intermediate seven-row states are required by
the proved shadow bounds to have d7=4 and capacity >=10, while the global
state must have d8=4 and capacity >=11.

The exact S7 six-row extension cover has 324 d6=3/capacity>=8 states. For each
we enumerate all remaining first cycles with a restriction-compatible
seven-row d4/capacity>=10 line, pair all such extensions, reconstruct the
unique eight-row line determined by the two seven-row lifts, and test the
global complete-set deficiency and singleton capacity. No global d8=4 state
has capacity >=11.

All complete-set ranks are computed modulo 2^127-1. Lucas-Lehmer primality,
complete T-row squared norm <=12, and P^2>12^15 give exact rational ranks by
Hadamard's inequality.
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
spec = importlib.util.spec_from_file_location("e99_A_pair_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)
S, R = B.S, B.R

EXPECTED_BASE = {8: 116, 9: 144, 10: 64}
EXPECTED_CAP8 = {7: 3398, 8: 9195, 9: 5499, 10: 924}


def combine(line6, line7_a, line7_b):
    """Recover the unique primitive eight-row line from two seven-row lifts."""
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
        complete = tuple(
            sorted(block for block in values if empty_line[block] != line)
        )
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
            complete6 = tuple(
                sorted(block for block in values6 if empty6[block] != line6)
            )
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
    cycle_count = Counter()
    pair_extensions = 0
    obtainable_pair_lines = 0
    global_d4 = 0
    global_d4_capacity = Counter()
    global_d4_capacity_ge11 = 0

    for ext6, line6 in base_states[start:end]:
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
                capacity7 = sum(
                    any(local is None or local == line7 for local in singles7[block])
                    for block in complete7
                )
                if capacity7 >= 10:
                    found.append(line7)
            assert len(found) <= 1
            if found:
                good[cycle] = found[0]

        cycle_count[len(good)] += 1
        for a, b in combinations(sorted(good), 2):
            pair_extensions += 1
            line8 = combine(line6, good[a], good[b])
            ext8 = ext6 + (a, b)
            complete8, capacity8, lines8 = profile(ext8, line8)
            assert line8 in lines8
            obtainable_pair_lines += 1
            if deficiency(complete8) != 4:
                continue
            global_d4 += 1
            global_d4_capacity[capacity8] += 1
            if capacity8 >= 11:
                global_d4_capacity_ge11 += 1

    assert obtainable_pair_lines == pair_extensions
    assert global_d4_capacity_ge11 == 0

    if start == 0 and end == len(base_states):
        assert pair_extensions == 684270
        assert global_d4 == 19016
        assert dict(sorted(global_d4_capacity.items())) == EXPECTED_CAP8

    print("PASS: branch-A d6=3 pair-extension obstruction")
    print("six_augmentation_cover", len(cover))
    print("synchronized_six_row_states", synchronized_states)
    print("base_d3_capacity_ge8", dict(sorted(base_capacity.items())))
    print("base_state_count", len(base_states))
    print("base_range", (start, end))
    print("good_extension_cycle_count", dict(sorted(cycle_count.items())))
    print("pair_extensions", pair_extensions)
    print("obtainable_pair_lines", obtainable_pair_lines)
    print("global_d4", global_d4)
    print("global_d4_capacity", dict(sorted(global_d4_capacity.items())))
    print("global_d4_capacity_ge11", global_d4_capacity_ge11)
    print("unique_complete_sets_ranked", len(rank_cache))
    print("hadamard_exact_rank_bound", R.P * R.P > 12 ** 15)


if __name__ == "__main__":
    main()
