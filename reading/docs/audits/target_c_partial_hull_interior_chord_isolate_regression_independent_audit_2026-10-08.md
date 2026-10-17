> Generated reading edition · [exact source](../../../docs/audits/target_c_partial_hull_interior_chord_isolate_regression_independent_audit_2026-10-08.md) · source SHA-256 `6d4c95e7fd28f06dc5d9fdefd3e5ee9c04158ca6a7e992bd1d5b505eb7c99ac8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B080632151D7","canonical":false,"claim_ids":["C-PARTIAL-WALL-INTERIOR-CHORD-ISOLATE-REGRESSION"],"claim_statuses":{"C-PARTIAL-WALL-INTERIOR-CHORD-ISOLATE-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit — partial-wall interior-chord isolate regression

**Date:** 2026-10-08  
**Audit base:** `419ab570f137bb5243155086285d10354b6c9616`, state `2026-10-08.audit.142`  
**Target:** C-II; C-II and Level I remain open.  
**Frozen source:** `research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5`.  
**Source report:** `docs/reports/target_c_exterior_cap_mixed_boundary_wall_capacity_2026-10-06.md`, SHA-256 `601865a16cd7c444696606e9cca2b09a47c494448d7aa050152baa3bad38a484`.  
**Source verifier:** `research/verify_target_c_exterior_cap_separator_refill_2026_10_06.py`, SHA-256 `a413e20ad53f1ba5685ff7d193ae157074b64793b94d618293289c84a8083c59`.

## Verdict

**REGRESSION VALID**, at the exact finite scope below. The coordinates were already checked as a boundary-condition example in Audits.140 and .141. This audit gives the example a separate theorem-state ID because it directly guards the actual-hull-arc hypothesis used by the exterior-cell shield.

## Exact statement

There is a finite unit-separated source with contact path

$$
(0,1)-(0,0)-(1,0)-(2,0)-(2,1)
$$

and a retained contact-isolated source point $q=(1,17/10)$. The apparent rectangular wall $[0,2]\times[0,1]$ has a nonunit top side of length two, but that side is an interior chord of the actual source hull because $q$ lies above it. After deleting the middle bottom vertex $v=(1,0)$, the point $x=(1,4/5)$ is strictly farther than one from all four remaining contact-path vertices, yet $|x-q|<1$. Thus a partial wall with a nonunit side that is not an actual source-hull side does not by itself shield a proposed replacement point from retained exterior labels.

This is an exact local feasibility regression. It is not asserted to satisfy canonical global-minimizer or KKT hypotheses, and it gives no Level I counterexample.

## Independent exact reconstruction

Write $S=\{a,v,b,\ell,r,q\}$, where

$$
a=(0,0),\quad v=(1,0),\quad b=(2,0),\quad \ell=(0,1),\quad r=(2,1),\quad q=(1,17/10).
$$

The four unit distances are exactly $\ell a,av,vb,br$. The remaining squared distances are

$$
|a-b|^2=4,\quad |a-r|^2=5,\quad |a-q|^2=389/100,\\
|v-\ell|^2=2,\quad |v-r|^2=2,\quad |v-q|^2=289/100,\\
|b-\ell|^2=5,\quad |b-q|^2=389/100,\\
|\ell-r|^2=4,\quad |\ell-q|^2=149/100,\quad |r-q|^2=149/100.
$$

All eleven displayed noncontacts have squared distance greater than one. Hence every old pair is at least one, and equality occurs exactly on $\ell-a-v-b-r$; $q$ has no unit contacts. The contact graph is a path plus an isolate, so it has no triangle.

Delete $v$ and consider $x=(1,4/5)$. Its squared distances to the four retained path vertices are

$$
|x-a|^2=|x-b|^2=41/25>1,
\qquad
|x-\ell|^2=|x-r|^2=26/25>1.
$$

But

$$
|x-q|^2=(17/10-4/5)^2=81/100<1.
$$

The point $x$ is inside the apparent rectangle. The top segment $\ell r$ is not on $\partial\operatorname{conv}(S)$: its endpoints are source labels, while the source label $q$ lies strictly above its supporting line. Its relative interior is therefore inside the actual source hull. In a genuine hull-augmented cell, source labels in that interior are part of the cell population and must be deleted or included in the exchange count; they cannot be treated as outside labels protected by an artificial hull side.

## Certificate review and distinction from the existing threshold regression

I inspected `partial_wall_regression()` in the frozen source verifier and reran it with exact integer arithmetic. It checks all 15 old pair distances, the four old contacts, the isolate condition, all four strict guard distances, and the colliding pair. It uses no floating-point tolerance. The function does not test global optimality or compute the convex hull; the latter is verified directly above from the location of $q$.

The already canonical `C-NONCONTACT-WALL-SQRT3-THRESHOLD-REGRESSION` concerns failure of an arbitrary polygon wall-vertex shield when its side-length cap exceeds $\sqrt3$. This example has a length-two side as well, but its separate route lesson is that this side is not an actual source-hull side and the retained isolate remains in the full source. It does not refute `C-EXTERIOR-INTERNAL-WALL-ONE-GUARD-CAPACITY` or `C-EXTERIOR-CELL-WEAK-GUARD-LEDGER`: their cell boundary is an actual hull arc, so the isolate here would be counted in the cell population rather than silently shielded outside it.

## Canonical disposition

Record `C-PARTIAL-WALL-INTERIOR-CHORD-ISOLATE-REGRESSION` as an exact scope guardrail. It refutes extending a one-vertex partial-wall shield by treating an arbitrary nonunit interior chord as part of the source-hull boundary while leaving the labels beyond it retained. It preserves the canonical actual-hull requirements and does not change the C-II frontier.
