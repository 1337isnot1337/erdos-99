#!/usr/bin/env python3
"""Exact high-symmetry shard of the (2,2,2,2) m=4 branch.

Covers every S7 orbit of four 4-supports whose setwise stabilizer in S7 has
order at least 16, with multiplicity profile (2,2,2,2).
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_m4_2222_sym16_base", BASE)
V = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)


def profile_2222_candidates(support_indices):
    faces = tuple(V.SUPPORTS[i] for i in support_indices)
    out = set()
    for omissions in product(range(3), repeat=4):
        ext = []
        for F, omit in zip(faces, omissions):
            es = V.SUPPORT_CYCLES[F]
            ext.extend(e for j, e in enumerate(es) if j != omit)
        out.add(tuple(sorted(ext)))
    assert len(out) == 3**4 == 81
    return out


def high_symmetry_cycle_orbits():
    reps = []
    raw_cycle_sets = 0
    stabilizer_orders = []
    for supports in V.four_support_orbits():
        stabilizer = [
            cmap
            for smap, cmap in V.PERM_DATA
            if tuple(sorted(smap[i] for i in supports)) == supports
        ]
        order = len(stabilizer)
        if order < 16:
            continue
        stabilizer_orders.append(order)
        raw_cycle_sets += (5040 // order) * 3**4

        unseen = profile_2222_candidates(supports)
        while unseen:
            ext = min(unseen)
            reps.append(ext)
            orbit = {
                tuple(sorted(cmap[e] for e in ext))
                for cmap in stabilizer
            }
            unseen.difference_update(orbit)

    assert Counter(stabilizer_orders) == Counter({16: 2, 24: 2, 36: 1, 48: 1, 144: 1})
    assert len(stabilizer_orders) == 7
    assert raw_cycle_sets == 107_730
    assert len(reps) == 56
    return tuple(reps), tuple(sorted(stabilizer_orders)), raw_cycle_sets


def touched_blocks(ext):
    return tuple(sorted(
        b for b in range(35)
        if any(V.R.QCOMP[e][b] != (0, 0) for e in ext)
    ))


def main():
    assert V.R.lucas_lehmer_127()
    assert V.R.P * V.R.P > V.ROOT_MAX_NORM2 ** 15

    reps, stabilizer_orders, raw_cycle_sets = high_symmetry_cycle_orbits()

    singleton_triples = 0
    direction_states = 0
    rank_three_states = 0
    generalized_weight_states = 0
    increment_census = Counter()
    max_norm2 = 0

    for ext in reps:
        touched = touched_blocks(ext)
        local_rows = {
            (b, d): V.singleton_row(ext, b, d)
            for b in touched
            for d in V.LOCAL
        }

        for singleton_blocks in combinations(touched, 3):
            complete = tuple(b for b in touched if b not in singleton_blocks)
            root_rank = V.R.rank_mod(tuple(V.HROW[b] for b in complete))
            root_nullity = len(complete) - root_rank
            if root_nullity != 1:
                continue
            singleton_triples += 1

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

                constraint_key = V.R.rowspace_key(rows)
                singletons = dict(zip(singleton_blocks, directions))
                states = tuple(
                    V.DIR_MASK[singletons[b]] if b in singletons else 7
                    for b in touched
                )
                rel_rows = V.relation_rows_int8(
                    ext, touched, states, constraint_key
                )
                for row in rel_rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
                increment = V.R.rank_mod(rel_rows) - root_rank
                increment_census[increment] += 1
                assert increment == 0

    assert singleton_triples == 10_262
    assert direction_states == 277_074
    assert rank_three_states == 277_074
    assert generalized_weight_states == 19_513
    assert dict(increment_census) == {0: 19_513}
    assert max_norm2 == 70
    assert V.R.P * V.R.P > max_norm2 ** 15

    print("PASS: high-symmetry (2,2,2,2) support shard is empty")
    print("support_set_orbits", 7)
    print("support_stabilizer_orders", stabilizer_orders)
    print("raw_cycle_sets_covered", raw_cycle_sets)
    print("S7_cycle_set_orbits", len(reps))
    print("admissible_singleton_triples", singleton_triples)
    print("direction_states", direction_states)
    print("rank_three_states", rank_three_states)
    print("generalized_weight_states", generalized_weight_states)
    print("external_rank_increment_census", dict(increment_census))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", V.R.P * V.R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
