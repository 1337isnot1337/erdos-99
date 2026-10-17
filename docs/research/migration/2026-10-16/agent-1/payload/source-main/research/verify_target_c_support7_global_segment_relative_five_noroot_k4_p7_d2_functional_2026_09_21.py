#!/usr/bin/env python3
"""Exact functional-span audit for the five-no-root k=4,p=7,d=2 residual.

The committed k=4 containment theorem gives a virtual canonical complete set C
with complete-row deficiency d=2.  At p=7, only q=6 or q=7 can evade the
uniform D>=3 bound.  The q=6 cases are either five canonical-complete
singletons plus one canonical-complete pair, or six canonical-complete
singletons plus one singleton on a canonical-empty block.  The q=7 case would
require seven canonical-complete singletons.

For a canonical relation matrix M with rank r=c-2, replacing a complete block b
by an incomplete compatible state imposes a row-index functional ell_b.  If q
complete blocks are replaced and s is the rank gained by their functionals
modulo Col(M), then the actual T-relation rank is r-q+s.  This verifier computes
an overapproximation to s exactly modulo 2^127-1.

Across the exact five-row orbit census, only nine d=2 canonical states admit at
least five compatible canonical-complete singleton blocks.  Every one has
singleton-functional extra rank exactly two.  Even after adjoining an arbitrary
pair functional, the extra rank is at most three.  The singleton capacity is at
most six, so q=7 is impossible.  Consequently the two q=6 forms have defect at
least 9 and 12 respectively.
"""
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k4_containment_2026_09_20.py"
spec = importlib.util.spec_from_file_location("five_k4_containment_for_p7_d2", BASE)
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(C)
R = C.R
MOD = R.P

EXPECTED_SINGLETON_SPAN = {(5, 2): 2, (6, 2): 7}
EXPECTED_PAIR_OVERAPP = {(5, 2, 3, 0): 2, (6, 2, 3, 0): 7}


def rank_mod_rows(rows):
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
        pv = a[rank][col]
        for i in range(rank + 1, nr):
            q = a[i][col]
            if q:
                a[i] = [(pv * x - q * y) % MOD for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def replacement_functional(ext, block, state, line, complete_index, c):
    out = [0] * (c + 4)
    out[complete_index[block]] = 1
    for i, alpha in enumerate(R.nullspace_int(line, 5)):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext))
        beta_complete = R.solve_local_coeffs_int(7, (-vx, -vy))
        beta_new = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [beta_new[j] - beta_complete[j] for j in range(3)]
        lam = diff[0]
        assert diff == [lam, -lam, -lam]
        out[c + i] = -lam
    return tuple(out)


def main():
    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = C.K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {C.K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    complete_rank_cache = {}
    singleton_span = Counter()
    pair_overapprox = Counter()
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
            if len(singleton_state) < 5:
                continue

            rows = C.relation_rows_line(ext, touched, states, line)
            assert len(rows) == c + 4
            assert R.rank_mod(rows) == rank_complete
            transposed = [
                tuple(rows[j][k] for j in range(len(rows)))
                for k in range(15)
            ]
            assert rank_mod_rows(transposed) == rank_complete
            complete_index = {b: i for i, b in enumerate(complete)}
            singleton_functionals = {
                b: replacement_functional(
                    ext, b, s, line, complete_index, c
                )
                for b, s in singleton_state.items()
            }

            singleton_extra = (
                rank_mod_rows(transposed + list(singleton_functionals.values()))
                - rank_complete
            )
            singleton_span[(len(singleton_state), singleton_extra)] += 1

            best_pair_extra = 0
            full_pair_states = 0
            for pair_block in complete:
                others = [
                    vec for b, vec in singleton_functionals.items()
                    if b != pair_block
                ]
                for pair_state in (3, 5, 6):
                    extra = (
                        rank_mod_rows(
                            transposed
                            + others
                            + [replacement_functional(
                                ext, pair_block, pair_state, line,
                                complete_index, c,
                            )]
                        )
                        - rank_complete
                    )
                    best_pair_extra = max(best_pair_extra, extra)
                    if extra >= 6:
                        full_pair_states += 1
            pair_overapprox[(
                len(singleton_state), singleton_extra,
                best_pair_extra, full_pair_states,
            )] += 1

            max_width = max(max_width, len(rows))
            for row in transposed + list(singleton_functionals.values()):
                max_norm2 = max(max_norm2, sum(x * x for x in row))

        if (orbit_index + 1) % 3000 == 0:
            print(
                "progress", orbit_index + 1,
                "candidate_bases", sum(singleton_span.values()),
                "elapsed", round(time.time() - t0, 1),
                flush=True,
            )

    assert dict(sorted(singleton_span.items())) == EXPECTED_SINGLETON_SPAN
    assert dict(sorted(pair_overapprox.items())) == EXPECTED_PAIR_OVERAPP
    assert max(capacity for capacity, _ in singleton_span) == 6
    assert max(extra for _, extra in singleton_span) == 2
    assert max(best for _, _, best, _ in pair_overapprox) == 3
    assert all(full == 0 for _, _, _, full in pair_overapprox)
    assert max_norm2 == 22
    assert max_width == 14
    assert MOD * MOD > max_norm2 ** max_width

    print("PASS: five-no-root k=4,p=7,d=2 functional audit")
    print("singleton_span", dict(sorted(singleton_span.items())))
    print("pair_overapprox", dict(sorted(pair_overapprox.items())))
    print("candidate_bases", sum(singleton_span.values()))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", MOD * MOD > max_norm2 ** max_width)
    print("elapsed", round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
