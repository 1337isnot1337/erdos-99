<!-- theorem-state: {"artifact_id":"ART-67A50F87EE8E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearcircle_central_hole_macroscopic_component_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=2a1897697a93669ca2c51e2c2e9ea06d1ae89c48; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle central-hole theorem forces a diameter-scale harmonic component

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** asymptotic convex-geometry strengthening of MC  
**Target:** PR #119 UF near-circle phase  
**Depends on:** DC near-circle convergence, C36/C44/C49 attachment cells, AR Oler cell lower bound  
**Computation:** only displayed decimal evaluation

## LEVEL I STATUS

`STILL OPEN`

MC corrects AR by proving that positive quadratic core population forces at least one harmonic unloaded component with graph diameter `Omega(D)`. In the UF near-circle phase, the disk limit gives a much stronger result.

Let

\[
\delta_{\max}:=\max_r\delta_r,
\qquad
\Delta:=\frac\pi{2\sqrt3},
\]

and along a near-circle subsequence write

\[
\frac{n-v}{D^2}\to\zeta,
\qquad
\frac v{D^2}\to\Delta-\zeta.
\]

Then

\[
\boxed{
\liminf\frac{\delta_{\max}}D
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\tag{CH.1}
\]

At UF's crossover `zeta_*=0.5572837714...`, this gives

\[
\boxed{
\delta_{\max}
\ge(0.6208918647\ldots-o(1))D.
}
\tag{CH.2}
\]

At the asymptotically full-core endpoint `zeta=0`,

\[
\boxed{
\delta_{\max}\ge(1-o(1))D.
}
\tag{CH.3}
\]

Thus the full-core near-circle branch contains one unloaded harmonic component whose internal contact-graph diameter reaches the entire source diameter scale. This is far stronger than the conservative `D/pi` bound from MC.

---

## 1. Geometry of a short chord set on a circle

Normalize first to a Euclidean circle of radius `1/2`, hence diameter one.

### Lemma CH.1 — circular central hole

Let `X` be a nonempty subset of the circle

\[
S=\{x:|x|=1/2\}
\]

with

\[
\operatorname{diam}X\le\mu<1.
\]

Then `X` is contained in a circular arc of central angle at most

\[
2\arcsin\mu<\pi,
\]

and

\[
\boxed{
\operatorname{conv}X
\cap
B^\circ\left(0,\frac12\sqrt{1-\mu^2}\right)
=\varnothing.
}
\tag{1.1}

\]

### Proof

For two circle points with central angular separation `theta in [0,pi]`, their chord length is

\[
\sin\frac\theta2
\]

because the circle radius is `1/2`. Thus every pair in `X` has minor angular distance at most

\[
\theta_\mu:=2\arcsin\mu<\pi.
\]

A subset of a circle with circular diameter below `pi` is contained in an arc of that angular length. Let the two rays bounding a minimal such arc make angles `+-theta/2` about its bisector, with `theta<=theta_mu`.

The chord joining the two arc endpoints has distance

\[
\frac12\cos\frac\theta2
\ge
\frac12\cos(\arcsin\mu)
=
\frac12\sqrt{1-\mu^2}
\]

from the origin. The convex hull of the minor arc lies in the closed circular cap on the outside of that chord. Therefore every point of `conv X` has distance at least the displayed quantity from the origin in the chord-normal direction, proving (1.1). `square`

The key feature is that the excluded central disk is independent of the orientation of the arc.

---

## 2. Stability under convergence of the force hull to the disk

PR #119 DC proves in the `x_B=o(D)` phase that, after translations and division by `D`,

\[
F/D\longrightarrow B_{1/2}
\tag{2.1}
\]

in Hausdorff distance, where `F` is the force hull.

Every attachment set `A_r` consists of vertices of `F`. C44/ZG gives

\[
\operatorname{diam}(P_r)
=\operatorname{diam}(A_r)
\le\delta_r+2,
\qquad
P_r:=\operatorname{conv}A_r.
\tag{2.2}
\]

Fix `mu<1` and suppose along a subsequence

\[
\delta_{\max}/D\le\mu+o(1).
\tag{2.3}
\]

Then every normalized attachment set has diameter at most `mu+o(1)` and lies on a convex boundary converging uniformly to `S=partial B_{1/2}`.

By compactness, Lemma CH.1 is stable under this perturbation: for every fixed `eta>0` and all sufficiently large members of the subsequence,

\[
\boxed{
P_r/D
\cap
B^\circ\left(
0,
\frac12\sqrt{1-\mu^2}-\eta
\right)
=\varnothing
}
\tag{2.4}
\]

for every `r`.

A direct contradiction proof is also available: if (2.4) failed along a sequence of cells, choose a point of the normalized cell entering the smaller central disk; pass to limits of the finitely many convex-combination vertices needed by Caratheodory in the plane. Their limits lie on `S`, have diameter at most `mu`, and their convex hull enters the forbidden disk, contradicting CH.1.

---

## 3. All harmonic cells miss one common central disk

C49 proves the interiors of the cells `P_r` are pairwise disjoint and every cell lies in `F`. Under (2.3), equation (2.4) says **every** cell misses the same central disk, despite their different boundary-arc orientations.

Therefore

\[
\sum_r\operatorname{area}(P_r)
\le
\operatorname{area}(F)
-
\pi D^2
\left(
\frac12\sqrt{1-\mu^2}-\eta
\right)^2.
\]

Using `area(F)/D^2->pi/4`, then letting `eta->0`, gives

### Theorem CH.2 — central-hole cell-area upper bound

If

\[
\limsup\frac{\delta_{\max}}D\le\mu<1,
\]

then

\[
\boxed{
\limsup
\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\mu^2.
}
\tag{CH.4}

\]

This upper bound is independent of `c_I`, `S=sum delta_r`, or how the component diameter is distributed. It is strictly stronger than the isodiametric-sum bound in the near-circle regime.

---

## 4. Oler forces the opposite cell-area lower bound

AR proves

\[
\sum_r\operatorname{area}(P_r)
\ge
 a_0(v-q)
-\frac{a_0\pi}{2}S
-a_0(\pi-2)c_I,
\qquad
a_0=\frac{\sqrt3}{2}.
\tag{4.1}
\]

All quantities after `a_0v` are `O(D)`, while by UF

\[
\frac v{D^2}\to\Delta-\zeta.
\]

Hence

\[
\boxed{
\liminf
\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\ge
 a_0(\Delta-\zeta).
}
\tag{4.2}

\]

Since

\[
a_0\Delta=\frac\pi4,
\]

this is

\[
\boxed{
\liminf
\frac1{D^2}
\sum_r\operatorname{area}(P_r)
\ge
\frac\pi4
\left(1-\frac\zeta\Delta\right).
}
\tag{4.3}

\]

---

## 5. Proof of the diameter-scale component theorem

Suppose, toward contradiction, that along a subsequence

\[
\frac{\delta_{\max}}D
\to\mu
<
\sqrt{1-\frac\zeta\Delta}.
\]

CH.4 gives

\[
\limsup\frac1{D^2}\sum_r\operatorname{area}(P_r)
\le\frac\pi4\mu^2
<
\frac\pi4\left(1-\frac\zeta\Delta\right),
\]

contradicting (4.3). Therefore

\[
\boxed{
\liminf\frac{\delta_{\max}}D
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\]

This proves CH.1.

Numerically, at

\[
\zeta_*=0.5572837714\ldots,
\]

we have

\[
\sqrt{1-\zeta_*/\Delta}
=0.6208918647\ldots,
\]

proving CH.2.

If `zeta=0`, the right side is one, proving CH.3.

---

## 6. The macroscopic component also has linearly many attachment contacts

Let `I_*` attain `delta_max`, and let `t_*` be its number of physical contact edges to loaded terminals.

C40 gives

\[
\boxed{t_*\ge\delta_{\max}+3.}
\tag{6.1}
\]

Hence throughout the UF near-circle branch

\[
\boxed{
\liminf\frac{t_*}D
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\tag{6.2}
\]

Moreover almost all loaded vertices have both adjacent hull intervals equal to direct unit contacts when `x_B=o(D)`. Such a vertex has at most one remaining contact slot by C35. Only `o(D)` bad hull vertices can support duplicate attachment contacts.

Consequently, if `a_*=|A_*|` is the number of **distinct** loaded attachments of `I_*`, then

\[
\boxed{
 a_*
\ge t_*-o(D),
}
\tag{6.3}
\]

and therefore

\[
\boxed{
\liminf\frac{a_*}D
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\tag{6.4}
\]

A direct finite version is obtained by observing that a loaded vertex incident to both direct hull-side contacts has at most one `B-I` contact, while the number of loaded vertices incident to a bad hull interval is at most `2x_B`; each such vertex contributes at most two duplicate contacts beyond its first. Thus

\[
\boxed{a_*\ge t_*-4x_B.}
\tag{6.5}
\]

This makes the surviving object very concrete: one harmonic component has both graph diameter and distinct boundary attachment population on the same linear source scale.

---

## 7. Full-core endpoint

If `zeta=0`, CH gives

\[
\delta_*\ge(1-o(1))D,
\qquad
a_*\ge(1-o(1))D.
\]

Thus an asymptotically full-core near-circle survivor contains one connected unloaded component which

1. has contact-graph diameter essentially `D`;
2. attaches to essentially `D` distinct loaded hull vertices;
3. lies inside the convex hull of those attachments;
4. coexists with the almost-complete direct unit-contact hull cycle and UF's linear exceptional-face defect.

This is close to a disk-spanning pinned mesh, not an arbitrary harmonic atom.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| circle central-hole lemma | proved | chord/angular diameter geometry |
| uniform stability under `F/D -> disk` | proved by compactness | Caratheodory reduces any violation to finitely many limit boundary points |
| CH.4 area upper bound | proved | all disjoint cells miss one common central disk |
| CH.1 macroscopic component bound | proved conditional on UF near-circle | compare CH.4 with AR Oler lower cell area |
| distinct attachment bound | proved | C40 + at most `2x_B` bad hull vertices + loaded degree cap |
| full-core `delta_max/D>=1` | proved asymptotically | `zeta=0` in CH.1 |
| Level I | still open | a disk-scale harmonic component is not yet excluded |

---

## 9. Next target

The positive-density near-circle branch no longer has a diffuse harmonic-cell obstruction. It contains one specific component `I_*` with

\[
\delta_*/D\ge\mu(\zeta),
\qquad
|A_*|/D\ge\mu(\zeta),
\qquad
\mu(\zeta)=\sqrt{1-\zeta/\Delta}.
\]

The next useful theorem is a **boundary-arc localization** of `A_*`.

Because `diam(A_*)<=delta_*+2`, the disk limit says that if `delta_*/D->mu<1`, then `A_*` must lie in a hull arc of normalized boundary length at most `arcsin(mu)`. Combined with `|A_*|/D>=mu`, this leaves only the narrow slack

\[
\arcsin\mu-\mu.
\]

At the UF crossover `mu=0.62089...`, that slack is only `0.04899...D`. Proving that the component requires more attachment spread than this, using TC 3-connectivity or UF's exceptional-face defect, would close that population subbranch.
