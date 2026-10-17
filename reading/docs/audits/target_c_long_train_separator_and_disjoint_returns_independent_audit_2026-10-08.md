> Generated reading edition · [exact source](../../../docs/audits/target_c_long_train_separator_and_disjoint_returns_independent_audit_2026-10-08.md) · source SHA-256 `943d36eeab06ec027fbac20f90ebd0051b63a6170f5bf8958004c386f1330d69`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4110538FF870","canonical":true,"claim_ids":["C-CORE-UNLOADED-SEPARATOR-AREA-BOUND","C-LONG-TRAIN-SEPARATOR-INEQUALITY","C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS"],"claim_statuses":{"C-CORE-UNLOADED-SEPARATOR-AREA-BOUND":"canonical","C-LONG-TRAIN-SEPARATOR-INEQUALITY":"canonical","C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.180 — long-train separators and disjoint full-source returns

Date: 2026-10-08  
Audit base: `origin/main=b673b9096416452b01eb013237f6d67beb231516`, state `2026-10-08.audit.175`  
Frozen source: `origin/research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`  
Classification: independent reconstruction; **PASS — promote the separator bound, train inequality, and positive-bulk corollary at the exact scopes below**.  
Target: C-II. C-II and Level I remain open.

The audited claims are Section 7, equations CB11--CB13, of the frozen source report `docs/reports/target_c_train_cut_hull_bank_2026-10-08.md`, SHA-256 `15e2530cbae69f6c43cf0d8dea664e626ded9ce80b216dbccf9d1c98de9d58e9`.
The exact-rational finite checker is `research/verify_target_c_train_cut_hull_bank_2026_10_08.py`, SHA-256 `fa8e9b25abf7949c61cc77a4ff27e9ee9e486442a885a57ee52a5d3aab86a9c0`.

## Starting endpoint and implication chain

Audit.179 had promoted a linear bank of long complete trains inside a common `o(D^2)`-edge contact carrier, but that carrier could reuse bottlenecks. This audit checks the separate source-global bridge:

```text
canonical mixed rigidity and positive unloaded equilibrium
  -> quadratic area bound behind any loaded separator
  -> long-train separator inequality
  -> linearly many vertex-disjoint actual contact returns
```

Dependencies used as canonical inputs are `C-ZRF` / `C-MIXED-CORE-FINITE-RIGIDITY` (Section 57), `C-RHOMBUS-POP`, `C-TRAIN-INTERFACE-CURRENCY`, `C-LOADED-HULL`, `C-TRAIN-CUT-HULL-BANK`, and `C-QUADRATIC-CORE-TRAIN-BANK`. Theory 01, Lemma 10.1 and Theorems 10.6 and 10.8 supply the actual rhombus-track geometry and monotone transverse progress. Audit.131 supplies the occurrence-counted train total used in the asymptotic selection. No audited-working or unreviewed theorem is used.

## Exact promoted claims

Let `A` be a canonical contact-minimal, then actual-diameter-pair-minimal, triangle-free global minimizer in the Section-57 mixed-rigidity scope, with `D>=9`. Let `V` be its nonisolated positive-contact core, `C=C_*` its positive unit-contact graph, and `B` the actual selected loaded set. All contact-isolated source points remain in `A`; the graph claims below concern only `V`.

**`C-CORE-UNLOADED-SEPARATOR-AREA-BOUND` (CB12).** For any terminal set `X subset V` and endpoint-inclusive vertex separator `S subset V`, `|S|=k`, between `X` and `B`, let `U` be the union of components of `C-S` meeting `X-S`. Then

$$
|U|\le {16\over\pi^2}k^2+{8\over\pi}k.
$$

**`C-LONG-TRAIN-SEPARATOR-INEQUALITY` (CB11).** For any `a` distinct complete physical tracks of strict unit rhombi, each of degree at least an integer `L>=1`, choose one rail endpoint for each train. If `k` is the minimum endpoint-inclusive `C`-vertex separator from the resulting terminal set to `B`, then

$$
(a-5k)_+(L+1)\le {80\over\pi^2}k^2+{40\over\pi}k.
$$

In particular Menger's theorem gives `k` mutually vertex-disjoint actual contact paths from distinct chosen train terminals to distinct loaded vertices, with paths counted in the full positive-contact graph `C`.

**`C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS` (CB13).** Along any unbounded sequence in the same canonical source scope with `R4/D^2 -> r>0`, fix `epsilon in (0,r)`, and put

$$
a_*={2\over3}\sqrt{r-\epsilon},\qquad \ell={\epsilon\over3\pi}.
$$

For the long bank from Audit.179, the minimum separator size obeys

$$
\liminf {k\over D}\ge {\pi^2\over32}
\left(\sqrt{\ell^2+{64a_*\ell\over5\pi^2}}-\ell\right)>0.
$$

Thus a linear-size subfamily of long bank trains has mutually vertex-disjoint actual-contact returns to distinct loaded vertices. The coefficient is for fixed `epsilon`; it is not uniform as `epsilon` tends to zero.

## Independent proof reconstruction

### Separator area bound

Fix a component `U_j` of `C-S` meeting `X-S`, with `n_j` vertices, `e_j` internal contact rows, and `t_j` contacts to `S`. It contains no loaded vertex. A velocity supported on `U_j` that is annihilated by its `e_j+t_j` contact rows extends by zero to a mixed active flex on `V`: there is no diameter row incident to `U_j`, and every contact leaving `U_j` ends in `S`. Section 57 says this flex is Euclidean. Since all loaded vertices are outside `U_j` and the canonical loaded set has at least six distinct vertices for `D>=9`, the Euclidean flex vanishes. Therefore the restricted contact matrix has full column rank `2n_j`.

Positive full-support equilibrium gives a nonzero dependence among those same rows when restricted to the `U_j` columns: sum each contact row with its positive KKT coefficient, and equilibrium cancels every `U_j` coordinate. Thus

$$
e_j+t_j\ge 2n_j+1.
$$

This is a pinned-rank deduction from canonical mixed rigidity and stress, not a generic planarity inference.

Put `K=C[U union S]`, and let `c_U,c_K` count the components of `C[U]` and `K`; let `e_S` count edges internal to `S`. The graph is a simple triangle-free plane contact graph. If `b_K` is the total outer-face boundary-walk length, with repetitions, and `Q_K` is the sum of bounded-face excesses `deg(F)-4`, Euler's formula gives

For disconnected `K`, “total outer-face boundary-walk length” means the sum of the outer boundary-walk lengths of its connected components, each considered as a plane graph by itself. Likewise, `Q_K` sums bounded-face excesses componentwise. This convention matters when the drawing has nested components: it is not merely the boundary walks incident with the single global unbounded face. Applying connected Euler to each component and summing gives the displayed identity.

$$
b_K+Q_K=4(|U|+k)-2|E(K)|-4c_K
\le4k-2c_U-4c_K-2e_S\le4k.
$$

The equality uses bounded facial walks of degree at least four; it also covers bridge edges, disconnected graphs, and isolated separator vertices. Every component of `K` contains a separator vertex. Otherwise it would be a closed component of the positive-contact core with no loaded vertex, and dotting its positive equilibrium equations with the source positions would give `sum_e alpha_e |p_i-p_j|^2=0`, impossible for a nonempty contact component. Hence `c_K<=k`.

For each component `K_j` of `K`, let `p_j,A_j` be the perimeter and area of its convex hull. The unit disks of radius `1/2` about its source vertices have disjoint interiors and lie in the hull's radius-`1/2` parallel body. Steiner's formula, the planar isoperimetric inequality, and `p_j<=b_j` give

$$
|V(K_j)|\le {p_j^2\over\pi^2}+{2p_j\over\pi}+1.
$$

Summing, using `sum p_j<=b_K<=4k` and `c_K<=k`, yields `|U|+k<=16k^2/pi^2+8k/pi+k`, hence CB12. Degenerate point and segment hulls obey the same parallel-body formula.

### Train inequality and Menger

At a source vertex, six distinct unit neighbors would have all six circular gaps at least `pi/3`; equality throughout would create unit triangles. Triangle-freeness therefore gives contact degree at most five. If a train rail contains a vertex inside one of its rhombi, that vertex is incident to one of the parallel unit sides defining the train track. Assign the rail to that incident track edge. Distinct tracks contain disjoint edge classes, so distinct rails through the vertex receive distinct incident contacts. The same assignment works at a join between consecutive rhombi. Thus at most five different train rails pass through any source vertex.

Each rail has one actual contact edge per rhombus and its transverse coordinate increases strictly by `sin(theta)>sqrt(3)/2` per rhombus. It has at least `L+1` distinct vertices. A separator of size `k` meets at most `5k` chosen rails. Every remaining rail starts outside `S` and lies in a component counted by `U`. Counting rail vertices with multiplicity at most five gives

$$
(a-5k)_+(L+1)\le5|U|.
$$

CB12 gives CB11. The endpoint-inclusive vertex-split form of Menger's theorem identifies `k` with the maximum number of vertex-disjoint `X`-to-`B` paths. The paths have distinct start vertices. Since each train contributed exactly one chosen start, assign each path to one train with that start; these are distinct trains. All path edges are actual positive unit contacts.

The path-count statement is endpoint-inclusive: if a chosen terminal already belongs to `B`, Menger may pair that vertex to itself by a zero-length path. If `X` and `B` are disjoint, all the paths are nontrivial. The separator inequality itself does not require this disjointness, and no positive path-length bound is claimed.

### Positive-bulk corollary

The exact train-occurrence identity gives `T=q-k_0+2f`, where `k_0=d_H+s_Z`; using `f<=Q`, `b>=q`, and `b+Q=2(q-k_0)` gives `T<=3q`. The loaded hull has `q<=pi D`, so `T<=3pi D`. With `L=floor(epsilon D/(3pi))`, all trains below threshold account for at most `LT<=epsilon D^2` rhombus incidences. The train-crossing graph has `R4` edges and is triangle-free. Removing short trains deletes at most `LT` crossings; Mantel gives at least `2 sqrt((r-epsilon)D^2+o(D^2))` long trains. Audit.179's canonical one-third bank then gives `a>=(a_*-o(1))D` long bank trains.

Divide CB11 by `D^2` along a subsequence attaining the liminf of `k/D`. If that ratio is unbounded, the claimed bound is immediate. Otherwise, with `a/D>=a_*-o(1)` and `(L+1)/D>=ell`, any limiting `x=k/D<a_*/5` satisfies

$$
\ell(a_*-5x)\le {80\over\pi^2}x^2.
$$

Solving the quadratic gives the displayed constant. If `x>=a_*/5`, the same lower bound follows because the positive root is smaller than `a_*/5`. Menger yields the disjoint returns.

## Hostile checks and exact computational scope

- The proof keeps the core/full-source distinction explicit. Contact isolates remain in the global configuration and in unit-separation assumptions; they are not inserted into the positive-contact separator graph or deleted by a motion.
- The rank step uses `D>=9`, canonical full mixed-core rank, and positive relative-interior contact stress on `C=C_*`. A geometric packing, a pinned scaffold, or generic planar rank alone does not supply it.
- The verifier was inspected and rerun at the frozen source snapshot. It uses exact rational coordinates and `Fraction` arithmetic; it checks 10 nonglobal fixtures, 13,259 source lower pairs, 164 physical train rails, 506 selections, 27 endpoint-inclusive flow/min-cut instances, and 113 vertex-disjoint returns. The pinned-count antecedent passes in 3 and fails in 24 fixtures. For cases where it passes, it checks the finite separator/packing bounds with weaker constants obtained from `pi>3`.
- This computation does not encode KKT equilibrium, the mixed-rigidity theorem, the analytic separator-area proof, or the asymptotic `R4/D^2 -> r` argument. The 24 antecedent failures show why the theorem cannot be generalized to nonglobal contact fixtures. The finite tests support the encoded implications only.
- Audit.168's common-trunk paths are a nonglobal regression and do not meet the mixed-rigidity/full-support hypotheses. Audit.179's carrier may still reuse bottlenecks: CB13's disjoint paths are in the full graph and need not stay inside that carrier. There is no contradiction between the results.
- These claims provide no path-length bound, no face/interface payment, no simultaneous displacement, no strict diameter improvement, and no same-cardinality competitor.

## Verdict and frontier effect

**PASS — promote all three exact claims above.** CB12 bounds the number of core vertices behind an endpoint-inclusive loaded cut; CB11 converts train length and cut size into a quantitative inequality; CB13 gives linear vertex-disjoint returns from a quadratic strict-rhombus bulk without cap extraction. This strictly strengthens the available source-global return structure. The remaining C-II endpoint is still a full-source finite-move or discrete replacement that checks every lower and actual-diameter upper constraint and produces strict contact loss at diameter `D` or a strict sub-`D` competitor. No branch is closed, and Level I remains open.

## Promotion recommendation

Promote with state version `2026-10-08.audit.176`, the Target C current-frontier entry, the theorem dependency registrations, and regenerated artifact/state views. Refresh the active prompt to replace its cap-only description of quadratic-bulk disjoint returns with the new canonical CB13 scope and limitations. Do not register the finite fixture checker as a proof certificate: it is supportive regression evidence, not a verifier of the analytic or asymptotic theorem.
