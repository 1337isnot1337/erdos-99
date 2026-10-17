> Generated reading edition · [exact source](../../../docs/audits/target_c_residual_cage_release_refill_independent_audit_2026-10-07.md) · source SHA-256 `d65f22d7de1f31553a6918b0480bbd3ce493f89db9a5bd7b7f2ab87f38a2aea8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DC3C5AB427A8","canonical":true,"claim_ids":["C-POSITIVE-CIRCUIT-STRICT-DIRECTION-TRANSVERSAL","C-POSITIVE-SPANNING-DELETION-REGRESSION","C-RESIDUAL-CAGE-RELEASE-REFILL","C-RESIDUAL-CAGE-TOPOLOGY-COST-REGRESSION"],"claim_statuses":{"C-POSITIVE-CIRCUIT-STRICT-DIRECTION-TRANSVERSAL":"canonical","C-POSITIVE-SPANNING-DELETION-REGRESSION":"regression","C-RESIDUAL-CAGE-RELEASE-REFILL":"superseded","C-RESIDUAL-CAGE-TOPOLOGY-COST-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: residual-cage release and strict refill

Date: 2026-10-07. Audit base: `e8e040e86bebe6cb2bfd191dbc8d6d99c6e366f2`, state `2026-10-07.audit.85`, Target C C-II open. Frozen source: PR #722 branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: `docs/reports/target_c_residual_cage_release_refill_2026-10-05.md`.

## Verdict

**PASS — already subsumed for the source report's wall-safe packet hypotheses.** The residual-cage release/refill construction is valid, but its strict packets and cost assumption are strictly weaker than the already canonical one-spare contact-budget endpoint: for a canonical source `kappa>=1`, so its packet count is at least `|S|+1`, and the existing endpoint gives a contradiction without deleting `U` or moving the source. The claimed broader relevance to weak-contact or post-motion packets is outside the stated theorem.

**PASS — promote the exact positive-circuit deletion characterization.** This is a finite covector theorem useful for identifying the minimum number of loaded vertices whose deletion permits a common strict-negative direction. Its application to the packet theorem is audited here but receives no separate canonical endpoint ID.

**REGRESSION VALID — promote the abstract topology-only cost example and the positive-spanning deletion example.** Their scope is finite covector data, not a planar source or global minimizer.

The direct vertex-cover statement is valid but follows from the stronger `kappa` formulation. A **positive circuit** is an inclusion-minimal nonempty index set of rows admitting a nonnegative, nonzero linear dependence summing to zero. The abstract topology and positive-spanning regressions are separately promotable guardrails.

## 1. Exact audited statement

Let `A` be a canonical contact-minimal, then diameter-pair-minimal triangle-free global minimizer in the Section-57 C-II regime. Write `V` for its nonisolated positive-contact core and retain every source label outside `V` in the full configuration. Let `M` be the exact unit-contact realization manifold of `V`, modulo Euclidean motions, and `T=T_A M`. Let `H` be the complete set of actual diameter pairs of `A`; by the canonical weak-row elimination in `C-ZRF`, every such pair is a strong row supported on `V`. For `e in H`, let `g_e` be the differential of its squared-distance excess on `T`.

For `U subset V`, set

```text
H_U = { ij in H : i notin U and j notin U }
```

and define

```text
kappa(H,G) = min |U| over U subset V for which there is u in T
              with g_e(u) < 0 for every e in H_U.
```

When `H_U` is empty, its condition is vacuous and `u=0` is allowed.

Let `C_1,...,C_a` be actual simple unit-contact polygonal walls with pairwise disjoint interiors. Put `S_i=A intersect int(C_i)` and `S=union_i S_i`. For each wall let `Y_i subset W_(C_i)` be a finite unit-separated packet, where `W_C` is the canonical open wall-safe region. If

```text
sum_i |Y_i| >= |S| + |U|
```

for any `U` witnessing the definition of `kappa`, then a same-cardinality unit-separated configuration of diameter strictly less than `D=diam(A)` exists. In particular, packets with total size at least `|S|+kappa(H,G)` are impossible for a global minimizer.

This includes the simpler basis-cover form. If `B` is any basis of the active-diameter differential rows and `R=H minus B`, every vertex cover `U` of `R` is an admissible deletion set, so packet surplus `|U|` suffices. Minimizing over bases gives

```text
kappa(H,G) <= tau_*(H,G) <= s_Z+1.
```

The bound is conditional on actual packet sets; it does not turn `s_Z`, a stress currency, or residual area into packing capacity. For the source report's strict wall-safe packets, it is not the strongest spendable endpoint: the argument below shows `kappa>=1`, and canonical `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` already excludes any such packet family with one extra site.

## 2. Independent proof reconstruction

First strictify each finite packet by a sufficiently small dilation about a fixed center. Finiteness and the strict guards defining `W_C` keep each dilated packet in its wall-safe region; every internal packet pair becomes strictly farther than one. The canonical wall shield gives strict unit clearance from every old point outside that wall interior, including boundary labels and contact-isolated source points. The same crossing argument for pairwise interior-disjoint walls gives strict clearance between different packets.

Every packet point lies in `int(conv A)`: the polygon interior is contained in the convex hull of its wall vertices, and the wall has nonempty interior. Its distance from every point of the old convex hull is strictly below `D`. Otherwise moving the interior point a small amount away from the other endpoint would create a pair longer than the diameter of the old hull. Thus all packet pairs and packet-to-source pairs have strict upper margin as well as the strict lower margin just established.

All endpoints of actual diameter pairs are extreme points of `conv A`; hence `U` is disjoint from the interior populations `S`. Choose exactly `|S|+|U|` of the strictified packet sites. For nonempty `H_U`, take a smooth contact-manifold curve `p(t)` with `p(0)=A|_V` and `p'(0)=u`. For each surviving active diameter pair,

```text
d/dt (|p_i(t)-p_j(t)|^2/2) at t=0 = g_ij(u) < 0.
```

Because `H_U` is finite, all its active pairs are strictly shortened for one sufficiently small positive `t`. If `H_U` is empty, leave the source stationary. The exact contact manifold preserves every old core contact; contact-isolated labels remain fixed. Every inactive old lower and upper constraint has strict slack and persists for sufficiently small `t`. Packet-to-source strict margins also persist by continuity while the old source moves; packet sites remain fixed. No wall is required to remain a contact wall after the move.

Delete `U union S` and insert the chosen sites. This preserves cardinality. Every old active diameter pair either has an endpoint in `U` and is deleted, or belongs to `H_U` and has been strictly shortened. Every other surviving old pair was already strictly shorter than `D`. All pairs involving an inserted site have strict upper margin by the interior-hull argument and weak lower bound by the wall shields and packet strictification. There are finitely many pairs, so the new diameter is strictly below `D`, contradicting global minimality.

For the basis-cover corollary, any basis `B` has `m` rows on the `m`-dimensional contact tangent. The canonical local-coordinate theorem gives `|H minus B|=s_Z+1`. Deleting a vertex cover of `H minus B` removes every residual active pair; the basis coordinates can be set to `-t` for all `b in B` by the inverse function theorem, strictly shortening the surviving basis pairs. This proves the vertex-cover version. More generally, a set `U` is admissible exactly when zero is outside `conv{g_e:e in H_U}`, which by strict separation is equivalent to a common strict negative direction. Zero lies in that convex hull exactly when some nonnegative dependence is supported on `H_U`; by finiteness such a dependence contains a minimal positive circuit. Thus admissible deletion sets are precisely the vertex sets hitting every positive circuit.

## 3. Hostile checks and exact scope

- **All actual diameter pairs:** The proof needs every length-`D` pair to lie in `H`. This follows only for the canonical diameter-pair-minimal representative from `C-ZRF` weak-diameter-row elimination; the claim is not made for an arbitrary KKT support subset. The isolated-source labels are retained globally, and no isolated coordinate enters `T`.
- **Finite motion:** A negative first derivative is used only on finitely many surviving active rows. Smooth contact-manifold integration and a common sufficiently small positive parameter make each inequality strict. No first-order velocity is treated as an endpoint without this step.
- **Global diameter:** The argument shortens every actual old diameter pair, not merely a selected stressed subset. No stress-energy decrease is substituted for maximum-diameter decrease.
- **Wall margins:** `C-EMBEDDED-WALL-REFILL` supplies simultaneous full-source wall clearance. Pairwise disjoint wall interiors supply cross-packet clearance. Wall vertices may be deleted in `U`; their original strict margins persist under the small source motion.
- **Contact isolates:** Every isolate in `S` is explicitly deleted and counted; every isolate outside `S` stays fixed and is covered by the strict wall shield. There is no use of the Section-57 affine kernel on isolated coordinates.
- **Triangle condition:** The conclusion is a strict sub-`D` competitor, so it contradicts global minimum diameter regardless of whether the competitor contains a unit triangle. No triangle-free packet claim is needed.
- **No capacity inference:** The theorem assumes the `Y_i`. Audit.57's empty terminal pentagon safe regions and the large-wall lock regression remain binding; neither residual surplus nor `kappa` constructs a site.
- **Subsumption:** If `kappa=0`, its defining direction strictly shortens every actual diameter row on the exact contact manifold, directly contradicting global minimality after a small finite integration. Hence every canonical source has `kappa>=1`. Strictifying the stated `W_C` packets gives pairwise new distances and all new-to-retained-source distances strictly above one and below `D`; they add no contacts and preserve triangle-freeness. With at least `|S|+1` sites, canonical `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` deletes `S` plus one nonisolated source vertex and contradicts contact minimality (or global optimality if diameter falls). No diameter release is needed for this stated packet class.

## 4. Independently checked regressions

### Abstract topology-only cost

For each `r>=1`, take `2r` disjoint two-vertex edges on `q=4r` vertices and assign their covectors in `T*=R^r` as `+e_j,-e_j` for `j=1,...,r`. Then `h=2r`, `d_H=q-h=2r`, `s_Z=r-1`, `k=3r-1`, and `m=q-k-1=r`; hence `h-m=s_Z+1`. The graph is a forest of caterpillar components and the rows admit equal positive weights summing to zero. Every row basis selects one row from each opposite pair, leaving `r` disjoint residual edges, so `tau_*=r`. Any admissible `U` must hit at least one edge in each opposite pair, since otherwise both `+e_j` and `-e_j` survive and no vector is strictly negative on both. One endpoint per pair suffices, so `kappa=r=s_Z+1`.

This exact abstract model satisfies the listed rank, positive-dependence, defect-identity, and forest-topology data. It proves that those data alone cannot improve the universal `s_Z+1` cost. It is not a planar embedding, a source framework, or a global minimizer.

### Loss of positive spanning is insufficient

Take rows `+e_1,-e_1,+e_2,-e_2` in `R^2` and delete the row `+e_2`. The remaining rows no longer positively span `R^2`, but the surviving `+e_1,-e_1` prevent every vector from being strictly negative on all surviving rows. Therefore a deletion criterion that merely destroys positive spanning cannot replace hitting every positive circuit.

## 5. Canonical dependencies and frontier effect

The audited source construction uses canonical `C-CONTACT-FACE-REGULARITY`, `C-ZRF`, and `C-CONTACT-DIAMETER-COORDINATES` for the smooth core chart, removal of weak diameter rows, and exact basis size; canonical `C-EMBEDDED-WALL-REFILL` supplies full-source wall and cross-wall margins. The exact independent covector characterization needs no repository dependency. The source construction is nevertheless subsumed for these strict packets by `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`.

The exact finite covector theorem identifies `kappa` as the minimum hitting number of the positive-circuit hypergraph. Its `kappa<=tau_*(H,G)<=s_Z+1` basis estimate follows from canonical `C-CONTACT-DIAMETER-COORDINATES`; the abstract regression shows that the bound cannot be improved from those defect identities and Woodall forest topology alone. The residual-cage packet application supplies no stronger endpoint than the canonical one-spare contact-budget result, no source-level capacity estimate, and no C-II branch elimination. The next obligation remains a source-realized strict spare site or a different full-source finite competitor.

## 6. Verification and disposition

No computational certificate is needed: the promoted conclusions are finite differential-geometric and convex-separation arguments. The two regressions above have complete exact data and are not numerical searches. Repository validation checks metadata and generated views, not these analytic steps.

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Residual-cage release/refill for the stated strict wall-safe packets | PASS — already subsumed | Do not add a separate canonical release/refill ID; `kappa>=1` reduces its packet condition to one spare site, already covered by `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` |
| Positive-circuit hitting characterization | PASS | Promote as `C-POSITIVE-CIRCUIT-STRICT-DIRECTION-TRANSVERSAL` |
| Basis residual-cover cost `kappa<=tau_*<=s_Z+1` | PASS — already follows | Follows from canonical `C-CONTACT-DIAMETER-COORDINATES`; record as a checked corollary, not a new theorem ID |
| Abstract topology-only cost equality | REGRESSION VALID | Promote as `C-RESIDUAL-CAGE-TOPOLOGY-COST-REGRESSION` |
| Loss-of-positive-spanning criterion | REGRESSION VALID | Promote as `C-POSITIVE-SPANNING-DELETION-REGRESSION` |
| Packet existence from residual, return currency, or large wall | NOT PROVED | No canonical capacity inference |
| C-II or Level I closure | NOT PROVED | Both remain open |
