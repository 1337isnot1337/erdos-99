<!-- theorem-state: {"artifact_id":"ART-056E4002057F","canonical":true,"claim_ids":["C-ONE-VACANCY-FLAT-PINNING-RATE"],"claim_statuses":{"C-ONE-VACANCY-FLAT-PINNING-RATE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: flat one-vacancy pinning and the curved-wall rate

Date: 2026-10-07. Audit base: `4b0b982451effe3e8183edfce349ce4c25f9a3bb`, state `2026-10-07.audit.74`. Source branch: `research/sol/target-c-overnight-closure-20261007`, frozen at `d4cf8ad02fc4a8fd0fb62d82a9ffb8b559f93d92`. The branch advanced first to `88f38a9c6a1bab8c02611211f386655e90baa01a` and then to `4bb549bd0ae37e1c7015d80b650dabc224b695d6`; the report, verifier, and saved certificate audited below are unchanged at both tips. No later branch content is used.

Source artifact: `docs/reports/target_c_one_deficit_flat_pinning_and_solidity_reduction_2026-10-07.md`, Sections 1--3. The FV/SS equivalence in Section 4, its literature discussion, and its curved-wall applications are outside this audit.

## Exact theorem promoted

Let (u=(1,0)), (v=(1/2,\sqrt3/2)), and
\[
H_M=\{iu+jv:\max(|i|,|j|,|i+j|)\le M\},\quad B_M=\partial H_M,\quad P_M=H_M\setminus B_M,
\]
where (M\ge2). For any vacancy (h\in P_M), set the moving chart to (P_M\setminus\{h\}), pin every point of (B_M), and impose the unit-distance lower constraints on every surviving unit-neighbor edge with a moving endpoint.

**Claim `C-ONE-VACANCY-FLAT-PINNING-RATE`.**

1. The surviving unit-edge row matrix (R), in the moving coordinates, has full column rank (2(|P_M|-1)). Its static first-order feasible cone is therefore ({0}).
2. With the flat boundary fixed, the vacancy chart is locally isolated among placements satisfying those edge constraints.
3. Replace the pinned boundary vertices by any family (q_b(\theta)=b+O(\theta)). For any feasible placements of the moving points that converge, after relabeling, to the same vacancy chart as \(\theta\downarrow0\), their displacement from that chart is (O(\theta)), with constants allowed to depend on (M) and (h). Every such sequence has a subsequence with bounded displacement divided by \(\theta\); when the normalized boundary displacements converge, the limiting moving velocity satisfies the associated inhomogeneous first-order inequalities for all surviving unit-neighbor pairs.

This is an auxiliary finite-chart theorem. It does not say an arbitrary source or one-deficit cloud can be relabeled into one of these charts.

## Independent proof reconstruction

Use axial coordinates for the triangular lattice and directions
\((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)\). Every moving point in the unpunctured interior has all six lattice neighbors in (H_M). Give each surviving unit edge weight one and add one to each of the six edges joining consecutive neighbors of (h); edges with both endpoints pinned can be dropped.

For a moving vertex (p) not adjacent to (h), the six unit-edge row gradients sum to zero. For (p=h+e_i), the omitted (ph) edge has gradient (e_i) in the full lattice stress, so the retained base rows sum to (-e_i). The two added ring-edge gradients incident to (p) sum to (e_i). Thus each moving column is equilibrated. Every retained edge weight is strictly positive, so if (R\delta\ge0) then
\[
0=\lambda^T R\delta,\quad \lambda>0,
\]
forces (R\delta=0).

To prove full column rank, triangulate (H_M) into elementary unit triangles and remove the six triangles incident to (h). If (h) has lattice radius at most (M-2), the removed one-ring is an interior hexagonal hole. If its radius is (M-1), that one-ring meets the outer boundary only in one boundary edge or in two consecutive boundary edges; it cannot join opposite sides when (M\ge2). In either case the remaining polygonal region is connected, so the edge-adjacency graph of its elementary triangles is connected. Every moving vertex lies in a remaining triangle: a vertex adjacent to (h) loses only the two triangles sharing the edge (ph). At least one surviving outer boundary edge remains because the one-ring removes at most two consecutive boundary edges while the outer hexagon has (6M\ge12).

A zero bar-variation on one nondegenerate triangle is an infinitesimal rigid motion. Two such motions agreeing on a shared edge agree everywhere. Connected triangle adjacency propagates one rigid motion across the remaining triangulation; its values vanish at the two fixed endpoints of a surviving outer edge, so that rigid motion is zero. This proves full column rank. The propagation argument also covers boundary-row and corner-adjacent vacancies.

For a finite feasible displacement \(\delta\) with fixed wall, each unit-edge inequality gives
\[
(R\delta)_e\ge-\tfrac12|\delta_p-\delta_q|^2\ge-c\|\delta\|^2.
\]
The positive equilibrium makes the weighted sum of these linear rows zero. Since there are finitely many rows and all weights are positive, every row is also bounded above by (c'\|\delta\|^2). A left inverse of (R) gives \(\|\delta\|\le c''\|\delta\|^2\), which forces \(\delta=0\) in a sufficiently small neighborhood.

For a moving wall, write the pinned displacements as \(\eta=O(\theta)\). The same old unit-edge constraints imply
\[
R\delta\ge-C(\theta+\|\delta\|^2)
\]
rowwise, since each wall contribution is linear (O(\theta)) and the squared edge displacement is (O(\|\delta\|^2+\theta^2)). The same positive equilibrium and full-rank left inverse give
\[
\|\delta\|\le C'(\theta+\|\delta\|^2).
\]
The assumed convergence makes \(\delta\to0\), so the quadratic term is absorbed and \(\delta=O(\theta)\). A bounded subsequence of the normalized moving and wall displacements then satisfies the linearized inequalities by division by \(\theta). This proves the rate reduction without assuming a first-order feasible velocity integrates to a finite motion.

## Adversarial checks and computation

The exact source verifier was inspected and run. It checks the integer force identity and triangle propagation from the pinned boundary for every vacancy at (M=2,\ldots,10): 999 vacancy charts and 178,002 moving-vertex equilibrium checks. Across these cases it checks 397,854 surviving triangle determinants exactly (160,974 for (M=10)). This is finite corroboration; the all-(M) connectivity and rank claims above come from the geometric argument, not extrapolation.

I also independently traversed the edge-adjacency graph after deleting the star of each vacancy for all (M=2,\ldots,10). Every remaining triangle set was connected and included a triangle with a surviving pinned outer edge. This directly tests the two delicate topology cases, including (M=2), radial boundary-row vacancies, and corner-adjacent vacancies. No counterexample was found.

The theorem does not use the canonical ZR/ZF affine-kernel theorem and does not extend it to isolates. It is about a fixed auxiliary lattice chart, not a canonical source; it proves neither a finite release nor global optimality. A bounded first-order cone still needs a separate argument to yield a triangle or a strict sub-(D) competitor. The source report's stronger flat-vacancy classification / strong-solidity equivalence is not promoted.

## Canonical disposition and frontier effect

Promote only `C-ONE-VACANCY-FLAT-PINNING-RATE` with no canonical dependencies. Record the verifier as exact finite support, not as the universal proof. The result can be used to normalize convergent curved-wall vacancy-chart sequences to scale \(\theta\), but supplies no arbitrary-cloud extraction, no exclusion of the top wall populations, and no Level I consequence by itself. Target C C-II remains open and its global endpoint is unchanged.
