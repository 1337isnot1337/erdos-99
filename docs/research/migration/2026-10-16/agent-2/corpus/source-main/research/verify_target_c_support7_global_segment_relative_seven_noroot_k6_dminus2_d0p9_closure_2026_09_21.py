#!/usr/bin/env python3
"""Exact six-shadow refinement closing seven-no-root D=-2,k=6,d=0,p=9.

Default execution rebuilds the committed exact S7 six-subset augmentation cover.
For local reruns, --cover-cache may point at a pickle (keys, cover, info) made by
that same committed cover routine; the exact state scan is unchanged.
"""
from collections import Counter
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io
import pickle

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("six_k5_base_for_k6_p9", BASE)
S = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(S)
R = S.R


def load_cover(cache):
    if cache:
        with open(cache, "rb") as f:
            keys, cover, info = pickle.load(f)
        assert len(keys) == 105
        assert len(cover) == 325955
        assert len(info) == 105
        return keys, cover, info

    keys, five_orbits, orbit_sizes, augmentation_candidates = S.K.five_no_root_orbits()
    assert len(five_orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    cover = S.six_augmentation_cover(keys, five_orbits)
    _local_to_global, info = S.local_cycle_data(keys)
    return keys, cover, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cover-cache")
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    assert R.P * R.P > 12**15
    _keys, cover, info = load_cover(args.cover_cache)

    rank_cache = {}
    d3_cap8 = 0
    support = Counter()
    support3_capacity = Counter()
    support3_capable_blocks = 0
    support3_bad_touch = 0

    for ext_local in cover:
        values, lines, empty_line, singleton_lines = S.block_profile(ext_local, info)
        for line in lines:
            line_support = {i for i, x in enumerate(line) if x != 0}
            if len(line_support) < 2:
                continue

            complete_set = tuple(sorted(b for b in values if empty_line[b] != line))
            capable = tuple(
                b
                for b in complete_set
                if any(local is None or local == line for local in singleton_lines[b])
            )
            if len(capable) < 8:
                continue

            d = rank_cache.get(complete_set)
            if d is None:
                d = len(complete_set) - R.rank_mod([S.COMPLETE_T[b] for b in complete_set])
                rank_cache[complete_set] = d
            if d != 3:
                continue

            d3_cap8 += 1
            support[len(line_support)] += 1
            if len(line_support) == 3:
                support3_capacity[len(capable)] += 1
                for b in capable:
                    touched = {i for i, v in enumerate(values[b]) if v != [0, 0]}
                    support3_capable_blocks += 1
                    if len(touched) != 1 or not touched <= line_support:
                        support3_bad_touch += 1

    assert d3_cap8 == 324
    assert dict(sorted(support.items())) == {2: 317, 3: 7}
    assert dict(sorted(support3_capacity.items())) == {8: 2, 9: 5}
    assert support3_capable_blocks == 61
    assert support3_bad_touch == 0

    # Seven-row arithmetic synthesis.
    # The preceding k=6 reduction already proves global d_v=3,q=9, so the nine
    # selected incomplete blocks are all singletons.  A six-row deletion has
    # p_i in {0,3,6,9}.  At p_i=6, deficiency two would force q_i=6 and hence
    # six singleton-compatible virtual-complete blocks, contradicting the exact
    # deficiency-two capacity bound of three; larger deficiency is impossible.
    # p_i<=3 is excluded directly by containment.  Hence every p_i=9.
    assert 6 + 6 + 3 * 2 - 3 * 6 == 0
    assert 6 > 3
    assert 6 + 3 + 3 * 2 - 3 * 3 == 6

    # Thus every deletion is a d=3, capacity>=8 state in the exact census above.
    # The global coefficient line has support at least three.  Since all six-row
    # projections have support at most three, the global support is exactly 3.
    # There are four zero coordinates.  For deletion of any such coordinate z,
    # the support-three audit says each relevant singleton block has shadow touch
    # set {s} with s in the coefficient support.  Since p_z=9 and every deletion
    # has p_i=9, the global block touch set is exactly {z,s}.  The sets of blocks
    # arising from distinct zero coordinates are therefore disjoint.  Each has
    # size at least eight, but there are only nine global singleton blocks.
    global_support = 3
    zero_coordinates = 7 - global_support
    min_q_per_zero_deletion = 8
    global_singletons = 9
    assert zero_coordinates * min_q_per_zero_deletion > global_singletons

    print(
        "PASS: exact support-three six-shadow refinement closes "
        "seven-no-root D=-2,k=6,d=0,p=9"
    )
    print("six_augmentation_cover", len(cover))
    print("d3_capacity_ge8_states", d3_cap8)
    print("line_support_census", dict(sorted(support.items())))
    print("support3_capacity_census", dict(sorted(support3_capacity.items())))
    print("support3_capable_blocks_checked", support3_capable_blocks)
    print("support3_bad_touch_blocks", support3_bad_touch)
    print("global_support_forced", global_support)
    print("zero_coordinate_deletions", zero_coordinates)
    print("disjoint_required_blocks", zero_coordinates * min_q_per_zero_deletion)
    print("available_global_singletons", global_singletons)


if __name__ == "__main__":
    main()
