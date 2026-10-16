# Hostile audit — sealed dual-component rotation flex

**Date:** 2026-09-18  
**Audited file:** `research/target_c_free_terminal_dual_component_rotation_flex_2026-09-18.md`  
**Verdict:** PASS at proof-only scope after the independence correction in commit `ef6f3ed617bb7edb58a6ff3f0bde187c6a2edd09`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This audit checks the four places where the new corank-to-flex transfer could fail: the fiber-component count, the degree-excess charge, nonlinear exact integration, and independence from previously counted pair-shield parameters.

## 1. Fiber dimension versus relation components

Projecting `ker C_face^T` onto the `n_0` and `n_2` residual face blocks has image dimension at most `2n_0+n_2`. Therefore the fiber supported on `n_1` faces has dimension at least

\[
d_1\ge\sigma_C-(2n_0+n_2).
\]

Inside one connected component of the nonparallel relation graph `R`, every edge equation has two nonzero coefficients, so one vertex scalar determines all others. The restriction of the fiber to that component has dimension at most one. Even if non-`R` trains couple several `R` components, the full fiber injects into the direct sum of the scalar component coordinates. Hence the number of components on which the fiber has nonzero projection is at least `d_1`.

No assumption that a fiber basis vector is supported on a single component is needed.

## 2. Unsealed components really consume `x_U`

Take a nonzero `R` component `K` and a residual train `FG` leaving it at `F\in K`. On the fiber, `y_F=c_Fa_F` with `c_F!=0`.

If `u_FG` is nonparallel to `a_F`, then the `F` term in

\[
(y_F-y_G)\cdot Ju_{FG}=0
\]

is nonzero. If `y_G=0`, this is impossible. If `G` is another nonzero one-anchor component, the edge is either nonparallel to both anchors, in which case it would be an `R` edge joining the components, or parallel at `G`, in which case the `G` term vanishes and the equation is again impossible. Thus the leaving train is parallel to `a_F`.

The unique outside anchor at `F` is another side in the same projective direction. A degree-five residual face is a bounded strict unit-contact pentagon, and the already proved no-parallel-side lemma excludes such a pair. Hence `deg F>=6`, so `F` contributes at least one unit to `x_U`.

Different `R` components have disjoint face sets. Charging one such endpoint per unsealed component is therefore injective at the component level, proving `c_bad<=x_U`.

## 3. The common-angle motion is exact, not infinitesimal

For a sealed component `K`, every residual train incident to a face of `K` ends at another face of `K`; each face also has exactly one outside/activated train. Rotating **all** complete trains incident to `K` by the same angle rotates every oriented side vector of each `K` face by one common rotation matrix. Thus

\[
\sum_jR_\theta r_j=R_\theta\sum_jr_j=0
\]

identically.

This does not assume that the component is pentagonal, fully rhombic, or minimally supported. Higher-degree faces are allowed. Strict rhombi remain exact because a complete train still has one angle parameter along the whole strip.

At activated endpoints, the selected `U--A` train is not an old pivot: the `U` endpoint was not active when the `A` face entered the activation order. The old triangular pivot Jacobian therefore remains invertible. Multiple sealed-component parameters may enter the same activated face; the implicit-function theorem handles them simultaneously because they are free nonpivot coordinates against the same invertible pivot block.

## 4. Independence from `p_U` required correction, but not a loss

The first draft claimed literal support-disjointness from the mutually parallel one-anchor link parameters. That was too strong: a non-`R` mutually parallel link can join two vertices already connected by other `R` edges inside the same `R` component.

The corrected proof uses a stronger coordinate witness. Every nonzero `R` component contains at least one actual `R` edge. Its common-angle component motion changes that residual-internal `R`-edge train. The peeled manifold freezes every residual-internal train, `n_2` pair parameters use `n_2` faces, and a `p_U` parameter changes only its mutually parallel non-`R` link plus the two outside anchors. It never changes an `R` edge. Therefore each sealed-component motion has a free-coordinate entry not used by any previously counted direction. Distinct sealed components have disjoint `R`-edge sets.

The component motions are consequently independent from the old exact manifold before Euclidean quotient. Allowing a loss of one dimension for the all-train rotation is conservative and sufficient.

## 5. Scalar elimination

Let

\[
g\ge(\sigma_C-2n_0-n_2-x_U)_+.
\]

After the conservative rotation loss, the new contribution is `(g-1)_+`. Together with the existing pair-shield structural term `(n_0+n_2)/2`, the elementary optimization

\[
{n_0+n_2\over2}
+(z-2n_0-n_2)_+\ge {z\over4}
\]

for `z>0` is correct. This yields

\[
m_D\ge {b-f\over2}+{1\over4}(\sigma_C-x_U)_+-1
\]

and then `x_U<=Q-f` gives (CR.1).

For the live consequence, the existing correlated ledger supplies

\[
{b-f\over2D}\ge C_0+{r\over2}-o(1),
\qquad r={Q-f\over D},
\]

with `C_0>1.1988388040`. The pointwise inequality

\[
{r\over2}+{1\over4}(s-r)_+\ge{s\over4}
\]

is valid for all `r,s>=0`, so (CR.2) follows without needing to insert the separate numerical bound `r<0.000141`.

This last observation matters: the threshold-free `sigma_C/4` term is not a decimal artifact of the live pinching width. It comes from matching the exact `+r/2` term already present in the pair-shield ledger against the `-(Q-f)` term in the finite corank transfer.

## 6. Scope and remaining obstruction

The result does not show `sigma_C=0`, does not integrate arbitrary singular closure-kernel directions, and does not produce a common diameter-decreasing tangent. A sequence can avoid the new flex penalty by having `sigma_C=o(D)` while the actual diameter graph positively locks the remaining `>1.1988D` exact manifold.

What has changed is the low-flex normal form: a macroscopic `K_5`-type pure-contact dual phase is no longer compatible with the pair-shield endpoint. The remaining endpoint is asymptotically near-full-row-rank on the contact closure side and still must be positively locked by the straight-line diameter system.

**Audit disposition:** PASS. The finite transfer (CR.1), the live threshold-free law (CR.2), and the implication `m_D/D->1.1988388040 => sigma_C=o(D)` are supported by the audited dependencies. The original support-disjointness overstatement was corrected before this audit. No theorem-state file is changed.
