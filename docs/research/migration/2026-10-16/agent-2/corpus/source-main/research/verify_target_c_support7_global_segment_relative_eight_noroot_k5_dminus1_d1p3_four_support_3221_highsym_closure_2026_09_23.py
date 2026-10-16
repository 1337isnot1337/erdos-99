#!/usr/bin/env python3
"""Exact closure of the high-symmetry (3,2,2,1) four-support shard for k=5,D=-1,d_root=1,p=3.

The imported (3,3,1,1) verifier supplies the exact K8 coordinate normal form,
S7 support action, singleton coefficient code, generalized-weight computation,
and certified modular relation-rank machinery. This verifier changes only the
four-support multiplicity profile to (3,2,2,1), selects the seven support
orbits with stabilizer order at least 16, and proves every admissible state has
external relation-rank increment zero instead of the required five.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
PARENT = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k5_dminus1_d1p3_four_support_3311_closure_2026_09_23.py"
spec = importlib.util.spec_from_file_location("eight_k5_p3_m4_3221_highsym_parent", PARENT)
V = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(V)
R = V.R


def support_stabilizer(support_indices):
    return tuple(
        cmap for smap, cmap in V.PERM_DATA
        if tuple(sorted(smap[i] for i in support_indices)) == support_indices
    )


def profile_3221_candidates(support_indices):
    faces = tuple(V.SUPPORTS[i] for i in support_indices)
    out = set()
    for pos3 in range(4):
        for pos1 in range(4):
            if pos1 == pos3:
                continue
            pos2 = tuple(i for i in range(4) if i not in (pos3, pos1))
            for omit0, omit1, choice1 in product(range(3), repeat=3):
                ext = []
                for i, F in enumerate(faces):
                    es = V.SUPPORT_CYCLES[F]
                    if i == pos3:
                        ext.extend(es)
                    elif i == pos1:
                        ext.append(es[choice1])
                    elif i == pos2[0]:
                        ext.extend(e for j, e in enumerate(es) if j != omit0)
                    else:
                        ext.extend(e for j, e in enumerate(es) if j != omit1)
                assert len(ext) == 8 and len(set(ext)) == 8
                out.add(tuple(sorted(ext)))
    assert len(out) == 324
    return out


def cycle_orbits_for_support(support_indices):
    stabilizer = support_stabilizer(support_indices)
    unseen = profile_3221_candidates(support_indices)
    reps = []
    while unseen:
        ext = min(unseen)
        reps.append(ext)
        orbit = {
            tuple(sorted(cmap[e] for e in ext))
            for cmap in stabilizer
        }
        unseen.difference_update(orbit)
    return tuple(reps), len(stabilizer)


def support_name(support_indices):
    return tuple(tuple(V.SUPPORTS[i]) for i in support_indices)


# stabilizer, cycle orbits, singleton triples, direction states, rank-3 states,
# generalized-weight states, maximum squared relation-row norm
EXPECTED = {
    ((1,2,3,4),(1,2,3,5),(1,2,3,6),(1,2,3,7)): (144,4,648,17496,13608,1063,70),
    ((1,2,3,4),(1,2,3,5),(1,2,3,6),(4,5,6,7)): (36,14,2772,74844,58016,4142,70),
    ((1,2,3,4),(1,2,3,5),(1,2,4,5),(1,2,6,7)): (24,28,5096,137592,111377,12620,70),
    ((1,2,3,4),(1,2,3,5),(1,2,4,5),(1,3,4,5)): (48,15,1650,44550,39454,10603,70),
    ((1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6)): (16,24,3936,106272,88566,13292,70),
    ((1,2,3,4),(1,2,3,5),(1,4,6,7),(1,5,6,7)): (16,30,6300,170100,134136,9816,36),
    ((1,2,3,4),(1,2,5,6),(1,3,5,7),(1,4,6,7)): (24,15,3840,103680,77760,2880,18),
}


def main():
    assert R.lucas_lehmer_127()
    assert R.P * R.P > V.ROOT_MAX_NORM2 ** 15

    high = tuple(
        supports for supports in V.four_support_orbits()
        if len(support_stabilizer(supports)) >= 16
    )
    assert len(high) == 7
    assert {support_name(s) for s in high} == set(EXPECTED)
    assert Counter(len(support_stabilizer(s)) for s in high) == Counter({16:2,24:2,36:1,48:1,144:1})

    total_cycle_orbits = labeled_cycle_sets = 0
    singleton_triples = direction_states = rank_three_states = generalized_weight_states = 0
    increment_census = Counter()
    max_norm2 = 0

    for supports in high:
        reps, stab = cycle_orbits_for_support(supports)
        name = support_name(supports)
        exp_stab, exp_orbits, exp_singletons, exp_dirs, exp_rank3, exp_gw, exp_norm = EXPECTED[name]
        assert stab == exp_stab and len(reps) == exp_orbits
        labeled_cycle_sets += (5040 // stab) * 324
        total_cycle_orbits += len(reps)

        sample_touched = V.touched_blocks(reps[0])
        assert all(V.touched_blocks(ext) == sample_touched for ext in reps)
        assert len(sample_touched) - R.exact_rank(tuple(V.HROW[b] for b in sample_touched)) == 4

        s_singletons = s_dirs = s_rank3 = s_gw = s_max_norm2 = 0
        s_increments = Counter()
        for ext in reps:
            touched = sample_touched
            local_rows = {
                (b, d): V.singleton_row(ext, b, d)
                for b in touched for d in V.LOCAL
            }
            for singleton_blocks in combinations(touched, 3):
                complete = tuple(b for b in touched if b not in singleton_blocks)
                root_rank = R.rank_mod(tuple(V.HROW[b] for b in complete))
                if len(complete) - root_rank != 1:
                    continue
                s_singletons += 1
                for directions in product(V.LOCAL, repeat=3):
                    s_dirs += 1
                    rows = tuple(local_rows[(b, d)] for b, d in zip(singleton_blocks, directions))
                    if not V.rank_three(rows):
                        continue
                    s_rank3 += 1
                    d1, d2, d3 = V.generalized_weights(rows)
                    if not (d1 >= 2 and d2 >= 4 and d3 >= 5):
                        continue
                    s_gw += 1

                    constraint_key = R.rowspace_key(rows)
                    singletons = dict(zip(singleton_blocks, directions))
                    states = tuple(
                        V.DIR_MASK[singletons[b]] if b in singletons else 7
                        for b in touched
                    )
                    rel_rows = V.relation_rows_int8(ext, touched, states, constraint_key)
                    for row in rel_rows:
                        s_max_norm2 = max(s_max_norm2, sum(x * x for x in row))
                    increment = R.rank_mod(rel_rows) - root_rank
                    s_increments[increment] += 1
                    assert increment == 0

        assert (s_singletons, s_dirs, s_rank3, s_gw, s_max_norm2) == (
            exp_singletons, exp_dirs, exp_rank3, exp_gw, exp_norm
        )
        assert dict(s_increments) == {0: exp_gw}
        singleton_triples += s_singletons
        direction_states += s_dirs
        rank_three_states += s_rank3
        generalized_weight_states += s_gw
        increment_census.update(s_increments)
        max_norm2 = max(max_norm2, s_max_norm2)

    assert total_cycle_orbits == 130
    assert labeled_cycle_sets == 430_920
    assert singleton_triples == 24_242
    assert direction_states == 654_534
    assert rank_three_states == 522_917
    assert generalized_weight_states == 54_416
    assert dict(increment_census) == {0: 54_416}
    assert max_norm2 == 70
    assert R.P * R.P > max_norm2 ** 15

    print("PASS: k5 p3 four-support (3,2,2,1) high-symmetry shard closure")
    print("support_orbits", len(high))
    print("S7_cycle_set_orbits", total_cycle_orbits)
    print("labeled_cycle_sets", labeled_cycle_sets)
    print("admissible_singleton_triples", singleton_triples)
    print("direction_states", direction_states)
    print("rank_three_states", rank_three_states)
    print("generalized_weight_states", generalized_weight_states)
    print("external_rank_increment_census", dict(increment_census))
    print("max_relation_row_norm_squared", max_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_norm2 ** 15)


if __name__ == "__main__":
    main()
