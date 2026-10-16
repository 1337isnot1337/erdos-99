#!/usr/bin/env python3
"""Fixed-nine-block consistency audit for the remaining eight-no-root k=6 Profile B.

This wraps the direct global Profile B lift audit.  A genuine global Profile B
has exactly nine actual singleton replacement blocks and replacement-functional
quotient dimension nine.  Hence those same nine block classes form a basis at
eight rows.  Along the selected three-clean seven-row puncture their images
must span the eight-dimensional quotient, and along every six-row puncture of
that clean seven-row state their images must span the seven-dimensional
quotient.

Singleton compatibility on a virtual-canonical complete block is unique.  Thus
there is no state-choice ambiguity: once a global singleton block is chosen,
its singleton state is fixed and descends unchanged whenever the block remains
virtual-canonical complete.  If it ceases to be complete, its replacement
class maps to zero.

The underlying global-lift audit is still an overapproximation in other ways,
but this wrapper removes its explicit freedom to use unrelated compatible
singleton blocks at the eight-, seven-, and six-row levels of the selected
clean fan.  Therefore a zero-survivor full cover remains a rigorous exclusion
of Profile B.
"""

from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_global_lift_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_global_lift", BASE)
L = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(L)

B = L.B
C = L.C
R = L.R
S = L.S
G = L.G
P0 = L.P0
ORIG_GLOBAL_EIGHT_OK = L.global_eight_ok

FIXED_NINE_COUNTS = {
    "eight_old_full_span": 0,
    "nine_block_subsets": 0,
    "nine_structural_fan_candidates": 0,
    "nine_rank9_at_eight": 0,
    "nine_rank8_at_seven": 0,
    "nine_full_six_fan": 0,
    "nine_full_five_fan": 0,
    "fixed_nine_survivors": 0,
}
FIXED_NINE_EXAMPLES = []


def canonical_state(ext, space, rank_cache):
    touched = S.touched_blocks(ext)
    states = G.virtual_canonical(ext, touched, space)
    complete = tuple(
        block for block, state in zip(touched, states) if state == 7
    )
    deficiency = S.deficiency(complete, rank_cache)
    rows = L.generic_relation_rows(ext, touched, states, space)
    canonical = C.canonical_columns(rows)
    base_rank = C.rank_q(canonical)
    complete_rank = C.rank_q([P0.COMPLETE_T[b] for b in complete])
    if base_rank != complete_rank:
        return None
    return complete, deficiency, rows, canonical, base_rank


def fixed_extra_rank(ext, space, state_data, block_states):
    """Exact quotient rank of fixed descended replacement classes over Q."""
    complete, _deficiency, _rows, canonical, base_rank = state_data
    complete_set = set(complete)
    complete_index = {block: i for i, block in enumerate(complete)}
    vectors = []
    for block, state in block_states:
        if block not in complete_set:
            # Puncture functoriality sends this replacement class to zero.
            continue
        options = B.singleton_options(ext, block, space)
        assert len(options) == 1
        assert options[0] == state
        vectors.append(
            B.replacement_functional(
                ext, block, state, space, complete_index, len(complete)
            )
        )
    return C.rank_q(canonical + vectors) - base_rank


def fixed_nine_basis_exists(ext8, space8, rank_cache):
    state8 = canonical_state(ext8, space8, rank_cache)
    if state8 is None:
        return False
    complete8, d8, _rows8, _canonical8, _base8 = state8
    assert d8 == 3

    good8 = []
    for block in complete8:
        options = B.singleton_options(ext8, block, space8)
        if not options:
            continue
        assert len(options) == 1
        good8.append((block, options[0]))
    if len(good8) < 9:
        return False

    # The selected lift was built by appending the eighth row, so deleting the
    # last coordinate recovers the clean seven-row parent.
    ext7 = ext8[:-1]
    space7 = S.project_space(space8, 7)
    if len(space7) != 2:
        return False
    state7 = canonical_state(ext7, space7, rank_cache)
    if state7 is None or state7[1] != 3:
        return False

    six_states = []
    for i in range(7):
        ext6 = ext7[:i] + ext7[i + 1:]
        space6 = S.project_space(space7, i)
        if len(space6) != 2:
            return False
        state6 = canonical_state(ext6, space6, rank_cache)
        if state6 is None or state6[1] != 3:
            return False
        six_states.append((ext6, space6, state6))

    five_state_map = {}
    for ext6, space6, _state6 in six_states:
        for j in range(6):
            ext5 = ext6[:j] + ext6[j + 1:]
            space5 = S.project_space(space6, j)
            if len(space5) != 2:
                return False
            state5 = canonical_state(ext5, space5, rank_cache)
            if state5 is None or state5[1] not in (2, 3):
                return False
            five_state_map[(ext5, space5)] = (ext5, space5, state5)
    five_states = tuple(five_state_map.values())
    assert len(five_states) == 21

    complete7 = set(state7[0])
    complete6_sets = tuple(set(state[2][0]) for state in six_states)
    complete5_data = tuple(
        (set(state[2][0]), 3 + state[2][1]) for state in five_states
    )

    for chosen in combinations(good8, 9):
        FIXED_NINE_COUNTS["nine_block_subsets"] += 1
        blocks = tuple(block for block, _state in chosen)

        # Since the nine classes are independent at eight rows, punctures to
        # dimensions eight, seven, and 5/6 can kill at most one, two, and 4/3
        # basis classes, respectively.  Apply these cheap tests first.
        if sum(block not in complete7 for block in blocks) > 1:
            continue
        if any(
            sum(block not in complete6 for block in blocks) > 2
            for complete6 in complete6_sets
        ):
            continue
        if any(
            sum(block not in complete5 for block in blocks) > 9 - target_dim
            for complete5, target_dim in complete5_data
        ):
            continue
        FIXED_NINE_COUNTS["nine_structural_fan_candidates"] += 1

        if fixed_extra_rank(ext8, space8, state8, chosen) != 9:
            continue
        FIXED_NINE_COUNTS["nine_rank9_at_eight"] += 1

        if fixed_extra_rank(ext7, space7, state7, chosen) != 8:
            continue
        FIXED_NINE_COUNTS["nine_rank8_at_seven"] += 1

        if any(
            fixed_extra_rank(ext6, space6, state6, chosen) != 7
            for ext6, space6, state6 in six_states
        ):
            continue
        FIXED_NINE_COUNTS["nine_full_six_fan"] += 1

        if any(
            fixed_extra_rank(ext5, space5, state5, chosen) != 3 + state5[1]
            for ext5, space5, state5 in five_states
        ):
            continue
        FIXED_NINE_COUNTS["nine_full_five_fan"] += 1

        if len(FIXED_NINE_EXAMPLES) < 20:
            FIXED_NINE_EXAMPLES.append(
                (ext8, space8, tuple((b, s) for b, s in chosen))
            )
        return True

    return False


def global_eight_ok_fixed_nine(ext8, space8, rank_cache):
    if not ORIG_GLOBAL_EIGHT_OK(ext8, space8, rank_cache):
        return False
    FIXED_NINE_COUNTS["eight_old_full_span"] += 1
    if not fixed_nine_basis_exists(ext8, space8, rank_cache):
        return False
    FIXED_NINE_COUNTS["fixed_nine_survivors"] += 1
    return True


L.global_eight_ok = global_eight_ok_fixed_nine


if __name__ == "__main__":
    try:
        L.B.main()
    finally:
        print("global_lift_counts", L.GLOBAL_LIFT_COUNTS)
        print("global_lift_examples", L.GLOBAL_LIFT_EXAMPLES)
        print("fixed_nine_counts", FIXED_NINE_COUNTS)
        print("fixed_nine_examples", FIXED_NINE_EXAMPLES)
