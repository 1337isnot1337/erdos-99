#!/usr/bin/env python3
"""Exact support certificate closing the r=1 weight-two-line subcase."""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_target_c_support7_global_segment_relative_eight_noroot_k4_dminus1_d1p0_support_closure_2026_09_26 as B

SHARDS = ((0, 5000), (5000, 10000), (10000, 15000),
          (15000, 20000), (20000, 25000), (25000, 27763))
EXPECTED_H19 = (3924, 1642, 1586, 781, 1065, 446)
PAIRS = tuple(combinations(range(8), 2))


def mask_of(occ):
    return sum(1 << i for i in occ)


def sharp_survival(mask, pair_mask):
    return (mask & ~pair_mask).bit_count() >= 2


def virtual_survivor(data, pair):
    pair_mask = (1 << pair[0]) | (1 << pair[1])
    T = tuple(sorted(data))
    rank_T = B.tri_rank(T)
    E = set()
    S = set()

    for b, (occ, dim, n) in data.items():
        mask = mask_of(occ)
        if (dim == 1 and ((n == 2 and mask == pair_mask) or n >= 3)) or (
            dim == 2 and n >= 4
        ):
            E.add(b)
        if sharp_survival(mask, pair_mask) and (
            (dim == 1 and n >= 2) or (dim == 2 and n >= 4)
        ):
            S.add(b)

    if len(S) < 3:
        return None

    C0 = set(T) - E

    for sing in combinations(sorted(S), 3):
        ss = set(sing)
        C = tuple(sorted(C0 - ss))

        if B.tri_rank(C) != len(C):
            continue
        if rank_T - B.tri_rank(C) < 4:
            continue

        dim = sum(data[b][1] for b in E if b not in ss)
        dim += sum(data[b][1] == 2 for b in ss)
        if dim < 4:
            continue

        cover = 0
        for b in E:
            if b not in ss:
                cover |= mask_of(data[b][0])
        for b in ss:
            if data[b][1] == 2:
                cover |= mask_of(data[b][0])
        if cover.bit_count() < 7:
            continue

        return (tuple(sorted(E)), sing, C, dim, cover)

    return None


def run_shard(reps, s):
    a, z = SHARDS[s]
    C = Counter()
    survivors = []

    for i in range(a, z):
        data = B.block_data(reps[i])
        C["orbits"] += 1

        if len(data) > 19:
            continue
        C["h19"] += 1

        for pair in PAIRS:
            C["tests"] += 1
            w = virtual_survivor(data, pair)
            if w is not None:
                survivors.append((i, reps[i], pair, w))
                break

        if survivors:
            break

    assert C["orbits"] == z - a, C
    assert C["h19"] == EXPECTED_H19[s], C
    assert C["tests"] == EXPECTED_H19[s] * len(PAIRS), C
    assert not survivors, survivors
    return C


def main():
    ap = ArgumentParser()
    ap.add_argument("--shard", type=int, choices=range(6))
    args = ap.parse_args()

    assert B.lucas_lehmer_31()
    assert B.MOD * B.MOD > 3**15

    reps = B.support_multiset_orbits()
    assert len(reps) == 27763

    shards = range(6) if args.shard is None else (args.shard,)
    total = Counter()

    for s in shards:
        C = run_shard(reps, s)
        total.update(C)
        print(
            "shard", s,
            "range", SHARDS[s],
            "h_le_19", C["h19"],
            "support_pair_tests", C["tests"],
            "virtual_survivors", 0,
        )

    if args.shard is None:
        assert total["orbits"] == 27763
        assert total["h19"] == 9444
        assert total["tests"] == 264432
        print("PASS: r=1 one-weight-two-line subcase closed")
        print("support_multiset_orbits_size_8", total["orbits"])
        print("touch_at_most_19", total["h19"])
        print("weight_two_supports", len(PAIRS))
        print("support_pair_tests", total["tests"])
        print("virtual_survivors", 0)
        print("hadamard_exact_rank_bound", B.MOD * B.MOD > 3**15)


if __name__ == "__main__":
    main()
