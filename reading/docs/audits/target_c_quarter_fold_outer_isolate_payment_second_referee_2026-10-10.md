> Generated reading edition · [exact source](../../../docs/audits/target_c_quarter_fold_outer_isolate_payment_second_referee_2026-10-10.md) · source SHA-256 `667f2f24c5c5b1290a480f5c84fbef1964dcd17588634b905a99bf9dc58d4595`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-474284C91D01","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent second referee — quarter-fold outer isolate payment

Date: 2026-10-10. Canonical audit base: `origin/main=5f78cc282f6371a9d13e20d8a3e620adf539a5da`, state `2026-10-10.audit.230`.

Frozen candidate: canonical `C-QUARTER-FOLD-OUTER-ISOLATE-PAYMENT`, promoted by Audit.230. The underlying discovery report is `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md` at `origin/research/level-i-fused-review-20261009=6132201c1d3056ca68a222217094acb819f5b4d7`, Section 7.3. Its SHA-256 is `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`.

## Verdict

**PASS — already canonical; second referee confirms the exact Audit.230 scope.** The outside-region population inequality follows from (i) zero isolates in each nonconstant folded eight-face, (ii) no increase in the isolate population of any rigidly carried face, and (iii) conservation of the full set of contact-isolate labels. The proof tracks counts only; it does not track individual labels or produce the endpoint.

## Independent reconstruction

Fix the old source and endpoint from Audit.230. Because the endpoint has the same exact unit-contact graph, the set of degree-zero labels is unchanged. For any two distinct source labels that are nonadjacent in this graph, unit separation gives distance at least one and graph equality rules out distance exactly one; hence their distance is strictly greater than one. In particular, every isolate is strictly clear of every face-boundary vertex and of every other isolate. An isolate cannot lie on a unit boundary edge: every point of that segment is within one of an endpoint.

For each nonconstant face, the old face is a simple convex actual eight-cycle. The endpoint's transformed boundary is unit-separated and triangle-free, and its quarter-fold has the four two-edge arcs supplied by `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`. The transformed-hull cover `C-QUARTER-FOLD-TRANSFORMED-EIGHT-FACE-HULL-COVER` says its convex hull is covered by closed unit disks centered at the transformed boundary labels. The bounded face interior lies in that hull. Any isolate in the new face would be strictly farther than one from every boundary label by the preceding exact-graph argument, contradicting the cover. Thus the new isolate count in every nonconstant face is zero, regardless of its old isolate population.

For a constant-sign face, the endpoint carries its boundary and interior by a rigid motion. Pull every new isolate in that face back by the inverse isometry. The pulled-back points remain strictly inside the old simple unit-contact cycle, strictly separated from one another, and strictly separated from every wall vertex. The canonical `C-UNIT-WALL-PACKET-POPULATION-BOUND` applies to this one cycle in the contact-minimal source and bounds their number by the old isolate population of the face. This does not require old isolate labels to stay in that face.

Let `B_old` and `B_new` be the total isolate counts inside all bounded face interiors before and after the endpoint. Summing the two facewise conclusions gives

$$
B_{new}\le B_{old}-\sum_{F_i\text{ nonconstant}}z_i(A).
$$

The exact contact graph preserves the total number `Z_total` of isolate labels, so `Z_out=Z_total-B` at both endpoints. Subtracting yields

$$
Z_{out}(A')\ge Z_{out}(A)+\sum_{F_i\text{ nonconstant}}z_i(A),
$$

including when a nonconstant face contains several old isolates. The face-interior/outer-region partition is valid at both endpoints: the preserved plane embedding makes the bounded faces disjoint, and a degree-zero label cannot lie on a unit cycle edge.

## Scope checks

- Exact contact-graph preservation is load-bearing. Merely retaining old contacts would not preserve the isolate labels or rule out new unit distances.
- The nonconstant-face argument uses a simple convex actual eight-face and the four-two-edge quarter-fold pattern. It does not cover larger or nonconvex faces.
- The rigid-face packet bound uses the canonical source's contact-minimality and a simple actual unit-contact cycle. It does not assume the new endpoint is a minimizer.
- No upper-diameter constraint, KKT stress, verifier, endpoint existence, individual isolate tracking, or outside-region capacity estimate is used or established.
- The source report's old claim that each occupied folded face has exactly one isolate is unnecessary here; the population proof handles arbitrary `z_i(A)`.

## Disposition

No theorem-state edit or state-version increment is needed: Audit.230 already records this exact scope and its three canonical dependencies. The current Target C endpoint remains the integrated-endpoint/outside-capacity obligation stated in `CURRENT.md`; C-II and Level I remain open.
