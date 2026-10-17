#!/usr/bin/env python3
"""Close the seven-no-root D=-1,k=5,d=1,p=4 branch.

The proof uses the previously certified all-depth generalized-weight bounds and
the exact synchronized six-row k=4 extension census.  In a rank-two
coefficient space P <= Q^7, a pair puncture can lower rank only when P has a
nonzero word supported on that pair.  The bounds d1(P)>=2 and d2(P)>=4 imply
that such rank-drop pairs form a matching of size at most two.  Therefore some
coordinate i is incident to no rank-drop pair.  Deleting i gives a six-row
shadow whose every one-coordinate deletion still has rank-two coefficient
space.

For that synchronized six-row shadow the lifted five-row containment theorem
applies.  Since its exact defect is D=1 and p=4, equality forces virtual
canonical deficiency d=1 and q=4 canonical-complete blocks replaced by
incomplete states.  Thus four canonical-complete blocks must admit compatible
singletons.

This verifier repeats the exact six-row d=1 synchronized census, but unlike the
older six-row counterexample verifier it counts *all* canonical-complete blocks
admitting a compatible singleton, with no support-multiplicity filter.  There
are 31 synchronized d=1 planes; their unfiltered singleton capacities are only
0, 2, or 3.  Hence capacity four never occurs.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
RESEARCH = HERE if HERE.name == "research" else HERE / "research"
BASE = RESEARCH / "verify_target_c_support7_global_segment_relative_six_noroot_k4_2026_09_20.py"
spec = importlib.util.spec_from_file_location("six_k4_for_seven_k5_d1p4", BASE)
S = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(S)

R = S.R
P0 = S.P0
MOD = S.MOD

EXPECTED_CAPACITY = {0: 1, 2: 6, 3: 24}


def all_compatible_singleton_blocks(ext6, space, complete):
    """Canonical-complete blocks admitting any compatible singleton.

    No support lower bound is imposed here.  That is essential for the
    seven-row application: the synchronized six-row shadow has D=1 rather than
    being a six-row negative-defect counterexample.
    """
    good = []
    for block in complete:
        options = tuple(
            state
            for state in (1, 2, 4)
            if R.is_subspace(R.local_constraint_key(ext6, block, state), space)
        )
        if options:
            support = sum(R.QCOMP[e][block] != (0, 0) for e in ext6)
            good.append((block, options, support))
    return tuple(good)


def scan(parent_start, parent_end, rank_cache):
    parents = S.five_row_d1_parents(rank_cache)
    counts = Counter()
    deficiency_census = Counter()
    capacity_census = Counter()
    support_census = Counter()
    first_capacity_four = None

    for parent_index in range(parent_start, parent_end):
        ext5, parent_space = parents[parent_index]
        for extra in R.NO_ROOT:
            if extra in ext5:
                continue
            ext6 = ext5 + (extra,)
            touched = S.touched_blocks(ext6)
            counts["extensions"] += 1

            for space in S.candidate_six_planes(ext6, touched, parent_space):
                counts["candidate_P6"] += 1
                projections = tuple(S.project_space(space, i) for i in range(6))
                if any(len(projected) != 2 for projected in projections):
                    continue
                counts["all_projection_rank2"] += 1

                states = S.G.virtual_canonical(ext6, touched, space)
                complete = tuple(
                    block
                    for block, state in zip(touched, states)
                    if state == 7
                )
                d = S.deficiency(complete, rank_cache)
                deficiency_census[d] += 1
                if d != 1:
                    continue
                counts["six_d1"] += 1

                good = all_compatible_singleton_blocks(ext6, space, complete)
                capacity_census[len(good)] += 1
                for _block, _options, support in good:
                    support_census[support] += 1
                if len(good) >= 4 and first_capacity_four is None:
                    first_capacity_four = (ext6, space, complete, good)

    return parents, {
        "counts": counts,
        "deficiency_census": deficiency_census,
        "capacity_census": capacity_census,
        "support_census": support_census,
        "first_capacity_four": first_capacity_four,
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--parent-start", type=int, default=0)
    parser.add_argument("--parent-end", type=int)
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    max_complete_norm2 = max(sum(x * x for x in row) for row in P0.COMPLETE_T)
    assert max_complete_norm2 == 12
    assert MOD * MOD > max_complete_norm2 ** 15

    rank_cache = {}
    parents0 = S.five_row_d1_parents(rank_cache)
    end = len(parents0) if args.parent_end is None else args.parent_end
    assert 0 <= args.parent_start <= end <= len(parents0)

    parents, result = scan(args.parent_start, end, rank_cache)
    assert len(parents) == 86
    assert result["first_capacity_four"] is None, result["first_capacity_four"]

    if args.parent_start == 0 and end == len(parents):
        assert dict(result["counts"]) == {
            "extensions": 8600,
            "candidate_P6": 16781,
            "all_projection_rank2": 4684,
            "six_d1": 31,
        }
        assert dict(sorted(result["deficiency_census"].items())) == S.EXPECTED_DEFICIENCY
        assert dict(sorted(result["capacity_census"].items())) == EXPECTED_CAPACITY
        assert max(result["capacity_census"], default=-1) == 3
        # Stronger than needed: every compatible singleton in the 31 d=1
        # states is touched by exactly three of the six no-root cycles.
        assert dict(result["support_census"]) == {3: 84}

    print("PASS: seven-no-root D=-1,k=5,d=1,p=4 closure obstruction")
    print("five_row_d1_parent_states", len(parents))
    print("parent_range", args.parent_start, end)
    print("extension_cover_counts", dict(result["counts"]))
    print("synchronized_deficiency_census", dict(sorted(result["deficiency_census"].items())))
    print("unfiltered_singleton_capacity_census", dict(sorted(result["capacity_census"].items())))
    print("compatible_singleton_support_census", dict(sorted(result["support_census"].items())))
    print("max_unfiltered_singleton_capacity", max(result["capacity_census"], default=-1))
    print("hadamard_exact_rank_bound", MOD * MOD > max_complete_norm2 ** 15)


if __name__ == "__main__":
    main()
