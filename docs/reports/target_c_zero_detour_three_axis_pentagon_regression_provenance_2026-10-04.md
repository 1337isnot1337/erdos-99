<!-- theorem-state: {"artifact_id":"ART-1B417242EBA0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — exact three-axis pentagon regression for the zero-detour route

**Date:** 2026-10-04  
**Status:** provenance record for a finite regression; no theorem-state or lifecycle promotion.  
**Source branch:** `research/cii-zero-detour-pentagon-regression-20260912`  
**Source tip:** `3c045bf852b51aec074c6cc98cfa9840eab5a728`  
**Original PR:** none.  
**Source file:** `research/target_c_zero_detour_three_axis_pentagon_regression_2026-09-12.md`  
**Verifier/certificate:** none; the construction below is analytic and exact.

## Attempted implication and failure

The failed route tried to infer that a strict convex contact pentagon whose edge
directions approach the three triangular-lattice projective axes must either acquire
an exact unit diagonal, have a fixed positive phase gap, or pay a uniform positive
finite Oler slack. The implication is false even for one finite face. This local
counterexample does not construct a global minimizer or address the global
minimum-diameter quantifier.

For any sufficiently small (a>0), set (b=b(a)) by

\[
\cos b=\cos a-\tfrac12,
\]

and take five oriented unit edge vectors with arguments

\[
-a,\quad a,\quad \pi-b,\quad \pi,\quad \pi+b.
\]

Their vector sum is (2\cos a-2\cos b-1=0), so they close. The successive exterior
turns are (2a,\pi-b-a,b,b,\pi-b-a); for sufficiently small positive (a), all
are strictly between (0) and (2\pi/3). The pentagon is therefore strictly
convex. Each diagonal joins vertices two edges apart and has length
\(2\cos(\delta/2)>1\) for its intervening turn \(\delta<2\pi/3\). Thus its only
unit pairs are its five sides, and it contains no unit equilateral triangle.

As (a\downarrow0), (b\to\pi/3), and the projective edge directions approach
the three axes (0,\pi/3,2\pi/3\). The limiting vertex polygon has area
\(3\sqrt3/4\). For the five-point face, the Oler slack is
\(A-3\sqrt3/4\), so it tends to zero. Hence neither approximate three-axis alignment
nor triangle-freeness supplies a uniform local phase gap or positive per-face Oler
slack.

## Durable consequence and limits

This records the exact near-orbit regression already cited in
[`target_c_free_terminal_pentagon_phase_capacity_gap_02088_2026-09-18.md`](../../research/target_c_free_terminal_pentagon_phase_capacity_gap_02088_2026-09-18.md): an atomic limiting direction does not make finite-source directions exact, and near-unit noncontact diagonals can invalidate a uniform local face charge. Any continuation must use additional global train-order, KKT/co-embedding, or collective-deformation information.

The result is only a finite local configuration family. It is not a sequence of global
minimizers, not a same-cardinality diameter competitor, and neither proves nor
disproves Target C-II or Level I. The source branch's route failure is recorded here;
the original unreviewed report remains recoverable in Git history and the pre-cleanup
bundle.
