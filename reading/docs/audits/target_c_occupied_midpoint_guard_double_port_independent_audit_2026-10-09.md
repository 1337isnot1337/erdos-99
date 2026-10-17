> Generated reading edition · [exact source](../../../docs/audits/target_c_occupied_midpoint_guard_double_port_independent_audit_2026-10-09.md) · source SHA-256 `200ba12d77e46ffd12e4146e73436322acee10dd44c1b09525719b5a505e9e9b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7E5DEF8BB9B6","canonical":true,"claim_ids":["C-FULLY-OCCUPIED-CHART-CONTACT-PORT-SCARCITY","C-FULLY-OCCUPIED-CHART-DOUBLE-PORT-COUNT"],"claim_statuses":{"C-FULLY-OCCUPIED-CHART-CONTACT-PORT-SCARCITY":"canonical","C-FULLY-OCCUPIED-CHART-DOUBLE-PORT-COUNT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: occupied midpoint guards for bounded-variation charts

## Frozen source and authority

- Audit base: `origin/main=8d44cfb00654515ad9937e301e247e8aaa316518`, state `2026-10-09.audit.211`.
- Frozen candidate: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate artifact: Section 15.1 of `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`.
- The frozen report hash was recomputed from that commit. No later discovery-branch changes were mixed into this audit.
- Canonical inputs: `C-CURVED-BOUNDARY-LATTICE-LOCAL-CAPACITY`, `C-BOUNDED-VARIATION-LATTICE-ENDPOINT-COUNT`, `C-ACTUAL-DIAMETER-ENDPOINT-STRIP-BOUND`, `C-BOUNDED-VARIATION-LEAF-PORT-COUNT`, `C-MIXED-CORE-ONE-ROW-REDUNDANCY`, `C-ZRF`, and `C-WOODALL`.

## Exact claims

1. **Arbitrary-source double-port theorem.** Let (A_D) be finite unit-separated planar sources with diameter (D\to\infty). For each source, suppose at most a fixed (J) finite rectangular additive charts are supplied,
   $$
   p_{ij}=p_{00}+iu_0+jv_0+a_i+b_j,
   $$
   where (u_0,v_0) are unit vectors with angle in ([\pi/3,2\pi/3]), the total shore variation is at most a fixed (M), and **every integer position in each rectangle is occupied by a distinct actual point of (A_D)**. Count actual diameter endpoints (p) that have two distinct actual unit neighbors occupying positions in one such chart. The number of distinct counted endpoints is (O_{J,M}(D^{4/5})). Other source points are unrestricted and retained. No optimality or KKT assumption is needed.

2. **Canonical contact-port corollary.** On an unbounded canonical post-ZF triangle-free C-II sequence, under the same fixed-family fully occupied chart hypothesis, call a loaded endpoint chart-covered if it is a contact leaf whose sole actual unit neighbor occupies a chart site, or if it has two distinct actual unit neighbors in one chart. Then the covered population is (O_{J,M}(D^{4/5})), and at least (D-O_{J,M}(D^{4/5})) loaded endpoints remain uncovered. The contact-leaf clause uses positivity of its actual contact in a normalized full-source KKT stress, supplied for canonical core edges by `C-MIXED-CORE-ONE-ROW-REDUNDANCY`; the linear lower bound uses (q\ge h\ge\lceil D\rceil) from `C-ZRF` and `C-WOODALL`.

## Independent reconstruction

Write (r=D^{4/5}) and $\delta=r/(16D)=D^{-1/5}/16$. Partition each chart shore into consecutive blocks of total within-block displacement variation at most $\delta$. The number of cuts is (O_M(D/r+1)). If a counted endpoint is outside constant-width physical strips around those cuts, both selected anchor labels lie in the same pair of shore blocks: each chart point differs from its reference lattice label by at most the total variation (M), and each anchor is within one unit of the endpoint. The actual-diameter-endpoint strip theorem removes only

$$
O_M((D/r+1)\sqrt D)=O_M(D^{7/10})
$$

endpoints at this choice of (r).

For two selected anchors (a,b), their unit separation and their being distinct give (1\le |b-a|\le2). On one block pair, let $\lambda_a,\lambda_b$ be the reference lattice labels and put (w_0=\lambda_b-\lambda_a). The block variation gives

$$
|(b-a)-w_0|\le4\delta.
$$

Thus (|w_0|\le3) for large (D). Writing (w_0=i u_0+jv_0), the rhombic Gram bound
$$
|iu_0+jv_0|^2\ge(i^2+j^2)/2
$$
leaves only the finite offset set (i^2+j^2\le18).

Round the coefficient midpoint of the two anchor labels to an integer label $\lambda_c$ inside their coordinate bounding box. If one coordinate is half-integral, a nearest round costs (1/2). If both are half-integral, the better of the two diagonal choices costs
$$
\tfrac12\min(|u_0+v_0|,|u_0-v_0|)\le1/\sqrt2.
$$
An integral midpoint costs zero. The rounded label stays in the same shore-block pair. Full rectangular occupancy supplies an actual source point (c) at that label. Since the chart bow at each of the three labels differs from the block base bow by at most (2\delta),
$$
|c-(a+b)/2|\le1/\sqrt2+4\delta.
$$

Endpoints that themselves occupy the chart are counted separately by canonical `C-BOUNDED-VARIATION-LATTICE-ENDPOINT-COUNT`, giving (O_{J,M}(D^{4/5})). For every remaining double-port endpoint (p), (p\ne c), so full-source unit separation gives (|p-c|\ge1). Put $\kappa=(1-1/\sqrt2)/2>0$. For sufficiently large (D), (|c-(a+b)/2|\le1-\kappa), hence
$$
|p-(a+b)/2|\ge\kappa.
$$
Because (|p-a|=|p-b|=1), the midpoint identity gives
$$
|p-(a+b)/2|^2=1-|a-b|^2/4,
$$
and therefore
$$
1\le|a-b|\le2\sqrt{1-\kappa^2}<2.
$$

The selected anchor differences thus lie in a fixed compact annulus away from both zero and two. The circle-intersection map
$$
F(w)=w/2\ \mathord\pm\ (Jw/|w|)\sqrt{1-|w|^2/4}
$$
is uniformly Lipschitz there. The (4\delta) anchor error consequently gives (O(\delta)) endpoint error, rather than the square-root error at tangency. For each finite lattice offset and each sign, the endpoints in a patch lie within (O(\delta)) of one translated reference rhombic lattice.

Actual diameter endpoints lie on the boundary of the full-source ball hull (W=\bigcap_{x\in A_D}\overline B(x,D)). Their convex hull has perimeter at most $\pi D$, and the cut lines divide its boundary into (O_M(D/r+1)) arcs. Subdivide these arcs into patches of diameter (O(r)); patch centers lie in (W). Canonical local curved-boundary capacity bounds one offset group in one patch by
$$
O_M(r\delta+(Dr)^{1/3}+1).
$$
There are only a fixed number of offsets and signs. Summing the patches and cut strips yields
$$
O_M\!\left(r+D^{4/3}r^{-2/3}+D/r+D^{3/2}/r\right)=O_M(D^{4/5}),
$$
since (r=D^{4/5}). Adding endpoints that occupy the chart gives the same order. A fixed (J)-chart union multiplies the constant.

For the canonical corollary, `C-BOUNDED-VARIATION-LEAF-PORT-COUNT` bounds the positive-stress leaf ports by (O_{J,M}(D^{4/5})). `C-MIXED-CORE-ONE-ROW-REDUNDANCY` supplies a positive coefficient on every actual contact edge of the canonical core, so every contact leaf's sole edge meets this condition. The new double-port theorem bounds the other covered class. Finally `C-ZRF` gives (h\ge\lceil D\rceil), while `C-WOODALL` gives (q\ge h). Subtracting the covered count proves the stated linear uncovered population.

## Hostile checks and scope

- Full occupancy is essential to this proof: a selected crossing grid or a chart with holes need not contain the rounded midpoint guard. The older square-root/tangency estimate remains the correct bound for arbitrary occupied subsets.
- If (p) itself occupies a chart site, it is not assumed distinct from a guard; it is placed in the separately counted chart-endpoint class.
- The guard (c), anchors (a,b), and endpoint (p) are actual points of the full source. Contact-isolated points and every other source point remain in the unit-separation and diameter geometry.
- The proof counts only actual diameter endpoints. It says nothing about arbitrary contact endpoints that are not on the diameter boundary.
- The canonical corollary counts only the two chart-port classes defined above. Endpoints with exactly one charted neighbor and additional off-chart neighbors are not automatically covered.
- No chart is extracted from a canonical minimizer, and no source move, strict diameter decrease, C-II closure, or Level-I conclusion follows. Audit.216 already forced a linear uncovered population under the weaker (O(D^{6/7})) double-port estimate; this audit sharpens the rate under full rectangular occupancy without changing the qualitative frontier.

## Verifier boundary and verdict

There is no candidate finite verifier: the midpoint geometry, Lipschitz estimate, and asymptotic patch sum are analytic. Repository certificates do not encode or certify these implications. No verifier output is used as mathematical evidence.

**Verdict:** PASS — promote `C-FULLY-OCCUPIED-CHART-DOUBLE-PORT-COUNT` and its canonical corollary `C-FULLY-OCCUPIED-CHART-CONTACT-PORT-SCARCITY`.

**Frontier effect:** none. The full-rectangle hypothesis is not extracted from a canonical C-II source. C-II and Level I remain open.

**Discovery-worker protection:** audited only Section 15.1 at frozen commit `6132201c1d3056ca68a222217094acb819f5b4d7`; no discovery branch or worktree was modified.
