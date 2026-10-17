> Generated reading edition · [exact source](../../../docs/audits/target_c_quarter_fold_minimum_face_size_independent_audit_2026-10-09.md) · source SHA-256 `39f9c94c1f735f10daec0b2720b0a9a0c6e890a62a1669a884705b9f25409a8a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F93DC944F16D","canonical":true,"claim_ids":["C-QUARTER-FOLD-MINIMUM-FACE-SIZE"],"claim_statuses":{"C-QUARTER-FOLD-MINIMUM-FACE-SIZE":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: endpoint-feasible quarter-folds need eight-sided faces

**Date:** 2026-10-09. **Audit:** 222.
**Audit base:** `origin/main=be483580933b4038e3172888b106b69f782c38e3`, state `2026-10-09.audit.215`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`.

## Verdict

**PASS — promote `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`.** A nonconstant face-closed quarter-fold on a simple convex actual unit-contact face can be fully unit-separated and triangle-free only if the face has at least eight sides. If it has exactly eight sides, its four transition arcs each have two edges. This is a necessary condition for an already feasible endpoint; it gives no endpoint or C-II closure.

The pentagonal subcase is already covered more strongly by `C-PENTAGON-TRAIN-COMPONENT-BIT-COLLAPSE` (Audit.98) and is not assigned a duplicate claim. The new claim retains the six-, seven-, and eight-side conclusions.

## Exact audited statement

Let `A` be a finite unit-separated source whose full actual unit-contact graph has a simple convex face `F` with `m>=5` sides, each an actual unit contact. Let `q_i` be its cyclic oriented side vectors. Give the sides signs `s_i` in `{+1,-1}` with `sum_i s_i q_i=0`, and define the quarter-fold by

```math
U_{i+1}-U_i=s_iJq_i,\qquad J(x,y)=(-y,x).
```

Replace the labels on `F` by these folded positions and retain every other source label. Assume this full endpoint is unit-separated and triangle-free. Then every one of the four transition arcs in a nonconstant sign pattern has at least two sides. Hence `m>=8`; for `m=8` all four arcs have exactly two sides. In particular, on an actual face with five, six, or seven sides, every endpoint-feasible sign pattern is constant.

No global-minimality, KKT, stress, or upper-diameter hypothesis is used. The condition is on the full lower-feasible endpoint, so retained isolates and all other source labels remain part of the feasibility test.

## Independent reconstruction

The canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION` gives exactly four transition vertices for a nonconstant endpoint-feasible pattern, and those vertices form an inscribed parallelogram. They divide the face into four positive-length boundary arcs; opposite arcs have equal endpoint chords.

If one transition arc has one side, its chord has length one. The opposite arc has the same chord. If that opposite arc had two or more sides, its endpoints would be nonconsecutive vertices of `F`, and their unit chord would be an actual contact drawn inside the face. That contradicts the face property. Thus the opposite arc also has one side. If both opposite pairs were one-side arcs, the face would be a quadrilateral. Since `m>=5`, any one-side pair is the only such pair, and the other two opposite arcs each have at least two sides.

Assume such a short pair exists. Write the parallelogram corners as

```math
a=0,\quad b=Lt,\quad d=v,\quad c=Lt+v,
```

where `t` and `v` are unit vectors and the angle `gamma` from `t` to `v` lies in `(0,pi)`. The two long face arcs run from `a` to `b` and from `d` to `c`. Their first unit edge vectors can be written

```math
e=(\cos\alpha)t-(\sin\alpha)Jt,\qquad
f=(\cos\beta)t+(\sin\beta)Jt,
```

with `alpha,beta>=0`, because convexity puts the two arcs on opposite sides of their equal chord.

At a transition vertex with exterior turn `theta`, the old two-step boundary chord has length `2 cos(theta/2)`. Its endpoints are nonconsecutive face vertices, so the old chord is strictly longer than one. At a sign transition the folded exterior turn is `pi-theta`; the two folded sides stay unit, and the full endpoint is both unit-separated and triangle-free, so its two-step chord is also strictly longer than one. Therefore each transition turn lies in `(pi/3,2pi/3)`.

At `a` and `d`, the old turns are respectively `pi-gamma-alpha` and `gamma-beta`. The lower turn bounds give

```math
\gamma<2\pi/3-\alpha,\qquad \gamma>\pi/3+\beta.
```

Put `delta=(alpha+beta)/2` and `d0=(beta-alpha)/2`. These inequalities imply `0<=delta<pi/6` and

```math
\pi/3+\delta<\gamma-d_0<2\pi/3-\delta.
```

Apply the inverse common quarter-turn to the folded coordinates, so each folded edge has increment `s_i q_i`. Up to reversing every sign, the long arcs have sign `+1` and the short arcs have sign `-1`. The bottom long arc stays in place, while the top long arc is translated by `-2v`. Thus the two first internal vertices have folded difference `f-e-v`, and direct expansion gives

```math
|f-e-v|^2=1+4\sin^2\!\delta-4\sin\delta\sin(\gamma-d0).
```

If `delta>0`, the displayed angle interval implies `sin(gamma-d0)>sin(delta)`, so this squared distance is strictly below one. If `delta=0`, then `alpha=beta=0`; the two old first internal vertices are separated by the unit vector `v`. They are nonconsecutive vertices of `F`, again contradicting its face property. Both cases are impossible. Therefore no transition arc has one side.

If there was no one-side arc to begin with, the same conclusion already holds. Four arcs each having at least two sides force `m>=8`, and equality at `m=8` forces lengths `(2,2,2,2)`.

## Adversarial checks and verifier boundary

- **Quadrilateral exception:** the proof uses `m>=5`. The exact eight-site rectangle regression in Audit.83 is not an actual face: a middle unit chord splits it into smaller faces.
- **Hexagon regression:** Audit.83's regular-hexagon nonconstant states have a zero-distance endpoint collision. This is consistent with, and illustrates, the required full endpoint lower-feasibility hypothesis.
- **Eight-side sharpness:** the source report's rational eight-cycle was independently checked with integer arithmetic after scaling coordinates by 41. All 28 old and endpoint pair distances were enumerated; each has exactly the eight boundary contacts and no triangle. The sign sum is zero and every folded edge equals `s_iJq_i`. The least endpoint noncontact squared distance is `1922/1681>1`, confirming that the eight-side threshold cannot be raised. This finite check is not used in the proof.
- No source verifier encodes the analytic transition-arc argument. The exact check above verifies only the stated finite sharpness example; the proof is the angle and chord argument given here.

## Dependency, frontier effect, and remaining claims

The only theorem dependency is canonical `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION`. The face property and the exact quarter-fold edge increments are used at the stated finite scope. No result is claimed about transition patterns on quadrilaterals, faces with eight or more sides, source-level extraction of such a face, or full-source upper-diameter feasibility.

The C-II endpoint is unchanged: a fully feasible nonaffine fold is still neither supplied nor ruled out on larger faces, and the stress-currency implication still requires all full-source lower and upper checks. The report's separate eight-face area bound, transformed-hull coverage and population claims, and conditional endpoint embedding claims were not audited here and remain outside this promotion.
