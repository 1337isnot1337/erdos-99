#!/usr/bin/env python3
"""Exact puncture-consistency strengthening for the remaining Profile A audit.

A surviving six-row Profile A state has exactly five singleton replacement
classes plus one pair replacement class, and those six classes form a basis of
the six-dimensional replacement-functional quotient.  Every one-coordinate
puncture has a five-dimensional quotient.  Puncture functoriality sends each
of the six fixed classes to the corresponding punctured class when its block
remains virtual-canonical complete and to zero otherwise.  Hence the images of
the same five singleton states and the same pair state must have exact rank five
in every puncture.

The underlying coverage-correct Profile A verifier already checks the six-row
rank, all six rank-two/d=2 punctures, and the necessary at-most-one block-loss
condition.  This wrapper filters its pair-state options by the stronger exact
common-basis condition before the base verifier can accept a survivor.
"""

from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_capacity5_singleton_pair_functional_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_a_base", BASE)
A0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(A0)

S = A0.S
G = A0.G
P0 = A0.P0
R = A0.R
ORIG_PAIR_OPTIONS = A0.pair_options

COMMON_BASIS_COUNTS = {
    "pair_option_calls": 0,
    "pair_states_before": 0,
    "pair_states_full_all_punctures": 0,
}
COMMON_BASIS_EXAMPLES = []


def rank_q(rows):
    basis = {}
    for row in rows:
        r = [Fraction(x) for x in row]
        for pivot in sorted(basis):
            if r[pivot]:
                q = r[pivot]
                b = basis[pivot]
                r = [x - q * y for x, y in zip(r, b)]
        pivot = next((i for i, x in enumerate(r) if x), None)
        if pivot is None:
            continue
        q = r[pivot]
        r = [x / q for x in r]
        for old in list(basis):
            if basis[old][pivot]:
                q0 = basis[old][pivot]
                basis[old] = [
                    x - q0 * y for x, y in zip(basis[old], r)
                ]
        basis[pivot] = r
    return len(basis)


def canonical_columns(rows):
    return [
        tuple(rows[j][k] for j in range(len(rows)))
        for k in range(15)
    ]


def replacement_functional(ext, block, state, space, complete_index, c):
    t = len(ext)
    nullity = t - len(space)
    out = [0] * (c + nullity)
    out[complete_index[block]] = 1
    alphas = R.nullspace_int(space, t)
    assert len(alphas) == nullity
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


def punctured_fixed_rank(ext, space, block_states):
    touched = S.touched_blocks(ext)
    states = G.virtual_canonical(ext, touched, space)
    complete = tuple(
        block for block, state in zip(touched, states) if state == 7
    )
    if S.deficiency(complete, {}) != 2:
        return None
    rows = P0.relation_rows(ext, touched, states, space)
    canonical = canonical_columns(rows)
    base_rank = rank_q(canonical)
    complete_rank = rank_q([P0.COMPLETE_T[b] for b in complete])
    if base_rank != complete_rank:
        return None

    complete_set = set(complete)
    complete_index = {block: i for i, block in enumerate(complete)}
    vectors = []
    for block, state in block_states:
        if block not in complete_set:
            continue
        if state in (1, 2, 4):
            options = A0.singleton_options(ext, block, space)
            assert len(options) == 1
            assert options[0] == state
        vectors.append(
            replacement_functional(
                ext, block, state, space, complete_index, len(complete)
            )
        )
    return rank_q(canonical + vectors) - base_rank


def strong_pair_options(ext6, pair_block, space6):
    options = ORIG_PAIR_OPTIONS(ext6, pair_block, space6)
    if not options:
        return ()
    COMMON_BASIS_COUNTS["pair_option_calls"] += 1
    COMMON_BASIS_COUNTS["pair_states_before"] += len(options)

    touched6 = S.touched_blocks(ext6)
    states6 = G.virtual_canonical(ext6, touched6, space6)
    complete6 = tuple(
        block for block, state in zip(touched6, states6) if state == 7
    )
    good6 = A0.A.compatible_singleton_blocks(ext6, space6, complete6)
    if len(good6) != 5:
        return ()

    singleton_states = []
    for block in good6:
        singleton = A0.singleton_options(ext6, block, space6)
        assert len(singleton) == 1
        singleton_states.append(singleton[0])
    fixed_singletons = tuple(zip(good6, singleton_states))

    projections = tuple(S.project_space(space6, i) for i in range(6))
    if any(len(projected) != 2 for projected in projections):
        return ()

    out = []
    for pair_state in options:
        block_states = fixed_singletons + ((pair_block, pair_state),)
        ok = True
        for i, projected in enumerate(projections):
            ext5 = ext6[:i] + ext6[i + 1:]
            extra_rank = punctured_fixed_rank(ext5, projected, block_states)
            if extra_rank != 5:
                ok = False
                break
        if not ok:
            continue
        COMMON_BASIS_COUNTS["pair_states_full_all_punctures"] += 1
        if len(COMMON_BASIS_EXAMPLES) < 20:
            COMMON_BASIS_EXAMPLES.append(
                (ext6, space6, good6, tuple(singleton_states), pair_block, pair_state)
            )
        out.append(pair_state)
    return tuple(out)


A0.pair_options = strong_pair_options


if __name__ == "__main__":
    try:
        A0.main()
    finally:
        print("profile_a_common_basis_counts", COMMON_BASIS_COUNTS)
        print("profile_a_common_basis_examples", COMMON_BASIS_EXAMPLES)
