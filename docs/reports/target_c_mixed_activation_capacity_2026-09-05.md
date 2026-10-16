<!-- theorem-state: {"artifact_id":"ART-9367C8B0434A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_mixed_activation_capacity_2026-09-05.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=3baa8526fa79dede56d9e038a7e4a7300fdbc797; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C102: mixed first-boundary capacity

**Date:** 2026-09-05  
**Repository base:** C101 branch after `6ef26015`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C82 chain-atom shell inequality, C87/C96 diameter-edge floor, C94 active-face flat, C101 activation-rank/area

C94 leaves a large exact tangent flat in the low-train pure-rhombic chain-face branch. C95 and C101 control triangle-free new-contact activations, but a first boundary event can also create new diameter equalities. C102 bounds the total diameter-equality rank by the global diameter-graph edge cap and then charges the unavoidable residual rank to the sharpened C101 triangle-free dissection theorem.

The result converts the mixed first-boundary obstruction into an explicit shell-area threshold.

## 1. Parameters

Let

`Delta_2=pi/(2sqrt(3))`,

`A=1+Delta_2`,

and along an asymptotic low-train chain-face sequence put

`x=T/D<3+o(1)`.

C82 gives

`x >= A/(1-y/2)+o(1)`,

where `y=q/T` and `q` is the diameter-endpoint/hull-endpoint count in the pure-rhombic exposed-hull normalization. Rearranging gives

`y <= 2-2A/x+o(1)`,

hence

### C102.1 — diameter-endpoint cap

`q/D <= 2x-2A+o(1)`.

This is the form already used in the C94/C96 low-train analysis.

The same asymptotic bound remains valid at a first outer-contact boundary point reached while preserving the old pure-rhombic disk and exact C80 chain face: the old rhombic train complex, train population `T`, chain atom, hull, and diameter endpoint set are still present in the limiting configuration. Adding an outer unit chord does not delete any of the data used in C82.

## 2. The old diameter graph already consumes `2D+1` edges

C87/C96 give at least

`2D+1`

actual source diameter edges before the continuation begins. The continuation under consideration preserves all original diameter equalities exactly until its first new-active boundary event.

Let `N_D` denote the number of newly activated diameter pairs at or before that first event. The complete diameter graph at the boundary therefore has at least

`2D+1+N_D`

edges.

Hopf--Pannwitz gives, for a planar diameter graph on `q` diameter endpoints,

`|E(H)|<=q`.

Therefore

`N_D <= q-(2D+1)`.

Using C102.1,

### Theorem C102.2 — new-diameter capacity

`N_D/D <= 2x-4-2Delta_2+o(1)`.

In particular throughout `x<3+o(1)`,

`N_D/D <= 2-2Delta_2+o(1)`

`=0.1862006358...+o(1)`.

The Jacobian rank contributed by all newly activated diameter equations is at most their number, so the same bound holds for new-diameter rank.

## 3. Residual contact rank

C94 gives an exact active-face tangent flat of dimension at least

`k/D >= 2A-x-o(1)`.

Suppose a first boundary event blocks all local continuation directions without immediately creating a unit equilateral triangle. Split the newly active equations into diameter equations and triangle-free contact equations. If their total Jacobian kills the `k`-dimensional tangent flat, then rank subadditivity gives

`rank_contact >= k-rank_diameter`.

Using C102.2,

`rank_contact/D`

`>= (2A-x)-(2x-4-2Delta_2)-o(1)`

`=6+4Delta_2-3x-o(1)`.

Thus:

### Theorem C102.3 — forced contact rank

In the low-train branch, any triangle-free mixed first-boundary event that blocks the entire C94 flat must activate triangle-free unit-contact constraints of train-angle rank at least

`boxed: [6+4Delta_2-3x-o(1)]D.`

For `x<3+o(1)`, this is uniformly at least

`(4Delta_2-3-o(1))D`

`=(0.6275987285...-o(1))D`.

## 4. Convert contact rank to shell area

The sharpened C101 theorem proves for an arbitrary simultaneous triangle-free first-contact family, including nested outer-pocket chords,

`rank_contact <= G/(2c_0)`,

where

`c_0=sqrt(3)/4`

and `G` is the pre-existing shell area defect of the old pure-rhombic disk. The factor two comes from the fact that the activation chords under each maximal root form a noncrossing dissection with no triangular cells.

Therefore C102.3 forces

### Theorem C102 — mixed activation shell threshold

`boxed: G/D >= 2c_0(6+4Delta_2-3x)-o(1).`

Across the whole low-train range `x<3+o(1)`,

`boxed: G/D >= 0.5435164422...-o(1)`

is necessary for a triangle-free first boundary to block the complete C94 flat.

At the lower extremal train scale `x=2+Delta_2+o(1)`, the threshold rises to

`2c_0 Delta_2 = pi/4 = 0.7853981634...`.

Thus the required shell budget varies linearly from approximately `0.785398D` near the C91 extremal train scale down to `0.543516D` at the top of the low-train phase.

## 5. What this settles

C102 removes two previously separate loopholes from the C94 activation program:

1. nested contact activations cannot hide rank, by C101's triangle-free dissection count;
2. new diameter equalities cannot absorb more than `0.186201D+o(D)` rank in the low-train phase, because the old diameter graph already uses `2D+1` of the Hopf--Pannwitz edge budget.

The remaining obstruction is now a quantitative shell question. A sufficient next theorem is

`G/D < 2c_0(6+4Delta_2-3x)-o(1)`

for the same low-train chain-face survivor. Any such upper bound contradicts C102 and forces a finite triangle-producing continuation.

No such upper bound is claimed here. The current Oler theory supplies strong lower bounds on `G`; those do not by themselves settle this comparison. The next step is to exploit the train geometry to upper-bound shell defect or to force a larger diameter/contact rank burden.