> Generated reading edition · [exact source](../../../docs/audits/target_c_finite_atlas_single_port_scarcity_independent_audit_2026-10-09.md) · source SHA-256 `525d4f8febbf5c9c1fd725ebfc9a3b939e0796727e9d1180718db08f4afd93a9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2E957AFCE925","canonical":true,"claim_ids":["C-FINITE-ATLAS-SINGLE-PORT-SCARCITY"],"claim_statuses":{"C-FINITE-ATLAS-SINGLE-PORT-SCARCITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.210 — finite-atlas single-port scarcity

Date: 2026-10-09. Audit base: `origin/main=29c314882b482d225ea2592724b922df01936338`, state `2026-10-09.audit.203`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate artifact: Section 13.5 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Verdict: **PASS WITH NARROWED SCOPE — promote** `C-FINITE-ATLAS-SINGLE-PORT-SCARCITY` under the explicit finite-rhombic-atlas and local-approximation hypotheses. I record the finite block count with an explicit additional `2m` endpoint charge for nonunit sides at block boundaries; the asymptotic conclusion is unchanged.

## Exact conditional theorem

Let a canonical post-ZF C-II source sequence have `D->infinity`, `q` actual loaded hull vertices, and `m` nonunit loaded-hull sides. Let `W_D` be a subset of loaded vertices, with one chosen actual unloaded unit neighbor at each member, and let `a_D=|W_D|`. Assign these neighbors to a fixed finite number `J` of charts. Each chart has a unit-rhombic reference lattice with basis angle in `[pi/3,2pi/3]`; its basis may vary with `D`.

Assume that for every fixed block size `M`, in every run of at most `M` consecutive loaded vertices whose intervening loaded-hull sides are unit, the neighbors assigned to any one chart lie within a common error `epsilon_{D,M}->0` of one translate of that chart's reference lattice. This error is uniform over windows and charts. Then

```math
 m=o(D)\quad\Longrightarrow\quad a_D=o(D).
```

The theorem does not require a small number of chart transitions or consecutive port coverage. The local atlas and `m=o(D)` are hypotheses, not consequences of canonical C-II structure.

## Independent reconstruction

### Straightening bounded unit runs

Audit.206 supplies `|m_p-o|<=7D^(2/3)` for every actual diameter midpoint and a one-sided support-derivative bound `|h'|<6D^(2/3)`. Thus each actual diameter endpoint `p` has `|p-o|>=D/2-7D^(2/3)`. By `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, a unit pair of loaded endpoints is a full-source hull side for all sufficiently large `D`. At that side's normal, the one-sided support derivatives are its endpoints' tangential coordinates, so the side normal differs from the endpoint radial direction by `O(D^(-1/3))`. Across a fixed `M`-vertex unit run the radial directions vary by `O(M/D)`. Every such run therefore converges, after normalization, to a straight unit chain. This uses the full source hull and retains contact isolates.

### Distinct ports and finite chart patterns

Within a fixed `M`-vertex unit run, distinct chosen ports have distinct actual neighbors for all sufficiently large `D`. Adjacent loaded sites cannot share a neighbor because that would form a unit triangle. If port indices differ by at least three, the limiting loaded-site distance is greater than two, so a common unit neighbor is impossible. If the indices differ by two, a common unit neighbor would converge to the intervening loaded vertex; that contradicts its source-separation distance of at least one from the unloaded neighbor. Compactness makes these exclusions uniform over the bounded windows.

For fixed `M`, any two neighbors in one chart are at bounded physical distance (at most `M+2+o(1)`). The inverse basis functionals have norm at most two throughout the stated rhombic angle range. Therefore only finitely many integer lattice-offset patterns can occur in one block, uniformly over the bases. Distinct actual neighbors round to distinct lattice sites once `2epsilon_{D,M}<1`.

Take a block with more than `2J` selected ports. Three belong to one chart, at loaded indices `i,i+r,i+s` with `0<r<s<M`. Along any subsequence, the finitely many chart bases have a convergent subsequence; for fixed `M`, pass again so the chart label and lattice-offset pattern are fixed. Normalize one loaded site and one lattice site. The three limiting unloaded anchors are distinct, and the loaded run converges to `z,z+rt,z+st`. `C-THREE-PORT-FINITE-DIRECTION-BOUND` gives at most ten possible limiting directions for this pattern. There are finitely many charts and patterns, so all rich-block tangents lie within `tau_{D,M}->0` of one fixed finite direction set. This is a compactness conclusion; no continuity of polynomial roots under changing bases is assumed.

### Actual-normal count and block ledger

Every loaded vertex in a rich block that is not incident to a nonunit loaded-hull side has two unit incident sides. The block tangent result controls the sides inside the block; if a unit side crosses a block boundary, radialization at their shared loaded endpoint forces its tangent to agree with the block tangent up to `o(1)`. The nonunit boundary endpoints were already included in the `2m` charge. Thus both side normals, and hence the vertex's actual diameter normal inside their normal cone, lie in a shrinking window around one of finitely many perpendicular directions. The audited Audit.203 normal-window bound is

```math
1+\frac{D\sin(tau_{D,M})+2L_D}{\cos(tau_{D,M})}=o(D),
\qquad L_D=\sqrt{D\eta_D+\eta_D^2}=o(D),
\quad \eta_D=3^{1/4}\sqrt D.
```

The finite direction set depends on fixed `M` and `J`, so the number of these good loaded vertices over all rich blocks is `o_M(D)`. There are at most `2m` loaded endpoints incident to a nonunit side; charge them separately.

Partition the cyclic loaded sequence into blocks of at most `M` vertices. Discard every block containing an internal nonunit side; at most `m` blocks are discarded, costing at most `Mm` vertices. Nonunit sides on block boundaries are covered by the separate `2m` endpoint charge. Each remaining nonrich block has at most `2J` selected ports, and there are at most `ceil(q/M)+1` blocks. Consequently, for every fixed `M`,

```math
 a_D\le (M+2)m+2J\bigl(\lceil q/M\rceil+1\bigr)+o_M(D).
```

The explicit `2m` charge makes the finite ledger valid without assuming a partition cut avoids every nonunit side. Since the loaded hull chords have length at least one and the full-source hull perimeter is at most `pi D`, `q<=pi D`. If `m=o(D)`, divide the inequality by `D`, take the limit at fixed `M`, then let `M->infinity`; this gives `a_D=o(D)`. The order of limits is essential.

## Dependencies and hostile scope

- `C-FS-GEOM` supplies the perimeter bound; `C-FS-DIAMETER-MIDPOINT-D2-3` supplies the midpoint and support-derivative estimates; `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE` supplies full-source sides.
- `C-THREE-PORT-FINITE-DIRECTION-BOUND` controls the three distinct limiting anchors. `C-LOADED-WALK-DIRECTIONAL-STRAIN` is used only for its audited actual-diameter-normal window inequality. `C-LOADED-HULL` supplies the canonical loaded set and variables.
- The proof never identifies a neighbor chart with a positional chart on its loaded endpoint, and does not infer a global lattice phase or chart extraction. The source report's K/D slow-chart corollary is not separately promoted here.
- All source points, including contact isolates, remain in the separation, hull, and support arguments. Triangle-freeness is used only for adjacent-port noncoincidence.
- No finite verifier certifies the compactness and asymptotic argument. Audit.209's finite direction theorem and the existing Audit.203 normal-window theorem are reused only in their stated scopes.

**Frontier effect:** none. The conditional theorem gives no actual atlas, no sublinear bound on `m`, and no source move, capacity, strict-diameter competitor, C-II closure, or Level-I conclusion.
