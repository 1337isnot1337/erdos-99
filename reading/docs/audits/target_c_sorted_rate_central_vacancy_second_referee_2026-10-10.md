> Generated reading edition · [exact source](../../../docs/audits/target_c_sorted_rate_central_vacancy_second_referee_2026-10-10.md) · source SHA-256 `045f8a60b6f7a92dbbf3b3df39b8b785de9d00cb4d05c846d625a1a26fbab3f1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-56780884D4DE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent second referee — central-vacancy sorting classification

Date: 2026-10-10. Canonical base: `origin/main=1473f4165b7b5fb0fc3284d35a866493a5b468b8`, state `2026-10-10.audit.230`.

Frozen source: `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`. Candidate report: `docs/reports/target_c_sorted_rate_packet_classification_2026-10-06.md`, SHA-256 `964e7d9dacd942e8dd5114217f271e79454a9222069fb8e125e882f281271fe4`. Finite verifier: `research/verify_target_c_sorted_rate_packets_2026_10_06.py`, SHA-256 `67f73a8f48757aef8a1c7aca4e4ba7c9a3803f44eea8220dfc78912e4178b061`.

## Verdict

**PASS — Audit.234 survives independent reconstruction at its stated local-chart scope.** This report is a second-referee confirmation, not a new theorem promotion. The result classifies only feasible sequences converging to the fixed-`M` punctured triangular chart; it does not classify arbitrary `N-1`-point clouds, extract the chart from a source, or imply C-II or Level I.

## Exact statement

Fix `M>=3`, `N=3M^2-3M+1`, and the specified arithmetic six-sided curved unit wall with all `6M` wall vertices retained. Let `Lambda={M-1,M-3,...,-M+1}`. For any sequence `theta_k -> 0` of feasible placements of exactly `N-1` additional pairwise unit-separated points in the closed wall, assume that after wall alignment and relabeling the added points converge to the radius-`M-1` triangular-lattice chart with its center omitted.

Then the sequence is eventually, at each sufficiently large `k`, exactly one of the finite sorting packets indexed by a permutation of `Lambda`, with the central site omitted. Each such packet contains `6(M-2)` actual interior unit equilateral triangles. The onset and constants may depend on fixed `M`; no statement covers placements outside the punctured-chart neighborhood.

## Independent proof reconstruction

### First-order equality field

The missing center is not silently restored as a source vertex. On the radius-one ring, the ring rows make its six velocities a common infinitesimal rotation, with coefficient `alpha_1`; use `alpha_0=0` only to define `t_0=alpha_1`. The outer corner velocity is zero, so `alpha_M=0`, and `t_r=alpha_(r+1)-alpha_r` has total sum zero.

In a sector, the two non-axis neighbor rows give

```text
s_(r,j) >= s_(r-1,j),
s_(r,j) >= s_(r-1,j-1)-t_(r-1),
s_(M,j) = j(M-j).
```

For paths to the outer wall that do not use `t_0`, start at `s_(1,0)=0`; for paths that do use it, start at `s_(1,1)=-t_0`. Thus the punctured chart still yields every subset inequality `-sum_(i in I)t_i <= |I|(M-|I|)`, including subsets containing `t_0`. With `sum t_i=0`, these inequalities describe the permutahedron whose vertices are the permutations of `Lambda`. Therefore `sum t_i^2 <= M(M^2-1)/3`.

The radius-one ring together with the six radial chains is a positive selected stress on actual unit rows, equilibrated at all moving vertices. Its quadratic velocity energy is

```text
6 alpha_1^2 + 6 sum_(r=1)^(M-1) t_r^2 = 6 sum_(r=0)^(M-1) t_r^2.
```

Summing the lower-distance inequalities cancels moving first-order terms. The six outer corners contribute `12(L(theta)-M)=-12C theta^2+O(theta^4)`, where `C=M(M^2-1)/6`, so the second-order stress inequality gives energy at least `12C=2M(M^2-1)`. This meets the permutahedron upper bound. Equality in the strictly convex squared norm forces `t` to be a permutation of `Lambda`. The sector recurrences then force each coordinate to be the negative sum of the `j` smallest rates in its prefix. This leaves finitely many first velocities and no continuous equality family.

### Exact packets and triangles

For a rate order `tau`, set `z_h=exp(i tau_h theta)`. In each sector, take the layer prefix sum of the `z_h` and add the sum over the `j` smallest rates of that prefix in the second triangular direction; rotate the sector through six angles and omit the center. Ring edges and two predecessor edges have length one. The remaining limiting unit rows open to first order because the rates are distinct; every other pair has strict separation slack at the flat chart. Strict interior containment of the nonboundary sites persists for sufficiently small fixed-`M` `theta`.

At each layer `r=2,...,M-1`, the two selected sites and their predecessor have edge vectors `z_h u`, `z_h v`, and `z_h(v-u)`. They give one exact unit triangle in each sector. The omitted center only removes the layer-one triangles, leaving exactly `6(M-2)` interior triangles.

### Local isolation and sequence quantifier

Let `P` be the bounded first-order feasible polytope after the ring/radial equalities. Each other limiting unit row is strict in at least one sorting velocity, by reversing the order of the distinct rates that control that row. Averaging the finite sorting velocities gives strict slack in every weak row. At a fixed sorting velocity `d_*`, the corresponding quadratic stress energy has a unique maximizing linear functional on `P`: equality in `t_* dot t <= |t_*|^2` forces `t=t_*`, and the sector recurrences fix all remaining coordinates. Its gradient therefore lies in the relative interior of the normal cone.

The active rows are exactly the moving-involving unit contacts of the finite packet. Their limiting matrix `R_0` has full column rank: a kernel vector would preserve every active row, while all inactive rows have slack, so both signs of a small line segment would lie in `P`, contradicting the unique maximizer. Start with the positive radius-one stress and add small positive multiples of the other nested stresses, so every strong row has positive zeroth-order weight. Relative-interior normal-cone membership supplies a first stress correction positive on each active weak row; signed corrections on strong rows do not remove their positive zeroth-order weights. A bounded right inverse of `R_theta^T` corrects the `O(theta^2)` residual, giving an exact pinned equilibrium with strong weights bounded below and weak active weights at least `c theta`.

For any nearby feasible displacement `delta`, each old unit-contact row is at least `-C|delta|^2`. The positive equilibrium makes their weighted sum zero, so every row is at most `C'|delta|^2/theta`. Uniform full rank then gives `|delta| <= C''|delta|^2/theta`; hence the packet is isolated within a radius proportional to `theta`.

The canonical `C-ONE-VACANCY-FLAT-PINNING-RATE` applies to this fixed punctured chart and gives displacement `O(theta)` for a convergent feasible sequence. Every normalized subsequential velocity is one of the finitely many sorting velocities. The sequence therefore differs from its matching exact packet by `o(theta)`, inside the local-isolation radius, and must equal that packet. This is an eventual-sequence conclusion; it does not assert a classification of arbitrary `N-1` clouds or uniformity in `M`.

## Adversarial checks and computation boundary

- Checked the central-vacancy base case explicitly: starting paths at both radius-one sites supplies inequalities for subsets with and without `t_0`.
- Checked that the stress support consists of actual ring/radial unit rows and retains the six outer-corner second-order term; no missing center row is used.
- Checked the normal-cone sign: weak active lower rows receive positive first-order weights, while strong rows may have signed first corrections because their base weights are strictly positive.
- Checked that rank is needed for the finite pinned packet only; the proof does not infer rank of an arbitrary source contact graph.
- Inspected and reran the frozen exact verifier. It uses `Fraction` and exact `Q(sqrt(3))` sign arithmetic; it passed 37,773 pair checks, 2,412 first-row checks, and 1,016 subset checks over its listed finite cases. Its modular rank checks certify only those integer matrices. The verifier does not prove the all-`M` polytope, stress continuation, compactness, or arbitrary-cloud classification; those are handled, where applicable, by the analytic argument and canonical pinning dependency.

## Canonical disposition

Audit.234 already promotes `C-SIX-SIDED-WALL-CENTRAL-VACANCY-CLASSIFICATION` with dependencies `C-ONE-VACANCY-FLAT-PINNING-RATE` and `C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND`. This second referee finds no correction, new theorem ID, state-version increment, or route-map change warranted. The Target C frontier is unchanged: the central-vacancy chart does not resolve arbitrary one-deficit clouds or provide a source extraction or move. C-II and Level I remain open.
