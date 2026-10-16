#!/usr/bin/env python3
"""Global two-row lift audit for the remaining eight-no-root k=6 Profile B.

This wrapper strengthens the coverage-correct six-row Profile B audit by
requiring every surviving synchronized six-row state to lift through the clean
seven-row profile to an eight-row rank-two deficiency-three state with full
compatible-singleton functional rank nine.

The cover is deliberately an overapproximation of actual counterexamples: it
uses all compatible singleton blocks at each level and does not yet require one
fixed set of nine actual global singleton blocks.  Hence a zero-survivor full
cover rigorously excludes Profile B, while a survivor is only a finite global
candidate.
"""

from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_profile_b_common_functional_basis_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_common_basis", BASE)
C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(C)

B = C.B
R = B.R
S = B.S
G = B.G
P0 = B.P0
ORIG_STRONG_COMMON_BASIS = B.common_basis_block_sets

GLOBAL_LIFT_COUNTS = {
    "seven_extensions": 0,
    "seven_candidate_planes": 0,
    "seven_clean_rank2": 0,
    "seven_d3": 0,
    "seven_full_span8": 0,
    "seven_all_six_shadows": 0,
    "eight_extensions": 0,
    "eight_candidate_planes": 0,
    "eight_all_single_rank2": 0,
    "eight_d3": 0,
    "eight_full_span9": 0,
    "global_lift_survivors": 0,
}
GLOBAL_LIFT_EXAMPLES = []


def generic_relation_rows(ext, touched, states, space):
    """Canonical relation rows for any rank-two coefficient space."""
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


def exact_singleton_span(ext, space, complete, rows):
    """Return (capacity, extra rank) exactly over Q, or None if containment fails."""
    c = len(complete)
    canonical = C.canonical_columns(rows)
    base_rank = C.rank_q(canonical)
    complete_rank = C.rank_q([P0.COMPLETE_T[b] for b in complete])
    if base_rank != complete_rank:
        return None

    complete_index = {block: i for i, block in enumerate(complete)}
    vectors = []
    capacity = 0
    for block in complete:
        options = B.singleton_options(ext, block, space)
        if not options:
            continue
        # A virtual-canonical complete block has at most one compatible singleton.
        assert len(options) == 1
        capacity += 1
        vectors.append(
            B.replacement_functional(
                ext, block, options[0], space, complete_index, c
            )
        )
    extra = C.rank_q(canonical + vectors) - base_rank
    return capacity, extra


def candidate_rank2_lifts(ext, touched, parent_space):
    """Enumerate every realizable rank-two space projecting to parent_space.

    The last external coordinate is the restored row.  As in the established
    six-row extension engine, a rank-two coefficient space has a basis supplied
    either by one rank-two local constraint or by rank-one local constraints on
    two distinct blocks.
    """
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
                assert len(local) == 1
                rank_one.append((block, local))

    for i, (block_i, space_i) in enumerate(rank_one):
        for block_j, space_j in rank_one[i + 1:]:
            if block_i == block_j:
                continue
            joined = R.union_key(space_i, space_j)
            if len(joined) == 2 and S.project_space(joined, drop) == parent_space:
                candidates.add(joined)
    return tuple(candidates)


def synchronized_six_shadow_ok(ext6, space6, rank_cache):
    touched6 = S.touched_blocks(ext6)
    states6 = G.virtual_canonical(ext6, touched6, space6)
    complete6 = tuple(
        b for b, state in zip(touched6, states6) if state == 7
    )
    if S.deficiency(complete6, rank_cache) != 3:
        return False
    rows6 = generic_relation_rows(ext6, touched6, states6, space6)
    span = exact_singleton_span(ext6, space6, complete6, rows6)
    return span is not None and span[0] >= 7 and span[1] == 7


def clean_seven_ok(ext7, space7, rank_cache):
    # The missing eighth coordinate is three-clean iff every one- and two-row
    # puncture of this seven-row projection retains coefficient rank two.
    one = tuple(S.project_space(space7, i) for i in range(7))
    if any(len(p) != 2 for p in one):
        return False
    for i in range(7):
        for j in range(i + 1, 7):
            p = S.project_space(space7, j)
            p = S.project_space(p, i)
            if len(p) != 2:
                return False
    GLOBAL_LIFT_COUNTS["seven_clean_rank2"] += 1

    touched7 = S.touched_blocks(ext7)
    states7 = G.virtual_canonical(ext7, touched7, space7)
    complete7 = tuple(
        b for b, state in zip(touched7, states7) if state == 7
    )
    if S.deficiency(complete7, rank_cache) != 3:
        return False
    GLOBAL_LIFT_COUNTS["seven_d3"] += 1

    rows7 = generic_relation_rows(ext7, touched7, states7, space7)
    span7 = exact_singleton_span(ext7, space7, complete7, rows7)
    if span7 is None or span7[0] < 8 or span7[1] != 8:
        return False
    GLOBAL_LIFT_COUNTS["seven_full_span8"] += 1

    # Every one-coordinate deletion lies in the synchronized d6=3 clean fan.
    for i, projected in enumerate(one):
        ext6 = ext7[:i] + ext7[i + 1:]
        if not synchronized_six_shadow_ok(ext6, projected, rank_cache):
            return False
    GLOBAL_LIFT_COUNTS["seven_all_six_shadows"] += 1
    return True


def global_eight_ok(ext8, space8, rank_cache):
    # Every external row is a Q-noncoloop in the eight-no-root k=6 layer.
    if any(len(S.project_space(space8, i)) != 2 for i in range(8)):
        return False
    GLOBAL_LIFT_COUNTS["eight_all_single_rank2"] += 1

    touched8 = S.touched_blocks(ext8)
    states8 = G.virtual_canonical(ext8, touched8, space8)
    complete8 = tuple(
        b for b, state in zip(touched8, states8) if state == 7
    )
    if S.deficiency(complete8, rank_cache) != 3:
        return False
    GLOBAL_LIFT_COUNTS["eight_d3"] += 1

    rows8 = generic_relation_rows(ext8, touched8, states8, space8)
    span8 = exact_singleton_span(ext8, space8, complete8, rows8)
    if span8 is None or span8[0] < 9 or span8[1] != 9:
        return False
    GLOBAL_LIFT_COUNTS["eight_full_span9"] += 1
    return True


def has_global_profile_b_lift(ext6, space6):
    rank_cache = {}
    for extra7 in R.NO_ROOT:
        if extra7 in ext6:
            continue
        GLOBAL_LIFT_COUNTS["seven_extensions"] += 1
        ext7 = ext6 + (extra7,)
        touched7 = S.touched_blocks(ext7)
        for space7 in candidate_rank2_lifts(ext7, touched7, space6):
            GLOBAL_LIFT_COUNTS["seven_candidate_planes"] += 1
            if not clean_seven_ok(ext7, space7, rank_cache):
                continue

            for extra8 in R.NO_ROOT:
                if extra8 in ext7:
                    continue
                GLOBAL_LIFT_COUNTS["eight_extensions"] += 1
                ext8 = ext7 + (extra8,)
                touched8 = S.touched_blocks(ext8)
                for space8 in candidate_rank2_lifts(ext8, touched8, space7):
                    GLOBAL_LIFT_COUNTS["eight_candidate_planes"] += 1
                    if not global_eight_ok(ext8, space8, rank_cache):
                        continue
                    GLOBAL_LIFT_COUNTS["global_lift_survivors"] += 1
                    if len(GLOBAL_LIFT_EXAMPLES) < 20:
                        GLOBAL_LIFT_EXAMPLES.append((ext6, space6, ext7, space7, ext8, space8))
                    return True
    return False


def global_lift_common_basis(good6, projected_complete, projected_data):
    candidates = ORIG_STRONG_COMMON_BASIS(
        good6, projected_complete, projected_data
    )
    if not candidates:
        return ()
    assert C.CURRENT_SIX is not None
    ext6, space6, _complete6, recorded_good6 = C.CURRENT_SIX
    assert tuple(good6) == recorded_good6
    if not has_global_profile_b_lift(ext6, space6):
        return ()
    return candidates


B.common_basis_block_sets = global_lift_common_basis


if __name__ == "__main__":
    try:
        B.main()
    finally:
        print("global_lift_counts", GLOBAL_LIFT_COUNTS)
        print("global_lift_examples", GLOBAL_LIFT_EXAMPLES)
