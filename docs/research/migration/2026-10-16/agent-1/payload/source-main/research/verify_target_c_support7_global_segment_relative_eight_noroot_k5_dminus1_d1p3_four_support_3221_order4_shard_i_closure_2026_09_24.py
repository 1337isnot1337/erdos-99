#!/usr/bin/env python3
"""Exact sharded closure of another nullity-four order-4 (3,2,2,1) support class.

This bounded shard is in the eight-no-root
k=5,D=-1,d_root=1,p=3,m=4,(3,2,2,1) branch. The imported high-symmetry
verifier supplies the exact K8 coordinate normal form, S7 action,
(3,2,2,1) cycle enumeration, singleton coefficient code, generalized-weight
calculation, and certified modular relation-rank machinery.
"""
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3221_highsym_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_m4_3221_order4i_parent", PARENT)
V = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)
R = V.R

TARGET = (
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 4, 5, 6),
    (4, 5, 6, 7),
)
EXPECTED_GLOBAL = (4, 102, 408_240, 14)
EXPECTED_SHARDS = {
    (0, 40): (8_400, 226_800, 178_512, 12_096, 50),
    (40, 80): (8_400, 226_800, 179_016, 11_484, 50),
    (80, 102): (4_620, 124_740, 98_484, 6_966, 50),
}
EXPECTED_TOTAL = (21_420, 578_340, 456_012, 30_546)


def support_name(support_indices):
    return tuple(tuple(V.SUPPORTS[i]) for i in support_indices)


def support_nullity(support_indices):
    ext = min(V.profile_3221_candidates(support_indices))
    touched = V.touched_blocks(ext)
    return len(touched) - R.exact_rank(tuple(V.HROW[b] for b in touched))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard", type=int, choices=range(3), required=True)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    assert R.P * R.P > V.ROOT_MAX_NORM2 ** 15

    order4 = tuple(
        supports for supports in V.four_support_orbits()
        if len(V.support_stabilizer(supports)) == 4
    )
    assert len(order4) == 12
    nullity4 = tuple(s for s in order4 if support_nullity(s) == 4)
    assert len(nullity4) == 11
    candidates = tuple(s for s in nullity4 if support_name(s) == TARGET)
    assert len(candidates) == 1
    supports = candidates[0]

    reps, stab = V.cycle_orbits_for_support(supports)
    exp_stab, exp_orbits, exp_labeled, exp_touched = EXPECTED_GLOBAL
    assert stab == exp_stab
    assert len(reps) == exp_orbits
    assert (5040 // stab) * 324 == exp_labeled

    touched = V.touched_blocks(reps[0])
    assert all(V.touched_blocks(ext) == touched for ext in reps)
    assert len(touched) == exp_touched
    assert len(touched) - R.exact_rank(tuple(V.HROW[b] for b in touched)) == 4

    intervals = tuple(EXPECTED_SHARDS)
    start, end = intervals[args.shard]
    selected = reps[start:end]
    exp_singletons, exp_dirs, exp_rank3, exp_gw, exp_norm = EXPECTED_SHARDS[(start, end)]

    admissible = []
    for singleton_blocks in combinations(touched, 3):
        complete = tuple(b for b in touched if b not in singleton_blocks)
        root_rank = R.rank_mod(tuple(V.HROW[b] for b in complete))
        if len(complete) - root_rank == 1:
            admissible.append((singleton_blocks, root_rank))

    singleton_triples = 0
    direction_states = 0
    rank_three_states = 0
    generalized_weight_states = 0
    increment_census = Counter()
    max_norm2 = 0

    for ext in selected:
        local_rows = {
            (b, d): V.singleton_row(ext, b, d)
            for b in touched for d in V.LOCAL
        }
        singleton_triples += len(admissible)
        for singleton_blocks, root_rank in admissible:
            for directions in product(V.LOCAL, repeat=3):
                direction_states += 1
                rows = tuple(
                    local_rows[(b, d)]
                    for b, d in zip(singleton_blocks, directions)
                )
                if not V.rank_three(rows):
                    continue
                rank_three_states += 1

                d1, d2, d3 = V.generalized_weights(rows)
                if not (d1 >= 2 and d2 >= 4 and d3 >= 5):
                    continue
                generalized_weight_states += 1

                constraint_key = R.rowspace_key(rows)
                singletons = dict(zip(singleton_blocks, directions))
                states = tuple(
                    V.DIR_MASK[singletons[b]] if b in singletons else 7
                    for b in touched
                )
                rel_rows = V.relation_rows_int8(ext, touched, states, constraint_key)
                for row in rel_rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
                increment = R.rank_mod(rel_rows) - root_rank
                increment_census[increment] += 1
                assert increment == 0

    assert singleton_triples == exp_singletons
    assert direction_states == exp_dirs
    assert rank_three_states == exp_rank3
    assert generalized_weight_states == exp_gw
    assert dict(increment_census) == {0: exp_gw}
    assert max_norm2 == exp_norm
    assert R.P * R.P > max_norm2 ** 15

    assert tuple(sum(EXPECTED_SHARDS[i][j] for i in intervals) for j in range(4)) == EXPECTED_TOTAL

    print("PASS: k5 p3 four-support (3,2,2,1) order-4 shard I closure")
    print("support", TARGET)
    print("representative_interval", (start, end))
    print("stabilizer", stab)
    print("S7_cycle_set_orbits", len(reps))
    print("labeled_cycle_sets", exp_labeled)
    print("touched_blocks", len(touched))
    print("admissible_singleton_triples", singleton_triples)
    print("direction_states", direction_states)
    print("rank_three_states", rank_three_states)
    print("generalized_weight_states", generalized_weight_states)
    print("external_rank_increment_census", dict(increment_census))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
