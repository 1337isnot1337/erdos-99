#!/usr/bin/env python3
"""External-kernel geometry filter for the remaining eight-no-root k=6 Profile B.

This wrapper sits on top of the all-three-clean-fans actual-state audit.  It
uses the fact that every rank-preserving puncture whose virtual deficiency
stays equal to the source value d=3 has its source quotient kernel inside one
fixed six-dimensional external subspace.

For the fixed nine source singleton classes, record every class that maps to
zero in a d=3 descendant from the clean depth-three fan.  A class that is zero
in several descendants must lie in the intersection of the corresponding
coordinate-kernel subspaces.  Since the nine source classes are independent,
the allowed intersection subspaces for all constrained labels must satisfy the
linear Hall/Rado inequalities.  Failure is a rigorous rejection.

The filter is necessary only.  It does not identify a source class with an
arbitrary vector in its allowed subspace; the existing exact same-nine-set
functional and actual-state checks remain authoritative after this prefilter.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_b_low_weight_filtered_all_clean_fans_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_low_weight_all_clean", BASE)
LW = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(LW)
M = LW.G

ORIG_CHOSEN_PASSES_ALL_CLEAN_FANS = M.chosen_passes_all_clean_fans
EXTERNAL_KERNEL_COUNTS = Counter()
EXTERNAL_KERNEL_EXAMPLES = []


def rref(rows, width=6):
    basis = {}
    for row in rows:
        r = [Fraction(x) for x in row]
        assert len(r) == width
        for pivot in sorted(basis):
            if r[pivot]:
                q = r[pivot]
                br = basis[pivot]
                r = [x - q * y for x, y in zip(r, br)]
        pivot = next((i for i, x in enumerate(r) if x), None)
        if pivot is None:
            continue
        q = r[pivot]
        r = [x / q for x in r]
        for old_pivot in list(basis):
            if basis[old_pivot][pivot]:
                q0 = basis[old_pivot][pivot]
                basis[old_pivot] = [
                    x - q0 * y for x, y in zip(basis[old_pivot], r)
                ]
        basis[pivot] = r
    return tuple(tuple(basis[p]) for p in sorted(basis))


def nullspace(rows, width=6):
    rr = rref(rows, width)
    pivots = []
    for row in rr:
        pivots.append(next(i for i, x in enumerate(row) if x))
    free = [i for i in range(width) if i not in pivots]
    out = []
    for f in free:
        v = [Fraction(0)] * width
        v[f] = Fraction(1)
        for row, pivot in zip(rr, pivots):
            v[pivot] = -row[f]
        out.append(tuple(v))
    return tuple(out)


def intersection_basis(a, b, width=6):
    """Exact basis for rowspace(a) intersect rowspace(b)."""
    return rref(nullspace(a, width) + nullspace(b, width), width)


def deleted_positions(source_ext, child_ext):
    """Original source-coordinate positions absent from an ordered puncture."""
    assert len(set(source_ext)) == len(source_ext)
    child = set(child_ext)
    deleted = frozenset(i for i, e in enumerate(source_ext) if e not in child)
    assert len(deleted) == len(source_ext) - len(child_ext)
    return deleted


def same_deficiency_zero_data(ext8, space8, block_states):
    """Return d=3 descendant zero sets keyed by source deletion coordinates."""
    fans = M.clean_fan_data(ext8, space8, {})
    if len(fans) < 2:
        return None

    by_deleted = {}

    def add_state(ext, space, state_data):
        if state_data[1] != 3:
            return True
        deleted = deleted_positions(ext8, ext)
        assert 1 <= len(deleted) <= 3
        zeros = M.zero_source_basis_blocks(ext, space, state_data, block_states)
        if zeros is None:
            EXTERNAL_KERNEL_COUNTS["state_mismatch"] += 1
            return False
        zero_set = frozenset(zeros)
        previous = by_deleted.get(deleted)
        if previous is not None and previous != zero_set:
            # The same puncture reached through two clean fans must induce the
            # same quotient map on the fixed source classes.
            EXTERNAL_KERNEL_COUNTS["duplicate_puncture_zero_mismatch"] += 1
            return False
        by_deleted[deleted] = zero_set
        return True

    for _source_i, ext7, space7, state7, six_states, five_states in fans:
        if not add_state(ext7, space7, state7):
            return None
        for ext6, space6, state6 in six_states:
            if not add_state(ext6, space6, state6):
                return None
        for ext5, space5, state5 in five_states:
            if state5[1] == 3 and not add_state(ext5, space5, state5):
                return None

    return by_deleted


def external_kernel_geometry_ok(ext8, space8, block_states):
    """Check exact necessary source-kernel incidence for all d=3 descendants.

    Let K be the source canonical dependency space and W the three-dimensional
    pure complete-block dependency kernel of K -> N, where N=null(P_8) has
    dimension six.  For every clean descendant obtained by deleting S, if the
    coefficient rank stays two and the virtual deficiency stays three, its
    dependency space is exactly the inverse image of N_S under K -> N.  Hence
    the source quotient kernel is span{ell_i : i in S} inside the fixed
    six-dimensional space W^perp, with ell_i the i-th coordinate functional on
    N.

    A fixed source basis class that vanishes in several descendants must lie in
    the intersection of those coordinate spans.  Distinct source basis classes
    are independent, so their allowed intersection spaces obey the linear
    Hall/Rado dimension inequalities.
    """
    by_deleted = same_deficiency_zero_data(ext8, space8, block_states)
    if by_deleted is None:
        return False

    R = M.A.R
    null_basis = R.nullspace_int(space8, 8)
    if len(null_basis) != 6:
        EXTERNAL_KERNEL_COUNTS["bad_source_nullity"] += 1
        return False

    # Coordinates of ell_i=e_i^*|_N in the dual basis induced by null_basis.
    ell = tuple(
        tuple(Fraction(alpha[i]) for alpha in null_basis)
        for i in range(8)
    )

    kernel_by_deleted = {}
    zero_occurrences = {}
    all_zero_labels = set()

    for deleted, zeros in by_deleted.items():
        kernel = rref((ell[i] for i in sorted(deleted)), 6)
        if len(kernel) != len(deleted):
            # Every state collected here is a rank-two puncture, so its deleted
            # coordinate functionals on N must be independent.
            EXTERNAL_KERNEL_COUNTS["bad_coordinate_kernel_dimension"] += 1
            return False
        kernel_by_deleted[deleted] = kernel
        all_zero_labels.update(zeros)
        for block in zeros:
            zero_occurrences.setdefault(block, []).append(deleted)

    # All d=3 puncture kernels lie in W^perp, dim 6.  Since the source classes
    # are a basis, at most six basis classes can vanish anywhere in this fan.
    if len(all_zero_labels) > 6:
        EXTERNAL_KERNEL_COUNTS["more_than_six_external_zero_labels"] += 1
        return False

    allowed = {}
    for block, occurrences in zero_occurrences.items():
        current = kernel_by_deleted[occurrences[0]]
        for deleted in occurrences[1:]:
            current = intersection_basis(current, kernel_by_deleted[deleted], 6)
            if not current:
                EXTERNAL_KERNEL_COUNTS["zero_label_empty_kernel_intersection"] += 1
                return False
        allowed[block] = current

    labels = tuple(sorted(allowed))

    # Rado's necessary inequalities for independent representatives x_b in J_b:
    # for every A, dim(sum_{b in A} J_b) >= |A|.  There are at most six labels
    # after the fixed-external-subspace bound, so exhaustive subset checking is
    # tiny.
    for size in range(1, len(labels) + 1):
        for subset in combinations(labels, size):
            span = rref(
                tuple(
                    row
                    for block in subset
                    for row in allowed[block]
                ),
                6,
            )
            if len(span) < size:
                EXTERNAL_KERNEL_COUNTS[("rado_failure_size", size)] += 1
                return False

    # A direct pairwise consequence is worth checking separately as an
    # implementation invariant.  Whenever the union puncture still has rank
    # two, common zero source classes can occupy only the coordinate span of
    # the common deleted positions.
    items = tuple(by_deleted.items())
    for (deleted_a, zeros_a), (deleted_b, zeros_b) in combinations(items, 2):
        union = deleted_a | deleted_b
        if len(union) > 6:
            continue
        _ext_u, space_u = M.delete_source_positions(ext8, space8, tuple(union))
        if len(space_u) != 2:
            continue
        shared = zeros_a & zeros_b
        if len(shared) > len(deleted_a & deleted_b):
            EXTERNAL_KERNEL_COUNTS["pairwise_kernel_intersection_failure"] += 1
            return False

    EXTERNAL_KERNEL_COUNTS[("constrained_zero_labels", len(labels))] += 1
    EXTERNAL_KERNEL_COUNTS["external_kernel_geometry_pass"] += 1
    if len(EXTERNAL_KERNEL_EXAMPLES) < 20:
        EXTERNAL_KERNEL_EXAMPLES.append(
            (
                tuple(ext8),
                space8,
                tuple(block_states),
                tuple((tuple(sorted(s)), tuple(sorted(z))) for s, z in sorted(
                    by_deleted.items(), key=lambda item: (len(item[0]), tuple(sorted(item[0])))
                )),
            )
        )
    return True


def chosen_passes_external_kernel_geometry(ext8, space8, rank_cache, block_states):
    if not external_kernel_geometry_ok(ext8, space8, block_states):
        return False
    return ORIG_CHOSEN_PASSES_ALL_CLEAN_FANS(ext8, space8, rank_cache, block_states)


# M.fixed_extra_rank_all_clean resolves this module-global function at call time.
M.chosen_passes_all_clean_fans = chosen_passes_external_kernel_geometry


# Pure exact-linear-algebra sanity checks independent of repository data.
_E = tuple(
    tuple(Fraction(int(i == j)) for j in range(6))
    for i in range(6)
)
assert len(intersection_basis((_E[0], _E[1]), (_E[1], _E[2]), 6)) == 1
assert not intersection_basis((_E[0],), (_E[1],), 6)
assert len(rref((_E[0], _E[1], _E[0]), 6)) == 2


if __name__ == "__main__":
    try:
        M.F.L.B.main()
    finally:
        print("global_lift_counts", M.F.L.GLOBAL_LIFT_COUNTS)
        print("fixed_nine_counts", M.F.FIXED_NINE_COUNTS)
        print("actual_realization_counts", M.A.ACTUAL_COUNTS)
        print("all_clean_counts", M.ALL_CLEAN_COUNTS)
        print("low_weight_counts", LW.LOW_WEIGHT_COUNTS)
        print("external_kernel_counts", EXTERNAL_KERNEL_COUNTS)
        print("external_kernel_examples", EXTERNAL_KERNEL_EXAMPLES)
