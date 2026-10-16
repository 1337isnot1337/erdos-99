<!-- theorem-state: {"artifact_id":"ART-571834594F74","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — pair-incidence extraction for anchored Groemer triples

**Date:** 2026-09-14\
**Repository base:** `cb3d4406`\
**State version:** `2026-09-14.audit.51`\
**Run type:** proof-only extraction refinement\
**Target:** Target C-II, canonical full-core Type-II branch\
**Dependencies:** hostile-audited anchored Groemer stability and the triangle-free contact-degree bound\
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The hostile audit of all-degree Groemer stability strengthens the small-residual branch
as follows.  For every fixed degree cutoff `K` and every fixed `eta>0`, all but `o(D)`
of the degree-at-most-`K` exceptional faces contain an **anchored almost-equilateral
triple**

\[
(u,v,w)
\]

with

\[
|u-v|=1,
\qquad
1\le |u-w|<1+\eta,
\qquad
1\le |v-w|<1+\eta,
\tag{AT.1}
\]

where `uv` is an actual cyclic boundary contact of that face.

The audit extracted vertex-disjoint triples by first making the whole containing faces
vertex-disjoint, losing a factor `169` at cutoff `K=42`.  That is unnecessary.  We may
choose one anchored triple from every good face and build the conflict graph of the
**three selected vertices only**.  Its maximum degree is at most twelve.  This yields a
`1/13` extraction, independent of the face degree, and lets the fixed cutoff tend to
infinity after the asymptotic estimate.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
f_*:=\sqrt{\Delta_2}-{\pi\over4}+0.00021
=0.167124643466509\ldots .
\tag{AT.2}
\]

The conclusion is

\[
\boxed{
R_F=o(D)
\Longrightarrow
\exists\eta_D\downarrow0:\quad
\liminf {N_{\triangle}(\eta_D)\over D}
\ge {f_*\over13}
=0.012855741805116\ldots,
}
\tag{AT.3}
\]

where `N_triangle(eta)` is the maximum number of pairwise vertex-disjoint triples
satisfying (AT.1) in distinct exceptional faces.

## 1. Supply of anchored triples

For a fixed integer `K>=5`, let `f_{<=K}` count exceptional bounded faces of degree at
most `K`.  The AG42 face floor and `Q<=P_F` give

\[
\liminf {f_{\le K}\over D}
\ge
\ell_K:=f_*-{\pi\over K-3}.
\tag{AT.4}
\]

The hostile-audited anchored Groemer theorem says that for every fixed `K,eta` there is
`tau_K(eta)>0` such that a degree-at-most-`K` exceptional face without a triple (AT.1)
has residual at least `tau_K(eta)`.

On the branch `R_F=o(D)`, all exceptional-face residuals are nonnegative and their sum
is at most `R_F`.  Therefore only `o(D)` degree-at-most-`K` faces can fail (AT.1).
Thus, for every fixed `K,eta`, there are at least

\[
(\ell_K-o(1))D
\tag{AT.5}
\]

good exceptional faces.  Choose one anchored triple from each.

## 2. Triple-conflict graph has maximum degree at most twelve

Form a graph whose vertices are the chosen anchored triples.  Join two graph vertices
when the corresponding source triples share at least one source point.

Every selected triple lies in one exceptional face.  An assigned contact-isolated
interior point belongs to only that chamber, so such an endpoint creates no conflict
with a triple selected from another face.

For a positive-core boundary vertex `x`, triangle-freeness gives

\[
\deg_C(x)\le5.
\tag{AT.6}
\]

Indeed, distinct unit neighbors around `x` have angular separation strictly greater
than `pi/3`; equality would create an exact unit equilateral triangle and smaller
separation would violate unit separation.

At a plane-graph vertex, the number of distinct incident bounded faces is at most the
number of contact-edge sectors, hence at most the contact degree.  Consequently a
fixed source vertex can occur in selected triples from at most five distinct
exceptional faces.

Take one chosen triple `{u,v,w}`.  Through each of its three source vertices there are
at most four *other* selected triples.  Union-bounding the three conflict sets gives

\[
\boxed{\Delta(G_{triple})\le12.}
\tag{AT.7}
\]

Repeated faces around a bridge or articulation vertex do not increase the number of
distinct selected-face triples, and overlaps between the three conflict sets only
improve (AT.7).

A graph of maximum degree twelve has an independent set containing at least one
thirteenth of its vertices.  Hence, for fixed `K,eta`,

\[
\boxed{
\liminf {N_{\triangle}(\eta)\over D}
\ge {\ell_K\over13}.
}
\tag{AT.8}
\]

## 3. Remove the cutoff loss

The left side of (AT.8) does not depend on `K`.  The estimate holds for every fixed
cutoff with positive `ell_K`, while

\[
\ell_K\uparrow f_*
\qquad(K\to\infty).
\]

Therefore for every fixed `eta>0`, on `R_F=o(D)`,

\[
\boxed{
\liminf {N_{\triangle}(\eta)\over D}
\ge {f_*\over13}
=0.012855741805116\ldots .
}
\tag{AT.9}
\]

The previous hostile-audit extraction gave `0.000512254353148...D` for fixed `eta`.
Thus (AT.9) improves the fixed-gap coefficient by a factor greater than `25`.

## 4. Vanishing gap without an additional density loss

Choose increasing fixed cutoffs `K_j` satisfying

\[
{\ell_{K_j}\over13}>{f_*\over13}-{1\over j},
\]

and set `eta_j=1/j`.  For each fixed `j`, (AT.8) holds asymptotically.  Choose increasing
thresholds `D_j` such that for all `D>=D_j` in the subsequence the extracted matching
has size at least

\[
\left({f_*\over13}-{2\over j}\right)D.
\]

For `D_j<=D<D_{j+1}`, put `eta_D=eta_j`.  Then `eta_D->0` and

\[
\boxed{
\liminf {N_{\triangle}(\eta_D)\over D}
\ge {f_*\over13}
=0.012855741805116\ldots .
}
\tag{AT.10}
\]

The hostile audit's conservative vanishing-gap coefficient was
`0.000256127176574...`; (AT.10) is larger by a factor greater than `50`.

## 5. Exact interpretation

Every extracted triple has one exact side and two asymptotically unit sides:

\[
|u-v|=1,
\qquad
|u-w|=1+o(1),
\qquad
|v-w|=1+o(1),
\]

with at least one of the last two distances strictly greater than one in every actual
triangle-free source.

Thus the low-residual branch is now quantitatively close to the forbidden object on a
macroscopic disjoint family:

```text
R_F=o(D)
  -> at least (0.0128557418...-o(1))D vertex-disjoint
     almost-unit equilateral triples
  -> each triple already contains one exact unit contact edge.
```

This is stronger than a generic hidden-near-contact matching because both missing
constraints of the target unit triangle are simultaneously near-active around one
already-active contact.

## 6. Scope and remaining gate

- This theorem changes only the extraction step.  It inherits the compactness-based
  anchored Groemer theorem and does not produce a quantitative modulus in `eta`.
- The third vertex `w` may be an assigned isolate or another positive-core boundary
  vertex.  No isolated-point activation theorem is applied.
- Pairwise vertex-disjointness prevents interactions through shared source variables,
  but it does not by itself show that all triples can be simultaneously activated.
- Near-unit constraints do not automatically acquire positive KKT weight after
  activation.
- No source-preserving strict diameter decrease is constructed here.

The next useful target is now specific: use the KKT/global-minimality equations on a
linear disjoint family of contact-anchored almost-equilateral triples to prove either
one exact activation or a simultaneous feasible perturbation that decreases the global
diameter.

C-II and Level I remain open.

---

**Recovery provenance:** copied from `research/c2-closure-sol-20260914-r7` at exact tip `1541dac85e9ddf6450bb3cd7b14f5ce76e119420` during the 2026-10-04 Slot 2 branch audit. This recovered claim remains unreviewed and noncanonical.
