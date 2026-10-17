> Generated reading edition · [exact source](../../../docs/reports/target_c_support7_local_rank_converse_counterexample_2026-10-04.md) · source SHA-256 `0a66b77d32cd158042fed34ce34687a3f2ddfc5e2e941495e002bf08c41c47de`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-21E49C79F54D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: counterexample to the support-only local-rank converse

**Date:** 2026-10-04
**Repository commit:** `d3e6c2e1fdd3abcea10647a0e98d0d780fceae87`
**State version:** `2026-09-14.audit.51`
**Run type:** audit
**Target:** C
**External literature search:** not used
**Computation:** exact local quotient coordinates; corrected finite verifier recorded separately

## Level I status

`STILL OPEN`. This correction concerns a finite support-level branch in the C-II route.

## Source and attempted claim

The source is branch `target-c-nine-k4-dm2-local-rank-repair-20260927`, exact tip
`cbf675ce6baa3395639c548f92a38c0c16f2567d`. No pull request was opened for that
branch. It repairs a support-level certificate whose original current-main report is
`research/target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_support_closure_2026-09-27.md`.

The rejected implication was: for a touched actual-empty triangle block, no repeated
containing tetrahedral support implies local constraint rank one. The forward
implication survives: a repeated support forces rank two. The converse does not.

## Exact counterexample

Let the triangle block be `b={1,2,5}`. Use three distinct tetrahedral supports
`{1,2,3,5}`, `{1,2,4,5}`, and `{1,2,5,6}`. In the exact two-dimensional local
quotient coordinates of the support-seven model, their quotient vectors at `b` are
`(-1,1)`, `(-1,1)`, and `(1,0)`. The resulting coefficient rows on the three
external coordinates are

```text
(-1, -1, 1)
( 1,  1, 0)
```

These rows are linearly independent over `Q`. Thus `dim(E_b)=2` although no
containing support repeats. The three-support configuration is an exact
counterexample to the converse, not a geometric counterexample to Erdős Problem 99.

## Consequence and correction

The original p=1 support verifier is invalid because it assigns rank one solely from
the absence of a repeated support. Its conclusion must not be used. The source branch
also contains a corrected C++ verifier and a larger support relaxation. That
replacement keeps both local dimensions when a nonrepeated block has at least four
incidences; it uses only dimensions forced by repetition and the generalized-weight
bounds. Its scope is only `k=4, D=-2, d_root=0, p=1`, and it does not close the
other nine-no-root branch or C-II. The copied verifier is
`research/verify_target_c_support7_global_segment_relative_nine_noroot_k4_dminus2_d0p1_local_rank_repair_2026_09_27.cpp`.

The original report and verifier on `main` now carry an explicit invalidation notice.
The p=1 claim remains unreviewed until the corrected verifier is run from this
checkout. No theorem-state or route status changes follow from this finite correction.

## Claim classification

| Claim | Status | Reason |
| --- | --- | --- |
| No repeated support implies local rank one | rejected | The three-support exact counterexample above has rank two. |
| A repeated containing support forces local rank two | unreviewed candidate | This forward implication is used in the corrected relaxation; no promotion is made here. |
| The corrected p=1 support relaxation has zero survivors | unreviewed candidate | Scope and exact run are recorded with the companion verifier; it is not a C-II closure. |

## Minimum durable information

Retain the exact three-support rank-two counterexample, reject the old converse, and
use the sound replacement verifier for this one arithmetic profile. The remaining
research branch can then be deleted after the replacement has been reviewed.
