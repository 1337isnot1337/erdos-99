#!/usr/bin/env python3
"""Exact five-row d=2 audit for four singleton functionals plus one pair.

This is the low-dimensional obstruction needed by the remaining eight-no-root
k=6, D=-1, p=9 profile A.  After a three-clean deletion fan, every relevant
five-row shadow has rank-two coefficient space and virtual deficiency d=2.  If
the unique pair replacement disappears, q>=5 forces at least five singleton
replacements, already excluded by the committed p=7,d=2 functional audit.
The only untested possibility is therefore four singleton replacements plus the
surviving pair, which would have to span the full five-dimensional replacement
functional quotient.

We deliberately overapproximate that possibility.  For every exact five-row
d=2 virtual-canonical state with at least four compatible singleton blocks, we
choose every four compatible singleton blocks, then adjoin every state 3,5,6
on every distinct canonical-complete block as an arbitrary pair functional.
The pair state is not required to satisfy its local compatibility constraint.
Thus a zero full-rank count rules out the actual mixed configuration a fortiori.

Ranks are computed modulo the Mersenne prime 2^127-1.  The final Hadamard bound
certifies that the modular upper bound is also an exact rational upper bound.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k4_p7_d2_functional_2026_09_21.py"
spec = importlib.util.spec_from_file_location("five_k4_d2_functional_base", BASE)
F = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(F)
C = F.C
R = F.R
MOD = F.MOD


def main():
    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = C.K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {C.K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    complete_rank_cache = {}
    capacity_distribution = Counter()
    four_single_rank_distribution = Counter()
    mixed_rank_distribution = Counter()
    candidate_states = 0
    four_single_choices = 0
    mixed_choices = 0
    full_rank_choices = 0
    max_four_single_extra = 0
    max_mixed_extra = 0
    max_norm2 = 0
    max_width = 0
    t0 = time.time()

    for orbit_index, five in enumerate(orbits):
        ext = tuple(key_to_global[keys[i]] for i in five)
        touched = tuple(sorted(
            b for b in range(35)
            if any(R.QCOMP[e][b] != (0, 0) for e in ext)
        ))

        for line in C.obtainable_lines(ext, touched):
            states = C.virtual_canonical(ext, touched, line)
            complete = tuple(b for b, s in zip(touched, states) if s == 7)
            c = len(complete)
            rank_complete = complete_rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([C.COMPLETE_T[b] for b in complete])
                complete_rank_cache[complete] = rank_complete
            if c - rank_complete != 2:
                continue

            singleton_state = {}
            for block in complete:
                opts = tuple(
                    s for s in (1, 2, 4)
                    if R.is_subspace(R.local_constraint_key(ext, block, s), line)
                )
                if opts:
                    assert len(opts) == 1
                    singleton_state[block] = opts[0]
            if len(singleton_state) < 4:
                continue

            candidate_states += 1
            capacity_distribution[len(singleton_state)] += 1

            rows = C.relation_rows_line(ext, touched, states, line)
            assert len(rows) == c + 4
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert F.rank_mod_rows(transposed) == rank_complete
            complete_index = {b: i for i, b in enumerate(complete)}
            singleton_functionals = {
                b: F.replacement_functional(
                    ext, b, s, line, complete_index, c
                )
                for b, s in singleton_state.items()
            }

            for chosen in combinations(sorted(singleton_functionals), 4):
                chosen_rows = [singleton_functionals[b] for b in chosen]
                four_extra = (
                    F.rank_mod_rows(transposed + chosen_rows) - rank_complete
                )
                four_single_choices += 1
                four_single_rank_distribution[four_extra] += 1
                max_four_single_extra = max(max_four_single_extra, four_extra)

                chosen_set = set(chosen)
                for pair_block in complete:
                    if pair_block in chosen_set:
                        continue
                    for pair_state in (3, 5, 6):
                        pair_vec = F.replacement_functional(
                            ext, pair_block, pair_state, line,
                            complete_index, c,
                        )
                        mixed_extra = (
                            F.rank_mod_rows(
                                transposed + chosen_rows + [pair_vec]
                            ) - rank_complete
                        )
                        mixed_choices += 1
                        mixed_rank_distribution[mixed_extra] += 1
                        max_mixed_extra = max(max_mixed_extra, mixed_extra)
                        if mixed_extra >= 5:
                            full_rank_choices += 1

                        max_norm2 = max(
                            max_norm2,
                            sum(x * x for x in pair_vec),
                        )

                for row in chosen_rows:
                    max_norm2 = max(max_norm2, sum(x * x for x in row))
            for row in transposed:
                max_norm2 = max(max_norm2, sum(x * x for x in row))
            max_width = max(max_width, len(rows))

        if (orbit_index + 1) % 3000 == 0:
            print(
                "progress", orbit_index + 1,
                "candidate_states", candidate_states,
                "mixed_choices", mixed_choices,
                "max_mixed_extra", max_mixed_extra,
                "elapsed", round(time.time() - t0, 1),
                flush=True,
            )

    hadamard_exact = MOD * MOD > max_norm2 ** max_width
    assert hadamard_exact

    print("PASS: five-no-root k=4,d=2 four-singleton plus pair audit")
    print("capacity_distribution", dict(sorted(capacity_distribution.items())))
    print("candidate_states", candidate_states)
    print("four_single_choices", four_single_choices)
    print("four_single_rank_distribution", dict(sorted(four_single_rank_distribution.items())))
    print("mixed_choices", mixed_choices)
    print("mixed_rank_distribution", dict(sorted(mixed_rank_distribution.items())))
    print("max_four_single_extra", max_four_single_extra)
    print("max_mixed_extra", max_mixed_extra)
    print("full_rank_choices", full_rank_choices)
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", hadamard_exact)
    print("elapsed", round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
