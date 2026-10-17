#!/usr/bin/env python3
"""Exact rank-two witness invalidating the rank-one five-row obstruction.

The eight-no-root k=6 residual projects to five rows with coefficient-space
rank two (the five-row k=3 branch).  The recently added k=4 functional audits
instead enumerate rank-one coefficient spaces.  This certificate exhibits a
rank-two five-row d=2 virtual state in which four compatible singleton
replacements plus one distinct pair replacement have full functional rank 5.
It therefore prevents importing the k=4 rank bounds into the k=6 punctures.
"""
from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k3_p4_sharp_2026_09_21.py"
spec = importlib.util.spec_from_file_location("five_k3_p4_for_rank2_witness", BASE)
P4 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(P4)
C = P4.C
P0 = P4.P0
R = P4.R
MOD = R.P

EXT = (106, 109, 112, 105, 107)
SPACE = (
    (Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1)),
)
EXPECTED_TOUCHED = (0, 1, 2, 3, 5, 6, 7, 15, 16, 17)
EXPECTED_COMPLETE = (1, 2, 3, 5, 6, 7, 15, 16, 17)
SINGLETONS = ((2, 1), (3, 1), (15, 2), (16, 2))
PAIR = (1, 3)
EXPECTED_STATES = (0, 3, 1, 1, 7, 7, 7, 2, 2, 7)


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


def replacement_functional(ext, block, state, space, complete_index, c):
    out = [0] * (c + 3)
    out[complete_index[block]] = 1
    alphas = R.nullspace_int(space, 5)
    assert len(alphas) == 3
    for i, alpha in enumerate(alphas):
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
    touched = tuple(sorted(
        b for b in range(35)
        if any(R.QCOMP[e][b] != (0, 0) for e in EXT)
    ))
    assert touched == EXPECTED_TOUCHED

    candidate = dict(C.candidate_spaces(EXT, touched))
    assert SPACE in candidate
    assert candidate[SPACE] == 0
    assert len(SPACE) == 2

    base = C.virtual_canonical(EXT, touched, SPACE)
    complete = tuple(b for b, s in zip(touched, base) if s == 7)
    assert complete == EXPECTED_COMPLETE
    complete_rows = [P0.COMPLETE_T[b] for b in complete]
    complete_rank = R.rank_mod(complete_rows)
    assert len(complete) - complete_rank == 2
    assert complete_rank == 7

    pos = {b: i for i, b in enumerate(touched)}
    states = list(base)
    for b, s in SINGLETONS:
        assert b in complete
        assert R.is_subspace(R.local_constraint_key(EXT, b, s), SPACE)
        states[pos[b]] = s
    pair_block, pair_state = PAIR
    assert pair_block in complete and pair_block not in {b for b, _ in SINGLETONS}
    assert pair_state in (3, 5, 6)
    states[pos[pair_block]] = pair_state
    states = tuple(states)
    assert states == EXPECTED_STATES
    assert P4.actual_space(EXT, touched, states) == SPACE

    base_rows = P0.relation_rows(EXT, touched, base, SPACE)
    assert len(base_rows) == len(complete) + 3
    assert R.rank_mod(base_rows) == complete_rank
    transposed = [
        tuple(base_rows[j][k] for j in range(len(base_rows)))
        for k in range(15)
    ]
    assert rank_mod_rows(transposed) == complete_rank

    complete_index = {b: i for i, b in enumerate(complete)}
    functionals = [
        replacement_functional(EXT, b, s, SPACE, complete_index, len(complete))
        for b, s in SINGLETONS + (PAIR,)
    ]
    functional_rank = rank_mod_rows(transposed + functionals) - complete_rank
    assert functional_rank == 5

    actual_rows = P0.relation_rows(EXT, touched, states, SPACE)
    delta = R.rank_mod(actual_rows)
    nrows = 5 + sum(R.STATES[s][1] for s in states)
    defect = nrows - 3 * delta
    assert (nrows, delta, defect) == (23, 7, 2)

    max_norm2 = max(
        sum(x * x for x in row)
        for row in transposed + functionals + actual_rows
    )
    max_width = max(len(row) for row in transposed + functionals)
    assert MOD * MOD > max(1, max_norm2) ** max(15, max_width)

    print("PASS: rank-two five-row d=2 mixed full-rank witness")
    print("external_rows", EXT)
    print("coefficient_rank", len(SPACE))
    print("virtual_deficiency", len(complete) - complete_rank)
    print("singleton_replacements", SINGLETONS)
    print("pair_replacement", PAIR)
    print("mixed_functional_extra_rank", functional_rank)
    print("actual_rank_defect", (nrows, delta, defect))
    print("hadamard_exact_rank_bound", True)


if __name__ == "__main__":
    main()
