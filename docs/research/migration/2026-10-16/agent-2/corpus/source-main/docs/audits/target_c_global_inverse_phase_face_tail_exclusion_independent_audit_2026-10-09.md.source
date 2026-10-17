<!-- theorem-state: {"artifact_id":"ART-6ECD86C6A2BC","canonical":true,"claim_ids":["C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION"],"claim_statuses":{"C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.202 — global inverse-phase and vanishing face-tail exclusion

Date: 2026-10-09. Audit base: `origin/main=3fee7c922dc5e6c1ec766ef8898c13105c8dd0de`, state `2026-10-09.audit.195`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate report: `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Auxiliary chart theorem: `docs/reports/target_c_localized_curved_boundary_slow_lattice_deformation_2026-10-09.md`, SHA-256 `2bc5da1876e0b2cd079fe2c533b62c8d884a61d845a90cb652dcfbcf28cf5a48`, independently promoted in Audit.201.
- Verdict: **PASS WITH NARROWED SCOPE — promote** `C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION` exactly under the hypotheses below. No implication from selected trains or selected grids to the global phase premise is included.

## Exact statement

Consider an unbounded sequence of canonical post-ZF C-II sources in the contact-minimal, then actual-diameter-pair-minimal triangle-free normal form, with diameters `D -> infinity`. Retain all source labels, including contact isolates. Let `G=(V,C)` be the connected positive unit-contact core, `B` the set of all actual diameter endpoints, `q=|B|`, and `F=conv(B)=conv(V)`. Add every missing straight hull side between consecutive vertices of `B` to form `Ghat`.

For each bounded face `Q` of `Ghat`, define `m(Q)` to be its unit-contact boundary length if it is an old bounded contact face, and the number of actual unit-contact edges on its simple path boundary if it is a convex pocket. Put

\[
T_M(D)=\sum_{Q:m(Q)>M}m(Q),\qquad M\ge4.
\]

Fix `K<infinity`. Suppose each source has a unit triangular frame

\[
U_D=\{\pm u_D,\pm v_D,\pm(v_D-u_D)\},\quad |u_D|=|v_D|=1,
\quad \angle(u_D,v_D)=\pi/3,
\]

such that every oriented actual unit-contact edge vector of `G` is within `K/D` of one of the six frame vectors, and suppose

\[
\lim_{M\to\infty}\limsup_{D\to\infty}T_M(D)/D=0.
\]

Then no such unbounded sequence exists. More quantitatively, the assumptions imply `q=o(D)`, whereas the canonical `C-ZRF` bound gives `h>=ceil(D)` for the number `h` of actual diameter edges and `C-WOODALL` gives `h<=q`.

The frame may vary with `D`. The phase premise covers every actual contact in the positive core, including contacts on exceptional faces. Contact isolates remain in the full source and in the ball hull used for counting. Every actual diameter endpoint belongs to `V`: `C-RHOMBUS-POP` gives `F=conv(B)=conv(V)`, while the strict full-source support inequality from an actual diameter partner makes each point of `B` an exposed point of `F`, hence a point of `V`. The result says nothing about a selected subset of contacts, local grains, or a chart family without the stated common frame and tail condition.

## Canonical geometry and dependencies

`C-RHOMBUS-POP` supplies the connected core, `F=conv(B)=conv(V)`, the convex hull augmentation, convex old contact faces, and the new convex pockets. In particular, the pockets are the bounded regions of `Ghat` that open to the unbounded face when the auxiliary hull sides are removed; they are not contact cycles. The strict full-source support inequality at an actual diameter endpoint then implies that the endpoint is exposed in `F`; no generic isolate perturbation theorem is needed. `C-ZRF` and `C-WOODALL` give the final inequalities `h>=ceil(D)` and `h<=q` respectively. `C-SLOW-LATTICE-DIAMETER-ENDPOINT-BOUND` is the already audited geometric endpoint-count theorem used after constructing one chart.

Dependencies recorded for the new claim: `C-RHOMBUS-POP`, `C-SLOW-LATTICE-DIAMETER-ENDPOINT-BOUND`, `C-ZRF`, and `C-WOODALL`.

## Independent reconstruction

### Face-tail control and zero holonomy

Let `M_0(D)` be the largest length of an old bounded contact face. For every fixed `M`,

\[
M_0(D)\le M+T_M(D).
\]

Consequently `limsup_D M_0(D)/D <= limsup_D T_M(D)/D`; taking `M -> infinity` gives `M_0(D)=o(D)`. Assign each oriented actual contact edge its nearest frame vector and negate that assignment on the reverse orientation. For large `D` the nearest vector is unique. Around an old bounded face of length `m`, the actual edge vectors sum to zero, so the assigned lattice vectors have sum of norm at most `mK/D=o(1)`. A nonzero vector of the unit triangular lattice has norm at least one, hence every such face has zero assigned sum.

The bounded facial cycles of `G` are precisely the old contact faces: each auxiliary hull side opens its pocket to the unbounded face when removed. Bounded facial cycles generate the cycle space of a connected plane graph, with bridge traversals canceling in opposite orientations. Thus every closed walk in `G` has zero assigned sum. Path integration defines a map `ell:V -> Z u_D+Z v_D`, unique up to translation, with the assigned vector as each edge increment. Set `g(p)=p-ell(p)`; every actual contact edge has displacement increment at most `K/D`.

### Actual contact routing with the face-tail term

For fixed `M>=4`, any `p,q in V` admit an actual contact path satisfying

\[
d_G(p,q)\le C_M(|p-q|+1)+2T_M(D),\qquad
C_M=56M(M+1)^2+42M(M+1).
\tag{1}
\]

To reconstruct (1), note that triangle-freeness makes the contact degree at most five: six unit neighbors would have six angular gaps at least `60` degrees and force a unit triangle. Hull augmentation adds at most two edges at a vertex, so `Ghat` has degree at most seven. Join `p` to `q` by a generic two-segment arc in the convex hull `F`, within distance `1/10` of the straight segment and of length at most `|p-q|+1/10`. Each convex face meets each segment in at most one interval, so each face is crossed at most twice. In an old contact face replace a crossed interval by a boundary arc of at most `m(Q)` actual unit edges. A pocket's auxiliary hull side lies on `partial F` and cannot be crossed by the interior arc; replace the interval by the intervening actual contact path, again of length at most `m(Q)`. No auxiliary side becomes a contact route.

Faces with `m(Q)>M` contribute at most `2T_M(D)`. Every crossed small face has a vertex within `M+1/10` of the straight segment. The disjoint radius-`1/2` disks about such source vertices lie in the radius-`M+1` tube about that segment, so their number is at most `4(M+1)^2+3(M+1)|p-q|`. Each such vertex is incident to at most seven faces, and each small face costs at most `2M`, yielding the first term in (1). A curve in the metric graph from `p` to `q` has graph distance no greater than its length.

### One global slowly deformed lattice chart

Choose a fixed `M` so large that `limsup_D T_M(D)/D<1`; then eventually `T_M(D)<=2D`. Since distinct source points are at least unit-separated, (1) and the edge displacement bound give, for distinct `p,q in V`,

\[
|g(p)-g(q)|\le \frac{KC_M}{D}(|p-q|+1)+\frac{2KT_M(D)}{D}
\le \frac{K'}D|p-q|,
\quad K'=2KC_M+4K.
\tag{2}
\]

For `D>K'`, (2) implies `ell` is injective, since

\[
|\ell(p)-\ell(q)|\ge(1-K'/D)|p-q|>0.
\]

Use `X=ell(B)` as a subset of the triangular lattice. With `g(ell(p))=g(p)`, equation (2) and the same lower bound give

\[
|g(\lambda)-g(\mu)|\le \frac{K'/D}{1-K'/D}|\lambda-\mu|
\le \frac{2K'}D|\lambda-\mu|
\]

for large `D`. Thus every actual diameter endpoint is represented by one chart `b=lambda+g(lambda)` with a fixed `2K'/D` displacement-Lipschitz constant and no bad endpoints. Audit.201's `C-SLOW-LATTICE-DIAMETER-ENDPOINT-BOUND` with `J=1` now gives `q=O(D^(4/5))=o(D)`. This use does not assume a bound on absolute displacement or any global source/scaffold identification beyond the injectivity just proved.

Finally, `C-ZRF` yields `h>=ceil(D)`. Under `C-WOODALL`, the loaded diameter graph is either connected unicyclic or a forest of caterpillars; in either case it has at most `q` edges. Hence `q>=h>=ceil(D)`, contradicting `q=o(D)`.

## Hostile scope checks and disposition

- The reference-edge sum is checked on actual bounded contact faces; the new hull pockets are not treated as contact cycles.
- The routing lemma uses only actual contact edges. Added hull sides are used to define the plane faces and degree bound, never as source motion or transport edges.
- The face-tail hypothesis is a genuine sequence-level premise. It is not supplied by the current grain extraction or by a bound on selected faces alone.
- The frame premise covers every actual core contact at `O(1/D)` accuracy. Selected trains, selected rhombi, or a coherent local grid do not meet it by themselves.
- The argument retains contact isolates in the source ball hull and does not assign them core coordinates. Actual diameter endpoints are in `V` by strict full-source support and `F=conv(B)=conv(V)`.
- No finite motion, strict sub-`D` competitor, global phase extraction, vanishing face tail, C-II closure, or Level I result follows.

There is no finite verifier for the analytic curved-boundary lattice estimate; Audit.201 explicitly makes no verifier claim for that Fourier argument. Its independent theorem is treated as a canonical input here. The finite graph routing and limit argument above are reconstructed directly.

**Verdict: PASS WITH NARROWED SCOPE — promote.** The exact global conditional exclusion is useful as a stop condition for this source class. It does not change the active C-II obligation because neither premise is established for canonical survivors.

## Promotion transaction

Pending PR and protected validation.
