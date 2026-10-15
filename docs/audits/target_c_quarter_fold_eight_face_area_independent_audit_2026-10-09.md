<!-- theorem-state: {"artifact_id":"ART-7F7534848EE5","canonical":true,"claim_ids":["C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND"],"claim_statuses":{"C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: area bound for an endpoint-feasible eight-face fold

**Date:** 2026-10-09. **Audit:** 223.
**Audit base:** `origin/main=1a7e85702143f7fef926fd3952eb3002252528ed`, state `2026-10-09.audit.216`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Section 5.2.

## Verdict

**PASS WITH NARROWED/SHARPENED SCOPE — promote `C-QUARTER-FOLD-EIGHT-FACE-AREA-LOWER-BOUND`.** Under the report's full endpoint-feasibility hypotheses, the face area is **strictly greater than** `2 sqrt(3)`, not merely at least that value. The infimum may equal `2 sqrt(3)`; no positive uniform gap is asserted. This is a conditional per-face geometric debit, not a source-population estimate.

## Exact audited statement

Let a finite unit-separated source have a simple convex actual unit-contact face `F` with eight sides. Consider a nonconstant face-closed quarter-fold of its boundary labels, retaining every other source label, and assume the full endpoint is unit-separated and triangle-free. The four transition arcs each have two sides by `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`. Let `alpha, beta >= 0` be their two outward unit-edge deflection angles, and let `gamma` be the angle between adjacent transition-parallelogram chord directions. Then

\[
\alpha+\beta<\pi/6,\qquad
\pi/3+\alpha+\beta<\gamma<2\pi/3-\alpha-\beta,
\]

and

\[
\operatorname{Area}(F)\ge4\cos\alpha\cos\beta\sin\gamma>2\sqrt3.
\]

The first displayed lower bound compares the convex face with its inscribed transition parallelogram; the strict area bound is the claimed consequence. The theorem uses the actual face and full lower-feasible endpoint at the stated finite scope. It assumes neither global optimality nor a diameter or stress hypothesis.

## Independent reconstruction

The canonical convex-face classification supplies four transition vertices forming an inscribed parallelogram. Each intervening arc has two unit sides. Convexity places its midpoint outside the transition chord, so a chord of length `2 cos(alpha)` has edge directions deflected by `+alpha` and `-alpha` from the chord; the opposite arc has the same chord and hence the same deflection magnitude. Use `alpha, beta >= 0` for the two alternating chord directions. Since the parallelogram is nondegenerate, `0 < gamma < pi`.

At each transition corner the old exterior turn is one of

\[
\gamma-\alpha-\beta,\qquad \pi-\gamma-\alpha-\beta,
\]

alternating around the four corners. The two adjacent old boundary edges are unit and their endpoints are nonconsecutive vertices of the actual face, so their chord is strictly longer than one. Thus the old turn is strictly between `pi/3` and `2pi/3`. At a sign transition the folded turn is supplementary; its two folded edges are unit, and endpoint triangle-freeness forces their chord also to be strictly longer than one. These inequalities give the same open interval for the old turn. Applying this at all four corners yields

\[
s:=\alpha+\beta<\pi/6,\qquad \pi/3+s<\gamma<2\pi/3-s.
\]

The transition parallelogram's area is `4 cos(alpha) cos(beta) sin(gamma)`, and it lies inside the convex face. Since

\[
\cos\alpha\cos\beta
=\cos(\alpha+\beta)+\sin\alpha\sin\beta
\ge\cos s
\]

and the open symmetric interval for \(\gamma\) gives \(\sin\gamma>\sin(\pi/3+s)\),

\[
\begin{aligned}
\operatorname{Area}(F)
&\ge 4\cos\alpha\cos\beta\sin\gamma\\
&>4\cos s\sin(\pi/3+s)\\
&=2\{\sin(\pi/3+2s)+\sin(\pi/3)\}\\
&\ge 2\sqrt3,
\end{aligned}
\]

because `0 <= s < pi/6`, so `pi/3+2s` lies in `[pi/3, 2pi/3]`. The strict turn inequalities are what justify promoting the strict bound even when `s=0`.

## Adversarial scope and verifier boundary

- The argument needs the actual convex face: its nonconsecutive boundary vertices have no unit chord through the face, and its convexity contains the transition parallelogram.
- It needs full endpoint unit separation and triangle-freeness. Without endpoint triangle-freeness, a folded two-edge path could acquire a unit chord and the strict turn interval would fail.
- The exact rational eight-cycle in source Section 5.3 is a compatible finite example, not an optimality witness. Its shoelace area is exactly `7840/1681`, whose square is `61465600/2825761 > 12`; this is consistent with the bound but is not its proof. No finite verifier encodes the strict angle/area proof.
- Source Section 5.4's sharpness family and the report's hull-cover and population conclusions were not audited here. In particular, this theorem gives no uniform excess above `2 sqrt(3)`.

## Dependencies and frontier effect

Dependencies are canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION` and `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`. This conditional area lower bound neither creates a feasible fold nor locates such a face in a canonical C-II source. It changes no route obligation; C-II and Level I remain open.
