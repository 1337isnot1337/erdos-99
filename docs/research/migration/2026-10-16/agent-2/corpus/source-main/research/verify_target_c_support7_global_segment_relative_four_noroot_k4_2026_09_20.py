#!/usr/bin/env python3
"""Close the t=4,k=4 branch of the Target-C four-cycle rank-density audit.

For a family with four no-root four-cycles, k=4 means the four external rows
are individually cancellable in Q by the selected root-0 rows. Compare any
such selection A with F, the selection obtained by completing every touched
root-0 quotient block. Since A is a row-subfamily of F, every Q-relation of A
is also a Q-relation of F after zero-padding, hence delta(A) <= delta(F).

This verifier computes delta(F) exactly on all 1,186 S7 orbits and combines it
with the exact minimum root-0 row cost for a k=4 state with p<=7. The rank
bound leaves only 367 states. Those are reranked exactly and all have defect
|A|-3*delta(A)=8.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

BASE = Path("research/verify_target_c_support7_global_segment_relative_four_noroot_k2_2026_09_20.py")
spec = importlib.util.spec_from_file_location("relative_four_noroot_k2_for_k4", BASE)
R = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(R)

SINGLETONS = (1, 2, 4)


def relation_rank(ext, touched, states, norm_tracker):
    rows = R.relation_rows_int(ext, touched, states, ())
    for row in rows:
        norm_tracker[0] = max(norm_tracker[0], sum(x * x for x in row))
    return R.rank_mod(rows)


def singleton_options(ext, b):
    out = tuple(s for s in SINGLETONS if R.local_constraint_key(ext, b, s) == ())
    # A touched block contains a nonzero external Q component. The three
    # singleton directions are pairwise distinct, so at most one can work.
    assert len(out) <= 1
    assert R.local_constraint_key(ext, b, 0) != ()
    return out


def min_p_for_q(q, singleton_count):
    use_singletons = min(q, singleton_count)
    return use_singletons + 2 * (q - use_singletons)


def main():
    assert R.lucas_lehmer_127()
    orbits = R.four_no_root_orbits()
    assert len(orbits) == 1186

    norm_tracker = [0]
    full_rank_census = Counter()
    coarse_defect_census = Counter()
    dangerous_class_census = Counter()
    dangerous = []

    for oi, (ext, _orbit_size, touched) in enumerate(orbits):
        m = len(touched)
        full_states = (7,) * m
        full_rank = relation_rank(ext, touched, full_states, norm_tracker)
        full_rank_census[(m, full_rank)] += 1

        singleton_data = []
        for pos, b in enumerate(touched):
            opts = singleton_options(ext, b)
            if opts:
                singleton_data.append((pos, opts[0]))
        s = len(singleton_data)

        best = None
        best_qp = []
        for q in range(m + 1):
            p = min_p_for_q(q, s)
            if p > 7:
                continue
            c = m - q
            defect_lb = 4 + 3 * c + p - 3 * full_rank
            if best is None or defect_lb < best:
                best = defect_lb
                best_qp = [(q, p)]
            elif defect_lb == best:
                best_qp.append((q, p))
        assert best is not None
        coarse_defect_census[best] += 1

        if best < 0:
            dangerous_class_census[(m, s, full_rank, best, tuple(best_qp))] += 1
            # The census below proves the only dangerous lower-bound point is
            # q=p=7. Thus all seven incomplete blocks must be compatible
            # singletons; no pair state can occur in an unresolved case.
            assert best == -1 and best_qp == [(7, 7)]
            assert (m, s, full_rank) in ((11, 7, 8), (12, 8, 9))
            for chosen in combinations(singleton_data, 7):
                states = [7] * m
                for pos, mask in chosen:
                    states[pos] = mask
                dangerous.append((oi, ext, touched, full_rank, tuple(states)))

    assert dict(dangerous_class_census) == {
        (11, 7, 8, -1, ((7, 7),)): 63,
        (12, 8, 9, -1, ((7, 7),)): 38,
    }
    assert len(dangerous) == 367

    exact_defect_census = Counter()
    exact_rank_census = Counter()
    min_exact_defect = None
    for oi, ext, touched, full_rank, states in dangerous:
        rank = relation_rank(ext, touched, states, norm_tracker)
        c = sum(s == 7 for s in states)
        p = sum(R.STATES[s][5] for s in states)
        assert p == 7
        defect = 4 + 3 * c + p - 3 * rank
        min_exact_defect = defect if min_exact_defect is None else min(min_exact_defect, defect)
        exact_defect_census[defect] += 1
        exact_rank_census[(len(touched), full_rank, rank)] += 1
        assert defect >= 0, (oi, defect, rank, ext, touched, states)

    assert dict(exact_defect_census) == {8: 367}
    assert dict(exact_rank_census) == {
        (11, 8, 5): 63,
        (12, 9, 6): 304,
    }
    assert min_exact_defect == 8

    B = max(1, norm_tracker[0])
    assert R.P * R.P > B ** 15

    print("PASS: four-no-root k=4,p<=7 rank-density branch")
    print("four_no_root_subsets", 4_780_230)
    print("S7_orbits", len(orbits))
    print("full_rank_census", dict(sorted(full_rank_census.items())))
    print("coarse_defect_census", dict(sorted(coarse_defect_census.items())))
    print("dangerous_class_census", dict(dangerous_class_census))
    print("dangerous_states_exactified", len(dangerous))
    print("exact_rank_census", dict(sorted(exact_rank_census.items())))
    print("exact_defect_census", dict(sorted(exact_defect_census.items())))
    print("min_exact_defect", min_exact_defect)
    print("max_relation_row_norm_squared", norm_tracker[0])
    print("hadamard_exact_rank_bound", R.P * R.P > B ** 15)
    print("corollary_min_no_root_cycles_in_any_sufficient_44_family", 5)


if __name__ == "__main__":
    main()
