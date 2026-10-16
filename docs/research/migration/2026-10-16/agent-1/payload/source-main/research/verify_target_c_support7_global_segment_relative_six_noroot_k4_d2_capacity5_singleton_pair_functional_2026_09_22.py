#!/usr/bin/env python3
"""Exact necessary-condition audit for the remaining eight-no-root k=6 Profile A.

Profile A has a rank-two six-row puncture state with virtual deficiency d6=2,
exactly five actual singleton replacements, one distinct pair replacement, and
replacement-functional rank six.  Every one-coordinate puncture preserves
coefficient rank two, has virtual deficiency d5=2, and the descended actual
replacement functionals span the five-dimensional punctured quotient.

The older six-row d=2 singleton-shadow audit seeds only from five-row parents
of singleton capacity at least five.  That is exhaustive for its six-singleton
target, but not for Profile A: when the pair survives and one singleton block
leaves the virtual-complete set, a five-row child may have singleton capacity
only four.  This verifier repairs the cover by starting from every repaired
five-row rank-two d=2 parent of singleton capacity at least four.

For every synchronized six-row d=2 child of singleton capacity exactly five it
requires all six five-row deficiencies to remain two.  The five singleton
replacement blocks are then forced to be all five singleton-compatible blocks.
A candidate pair block must be a distinct canonical-complete block, and every
five-row puncture must retain at least five of these six actual replacement
blocks.  This last condition is necessary because a surjective puncture map
from the six-dimensional functional quotient to a five-dimensional quotient
cannot be spanned by fewer than five nonzero descended replacement classes.

The verifier finally computes the five singleton replacement functionals.  They
must already have extra rank five, and a compatible pair functional must raise
the extra rank to six.  The search is an overapproximation of actual states: it
does not require the displayed six replacement states alone to generate the
coefficient plane.  Therefore zero survivors is a rigorous exclusion of
Profile A, while a survivor is only a finite candidate for further checking.

All coefficient-space operations are exact rational row-space operations.
Integer relation and functional ranks use P=2^127-1, with Lucas-Lehmer and
explicit Hadamard bounds reported by the verifier.
"""

from argparse import ArgumentParser
from collections import Counter
from itertools import product
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_singleton_capacity_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_k6_profile_a_d2_cover", BASE)
A = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(A)

S = A.S
G = A.G
P0 = A.P0
R = A.R
K = A.K
MOD = A.MOD


def rank_mod_rows(rows):
    """Rank of an integer matrix with arbitrary width modulo MOD."""
    if not rows:
        return 0
    a = [[int(x) % MOD for x in row] for row in rows]
    nr = len(a)
    nc = len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, MOD)
        a[rank] = [(x * inv) % MOD for x in a[rank]]
        for i in range(nr):
            if i == rank or not a[i][col]:
                continue
            q = a[i][col]
            a[i] = [(x - q * y) % MOD for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def singleton_options(ext, block, space):
    return tuple(
        state
        for state in (1, 2, 4)
        if R.is_subspace(R.local_constraint_key(ext, block, state), space)
    )


def pair_options(ext, block, space):
    return tuple(
        state
        for state in (3, 5, 6)
        if R.is_subspace(R.local_constraint_key(ext, block, state), space)
    )


def replacement_functional(ext, block, state, space, complete_index, c):
    """Functional class for replacing one canonical-complete six-row block."""
    out = [0] * (c + 4)
    out[complete_index[block]] = 1
    alphas = R.nullspace_int(space, 6)
    assert len(alphas) == 4
    for i, alpha in enumerate(alphas):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext))
        beta_complete = R.solve_local_coeffs_int(7, (-vx, -vy))
        beta_new = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [beta_new[j] - beta_complete[j] for j in range(3)]
        lam = diff[0]
        assert diff == [lam, -lam, -lam]
        out[c + i] = -lam
    return tuple(out)


def scan(start, stop, stop_on_survivor=False):
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    rank_cache = {}
    counts = Counter()
    parent_capacity_census = Counter()
    six_capacity_census = Counter()
    singleton_rank_census = Counter()
    pair_rank_census = Counter()
    max_singleton_multiplicity = 0
    max_pair_multiplicity = 0
    max_relation_norm2 = 0
    max_functional_norm2 = 0
    max_functional_width = 0
    survivors = []

    for orbit_index in range(start, stop):
        ext5 = tuple(key_to_global[keys[i]] for i in orbits[orbit_index])
        touched5 = S.touched_blocks(ext5)

        for parent_space, _min_singletons in G.candidate_spaces(ext5, touched5):
            states5 = G.virtual_canonical(ext5, touched5, parent_space)
            complete5 = tuple(
                b for b, state in zip(touched5, states5) if state == 7
            )
            if S.deficiency(complete5, rank_cache) != 2:
                continue
            counts["five_d2_parents"] += 1
            good5 = A.compatible_singleton_blocks(ext5, parent_space, complete5)
            parent_capacity_census[len(good5)] += 1
            if len(good5) < 4:
                continue
            counts["five_d2_capacity4_parents"] += 1

            for extra in R.NO_ROOT:
                if extra in ext5:
                    continue
                counts["parent_extensions"] += 1
                ext6 = ext5 + (extra,)
                touched6 = S.touched_blocks(ext6)

                for space in S.candidate_six_planes(ext6, touched6, parent_space):
                    counts["candidate_P6"] += 1
                    projections = tuple(S.project_space(space, i) for i in range(6))
                    if any(len(projected) != 2 for projected in projections):
                        continue
                    counts["synchronized_P6"] += 1

                    states6 = G.virtual_canonical(ext6, touched6, space)
                    complete6 = tuple(
                        b for b, state in zip(touched6, states6) if state == 7
                    )
                    rank_complete = len(complete6) - S.deficiency(complete6, rank_cache)
                    if len(complete6) - rank_complete != 2:
                        continue
                    counts["synchronized_d2"] += 1

                    good6 = A.compatible_singleton_blocks(ext6, space, complete6)
                    six_capacity_census[len(good6)] += 1
                    if len(good6) != 5:
                        continue
                    counts["six_d2_capacity5"] += 1

                    projected_complete = []
                    all_d2 = True
                    for i, projected in enumerate(projections):
                        ext_i = ext6[:i] + ext6[i + 1:]
                        _touched_i, complete_i = S.canonical_complete_set(ext_i, projected)
                        if S.deficiency(complete_i, rank_cache) != 2:
                            all_d2 = False
                            break
                        projected_complete.append(complete_i)
                    if not all_d2:
                        continue
                    counts["all_five_projections_d2"] += 1
                    projected_complete = tuple(projected_complete)

                    rows = S.relation_rows_six(ext6, touched6, states6, space)
                    assert len(rows) == len(complete6) + 4
                    assert R.rank_mod(rows) == rank_complete
                    for row in rows:
                        max_relation_norm2 = max(
                            max_relation_norm2, sum(x * x for x in row)
                        )
                    transposed = [
                        tuple(rows[j][k] for j in range(len(rows)))
                        for k in range(15)
                    ]
                    assert rank_mod_rows(transposed) == rank_complete
                    max_functional_width = max(max_functional_width, len(rows))
                    for row in transposed:
                        max_functional_norm2 = max(
                            max_functional_norm2, sum(x * x for x in row)
                        )

                    complete_index = {
                        block: i for i, block in enumerate(complete6)
                    }
                    singleton_state_options = {
                        block: singleton_options(ext6, block, space)
                        for block in good6
                    }
                    assert all(singleton_state_options.values())
                    for options in singleton_state_options.values():
                        max_singleton_multiplicity = max(
                            max_singleton_multiplicity, len(options)
                        )

                    option_lists = [singleton_state_options[b] for b in good6]
                    for singleton_states in product(*option_lists):
                        singleton_vecs = [
                            replacement_functional(
                                ext6, block, state, space,
                                complete_index, len(complete6),
                            )
                            for block, state in zip(good6, singleton_states)
                        ]
                        for vec in singleton_vecs:
                            max_functional_norm2 = max(
                                max_functional_norm2, sum(x * x for x in vec)
                            )
                        singleton_extra = (
                            rank_mod_rows(transposed + singleton_vecs)
                            - rank_complete
                        )
                        singleton_rank_census[singleton_extra] += 1
                        if singleton_extra < 5:
                            continue
                        assert singleton_extra == 5
                        counts["five_singletons_independent"] += 1

                        good_set = set(good6)
                        for pair_block in complete6:
                            if pair_block in good_set:
                                continue

                            replacement_blocks = good6 + (pair_block,)
                            if any(
                                sum(block not in complete_i for block in replacement_blocks) > 1
                                for complete_i in projected_complete
                            ):
                                continue
                            counts["pair_blocks_puncture_eligible"] += 1

                            options = pair_options(ext6, pair_block, space)
                            max_pair_multiplicity = max(
                                max_pair_multiplicity, len(options)
                            )
                            for pair_state in options:
                                pair_vec = replacement_functional(
                                    ext6, pair_block, pair_state, space,
                                    complete_index, len(complete6),
                                )
                                max_functional_norm2 = max(
                                    max_functional_norm2,
                                    sum(x * x for x in pair_vec),
                                )
                                combined_extra = (
                                    rank_mod_rows(
                                        transposed + singleton_vecs + [pair_vec]
                                    )
                                    - rank_complete
                                )
                                pair_rank_census[combined_extra] += 1
                                if combined_extra < 6:
                                    continue
                                assert combined_extra == 6
                                counts["full_mixed_rank6"] += 1
                                if len(survivors) < 20:
                                    survivors.append(
                                        (
                                            orbit_index,
                                            ext6,
                                            space,
                                            complete6,
                                            good6,
                                            singleton_states,
                                            pair_block,
                                            pair_state,
                                            projected_complete,
                                        )
                                    )
                                if stop_on_survivor:
                                    return {
                                        "counts": counts,
                                        "parent_capacity_census": parent_capacity_census,
                                        "six_capacity_census": six_capacity_census,
                                        "singleton_rank_census": singleton_rank_census,
                                        "pair_rank_census": pair_rank_census,
                                        "max_singleton_multiplicity": max_singleton_multiplicity,
                                        "max_pair_multiplicity": max_pair_multiplicity,
                                        "max_relation_norm2": max_relation_norm2,
                                        "max_functional_norm2": max_functional_norm2,
                                        "max_functional_width": max_functional_width,
                                        "survivors": survivors,
                                        "rank_cache_size": len(rank_cache),
                                    }

    return {
        "counts": counts,
        "parent_capacity_census": parent_capacity_census,
        "six_capacity_census": six_capacity_census,
        "singleton_rank_census": singleton_rank_census,
        "pair_rank_census": pair_rank_census,
        "max_singleton_multiplicity": max_singleton_multiplicity,
        "max_pair_multiplicity": max_pair_multiplicity,
        "max_relation_norm2": max_relation_norm2,
        "max_functional_norm2": max_functional_norm2,
        "max_functional_width": max_functional_width,
        "survivors": survivors,
        "rank_cache_size": len(rank_cache),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    parser.add_argument("--stop-on-survivor", action="store_true")
    parser.add_argument("--require-no-survivors", action="store_true")
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    max_complete_norm2 = max(sum(x * x for x in row) for row in P0.COMPLETE_T)
    assert max_complete_norm2 == 12
    assert MOD * MOD > max_complete_norm2 ** 15

    _, orbits, _, _ = K.five_no_root_orbits()
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)

    result = scan(args.orbit_start, end, args.stop_on_survivor)

    relation_bound = max(max_complete_norm2, result["max_relation_norm2"])
    assert MOD * MOD > max(1, relation_bound) ** 15
    if result["max_functional_width"]:
        assert (
            MOD * MOD
            > max(1, result["max_functional_norm2"])
            ** result["max_functional_width"]
        )

    if args.require_no_survivors:
        assert not result["survivors"], result["survivors"][0]
        assert result["counts"]["full_mixed_rank6"] == 0

    print("PASS: six-row rank-two d2 capacity-five singleton-plus-pair audit")
    print("orbit_range", args.orbit_start, end)
    print("cover_counts", dict(result["counts"]))
    print(
        "five_d2_singleton_capacity_census",
        dict(sorted(result["parent_capacity_census"].items())),
    )
    print(
        "six_d2_singleton_capacity_census",
        dict(sorted(result["six_capacity_census"].items())),
    )
    print(
        "five_singleton_extra_rank_census",
        dict(sorted(result["singleton_rank_census"].items())),
    )
    print(
        "mixed_extra_rank_census",
        dict(sorted(result["pair_rank_census"].items())),
    )
    print("full_mixed_rank6_count", result["counts"]["full_mixed_rank6"])
    print("survivor_examples", result["survivors"])
    print("max_singleton_state_multiplicity", result["max_singleton_multiplicity"])
    print("max_pair_state_multiplicity", result["max_pair_multiplicity"])
    print("complete_rank_cache_size", result["rank_cache_size"])
    print("max_relation_row_norm_squared", result["max_relation_norm2"])
    print("max_functional_row_norm_squared", result["max_functional_norm2"])
    print("max_functional_width", result["max_functional_width"])
    print(
        "hadamard_exact_relation_rank_bound",
        MOD * MOD > max(1, relation_bound) ** 15,
    )
    print(
        "hadamard_exact_functional_rank_bound",
        (not result["max_functional_width"])
        or MOD * MOD
        > max(1, result["max_functional_norm2"])
        ** result["max_functional_width"],
    )


if __name__ == "__main__":
    main()
