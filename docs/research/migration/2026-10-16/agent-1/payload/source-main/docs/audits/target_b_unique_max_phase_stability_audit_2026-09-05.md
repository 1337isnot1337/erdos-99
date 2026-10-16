<!-- theorem-state: {"artifact_id":"ART-23BE40649360","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Audit — Target B unique-max phase stability exclusion

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_unique_max_phase_stability_exclusion_2026-09-05.md`  
**Verdict:** PASS under the stated coherent dense-core hypotheses.  
**LEVEL I status:** STILL OPEN.

## 1. Interval-neighborhood lemma

A train crossing a linearly ordered family of pairwise noncrossing proper tracks changes region index by one at each crossing. Because two trains cross at most once, the crossed indices form one interval.

PASS.

## 2. Dense interval bigraph extraction

For a row with crossing interval `[l,r]`, the missing count is

`(l-1)+(M-r)`.

If this is at most `eta M`, then the interval contains every central index between `eta M` and `(1-eta)M`. Deleting rows with larger missing count costs at most `q/(eta M)=o(b)` when `q=o(Mb)` and `q/(eta Mb)->0`.

Therefore a complete `(M-o(M)) x (b-o(M))` rectangle exists.

PASS.

## 3. Stability algebra

With

`e_AB=Mb-x`, `e_AC=Ma-y`, `e_BC=z`,

the transversal-triangle inequality

`a e_AB + M e_BC + b e_AC <= 2Mab`

reduces exactly to

`Mz<=ax+by`.

Thus

`M(a+b)-E=x+y-z`

`>=(1-a/M)x+(1-b/M)y`.

Under the fixed gap `a,b<=(1-kappa)M`, an `o(M^2)` extremal deficit forces `x+y=o(M^2)` and then `z=o(M^2)`.

PASS.

## 4. Positive-density leaf class

If `E=Theta(M^2)` while `E<=M(a+b)`, then `a+b=Theta(M)`. Since `b>=a`, one has `b>=tau M` along a subsequence. Hence the `A`–`B` missing count `x=o(M^2)` is also `o(Mb)`, so the interval extraction applies.

PASS.

## 5. Use of the trimmed-grid theorem

The retained `A'`–`B'` pair is complete. The trimmed-grid diagonal argument does not need the third phase to cross every retained `A'` train: each third-phase train contributes to the selected corner displacement with coefficient `-1,0`, or `+1`, and coherence bounds the total by an arbitrary scalar in the third phase direction with magnitude at most `a+o(M)`.

Thus allowing incomplete `A`–`C` crossings is already covered by the worst coherent cancellation used in `F(s,t)`.

PASS.

## 6. Asymptotic count and contradiction

Near saturation gives

`R=M(a+b)+o(M^2)`

once all non-core crossings are `o(M^2)`. With `T=O(M)` in the coherent phase endpoint,

`n=(s+t)M^2+o(M^2)`.

The trimmed-grid lower bound gives

`D^2>=(F(s,t)-o(1))M^2`,

while the strict translated-lattice comparison gives

`D^2<(c(s+t)+o(1))M^2`.

Since the audited trimmed-grid theorem proves `F(s,t)>c(s+t)`, contradiction follows.

PASS.

## Scope

The theorem does not prove that every pure-rhombic survivor is near-saturated in the three-phase inequality. It removes the fixed unique-largest class regime once that near-saturated coherent core has been obtained.
