#!/usr/bin/env python3
"""Exact omitted c=14 audit for the t=5,k=3,p=2 rank-density proof.

The original p=2 verifier handles canonical p=0 states with c<14 complete
blocks and skips c>=14.  For p=2, c>=15 is safe from dim(T)=15 after at most
two complete-block replacements.  The only omitted potentially dangerous
slice is therefore c=14 with two singleton replacements, which can leave 12
complete blocks and 43 selected rows.

This verifier classifies the rank of the 14 complete-block T rows in every
canonical c=14 state.  Their rank is always 10 or 11, so every 12-block subset
is dependent.  Hence its rank is at most 11; the three-dimensional external
coefficient nullspace then gives delta<=14 and defect |A|-3 delta>=1.

All rank decisions are exact over Q: the established complete-block rows are
integer vectors of squared norm at most 12, ranks are computed modulo the
Mersenne prime P=2^127-1, Lucas-Lehmer certifies primality, and the explicit
Hadamard bound P^2>12^15 prevents a nonzero rational minor from vanishing
modulo P.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
P0_PATH = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k3_p0_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k3p0_for_p2c14", P0_PATH)
P0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P0)
R = P0.R
K = P0.K


def scan(keys, orbits, start, stop):
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    complete_rank_cache = {}
    c14_states = 0
    rank_census = Counter()

    for orbit_index in range(start, stop):
        local_five = orbits[orbit_index]
        ext = tuple(key_to_global[keys[i]] for i in local_five)
        touched = tuple(sorted(
            b for b in range(35)
            if any(R.QCOMP[e][b] != (0, 0) for e in ext)
        ))

        for space in P0.candidate_rank2_constraint_spaces(ext, touched):
            states = P0.canonical_minimal_state(ext, touched, space)
            assert states is not None
            complete_set = tuple(
                b for b, state in zip(touched, states) if state == 7
            )
            if len(complete_set) != 14:
                continue

            c14_states += 1
            rank = complete_rank_cache.get(complete_set)
            if rank is None:
                rank = R.rank_mod([P0.COMPLETE_T[b] for b in complete_set])
                complete_rank_cache[complete_set] = rank
            rank_census[rank] += 1

    return {
        "c14_states": c14_states,
        "rank_census": rank_census,
        "complete_rank_cache_size": len(complete_rank_cache),
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

    max_complete_norm2 = max(
        sum(x * x for x in row) for row in P0.COMPLETE_T
    )
    assert max_complete_norm2 == 12
    assert R.P * R.P > max_complete_norm2 ** 15

    if args.orbit_start == 0 and end == len(orbits):
        assert len(orbits) == 20451
        assert sum(orbit_sizes) == 96560646
        assert augmentation_candidates == 20475
        assert result["c14_states"] == 10250
        assert dict(sorted(result["rank_census"].items())) == {
            10: 1224,
            11: 9026,
        }

    print("PASS: five-no-root k=3,p=2 c=14 omitted-slice audit")
    print("five_no_root_subsets", 96560646)
    print("S7_orbits", len(orbits))
    print("orbit_range", args.orbit_start, end)
    print("c14_canonical_states", result["c14_states"])
    print("c14_complete_rank_census", dict(sorted(result["rank_census"].items())))
    print("max_complete_row_norm_squared", max_complete_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_complete_norm2 ** 15)
    print("complete_rank_cache_size", result["complete_rank_cache_size"])


if __name__ == "__main__":
    main()
