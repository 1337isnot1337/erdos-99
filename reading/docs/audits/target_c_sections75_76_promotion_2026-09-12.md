> Generated reading edition · [exact source](../../../docs/audits/target_c_sections75_76_promotion_2026-09-12.md) · source SHA-256 `c91fa2ee5423d736a9bae676190efa01e71e5cf2e33e3e08619d7ed43e2e4e93`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-FCA6C815AA97","canonical":true,"claim_ids":["C-COMP-DEATOMIZATION","C-HOLE-GRID-DIAMETER"],"claim_statuses":{"C-COMP-DEATOMIZATION":"canonical","C-HOLE-GRID-DIAMETER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Sections 75–76 promotion audit

**Date:** 2026-09-12

This note records an independent hostile audit of proof-only Sections 75 and 76 before theorem-state promotion. The artifact-index generator replaces the temporary artifact id in this header with the path-derived canonical id.

## Section 75 — all-phase component deatomization

Certified.

The finite curvature-window argument is valid. For a fat convex force hull, an unloaded component of graph diameter at most `M` has all loaded attachments within Euclidean distance `L=M+2` of one representative attachment. The inner/outer concentric disk bounds convert this into a boundary-arclength window of radius at most `22L`. If that window spent less than `atan(1/(4L))` exterior turning, all attachments and their convex hull would lie in a strip of width below `1/2`; harmonic trapping would then put an unloaded vertex and at least three unit neighbors in the same strip, contradicting the unit-separation strip lemma. Packing disjoint turning windows gives the stated `N_M=O((M+2)^2)` bound.

Canonical full-force area stability plus the source circumradius bound really does imply the finite fatness `B(o,D/20) subset F subset B(o,11D/20)` for all sufficiently large survivors. The Section-62 component-diameter ledger gives `sum delta_r <= 2+2*pi*D`; choosing `M=floor(D^(1/3))` therefore yields `c_I=O(D^(2/3))`.

The exact ledger eliminations in (75.19)–(75.26) were recomputed independently; the signs and coefficients are correct. Contact-isolated source points remain outside `c_I` and are not bounded.

## Section 76 — hole-stable complete-grid order and diameter

Certified.

For the canonical Section-73 phase-pure complete shores `A,B`, the Section-68 phase law and fixed labels force every product crossing to have the same orientation and `delta_ab=x_b-x_a>0`. The displacement cones from Theorem 10.6 then admit the common projection chosen in (76.12); every selected train centerline is strictly monotone in that coordinate.

Lemma 76.1 was checked separately. For two same-shore graph arcs with overlapping domains, their vertical order is constant. If one opposite-shore arc crossed them in the wrong relative order, the interval between the two crossings must intersect the common domain, where the uniform crossing sign gives an immediate vertical-order contradiction. If the domains are disjoint, their left-to-right order is already fixed. Hence every selected train sees one common order even with holes and arbitrary finite endpoints.

The two-leg path estimate (76.25) is also correct. Between the first and last selected crossing on one train, all omitted intervening rhombi have positive projection. The selected crossing rhombi contribute full side vectors except for two endpoint half-vectors, whose total loss is at most one on each leg, giving the exact `-2`.

Finally canonical (68.14) gives `S_AB < C_phase D` with `C_phase=pi^2*sqrt(3)*(2+sqrt(3))/12`. The decomposition `S_AB=abg+b sum r_a+a sum q_b` implies (76.36), so the finite diameter inequality

`D >= (sqrt(3)/2)(a+b) - S_AB/min(a,b) - 2`

and its `a+b`, `ab` corollaries are valid.

## Section 73 phase-purification sharpening

The canonical `(c_PS/3)R/T` phase-pure shore bound is valid but not sharp at the combinatorial step. Let `L_1,L_2` be the phase-label supports of the two all-crossing Fox--Pach shores. Since every cross-shore pair crosses and same-label trains cannot cross, `L_1` and `L_2` are disjoint nonempty subsets of `Z/3`. Therefore each has size at most two. Taking the largest phase class in each shore retains at least one half of each shore, so the same proof gives

`|A|,|B| >= (c_PS/2) R/T`.

No new theorem or topology assumption is used. This sharpening is promoted in the same transaction.

## Disposition

Promote Section 75 as an all-phase structural theorem and Section 76 as a quadratic-core complete-grid theorem. Neither is a Level I closure. Section 75 does not control contact-isolated source points or component population; Section 76 does not force a sufficiently large complete-grid coverage coefficient by itself.
