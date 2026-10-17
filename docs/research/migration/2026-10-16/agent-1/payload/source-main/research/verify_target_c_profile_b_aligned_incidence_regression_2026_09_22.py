#!/usr/bin/env python3
"""Exact counterexample to the proposed aligned-support Lemma 1.

The concurrent aligned-incidence closure claims that an aligned rank-one
singleton block has empty-space generator in the source coefficient plane P,
and therefore support at least d_1(P).  The virtual-canonical convention has
the opposite implication: a block is canonical-complete precisely when its
empty constraint E_b is *not* contained in P.  Alignment makes the singleton
constraint zero, but does not put E_b in P.

This certificate constructs eight no-root rows with one row touching the root
block b=(0,1,2), all seven other rows avoiding b, and a rank-two plane P whose
columns are projectively distinct.  Then d_1(P)=7, the local empty space is
the coordinate line <e_0> not contained in P, and singleton state 1 is
compatible with P with zero local constraint.  Thus the aligned support has
size one, contradicting the claimed support>=4 inference.
"""

from fractions import Fraction
from pathlib import Path
import contextlib
import importlib.util
import io

HERE = Path(__file__).resolve().parent
BASE = HERE / "verify_target_c_support7_global_segment_relative_five_noroot_k5_2026_09_20.py"
spec = importlib.util.spec_from_file_location("e99_aligned_regression_base", BASE)
K = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K)
R = K.R


def main():
    block = 0  # root triple (0,1,2)
    touching = 105  # DESC[105]=(1,2,3,4), with QCOMP[105][0]=(1,0)
    ext = (touching,) + tuple(
        e for e in R.NO_ROOT
        if R.QCOMP[e][block] == (0, 0)
    )[:7]
    assert len(ext) == 8
    assert R.DESC[ext[0]] == (1, 2, 3, 4)
    assert all(R.QCOMP[e][block] == (0, 0) for e in ext[1:])

    # P has eight distinct projective columns, hence d_1(P)=7.
    P = R.rowspace_key((
        (1, 0, -1, -2, -3, -4, -5, -6),
        (0, 1, 2, 3, 4, 5, 6, 7),
    ))
    assert len(P) == 2

    empty = R.local_constraint_key(ext, block, 0)
    singleton = R.local_constraint_key(ext, block, 1)
    assert empty == ((Fraction(1),) + (Fraction(0),) * 7,)
    assert singleton == ()  # all touching local vectors are parallel to (1,0)
    assert not R.is_subspace(empty, P)  # therefore virtual-canonical complete

    # The counterexample can even use an *obtainable* rank-two local
    # constraint plane, rather than an arbitrary abstract P.  Block 1's
    # empty-state constraint has rank two on these eight rows, has d1=5, and
    # still leaves b virtual-canonical complete.
    P_obtainable = R.local_constraint_key(ext, 1, 0)
    assert len(P_obtainable) == 2
    assert not R.is_subspace(empty, P_obtainable)
    generated_projective = []
    zero_generated = 0
    for i in range(8):
        x, y = P_obtainable[0][i], P_obtainable[1][i]
        if x == 0 and y == 0:
            zero_generated += 1
        elif x == 0:
            generated_projective.append("inf")
        else:
            generated_projective.append(Fraction(y, x))
    generated_d1 = (
        8 - zero_generated
        - max(generated_projective.count(value) for value in set(generated_projective))
    )
    assert generated_d1 == 5

    # Projective-column minimum distance of P.
    projective = []
    for i in range(8):
        x, y = P[0][i], P[1][i]
        projective.append("inf" if x == 0 else Fraction(y, x))
    assert len(set(projective)) == 8
    d1 = 8 - max(projective.count(value) for value in set(projective))
    assert d1 == 7

    touched = tuple(i for i, e in enumerate(ext) if R.QCOMP[e][block] != (0, 0))
    assert touched == (0,)
    print("PASS: aligned-support Lemma 1 regression")
    print("block", block, "root_triple", R.BLOCKS[block])
    print("external_rows", ext)
    print("empty_space", empty)
    print("singleton_state_1_constraint", singleton)
    print("empty_contained_in_P", R.is_subspace(empty, P))
    print("source_d1", d1)
    print("aligned_touched_support", touched)
    print("obtainable_plane_generator_block", 1)
    print("obtainable_plane_d1", generated_d1)
    print("empty_contained_in_obtainable_P", R.is_subspace(empty, P_obtainable))


if __name__ == "__main__":
    main()
