<!-- theorem-state: {"artifact_id":"ART-80A0A5A44E42","canonical":true,"claim_ids":["C-ONE-CORNER-ONE-VACANCY-OLER-RESIDUAL","C-ONE-CORNER-ONE-VACANCY-SOURCE-EXCLUSION","C-ONE-CORNER-ONE-VACANCY-STRICT-PACKET"],"claim_statuses":{"C-ONE-CORNER-ONE-VACANCY-OLER-RESIDUAL":"canonical","C-ONE-CORNER-ONE-VACANCY-SOURCE-EXCLUSION":"canonical","C-ONE-CORNER-ONE-VACANCY-STRICT-PACKET":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: one-corner, one-vacancy curved-wall packet

Date: 2026-10-07. Source branch: `research/sol/target-c-owner-order-closure-20261006`, immutable snapshot `6ee89d204688df2de70594e08ad6b12edeb9145a`. Source artifact: [`target_c_one_corner_one_vacancy_nonaffine_packet_2026-10-06.md`](../reports/target_c_one_corner_one_vacancy_nonaffine_packet_2026-10-06.md).

**Verdict: PASS — promote the all-M strict packet, the conditional full-source contact-loss exclusion for populations at least two below capacity, and the exact Oler residual classification.** Scope is fixed M with curvature sufficiently small depending on M. This does not extract such a wall from a canonical source or eliminate the top two populations.

The branch advanced after the audited snapshot to `0d3b0182c064f73d2a6a64452ee01d140f1b1475`. The diff adds a separate sorted-rate / highest-population report, verifier, and literature file; it does not modify the one-corner report, verifier, or input certificates audited here. That added theorem remains outside this verdict.

## Exact audited statements

Let M >= 3, R=M-1, and let P_R be the radius-R hexagon in the triangular lattice, with N=|P_R|=3M^2-3M+1. Remove the center from this target chart, so the chart has N-1 sites. The wall F_(M,theta) has six sides of M unit edges each. On each side k, its edge vectors have directions arg(w_k)+(2j-M+1)theta for j=0,...,M-1, where w_k are the six regular-hexagon side directions at theta=0. Its six corners are L(theta)e_k, where e_k=Rot(k pi/3)u and L(theta)=sum over j of cos((2j-M+1)theta). For each fixed M there is theta_0(M)>0 such that, for 0<theta<theta_0(M), the wall is strictly convex, unit-separated, and triangle-free, and it admits N-1 points strictly inside it that are pairwise more than one apart and more than one from every wall vertex except one chosen corner. The points are a strict packet in the specified chart class. They are not old source points.

For a contact-minimal triangle-free global minimizer containing this wall as an actual unit-contact polygon, let z be the number of source points strictly inside the wall. If z <= N-2, replacing all z points and the one wall corner with z+1 packet sites gives a same-cardinality unit-separated triangle-free source with fewer unit contacts and diameter at most the original D. This contradicts the canonical contact-minimal choice (or global minimality if the diameter drops).

If, in addition, area(F_(M,theta)) < (sqrt(3)/2)(3M^2+1), Oler's finite inequality gives z <= N. Thus a canonical source in this exact wall class, if it exists, must have z in {N-1,N}. The wall-existence and top-population cases remain open.

## Independent reconstruction of strict packet existence

Write a_l for the gradient row of each unit pair among the N-1 chart sites and the five retained corner guards. A nonnegative dependence among these rows is a nonnegative contact equilibrium at every moving chart vertex. The following layer argument shows that every such dependence is zero.

Let the shell radius be rho(i,j)=max(|i|,|j|,|i+j|). A unit lattice edge joins equal or consecutive shells. At the outer radius-R ring, each noncorner site has two tangent ring edges and exactly two edges to the next inner shell. The force gradients of those inner edges have positive outward-normal projection, so both inward-edge stress weights are zero. Tangential balance then makes the two incident ring weights equal; the side weight is constant along each side.

At a guarded corner, the radial guard and inner radial edge have no tangential component, so tangential balance equates the two adjacent side weights. The five retained corners connect all six side weights in a path, so they have one common value. At the unguarded corner, both incident ring gradients and the single inward radial gradient have strictly positive projection on the outward corner ray. Equilibrium forces all three weights to vanish. The common side weight is therefore zero, and the inward radial weight on the missing-guard ray is zero.

Peel the ring inward. Inductively, suppose every cross-layer weight from radius r+1 to r is zero except possibly the five radial corner-chain weights, and the radius-(r+1) ring weights are zero. At a noncorner vertex of radius r there is no remaining force from the outer layer; its inward-edge weights vanish by outward-normal projection and its ring weights balance tangentially. At each corner, radial chain rows have no tangential component, so the adjacent side weights agree. The five corner relations connect all six side weights. On the missing-guard ray there is no incoming outer radial weight. Both ring gradients and the inward radial gradient at that corner have positive outward projection; hence they all vanish, forcing the common ring weight to zero. This also kills every noncorner inward edge at radius r. The induction reaches radius one. The center is absent, so no inward radial edge remains to balance any surviving outer-chain weight at its five corners; those weights must be zero. At each higher corner shell the zero inner radial weight forces its outer radial weight to be zero as well. Thus all five guard weights and all rows vanish. This proves that no nonzero nonnegative row dependence exists.

The finite row set therefore has a compact convex hull that excludes zero. Let d be its closest point to zero. The projection inequality gives a_l dot d >= |d|^2 > 0 for every chart-contact and retained-corner row. Thus all those unit pairs open strictly to first order.

The curved wall opens every remaining unit pair between a noncorner wall vertex and a chart site. On a side with unit direction w, the wall vertex at index i has velocity -i(M-i)Jw. For a limiting unit pair to an interior chart site, the inward vector has dot product sqrt(3)/2 with Jw. Its half-squared-distance derivative from wall motion alone is therefore sqrt(3)i(M-i)/2 > 0 for i=1,...,M-1. Scale d by a sufficiently small positive factor so these finitely many positive wall margins remain positive while all chart and corner margins stay positive. Other lower pairs have strict limiting slack. Every chart point starts strictly inside F_(M,0), so its small-motion position remains inside F_(M,theta).

The resulting packet is genuinely nonaffine. If d_i=A p_i+t were affine, let S be the symmetric part of A. Strict opening of any chart edge in direction e_1 requires e_1 dot S e_1 > 0. The retained opposite corner guards at e_1 and -e_1 require, after summing their two strict first-order inequalities, -2R(e_1 dot S e_1)>0. Contradiction. Both opposite guards are retained because only e_0 is deleted.

This proves existence for every fixed M and sufficiently small positive theta. It does not give a uniform onset in M. Rational axial velocities are dense, so the finite strict inequalities also admit rational velocity data if desired.

## Full-source exchange and Oler arithmetic

All z old interior labels are removed. The one deleted wall corner removes its two incident unit contacts. Since z+1 <= N-1, choose z+1 distinct sites from the strict packet. Every inserted point is strictly clear of all retained wall vertices, so canonical `C-ONE-VERTEX-CONVEX-WALL-SHIELD` separates it from every retained exterior source point, including contact isolates. All old interior points are gone. The packet creates no new unit contact, retains no equilateral triangle, and preserves cardinality. Its points lie strictly inside the old source hull, so every inserted-involving distance is strictly below D. This checks the complete source and the actual upper-diameter constraint.

For the population bound, Oler Lemma 21.1 in `docs/theory/03-oler-shell.md` applies to the 6M wall vertices together with the z interior points. With perimeter 6M and area below (sqrt(3)/2)(3M^2+1), it gives

    6M + z < 3M^2 + 3M + 2.

Since z is an integer, z <= 3M^2-3M+1=N. Combining this with the contact-loss exclusion of z<=N-2 leaves precisely z=N-1 or z=N. This is only a conditional wall-class reduction.

## Verifier audit and hostile scope checks

The exact source verifier was run at the immutable snapshot. It imports the exact Q(sqrt(3)) helper `verify_target_c_three_direction_corner_barrier_2026_10_06.py` and the exact axial helper from the nested-stress audit; both were preserved from the same source snapshot or the already merged audit. Its rational and Q(sqrt(3)) arithmetic checks M=3,4,6: 489 exact first-variation inequalities, 9,072 inserted-pair upper checks, 1,137 old-source pair checks, 1,137 endpoint pair checks, 144 integer population counts, and velocity-input SHA256 `868c4bb060ead30f8f98a8bb01d443ef3eb0de5b510a3be845f976122f1ea1db`. The verifier checks finite packets; it does not prove the all-M peeling, the all-M first-order direction, or arbitrary-source chamber extraction. Those conclusions rest on the analytic proofs above and the canonical shield/Oler inputs.

- Audit.70's affine barrier assumes the full center-containing chart and all six corner guards. This theorem removes the center from the target chart and deletes one actual wall corner, so its hypotheses do not apply.
- Audit.71's nested-ring stresses also use the full center-containing chart and all six guards. The missing chart center and guard invalidate that selected-support argument; the separate layer-peeling proof above handles the punctured chart.
- The two-deletion exterior-shield regression is inapplicable: exactly one corner is deleted, and the canonical one-vertex shield is used with every exterior source point retained.
- The finite D(8) heptagon capacity regression has a different wall geometry and does not refute this fixed-M six-sided curved-wall theorem.
- The theorem does not infer a spare site from residual area. It constructs and certifies an explicit strict packet, then pays every old interior source label and the deleted corner.
- The report's phrase “old population choices” in the verifier describes the integer capacity bookkeeping. The universal source replacement is established analytically with the full-source shield; the sample endpoint itself uses a wall-plus-center source.

## Canonical disposition

Promote `C-ONE-CORNER-ONE-VACANCY-STRICT-PACKET` and `C-ONE-CORNER-ONE-VACANCY-SOURCE-EXCLUSION`. Keep the later sorted-rate/highest-population report proof-only until its own audit. The local obligation under the area threshold is now restricted to z=N-1 or z=N, but no canonical source is known to contain this wall, and C-II and Level I remain open.
