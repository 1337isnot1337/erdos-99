<!-- theorem-state: {"artifact_id":"ART-AB8493A5CDE7","canonical":true,"claim_ids":["C-CORE-UNLOADED-SEPARATOR-AREA-BOUND","C-LONG-TRAIN-SEPARATOR-INEQUALITY","C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS"],"claim_statuses":{"C-CORE-UNLOADED-SEPARATOR-AREA-BOUND":"canonical","C-LONG-TRAIN-SEPARATOR-INEQUALITY":"canonical","C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.235 — Oler-sharpened separator and return bounds

Date: 2026-10-10. Audit base: `origin/main=27fbc92b7c1e51bc6b418b90687afc6c73a66071`, state `2026-10-10.audit.228`.

Frozen candidate: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`. The audited source is Section 18 of [`target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`](../reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md), SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`. The frozen branch and report were not modified.

## Verdict

**PASS — sharpen three existing canonical claims.** The exact Oler inequality improves the separator population bound, the resulting long-train cut inequality, and the positive-bulk linear return constant. These are refinements of `C-CORE-UNLOADED-SEPARATOR-AREA-BOUND`, `C-LONG-TRAIN-SEPARATOR-INEQUALITY`, and `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS`; no duplicate theorem IDs are needed.

The result only strengthens a necessary separator/return budget. It does not give positive individual path lengths, a source motion, a payment against exceptional faces, a strict diameter improvement, or C-II closure. Contact-isolated labels remain in the full source and are not included in the bounded core population.

## Exact scope and promoted statements

Use the exact canonical source scope of Audit.180: a contact-minimal, then actual-diameter-pair-minimal triangle-free C-II global minimizer with `D>=9`; `V` is its nonisolated positive-contact core, `C=C_*`, `B` is the selected actual loaded set, and every source point, including each contact isolate, remains in the global configuration. Let `X subset V`, let `S subset V` be any endpoint-inclusive vertex separator from `X` to `B`, and write `k=|S|`. Let `U` be the union of components of `C-S` meeting `X-S`.

Set `K=C[U union S]`. Let `c_U` be the number of components of `C[U]`, `c_K` the number of components of `K`, `e_S` the number of contact edges internal to `S`, and `Q_K` the sum, over bounded faces of each component of `K`, of `deg(F)-4`. Let `b_K` be the sum of the exterior facial-walk lengths of the components of `K`, each embedded and counted separately, with bridge traversals repeated. Define

\[
b_* = 4k-2c_U-4c_K-2e_S-Q_K.
\]

The sharpened `C-CORE-UNLOADED-SEPARATOR-AREA-BOUND` is

\[
\boxed{|U|\le {b_*^2\over4\pi a_0}+{b_*\over2}+c_K-k},
\qquad a_0={\sqrt3\over2},
\]

and in particular

\[
\boxed{|U|\le {8\over\pi\sqrt3}k^2+2k.}
\]

For the same source and graph, let there be `a` distinct complete physical strict-rhombus trains, each of degree at least an integer `L>=1`, with one rail endpoint selected per train. Let `k` now be the minimum endpoint-inclusive positive-contact vertex separator from those selected terminals to `B`. The sharpened `C-LONG-TRAIN-SEPARATOR-INEQUALITY` is

\[
\boxed{(a-5k)_+(L+1)\le {40\over\pi\sqrt3}k^2+10k.}
\]

Menger gives `k` mutually vertex-disjoint actual positive-contact paths from distinct selected train terminals to distinct loaded vertices. The paths remain endpoint-inclusive and can have length zero if a selected terminal is already loaded.

For an unbounded sequence in the canonical `C-QUADRATIC-CORE-TRAIN-BANK` scope with `D\to\infty` and `R_4/D^2\to r>0`, fix `epsilon in (0,r)` and set

\[
a_*={2\over3}\sqrt{r-\epsilon},\qquad
\ell={\epsilon\over3\pi},\qquad
\beta={40\over\pi\sqrt3}.
\]

The sharpened `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS` bound is

\[
\boxed{\liminf {k\over D}\ge
{\sqrt{25\ell^2+4\beta a_*\ell}-5\ell\over2\beta}>0.}
\]

Here `k` is the minimum separator size for one selected endpoint from each train in the Audit.179 long bank. For every fixed `epsilon` the bound yields linearly many mutually vertex-disjoint paths in the full positive-contact graph; no bound uniform as `epsilon\downarrow0` is claimed.

## Independent reconstruction

### Exact componentwise Euler budget

Audit.180's pinned-rank argument applies unchanged to each component `U_j` of `C-S` meeting `X-S`. Since `S` separates `X` from `B`, `U_j` contains no loaded vertex, so no actual diameter row is incident to it. If `n_j=|U_j|`, `e_j` is its number of internal contacts, and `t_j` its number of contacts to `S`, then a contact-row null velocity supported on `U_j` extends by zero to a mixed active flex. Canonical mixed rigidity makes it Euclidean, and two distinct loaded vertices outside `U_j` pin that Euclidean motion to zero. Thus the restricted contact rows have rank `2n_j`. Positive full-support equilibrium supplies a nonzero row dependence on those coordinates, so

\[
e_j+t_j\ge2n_j+1.
\]

Summing over `j` and adding the `e_S` edges gives `|E(K)|>=2|U|+c_U+e_S`. The actual contact graph is simple, planar, and triangle-free. Hence every bounded facial walk has length at least four; with `Q_K` summed componentwise, disconnected Euler gives

\[
b_K+Q_K=4(|U|+k)-2|E(K)|-4c_K
\le4k-2c_U-4c_K-2e_S.
\]

Thus `0<=b_K<=b_*`. The nonnegativity of `Q_K` follows from the same triangle-free planar embedding. Every component of `K` meets `S`: a component containing only vertices of `U` would be a closed positive-contact component with no loaded vertex, contradicting positive equilibrium after dotting its force equations with the source positions. Components of `K` are vertex-disjoint and each contains a separator vertex, so `c_K<=k`.

### Oler bound for each component

For each connected component `K_j` let `P_j` be the convex hull of its source vertices, `p_j=per(P_j)`, and `b_j` its componentwise exterior-walk length. An exterior facial walk need not visit every interior vertex, but every extreme vertex of `P_j` is incident to the unbounded face: the open exterior sector beyond a supporting line lies in that face. Thus the exterior walk visits all vertices needed to determine `P_j`. Its length is at least the perimeter of their convex hull. Indeed, projection onto any direction has total variation at least twice the hull width, and Cauchy's perimeter formula integrates those widths. Therefore `p_j<=b_j`.

The canonical finite Oler inequality in shared theory 03, Section 21.1, applies to the unit-separated vertex set of `K_j` in `P_j`:

\[
|V(K_j)|\le {\operatorname{area}(P_j)\over a_0}+{p_j\over2}+1.
\]

It also applies to point and segment hulls under the degenerate perimeter convention. Isoperimetry gives `area(P_j)<=p_j^2/(4pi)`. Since the graph components partition `U union S`,

\[
|U|+k=\sum_j |V(K_j)|
\le {\sum_j p_j^2\over4\pi a_0}+{1\over2}\sum_jp_j+c_K
\le {b_K^2\over4\pi a_0}+{b_K\over2}+c_K.
\]

The function on the right is increasing for nonnegative `b_K`, and `b_K<=b_*`, proving the exact bound. Since `c_K<=k` and `b_*<=4k`, this implies

\[
|U|\le {16k^2\over4\pi a_0}+2k
={8\over\pi\sqrt3}k^2+2k.
\]

### Train inequality and asymptotic return constant

Audit.180's rail-incidence proof is unchanged: triangle-freeness bounds contact degree by five, at most five distinct train rails pass through any source vertex, and a degree-`L` train has at least `L+1` distinct vertices by strict transverse progress. A cut of size `k` meets at most `5k` selected trains; every remaining rail is contained in the counted components of `U`. Counting rail vertices with multiplicity at most five gives `(a-5k)_+(L+1)<=5|U|`. Substitution of the sharpened uniform bound proves the displayed coefficient `beta` and linear term `10k`. The canonical Audit.179 bank and the old train-occurrence argument still give `a/D>=a_*-o(1)` and `(L+1)/D->ell`.

To derive the new limiting constant, if `liminf k/D` is infinite the bound is immediate; otherwise pass to a subsequence attaining the finite value `x=liminf k/D`. If `x>=a_*/5`, then it exceeds the displayed positive root. If `x<a_*/5`, divide the train inequality by `D^2` to obtain

\[
\ell(a_*-5x)\le\beta x^2,
\]

which is equivalent to `x>=(sqrt(25ell^2+4beta a_*ell)-5ell)/(2beta)`. This is the positive root of `beta x^2+5ell x-ell a_*=0`; it is strictly below `a_*/5`, as required. Endpoint-inclusive Menger then gives the stated number of disjoint paths.

## Hostile checks and limits

- Oler is applied separately to the actual unit-separated vertices in each graph component. No disjointness of their convex hulls is assumed or needed; populations are summed, not hull areas.
- The componentwise exterior-walk convention handles nested graph components and repeated bridge traversals. Interior vertices of a connected component need not lie on its exterior walk, but its convex-hull extreme vertices do; this is the fact needed for `p_j<=b_j`. Replacing the componentwise convention with only the walks incident to one global unbounded face would not justify the Euler identity.
- The `c_K<=k` step requires excluding a closed unloaded core component. It follows from the canonical positive-equilibrium hypothesis, not from planarity alone.
- `U` counts only vertices in the nonisolated positive-contact core. Contact-isolated source labels are never deleted or bounded by this argument.
- The train conclusion is endpoint-inclusive. It does not assert positive path length, route cost, simultaneous motion, or an upper-diameter release.
- The asymptotic constant is for each fixed `epsilon in (0,r)` and is not uniform as `epsilon` tends to zero.
- No finite certificate encodes the analytic Oler or pinned-rank implications; none is claimed.

## Canonical disposition and frontier effect

Update the existing claims `C-CORE-UNLOADED-SEPARATOR-AREA-BOUND`, `C-LONG-TRAIN-SEPARATOR-INEQUALITY`, and `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS` with these stronger conclusions and this audit as their source. Dependencies remain canonical: mixed-core rigidity/`C-ZRF`/`C-LOADED-HULL` for the pinned count, the finite Oler inequality in shared theory 03, and the existing rhombus, train-interface, quadratic-bank, and loaded-hull claims for the two downstream consequences.

The frontier is unchanged. The sharpened budget still yields only linear many actual-contact returns from quadratic bulk. The open C-II obligation remains a full-source finite move or discrete replacement that checks every lower and actual-diameter upper constraint and produces strict contact loss at diameter `D` or a strict sub-`D` competitor. C-II and Level I remain open.
