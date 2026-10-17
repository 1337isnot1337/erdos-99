> Generated reading edition · [exact source](../../../docs/audits/target_c_oo_short_pair_path_bandwidth_independent_audit_2026-10-08.md) · source SHA-256 `7e1d3121a04befb341fba6b0997ececc0a6c34cd0f05adea39d2c0397b1e0e7f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B5A192486F61","canonical":true,"claim_ids":["C-OO-SHORT-PAIR-PATH-BANDWIDTH"],"claim_statuses":{"C-OO-SHORT-PAIR-PATH-BANDWIDTH":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of the Oler short-pair path-bandwidth theorem

**Date:** 2026-10-08  
**Audit base:** `origin/main=350c8ed6cf38d9a051bffe1edae1d0d54df10672`, state `2026-10-08.audit.145`  
**Source branch:** `research/sol/target-c-owner-order-closure-20261006`  
**Frozen source tip:** `bf288c82e8a62466d5580025c94e750a177e63e2` (open PR #737)  
**Source artifact:** `research/target_c_high_t_tb1_short_blocker_oler_bandwidth_t18687_2026-09-17.md`, SHA-256 `d2ad07bd352354b7edef066ff3b6b9e3bad0647b592b5b437a138be35afbc6d4`; Sections 1–3 only.  
**Source verifier:** `research/verify_target_c_high_t_tb1_short_blocker_oler_bandwidth_t18687.py`, SHA-256 `8f1fe71f107aaf49544deac6a6821f119a5af6a0faca8e3f2ef7409b7a14b8e4`.

**Verdict:** **PASS — promote `C-OO-SHORT-PAIR-PATH-BANDWIDTH`.** This is a finite conditional geometry theorem. The stronger six-row estimate supersedes the earlier fourteen-row whole-rhombus tube estimate at its common scope. The subsequent exact-swap thinning and Horn consequences in source Sections 4–5 are outside this audit.

## Exact statement

Let a convex disk Ω be cut by proper, pairwise-disjoint crosscuts τ₁,…,τ_m whose complementary regions form a path

```math
R_0\xleftrightarrow{\tau_1}R_1\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
```

Assume each crosscut, where it lies in Ω, follows midpoint-centerline segments of actual strict unit-rhombus faces in a unit-separated planar source. Assume every crossing of a segment `xy` with a row τ_i occurs on one of that row's rhombus centerlines, distinct rows use distinct rhombi, and the selected rhombus interiors are pairwise disjoint. For source points `x` in `R_p` and `y` in `R_q`, with `p<q`, put `L=|x-y|` and `N=q-p`. Then

```math
\boxed{N\le 1+\frac{14L+5\pi}{3\sqrt3}.}
\tag{1}
```

Consequently, for any fixed `K>0`, if the source diameter is `D`, `D>10K`, and

```math
|x-y|\le 1+\frac K D,
```

then

```math
\boxed{|p-q|\le6.}
\tag{2}
```

In particular, every noncontact pair with `1<|x-y|<=1+K/D` in these path regions is at most six row steps apart. The geometric statement needs no high-`t`, KKT, stress, TB1, or global-minimality hypothesis beyond the existence of the specified source geometry and crosscut path.

## Dependency chain

```text
distinct strict rhombi crossed by a short source segment
-> their centers are sqrt(3)/2-separated in its radius-1/2 capsule
-> finite Oler gives (1)
-> exact rational threshold gives the six-row bound (2)
-> lower near-unit pairs in this supplied path system have bounded row span
```

The only packing input is Lemma 21.1 in `docs/theory/03-oler-shell.md`. The unit-rhombus angle and face-interior properties are at the canonical scope of `C-RHOMBUS-POP`. The ordered path of pairwise-disjoint crosscuts is an explicit hypothesis; no theorem extracting such a path from an arbitrary owner tree is asserted here.

## Independent proof

Since Ω is convex, the segment `xy` stays in Ω. Each of the `N` crosscuts between `R_p` and `R_q` separates the endpoints, so `xy` meets it. By hypothesis the crossing lies on a unit-length midpoint-centerline segment of a strict rhombus. Choose one such rhombus for each row. Distinct rows give distinct faces.

For an interior angle θ of a strict unit rhombus, π/3<θ<2π/3. Its inradius is `sin(θ)/2`, so it contains the closed disk of radius `δ=√3/4` about its center strictly inside its face. The selected face interiors are disjoint. Therefore the chosen centers are pairwise at distance at least `2δ=√3/2`.

The center of a unit-length centerline segment is at distance at most `1/2` from any point on that segment. Thus every chosen rhombus center lies in the radius-`1/2` capsule around `xy`. This capsule has area `L+π/4` and perimeter `2L+π`.

Write `s=√3/2` for the minimum separation of the chosen centers. Rescale the center set and capsule by `1/s` and apply finite Oler, in the unit-separation form `n <= (2/√3) area + (1/2) perimeter + 1`:

```math
\begin{aligned}
N&\le \frac{2}{\sqrt3\,s^2}\left(L+\frac\pi4\right)
 +\frac{1}{2s}(2L+\pi)+1\\
 &=1+\frac{14L+5\pi}{3\sqrt3}.
\end{aligned}
```

Here `s=√3/2`; the inradius lower bound `√3/4` is used only to obtain this center-separation bound, not as the Oler rescaling length.

For the threshold, `\sqrt3>265/153` because `3*153^2-265^2=2`, and `\pi<22/7`. Hence

```math
\frac{14}{3\sqrt3}<\frac{714}{265},\qquad
1+\frac{5\pi}{3\sqrt3}<\frac{1493}{371}.
```

When `D>10K`, `L<=1+K/D<11/10`, and so

```math
N<\frac{714}{265}\frac{11}{10}+\frac{1493}{371}
 =\frac{64814}{9275}
 =7-\frac{111}{9275}<7.
```

Since `N` is an integer, `N<=6`.

## Hostile scope checks

- **Path geometry:** the conclusion concerns points in regions of the supplied ordered crosscut path. It does not convert arbitrary source points, owner labels, or a branched dual tree into path coordinates.
- **Contact isolates:** every source point that actually lies in a path region is eligible as `x` or `y`, including an isolate. The result says nothing about points outside Ω or points not assigned to these regions; no isolate is discarded from the source.
- **Actual geometry:** the rows and rhombi are actual embedded objects. Selected stress edges, a scaffold, or a response-network edge cannot be substituted without a separate co-embedding theorem.
- **Distance scope:** the six-row conclusion is for distances at most `1+K/D`; the row bound is not inferred from an asymptotic `o(1)` without a fixed `K`. Exact unit contacts also satisfy the geometric bound, but this audit does not classify them as inactive blockers.
- **No motion conclusion:** six-row locality does not prove that a swap is feasible, that multiple swaps are compatible, or that a strict-diameter competitor exists. The source report's residue-class thinning and subsequent Horn claims remain unreviewed here.
- **Fourteen-row predecessor:** the whole-rhombus tube estimate is weaker. The Oler center packing applies under the same row/crossing conditions and replaces fourteen by six, so the weaker numerical result is superseded at that scope.

## Verifier boundary

The frozen source verifier was inspected and rerun. It passes. Its exact `Fraction` checks verify the rational coefficient envelope, `D>10K` cap `64814/9275`, and positive margin `111/9275`; its displayed limiting value uses floating-point `math.pi` and `math.sqrt` only as a numerical sanity check. It does **not** verify Oler's theorem, crosscut separation, rhombus-center packing, or any infinite/asymptotic source claim. Those steps are proved above from the canonical finite Oler inequality and explicit geometric hypotheses.

## Frontier effect

This replaces the open fourteen-cut metric estimate by a stronger six-row bound for the same short-pair/path setup. It improves a local constraint on lower near-unit blockers but does not establish a path extraction for every active owner system or any source motion. C-I remains closed; C-II and Level I remain open, and the current finite-move/payment obligation is unchanged.
