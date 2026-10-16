#!/usr/bin/env python3
"""Exact functional-span audit for the five-no-root k=4,p=7,d=3 residual.

The committed k=4 containment theorem gives D>=5+p+3d-3q.  At p=7 and
d=3, only q=7 can lie below D=3, forcing seven singleton replacements of
canonical-complete blocks.

For the canonical relation matrix M, let r=c-3.  Replacing complete block b by
its compatible singleton imposes a row-index functional ell_b.  If q=7 such
blocks are replaced and the chosen functionals gain rank s modulo Col(M), the
actual T-relation rank is r-q+s and the defect is 21-3s.  Thus a defect below
3 would require s=7.

This verifier exhausts every d=3 virtual canonical line with at least seven
compatible singleton-complete blocks and proves that even the span of all such
singleton functionals has extra rank at most six.  Hence every d=3,q=7,p=7
state has defect at least three.
"""
from collections import Counter
from pathlib import Path
import contextlib
import importlib.util
import io
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k4_containment_2026_09_20.py"
spec = importlib.util.spec_from_file_location("five_k4_containment_for_p7_d3", BASE)
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(C)
R = C.R
MOD = R.P

EXPECTED = {
    (7, 3): 55,
    (7, 4): 4920,
    (7, 5): 52,
    (7, 6): 11,
    (8, 3): 40,
    (8, 4): 3068,
    (8, 5): 80,
    (8, 6): 73,
    (9, 4): 383,
    (9, 6): 122,
    (10, 4): 159,
    (10, 6): 96,
}


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


def singleton_functional(ext, block, state, line, complete_index, c):
    out = [0] * (c + 4)
    out[complete_index[block]] = 1
    for i, alpha in enumerate(R.nullspace_int(line, 5)):
        vx = sum(alpha[j] * R.QCOMP[e][block][0] for j, e in enumerate(ext))
        vy = sum(alpha[j] * R.QCOMP[e][block][1] for j, e in enumerate(ext))
        beta_complete = R.solve_local_coeffs_int(7, (-vx, -vy))
        beta_singleton = R.solve_local_coeffs_int(state, (-vx, -vy))
        diff = [
            beta_singleton[j] - beta_complete[j]
            for j in range(3)
        ]
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

    rank_cache = {}
    census = Counter()
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
            rank_complete = rank_cache.get(complete)
            if rank_complete is None:
                rank_complete = R.rank_mod([C.COMPLETE_T[b] for b in complete])
                rank_cache[complete] = rank_complete
            if c - rank_complete != 3:
                continue

            singleton_state = []
            for block in complete:
                opts = tuple(
                    s for s in (1, 2, 4)
                    if R.is_subspace(R.local_constraint_key(ext, block, s), line)
                )
                if opts:
                    assert len(opts) == 1
                    singleton_state.append((block, opts[0]))
            if len(singleton_state) < 7:
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
            functionals = [
                singleton_functional(
                    ext, b, state, line, complete_index, c
                )
                for b, state in singleton_state
            ]
            total_rank = rank_mod_rows(transposed + functionals)
            extra_rank = total_rank - rank_complete
            census[(len(singleton_state), extra_rank)] += 1
            assert extra_rank < 7, (
                orbit_index, ext, line, complete,
                tuple(singleton_state), extra_rank,
            )

            max_width = max(max_width, len(rows))
            for row in transposed + functionals:
                max_norm2 = max(max_norm2, sum(x * x for x in row))

        if (orbit_index + 1) % 3000 == 0:
            print(
                "progress", orbit_index + 1,
                "candidate_bases", sum(census.values()),
                "elapsed", round(time.time() - t0, 1),
                flush=True,
            )

    assert dict(sorted(census.items())) == EXPECTED
    assert sum(census.values()) == 9059
    assert max(extra for _, extra in census) == 6
    assert max_norm2 == 35
    assert max_width == 18
    assert MOD * MOD > max_norm2 ** max_width

    print("PASS: five-no-root k=4,p=7,d=3 functional audit")
    print("functional_span_census", dict(sorted(census.items())))
    print("candidate_bases", sum(census.values()))
    print("max_extra_rank", max(extra for _, extra in census))
    print("max_row_norm_squared", max_norm2)
    print("max_functional_width", max_width)
    print("hadamard_exact_rank_bound", MOD * MOD > max_norm2 ** max_width)
    print("elapsed", round(time.time() - t0, 2))


if __name__ == "__main__":
    main()
