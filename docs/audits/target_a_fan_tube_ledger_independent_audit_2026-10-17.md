<!-- theorem-state: {"artifact_id":"ART-D6983CBF70C5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
# Target A seed-63 full-tube ledger: corrected audit disposition

**Original package:** PR #87, `33a4aaa016d0a219e2f9e8e7a92c87ff4aa77afb`.  
**Original audit:** PR #92, `96e54788d1a42d246dba0a60ab5e8a81fc5aea4a`.  
**Authority:** theorem state `2026-10-15.publication.2`. Target A and Level I remain open.

## Disposition

**The original PASS is superseded in its canonical-admissibility conclusion.**
The audit repeated the package's incorrect definition of a deep source column.
It accepted an optimum of `M-1` over Section-102 admissible bases.
That witness omits required deep columns.

The [corrected package](../../research-packages/target-a-fan-tube-ledger/README.md)
proves an admissible optimum of **1**, attained by the predecessor.
The `M-1` calculation remains valid for the larger class of `Z`-perfect
matchings, with the full nonbasis complement retained.
It cannot certify the canonical boundary Schur interface.

This document records a correction by the implementing AI session and its
mathematical collaborator. They contributed to the correction and do not count
as its independent reviewers. The original audit and its reported runs remain
available at the [immutable submitted audit](https://github.com/1337isnot1337/erdos-99/blob/96e54788d1a42d246dba0a60ab5e8a81fc5aea4a/docs/audits/target_a_fan_tube_ledger_independent_audit_2026-10-17.md).
Current verification must examine the corrected source.

A separate AI-agent reviewer has now reconstructed the corrected proof and
completed independent exact checks. The [review record](../research/review-artifacts/fan-ledger-correction/independent-audit.txt)
records the reviewed commit, exhaustive finite control, independent replay and
limitations. This is review of the supplied regression, with no canonical promotion.

## The definition mismatch

Section 102 of [Scaffold and Hall](../targets/target-a/02-scaffold-and-hall.md)
defines `X^circ={x:N(x) subseteq Z}`.
For this phase, the strict neighbor offsets are
`(0,0),(-1,0),(0,-1)`. Thus

`X^circ={(i,j):i,j>=1, i+j<=M-1}`.

The identity matching makes this whole restriction independent.
Every admissible deep-first basis must therefore contain all of `X^circ`.
The original test instead required geometric distance greater than one from
the hull. That sufficient depth condition does not characterize `X^circ`.

The relaxed witness omits `(2,1)` and `(1,j)` for `2<=j<=M-2`.
There are `M-2` omitted deep columns.
At `M=5`, they are exactly `(1,2),(1,3),(2,1)`;
the old geometric predicate has an empty deep set and accepts the witness.
This is a concrete failed admissibility check.

## Corrected all-basis argument

The collar and tube calculations remain useful:
`|O|=3M+3`, `|T_Z|=2M+1`, and `|T_O|=3`.
For an admissible basis, all `M+1` nonbasis columns are boundary terminals.
Only three boundary source vertices belong to the fixed fan.

Each exterior row has one source neighbor.
The three exterior tube rows neighbor only those three boundary fan vertices.
Every surviving terminal consequently has a distinct exterior neighbor in
its sector outside the tube. Hence `|O_i|>=|C_i|`.

Write `t_Sigma` for the number of nonbasis fan terminals.
Basis closure cannot remove another nonbasis column, so

`sum_i min(|C_i|,|O_i|)=M+1-t_Sigma`, with `t_Sigma<=3`.

The exact cut identity gives

`Xi-|T_Z|=(M-1)-(M+1-t_Sigma)=t_Sigma-2<=1`.

The predecessor is admissible and has `t_Sigma=3`; it attains 1.
Its actual generic right deficiency is `2M+2`, so its raw tube cut loses
`2M+1`. The larger relaxed class attains `M-1`, but that comparison
uses all unmatched columns and supplies no canonical admissibility.

## Retained scope and next action

The original audit independently reconstructed the phase, complete collar,
tube tables, injective matchings, sector counts and full generic rank.
The correction preserves those useful calculations while withdrawing their
incorrect use as evidence of the deep-first normalization.

The corrected checker tests the incidence definition and rejects the relaxed
witness at every declared size. Its normal and optimized replay, saved evidence,
source metadata and independent correction audit must be recorded at the
actual reviewed commit.

The next research question is a joint source-demand and sink-population
inequality for an actual plateau response.
Changing the basis of this fixed fixture cannot improve its admissible optimum.
This supplied family gives no canonical demand `j_*`, source extraction,
same-cardinality competitor, zero-slack resolution or Level I closure.
