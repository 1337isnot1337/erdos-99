> Generated reading edition · [exact source](../../../docs/audits/target_c_bounded_variation_chart_port_scarcity_independent_audit_2026-10-09.md) · source SHA-256 `6fe7e1a4bf1b9ca34a955a0187508bcc3d980bf7f29494fc03e5f9ed09571bcc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-652F2AB17613","canonical":true,"claim_ids":["C-ACTUAL-DIAMETER-ENDPOINT-STRIP-BOUND","C-BOUNDED-VARIATION-CHART-PORT-SCARCITY"],"claim_statuses":{"C-ACTUAL-DIAMETER-ENDPOINT-STRIP-BOUND":"canonical","C-BOUNDED-VARIATION-CHART-PORT-SCARCITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.212 — bounded-variation chart port scarcity

Date: 2026-10-09. Audit base: `origin/main=85e17a4fab2460f58d32b30e840cec2290cd4244`, state `2026-10-09.audit.205`.

## Frozen candidates and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Primary candidate: Section 14 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Strip-bound proof also appears in Section 12 of `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`.
- Verdicts: **PASS — promote** `C-ACTUAL-DIAMETER-ENDPOINT-STRIP-BOUND`; **PASS WITH EXPLICIT HYPOTHESES — promote** `C-BOUNDED-VARIATION-CHART-PORT-SCARCITY`.

## Actual diameter endpoints in a strip

Let `A` be any finite unit-separated planar source of diameter `D>0`, and let `E` consist of source points that occur in at least one actual diameter pair. For any strip of width `w>=0`,

$$
 |E\cap S|\le 4\sqrt{2Dw}+4w+4.
$$

This statement uses actual diameter endpoints, not arbitrary points in the source.

### Independent proof

Every actual diameter endpoint `q`, with partner `p`, is a strict exposed vertex of `conv(A)`: for every `x!=q`,

$$
 |x-p|^2\le D^2=|q-p|^2
 \quad\Longrightarrow\quad
 (x-q)\cdot(q-p)<0.
$$

Thus the diameter endpoints are in convex position. Their own convex hull has perimeter at least their number, because its sides join distinct unit-separated source points, and its perimeter is at most that of `conv(A)`, hence at most `pi D`. If `w>=D/2`, this global estimate is already below `4 sqrt(2Dw)+4w+4`.

Now suppose `w<D/2`. Use longitudinal and transverse coordinates parallel and perpendicular to the strip. Choose `x_0,x_1` in `E intersect S` at its two extreme longitudinal coordinates, say `s_0<=s_1`. For any `q` in the strip set, let `q_*` be the convex interpolation of `x_0,x_1` with the same longitudinal coordinate as `q`. Then `|q-q_*|<=w`. If `p` is an actual diameter partner of `q` and `lambda=(s-s_0)/(s_1-s_0)`, the weighted square identity gives

$$
 D^2\ge \lambda|p-x_0|^2+(1-\lambda)|p-x_1|^2
 =|p-q_*|^2+\lambda(1-\lambda)|x_1-x_0|^2
 \ge |p-q_*|^2+(s-s_0)(s_1-s).
$$

Since `|p-q_*|>=D-w`,

$$
 (s-s_0)(s_1-s)\le D^2-(D-w)^2\le 2Dw.
$$

Therefore each selected longitudinal coordinate is within `sqrt(2Dw)` of at least one extreme. Split the endpoints into the two resulting groups. Each group lies in a rectangle of width at most `sqrt(2Dw)` and height `w`. Its convex hull has perimeter at most twice the sum of these side lengths. If a group has at least three points, they are all vertices of its hull and consecutive vertices are unit-separated, so its population is at most that perimeter; groups of one or two points are covered by an additive two. Summing the two group bounds gives the displayed estimate. If the extreme longitudinal coordinates coincide, the selected set lies in one rectangle of width zero and height `w`, and the same bound follows directly.

## Bounded-variation additive charts

Consider an unbounded canonical post-ZF C-II sequence in either branch, `D->infinity`, with all source points retained, loaded-hull vertex count `q`, perimeter `P_F`, and `P_F-q=o(D)`. Fix constants `J,C<infinity`. For each source, take at most `J` finite rectangular additive charts

$$
 x_{ij}=x_{00}+iu+jv+a_i+b_j,
 \qquad a_0=b_0=0,
 \qquad \sum_i|a_i-a_{i-1}|+\sum_j|b_j-b_{j-1}|\le C,
$$

where `u,v` are unit rhombic bases with angle in `[pi/3,2pi/3]`. The bases may vary with `D`. A chart position may be unoccupied; every occupied position is a distinct actual source point. At each counted loaded vertex choose one actual unloaded unit neighbor that occupies a position in one of these charts. Then the number `a_D` of such loaded vertices is `o(D)`. The loaded vertex need only have the chosen neighbor; it may have other unit neighbors as well.

### Independent reconstruction

Set `delta_D=D^(-1/4)`. Across the `J` charts, at most `O_{J,C}(D^(1/4))` first- or second-shore increments have length greater than `delta_D`. For each source choose a growing index radius `L_D=floor(D^(1/8))`. Around every bad increment, exclude counted loaded endpoints whose chosen anchor index on that shore is within `L_D` of the increment. The chart position differs from its reference lattice position by at most `C`; the loaded endpoint is within one of its anchor. For the first shore, use the dual functional `alpha(u)=1, alpha(v)=0` (and analogously for the second shore). Its norm is in `[1,2]`; a chart position with first index within `L_D` of a cut has `alpha`-coordinate within `L_D+2C+O(1)` of the cut line, and moving to its loaded neighbor changes that coordinate by at most two. These endpoints lie in a physical strip of width `O(L_D+C+1)` parallel to the other basis vector. The strip theorem bounds each strip's actual diameter endpoints by `O(sqrt(D L_D)+L_D+1)=O(D^(9/16))`. The total excluded population is at most `O_{J,C}(D^(1/4)D^(9/16))=O_{J,C}(D^(13/16))=o(D)`.

Fix any bounded physical loaded window, of diameter at most a constant `R`. Its chosen anchors are within `R+2` of one another. The total chart displacement has norm at most `C`, and the dual basis functionals have norms at most two, so their two index-coordinate differences are at most a fixed integer `L_R=L(R,C)`. For all sufficiently large `D`, `L_D>=L_R`. No bad increment can lie between two retained anchors in the window: it would be within `L_D` of one of their indices and that port would have been excluded. Each shore interval between the indices therefore has at most `L_R` increments, all of norm at most `delta_D`. Their displacement vectors differ by at most `2L_R delta_D=o(1)`. The same retained port subset consequently has uniform `o(1)` approximation by one translate on every bounded physical window, for each fixed window size. The number of charts is fixed and their bases remain in the compact rhombic angle range. Audit.211's `C-NEAR-UNIT-ATLAS-PORT-SCARCITY` applies to this retained port subset, giving `o(D)` retained ports. Adding the `O(D^(13/16))` excluded ports proves `a_D=o(D)`.

This argument counts endpoints only. It does not delete source points, assemble individually feasible exchanges, or treat a selected train grid as an additive chart without the displayed chart hypothesis.

## Dependencies, regression checks, and limit

- The strip theorem is independent of global optimality; its only point-set input is unit separation and the definition of an actual diameter endpoint.
- The chart theorem uses `C-NEAR-UNIT-ATLAS-PORT-SCARCITY`, `C-LOADED-HULL`, and the strip theorem. The middle loaded endpoint and the chosen unloaded anchor are distinct source points; all source isolates remain in the source and in the endpoint count.
- The finite number of charts and their total variation bound must be uniform in `D`. A per-source atlas with growing chart count, unbounded total variation, or only selected-grid positions is outside the claim.
- No finite verifier certifies the strip count or the asymptotic chart reduction. No verifier from the source report is treated as proof of these analytic steps.

**Frontier effect:** none. The result rules out a linear direct-port bank inside finitely many actual additive charts of uniformly bounded total shore variation when `P_F-q=o(D)`. It does not extract such charts or the perimeter-saturation regime, and gives no source motion, strict-diameter competitor, C-II closure, or Level-I conclusion.
