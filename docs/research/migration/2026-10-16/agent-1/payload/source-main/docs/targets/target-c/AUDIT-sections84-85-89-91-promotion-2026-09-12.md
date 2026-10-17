# Target C audit-chain correction — Sections 84–95

**Date:** 2026-09-12  
**Current state:** `2026-09-11.audit.36`  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

> Historical-path note: this file was originally written as
> `AUDIT-sections84-85-89-91-promotion-2026-09-12.md`. Its first version incorrectly
> called the protected-contact obstruction “Section 91.” The actual numbered Section 91
> is `91-explicit-ordered-grid-audit.md`. The protected-contact theorem has since been
> corrected and renumbered as proof-only Section 95. The stable path of this audit is
> retained so existing references do not break.

This file is an audit correction, not a theorem-state transaction. The canonical
promotion of Sections 90–94 is recorded in
`docs/audits/target_c_sections90_94_promotion_audit_2026-09-12.md` and the audit.36
manifest.

## Correct disposition

- **Sections 84, 85, and 89:** the proofs checked by the original audit are valid and
  canonical.
- **Sections 90–94:** independently audited and canonical as of audit.36.
- **Section 95:** the corrected protected-contact obstruction is mathematically valid
  under its stated scope but remains proof-only pending lifecycle promotion.
- **Rejected inference:** protected simultaneous contact creation does not imply
  positive new KKT support or force visibility.
- **C-II:** open.

## Sections 84, 85, and 89

The load-bearing checks from the first version survive.

For Section 84, canonical Section 67 supplies the needed 2-connected planar embedding,
simple bounded-face cycles, and convexity of bounded positive-contact faces. In the
Type-II near-disk limit, a linear-diameter zero-area exterior cap would converge to a
nondegenerate segment contained in the limiting circle, which is impossible. A convex
internal chamber with perimeter `lambda D+o(D)` and area `o(D^2)` collapses to a segment
of length `lambda/2`. The result is structural; no contradiction is inferred merely
from near-geodesicity.

For Section 85, the strict-rhombus train theorem gives

\[
B_4=2T,\qquad R_4\le T^2/4,
\]

so `B_4>=4sqrt(R_4)`. With `B_4<=b+4f+Q` and
`b+Q=2(q-k)`, this yields

\[
q-k+2f\ge2\sqrt{R_4}.
\]

Writing `d=b-P_F`, `J=d+4f+Q`, and `H=d+2f+Q`, the algebraic step is valid because

\[
5H-3J=2(d+Q-f)\ge0.
\]

Hence the recorded Oler-weighted train-interface surplus is sound. It is a required
currency, not a C-II contradiction.

For Section 89, Section 82 gives

\[
L+Q=4a-6-2s-2c,
\qquad
Q\le2a-6-2s-2c+c^\partial.
\]

Together with `P_R<=L+5Q`,

\[
P_R\le12a-30-10s-10c+4c^\partial.
\]

Every local rhombus train has exactly two physical boundary ends, holes included, so
`2T_R=P_R`. The exact transverse spans give

\[
2A_4\le T_R\operatorname{diam}(P).
\]

The local train/area/diameter budget is therefore valid.

## Sections 90–94

Audit.36 correctly promotes the five numbered modules:

- `C-DENSE-PHASE-CORE` — Section 90;
- `C-EXPLICIT-ORDERED-GRID` — Section 91;
- `C-WRAP-PERIMETER` — Section 92;
- `C-WRAP-FULL-GAP` — Section 93;
- `C-WRAP-THREE-GAP` — Section 94.

The two main advances are independent in type.

Sections 90–91 turn the macroscopic harmonic carrier into a dense inverse-diameter
phase crossing core and then into an explicit linear-by-linear complete ordered train
grid. The key subtlety in Section 91 is handled correctly: the Section-76 common-cone
monotonicity is used before completeness, but that part of Section 76 depends only on
the pairwise phase inequalities. After endpoint-balanced slab selection, common
crossing sign makes each crossing neighborhood an interval, and the dense
consecutive-ones graph admits the claimed linear biclique. The coefficient is too small
to force the localized diameter above `D`, so this closes an extraction gap but not
C-II.

Sections 92–94 progressively strengthen the wrapping-cell diameter floor. Section 94
uses three distinct support-free gaps left by the canonical three-anchor geometry and
obtains

\[
\sin\theta\le3\theta-2\pi,
\qquad \theta=2\arcsin\lambda.
\]

The unique relevant root gives

\[
\boxed{\lambda\ge0.919778662688621\ldots}.
\]

This is the current canonical scalar carrier threshold. Sections 92 and 93 remain valid
intermediate canonical results; Section 94 supersedes them only as a scalar bound.

## Section 95 — protected contact creation

The corrected theorem now lives at
`docs/targets/target-c/95-protected-contact-creation-obstruction-audit.md`.

The finite simultaneous-motion argument is valid. Radius-3 thinning keeps at least
`ceil(M/49)` moving centers. Each selected center moves only to its actual first
contact, by at most `epsilon<=1/4`, so two moving centers remain separated by more than
`3-2epsilon>1`; moving/fixed distances are protected by the individual first-contact
stopping times. All selected centers start and remain in the inner parallel body
`C_{-w}`.

The zero-stress conclusion is also valid. Every new contact component is disconnected
from the old positive-contact core and has no incident diameter edge. Dotting each
vertex equilibrium equation with the vertex position and summing over the new component
gives

\[
\sum_{e\text{ new}}\alpha_e=0.
\]

Since every contact multiplier is nonnegative, all new multipliers vanish. Restriction
and zero-extension identify the terminal and original normalized KKT polytopes.

The general fixed-core statement requires the hypothesis now present in Section 95:
the moved originally isolated points must have their **original positions** in
`C_{-w}`, not merely their terminal positions. Without that condition, an originally
isolated point could be a hull extreme or an active diameter endpoint, so moving it
inward could change the hull or active diameter set. The former duplicate Section 91
omitted this hypothesis; that version was invalid and has correctly been deleted.

Thus Section 95 establishes an obstruction:

> Rearranging already-protected isolates can create linearly many new contacts while
> leaving the old KKT polytope unchanged; contact creation alone cannot force those
> isolates into positive force support.

It does not close the inactive-container branch.

## Authority corrections

The first version of this file contained three bookkeeping/provenance errors.

1. It mislabeled the protected-contact theorem as Section 91. Correct numbering is
   ordered-grid Section 91 and protected-contact Section 95.
2. It claimed canonical Sections 81 and 87 needed to be inserted into
   `canonical_modules`. They were already canonical through manifest
   `current_canonical_entries`; `canonical_modules` is not the only canonical-source
   bucket.
3. It described `|A_r|>=3` in Section 83 as needing a new provenance repair. Canonical
   Section 62 already proves it: `s_r<=a_r-3` and `s_r>=0`, hence `a_r>=3`.

## True mathematical state

The controlling state is

```text
Level I: OPEN
C-I: closed
C-II: open
highest numbered canonical Target C theorem source: Section 94
Section 95: proof-only protected-contact obstruction
Type-II carrier diameter floor: (0.919778662688621... - o(1)) D
```

The full-core Type-II branch now has a macroscopic locally rhombic-saturated harmonic
carrier, an exact `O(D)` train budget, a dense inverse-diameter phase core, and an
explicit linear-by-linear ordered complete train grid. The separate inactive-container
branch still contains a quadratic population of deeply protected contact isolates, and
Section 95 shows why contact creation among those isolates alone cannot be the closing
mechanism.

The missing global theorem must still convert one of these two branches into either an
exact unit equilateral triangle or a source-preserving feasible configuration of
diameter strictly below `D`. Nothing in this audit supports claiming Erdős Problem #99
settled.
