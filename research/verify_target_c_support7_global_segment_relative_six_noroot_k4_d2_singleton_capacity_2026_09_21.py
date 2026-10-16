#!/usr/bin/env python3
"""Exact synchronized six-row d=2 singleton-shadow audit for Target C.

This is the finite obstruction produced by the seven-no-root
D=-2,k=5,d=0,p=6 reduction.

A hypothetical seven-row state forces every one-coordinate deletion to be a
synchronized six-row rank-two coefficient state with virtual deficiency d6=2
and six actual singleton blocks, all virtual-canonical complete. Every further
coordinate deletion has five-row virtual deficiency d5=2 and at least five of
those same six singleton blocks still virtual-canonical complete.

Coverage therefore starts only from repaired five-row d=2 rank-two parents
having at least five singleton-compatible canonical-complete blocks, augments
by every possible sixth no-root row, enumerates every rank-two six-row plane
projecting to the parent, and applies the exact six/five-shadow conditions.
Duplicates are harmless: zero survivors is an exact exclusion.
"""
from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_six_noroot_k4_2026_09_20.py"
spec = importlib.util.spec_from_file_location("six_k4_base_for_d2_capacity", BASE)
S = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(S)
G = S.G
P0 = S.P0
R = S.R
K = S.K
MOD = S.MOD

EXPECTED_FIVE_D2 = 15865


def compatible_singleton_blocks(ext, space, complete):
    """Canonical-complete blocks admitting at least one singleton state."""
    return tuple(
        block
        for block in complete
        if any(
            R.is_subspace(R.local_constraint_key(ext, block, state), space)
            for state in (1, 2, 4)
        )
    )


def common_six_block_sets(good6, projected_complete):
    """Six blocks with at most one becoming canonical-empty per deletion."""
    projected_sets = tuple(set(x) for x in projected_complete)
    out = []
    for blocks in combinations(good6, 6):
        ok = True
        for complete_i in projected_sets:
            if sum(block not in complete_i for block in blocks) > 1:
                ok = False
                break
        if ok:
            out.append(blocks)
    return tuple(out)


def scan_orbits(start, stop, stop_on_survivor=False):
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    rank_cache = {}
    counts = Counter()
    parent_capacity_census = Counter()
    six_capacity_census = Counter()
    common_set_census = Counter()
    first_survivor = None

    for orbit_index in range(start, stop):
        ext5 = tuple(key_to_global[keys[i]] for i in orbits[orbit_index])
        touched5 = S.touched_blocks(ext5)

        for parent_space, _min_singletons in G.candidate_spaces(ext5, touched5):
            states5 = G.virtual_canonical(ext5, touched5, parent_space)
            complete5 = tuple(
                b for b, state in zip(touched5, states5) if state == 7
            )
            d5 = S.deficiency(complete5, rank_cache)
            if d5 != 2:
                continue
            counts["five_d2_parents"] += 1
            good5 = compatible_singleton_blocks(ext5, parent_space, complete5)
            parent_capacity_census[len(good5)] += 1
            if len(good5) < 5:
                continue
            counts["five_d2_capacity5_parents"] += 1

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
                    if S.deficiency(complete6, rank_cache) != 2:
                        continue
                    counts["synchronized_d2"] += 1

                    good6 = compatible_singleton_blocks(ext6, space, complete6)
                    six_capacity_census[len(good6)] += 1
                    if len(good6) < 6:
                        continue
                    counts["six_d2_capacity6"] += 1

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

                    block_sets = common_six_block_sets(
                        good6, tuple(projected_complete)
                    )
                    common_set_census[len(block_sets)] += 1
                    if not block_sets:
                        continue
                    counts["structural_survivor_P6"] += 1
                    counts["structural_survivor_block_sets"] += len(block_sets)
                    if first_survivor is None:
                        first_survivor = (
                            orbit_index, ext5, extra, ext6, space,
                            complete6, good6, tuple(projected_complete), block_sets,
                        )
                    if stop_on_survivor:
                        return {
                            "counts": counts,
                            "parent_capacity_census": parent_capacity_census,
                            "six_capacity_census": six_capacity_census,
                            "common_set_census": common_set_census,
                            "first_survivor": first_survivor,
                            "rank_cache_size": len(rank_cache),
                        }

    return {
        "counts": counts,
        "parent_capacity_census": parent_capacity_census,
        "six_capacity_census": six_capacity_census,
        "common_set_census": common_set_census,
        "first_survivor": first_survivor,
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

    result = scan_orbits(args.orbit_start, end, args.stop_on_survivor)

    if args.orbit_start == 0 and end == len(orbits) and not args.stop_on_survivor:
        assert result["counts"]["five_d2_parents"] == EXPECTED_FIVE_D2

    if args.require_no_survivors:
        assert result["first_survivor"] is None, result["first_survivor"]

    print("PASS: synchronized six-row d=2 singleton-shadow audit")
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
        "common_six_block_set_census",
        dict(sorted(result["common_set_census"].items())),
    )
    print("has_structural_survivor", result["first_survivor"] is not None)
    if result["first_survivor"] is not None:
        (
            oi, _ext5, _extra, ext6, _space, complete6, good6,
            projected_complete, block_sets,
        ) = result["first_survivor"]
        print("first_survivor_parent_orbit", oi)
        print("first_survivor_ext6", ext6)
        print("first_survivor_complete6", complete6)
        print("first_survivor_good6", good6)
        print("first_survivor_projected_complete", projected_complete)
        print("first_survivor_block_sets", block_sets)
    print("complete_rank_cache_size", result["rank_cache_size"])
    print(
        "hadamard_exact_complete_rank_bound",
        MOD * MOD > max_complete_norm2 ** 15,
    )


if __name__ == "__main__":
    main()
