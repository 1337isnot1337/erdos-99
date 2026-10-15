<!-- theorem-state: {"artifact_id":"ART-2B737E3D9B5F","canonical":true,"claim_ids":["C-MIXED-CORE-ONE-ROW-REDUNDANCY","C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY","C-TWO-PUNCTURE-LOADED-ANCHORING"],"claim_statuses":{"C-MIXED-CORE-ONE-ROW-REDUNDANCY":"canonical","C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY":"canonical","C-TWO-PUNCTURE-LOADED-ANCHORING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: mixed-core connectivity and two-puncture loading

Date: 2026-10-07. Audit base: `origin/main=37bb586eacfc612f78a5082f890f2577f4daaac9`, state `2026-10-07.audit.117`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source report `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`.

## Verdict

**PASS — promote** `C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY`, `C-TWO-PUNCTURE-LOADED-ANCHORING`, and `C-MIXED-CORE-ONE-ROW-REDUNDANCY`. The source's Theorems 2–4 are valid under the canonical source hypotheses. Corollary 4.1, stated below, is included with the connectivity theorem. No other claim in the source report was audited here.

## Exact statement and scope

Let `A` be the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`. Let `V` be its nonisolated positive-contact core. Let `C` be **all** actual unit-contact edges on `V`, let `H` be **all** actual diameter edges, and put `G=(V,C union H)`. Every endpoint of an actual diameter edge belongs to `V` by the canonical relative-interior stress theorem. Let `B` be the set of those endpoints. The core affinely spans the plane and `|B|>=3` because the actual loaded force hull is two-dimensional.

The promoted claims are:

1. `G-S` is connected for every `S subset V` with `|S|<=2`.
2. For each such `S`, every connected component of the contact graph `(V minus S, C minus S)` contains a vertex of `B minus S`.
3. If `V=X disjoint union Y` has exactly one crossing contact `ab` (`a in X`, `b in Y`) and both `X minus {a}` and `Y minus {b}` are nonempty, some actual diameter edge joins these two remainders. Otherwise deleting `a,b` disconnects `G`, contrary to claim 1.

These statements concern the mixed graph on `V`. Contact-isolated labels remain in the global source but are outside this graph theorem. The result does not find a contact separator, a physical train/face cut, or a source move.

The mixed rigidity matrix on `V` has rank `2v-3`, and deleting any one row corresponding to an actual edge of `C union H` leaves the rank `2v-3`. This does not assert that deleting two or more rows preserves rank.

## Independent reconstruction of three-vertex connectivity

The proof uses canonical `C-ZRF` for the core-scoped ZF fact (every infinitesimal flex of the full actual mixed bar graph on `V` is Euclidean) and the two-dimensional span of `V`. It also uses the newly canonical finite theorem `C-MIXED-CORE-FINITE-RIGIDITY`, which converts exact length preservation on every edge of `C union H` into congruence of the core.

- **No deletion.** If `G` were disconnected, choose a component whose complement contains at least two vertices; such a component exists since `|V|>=3` (because `|B|>=3`). Translate it with nonzero velocity and set all other velocities to zero. This is an infinitesimal bar flex because there is no crossing edge. It fixes two distinct vertices outside the component and moves a vertex, so it is not Euclidean, contradicting ZF.
- **One deleted vertex `s`.** If `G-s` were disconnected, rotate one component infinitesimally about `P_s` and set all other velocities to zero. Edges inside the component preserve length to first order; every edge from it to `s` is tangent to this rotation; no edge joins it to another component. The flex fixes `s` and a distinct vertex in another component, yet moves a vertex, so it is non-Euclidean and contradicts ZF.
- **Two deleted vertices `s,t`.** They are distinct source points; let `L` be their line. Every component `W` of `G-{s,t}` has a vertex off `L`. Indeed, if all vertices of some `W` lay on `L`, move one vertex of `W` perpendicularly to `L` and keep all others fixed. Every active bar incident to that vertex has its other endpoint on `L`, so the velocity is a bar flex. Its fixed vertices include `s,t` and an off-line core vertex (the core spans the plane), making it non-Euclidean, again contradicting ZF.

  Now reflect one component `W` across `L`, leaving every other vertex fixed. Edges within `W` retain length, edges from `W` to the deleted set end at `s` or `t` on the reflection axis, and no edge joins `W` to another component. Thus every edge of the actual mixed graph retains its exact length. A second component has an off-line vertex by the preceding argument; that vertex and `s,t` are three noncollinear fixed points, while an off-line vertex of `W` moves. The placement is not congruent to the source. This contradicts `C-MIXED-CORE-FINITE-RIGIDITY`.

The argument checks the full actual `C union H` edge set. It does not replace it with selected stressed edges. The finite reflection step is essential: ZF alone is only infinitesimal and would not rule out a two-triangle hinge framework, whose two triangles can be reflected across their shared edge. That generic hinge lacks the canonical finite-rigidity hypotheses.

## One-row redundancy

The canonical mixed rigidity matrix has rank `2v-3` by `C-ZRF`. In the canonical relative-interior stress, every actual contact and diameter coefficient is strictly positive. Equilibrium therefore gives a row dependence on the full actual rigidity matrix with a nonzero coefficient on every row (with opposite signs for the two edge classes). Solving this dependence for any chosen row expresses that row as a linear combination of all the others. Deleting any one row leaves the row span, and hence the rank, unchanged. This argument applies separately to each single row; it gives no simultaneous redundancy for a packet of rows.

## Two-puncture loading

Fix `S subset V`, `|S|<=2`, and a component `W` of the contact graph after deleting `S`. Suppose `W` contains no vertex of `B minus S`. No actual diameter edge can be incident to `W`, because every such edge has an endpoint in `B`. By the definition of contact component, no contact edge joins `W` to another vertex of `V minus S`. Hence `W` is a component of `G-S`. Since `|B|>=3`, the set `B minus S` is nonempty and lies outside `W`, contradicting three-vertex connectivity. Therefore every punctured contact component contains an actual diameter endpoint.

For Corollary 4.1, if no actual diameter joins `X minus {a}` to `Y minus {b}`, then deleting `a,b` removes the unique crossing contact and leaves no crossing diameter edge. The two nonempty remainders are disconnected in `G-{a,b}`, which is impossible.

## Adversarial scope and regression checks

- The graph in each claim is the actual mixed graph on the nonisolated core; no scaffold, stress subgraph, or graph on the full source with isolates silently replaces it.
- `H` is the full actual diameter set, not an arbitrary subset. Canonical full support puts every actual diameter endpoint in `V`.
- `B minus S` is nonempty for every permitted puncture because the loaded force hull is two-dimensional and `|B|>=3`.
- The shared-edge two-triangle hinge is a regression against deriving finite rigidity from infinitesimal rigidity alone. The proof avoids that invalid inference by invoking the independently promoted PSD finite-rigidity theorem.
- The source report's finite verifier checks examples for its Theorem 1 only. No executable certificate checks the universal graph/matrix claims in Theorems 2–4; the conclusions here follow from the analytic reconstruction above, not from sampled instances.

## Dependencies and disposition

| Claim | Verdict | Canonical dependency |
| --- | --- | --- |
| Three-vertex connectivity of the actual mixed core graph | PASS — promote `C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY` | `C-ZRF`; `C-MIXED-CORE-FINITE-RIGIDITY` |
| Two-puncture loading of every contact component | PASS — promote `C-TWO-PUNCTURE-LOADED-ANCHORING` | `C-ZRF`; `C-MIXED-CORE-THREE-VERTEX-CONNECTIVITY` |
| One-row redundancy of the full mixed rigidity matrix | PASS — promote `C-MIXED-CORE-ONE-ROW-REDUNDANCY` | `C-ZRF` |
| Source report's incidence theorem, move-energy and interpolation claims, and remaining regressions | Not audited in this cycle; lifecycle unchanged | None assigned |
| C-II and Level I closure | NOT CLAIMED; both remain open | — |

The claims strengthen the canonical description of the source graph but do not change the active C-II endpoint. In particular, they supply no source-level cut certificate or strict sub-`D` competitor.
