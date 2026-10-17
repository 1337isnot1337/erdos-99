#!/usr/bin/env python3
"""Exact next-stage audit for the final seven-no-root k6,p10 reduction.

The support-zero pair-shadow theorem reduces every forced five-row
D=3,k=4,p=10 all-singleton shadow to virtual deficiency d in {4,5,6}.  If the
canonical-complete singleton replacement functionals gain extra rank s, the
functional defect bound

    D >= 5 + p + 3*d - 3*s

shows that D=3 requires s >= d+4.  Thus only the thresholds

    d=4: capacity >=8 and extra rank >=8
    d=5: capacity >=9 and extra rank >=9
    d=6: capacity >=10 and extra rank >=10

can matter.  This verifier scans exactly those virtual canonical states.  It
uses the same exact S7 five-subset orbit cover, replacement functionals, prime
modulus, and Hadamard rank certificate as the committed d=3 functional audit.

No expected survivor count is hard-coded: this file is an executable finite
target.  A zero `threshold_survivors` result would close every p=10 support-zero
pair shadow and therefore the final seven-no-root k=6 branch.
"""
from collections import Counter
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d3_functional_2026_09_21.py"
spec = importlib.util.spec_from_file_location("five_k4_d3_functional_for_p10", BASE)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)
C = F.C
R = F.R
MOD = F.MOD


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--orbit-start", type=int, default=0)
    ap.add_argument("--orbit-end", type=int)
    args = ap.parse_args()

    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = C.K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475

    start = args.orbit_start
    end = len(orbits) if args.orbit_end is None else args.orbit_end
    assert 0 <= start <= end <= len(orbits)

    key_to_global = {C.K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}
    rank_cache = {}
    candidate_census = Counter()
    threshold_survivors = Counter()
    max_extra = {4: 0, 5: 0, 6: 0}
    max_norm2 = 0
    max_width = 0
    t0 = time.time()

    for orbit_index in range(start, end):
        five = orbits[orbit_index]
        ext = tuple(key_to_global[keys[i]] for i in five)
        touched = tuple(sorted(
            b for b in range(35)
            if any(R.QCOMP[e][b] != (0, 0) for e in ext)
        ))

        for line in C.obtainable_lines(ext, touched):
            states = C.virtual_canonical(ext, touched, line)
            complete = tuple(b for b, state in zip(touched, states) if state == 7)
            c = len(complete)
            rank_complete = rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([C.COMPLETE_T[b] for b in complete])
                rank_cache[complete] = rank_complete
            d = c - rank_complete
            if d not in (4, 5, 6):
                continue

            threshold = d + 4
            singleton_state = []
            for block in complete:
                opts = tuple(
                    state
                    for state in (1, 2, 4)
                    if R.is_subspace(R.local_constraint_key(ext, block, state), line)
                )
                if opts:
                    assert len(opts) == 1
                    singleton_state.append((block, opts[0]))
            capacity = len(singleton_state)
            if capacity < threshold:
                continue

            rows = C.relation_rows_line(ext, touched, states, line)
            assert len(rows) == c + 4
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert F.rank_mod_rows(transposed) == rank_complete
            complete_index = {b: i for i, b in enumerate(complete)}
            functionals = [
                F.singleton_functional(
                    ext, block, state, line, complete_index, c
                )
                for block, state in singleton_state
            ]
            extra = F.rank_mod_rows(transposed + functionals) - rank_complete
            candidate_census[(d, capacity, extra)] += 1
            max_extra[d] = max(max_extra[d], extra)
            if extra >= threshold:
                threshold_survivors[(d, capacity, extra)] += 1

            max_width = max(max_width, len(rows))
            for row in transposed + functionals:
                max_norm2 = max(max_norm2, sum(x * x for x in row))

        if (orbit_index + 1 - start) % 2000 == 0:
            print(
                "progress", orbit_index + 1,
                "candidate_states", sum(candidate_census.values()),
                "threshold_survivors", sum(threshold_survivors.values()),
                "elapsed", round(time.time() - t0, 1),
                flush=True,
            )

    # Every modular rank reported here is exact over Q by the same determinant
    # argument as the parent audits.  The bound is checked against the largest
    # row norm and width actually encountered in this shard/full run.
    if max_width:
        assert MOD * MOD > max_norm2 ** max_width

    print("PASS: five-no-root k4,p10 d=4..6 functional target completed")
    print("orbit_range", (start, end))
    print("candidate_census", dict(sorted(candidate_census.items())))
    print("max_extra_rank", max_extra)
    print("threshold_survivors", dict(sorted(threshold_survivors.items())))
    print("threshold_survivor_count", sum(threshold_survivors.values()))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", (not max_width) or MOD * MOD > max_norm2 ** max_width)
    print("elapsed", round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
