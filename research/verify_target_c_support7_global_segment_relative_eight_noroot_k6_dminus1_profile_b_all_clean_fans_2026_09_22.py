#!/usr/bin/env python3
"""All-three-clean-fans wrapper for the remaining eight-no-root k=6 Profile B.

A genuine Profile B source has a rank-two coefficient plane P_8 with at least
two three-clean coordinates.  The existing actual-state verifier follows one
selected three-clean deletion.  This wrapper requires the same fixed global
nine-singleton basis to satisfy the proved d=3/full-functional-rank puncture
conditions through every three-clean coordinate of the reconstructed source.

The added test is a necessary condition only.  It cannot exclude a genuine
Profile B state: the sharpening theorem applies to every three-clean source
coordinate, and puncture functoriality uses the same nine actual singleton
replacement classes in every clean fan.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_actual_state_realization_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_actual_state", BASE)
A = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(A)

F = A.F
B = A.B
C = A.C
S = A.S

ORIG_ACTUAL_FIXED_EXTRA_RANK = F.fixed_extra_rank

ALL_CLEAN_COUNTS = Counter()
ALL_CLEAN_EXAMPLES = []
FAN_CACHE = {}


def delete_source_positions(ext, space, positions):
    """Delete original coordinate positions, preserving their original labels."""
    ext_now = tuple(ext)
    space_now = space
    for pos in sorted(positions, reverse=True):
        space_now = S.project_space(space_now, pos)
        ext_now = ext_now[:pos] + ext_now[pos + 1:]
    return ext_now, space_now


def three_clean_positions(ext8, space8):
    """Coordinates whose every containing puncture of size <=3 keeps rank two."""
    assert len(ext8) == 8 and len(space8) == 2
    out = []
    positions = tuple(range(8))
    for i in positions:
        if len(delete_source_positions(ext8, space8, (i,))[1]) != 2:
            continue
        good = True
        others = tuple(j for j in positions if j != i)
        for j in others:
            if len(delete_source_positions(ext8, space8, (i, j))[1]) != 2:
                good = False
                break
        if not good:
            continue
        for j, k in combinations(others, 2):
            if len(delete_source_positions(ext8, space8, (i, j, k))[1]) != 2:
                good = False
                break
        if good:
            out.append(i)
    return tuple(out)


def clean_fan_data(ext8, space8, rank_cache):
    """Canonical state data for every source three-clean puncture fan."""
    key = (tuple(ext8), space8)
    cached = FAN_CACHE.get(key)
    if cached is not None:
        return cached

    clean = three_clean_positions(ext8, space8)
    ALL_CLEAN_COUNTS[("source_three_clean_count", len(clean))] += 1
    if len(clean) < 2:
        # The rank-two projective-column theorem guarantees at least two for a
        # genuine source, so this is a safe rejection of an overapproximation.
        FAN_CACHE[key] = ()
        return ()

    fans = []
    for source_i in clean:
        ext7, space7 = delete_source_positions(ext8, space8, (source_i,))
        if len(space7) != 2:
            FAN_CACHE[key] = ()
            return ()
        state7 = F.canonical_state(ext7, space7, rank_cache)
        if state7 is None or state7[1] != 3:
            FAN_CACHE[key] = ()
            return ()

        six_states = []
        five_state_map = {}
        for j in range(7):
            ext6 = ext7[:j] + ext7[j + 1:]
            space6 = S.project_space(space7, j)
            if len(space6) != 2:
                FAN_CACHE[key] = ()
                return ()
            state6 = F.canonical_state(ext6, space6, rank_cache)
            if state6 is None or state6[1] != 3:
                FAN_CACHE[key] = ()
                return ()
            six_states.append((ext6, space6, state6))

            for k in range(6):
                ext5 = ext6[:k] + ext6[k + 1:]
                space5 = S.project_space(space6, k)
                if len(space5) != 2:
                    FAN_CACHE[key] = ()
                    return ()
                state5 = F.canonical_state(ext5, space5, rank_cache)
                if state5 is None or state5[1] not in (2, 3):
                    FAN_CACHE[key] = ()
                    return ()
                five_state_map[(ext5, space5)] = (ext5, space5, state5)

        five_states = tuple(five_state_map.values())
        assert len(six_states) == 7
        assert len(five_states) == 21
        fans.append((source_i, ext7, space7, state7, tuple(six_states), five_states))

    result = tuple(fans)
    FAN_CACHE[key] = result
    return result


def safe_fixed_extra_rank(ext, space, state_data, block_states):
    """Exact fixed-block quotient rank, rejecting state mismatches safely."""
    complete, _deficiency, _rows, canonical, base_rank = state_data
    complete_set = set(complete)
    complete_index = {block: i for i, block in enumerate(complete)}
    vectors = []
    for block, state in block_states:
        if block not in complete_set:
            continue
        options = B.singleton_options(ext, block, space)
        if len(options) != 1 or options[0] != state:
            return -1
        vectors.append(
            B.replacement_functional(
                ext, block, state, space, complete_index, len(complete)
            )
        )
    return C.rank_q(canonical + vectors) - base_rank


def zero_source_basis_blocks(ext, space, state_data, block_states):
    """Chosen source-basis classes mapping to zero in this descendant quotient."""
    zeros = []
    for block_state in block_states:
        rank = safe_fixed_extra_rank(ext, space, state_data, (block_state,))
        if rank < 0:
            return None
        assert rank in (0, 1)
        if rank == 0:
            zeros.append(block_state[0])
    return tuple(zeros)


def six_kernel_incidence_ok(ext7, space7, state7, six_states, block_states):
    """Exact zero-class incidence forced by seven distinct six-row kernels."""
    z7 = zero_source_basis_blocks(ext7, space7, state7, block_states)
    if z7 is None or len(z7) > 1:
        ALL_CLEAN_COUNTS["kernel_incidence_bad_z7"] += 1
        return False, ()

    z6s = []
    for ext6, space6, state6 in six_states:
        z6 = zero_source_basis_blocks(ext6, space6, state6, block_states)
        if z6 is None or len(z6) > 2:
            ALL_CLEAN_COUNTS["kernel_incidence_bad_z6"] += 1
            return False, ()
        z6s.append(z6)

    if not z7:
        # K0 is not a coordinate basis line.  Two distinct coordinate
        # two-planes cannot both contain that same non-coordinate line.
        if sum(len(z6) == 2 for z6 in z6s) > 1:
            ALL_CLEAN_COUNTS["kernel_incidence_two_double_zero_children"] += 1
            return False, ()
    else:
        common = z7[0]
        second_seen = set()
        for z6 in z6s:
            if common not in z6:
                ALL_CLEAN_COUNTS["kernel_incidence_lost_common_zero"] += 1
                return False, ()
            second = tuple(block for block in z6 if block != common)
            if len(second) > 1:
                ALL_CLEAN_COUNTS["kernel_incidence_too_many_second_zeros"] += 1
                return False, ()
            if second:
                if second[0] in second_seen:
                    ALL_CLEAN_COUNTS["kernel_incidence_repeated_second_zero"] += 1
                    return False, ()
                second_seen.add(second[0])

    ALL_CLEAN_COUNTS[("kernel_incidence_pass_z7_size", len(z7))] += 1
    return True, z7


def chosen_passes_all_clean_fans(ext8, space8, rank_cache, block_states):
    fans = clean_fan_data(ext8, space8, rank_cache)
    if len(fans) < 2:
        return False

    blocks = tuple(block for block, _state in block_states)

    # Distinct three-clean source punctures have distinct one-dimensional
    # quotient kernels.  Hence the same nonzero source basis class cannot map
    # to zero in two different clean seven-row shadows.  This uses exact
    # individual descendant quotient ranks, not merely block disappearance.
    clean_zero_seen = set()
    for source_i, ext7, space7, state7, six_states, _five_states in fans:
        incidence_ok, z7 = six_kernel_incidence_ok(
            ext7, space7, state7, six_states, block_states
        )
        if not incidence_ok:
            return False
        if z7:
            if z7[0] in clean_zero_seen:
                ALL_CLEAN_COUNTS["clean_fan_repeat_zero7_basis_class"] += 1
                return False
            clean_zero_seen.add(z7[0])

    for source_i, ext7, space7, state7, six_states, five_states in fans:
        # Cheap disappearance bounds implied by a nine-element source basis.
        for _ext6, _space6, state6 in six_states:
            complete6 = set(state6[0])
            if sum(block not in complete6 for block in blocks) > 2:
                ALL_CLEAN_COUNTS["clean_fan_fail_complete6"] += 1
                return False

        for _ext5, _space5, state5 in five_states:
            target = 3 + state5[1]
            complete5 = set(state5[0])
            if sum(block not in complete5 for block in blocks) > 9 - target:
                ALL_CLEAN_COUNTS["clean_fan_fail_complete5"] += 1
                return False

        # Exact rational functional ranks of the same nine source classes.
        if safe_fixed_extra_rank(ext7, space7, state7, block_states) != 8:
            ALL_CLEAN_COUNTS["clean_fan_fail_rank7"] += 1
            return False
        if any(
            safe_fixed_extra_rank(ext6, space6, state6, block_states) != 7
            for ext6, space6, state6 in six_states
        ):
            ALL_CLEAN_COUNTS["clean_fan_fail_rank6"] += 1
            return False
        if any(
            safe_fixed_extra_rank(ext5, space5, state5, block_states)
            != 3 + state5[1]
            for ext5, space5, state5 in five_states
        ):
            ALL_CLEAN_COUNTS["clean_fan_fail_rank5"] += 1
            return False

        ALL_CLEAN_COUNTS[("clean_fan_pass", source_i)] += 1

    ALL_CLEAN_COUNTS["chosen_nine_all_clean_fans"] += 1
    if len(ALL_CLEAN_EXAMPLES) < 20:
        ALL_CLEAN_EXAMPLES.append((tuple(ext8), space8, tuple(block_states)))
    return True


def fixed_extra_rank_all_clean(ext, space, state_data, block_states):
    if len(ext) == 8 and len(block_states) == 9:
        # Do not spend on all clean fans unless the chosen source classes are
        # already a rank-nine basis in the canonical source quotient.
        if safe_fixed_extra_rank(ext, space, state_data, block_states) != 9:
            return -1
        if not chosen_passes_all_clean_fans(
            ext, space, {}, block_states
        ):
            return -1
    return ORIG_ACTUAL_FIXED_EXTRA_RANK(ext, space, state_data, block_states)


# The fixed-nine source routine resolves this module global at call time.
F.fixed_extra_rank = fixed_extra_rank_all_clean


if __name__ == "__main__":
    try:
        F.L.B.main()
    finally:
        print("global_lift_counts", F.L.GLOBAL_LIFT_COUNTS)
        print("fixed_nine_counts", F.FIXED_NINE_COUNTS)
        print("actual_realization_counts", A.ACTUAL_COUNTS)
        print("all_clean_counts", ALL_CLEAN_COUNTS)
        print("all_clean_examples", ALL_CLEAN_EXAMPLES)
