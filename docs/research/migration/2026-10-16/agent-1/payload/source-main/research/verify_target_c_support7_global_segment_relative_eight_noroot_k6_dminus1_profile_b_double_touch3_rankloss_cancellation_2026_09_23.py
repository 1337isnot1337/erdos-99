#!/usr/bin/env python3
"""Rank-loss-robust double touch-three union-kernel filter.

The preceding double-touch-three filter proved

    d_R <= 3-sigma_R

for a witness-pair union R only when deleting R preserved coefficient rank two.
The rank-uniform functional quotient formula and the labeled one-puncture
relation-plane theorem show that coefficient-rank loss cancels exactly:

    k_R = 2-rank(P_R),
    dim(E_R) = |R|-k_R,
    dim(V_R) = (8-|R|)-(2-k_R)+d_R,

so the same inequality holds for rank-one and rank-zero union descendants.
This wrapper enforces that stronger necessary condition without skipping
rank-drop unions.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_double_touch3_union_kernel_2026_09_23.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_double_touch3", BASE)
D = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(D)

M = D.M
K = D.K
T = D.T

ORIG_CHOSEN_PASSES_DOUBLE = M.chosen_passes_all_clean_fans
RANKLOSS_COUNTS = Counter()
RANKLOSS_EXAMPLES = []


def quotient_kernel_fixed_states(state_data, ext, space, block_states):
    """Exact Q^9 -> descendant quotient kernel using the fixed source states.

    Unlike K.quotient_kernel, this permits a lower-rank descendant to have
    multiple compatible singleton states on a surviving source block. The
    actual source state is followed functorially; it only needs to remain one
    of the compatible options.
    """
    complete, _deficiency, _rows, canonical, _base_rank = state_data
    complete_set = set(complete)
    complete_index = {block: i for i, block in enumerate(complete)}
    width = len(canonical[0]) if canonical else len(complete) + len(ext) - len(space)

    canonical_basis = K.E.rref(canonical, width)
    images = []
    for block, state in block_states:
        if block not in complete_set:
            images.append((Fraction(0),) * width)
            continue
        options = M.B.singleton_options(ext, block, space)
        if state not in options:
            return None
        vector = M.B.replacement_functional(
            ext,
            block,
            state,
            space,
            complete_index,
            len(complete),
        )
        images.append(K.reduce_mod_rref(vector, canonical_basis))

    if len(images) != 9:
        return None

    image_rank = len(K.E.rref(images, width))
    equations = tuple(
        tuple(images[i][j] for i in range(9))
        for j in range(width)
    )
    kernel = K.E.rref(K.E.nullspace(equations, 9), 9)
    if len(kernel) != 9 - image_rank:
        return None
    return kernel, image_rank


def rankloss_cancellation_ok(ext8, space8, rank_cache, block_states):
    data = D.reconstruct_witnesses(ext8, space8, block_states)
    if data is None:
        RANKLOSS_COUNTS["witness_reconstruction_failed"] += 1
        return False
    L, one_kernels, witnesses = data

    if len(witnesses) < 2:
        RANKLOSS_COUNTS[("too_few_witnesses", len(witnesses))] += 1
        return False

    pair_records = []
    for wa, wb in combinations(witnesses, 2):
        ia, ba, Ta, Ka, _Ea, ea = wa
        ib, bb, Tb, Kb, _Eb, eb = wb

        if Ta == Tb or len(Ta & Tb) > 1:
            RANKLOSS_COUNTS["bad_touch_triple_intersection"] += 1
            return False

        union = frozenset(Ta | Tb)
        if len(union) not in (5, 6):
            RANKLOSS_COUNTS[("bad_union_size", len(union))] += 1
            return False

        ext_u, space_u = M.delete_source_positions(
            ext8, space8, tuple(sorted(union))
        )
        rank_u = len(space_u)
        if rank_u not in (0, 1, 2):
            RANKLOSS_COUNTS[("bad_union_coefficient_rank", rank_u)] += 1
            return False
        rank_loss = 2 - rank_u

        state_u = M.F.canonical_state(ext_u, space_u, rank_cache)
        if state_u is None:
            RANKLOSS_COUNTS[("union_canonical_state_failed", rank_u)] += 1
            return False
        deficiency_u = state_u[1]

        item_u = quotient_kernel_fixed_states(
            state_u, ext_u, space_u, block_states
        )
        if item_u is None:
            RANKLOSS_COUNTS[("union_quotient_kernel_failed", rank_u)] += 1
            return False
        kernel_u, image_rank_u = item_u

        target_rank_u = (len(ext_u) - rank_u) + deficiency_u
        if image_rank_u != target_rank_u:
            RANKLOSS_COUNTS[(
                "union_wrong_image_rank",
                rank_u,
                image_rank_u,
                target_rank_u,
            )] += 1
            return False
        if len(kernel_u) != 9 - target_rank_u:
            RANKLOSS_COUNTS[(
                "union_wrong_kernel_dimension",
                rank_u,
                len(kernel_u),
                9 - target_rank_u,
            )] += 1
            return False

        if not K.is_subspace(Ka, kernel_u, width=9):
            RANKLOSS_COUNTS[("union_missing_first_witness_kernel", rank_u)] += 1
            return False
        if not K.is_subspace(Kb, kernel_u, width=9):
            RANKLOSS_COUNTS[("union_missing_second_witness_kernel", rank_u)] += 1
            return False

        external_u = K.span_basis(
            *(one_kernels[i] for i in sorted(union)),
            width=9,
        )
        expected_external_dim = len(union) - rank_loss
        if len(external_u) != expected_external_dim:
            RANKLOSS_COUNTS[(
                "union_external_rank_mismatch",
                len(union),
                rank_loss,
                len(external_u),
                expected_external_dim,
            )] += 1
            return False
        if not K.is_subspace(external_u, L, width=9):
            RANKLOSS_COUNTS["union_external_not_in_L"] += 1
            return False

        forced = K.span_basis(external_u, (ea,), (eb,), width=9)
        sigma = len(forced) - len(external_u)
        if sigma not in (1, 2):
            RANKLOSS_COUNTS[("bad_internal_increment", rank_u, sigma)] += 1
            return False
        if not K.is_subspace(forced, kernel_u, width=9):
            RANKLOSS_COUNTS[("union_kernel_missing_forced_span", rank_u)] += 1
            return False

        bound = 3 - sigma
        if deficiency_u > bound:
            RANKLOSS_COUNTS[(
                "union_deficiency_bound_fail",
                rank_u,
                sigma,
                deficiency_u,
            )] += 1
            return False

        rho = len(K.span_basis(L, (ea,), (eb,), width=9)) - len(L)
        if rho not in (1, 2) or rho > sigma:
            RANKLOSS_COUNTS[("bad_quotient_increment", rank_u, rho, sigma)] += 1
            return False
        if rho == 2 and deficiency_u > 1:
            RANKLOSS_COUNTS[(
                "independent_mod_L_wrong_deficiency",
                rank_u,
                deficiency_u,
            )] += 1
            return False

        RANKLOSS_COUNTS[(
            "union",
            len(union),
            rank_u,
            rank_loss,
            sigma,
            rho,
            deficiency_u,
        )] += 1
        pair_records.append((
            ia,
            ib,
            tuple(sorted(union)),
            rank_u,
            rank_loss,
            sigma,
            rho,
            deficiency_u,
            len(external_u),
            len(kernel_u),
            ba,
            bb,
        ))

    RANKLOSS_COUNTS["rankloss_cancellation_pass"] += 1
    if len(RANKLOSS_EXAMPLES) < 20:
        RANKLOSS_EXAMPLES.append((
            tuple(ext8),
            space8,
            tuple(block_states),
            tuple(pair_records),
        ))
    return True


def chosen_passes_rankloss_cancellation(ext8, space8, rank_cache, block_states):
    if not ORIG_CHOSEN_PASSES_DOUBLE(
        ext8, space8, rank_cache, block_states
    ):
        return False
    return rankloss_cancellation_ok(
        ext8, space8, rank_cache, block_states
    )


M.chosen_passes_all_clean_fans = chosen_passes_rankloss_cancellation


# Abstract dimension checks: the rank-loss term cancels from both sides.
for union_size in (5, 6):
    for rank_loss in (0, 1, 2):
        rank_u = 2 - rank_loss
        if rank_u < 0:
            continue
        ext_dim = union_size - rank_loss
        t = 8 - union_size
        for sigma in (1, 2):
            for deficiency in range(0, 4):
                quotient_dim = t - rank_u + deficiency
                kernel_dim = 9 - quotient_dim
                forced_dim = ext_dim + sigma
                assert (kernel_dim >= forced_dim) == (deficiency <= 3 - sigma)


if __name__ == "__main__":
    try:
        M.F.L.B.main()
    finally:
        print("global_lift_counts", M.F.L.GLOBAL_LIFT_COUNTS)
        print("fixed_nine_counts", M.F.FIXED_NINE_COUNTS)
        print("actual_realization_counts", M.A.ACTUAL_COUNTS)
        print("all_clean_counts", M.ALL_CLEAN_COUNTS)
        print("kernel_lattice_counts", K.KERNEL_LATTICE_COUNTS)
        print("touch3_kernel_counts", T.TOUCH3_KERNEL_COUNTS)
        print("double_touch3_union_counts", D.DOUBLE_TOUCH3_COUNTS)
        print("rankloss_cancellation_counts", RANKLOSS_COUNTS)
        print("rankloss_cancellation_examples", RANKLOSS_EXAMPLES)
