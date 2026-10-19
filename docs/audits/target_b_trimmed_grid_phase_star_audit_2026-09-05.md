<!-- theorem-state: {"artifact_id":"ART-F2F397E1FC35","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "baaf8229da8a4ec18862b8d901bf7a430a04ca9f", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/audits/target_b_trimmed_grid_phase_star_audit_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3f881972504e85af03466c83ce5df0eae8abae0427cc74d8d054d7cb2176fb45"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Audit — Target B trimmed-grid phase-star exclusion

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md`  
**Verdict:** PASS under its stated complete coherent phase-star and pure-rhombic asymptotic hypotheses.  
**LEVEL I status:** STILL OPEN.

## 1. Grid penetration

Two pairwise-noncrossing train families with complete mutual crossing form a topological rectangular pseudoline grid. Region coordinates count crossed tracks from the two outer sides. After trimming `k,l` layers, every point of the retained central rectangle has both coordinates at least the corresponding trim depth up to the fixed corner convention.

Every disk-boundary region is exterior in at least one coordinate because endpoints of the two complete train families occur in four alternating boundary blocks. Therefore a proper train arc that reaches the central rectangle from the boundary must cross at least `min(k,l)-O(1)` selected grid tracks.

The stated `min(k,l)-2` bound is a safe finite form.

PASS.

## 2. External separator count

Every external train contributing to the selected corner displacement separates the diagonal pair and hence penetrates the trimmed grid. If each such train incurs `Omega(M)` crossings with the phase-star grid and the total crossing mass involving external trains is `o(M^2)`, only `o(M)` such trains can contribute.

Since every train vector has unit norm, their total displacement contribution is `o(M)`.

PASS.

## 3. Third-phase cancellation

A third coherent phase of at most `a` trains can contribute to one diagonal only through coefficients in `{-1,0,1}`. Projective coherence around one unit direction `w` therefore gives

`E_C=xw+o(M)` with `|x|<=a+o(M)`.

No sign assumption is needed; allowing arbitrary real `x` in the interval is the worst possible coherent cancellation.

PASS.

## 4. Constrained quadratic minimum

With

`u=(1,0)`, `v=(1/2,sqrt(3)/2)`, `w=(1/2,-sqrt(3)/2)`,

one has

`|u+t v+xw|^2=1+t+t^2+(1-t)x+x^2`.

The unconstrained minimizer is `x=-(1-t)/2`. Restricting to `|x|<=s` gives exactly

`F(s,t)=1+t+t^2-s(1-t)+s^2`

for `s<(1-t)/2`, and

`F(s,t)=3(1+t)^2/4`

otherwise.

PASS.

## 5. Comparison with the translated-lattice scale

Let `c=2sqrt(3)/pi`. In the complete-star quadratic-core regime,

`n=(s+t)M^2+o(M^2)`

under the stated `T=O(M)` pure-disk hypothesis, so the canonical strict lattice comparison gives

`D(n)^2<(c(s+t)+o(1))M^2`.

For `s>=(1-t)/2`, `s<=t` gives `c(s+t)<=2ct`, while

`3(1+t)^2/4-2ct`

has positive leading coefficient and negative discriminant because `2c<3`.

For `s<(1-t)/2`, the difference

`H=F-c(s+t)`

is decreasing in `s` on the allowed interval, and at `s=(1-t)/2` equals

`(1+t)(3(1+t)/4-c/2)>0`.

Thus `F(s,t)>c(s+t)` everywhere on `0<=s<=t<=1`.

PASS.

## 6. Scope

The theorem requires a complete positive-density center-to-leaf grid after trimming and only `o(M^2)` non-star crossings. It does not itself show that every near-extremal coherent phase core contains such a grid. That is the separate ordered-stability problem addressed by the unique-max and balanced-phase notes.

Audited conclusion:

> Complete coherent phase stars cannot occur in sufficiently large pure-rhombic global minimizers, even when train-coordinate bases are misaligned and a third coherent phase contributes its worst admissible linear cancellation.
