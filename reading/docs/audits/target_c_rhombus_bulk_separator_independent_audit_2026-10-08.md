> Generated reading edition · [exact source](../../../docs/audits/target_c_rhombus_bulk_separator_independent_audit_2026-10-08.md) · source SHA-256 `06d60fa1e58ae9add0f5805e392ec967674a657fbb48290ac309f3df724f15a0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-04DAF63E6D2C","canonical":true,"claim_ids":["C-CONVEX-FACE-LOADED-RETURN-BOUND","C-PINNED-GRID-RETURN-SQRT-REGRESSION","C-RHOMBUS-BULK-LOADED-RETURN-BOUND","C-RHOMBUS-SEPARATOR-CAPACITY"],"claim_statuses":{"C-CONVEX-FACE-LOADED-RETURN-BOUND":"canonical","C-PINNED-GRID-RETURN-SQRT-REGRESSION":"regression","C-RHOMBUS-BULK-LOADED-RETURN-BOUND":"canonical","C-RHOMBUS-SEPARATOR-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C Audit.133 — rhombus bulk separators and loaded returns

Date: 2026-10-08
Audit base: `origin/main=8440641068c20a58c2f0a83679773f5303351d3a`, state `2026-10-08.audit.132`
Source snapshot: `origin/research/target-c-port-route-audit-20261004` at `0e49b450cc4819cc2f4f205303cbb9a09b45d269` (open draft PR #671)
Source report SHA-256: `3bf843495465d0aa2b35022f08ec10e9bdd43ae8d12c8205888024e4281e044a`
Source verifier SHA-256: `26349d267cb3e2a1bed4979cb732d5d6e98772768179bc8331b019bb088803c7`
Classification: **PASS — promote** for the finite separator and path theorems; **CONDITIONAL ONLY** for the deep-cap consequence; **REGRESSION VALID** for the pinned-grid order example.

## Exact scope and endpoint

Work with a canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`. Let `V` be its nonisolated positive-contact core, `B` its loaded actual diameter endpoints, and `I` one connected component of unloaded core vertices. Let `A` be the set of loaded vertices with a contact to `I`. In the contact graph `J` induced on `I union A`, omit loaded-loaded edges; paths stop at their first loaded vertex, so those edges are irrelevant.

Let `R` be a finite family of bounded strict unit-rhombus contact faces whose vertices lie in `I`, and let `X` be the union of their vertices. For a separator `S subset I union A` between `X` and `A`, write

`k_I=|S intersect I|`, `k_B=|S intersect A|`, and `w=5 k_I+3 k_B`.

The audited chain is

`quadratic rhombus population -> a separator has quadratic capacity -> every minimum separator has linear size -> linearly many vertex-disjoint paths to distinct actual loaded attachments`.

This is a source-graph statement. It does not move points, delete source labels, or produce a strict sub-`D` competitor.

## 1. Finite separator capacity — PASS

Let `R_0` be the number of rhombi in the family with no vertex in `S`, and let `c` be the number of components of `J-S` containing at least one such rhombus. The strongest finite statement audited is

`R_0 >= R-5 k_I`,

and, when `R_0>0`,

`(sqrt(3)/2) R_0 <= (pi/4) (w-3c)^2`.

Consequently every separator satisfies

`R <= 5 k_I + (pi/(2 sqrt(3))) (w-3)_+^2`.                 (1)

### Independent reconstruction

Every contact vertex has degree at most five: the rays to its unit-contact neighbors are pairwise separated by more than 60 degrees, since equality would create a unit equilateral triangle. At a loaded vertex, all contact rays lie inside the open hull angle of an extreme point, an interval shorter than 180 degrees; hence its contact degree is at most three. A strict unit rhombus has area at least `sqrt(3)/2`, because its acute angle is greater than 60 degrees.

At most five rhombi are incident with each deleted unloaded vertex, so at most `5 k_I` faces are lost. Consider one component `U_j` of `J-S` containing a retained rhombus. The separator property makes `U_j` entirely unloaded. Every contact from `U_j` to its complement meets `S`; write `n_j=|U_j|`, `e_j` for its internal contact edges, `t_j` for its edges to `S`, and `delta_j` for the graph diameter of its connected contact graph.

Restrict the mixed rigidity matrix on `V` to the `2n_j` velocity columns of `U_j`, retaining every contact row incident with `U_j`. Its kernel is zero. Indeed, a vector in that kernel extends by zero to a flex of the full mixed active framework: no actual diameter edge meets an unloaded vertex of `U_j`. Canonical `C-ZRF` makes the extended flex Euclidean on `V`; it vanishes at two distinct loaded endpoints outside `U_j`, so it is zero. The restricted matrix therefore has full column rank. Positive KKT contact equilibrium at every unloaded vertex supplies a nonzero row dependence, using the positive weights on all internal and boundary contact rows. It follows that

`e_j+t_j >= 2 n_j+1`.

Eppstein's connected triangle-free penny-graph theorem gives `e_j <= 2 n_j-delta_j-2`, including the singleton case `n_j=1, delta_j=0`. This is Theorem 2 of David Eppstein, “Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs,” *Journal of Graph Algorithms and Applications* 22(3) (2018), 483–499, DOI 10.7155/jgaa.00463. I checked the exact connected-graph statement in the repository's transcription at `extracted/text/463.txt` and its normalization in `docs/problem/literature_baseline.md`, §2.4. Thus `t_j >= delta_j+3`. Distinct components use distinct boundary edges, and the degree bounds on `S` give

`sum_j t_j <= 5 k_I+3 k_B=w`, hence `sum_j delta_j <= w-3c`.

Every retained rhombus lies in `conv(U_j)` for its component. Unit contact paths imply `diam(conv(U_j))<=delta_j`; the planar isodiametric inequality then yields

`(sqrt(3)/2) R_0 <= sum_j area(conv(U_j)) <= (pi/4) sum_j delta_j^2 <= (pi/4)(w-3c)^2`.

Together with the deletion count this proves the displayed estimates. If `R_0=0`, the consequence (1) follows directly. If `R_0>0`, then `c>=1` and `w>=3c`, so replacing `w-3c` by `(w-3)_+` proves (1).

The critical scope points are explicit: the rank argument is on `V`; contact-isolated source points remain in the source but are not assigned affine-kernel coordinates; loaded endpoints in this argument are actual diameter endpoints; and `J` uses actual contact edges.

## 2. Minimum separators give simultaneous actual returns — PASS

Define `C_0=8 pi/sqrt(3)` and

`F(R)=(sqrt(25+4 C_0 R)-5)/(2 C_0)`.

For any family above, let `p` be the maximum number of pairwise vertex-disjoint contact paths from `X` to distinct vertices of `A`. Each path can be trimmed to have only its first vertex in `X` and only its last vertex in `A`. The exact conclusion is

`p >= ceil(F(R))`,

and in particular

`p >= (1/4) sqrt(2 sqrt(3)/pi) sqrt(R) - 5 sqrt(3)/(16 pi)`.     (2)

### Independent separator and flow argument

Take a minimum-cardinality vertex separator `S`, of size `k`. If `s` is an unloaded vertex of `S`, minimality says that restoring only `s` creates an `X`-to-`A` path. The neighbor of `s` on the path toward its first surviving loaded endpoint lies in a component of `J-S` meeting `A-S`. That component cannot contain an unremoved rhombus: it would then connect `X-S` to `A-S`. Thus one contact at each unloaded `s` is not counted by the boundary totals `t_j`. These excluded edges are distinct, so

`sum_j t_j <= 4 k_I+3 k_B <=4k`,

and hence `sum_j delta_j <=4k-3c`. Using the same area proof as in (1) gives

`R <= 5 k_I+(pi/(2 sqrt(3)))(4k)^2 <= 5k+C_0 k^2`.

Solving this quadratic gives `k>=F(R)`.

For the path conversion, split each vertex into an in/out pair joined by a unit-capacity arc; give each directed contact arc, each source-to-`X` arc, and each `A`-to-sink arc capacity `|V(J)|+1`. Cutting all vertex arcs shows that a minimum cut has value at most `|V(J)|`, so it uses only unit vertex arcs. Integral max-flow/min-cut gives equality between minimum vertex-separator size and the maximum number of vertex-disjoint `X`-to-`A` paths, with distinct endpoints because terminal vertices also have unit capacity. Trimming each path at its last `X` vertex before its first `A` preserves disjointness and gives the stated endpoint convention.

Thus if `R>=alpha D^2` for fixed `alpha>0`, there are `Omega_alpha(D)` pairwise vertex-disjoint paths to distinct actual loaded attachments. Removing a specified set of `o(D)` graph vertices can destroy only `o(D)` of these paths. Neither statement makes a path length a payment unit or a finite motion.

## 3. A convex exceptional face — PASS WITH EXPLICIT CONVEXITY SCOPE

Let `f` be a convex bounded unit-contact face of the induced contact graph on `I union A`, with degree `m` and `ell` loaded boundary vertices. Then there are at least

`ceil((m-2 ell)_+/(4 pi+2))`

pairwise vertex-disjoint contact paths from its unloaded boundary vertices to distinct actual attachments in `A`.

For a minimum separator of size `k`, deleting its unloaded vertices removes at most `2 k_I` face edges; loaded boundary vertices remove at most `2 ell` more. Every surviving face edge belongs to the boundary of the convex hull of the face vertices in one entirely unloaded component `U_j`. These edges are supporting edges of the convex face, so their total length in `U_j` is at most `per(conv(U_j))<=pi delta_j`. For these selected components, the restricted-rigidity and positive-equilibrium argument gives `t_j>=delta_j+3`. Minimum-separator minimality gives one additional, uncounted contact at each unloaded cut vertex into a component meeting `A`; that component cannot contain an unremoved face-boundary start vertex. Therefore `sum t_j<=4k_I+3k_B`, and `sum delta_j<=4k_I+3k_B`. Consequently

`m-2 ell-2 k_I <= pi(4 k_I+3 k_B) <= (4 pi+2)k`.

The same vertex-flow argument identifies `k` with the path count. Convexity is stated as a hypothesis of this theorem; no conclusion is promoted for a nonconvex face or for summing face perimeter over a family.

## 4. Deep-cap consequence — CONDITIONAL ONLY

The source report's deep-cap calculation is valid under the following explicit additional geometry. Let `C` be a convex cap of diameter at most `D`, bounded in part by a supporting chord `L` and the designated host arc `Gamma`; let signed height `eta` be zero on `L` and nonnegative on `C`. Assume `B intersect int(C)=empty`. Let `G` be a finite family of strict unit rhombus faces in `I`, with disjoint interiors, contained in `int(C) intersect conv(A)`, and total area `A_G`. Assume an attachment `a_* in A` has

`H=eta(a_*)=max_{a in A} eta(a) >= A_G/D`,

and `eta(b)<=0` for every loaded endpoint `b in B outside Gamma`. If `A_G>=16(pi+1)D`, set

`h=A_G/(8 pi D)`, `s=A_G/(4D)`.

Retain the rhombi whose entire faces have distance greater than `h` from `partial C` and height below `H-s`. Call their union `G_0`, their vertex set `X_0`, and their count `R_0`. A discarded face lies either in the inner boundary strip of width `h+2` or in the height strip `H-s-2<=eta<=H`, since a unit rhombus has diameter less than two. Cauchy's perimeter formula gives `per(C)<=pi D`, and each height slice has length at most `D`, so the discarded area is at most

`pi D(h+2)+D(s+2)=3 A_G/8+(2 pi+2)D`.

Hence `area(G_0)>=A_G/2`, and since a unit rhombus has area at most one, `R_0>=A_G/2`. Apply (2) to obtain `p>=F(A_G/2)` disjoint paths from `X_0` to distinct actual attachments. Their lengths exceed `h`, because every loaded endpoint is outside `int(C)` and every retained vertex is deeper than `h`; trimming leaves at least `ceil(h)-1` distinct internal vertices per path in `I\X_0`. In particular, if `A_G>=alpha D^2` with fixed `alpha>0`, then `p=Omega_alpha(D)` and the number of such outside vertices is `Omega_alpha(D^2)`.

At least half the paths end on `Gamma` or at least half end outside it. In the latter case each path crosses `L` from height greater than `h` to height at most zero, giving distinct actual unit-contact edges meeting `L` and distinct source vertices within distance one of `L`. At most one path ends at `a_*`, since endpoints are distinct. The port/chord placement is a conditional structural conclusion only; it gives no source deformation. The existence of this extracted cap and grain remains unpromoted, so this claim is registered as conditional and is not used to change the canonical route by itself.

The separate complete-grid trim in the source report also assumes a coherent grain with perimeter `O(D)` and the Section-78 extraction. It is not promoted here.

## 5. Pinned-grid order regression — REGRESSION VALID

For unit vectors `u,v` with `u dot v=c` in `(0,1/2)`, the lattice grid points `(i,j) -> i u+j v` are unit-separated: for integer differences of the same sign the squared distance is at least one; for opposite nonzero signs it is strictly greater than `i^2+j^2-|ij|>=1`. Equality occurs only for the two unit coordinate steps. Thus the contact graph is the two-axis grid. Equal weights on the four axis contacts balance at every interior vertex. Pin all boundary vertices. The horizontal edge toward the left pin and the second-axis edge toward the bottom pin at each interior vertex give a full-column-rank pinned contact matrix: the two independent lattice projections vanish rowwise and columnwise from their pinned boundaries.

A central `w`-by-`w` cell block has `R=w^2` unit rhombi, and its boundary-vertex ring of size `4w` separates the block from the boundary pins. Consequently a quadratic rhombus population and full pinned rank/positive equilibrium alone permit only `O(sqrt(R))` returns to pins. The report's oblique sequence takes `M=L^2`, `p=floor(M/sqrt(3))+1`, and

`u=(1,0)`, `v=((M^2-p^2)/(M^2+p^2), 2pM/(M^2+p^2))`.

It has `0<u dot v<1/2` and angle `pi/3+O(L^-2)`, so vanishing phase excess does not improve the pinned-only order. These are pinned-framework examples, not canonical source examples: in them the pinned boundary is strictly larger than the actual diameter-endpoint set. They refute no theorem whose pins are all actual loaded endpoints.

The frozen exact verifier was inspected and rerun. It uses `Fraction` arithmetic; it checks 12 square/oblique rank and equilibrium cases, all 2,517 removed-vertex subsets on the stated small board, four exact max-flow grid instances, and rational relaxations of the constants. It corroborates those finite cases only. The arbitrary-`L` lattice and ring arguments above are analytic; the verifier does not prove the universal separator theorems or global optimality.

## Disposition and remaining obligation

- **PASS — promote** the finite rhombus-separator capacity theorem.
- **PASS — promote** the `F(R)` lower bound for vertex-disjoint paths to distinct actual loaded attachments.
- **PASS WITH EXPLICIT CONVEXITY SCOPE — promote** the convex-face return bound.
- **CONDITIONAL ONLY — retain the derivation in this audit artifact.** The deep-cap return and chord fork require the explicit geometric premises above, including an unproved cap/grain extraction; no theorem-state entry or canonical dependency is created for this corollary.
- **REGRESSION VALID — record** the pinned-grid `O(sqrt(R))` limitation; it is not a canonical-source counterexample.
- Do not promote the host-cap extraction, the complete-grid trimming/extraction, any source realization of the pinned grids as canonical global minimizers, or a finite-motion/strict-`D` conclusion.

The result turns quadratic unloaded rhombus bulk into linear simultaneous paths to actual loaded endpoints. The exact C-II obligation becomes to charge those paths, their shared rhombi, and the host/chord endpoint pattern to canonical train/interface/face currency, or to use them in a full-source contact-changing strict sub-`D` replacement. C-II and Level I remain open.

Frozen verifier run: `python3 research/verify_target_c_bulk_separator_2026_10_04.py` at source commit `0e49b450cc4819cc2f4f205303cbb9a09b45d269` returned `PASS: exact finite pinned-grid checks; no global optimality or C-II closure certified`.
