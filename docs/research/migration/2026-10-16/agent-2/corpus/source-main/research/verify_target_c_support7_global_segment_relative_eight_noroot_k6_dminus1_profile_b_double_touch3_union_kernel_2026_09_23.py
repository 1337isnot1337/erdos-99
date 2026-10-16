#!/usr/bin/env python3
"""Double touch-three union-kernel filter for the remaining Profile B.

Every genuine remaining Profile B source has at least two dependency-active
aligned touch-three source singleton blocks. Each witness b with touch triple
T has

    K_T = E_T + <e_b>,

where E_T is the three-dimensional external puncture-kernel span in the fixed
six-dimensional space L.

For two witnesses with triples T,U, put R=T union U. If deleting R preserves
coefficient rank two, puncture functoriality gives

    span(E_R,e_b,e_c) <= K_R.

Writing sigma = dim span(E_R,e_b,e_c)-dim(E_R), the rank-two descendant
quotient formula yields

    d_R <= 3-sigma.

In particular d_R<=2 always, and d_R<=1 when sigma=2. This wrapper enforces
that exact necessary condition and directly checks the deeper kernel
containments. Rank-drop union punctures are recorded but left for a separate
branch.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_touch3_kernel_witness_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_touch3_kernel", BASE)
T = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(T)

M = T.M
K = T.K
R = T.R

ORIG_CHOSEN_PASSES_TOUCH3 = M.chosen_passes_all_clean_fans
DOUBLE_TOUCH3_COUNTS = Counter()
DOUBLE_TOUCH3_EXAMPLES = []


def source_basis_vector(index, width=9):
    return tuple(Fraction(int(i == index)) for i in range(width))


def reconstruct_witnesses(ext8, space8, block_states):
    """Return (L, one-puncture lines, witnesses) or None on inconsistency."""
    fans, by_deleted = K.all_descendant_kernels(ext8, space8, block_states)
    if fans is None:
        return None

    d3_spaces = tuple(
        kernel
        for deficiency, kernel in by_deleted.values()
        if deficiency == 3
    )
    L = K.span_basis(*d3_spaces, width=9)
    if len(L) != 6:
        return None

    one_kernels = {}
    for i in range(8):
        item = by_deleted.get(frozenset((i,)))
        if item is None or item[0] != 3 or len(item[1]) != 1:
            return None
        one_kernels[i] = item[1]

    witnesses = []
    for basis_index, (block, _state) in enumerate(block_states):
        if not T.is_aligned(ext8, block):
            continue
        e_block = source_basis_vector(basis_index)
        if K.is_subspace((e_block,), L, width=9):
            continue

        deleted = T.touch_positions(ext8, block)
        if len(deleted) != 3:
            continue
        deleted_set = frozenset(deleted)
        item = by_deleted.get(deleted_set)
        if item is None:
            continue
        deficiency, kernel = item
        if deficiency != 2 or len(kernel) != 4:
            continue

        external = K.span_basis(
            *(one_kernels[i] for i in deleted),
            width=9,
        )
        if len(external) != 3:
            continue
        expected = K.span_basis(external, (e_block,), width=9)
        if expected != kernel:
            continue

        witnesses.append(
            (basis_index, block, deleted_set, kernel, external, e_block)
        )

    return L, one_kernels, tuple(witnesses)


def double_touch3_union_ok(ext8, space8, rank_cache, block_states):
    data = reconstruct_witnesses(ext8, space8, block_states)
    if data is None:
        DOUBLE_TOUCH3_COUNTS["witness_reconstruction_failed"] += 1
        return False
    L, one_kernels, witnesses = data

    if len(witnesses) < 2:
        DOUBLE_TOUCH3_COUNTS[("too_few_witnesses", len(witnesses))] += 1
        return False

    DOUBLE_TOUCH3_COUNTS[("witness_count", len(witnesses))] += 1

    rank_preserving_pairs = 0
    rank_drop_pairs = 0
    pair_records = []

    for wa, wb in combinations(witnesses, 2):
        ia, ba, Ta, Ka, _Ea, ea = wa
        ib, bb, Tb, Kb, _Eb, eb = wb

        if Ta == Tb or len(Ta & Tb) > 1:
            DOUBLE_TOUCH3_COUNTS["bad_touch_triple_intersection"] += 1
            return False

        union = frozenset(Ta | Tb)
        if len(union) not in (5, 6):
            DOUBLE_TOUCH3_COUNTS[("bad_union_size", len(union))] += 1
            return False

        ext_u, space_u = M.delete_source_positions(
            ext8, space8, tuple(sorted(union))
        )
        if len(space_u) != 2:
            rank_drop_pairs += 1
            DOUBLE_TOUCH3_COUNTS[("union_rank_drop", len(union), len(space_u))] += 1
            pair_records.append((ia, ib, tuple(sorted(union)), "rank_drop", len(space_u)))
            continue

        rank_preserving_pairs += 1
        state_u = M.F.canonical_state(ext_u, space_u, rank_cache)
        if state_u is None:
            DOUBLE_TOUCH3_COUNTS["union_canonical_state_failed"] += 1
            return False

        deficiency_u = state_u[1]
        item_u = K.quotient_kernel(
            state_u, ext_u, space_u, block_states
        )
        if item_u is None:
            DOUBLE_TOUCH3_COUNTS["union_quotient_kernel_failed"] += 1
            return False
        kernel_u, image_rank_u = item_u

        target_rank_u = (len(ext_u) - 2) + deficiency_u
        if image_rank_u != target_rank_u:
            DOUBLE_TOUCH3_COUNTS[(
                "union_wrong_image_rank", image_rank_u, target_rank_u
            )] += 1
            return False

        if not K.is_subspace(Ka, kernel_u, width=9):
            DOUBLE_TOUCH3_COUNTS["union_missing_first_witness_kernel"] += 1
            return False
        if not K.is_subspace(Kb, kernel_u, width=9):
            DOUBLE_TOUCH3_COUNTS["union_missing_second_witness_kernel"] += 1
            return False

        external_u = K.span_basis(
            *(one_kernels[i] for i in sorted(union)),
            width=9,
        )
        if len(external_u) != len(union):
            DOUBLE_TOUCH3_COUNTS[(
                "union_external_rank_mismatch", len(union), len(external_u)
            )] += 1
            return False
        if not K.is_subspace(external_u, L, width=9):
            DOUBLE_TOUCH3_COUNTS["union_external_not_in_L"] += 1
            return False

        forced = K.span_basis(external_u, (ea,), (eb,), width=9)
        sigma = len(forced) - len(external_u)
        if sigma not in (1, 2):
            DOUBLE_TOUCH3_COUNTS[("bad_internal_increment", sigma)] += 1
            return False
        if not K.is_subspace(forced, kernel_u, width=9):
            DOUBLE_TOUCH3_COUNTS["union_kernel_missing_forced_span"] += 1
            return False

        bound = 3 - sigma
        if deficiency_u > bound:
            DOUBLE_TOUCH3_COUNTS[(
                "union_deficiency_bound_fail", sigma, deficiency_u
            )] += 1
            return False

        rho = len(K.span_basis(L, (ea,), (eb,), width=9)) - len(L)
        if rho not in (1, 2) or rho > sigma:
            DOUBLE_TOUCH3_COUNTS[("bad_quotient_increment", rho, sigma)] += 1
            return False
        if rho == 2 and deficiency_u > 1:
            DOUBLE_TOUCH3_COUNTS[(
                "independent_mod_L_wrong_deficiency", deficiency_u
            )] += 1
            return False

        DOUBLE_TOUCH3_COUNTS[(
            "rank_preserving_union", len(union), sigma, rho, deficiency_u
        )] += 1
        pair_records.append((
            ia,
            ib,
            tuple(sorted(union)),
            "rank_two",
            sigma,
            rho,
            deficiency_u,
            len(kernel_u),
            ba,
            bb,
        ))

    DOUBLE_TOUCH3_COUNTS[("rank_preserving_pair_count", rank_preserving_pairs)] += 1
    DOUBLE_TOUCH3_COUNTS[("rank_drop_pair_count", rank_drop_pairs)] += 1
    DOUBLE_TOUCH3_COUNTS["double_touch3_union_pass"] += 1

    if len(DOUBLE_TOUCH3_EXAMPLES) < 20:
        DOUBLE_TOUCH3_EXAMPLES.append((
            tuple(ext8),
            space8,
            tuple(block_states),
            tuple(pair_records),
        ))
    return True


def chosen_passes_double_touch3_union(ext8, space8, rank_cache, block_states):
    if not ORIG_CHOSEN_PASSES_TOUCH3(
        ext8, space8, rank_cache, block_states
    ):
        return False
    return double_touch3_union_ok(ext8, space8, rank_cache, block_states)


M.chosen_passes_all_clean_fans = chosen_passes_double_touch3_union


# Abstract dimension sanity checks for the theorem.
_E9 = tuple(source_basis_vector(i) for i in range(9))
_LTEST = K.span_basis(*_E9[:6], width=9)
_ERTEST = K.span_basis(*_E9[:5], width=9)
_FORCED2 = K.span_basis(_ERTEST, (_E9[6],), (_E9[7],), width=9)
assert len(_LTEST) == 6
assert len(_ERTEST) == 5
assert len(_FORCED2) - len(_ERTEST) == 2
assert 3 - (len(_FORCED2) - len(_ERTEST)) == 1


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
        print("double_touch3_union_counts", DOUBLE_TOUCH3_COUNTS)
        print("double_touch3_union_examples", DOUBLE_TOUCH3_EXAMPLES)
