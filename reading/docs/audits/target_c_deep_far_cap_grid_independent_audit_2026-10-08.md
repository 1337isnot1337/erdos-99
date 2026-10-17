> Generated reading edition · [exact source](../../../docs/audits/target_c_deep_far_cap_grid_independent_audit_2026-10-08.md) · source SHA-256 `133818e3fa79ba327494e264b9603e5867b76f0f6081fb22d7c3ffec3deeb764`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B625364A5605","canonical":false,"claim_ids":["C-DEEP-FAR-COMPLETE-GRID-LOADED-RETURNS"],"claim_statuses":{"C-DEEP-FAR-COMPLETE-GRID-LOADED-RETURNS":"audited-working"},"index":"docs/state/artifact-index.jsonl","status":"audited-working","target":"target-c"} -->
# Target C Audit.137 — deep/far cap grid and loaded returns

Date: 2026-10-08  
Audit base: `origin/main=3530a6f5c0d4030d435b7f19e77faf818f839c5e`, state `2026-10-08.audit.136`  
Source snapshot: open draft PR #671, branch `research/target-c-port-route-audit-20261004` at `0e49b450cc4819cc2f4f205303cbb9a09b45d269`  
Source report SHA-256: `3bf843495465d0aa2b35022f08ec10e9bdd43ae8d12c8205888024e4281e044a`  
Source verifier SHA-256: `26349d267cb3e2a1bed4979cb732d5d6e98772768179bc8331b019bb088803c7`

## Audit boundary

Audit.133 already promotes the report's universal finite separator, disjoint-return, and convex-face theorems, and records the deep-cap scalar trimming argument only under explicit cap/grain hypotheses. This audit covers only the report's additional **complete-grid version**: trimming a coherent quadratic grain away from the cap boundary and one deep attachment, extracting a complete train grid in the retained region, and applying the canonical loaded-return theorem to its crossing rhombi. The source extraction of the cap/grain package remains unproved. The same-host/chord endpoint fork is outside this promotion; the exact segment-crossing hypotheses are not needed for the grid/return conclusion below.

## Exact conditional statement audited

Work along a canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global-source sequence with `$D\to\infty$`; retain every source point. For each sufficiently large member, let `I` be one unloaded positive-contact component, `A` its actual loaded attachment set, and `B` the full loaded set. Assume:

- `C` is a convex cap in the source force hull, of diameter at most `D`, with a chord `L subset partial C` and affine signed height `eta` that vanishes on `L`, is nonnegative on `C`, and has gradient of norm one;
- `B intersect int(C) = empty`;
- `G` is a finite family of strict source unit-rhombus faces with disjoint interiors, all four vertices of each face in `I`, and `G subset int(C) intersect conv(A)`; its total area is `A_G >= alpha D^2` for a fixed `alpha > 0`;
- `G` is an `epsilon`-coherent grain for fixed `0 < epsilon < pi/6`, and its physical perimeter, including hole boundaries, satisfies `P(G) <= C_epsilon D` for fixed `C_epsilon`;
- for an attachment `a_* in A`, `H = eta(a_*) = max_{a in A} eta(a) >= A_G/D`.

Set `h = A_G/(8 pi D)`, `s = A_G/(4D)`, and retain the rhombi whose entire faces have distance greater than `h` from `partial C` and lie strictly below height `H-s`. For all sufficiently large `D`, the retained complex contains an `epsilon`-coherent subgrain of area `Omega_{alpha,epsilon,C_epsilon}(D^2)`, and hence a complete train grid with both shores `Omega_{alpha,epsilon,C_epsilon}(D)`, entirely inside

```math
W=C_{-h}\cap\{\eta\le H-s\},
```
where `C_{-h} = {x in C: dist(x, partial C) >= h}`. Every grid vertex is farther than `h` from every loaded endpoint and farther than `s` from `a_*`.

Writing `X` for the grid-vertex set and `a,b >= gamma D` for its two shore sizes, its `ab` crossing rhombi yield at least

```math
p\ge\lceil F(ab)\rceil=\Omega_{\alpha,\epsilon,C_\epsilon}(D)
```
pairwise vertex-disjoint actual contact paths in the induced contact graph on `I union A`, stopped at their first loaded endpoint, from distinct grid vertices to distinct actual loaded attachments. Each path has more than `h` edges from its last vertex in `X` to its loaded endpoint. Consequently these paths contain `Omega_{alpha,epsilon,C_epsilon}(D^2)` distinct internal vertices in `I setminus X`, counted across all paths. Here `F(R) = (sqrt(25 + 4 C_0 R) - 5)/(2 C_0)` with `C_0 = 8 pi/sqrt(3)`, as in canonical `C-RHOMBUS-BULK-LOADED-RETURN-BOUND`.

This is a conditional structural theorem. It does not assert that canonical sources supply `C`, `G`, and `a_*`, and it produces no finite source motion, strict-`D` competitor, or C-II closure.

## Independent reconstruction

Let `a_0 = sqrt(3)/2`, the minimum area of a strict unit rhombus. The cap perimeter obeys `per(C) <= pi D`. A rhombus omitted because it meets the boundary strip lies wholly within distance `h+2` of `partial C`, since its diameter is less than two. The inner boundary strip of a convex body of width `t` has area at most `t per(C)`, so these omissions have area at most

```math
\pi D(h+2)=A_G/8+2\pi D.
```

Also `G subset conv(A)` and `H = max_A eta` imply `eta <= H` on every grain face. If a face fails the strict height cutoff, its whole face lies in the slab `H-s-2 <= eta <= H`. Every parallel slice of `C` has length at most `D`, so this slab has area at most

```math
D(s+2)=A_G/4+2D.
```

The two discarded unions therefore have area at most `3A_G/8 + (2pi+2)D <= A_G/2` once `A_G >= 16(pi+1)D`, which follows eventually from `A_G >= alpha D^2`. The retained rhombi have total area at least `A_G/2`.

The set `W` is convex and has diameter at most `D`. Every discarded grain rhombus that can create a new boundary edge of the retained subcomplex meets `partial W`; because its diameter is less than two, it lies in the two-neighborhood of `partial W`. For a convex `W`, the two-sided width-two boundary tube has area at most `4 per(W) + 4pi <= 4pi(D+1)`. Disjoint rhombus interiors and their area lower bound `a_0` give at most `4pi(D+1)/a_0` such crossing rhombi. Each exposes at most four unit edges. Thus the sum `P_0` of the retained edge-connected component perimeters obeys

```math
P_0\le P(G)+\frac{16\pi(D+1)}{a_0}=O_{\epsilon,C_\epsilon}(D).
```

If the retained component areas are `A_j`, planar isoperimetry gives

```math
\sum_j\sqrt{A_j}\le\frac{P_0}{2\sqrt\pi},\qquad
\sum_j A_j\ge A_G/2.
```

Using `sum_j A_j <= sqrt(max_j A_j) sum_j sqrt(A_j)`, some one component has area at least

```math
\max_jA_j\ge\frac{\pi A_G^2}{P_0^2}=\Omega_{\alpha,\epsilon,C_\epsilon}(D^2).
```

It remains a subcomplex of the original coherent grain, so its trains inherit the same phase labels and local geometry. Each strict unit rhombus has area at most one, so the component also has `Omega(D^2)` rhombi. Its perimeter is `O(D)`; canonical `C-PSEUDO-GRID` (the Section-73 extraction used in Section 78.3) yields two linear-size distinct-phase shores and the complete grid within this component and hence within `W`. No train is joined across a deleted rhombus.

Each grid rhombus is a strict source face in `I`, so canonical `C-RHOMBUS-BULK-LOADED-RETURN-BOUND` applies to the `ab = Omega(D^2)` crossing rhombi and gives `p >= ceil(F(ab)) = Omega(D)` vertex-disjoint paths to distinct actual attachments. A grid vertex `x in W` satisfies `dist(x, partial C) > h`; every loaded endpoint lies outside `int(C)`, hence `|x-b| > h` and every contact path from `x` to `b` has more than `h` unit edges. Also `eta(x) < H-s = eta(a_*)-s`, so, since `eta` is 1-Lipschitz, `|x-a_*| > s`.

For each vertex-disjoint path, truncate its initial portion after its last visit to `X`. The remaining internal vertices are all outside `X`, remain in `I` (paths stop at their first loaded endpoint), and are disjoint from those on every other path. The suffix still starts at a grid vertex of depth greater than `h`, so it has at least `ceil(h)-1 = Omega_alpha(D)` internal vertices. Multiplying by `p = Omega(D)` gives the claimed quadratic distinct population.

## Adversarial scope checks

- Long, thin caps are allowed: the boundary-strip estimate uses convex perimeter, and the height-slab estimate uses only the diameter bound.
- Large `h` or `s` causes no invalid empty-set inference. The quadratic area bound first guarantees `A_G >= 16(pi+1)D` and positive retained area for all sufficiently large members.
- The perimeter budget counts outer and hole boundaries. Removing the cut faces adds at most four unit edges per face meeting ∂W.
- The selected component can have holes; the canonical pseudogrid extraction allows them. Its local trains inherit the parent's phase labels after trimming.
- Return sources and endpoints are actual source vertices. The paths use distinct loaded endpoints, and their external internal vertices are distinct; no pin-only substitute or contact-isolate deletion is used.
- The pinned-grid order regression remains irrelevant: its pins are not all actual loaded endpoints and it does not satisfy the canonical loaded-return theorem.
- This result does not establish a fixed-port route family or pay the path packet against train/interface/face currency. The user-supplied cap/grain extraction remains the open premise.

## Verifier audit

At the frozen source commit I inspected and reran `research/verify_target_c_bulk_separator_2026_10_04.py`. It uses `Fraction` arithmetic and checks 12 finite grounded-grid rank/equilibrium cases, 2,517 removed-vertex subsets on the stated small board, and four exact max-flow grid instances. All passed. These checks corroborate the finite separator/path examples only; the code does not encode the deep/far truncation, boundary-tube counting, coherent-component extraction, or asymptotic grid/return argument. No certificate is registered for this conditional claim.

## Verdict and disposition

- **PASS WITH NARROWED CONDITIONAL SCOPE:** the deep/far trim, complete-grid extraction, and linear disjoint loaded returns follow from the explicit cap, grain, height, and perimeter hypotheses above plus the canonical grid and loaded-return theorems.
- The source's same-host/chord endpoint fork is not included in the theorem recorded here.
- The October host-cap/grain extraction is not proved by this result and remains unpromoted. No canonical dependency is created.
- The conditional bridge gives a grid far from one actual loaded attachment and a quadratic number of distinct internal return vertices, but no source move or C-II frontier reduction. C-II and Level I remain open.

## Source coordination

PR #671 remains open at the audited snapshot `0e49b450cc4819cc2f4f205303cbb9a09b45d269`. Its finite separator and loaded-return claims are already canonical from Audit.133; this audit covers only the complete-grid extension. No discovery-worker branch or worktree was changed.
