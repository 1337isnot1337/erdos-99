# Target C: close S1 in nine-no-root k=5, D=-1, d_root=0, p=5

Date: 2026-09-29

Status: exact finite closure of the support orbit

    S1 = [0123]^3 [0124]^3 [0134]^3

inside the nine-no-root `k=5, D=-1, d_root=0, p=5` branch.

This note also records a correction to the immediately preceding orientation-narrowing attempt: local empty-state coefficient spaces lie in the rank-four coefficient-constraint space `P`, not in `P^perp`. The preceding four-support narrowing is therefore withdrawn and is not used below.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_nine_noroot_k5_dminus1_d0p5_S1_three_empty_obstruction_2026_09_29.py`

## 1. Forced orientation and touched blocks

Each of the three tetrahedral supports occurs with multiplicity three. There are exactly three four-cycle orientations on a fixed support, so all three occur. Thus S1 has a unique oriented external family.

Its touched triangle blocks are

    012, 013, 014, 023, 024, 034, 123, 124, 134.

Hence `|T|=9`.

The exact ordinary triangle-boundary rank is

    rank H(T) = 6.

## 2. At least three actual-empty blocks are required

Let `C` be the touched actual-complete blocks and `E` the touched actual-empty blocks.

The committed face-local `k=5` identity gives

    rank H(T) - rank H(C) >= 5.

Here `d_root=0`, so the actual complete-root rows are independent and

    rank H(C) = |C|.

Since `rank H(T)=6`,

    |C| <= 1.

The incomplete-root cost is `p=5`. Every touched nonempty incomplete block consumes at least one selected root row, so there are at most five such blocks. The nine touched blocks are partitioned into actual-empty, actual-complete, and nonempty incomplete blocks. Therefore every realization would satisfy

    |E| >= 9 - 1 - 5 = 3.

## 3. Three actual-empty blocks cannot fit in P

For an actual-empty block `b`, let `E_b <= Q^9` be its exact local empty-state coefficient space. Under the current-main coefficient-space convention,

    E_b <= P,

where

    rank(P)=4.

The companion verifier persists the exact S1 local quotient table. Every `E_b` has rank two. It exhausts all

    C(9,3) = 84

three-block choices and computes the exact rational rank of

    span(E_b : b in F).

The census is

    span rank 5: 28 triples
    span rank 6: 56 triples
    span rank <=4: 0 triples.

Thus any three distinct actual-empty blocks would force a subspace of `P` of rank at least five, impossible because `rank(P)=4`.

Combined with Section 2, S1 has no realizable state.

## 4. Execution and audit status

The standalone verifier uses Python `Fraction` arithmetic for every rank calculation. The exact persisted source was executed before commit and terminated with

    PASS: S1 is impossible in nine-no-root k=5,D=-1,d_root=0,p=5
    touched_blocks 9
    rank_H_T 6
    triple_empty_span_rank_census {5: 28, 6: 56}
    max_complete_blocks 1
    min_empty_blocks 3

The local quotient table is written explicitly in the verifier, with the nine external orientations and nine touched blocks fixed. It was reconstructed from the same committed Target-C quotient normal form used by the current-main orientation helper. The closure claim depends only on that explicit table and exact rational ranks. It does not use the withdrawn `P^perp` extension test, generalized-weight heuristics, finite-field ranks, or unexecuted verifier code.

## 5. Remaining frontier

The sound support-level certificate preceding the withdrawn orientation narrowing left S1 through S8. This note removes S1. Therefore the defensible frontier is now S2 through S8 until each is re-audited with the correct containment direction `E_b <= P`.

The immediate next target is a corrected orientation/local-space test on S2 through S8, or a direct empty-span obstruction analogous to this S1 argument.
