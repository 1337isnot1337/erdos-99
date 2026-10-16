#!/usr/bin/env python3
"""Exact sharp boundary audit for five-no-root k=3,p=4.

The coverage-correct k=3 containment theorem gives
    D >= 5+p+3*d-3*q = 9+3*d-3*q,
with d>=1 and q<=p.  For p=4, only d=1,q=4 can lie below D=3;
the equality boundary D=3 can additionally occur at d=1,q=3 or d=2,q=4.
This verifier exhausts exactly those local replacement classes over all
535,040 repaired rank-two coefficient spaces.

The result is D>=3 uniformly.  There is no realizable d=1,q=4 state.  The
only canonical-minimal D=3 cores have d=2,q=4 and four singleton replacements;
there are exactly 19,392 such cores.
"""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_five_noroot_k3_containment_2026_09_20.py"
spec = importlib.util.spec_from_file_location("five_k3_containment_for_p4", BASE)
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(C)

R = C.R
P0 = C.P0
K = C.K
MOD = R.P

EXPECTED_COUNTS = {
    ("4sing_q3_d1", "exact"): 36,
    ("pair+1+1_q3", "exact"): 576,
    ("4sing_q4_d2", "exact"): 81950,
    ("4sing_q4_d2", "not_realize_P"): 1286,
}
EXPECTED_DEFECTS = {
    ("4sing_q3_d1", 9): 36,
    ("pair+1+1_q3", 6): 468,
    ("pair+1+1_q3", 9): 108,
    ("4sing_q4_d2", 3): 19392,
    ("4sing_q4_d2", 6): 33188,
    ("4sing_q4_d2", 9): 27880,
    ("4sing_q4_d2", 12): 1490,
}
EXPECTED_D3_RANKS = {
    (3, 5): 379,
    (4, 6): 2439,
    (5, 7): 1118,
    (6, 8): 8288,
    (7, 9): 7168,
}


def actual_space(ext, touched, states):
    space = ()
    for block, state in zip(touched, states):
        space = R.union_key(space, R.local_constraint_key(ext, block, state))
        if len(space) > 2:
            return space
    return space


def compatible_singletons(ext, block, space):
    return tuple(
        state
        for state in (1, 2, 4)
        if R.is_subspace(R.local_constraint_key(ext, block, state), space)
    )


def scan(start, stop):
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    rank_cache = {}
    base_census = Counter()
    counts = Counter()
    defect_census = Counter()
    d3_rank_census = Counter()
    candidate_space_count = 0
    dangerous_base_count = 0
    max_relation_norm2 = 0
    first_below_three = None

    for orbit_index in range(start, stop):
        local_five = orbits[orbit_index]
        ext = tuple(key_to_global[keys[i]] for i in local_five)
        touched = tuple(sorted(
            block
            for block in range(35)
            if any(R.QCOMP[e][block] != (0, 0) for e in ext)
        ))
        position = {block: i for i, block in enumerate(touched)}

        for space, min_singletons in C.candidate_spaces(ext, touched):
            candidate_space_count += 1
            base = C.virtual_canonical(ext, touched, space)
            complete = tuple(
                block for block, state in zip(touched, base) if state == 7
            )
            basis = rank_cache.get(complete)
            if basis is None:
                basis = C.rref_basis_mod([P0.COMPLETE_T[b] for b in complete])
                rank_cache[complete] = basis
            d = len(complete) - len(basis)
            base_census[(min_singletons, d)] += 1
            if d not in (1, 2):
                continue
            dangerous_base_count += 1

            complete_set = set(complete)
            canonical_empty = tuple(b for b in touched if b not in complete_set)
            singleton_options = {
                b: compatible_singletons(ext, b, space) for b in touched
            }
            signatures = set()

            if d == 1:
                eligible_complete = [b for b in complete if singleton_options[b]]

                # q=3, local partition 2+1+1, all three incomplete blocks
                # replacing canonical-complete blocks.
                for pair_block in complete:
                    single_blocks = [b for b in eligible_complete if b != pair_block]
                    for b1, b2 in combinations(single_blocks, 2):
                        for pair_state in (3, 5, 6):
                            for s1, s2 in product(
                                singleton_options[b1], singleton_options[b2]
                            ):
                                states = list(base)
                                states[position[pair_block]] = pair_state
                                states[position[b1]] = s1
                                states[position[b2]] = s2
                                signatures.add(("pair+1+1_q3", tuple(states)))

                # q=4 is the only containment class whose lower bound is <3.
                # It necessarily consists of four singleton replacements.
                for blocks in combinations(eligible_complete, 4):
                    for states4 in product(*(singleton_options[b] for b in blocks)):
                        states = list(base)
                        for b, state in zip(blocks, states4):
                            states[position[b]] = state
                        signatures.add(("4sing_q4_d1", tuple(states)))

                # q=3, four singleton blocks: three canonical-complete plus one
                # canonical-empty.  This is another possible sharp D=3 class.
                eligible_empty = [b for b in canonical_empty if singleton_options[b]]
                for complete_blocks in combinations(eligible_complete, 3):
                    for empty_block in eligible_empty:
                        blocks = complete_blocks + (empty_block,)
                        for states4 in product(*(singleton_options[b] for b in blocks)):
                            states = list(base)
                            for b, state in zip(blocks, states4):
                                states[position[b]] = state
                            signatures.add(("4sing_q3_d1", tuple(states)))
            else:
                # d=2 can reach the D=3 containment boundary only at q=4,
                # again forcing four singleton replacements.
                eligible_complete = [b for b in complete if singleton_options[b]]
                for blocks in combinations(eligible_complete, 4):
                    for states4 in product(*(singleton_options[b] for b in blocks)):
                        states = list(base)
                        for b, state in zip(blocks, states4):
                            states[position[b]] = state
                        signatures.add(("4sing_q4_d2", tuple(states)))

            for kind, states in signatures:
                if actual_space(ext, touched, states) != space:
                    counts[(kind, "not_realize_P")] += 1
                    continue
                rows = P0.relation_rows(ext, touched, states, space)
                for row in rows:
                    max_relation_norm2 = max(
                        max_relation_norm2, sum(x * x for x in row)
                    )
                delta = R.rank_mod(rows)
                nrows = 5 + sum(R.STATES[state][1] for state in states)
                defect = nrows - 3 * delta
                counts[(kind, "exact")] += 1
                defect_census[(kind, defect)] += 1
                if defect < 3 and first_below_three is None:
                    first_below_three = (
                        orbit_index, kind, defect, ext, space, states
                    )
                if defect == 3:
                    complete_count = sum(state == 7 for state in states)
                    d3_rank_census[(complete_count, delta)] += 1

    return {
        "candidate_space_count": candidate_space_count,
        "dangerous_base_count": dangerous_base_count,
        "base_census": base_census,
        "counts": counts,
        "defect_census": defect_census,
        "d3_rank_census": d3_rank_census,
        "max_relation_norm2": max_relation_norm2,
        "first_below_three": first_below_three,
        "rank_cache_size": len(rank_cache),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    _, orbits, _, _ = K.five_no_root_orbits()
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)

    result = scan(args.orbit_start, end)
    assert result["first_below_three"] is None, result["first_below_three"]
    assert MOD * MOD > max(1, result["max_relation_norm2"]) ** 15

    if args.orbit_start == 0 and end == len(orbits):
        assert result["candidate_space_count"] == 535040
        assert result["dangerous_base_count"] == 15951
        assert dict(sorted(result["base_census"].items())) == C.EXPECTED
        assert dict(result["counts"]) == EXPECTED_COUNTS
        assert dict(result["defect_census"]) == EXPECTED_DEFECTS
        assert dict(sorted(result["d3_rank_census"].items())) == EXPECTED_D3_RANKS
        assert sum(result["d3_rank_census"].values()) == 19392
        assert result["max_relation_norm2"] == 44
        # In particular there are no realizable d=1,q=4 cores at all.
        assert ("4sing_q4_d1", "exact") not in result["counts"]
        assert ("4sing_q4_d1", "not_realize_P") not in result["counts"]

    print("PASS: five-no-root k=3,p=4 sharp boundary")
    print("orbit_range", args.orbit_start, end)
    print("rank2_virtual_states", result["candidate_space_count"])
    print("d1_or_d2_virtual_states", result["dangerous_base_count"])
    print("replacement_census", dict(sorted(result["counts"].items())))
    print("exact_defect_census", dict(sorted(result["defect_census"].items())))
    print("D3_core_rank_census", dict(sorted(result["d3_rank_census"].items())))
    print("D3_canonical_cores", sum(result["d3_rank_census"].values()))
    print("max_relation_row_norm_squared", result["max_relation_norm2"])
    print("hadamard_exact_rank_bound", MOD * MOD > max(1, result["max_relation_norm2"]) ** 15)


if __name__ == "__main__":
    main()
