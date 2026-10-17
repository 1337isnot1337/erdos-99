> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_static_packet_barrier_independent_audit_2026-10-07.md) · source SHA-256 `3e55eb4e54a619ac808207b9733d357a8dc76b619a9614dbf2dcbb455a4babe3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BDC0CB5E5AF4","canonical":true,"claim_ids":["C-EXTERIOR-STATIC-PACKET-BARRIER"],"claim_statuses":{"C-EXTERIOR-STATIC-PACKET-BARRIER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.110 — exterior static-packet barrier

**Date:** 2026-10-07

**Audit base:** `origin/main=482bcd59140a350f758720f87d3f7ec6936d8b8a`, tree `1a123e211c46a7c98a3703acc6e2c81a28991722`, state `2026-10-07.audit.109`

**Target:** C-II; C-I is closed, C-II and Level I are open

**External literature / computation:** not used

## 1. Frozen source and audited unit

The frozen Worker 2 source is `origin/research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`. This audit covers only Theorem E.6 in Section 6 of `docs/reports/target_c_exterior_packet_release_and_unloaded_core_cut_2026-10-06.md`, SHA-256 `6b8722e95d92cfc1c32f7bcc6d4ba5cd71f6138df657d73ce5be982d8299fa08`.

The antipodal cap pairing, loaded-only stress exclusion, unloaded-core transversal, and other claims in Sections 3–5 and 7 are not included in this verdict. The finite proof below is reconstructed from the theorem's exact pair hypotheses and canonical source normalization; it does not use those neighboring candidate results.

## 2. Exact theorem

Let `A` be a canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D=diam(A)≥9` and strong-support normalization `C=C_*`, `H=H_*`. Let `V` be its nonisolated positive-contact core, `Z=A\V` its contact isolates, and `F=conv(V)=conv(B)` its loaded force hull. Retain every source label not explicitly deleted.

Choose `R⊂A`, put `T=A\R`, and let `Y` be a finite packet with `Y∩T=∅` and `|Y|=|R|`. Assume the proposed source `A'=T∪Y` is unit-separated, every pair in `A'` with at least one endpoint in `Y` has distance strictly less than `D`, and `Y⊂R²\int(F)`. No triangle-free assumption is imposed on `A'`.

If `R` is incident to at least one old unit contact, or if `R` meets every old actual diameter pair, then no such packet exists. More precisely, keeping `V\R` fixed and allowing `Y∪(Z\R)` to move, there is a straight arbitrarily small finite motion that opens every unit contact of `A'` involving a free variable. The final contact graph is the induced old contact graph on `T`; every moving pair remains strictly below `D`. Thus the final source is triangle-free. In the first case it loses an old contact and contradicts contact minimality if its diameter stays `D`; in the second case it has diameter strictly below `D`.

The `Y` points may lie on the boundary of `F` and the proposed packet may initially contain unit triangles. The strict upper bounds on all pairs involving `Y` are required.

## 3. Independent reconstruction of the finite motion

Pin every retained positive-contact core vertex in `V\R`; let the free labels be `Y∪(Z\R)`. Let `E` be all unit pairs in `A'` that have a free endpoint. Old contacts between two retained core vertices are pinned and unchanged. Contact isolates have no old unit contacts. Therefore every edge in `E` is a new contact and is incident to `Y`.

For `e=ij∈E`, define the lower-distance row on free velocities by

$$
a_e(u)=(p_i-p_j)\cdot(u_i-u_j),
$$

with zero velocity at pins. Define `E_+` as the union of the supports of all nonnegative row dependencies

$$
\lambda_e\ge0,\qquad \sum_{e\in E}\lambda_e a_e=0.
$$

Because `E` is finite, summing one witness dependency for each edge of `E_+` gives a single dependency positive on every edge in `E_+`.

### Geometry of the supported rows

In each connected component of that positive-support graph, every free vertex is a positive weighted average of its support neighbors. A component without a pin would have constant coordinates by the finite maximum principle, which is impossible when it contains a unit edge. With pins present, the same maximum principle, applied to every linear functional, puts every free vertex of the component in the convex hull of its pins, hence in `F`.

Each supported edge is incident to a point of `Y`. Such a point is outside `int(F)` by hypothesis and inside `F` by the preceding convex-hull argument, so it lies on `∂F`. At that point choose a supporting line of `F`. Equality in the positive weighted-average relation puts every supported neighbor on this line. If the point is an extreme vertex, choose an exposing support line; its only point in `F` is the vertex itself, impossible for a unit neighbor. At the relative interior of a hull side, unit separation permits at most one unit neighbor in each direction along the line, and equilibrium requires both. Propagating this condition shows that supported edges form collinear unit chains on hull sides. The chains may meet at pinned vertices.

Every supported edge has a free endpoint, since it is in `E` and every edge of `E` is incident to `Y`. Moving a free endpoint perpendicular to its chain preserves all first-order supported-row equalities while changing its relative velocity across each incident supported edge. Thus, inside the kernel of the supported rows, the equality subspace `u_i=u_j` is proper for every `ij∈E_+`.

### Exact conic alternative and finite opening

For any `e∉E_+`, there is a velocity `u_e` with `a_f(u_e)≥0` for all `f∈E` and `a_e(u_e)>0`. Otherwise the finite Farkas alternative gives `-a_e` as a nonnegative combination of the rows, producing a nonnegative row dependency with positive coefficient on `e`, contrary to `e∉E_+`. Summing these velocities gives `u_0` with strictly positive derivative on every edge outside `E_+` and zero derivative on `E_+`: the latter follows by pairing each feasible velocity with the dependency positive on all supported rows.

Choose a vector `w` in the kernel of the supported rows and outside the finite union of the proper subspaces `w_i=w_j`, `ij∈E_+`. A sufficiently small perturbation of `u_0` in direction `w` preserves the positive derivatives on `E\E_+` and gives nonzero relative velocity on every edge in `E_+`. For the resulting velocity `u`, every initially unit free pair has exact squared-length change

$$
|p_i+tu_i-p_j-tu_j|^2-1
=2t\,a_{ij}(u)+t^2|u_i-u_j|^2>0\qquad(t>0).
$$

The inequality is first-order strict outside `E_+` and second-order strict on `E_+`. This is a finite straight motion; no first-order condition is being integrated without a second-order opening term.

All other lower pairs begin strictly above one, and all moving-pair upper constraints begin strictly below `D`. The strict isolate margins in the canonical normalization and the packet's strict new upper margins give one common positive slack over the finite pair list. A sufficiently small `t>0` preserves every inactive lower and upper constraint. Pinned contacts stay unit and all old actual diameter pairs not deleted are pinned. Every free-contact edge opens, so the final contact graph is exactly the induced old graph on `T` and is triangle-free.

If `R` removes an old contact, the induced graph has fewer contacts. If the resulting diameter is less than `D`, global optimality fails; otherwise it is another triangle-free global minimizer with fewer contacts. If `R` meets every old diameter pair, no retained pinned pair has length `D`; all moving pairs are strictly below `D`, so the resulting diameter is less than `D`. Both alternatives contradict canonical minimality.

## 4. Dependencies and scope

- `C-ZRF` supplies the nonisolated positive-contact core, the loaded-endpoint convention, and equilibrium at unloaded core vertices. `C-LOADED-HULL-CAP-BUDGET` supplies `V⊂F=conv(B)` and the positive-area loaded hull. These give the hull geometry used for the supported-row maximum principle.
- `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE` supplies strict `(1,D)` pair slack for contact isolates in the strong-support normalization. Contact isolates outside `R` are retained as moving variables; none is silently removed.
- `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` is the canonical finite contradiction endpoint after release. The release proof itself does not use KKT stresses of the original source, PSD, occupied-cap asymptotics, a packet wall shield, or Delaunay edges.
- This is a static replacement barrier for packets entirely outside the interior of `F`. It supplies no exterior packet, no interior capacity in `F`, and no movable-core construction. It does not close either exhaustive C-II branch or Level I.

## 5. Hostile checks and redundancy disposition

Checked packets strictly outside `F` and packets touching `∂F`; exposed hull corners and side-interior points; support components with no pins; several collinear chains meeting at pinned vertices; retained isolates that lie on or off the loaded hull; unit contacts between packet sites and between packets and retained isolates; initially triangular packets; inactive lower pairs and every strict upper pair involving moving labels; and the case where `R` removes the last actual diameter pair. Exterior stressed endpoints are excluded by the maximum principle; boundary stressed endpoints reduce to straight chains, whose contacts open at second order. No counterexample to the narrowed claim was found.

The Audit.109 one-site saturation theorem is a direct special case: choose `R` to delete one positive-contact vertex and `Y={r}`. Its claim remains mathematically valid, but this broader theorem makes the one-site ID redundant; the promotion transaction marks `C-EXTERIOR-ONE-SITE-SATURATION` superseded by `C-EXTERIOR-STATIC-PACKET-BARRIER`.

**Verdict: PASS — promote `C-EXTERIOR-STATIC-PACKET-BARRIER`.** It rules out an equal-cardinality, strict-upper, unit-separated static replacement packet outside the interior of the loaded hull whenever the replacement deletes old contact or covers every old diameter pair. It creates no packet or capacity and does not change Target C's endpoint.
