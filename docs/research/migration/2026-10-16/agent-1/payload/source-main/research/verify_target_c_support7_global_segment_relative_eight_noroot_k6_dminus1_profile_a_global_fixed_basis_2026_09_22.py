#!/usr/bin/env python3
"""Direct fixed-eight-block global lift audit for remaining Profile A.

A genuine eight-row Profile A state has exactly seven singleton replacement
blocks plus one pair block.  The eight actual replacement classes span the
8-dimensional global quotient, so they form a basis.  Choose a three-clean
coordinate and then any further coordinate; the resulting six-row state lies
in the existing coverage-correct Profile A audit and has exactly five surviving
singleton blocks plus the same pair block.

This wrapper starts only from pair states that already pass the exact common
six-to-five puncture-basis filter.  It exhaustively restores a clean seventh row
and then the eighth row, enumerates the two missing global singleton blocks, and
requires one fixed eight-class basis to have the forced ranks 8,7,6,5 through
the entire selected 8->7->6->5 puncture fan.  A zero-survivor full cover is
therefore a rigorous exclusion of Profile A.
"""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k4_d2_profile_a_common_functional_basis_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_a_common_basis", BASE)
C0 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(C0)

A0 = C0.A0
S = C0.S
G = C0.G
P0 = C0.P0
R = C0.R
ORIG_STRONG_PAIR_OPTIONS = A0.pair_options

GLOBAL_A_COUNTS = {
    "pair_states_after_common_basis": 0,
    "seven_extensions": 0,
    "seven_candidate_planes": 0,
    "seven_clean_d2": 0,
    "eight_extensions": 0,
    "eight_candidate_planes": 0,
    "eight_d2": 0,
    "fixed_global_singleton_choices": 0,
    "fixed_basis_structural_candidates": 0,
    "fixed_rank8": 0,
    "fixed_rank7": 0,
    "fixed_full_six_fan": 0,
    "fixed_full_five_fan": 0,
    "global_profile_a_survivors": 0,
}
GLOBAL_A_EXAMPLES = []


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
                basis[old] = [x - q0 * y for x, y in zip(basis[old], r)]
        basis[pivot] = r
    return len(basis)


def canonical_columns(rows):
    return [tuple(rows[j][k] for j in range(len(rows))) for k in range(15)]


def generic_relation_rows(ext, touched, states, space):
    rows = [
        P0.COMPLETE_T[block]
        for block, state in zip(touched, states)
        if state == 7
    ]
    alphas = R.nullspace_int(space, len(ext))
    assert len(alphas) == len(ext) - 2
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
            for local_index, q in enumerate(beta):
                if not q:
                    continue
                for j in range(15):
                    tv[j] += q * R.MCOORD[ids[local_index]][70 + j]
        rows.append(tuple(tv))
    return rows


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


def canonical_state(ext, space, rank_cache):
    touched = S.touched_blocks(ext)
    states = G.virtual_canonical(ext, touched, space)
    complete = tuple(b for b, s in zip(touched, states) if s == 7)
    d = S.deficiency(complete, rank_cache)
    rows = generic_relation_rows(ext, touched, states, space)
    canonical = canonical_columns(rows)
    base_rank = rank_q(canonical)
    complete_rank = rank_q([P0.COMPLETE_T[b] for b in complete])
    if base_rank != complete_rank:
        return None
    return complete, d, rows, canonical, base_rank


def fixed_extra_rank(ext, space, state_data, block_states):
    complete, _d, _rows, canonical, base_rank = state_data
    complete_set = set(complete)
    complete_index = {b: i for i, b in enumerate(complete)}
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


def candidate_rank2_lifts(ext, touched, parent_space):
    drop = len(ext) - 1
    options = {}
    for block in touched:
        local_spaces = set()
        for state in (0, 1, 2, 4):
            local = R.local_constraint_key(ext, block, state)
            if not local or len(local) > 2:
                continue
            if R.is_subspace(S.project_space(local, drop), parent_space):
                local_spaces.add(local)
        if local_spaces:
            options[block] = tuple(local_spaces)

    candidates = set()
    rank_one = []
    for block, spaces in options.items():
        for local in spaces:
            if len(local) == 2:
                if S.project_space(local, drop) == parent_space:
                    candidates.add(local)
            else:
                rank_one.append((block, local))

    for i, (block_i, space_i) in enumerate(rank_one):
        for block_j, space_j in rank_one[i + 1:]:
            if block_i == block_j:
                continue
            joined = R.union_key(space_i, space_j)
            if len(joined) == 2 and S.project_space(joined, drop) == parent_space:
                candidates.add(joined)
    return tuple(candidates)


def clean_seven_state(ext7, space7, rank_cache):
    one = tuple(S.project_space(space7, i) for i in range(7))
    if any(len(p) != 2 for p in one):
        return None
    for i in range(7):
        for j in range(i + 1, 7):
            p = S.project_space(space7, j)
            p = S.project_space(p, i)
            if len(p) != 2:
                return None
    state7 = canonical_state(ext7, space7, rank_cache)
    if state7 is None or state7[1] != 2:
        return None
    return state7


def fixed_global_basis_exists(
    ext8, space8, ext7, space7, state7,
    ext6_seed, space6_seed, fixed5, pair_block, pair_state, rank_cache,
):
    if any(len(S.project_space(space8, i)) != 2 for i in range(8)):
        return False
    state8 = canonical_state(ext8, space8, rank_cache)
    if state8 is None or state8[1] != 2:
        return False
    GLOBAL_A_COUNTS["eight_d2"] += 1

    complete8 = state8[0]
    if pair_block not in complete8:
        return False
    good8 = []
    for block in complete8:
        options = A0.singleton_options(ext8, block, space8)
        if not options:
            continue
        assert len(options) == 1
        good8.append((block, options[0]))
    good8_map = dict(good8)
    if any(block not in good8_map or good8_map[block] != state for block, state in fixed5):
        return False

    six_states = []
    for i in range(7):
        ext6 = ext7[:i] + ext7[i + 1:]
        space6 = S.project_space(space7, i)
        if len(space6) != 2:
            return False
        state6 = canonical_state(ext6, space6, rank_cache)
        if state6 is None or state6[1] != 2:
            return False
        if pair_block not in state6[0]:
            return False
        six_states.append((ext6, space6, state6))

    # The seed six-row state is the deletion of the appended seventh row.
    seed_key = (ext6_seed, space6_seed)
    assert any((ext6, space6) == seed_key for ext6, space6, _ in six_states)

    five_map = {}
    for ext6, space6, _state6 in six_states:
        for j in range(6):
            ext5 = ext6[:j] + ext6[j + 1:]
            space5 = S.project_space(space6, j)
            if len(space5) != 2:
                return False
            state5 = canonical_state(ext5, space5, rank_cache)
            if state5 is None or state5[1] != 2:
                return False
            five_map[(ext5, space5)] = (ext5, space5, state5)
    five_states = tuple(five_map.values())
    assert len(five_states) == 21

    fixed_blocks = {b for b, _ in fixed5}
    extra_options = [item for item in good8 if item[0] not in fixed_blocks and item[0] != pair_block]
    if len(extra_options) < 2:
        return False

    complete7 = set(state7[0])
    complete6_sets = tuple(set(state[2][0]) for state in six_states)
    complete5_sets = tuple(set(state[2][0]) for state in five_states)

    for extra_two in combinations(extra_options, 2):
        global_singletons = tuple(fixed5) + tuple(extra_two)
        global_blocks = tuple(b for b, _ in global_singletons) + (pair_block,)
        GLOBAL_A_COUNTS["fixed_global_singleton_choices"] += 1

        # Exact profile consequences before expensive ranks.
        if sum(b not in complete7 for b in global_blocks) > 1:
            continue
        # Every six-row child has exactly five surviving global singletons and
        # the pair survives; this is the exact Profile A six-row form.
        if any(
            sum(b in complete6 for b, _ in global_singletons) != 5
            for complete6 in complete6_sets
        ):
            continue
        # V8 -> V5 has kernel dimension three.
        if any(
            sum(b not in complete5 for b in global_blocks) > 3
            for complete5 in complete5_sets
        ):
            continue
        GLOBAL_A_COUNTS["fixed_basis_structural_candidates"] += 1

        block_states = global_singletons + ((pair_block, pair_state),)
        if fixed_extra_rank(ext8, space8, state8, block_states) != 8:
            continue
        GLOBAL_A_COUNTS["fixed_rank8"] += 1
        if fixed_extra_rank(ext7, space7, state7, block_states) != 7:
            continue
        GLOBAL_A_COUNTS["fixed_rank7"] += 1
        if any(
            fixed_extra_rank(ext6, space6, state6, block_states) != 6
            for ext6, space6, state6 in six_states
        ):
            continue
        GLOBAL_A_COUNTS["fixed_full_six_fan"] += 1
        if any(
            fixed_extra_rank(ext5, space5, state5, block_states) != 5
            for ext5, space5, state5 in five_states
        ):
            continue
        GLOBAL_A_COUNTS["fixed_full_five_fan"] += 1

        if len(GLOBAL_A_EXAMPLES) < 20:
            GLOBAL_A_EXAMPLES.append(
                (ext8, space8, global_singletons, pair_block, pair_state)
            )
        return True
    return False


def has_global_profile_a_lift(ext6, space6, fixed5, pair_block, pair_state):
    rank_cache = {}
    for extra7 in R.NO_ROOT:
        if extra7 in ext6:
            continue
        GLOBAL_A_COUNTS["seven_extensions"] += 1
        ext7 = ext6 + (extra7,)
        touched7 = S.touched_blocks(ext7)
        for space7 in candidate_rank2_lifts(ext7, touched7, space6):
            GLOBAL_A_COUNTS["seven_candidate_planes"] += 1
            state7 = clean_seven_state(ext7, space7, rank_cache)
            if state7 is None:
                continue
            if pair_block not in state7[0]:
                continue
            GLOBAL_A_COUNTS["seven_clean_d2"] += 1

            for extra8 in R.NO_ROOT:
                if extra8 in ext7:
                    continue
                GLOBAL_A_COUNTS["eight_extensions"] += 1
                ext8 = ext7 + (extra8,)
                touched8 = S.touched_blocks(ext8)
                for space8 in candidate_rank2_lifts(ext8, touched8, space7):
                    GLOBAL_A_COUNTS["eight_candidate_planes"] += 1
                    if not fixed_global_basis_exists(
                        ext8, space8, ext7, space7, state7,
                        ext6, space6, fixed5, pair_block, pair_state, rank_cache,
                    ):
                        continue
                    GLOBAL_A_COUNTS["global_profile_a_survivors"] += 1
                    return True
    return False


def global_pair_options(ext6, pair_block, space6):
    options = ORIG_STRONG_PAIR_OPTIONS(ext6, pair_block, space6)
    if not options:
        return ()

    touched6 = S.touched_blocks(ext6)
    states6 = G.virtual_canonical(ext6, touched6, space6)
    complete6 = tuple(b for b, s in zip(touched6, states6) if s == 7)
    good6 = A0.A.compatible_singleton_blocks(ext6, space6, complete6)
    assert len(good6) == 5
    fixed5 = []
    for block in good6:
        singleton = A0.singleton_options(ext6, block, space6)
        assert len(singleton) == 1
        fixed5.append((block, singleton[0]))
    fixed5 = tuple(fixed5)

    out = []
    for pair_state in options:
        GLOBAL_A_COUNTS["pair_states_after_common_basis"] += 1
        if has_global_profile_a_lift(
            ext6, space6, fixed5, pair_block, pair_state
        ):
            out.append(pair_state)
    return tuple(out)


A0.pair_options = global_pair_options


if __name__ == "__main__":
    try:
        A0.main()
    finally:
        print("profile_a_common_basis_counts", C0.COMMON_BASIS_COUNTS)
        print("profile_a_common_basis_examples", C0.COMMON_BASIS_EXAMPLES)
        print("profile_a_global_counts", GLOBAL_A_COUNTS)
        print("profile_a_global_examples", GLOBAL_A_EXAMPLES)
