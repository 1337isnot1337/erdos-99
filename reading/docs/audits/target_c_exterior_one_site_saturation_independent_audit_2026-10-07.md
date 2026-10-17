> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_one_site_saturation_independent_audit_2026-10-07.md) · source SHA-256 `f9be133ac75dadb9e468745495f6c225b8d9e253593930e97c2edd92aa9bed40`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-45BF47F5B725","canonical":false,"claim_ids":["C-EXTERIOR-ONE-SITE-SATURATION"],"claim_statuses":{"C-EXTERIOR-ONE-SITE-SATURATION":"superseded"},"index":"docs/state/artifact-index.jsonl","status":"superseded","target":"target-c"} -->
# Target C Audit.109 — exterior one-site saturation

**Date:** 2026-10-07

**Audit base:** `origin/main=dfd3bdc69708b0ba23f535338e3f747d61d39d29`, tree `9ba5559f3e7aa6c41cc453bbc754922bbbe8606f`, state `2026-10-07.audit.108`

**Target:** C-II; C-I is closed, C-II and Level I are open

**External literature / computation:** not used

## 1. Frozen source and audited unit

The frozen Worker 1 source is `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82`. The claim is Section 5 of `docs/reports/target_c_coupled_delaunay_transfer_for_arbitrary_convex_containers_2026-10-07.md`, SHA-256 `85cb5d5dc25cf908219962f7d1bcd936ef16405af065f0cd2797dc103e8f8ab6`.

This claim is audited independently of the preceding Delaunay crop theorem. The proof uses canonical C-II source minimality and a finite source exchange; it does not use Delaunay estimates.

## 2. Exact theorem

Let `A` be a contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer, with `D=diam(A)≥9`, in the strong-support normalization `C=C_*`, `H=H_*`. Let `V` be its nonisolated positive-contact core and `F=conv(V)`. Retain every source point, including all contact isolates.

There is no new point `r∉A` with `r∉int(F)` such that

$$
1\le |r-x|<D\qquad\text{for every }x\in A.
$$

Consequently, for every unit-separated extension `P⊃A`, each auxiliary point in `P∩conv(A)` lies in `int(F)`. Since `F` is the convex hull of the loaded endpoints in this normalization, no auxiliary point is added in a closed exterior cap contained in `conv(A)` outside `int(F)`.

The strict upper hypothesis is part of the theorem. It makes no claim about an inserted point already at distance `D` from a retained source point.

## 3. Independent reconstruction of the finite exchange

Under `C=C_*`, `H=H_*`, every old unit contact belongs to the positive contact support; every source point outside `V` is a contact isolate, and every actual diameter endpoint belongs to `V`. At each unloaded core vertex, equilibrium expresses its position as a positive weighted average of its contact neighbors. The positive-contact components are grounded at loaded vertices, so the finite maximum principle gives `V⊆conv(B)`, where `B` is the loaded set. Since `B⊆V`, this yields `F=conv(B)`; the canonical loaded-hull theorem gives positive area.

Because `r∉int(F)`, convex separation supplies a unit vector `u` such that

$$
(r-x)\cdot u\ge0\qquad(x\in V).
$$

Choose a vertex `v∈V` incident to a positive unit contact, delete it, and insert `r(t)=r+tu`. For every old contact isolate `z` with `|r-z|=1`, also move that isolate by

$$
z(t)=z+t\bigl(u+z-r\bigr),
$$

and keep every other retained point fixed. All old labels outside `v` remain in the source.

Check the full pair list:

- For a retained core point `x∈V\{v}` with `|r-x|=1`, the squared distance changes by `2t(r-x)·u+t²|u|²>0`. If `|r-x|>1`, strict lower slack persists. The hypothesis `|r-x|<D` gives strict upper slack in either case.
- If `|r-z|=1` for a contact isolate `z`, then `r(t)-z(t)=(1+t)(r-z)`, so this new unit pair opens. Other `r`-to-isolate pairs have strict lower slack and, by hypothesis, strict upper slack.
- Every old pair involving a contact isolate starts strictly between `1` and `D`: isolates have no old unit contacts and are not actual diameter endpoints. There are finitely many such pairs, so one sufficiently small positive `t` preserves all their lower and upper constraints simultaneously, including isolate-to-isolate pairs.
- All retained core-to-core pairs are unchanged. This includes every old contact and every old actual diameter pair not incident to `v`. Deleting `v` removes at least one contact.

Thus for sufficiently small positive `t`, all constraints hold, every new `r`-involving unit pair has opened, and no new diameter pair appears. The resulting contact graph is a subgraph of the old one with the edges incident to `v` removed. It remains triangle-free and has strictly fewer unit contacts.

If the new diameter is less than `D`, global minimum-diameter optimality is contradicted. If it equals `D`, contact minimality is contradicted. This is a finite perturbation of the full source, including the required isolate motions; it does not infer finite feasibility from first-order data alone.

## 4. Hull-interior corollary

Let `K=conv(A)`, and let `r∈(P∖A)∩K` for a unit-separated extension `P⊃A`. The point `r` is not a vertex of `K`, because every vertex of the finite hull `K` belongs to `A`. Thus `r` is a nontrivial convex combination of distinct vertices `a_j∈A`. For each fixed `x∈A`, strict convexity of `y↦|y-x|²` gives

$$
|r-x|^2<\sum_j\lambda_j|a_j-x|^2\le D^2.
$$

Unit separation gives `|r-x|≥1`. The one-site theorem therefore forces `r∈int(F)`. This applies to the common saturated Delaunay completion in Audit.108, but it creates no site or capacity inside `F`.

## 5. Dependencies, scope, and adjacent Worker 2 result

- `C-ZRF` supplies the canonical positive-contact core, loaded diameter endpoints, and equilibrium on unloaded core vertices. `C-LOADED-HULL-CAP-BUDGET` supplies the canonical inclusion of the positive-contact core in the loaded hull and its positive-area scope. `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE` records the strict pair-slack neighborhood of contact isolates under `C=C_*`, `H=H_*`. The strong-support normalization is necessary: it ensures source points outside `V` are contact isolates, so no weak old unit pair is omitted from the motion check.
- Contact isolates are not deleted. Isolates at unit distance from `r` receive explicit velocities; all other isolate-involving pairs retain strict old margins for one common sufficiently small `t>0`.
- Worker 2's unreviewed Theorem E.6 treats multi-site packets under a common half-plane separation condition for packet sites relative to all retained source points. It is related but is neither imported nor promoted here. This one-site proof separates `r` from the positive-contact core and explicitly moves isolates that may lie across the support line.
- The claim says nothing about new sites outside `K`, moving retained core labels, exact new diameter pairs, or a replacement packet paying quadratic interior population.

## 6. Adversarial checks and verdict

Checked the boundary case `r∈∂F`, tangent unit pairs with zero first variation, multiple isolates at unit distance from `r`, every changed isolate-to-source and isolate-to-isolate pair, deletion of the last diameter pair, and the distinction between contact isolates and weak unit contacts. A support line handles boundary `r`; the `t²|u|²` term opens tangent core contacts; finite strict margins handle all moved-isolate pairs. The strong-support normalization rules out unhandled weak old contacts outside `V`. No counterexample to the stated scope was found.

**Verdict: PASS — promote `C-EXTERIOR-ONE-SITE-SATURATION`.** It rules out one unit-clear point with strict upper slack outside the canonical positive-contact hull, and therefore excludes auxiliary Delaunay sites from the specified closed exterior caps inside the old source hull. It supplies no refill, spare site, source-capacity theorem, finite packet, or change to the C-II/Level I endpoint.
