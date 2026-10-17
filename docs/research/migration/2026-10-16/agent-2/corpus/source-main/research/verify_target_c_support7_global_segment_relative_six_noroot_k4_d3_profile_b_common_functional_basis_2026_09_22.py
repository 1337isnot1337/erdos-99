#!/usr/bin/env python3
"""Strengthened exact necessary-condition audit for eight-no-root k=6 Profile B.

This wrapper imports the coverage-correct Profile B audit and replaces its
block-only common-basis filter by an exact rational functional-basis test.
For a genuine six-row Profile B state, seven actual singleton replacement
classes form a basis of the seven-dimensional replacement quotient.  The same
basis must map onto every one-coordinate puncture quotient.  Singleton
compatibility on a virtual-canonical complete block is unique, so each block
has at most one functional class to test.

The wrapper keeps the parent/extension cover and all other filters of the base
audit unchanged.  Its additional rank decisions are over Q using Fraction, not
modular arithmetic, so no extra finite-field exactness certificate is needed.
"""

from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_six_noroot_k4_d3_profile_b_singleton_functional_2026_09_22.py"
spec = importlib.util.spec_from_file_location("e99_profile_b_base", BASE)
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(B)

ORIG_COMPATIBLE_BLOCKS = B.A.compatible_singleton_blocks
ORIG_COMMON_BASIS = B.common_basis_block_sets
CURRENT_SIX = None


def rank_q(rows):
    """Exact row rank over Q for the small functional matrices used here."""
    if not rows:
        return 0
    a = [[Fraction(int(x)) for x in row] for row in rows]
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
            if not a[i][col]:
                continue
            q = a[i][col] / pv
            for j in range(col, nc):
                a[i][j] -= q * a[rank][j]
        rank += 1
        if rank == nr:
            break
    return rank


def canonical_columns(rows):
    return [
        tuple(rows[j][k] for j in range(len(rows)))
        for k in range(15)
    ]


def recording_compatible_singleton_blocks(ext, space, complete):
    global CURRENT_SIX
    out = ORIG_COMPATIBLE_BLOCKS(ext, space, complete)
    if len(ext) == 6:
        CURRENT_SIX = (tuple(ext), space, tuple(complete), tuple(out))
    return out


def exact_common_basis_block_sets(good6, projected_complete, projected_data):
    """Common seven-block bases whose classes span every puncture quotient."""
    candidates = ORIG_COMMON_BASIS(
        good6, projected_complete, projected_data
    )
    if not candidates:
        return ()

    assert CURRENT_SIX is not None
    ext6, space6, complete6, recorded_good6 = CURRENT_SIX
    assert tuple(good6) == recorded_good6

    touched6 = B.S.touched_blocks(ext6)
    states6 = B.G.virtual_canonical(ext6, touched6, space6)
    rows6 = B.S.relation_rows_six(ext6, touched6, states6, space6)
    base6 = canonical_columns(rows6)
    base_rank6 = rank_q(base6)
    complete_index6 = {block: i for i, block in enumerate(complete6)}

    state6 = {}
    vector6 = {}
    for block in good6:
        options = B.singleton_options(ext6, block, space6)
        # Two compatible singleton states would force the block canonical-empty.
        assert len(options) == 1
        state = options[0]
        state6[block] = state
        vector6[block] = B.replacement_functional(
            ext6, block, state, space6, complete_index6, len(complete6)
        )

    punctures = []
    projections = tuple(B.S.project_space(space6, i) for i in range(6))
    for i, projected in enumerate(projections):
        ext_i = ext6[:i] + ext6[i + 1:]
        touched_i, complete_i = B.S.canonical_complete_set(ext_i, projected)
        # Match the base verifier's already-computed deficiency profile.
        d_i = projected_data[i][0]
        need_i = 3 + d_i
        assert tuple(complete_i) == tuple(projected_complete[i])
        states_i = B.G.virtual_canonical(ext_i, touched_i, projected)
        rows_i = B.P0.relation_rows(ext_i, touched_i, states_i, projected)
        base_i = canonical_columns(rows_i)
        base_rank_i = rank_q(base_i)
        complete_index_i = {block: j for j, block in enumerate(complete_i)}

        vec_i = {}
        for block in good6:
            if block not in complete_index_i:
                continue
            # Compatibility projects.  Uniqueness forces the same singleton state.
            options_i = B.singleton_options(ext_i, block, projected)
            assert state6[block] in options_i
            assert len(options_i) == 1
            vec_i[block] = B.replacement_functional(
                ext_i,
                block,
                state6[block],
                projected,
                complete_index_i,
                len(complete_i),
            )
        punctures.append((base_i, base_rank_i, need_i, vec_i))

    out = []
    for blocks in candidates:
        if rank_q(base6 + [vector6[b] for b in blocks]) != base_rank6 + 7:
            continue
        ok = True
        for base_i, base_rank_i, need_i, vec_i in punctures:
            image_vectors = [vec_i[b] for b in blocks if b in vec_i]
            if rank_q(base_i + image_vectors) != base_rank_i + need_i:
                ok = False
                break
        if ok:
            out.append(blocks)
    return tuple(out)


B.A.compatible_singleton_blocks = recording_compatible_singleton_blocks
B.common_basis_block_sets = exact_common_basis_block_sets


if __name__ == "__main__":
    B.main()
