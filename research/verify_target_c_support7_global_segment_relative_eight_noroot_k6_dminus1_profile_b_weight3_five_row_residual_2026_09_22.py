#!/usr/bin/env python3
"""Exact five-row rank-one audit for the Profile B weight-three residual.

The low-weight-support reduction for the remaining eight-no-root k=6,
D=-1,p=9 Profile B proves that if its rank-two coefficient plane has minimum
word weight three, deleting the support of a minimum word can survive only as

    t=5, k=4, D=2, p=6, d_root=1,
    virtual deficiency d=3,

with all six retained incomplete rows singleton blocks and with their six
canonical-complete replacement functionals gaining full extra rank six.

This verifier exhausts the exact five-no-root S7 orbit cover and every rank-one
virtual-canonical d=3 state with singleton capacity at least six. It computes
the span of all compatible singleton replacement functionals and reports every
state whose extra rank reaches six. A full-cover zero-survivor result would
exclude minimum coefficient weight three and force all eight source
coordinates to be three-clean.

Ranks use the same exact modular/Hadamard framework as the committed d=3,
capacity-at-least-seven audit.
"""

from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_weight3_d3_base", BASE)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)

C = F.C
R = F.R
MOD = R.P


def scan(orbits, keys, start, end):
    key_to_global = {C.K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    rank_cache = {}
    census = Counter()
    survivors = []
    max_norm2 = 0
    max_width = 0

    for orbit_index in range(start, end):
        five = orbits[orbit_index]
        ext = tuple(key_to_global[keys[i]] for i in five)
        touched = tuple(sorted(
            block for block in range(35)
            if any(R.QCOMP[e][block] != (0, 0) for e in ext)
        ))

        for line in C.obtainable_lines(ext, touched):
            states = C.virtual_canonical(ext, touched, line)
            complete = tuple(
                block for block, state in zip(touched, states) if state == 7
            )
            c = len(complete)
            rank_complete = rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([C.COMPLETE_T[b] for b in complete])
                rank_cache[complete] = rank_complete
            if c - rank_complete != 3:
                continue

            singleton_state = []
            for block in complete:
                options = tuple(
                    state for state in (1, 2, 4)
                    if R.is_subspace(R.local_constraint_key(ext, block, state), line)
                )
                if options:
                    assert len(options) == 1
                    singleton_state.append((block, options[0]))
            capacity = len(singleton_state)
            if capacity < 6:
                continue

            rows = C.relation_rows_line(ext, touched, states, line)
            assert len(rows) == c + 4
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert F.rank_mod_rows(transposed) == rank_complete

            complete_index = {block: i for i, block in enumerate(complete)}
            functionals = [
                F.singleton_functional(
                    ext, block, state, line, complete_index, c
                )
                for block, state in singleton_state
            ]
            extra = F.rank_mod_rows(transposed + functionals) - rank_complete
            census[(capacity, extra)] += 1

            if extra >= 6 and len(survivors) < 100:
                survivors.append((
                    orbit_index,
                    ext,
                    line,
                    complete,
                    tuple(singleton_state),
                    extra,
                ))

            max_width = max(max_width, len(rows))
            for row in transposed + functionals:
                max_norm2 = max(max_norm2, sum(x * x for x in row))

    if max_width:
        assert MOD * MOD > max_norm2 ** max_width

    return {
        "census": census,
        "survivors": survivors,
        "survivor_count": sum(
            count for (_capacity, extra), count in census.items() if extra >= 6
        ),
        "max_extra": max((extra for _, extra in census), default=0),
        "max_norm2": max_norm2,
        "max_width": max_width,
        "rank_cache_size": len(rank_cache),
    }


def main():
    parser = ArgumentParser()
    parser.add_argument("--orbit-start", type=int, default=0)
    parser.add_argument("--orbit-end", type=int)
    parser.add_argument(
        "--assert-empty",
        action="store_true",
        help="fail unless this shard has no extra-rank-six residual",
    )
    args = parser.parse_args()

    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = C.K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475

    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= args.orbit_start <= end <= len(orbits)
    result = scan(orbits, keys, args.orbit_start, end)

    if args.assert_empty:
        assert result["survivor_count"] == 0, result["survivors"][:5]

    print("PASS: Profile B weight-three five-row residual audit completed")
    print("orbit_range", (args.orbit_start, end))
    print("candidate_census", dict(sorted(result["census"].items())))
    print("candidate_count", sum(result["census"].values()))
    print("max_extra_rank", result["max_extra"])
    print("extra_rank_six_survivor_count", result["survivor_count"])
    print("survivor_examples", result["survivors"][:20])
    print("unique_complete_sets_ranked", result["rank_cache_size"])
    print("max_row_norm_squared", result["max_norm2"])
    print("max_functional_width", result["max_width"])
    print(
        "hadamard_exact_rank_bound",
        (not result["max_width"])
        or MOD * MOD > result["max_norm2"] ** result["max_width"],
    )


if __name__ == "__main__":
    main()
