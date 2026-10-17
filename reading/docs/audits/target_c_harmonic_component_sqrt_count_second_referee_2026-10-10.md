> Generated reading edition · [exact source](../../../docs/audits/target_c_harmonic_component_sqrt_count_second_referee_2026-10-10.md) · source SHA-256 `31767f698d4354ce7764e3d5b1a40f26fe8fa705635297a4a7e85126b3b9e3da`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-70BBC912FFBE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent second referee — harmonic component square-root count

Date: 2026-10-10. Canonical audit base: `origin/main=c89aa7f2becfe2b2608a9b715d7753245d94f625`, state `2026-10-10.audit.230`.

Frozen candidate: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`. Candidate artifact: `docs/reports/target_c_disjoint_attachment_cell_square_root_count_2026-10-09.md`, SHA-256 `89b840f869d135f3ce509f8e248ce5a74c829d1aa15cbcefe5e12d54d115dced`. The frozen branch and candidate were not modified.

## Verdict

**PASS — independently rechecked; theorem remains canonical as `C-HARMONIC-COMPONENT-SQRT-COUNT`.** The exact short-component estimate and its square-root consequence survive reconstruction from the canonical premises. This second referee adds no new theorem-state claim, dependency, or frontier change; Audit.200 remains the original promotion record.

## Exact scope

For every sufficiently large canonical post-ZF C-II source in either canonical alternative, let `I_r` range over the unloaded connected components of the nonisolated positive-contact core, let `delta_r` be their positive-contact graph diameters, and let `c_I` count only these components. Contact-isolated source points remain in the full source and are outside this count. For every integer `M>=0`, the claim is

$$
N_M:=\#\{r:\delta_r\le M\}\le12{,}000{,}000\pi(M+2).
$$

With the canonical budget `sum_r delta_r<=2+2*pi*D`, this implies

$$
c_I\le12{,}000{,}000\pi(\lfloor\sqrt D\rfloor+2)
 +\frac{2+2\pi D}{\lfloor\sqrt D\rfloor+1}=O(\sqrt D).
$$

Canonical dependencies are `C-COMP-DEATOMIZATION` (harmonic trapping, degree and graph-diameter facts, local arc control, and eventual force-hull fatness) and `C-HARMONIC-CELL-TILING` (interior disjointness of the actual attachment cells). No selected-grid proxy is used.

## Independent reconstruction

### Cell width and curvature-window count

For an unloaded core vertex `x`, choose three distinct unit-contact neighbors. Harmonic trapping puts `x` and all three neighbors in the actual convex attachment cell `P_r`. If they fit in a strip of width below `1/2`, their three unit directions from `x` satisfy `|n dot u|<1/2` for the strip normal `n`. The allowed directions lie in two open arcs of angular width `pi/3`; each arc contains at most one direction because two directions less than `pi/3` apart give neighbors less than unit distance apart. This contradicts three neighbors. Thus `minwidth(P_r)>=1/2`, including singleton core components.

For the analytic counting lemma, take a maximum-area triangle `T` among the vertices of each convex cell `Q`. Replacing a vertex of `T` by `x in Q` multiplies signed area by the corresponding barycentric coordinate. Maximality and affinity over `Q` give `|lambda_i|<=1`; hence `Q` lies in the factor-four homothet of `T` about its centroid and `minwidth(T)>=minwidth(Q)/4`. A triangle's inradius is at least one third of its minimum width, so each selected triangle has inradius at least `w/12` when `Q` has minimum width `w`.

Place pairwise interior-disjoint cells with vertices on a concave piecewise-affine graph inside the cap above its endpoint chord. Concavity puts every graph vertex on or above each chord between graph points, so no graph vertex lies strictly inside a selected triangle. A graph vertex on an edge can only occur where that chord is part of the graph boundary; two nondegenerate triangles on the same interior side of that boundary cannot both meet there with disjoint interiors. Thus the selected triangles form a noncrossing straight-line complex, with no T-junction, and can be retained as faces when the cap is triangulated. This handles nested horizontal spans and shared cell boundaries.

Root that triangulation at the endpoint chord. At a triangle with horizontal runs `l_1,l_2` and adjacent secant slopes `s_1>=s_2`, area and semiperimeter give

$$
r_T\le\frac12\min(l_1,l_2)(s_1-s_2).
$$

Writing the nonnegative slope-drop measure as `mu=-f''`, the secant difference is the integral against `mu` of the triangular tent kernel supported on the interval of that triangle. For a fixed curvature location `t`, triangles with nonzero kernels follow the single rooted path through the nested interval tree: at a split vertex the parent kernel is one and the path terminates. At each step, `min(l_1,l_2)` is no greater than the horizontal length removed when passing to the child interval containing `t`; these lengths telescope to at most the original interval length `X`. Since each kernel is at most one, integration yields `sum_T r_T<=XV/2`, where `V` is total slope drop. Therefore the number of cells is at most `6XV/w`, and in particular at most the canonical loose bound `12XV/w`.

For cells with `delta_r<=M`, set `L=M+2`. Canonical trapping puts all attachments within distance `L` of a representative. If `L>D/10^6`, the width bound forces each counted component to have at least three distinct loaded attachments. Each loaded vertex has contact degree at most three, so `3N_M<=3q`. Consecutive vertices of the loaded convex polygon are unit-separated, hence `q<=per(F)`; Cauchy's perimeter formula and `diam(F)<=D` give `per(F)<=pi D`. Thus `N_M<=q<=pi D<10^6*pi*L`.

Otherwise, the canonical local arc lemma puts each cell's attachments in an arc of boundary radius `22L`. Since `B(o,D/20) subset F`, Cauchy's formula gives `per(F)>=pi D/10`. With `L<=D/10^6`, this perimeter is much greater than `22L`; taking `floor(per(F)/(22L))` equal blocks gives block lengths in `[22L,44L]`. Extend each block by `22L` on both sides. Each assigned cell is contained in the cap under one concave graph of span at most `88L`.

The fat-hull bounds imply every supporting normal has radial component at least `1/11`. Across an extended arc, radial direction changes by at most `1760L/D<=0.00176`; consequently all supporting normals have component greater than `1/22` in the chosen radial direction. Projection onto the perpendicular axis is strictly monotone, the arc is an upper concave graph with slope magnitude at most `22`, and slope drop is at most `485*Theta`, where `Theta` is that arc's exterior turning. Applying the cell count with `w=1/2`, `X=88L`, and `V=485*Theta` gives `1,024,320 L Theta` cells per block. Every boundary point, including block endpoints carrying curvature atoms, belongs to at most five expanded blocks. Total hull turning is `2*pi`, so summing gives `N_M<=10,243,200*pi*L<12,000,000*pi*L`.

Finally, the canonical diameter budget bounds the number with `delta_r>=M+1` by `(2+2*pi*D)/(M+1)`. Taking `M=floor(sqrt(D))` gives the claimed `O(sqrt(D))` count. This implication concerns component count only; it supplies no component-population estimate or source motion.

## Hostile scope and verifier record

- Actual convex attachment cells are used; their pairwise interior-disjointness is the canonical Section 83 theorem. The proof does not assume their horizontal spans are disjoint.
- Contact-isolated labels are retained in the source and are not counted or bounded by this theorem.
- The curvature-window proof is analytic. There is no finite verifier for the universal arc/curvature argument, and no numerical computation is used as proof evidence.
- The improved component error sharpens the pinned ledger only. It gives no spare packing capacity, finite competitor, C-II closure, or Level I conclusion.

**Disposition.** PASS — already canonical at exactly this scope under `C-HARMONIC-COMPONENT-SQRT-COUNT`; no state-version increment or route/prompt edit is warranted. C-II and Level I remain open. No discovery branch or worktree was modified.
