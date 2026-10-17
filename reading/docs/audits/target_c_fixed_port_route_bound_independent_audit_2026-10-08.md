> Generated reading edition · [exact source](../../../docs/audits/target_c_fixed_port_route_bound_independent_audit_2026-10-08.md) · source SHA-256 `f914d607114e70a2a7388ad038a82b3df5f0fd81f745ac0b436c50de34f214ad`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CABC7F437B0D","canonical":true,"claim_ids":["C-BOUNDED-FACE-PORT-ROUTE-BUDGET","C-FIXED-PORT-CONTACT-ROUTE-BOUND","C-RHOMBUS-BOUNDARY-ROUTE-FACTOR-TWO-REGRESSION"],"claim_statuses":{"C-BOUNDED-FACE-PORT-ROUTE-BUDGET":"canonical","C-FIXED-PORT-CONTACT-ROUTE-BOUND":"canonical","C-RHOMBUS-BOUNDARY-ROUTE-FACTOR-TWO-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C Audit.134 — fixed-port contact routes and face-defect payment

Date: 2026-10-08  
Audit base: `origin/main=6049e3f751b9e5efd472d2d36b670f228c1e8997`, state `2026-10-08.audit.133`  
Source snapshot: open draft PR #668, branch `research/sol-c2-deep-port-route-20261004` at `a2ccd6161519c7d27482a7c6e751cd44e595e1b6`  
Source report SHA-256: `bf0ae00a71c86ac895059c6c5b9edff9fb2b27ccab4d6a62bd18efbce191b018`  
Source verifier SHA-256: `21367e572ced2b7967731ed817763717d21f7472778dd8f3f04709d217d861cc`

## Audit boundary and verdict

I independently audited source Theorem 3 (the finite fixed-port route) and Theorem 3b (its bounded-degree/high-degree-face refinement). I did not audit the Type-II near-port-grid extraction or its strong-branch composition in Section 5; those claims remain unreviewed and are not promoted. The Section 6.1 thin-face regression is subsumed by canonical `C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION`; the zero-defect oblique-grid regression is subsumed by `C-RHOMBIC-PATH-ROUTE-EXCESS-SHARP-REGRESSION`.

- **PASS — promote `C-FIXED-PORT-CONTACT-ROUTE-BOUND`.** A specified actual loaded attachment can reach any vertex of its unloaded contact component along actual contacts, with cost bounded by Euclidean displacement, nearby attachments, and the augmented-face defect met by the segment.
- **PASS — promote `C-BOUNDED-FACE-PORT-ROUTE-BUDGET`.** For every fixed degree cutoff, a macroscopic detour at submacroscopic Euclidean distance requires a linear tail of higher-degree augmented faces; the single global tail is bounded by the canonical Section-123 currency.
- **REGRESSION VALID — record `C-RHOMBUS-BOUNDARY-ROUTE-FACTOR-TWO-REGRESSION`.** A rational strict unit rhombus has boundary points whose shorter boundary arc is longer than twice their chord. The corrected `4/sqrt(3)` factor is necessary.
- **NOT AUDITED — do not promote** the source's Section 5 Type-II extraction, its Corollary 5, or the claimed strong-branch composition. Their cap/grid antecedents remain proof-only.

These results are metric path bounds, not a source motion or diameter improvement. The linear face-tail allowance can still be paid by canonical `e_BB-k`, and the argument gives no multiplicity bound for applying one face bank to many routes.

## Canonical source and dependency scope

Take a canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`, `C=C_*`, and `H=H_*`, retaining all source points. Let `B` be the actual diameter endpoints. Let `I` be one connected component of the nonisolated positive-contact core after removing `B`, and let `A` be the actual loaded endpoints with at least one contact to `I`; put `P=conv(A)`. The contact-isolated source points remain in the full source and receive no core coordinates.

For the local route graph, retain only actual contacts internal to `I` and actual contacts from `I` to `A`, omit loaded-loaded contacts, and add every side of `P` as a designated polygon side even if that side is an actual loaded-loaded contact. Call the resulting embedded graph `J^+`. Let `d(f)` be the boundary degree of a bounded face of `J^+`.

The universal route proof uses the positive equilibrium and canonical attachment geometry from `C-ZRF` and `C-ATTACH-CURRENCY`. The global refinement also uses the exact augmented-cell defect budget `C-AUGMENTED-CELL-DEFECT-BUDGET`, which states

`sum_r Q_r^+ <= 2(e_BB-k)`, where `k=d_H+s_Z` and `Q_r^+=sum_f (d(f)-4)_+` over bounded faces of each augmented harmonic cell.

The exact connected triangle-free penny-graph edge/diameter inequality used in the proof is Eppstein's Theorem 2, checked in the repository transcription `extracted/text/463.txt` and normalized in `docs/problem/literature_baseline.md`, §2.4.

## Independent face-topology reconstruction

Every member of `A` is an extreme vertex of `P`; every vertex of `I` lies strictly inside `P`. For the latter, if an unloaded vertex maximized a supporting linear functional of `P`, positive contact equilibrium would force all its contact neighbors onto that supporting line. Unit contacts then give degree at most two, contrary to the canonical unloaded-degree bound.

The graph `J^+` is 2-connected. Deleting an attachment leaves `I` connected and every other attachment adjacent to `I`. If an unloaded vertex `x` is deleted and some component of `I-x` contains no attachment, every contact neighbor of that component lies in the component or at `x`. The positive weighted coordinate maximum principle with the sole boundary value `x` forces all its points to equal `x`, impossible. Thus every component of `I-x` meets `A`; the added polygon cycle joins them. Every face boundary is consequently a simple cycle.

Every bounded face is convex. At an unloaded vertex, an angle greater than `pi` would put every contact ray in an open half-plane, contradicting positive equilibrium. At an attachment, the face sector is contained in the interior tangent cone of the strictly convex polygon `P`, whose angle is below `pi`. Hence every bounded-face angle is at most `pi`.

Any two distinct polygon sides can be separated by an interior contact crosscut joining suitable attachment vertices: use contact edges from the endpoints into `I` and a simple path through connected `I`. The crosscut lies in `P` and prevents a single face from meeting both sides. Thus a bounded face uses at most one added side.

A bounded face without an added side contains at most one attachment. Otherwise, convexity puts the chord between two nonconsecutive attachment vertices in the face interior. Both boundary arcs contain unloaded vertices, and a contact path in connected `I` between opposite arcs, which stays in `P`, would have to cross that chord inside the face. Such a crossing is impossible: the path edges belong to `J+`, whose face interior contains no graph edge; if the chord itself is an omitted actual loaded-loaded contact, planarity of the full unit-contact graph also forbids a crossing. The same chord argument shows that a face with one added side has no other attachment on its contact arc. Therefore its remaining boundary is a simple path of actual contacts from one endpoint of the added side to the other, with all internal vertices in `I`.

These claims use the actual graph and the explicit polygon-side augmentation. They do not assume a face theorem for the graph with arbitrary loaded-loaded chords retained.

## `C-FIXED-PORT-CONTACT-ROUTE-BOUND` — PASS

For a fixed loaded port `a in A` and unloaded target `z in I`, write

`R=|a-z|`, `sigma=[a,z]`,

`N=|A intersect closed_ball(a,R+3)|`,

`Q_sigma=sum_{f: closure(f) intersects sigma} (d(f)-4)_+`.

There is an actual contact path from `a` to `z`, with every internal vertex in `I`, of length

`ell <= (4/sqrt(3)) R + 15 N + 5 Q_sigma`.                         (1)

The same local estimate holds from any `p in I` to `z in I`, with the radius and attachment count centered at `p`; that path stays wholly in `I`.

To reconstruct (1), traverse the straight segment through its convex faces. It meets a given face in one interval. Replace each interval by an actual contact-boundary route and concatenate across shared contact edges. A continuous route in the geometric realization of the contact graph yields an edge path no longer than that route. Degenerate vertex/edge incidences follow by a general-position polygonal perturbation and a finite-face limit; closed face and ball definitions retain every limiting charged face and boundary attachment.

The costs split into exhaustive face types:

1. **Interior strict rhombi without an attachment.** For boundary points on one edge, route along that edge. On adjacent edges, the route through their common vertex has length at most twice the chord because every rhombus angle is at least `pi/3`. On opposite edges, the shorter boundary arc has length at most two and the chord is at least the altitude `sqrt(3)/2`. Thus the boundary stretch is at most `4/sqrt(3)`. Summing over these faces costs at most `(4/sqrt(3))R`.
2. **Interior rhombi incident to an attachment.** There is at most one attachment per face. Choose a boundary route with no attachment as an internal vertex; if the unique attachment is the specified initial port `a`, start at `a` and take the contact arc into the component. The route costs at most four. A loaded endpoint has contact degree at most three, so at most three such rhombi are charged per attachment. If the segment meets one, its attachment lies within distance `R+2` of `a`. Total cost is at most `12N`.
3. **Polygon-side faces of degree three or four.** The actual contact arc has length `d(f)-1<=3` and has no attachment internally; its two endpoints are the allowed attachments. The face diameter is at most three because that contact arc has at most three unit edges. If it meets the segment, both endpoints of its unique polygon side lie within `R+3` of `a`. There are at most `N` such polygon sides, so the cost is at most `3N`.
4. **Exceptional faces of degree `d>=5`.** In an interior face, choose a boundary route with no attachment internally; if its sole attachment is the specified initial port, that port is the allowed initial endpoint. In a polygon-side face, use its contact-only arc. The cost is at most `d` (or `d-1`) and hence at most `5(d-4)`. Summing over faces meeting `sigma` costs at most `5Q_sigma`.

For `N>=3`, all points of `A` counted by `N` remain vertices of their own convex hull, its consecutive edges have length at least one, and its perimeter is at most `2pi(R+3)`. Thus `N<=2pi(R+3)+2`, also valid for `N<=2`. Substitution gives

`ell <= C R + C_0 + 5Q_sigma`,

where `C=4/sqrt(3)+30pi` and `C_0=90pi+30`. Since `Q_sigma<=sum_r Q_r^+<=2(e_BB-k)`, this also yields the canonical global bound

`contact_distance_I(a,z) <= C|a-z|+C_0+10(e_BB-k)`.               (2)

The bound is fixed-port: the endpoint is the specified `a`, and no other loaded vertex is internal to the path.

## `C-BOUNDED-FACE-PORT-ROUTE-BUDGET` — PASS

Fix an integer `M>=5`, and define the single global high-degree budget

`T_M=sum_{r,f: d(f)>M} (d(f)-4)`

over bounded faces of all canonical augmented harmonic cells. By Section 123,

`T_M<=2(e_BB-k)`.

For `r=M+1/2`, set

`K_M=C+200r/pi`, `B_M=C_0+100r^2`.

The path in (1) can be chosen with length

`ell <= K_M R + B_M + 5T_M`.                                   (3)

For a bounded exceptional face with degree at most `M`, its diameter is at most `M`: in a face without a polygon side use the unit boundary, and in a polygon-side face use its contact arc of at most `M-1` unit edges. If such a face meets `sigma`, all its vertices lie within distance `M` of the segment. The disjoint radius-`1/2` disks centered at these unit-separated vertices lie in the radius-`r` capsule around a segment of length `R`, whose area is `2rR+pi r^2`. Hence their number is at most `(8r/pi)R+4r^2`.

Each vertex is incident to at most five bounded augmented faces: unloaded contact degree is at most five, and a loaded attachment has contact degree at most three plus its two polygon sides. Therefore the sum of degrees, and so the low-degree defect on the segment, is at most five times the displayed vertex count. Its route coefficient is five, giving the additions `200r/pi` to the linear coefficient and `100r^2` to the constant. Faces of degree greater than `M` on the segment spend at most the one global `T_M`; this proves (3).

If every actual contact route from `a` to `z` has length at least `lambda D` while `R<=rho D`, (3) forces

`T_M >= ((lambda-K_M rho)D-B_M)/5`.

In particular, for any fixed `M` and `rho<lambda/K_M`, the high-degree face tail is linear in `D`. This does not contradict the canonical allowance `T_M<=2(e_BB-k)`, which can itself be linear. It also does not let multiple paths spend the same `T_M` independently.

## Regression dispositions

The exact rational rhombus has edge vectors `u=(1,0)` and `v=(5/13,12/13)`. It is strict triangle-free because its diagonal squared lengths are `16/13` and `36/13`. On opposite edges, boundary parameters `9/13` and `3-4/13` give chord length `12/13` and shorter boundary arc length two, ratio `13/6>2`. The verifier checked this exact case. The analytic rhombus estimate above is correct; no factor-two estimate is used in the promoted theorem.

The thin convex unit-edge polygon family in source Section 6.1 is a valid area/perimeter-only tail regression, but Audit.123 already promotes a stronger positive-pinned-equilibrium, full-pinned-rigidity family with the same `T_M/D -> 2` obstruction (`C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION`). The oblique-grid example in source Section 6 is already covered by `C-RHOMBIC-PATH-ROUTE-EXCESS-SHARP-REGRESSION`. No additional IDs are needed for those two examples.

## Verifier and scope

I inspected and reran `research/verify_target_c_deep_port_defect_routes_2026_10_04.py` from the frozen source commit. It uses only `Fraction` arithmetic. It checked 14 bounded augmented faces in three exact harmonic fixtures, 111 rational strict rhombi and 13,320 boundary-point pairs for the stretch inequality, 17,736 pair checks in three oblique grids, and 3,164 pair checks in four thin-face polygons. These checks validate the listed fixtures, exact counterexamples, and rational identities; they do not verify Theorem 3, Theorem 3b, the topological crosscut claims for all sources, the Type-II extraction, or global optimality. The universal results above rest on the independent analytic proof.

The theorem outputs a structural graph route only. It establishes no local-to-global optimality implication, source motion, contact-changing replacement, exact triangle, C-II closure, or Level I conclusion.
