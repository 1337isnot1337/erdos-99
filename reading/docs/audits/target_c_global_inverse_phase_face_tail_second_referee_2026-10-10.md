> Generated reading edition · [exact source](../../../docs/audits/target_c_global_inverse_phase_face_tail_second_referee_2026-10-10.md) · source SHA-256 `9ed749f51f560af597875fc9fb7c2647395ce47a970583a9e3349df6f8e2bb38`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-886FE82FF93C","canonical":false,"claim_ids":["C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION"],"claim_statuses":{"C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION":"audited-working"},"index":"docs/state/artifact-index.jsonl","status":"audited-working","target":"target-c"} -->
# Target C Audit.236 — second referee and repair of the inverse-phase face-tail exclusion

> **Publication lifecycle:** the repaired sequence exclusion is audited-working
> on the basis of agent audits. Independent human mathematical review is still
> required before canonical reuse. This imports the correction without adopting
> the other promotions proposed in source PR #947. Global chart/rate assertions
> from Audit.202 are withdrawn; all source labels and both global hypotheses
> remain required.


Date: 2026-10-10. Audit base: `origin/main=ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`.

Numbering note: main already uses Audit.235 for the Oler-sharpened separator
results, so this independent proof correction is Audit.236. The proposed
manifest increment `2026-10-10.audit.235` is a separate state-version counter.

- Prior Audit.202 artifact on the audit base: blob `ec8c2e728c1f11caf63d0cd321778fe9be0064b4`; its discovery source was `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Canonical local-capacity input on the audit base: Audit.214 artifact blob `bfa12709933a3ff9cc41130cd4cad5e3e65ce4e0`.

## Verdict and correction

**PASS WITH REPAIR — retain** `C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION` under its existing hypotheses and sequence-level conclusion. The original Audit.202 proof has a genuine gap: its fixed-cutoff routing estimate leaves an additive term `2K T_M(D)/D`, which is only `o(1)` after the face-tail limit and cannot be absorbed into a term proportional to `|p-q|/D`. Thus Audit.202 did not establish one globally `O(1/D)`-Lipschitz chart, nor the claimed `q=O(D^(4/5))` rate.

The sequence-level exclusion is repaired by a diagonal cutoff and local patches of radius `D^(3/4)`. The corrected proof gives only `q=o(D)`, which is enough for the same contradiction. It does not construct any global Lipschitz chart or claim a `D^(4/5)` endpoint bound.

## Exact statement retained

Consider an unbounded sequence of canonical post-ZF C-II sources in the contact-minimal, then actual-diameter-pair-minimal, triangle-free normal form, with `D -> infinity` and the full source retained, including contact isolates. Let `G=(V,C)` be the connected positive-contact core, `B` the set of all actual diameter endpoints, and `Ghat` the core augmented by every missing straight hull side between consecutive vertices of `B`. For each bounded face `Q` of `Ghat`, let `m(Q)` be its unit-contact boundary length when it is an old bounded contact face, and the number of actual unit-contact edges on its simple path boundary when it is a convex pocket. Define

$$
T_M(D)=\sum_{Q:m(Q)>M}m(Q),\qquad M\ge4.
$$

Fix `0<=K<infinity`. Suppose that for each source there is one D-dependent unit triangular frame

$$
U_D=\{\pm u_D,\pm v_D,\pm(v_D-u_D)\},\quad |u_D|=|v_D|=1,
\quad \angle(u_D,v_D)=\pi/3,
$$

such that every oriented actual unit-contact edge vector of `G` is within `K/D` of a vector in `U_D`, and suppose

$$
\lim_{M\to\infty}\limsup_{D\to\infty}T_M(D)/D=0.
$$

Then no such unbounded canonical sequence exists. The conclusion is conditional on both global premises; neither is extracted by this theorem.

## Canonical inputs and scope

- `C-RHOMBUS-POP` supplies the connected core, `F=conv(B)=conv(V)`, convex old contact faces, and the convex hull-augmented pockets. It also ensures the augmented graph and face-path quantities above are the canonical ones. The pockets are not contact cycles.
- `C-CURVED-BOUNDARY-LATTICE-LOCAL-CAPACITY` says that for a finite unit-separated source of diameter `D`, its actual diameter-endpoint set `B`, and
  $$
  W=\bigcap_{a\in A}\overline B(a,D),
  $$
  every `S subset B intersect closed_ball(c,r/2)` with `c in W`, `sqrt(D)<=r<=D`, and every point within `epsilon<=1/8` of one translate of a unit rhombic lattice satisfies
  $$
  |S|\le C\bigl(r\epsilon+(Dr)^{1/3}+1\bigr),
  $$
  with absolute constants, uniformly in the source and lattice.
- `C-ZRF` gives `h>=ceil(D)` for the number `h` of actual diameter edges; `C-WOODALL` gives `h<=q`, where `q=|B|`.

No chart, motion, source/scaffold identification, or co-embedding is assumed. Contact isolates stay in the full source and in `W`; they are not assigned core coordinates. Every actual diameter endpoint lies in `V`: it is an exposed point of `F` by its actual diameter partner and `F=conv(V)`.

## Independent reconstruction

### Diagonal face cutoff and zero holonomy

Assume for contradiction that a sequence satisfies both premises. For each integer `j>=1`, choose a fixed integer `M_j>=4`, increasing to infinity, so that
$$
\limsup_{D\to\infty}T_{M_j}(D)/D<1/(2j).
$$
Choose increasing thresholds `D_j` so that for every sequence term with `D>=D_j`,
$$
T_{M_j}(D)/D\le1/j,\qquad C_{M_j}D^{-1/4}\le1/j,
\qquad M_j/D\le1/j,
$$
where `C_M=56M(M+1)^2+42M(M+1)`. Define `M(D)=M_j` on `D_j<=D<D_{j+1}`. Then
$$
M(D)\to\infty,\quad T_{M(D)}(D)/D\to0,\quad C_{M(D)}D^{-1/4}\to0,
\quad M(D)/D\to0.
$$

The largest old bounded contact-face length is at most `M(D)+T_{M(D)}(D)=o(D)`. Assign every oriented actual contact edge its nearest frame vector, with opposite assignments on opposite orientations. For sufficiently large `D` this is unique. Around an old bounded contact face of length `m`, the assigned lattice vectors sum to a vector of norm at most `mK/D=o(1)`. Since a nonzero vector of the unit triangular lattice has norm at least one, this sum is zero. The bounded facial cycles of the connected plane graph generate its cycle space; bridge traversals cancel in opposite orientations. Therefore every closed contact walk has zero assigned sum. Path integration gives `ell:V -> Lambda_D`, where `Lambda_D=Z u_D+Z v_D`, with each contact edge mapped to its assigned frame vector. For `g(p)=p-ell(p)`, every actual contact edge satisfies
$$
|g(p)-g(q)|\le K/D.
$$

### Actual-contact routing, including the tail

For every fixed cutoff `M>=4`, the actual-contact graph has a path between any `p,q in V` with
$$
d_G(p,q)\le C_M(|p-q|+1)+2T_M(D),\qquad
C_M=56M(M+1)^2+42M(M+1).\tag{1}
$$
Here is the routing count. Triangle-freeness bounds contact degree by five: six unit neighbors would force all six successive angular gaps to equal `pi/3`, creating a unit triangle. Hull augmentation adds at most two incident edges, so `Ghat` has degree at most seven. Route from `p` to `q` by a generic two-segment arc in the convex hull, within distance `1/10` of the chord and of length at most `|p-q|+1/10`. Convexity makes each face meet each segment in at most one interval. Replace each crossing through a face by a boundary path of actual contacts. An auxiliary hull side is never used: a pocket crossing is replaced along its actual contact path boundary. Each face is crossed at most twice, so faces with `m(Q)>M` cost at most `2T_M(D)`.

For a crossed face with `m(Q)<=M`, one of its vertices lies within distance `M+1/10` of the chord. Disjoint radius-`1/2` disks about all such source vertices fit in the radius-`M+1` tube around the chord. Its area gives at most `4(M+1)^2+3(M+1)|p-q|` such vertices. Each is incident to at most seven faces, and each small-face crossing costs at most `M`; allowing two crossings per face gives the upper bound `14M(4(M+1)^2+3(M+1)|p-q|)`, which is at most `C_M(|p-q|+1)`. The replacements form an actual contact walk, proving (1). This estimate is used with a varying cutoff only after proving its constant is controlled diagonally.

### Patchwise lattice approximation and endpoint count

Put `r_D=D^(3/4)`. If `p,q` are actual diameter endpoints in one boundary arc of length at most `r_D/2`, then `|p-q|<=r_D/2`. Use (1) with `M=M(D)` and sum the `K/D` edge errors along its actual contact route:
$$
|g(p)-g(q)|\le \frac K D\{C_{M(D)}(r_D+1)+2T_{M(D)}(D)\}
=:\epsilon_D\longrightarrow0.
$$
For each such arc choose one representative endpoint `p_0`. Every endpoint `p` assigned to the arc has `p=ell(p)+g(p)` with `ell(p)` in the same triangular lattice and `|g(p)-g(p_0)|<=epsilon_D`. Thus the endpoints in this patch are within `epsilon_D` of one translate of that lattice. This is only a patchwise approximation; it is not a global Lipschitz chart.

Every actual diameter endpoint is on `partial W`, since its diameter partner supplies an active radius-`D` disk. A diameter pair at distance `D` also implies `W` lies in the lens of two radius-`D` disks, hence in a disk of radius `sqrt(3)D/2`; convex perimeter monotonicity gives `per(W)=O(D)`. Partition `partial W` into `O(D/r_D)` arcs of length at most `r_D/2`, and assign each endpoint to one arc. For each arc choose its midpoint `c` on `partial W`; then `c in W` and every assigned endpoint lies in `closed_ball(c,r_D/2)`. For all large `D`, `sqrt(D)<=r_D<=D` and `epsilon_D<=1/8`, so the canonical local-capacity theorem applies to each assigned set. Summing gives
$$
q\le O(D/r_D)\bigl(r_D\epsilon_D+(Dr_D)^{1/3}+1\bigr)
=O(D\epsilon_D+D^{5/6}+D^{1/4})=o(D).
$$

But `C-ZRF` and `C-WOODALL` give `q>=h>=ceil(D)`, a contradiction. This proves the retained sequence-level exclusion.

## Hostile checks and disposition

- The original fixed-`M` step only made `T_M(D)/D` bounded (and, after a second limit, small); the additive endpoint error cannot be absorbed into `K'|p-q|/D` for nearby `p,q`. The global chart and `O(D^(4/5))` rate are therefore withdrawn.
- The diagonal cutoff controls both the tail and the cubic growth of the route constant; it does not silently exchange the fixed-`M` and large-`D` limits.
- The local count is applied only to actual diameter endpoints in `partial W`, in one patch and one lattice translate. It is not applied to arbitrary source points or to a scaffold.
- Hull sides define faces but never become transport edges. Pockets are routed on actual contacts, not treated as contact cycles.
- Isolates remain in the full-source ball hull and unit-separation hypotheses. No core coordinates are assigned to them.
- No finite verifier certifies the analytic local lattice-capacity theorem; that independently audited canonical input is taken in its stated scope. The routing estimate and diagonal argument above are reconstructed here. No numerical or finite verifier is claimed to prove the sequence theorem.

**Canonical disposition:** retain the existing theorem ID and sequence-level conclusion, replace its audit pointer with this corrected proof, and replace dependency `C-SLOW-LATTICE-DIAMETER-ENDPOINT-BOUND` by `C-CURVED-BOUNDARY-LATTICE-LOCAL-CAPACITY`. The conditional premises remain unextracted, so C-II and Level I remain open. The active frontier does not change.
