#!/usr/bin/env python3
"""Exact t=5, k=3, p=2 rank-density barrier for Target C.

This closes the p=2 slice of the five-no-root k=3 branch.

Fix the rank-two coefficient-constraint space P and start from the canonical
p=0 state.  Let C be its complete-block set and d=|C|-rank_T(C).  A canonical
p=2 state has either one two-row incomplete block or two singleton incomplete
blocks.  Let C' be its remaining complete-block set.

Since the coefficient nullspace has dimension three,
    delta <= rank_T(C') + 3.
If C' is dependent then
    |A|-3*delta >= 1,
so only states with C' independent can possibly violate the factor-three
inequality.  Replacing at most two complete blocks means only p=0 canonical
states with d<=2 need consideration.

For d=1, the only potentially independent cases are one pair replacing a
complete block, or two singletons replacing two complete blocks.  For d=2,
only two complete-block singleton replacements can work.  Cases involving an
incomplete base-empty block leave too few complete-block deletions, except for
the d=1 singleton case already ruled out by the p=1 audit.

The exact scan finds 346 independent one-block pair-removal sets, giving 1,038
pair states.  It also finds 3,534 independent two-block singleton-removal
states, all from d=2 p=0 states.  Every one of the resulting 4,572 canonical
p=2 states has exact defect 7.  Thus the p=2 branch is closed.

Coefficient-space operations use exact Fraction arithmetic.  T-ranks use
P=2^127-1 with Lucas-Lehmer and an explicit Hadamard bound; the maximum
squared norm of any full relation row in this scan is 44.
"""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
P0_PATH = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k3_p0_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k3p0_for_p2", P0_PATH)
P0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P0)
R = P0.R
K = P0.K


def scan(keys, orbits, start, stop):
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    complete_rank_cache = {}
    p0_deficiency_census = Counter()
    independent_removal_census = Counter()
    exact_type_census = Counter()
    exact_defect_census = Counter()
    exact_rank_census = Counter()
    max_relation_norm2 = 0
    first_negative = None

    for orbit_index in range(start, stop):
        local_five = orbits[orbit_index]
        ext = tuple(key_to_global[keys[i]] for i in local_five)
        touched = tuple(sorted(
            b for b in range(35)
            if any(R.QCOMP[e][b] != (0, 0) for e in ext)
        ))
        position = {b: i for i, b in enumerate(touched)}

        for space in P0.candidate_rank2_constraint_spaces(ext, touched):
            base_states = P0.canonical_minimal_state(ext, touched, space)
            assert base_states is not None
            complete_set = tuple(
                b for b, state in zip(touched, base_states) if state == 7
            )
            c = len(complete_set)
            if c >= 14:
                continue

            rank = complete_rank_cache.get(complete_set)
            if rank is None:
                rank = R.rank_mod([P0.COMPLETE_T[b] for b in complete_set])
                complete_rank_cache[complete_set] = rank
            deficiency = c - rank
            assert deficiency >= 1
            if deficiency > 2:
                continue
            p0_deficiency_census[deficiency] += 1

            # Type I: one two-row incomplete state.  Removing one complete
            # block can make the complete set independent only when d=1.
            if deficiency == 1:
                for block in complete_set:
                    reduced = tuple(b for b in complete_set if b != block)
                    reduced_rank = complete_rank_cache.get(reduced)
                    if reduced_rank is None:
                        reduced_rank = R.rank_mod(
                            [P0.COMPLETE_T[b] for b in reduced]
                        )
                        complete_rank_cache[reduced] = reduced_rank
                    if reduced_rank != len(reduced):
                        continue
                    independent_removal_census["pair_d1"] += 1

                    for pair_state in (3, 5, 6):
                        states = list(base_states)
                        states[position[block]] = pair_state
                        states = tuple(states)
                        rows = P0.relation_rows(ext, touched, states, space)
                        for row in rows:
                            max_relation_norm2 = max(
                                max_relation_norm2,
                                sum(x * x for x in row),
                            )
                        delta = R.rank_mod(rows)
                        defect = 5 + 3 * len(reduced) + 2 - 3 * delta
                        exact_type_census["pair"] += 1
                        exact_defect_census[defect] += 1
                        exact_rank_census[
                            (len(reduced), reduced_rank, delta)
                        ] += 1
                        if defect < 0:
                            first_negative = (
                                orbit_index,
                                "pair",
                                defect,
                                delta,
                                ext,
                                touched,
                                space,
                                states,
                            )
                            break
                    if first_negative is not None:
                        break
            if first_negative is not None:
                break

            # Type II: two singleton incomplete states.  If either singleton
            # is placed in a p=0-empty block then at most one complete block
            # is removed.  For d>=2 this cannot yield independence; for d=1
            # the p=1 verifier already shows every admissible one-block
            # singleton removal remains dependent.  Hence only two complete
            # blocks need to be enumerated here.
            for block1, block2 in combinations(complete_set, 2):
                reduced = tuple(
                    b for b in complete_set if b != block1 and b != block2
                )
                reduced_rank = complete_rank_cache.get(reduced)
                if reduced_rank is None:
                    reduced_rank = R.rank_mod(
                        [P0.COMPLETE_T[b] for b in reduced]
                    )
                    complete_rank_cache[reduced] = reduced_rank
                if reduced_rank != len(reduced):
                    continue

                opts1 = tuple(
                    state
                    for state in (1, 2, 4)
                    if R.is_subspace(
                        R.local_constraint_key(ext, block1, state), space
                    )
                )
                opts2 = tuple(
                    state
                    for state in (1, 2, 4)
                    if R.is_subspace(
                        R.local_constraint_key(ext, block2, state), space
                    )
                )
                if not opts1 or not opts2:
                    continue

                independent_removal_census[
                    f"two_singletons_d{deficiency}"
                ] += 1
                for state1 in opts1:
                    for state2 in opts2:
                        states = list(base_states)
                        states[position[block1]] = state1
                        states[position[block2]] = state2
                        states = tuple(states)
                        rows = P0.relation_rows(ext, touched, states, space)
                        for row in rows:
                            max_relation_norm2 = max(
                                max_relation_norm2,
                                sum(x * x for x in row),
                            )
                        delta = R.rank_mod(rows)
                        defect = 5 + 3 * len(reduced) + 2 - 3 * delta
                        exact_type_census["two_singletons"] += 1
                        exact_defect_census[defect] += 1
                        exact_rank_census[
                            (len(reduced), reduced_rank, delta)
                        ] += 1
                        if defect < 0:
                            first_negative = (
                                orbit_index,
                                "two_singletons",
                                defect,
                                delta,
                                ext,
                                touched,
                                space,
                                states,
                            )
                            break
                    if first_negative is not None:
                        break
                if first_negative is not None:
                    break
            if first_negative is not None:
                break
        if first_negative is not None:
            break

    return {
        "p0_deficiency_census": p0_deficiency_census,
        "independent_removal_census": independent_removal_census,
        "exact_type_census": exact_type_census,
        "exact_defect_census": exact_defect_census,
        "exact_rank_census": exact_rank_census,
        "max_relation_norm2": max_relation_norm2,
        "complete_rank_cache_size": len(complete_rank_cache),
        "first_negative": first_negative,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)

    result = scan(keys, orbits, args.orbit_start, end)
    assert result["first_negative"] is None, result["first_negative"]

    max_complete_norm2 = max(
        sum(x * x for x in row) for row in P0.COMPLETE_T
    )
    bound_norm2 = max(max_complete_norm2, result["max_relation_norm2"])
    assert R.P * R.P > max(1, bound_norm2) ** 15

    if args.orbit_start == 0 and end == len(orbits):
        assert len(orbits) == 20451
        assert sum(orbit_sizes) == 96560646
        assert augmentation_candidates == 20475
        assert dict(sorted(result["p0_deficiency_census"].items())) == {
            1: 86,
            2: 13349,
        }
        assert dict(result["independent_removal_census"]) == {
            "pair_d1": 346,
            "two_singletons_d2": 3534,
        }
        assert dict(result["exact_type_census"]) == {
            "pair": 1038,
            "two_singletons": 3534,
        }
        assert dict(result["exact_defect_census"]) == {7: 4572}
        assert dict(sorted(result["exact_rank_census"].items())) == {
            (3, 3, 3): 840,
            (5, 5, 5): 61,
            (6, 6, 6): 354,
            (7, 7, 7): 465,
            (8, 8, 8): 1828,
            (9, 9, 9): 1024,
        }
        assert result["max_relation_norm2"] == 44

    print("PASS: five-no-root k=3,p=2 rank-density branch")
    print("five_no_root_subsets", 96560646)
    print("S7_orbits", len(orbits))
    print("orbit_range", args.orbit_start, end)
    print(
        "p0_deficiency_census",
        dict(sorted(result["p0_deficiency_census"].items())),
    )
    print(
        "independent_removal_census",
        dict(sorted(result["independent_removal_census"].items())),
    )
    print(
        "exact_type_census",
        dict(sorted(result["exact_type_census"].items())),
    )
    print(
        "exact_defect_census",
        dict(sorted(result["exact_defect_census"].items())),
    )
    print(
        "exact_rank_census",
        dict(sorted(result["exact_rank_census"].items())),
    )
    print("max_complete_row_norm_squared", max_complete_norm2)
    print("max_relation_row_norm_squared", result["max_relation_norm2"])
    print("hadamard_exact_rank_bound", R.P * R.P > max(1, bound_norm2) ** 15)
    print("complete_rank_cache_size", result["complete_rank_cache_size"])


if __name__ == "__main__":
    main()
