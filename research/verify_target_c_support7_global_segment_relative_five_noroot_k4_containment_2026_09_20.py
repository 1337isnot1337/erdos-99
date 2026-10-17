#!/usr/bin/env python3
"""Exact closure of the t=5, k=4, p<=6 rank-density branch.

For five no-root four-cycles, k=4 means that the global coefficient-constraint
space P is a line in the five external coefficients.  Every actual rank-one P
must occur as a nonzero local constraint from an empty or singleton state.
For each such P this verifier forms a virtual canonical state: a touched root-0
block is empty when its empty-state constraint is contained in P, and complete
otherwise.  The virtual state need not itself generate P; this is essential for
covering lines generated only by singleton constraints.

Let C be the canonical complete-block set, c=|C|, and H(C) the span in T of the
complete-block relation rows.  Exhaustively over all 20,451 S7 orbits and all
177,316 obtainable lines P, the verifier proves exactly that

  * c-rank H(C) >= 2; and
  * all four external null(P) relation rows lie in H(C).

These facts propagate from the virtual canonical state to every actual state
with the same P.  If q canonical-complete blocks are made incomplete and p is
the total number of selected root-0 rows in incomplete blocks, then q<=p and

    delta(A) <= rank H(C) = c-d,
    |A|-3 delta(A) >= 5 + p + 3d - 3q.

Thus p<=5 is automatic.  For p=6 the only potentially negative case is
(d,q,p)=(2,6,6), so six canonical-complete blocks must each be replaced by a
singleton.  Among all 342 d=2 virtual canonical states there are only seven
such realizable states.  Each is reranked over Q with Fraction arithmetic and
has delta=4, |A|=23, defect 11.

Therefore every five-no-root k=4,p<=6 family satisfies 3*delta(A)<=|A|.
The modular containment/rank screening is exact over Q by a Lucas-Lehmer check
for P=2^127-1 and an explicit Hadamard determinant bound.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("relative_five_noroot_k5_for_k4_containment", BASE)
K = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K)
R = K.R

COMPLETE_T = tuple(
    tuple(
        R.MCOORD[ids[0]][70 + j]
        - R.MCOORD[ids[1]][70 + j]
        - R.MCOORD[ids[2]][70 + j]
        for j in range(15)
    )
    for ids in R.BLOCKS
)
assert max(sum(x * x for x in row) for row in COMPLETE_T) == 12


def relation_rows_line(ext, touched, states, line):
    """Integer T-relation rows for a rank-one external constraint space."""
    rows = []
    for block, state in zip(touched, states):
        if state == 7:
            rows.append(COMPLETE_T[block])

    alphas = R.nullspace_int(line, 5)
    assert len(alphas) == 4
    for alpha in alphas:
        tv = [
            sum(alpha[i] * R.MCOORD[e][70 + j] for i, e in enumerate(ext))
            for j in range(15)
        ]
        for block, state in zip(touched, states):
            vx = sum(alpha[i] * R.QCOMP[e][block][0] for i, e in enumerate(ext))
            vy = sum(alpha[i] * R.QCOMP[e][block][1] for i, e in enumerate(ext))
            beta = R.solve_local_coeffs_int(R.STATES[state][0], (-vx, -vy))
            ids = R.BLOCKS[block]
            for local_index, coeff in enumerate(beta):
                if coeff:
                    for j in range(15):
                        tv[j] += coeff * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tuple(tv))
    return rows


def obtainable_lines(ext, touched):
    """All rank-one P that an actual k=4 state can generate locally."""
    return tuple(sorted({
        key
        for block in touched
        for state in (0, 1, 2, 4)
        for key in (R.local_constraint_key(ext, block, state),)
        if len(key) == 1
    }, key=repr))


def virtual_canonical(ext, touched, line):
    """Empty iff the empty constraint is contained in P; otherwise complete."""
    return tuple(
        0 if R.is_subspace(R.local_constraint_key(ext, block, 0), line) else 7
        for block in touched
    )


def union_constraints(ext, touched, states):
    key = ()
    for block, state in zip(touched, states):
        key = R.union_key(key, R.local_constraint_key(ext, block, state))
    return key


def main():
    assert R.lucas_lehmer_127()
    keys, orbits, orbit_sizes, augmentation_candidates = K.five_no_root_orbits()
    assert len(orbits) == 20451
    assert sum(orbit_sizes) == 96560646
    assert augmentation_candidates == 20475
    key_to_global = {K.cycle_key(R.DESC[e]): e for e in R.NO_ROOT}

    canonical_count = 0
    generated_by_empty = Counter()
    complete_count = Counter()
    deficiency = Counter()
    max_relation_norm2 = 0
    d2_records = []

    for local_five in orbits:
        ext = tuple(key_to_global[keys[i]] for i in local_five)
        touched = tuple(sorted(
            block
            for block in range(35)
            if any(R.QCOMP[e][block] != (0, 0) for e in ext)
        ))

        for line in obtainable_lines(ext, touched):
            states = virtual_canonical(ext, touched, line)
            canonical_count += 1
            generated = union_constraints(ext, touched, states) == line
            generated_by_empty[generated] += 1

            complete_set = tuple(
                block for block, state in zip(touched, states) if state == 7
            )
            c = len(complete_set)
            hrows = [COMPLETE_T[block] for block in complete_set]
            hrank = R.rank_mod(hrows)
            d = c - hrank
            complete_count[c] += 1
            deficiency[d] += 1
            assert d >= 2, (ext, touched, line, complete_set, hrank)

            rows = relation_rows_line(ext, touched, states, line)
            external_rows = rows[c:]
            assert len(external_rows) == 4
            for row in rows:
                max_relation_norm2 = max(
                    max_relation_norm2, sum(x * x for x in row)
                )
            # The Hadamard check below makes these modular containments exact
            # over Q rather than probabilistic finite-field statements.
            for row in external_rows:
                assert R.rank_mod(hrows + [row]) == hrank, (
                    ext, touched, line, complete_set, row
                )

            if d == 2:
                singleton_options = []
                for block in complete_set:
                    opts = tuple(
                        state
                        for state in (1, 2, 4)
                        if R.is_subspace(
                            R.local_constraint_key(ext, block, state), line
                        )
                    )
                    assert len(opts) <= 1
                    if opts:
                        singleton_options.append((block, opts[0]))
                d2_records.append((ext, touched, line, complete_set, tuple(singleton_options)))

    assert canonical_count == 177316
    assert dict(generated_by_empty) == {False: 65494, True: 111822}
    assert dict(sorted(complete_count.items())) == {
        7: 117,
        8: 216,
        9: 637,
        10: 3194,
        11: 7028,
        12: 12832,
        13: 25586,
        14: 48808,
        15: 38643,
        16: 21636,
        17: 13504,
        18: 4662,
        19: 453,
    }
    assert dict(sorted(deficiency.items())) == {
        2: 342,
        3: 14467,
        4: 116835,
        5: 40038,
        6: 5487,
        7: 147,
    }
    assert len(d2_records) == 342
    assert max_relation_norm2 == 26
    assert R.P * R.P > max_relation_norm2 ** 15

    singleton_capacity = Counter(len(record[4]) for record in d2_records)
    assert dict(sorted(singleton_capacity.items())) == {
        0: 156,
        1: 7,
        2: 28,
        3: 47,
        4: 95,
        5: 2,
        6: 7,
    }

    # Only d=2,p=q=6 can evade the uniform lower bound.  Such a state uses
    # six singleton replacements of canonical-complete blocks.  Canonical-empty
    # blocks stay empty because p is already exhausted.
    candidate_six_sets = 0
    realized_states = 0
    exact_defect = Counter()
    exact_rank = Counter()
    max_exact_norm2 = 0

    for ext, touched, line, complete_set, singleton_options in d2_records:
        if len(singleton_options) < 6:
            continue
        complete_lookup = set(complete_set)
        for six in combinations(singleton_options, 6):
            candidate_six_sets += 1
            singleton_map = dict(six)
            states = tuple(
                singleton_map[block]
                if block in singleton_map
                else (7 if block in complete_lookup else 0)
                for block in touched
            )
            if union_constraints(ext, touched, states) != line:
                continue
            realized_states += 1
            rows = relation_rows_line(ext, touched, states, line)
            delta = R.exact_rank(rows)
            n = 5 + sum(R.STATES[state][1] for state in states)
            defect = n - 3 * delta
            exact_defect[defect] += 1
            exact_rank[(n, delta, defect)] += 1
            for row in rows:
                max_exact_norm2 = max(max_exact_norm2, sum(x * x for x in row))
            assert defect >= 0, (ext, touched, line, states, delta, defect)

    assert candidate_six_sets == 7
    assert realized_states == 7
    assert dict(exact_defect) == {11: 7}
    assert dict(exact_rank) == {(23, 4, 11): 7}
    assert max_exact_norm2 == 12

    print("PASS: five-no-root k=4,p<=6 containment closure")
    print("five_no_root_subsets", 96560646)
    print("S7_orbits", len(orbits))
    print("rank_one_virtual_canonical_states", canonical_count)
    print("generated_by_empty", dict(sorted(generated_by_empty.items())))
    print("complete_count_census", dict(sorted(complete_count.items())))
    print("deficiency_census", dict(sorted(deficiency.items())))
    print("max_canonical_relation_row_norm_squared", max_relation_norm2)
    print("hadamard_exact_rank_bound", R.P * R.P > max_relation_norm2 ** 15)
    print("d2_states", len(d2_records))
    print("d2_singleton_capacity", dict(sorted(singleton_capacity.items())))
    print("dangerous_p6_candidate_sets", candidate_six_sets)
    print("dangerous_p6_realized_states", realized_states)
    print("dangerous_p6_exact_rank_census", dict(sorted(exact_rank.items())))
    print("dangerous_p6_exact_defect_census", dict(sorted(exact_defect.items())))
    print("max_dangerous_exact_row_norm_squared", max_exact_norm2)


if __name__ == "__main__":
    main()
