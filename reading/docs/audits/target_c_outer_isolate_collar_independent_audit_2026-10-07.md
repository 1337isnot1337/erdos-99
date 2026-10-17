> Generated reading edition · [exact source](../../../docs/audits/target_c_outer_isolate_collar_independent_audit_2026-10-07.md) · source SHA-256 `e1388a8556fdc5b844b2d778b4c1a31038f5efb0e60ff184609b299c096c4112`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3987D8C7908B","canonical":true,"claim_ids":["C-OO-OUTER-ISOLATE-COLLAR-BOUND"],"claim_statuses":{"C-OO-OUTER-ISOLATE-COLLAR-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.105 — outer-isolate blocker collars

**Date:** 2026-10-07  
**Base:** `origin/main=0aa93dd448463ee2a8f964a42c28ada45a291941`, state `2026-10-07.audit.104`  
**Target:** C-II; C-I closed, C-II and Level I open  
**Verdict:** **PASS WITH NARROWED SCOPE — promote `C-OO-OUTER-ISOLATE-COLLAR-BOUND`.**

## Frozen source and audit boundary

I audited §§2–5 and the witness-location argument in §4 of
`docs/reports/target_c_outer_isolate_blocker_collars_2026-10-05.md` from the immutable
PR #722 source snapshot `research/target-c-residual-closure-20261005` at
`ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. The artifact SHA-256 is
`253ff02de18c916d411360e5d1a87b371b4eb4efb3746c594dc9607290ce51f7`.

The source report's §6 owner-count composition and its final owner-family exclusion are
not audited here. The loaded-neighbor theorem from Audit.104 is not needed for the
promoted result. In particular, this audit does not promote a bound on the number of
owners, safe singleton proposals, or simultaneous moves.

## Exact promoted statement

Consider any unbounded sequence of canonical post-ZF C-II sources in the Type-II branch
of `C-FULLCORE-NEAR-DISK`. For one source write

- `A` for the full unit-separated source, `K=conv(A)`, and `D=diam(A)`;
- `G` for its nonisolated positive-contact core, `F=conv(V(G))=conv(B)`, and `B` for
  the actual diameter endpoints;
- `q=|B|`, `b` for the occurrence-counted length of the old outer contact walk,
  `x_B=b-q`, and `a` for the number of nonunit sides of `F`;
- `L_add` for the sum of the lengths of those `a` sides.

Section 67 assigns every contact isolate in `F` outside the bounded physical contact
faces to one of the `a` convex outer pockets. Section 77 assigns every source point
outside `F` to a convex exterior cap. Let `R` range over those pockets and
nondegenerate exterior caps. Then, for all sufficiently large sources along the
sequence, the number `N` of distinct contact-isolated source points within distance
`5/4` of the boundary of at least one such region satisfies

```math
\boxed{N\le 48(x_B+a).}
```

The onset is sequence-dependent through the Type-II near-disk convergence. If in
addition `x_B+a=o(D)`, the number of distinct isolate endpoints available to obstruct
the audited small O–O lower clauses is `o(D)`.

The lower-clause interpretation is conditional on the canonical small O–O move scope:
the displacement cloud has diameter
```math
s<\min\{D-\sqrt{D^2-1},\sqrt2-1\},
```
bounded-face isolates are transported by their common core owner, outer-pocket isolates
are fixed, exterior isolates use the canonical long-pair dispatch with unanchored
isolates fixed, and unary rhombus blockers are handled separately. Under these
hypotheses, every isolate endpoint of a lower equality or violation lies in one of the
counted collars. The `o(D)` consequence bounds distinct isolate blockers; it does not
bound how many owners one isolate can obstruct.

## Independent proof

### Pocket perimeter

The Section 67 hull augmentation adds exactly `a` missing loaded-hull sides and creates
exactly `a` convex pockets. With `P_F=per(F)`, its Euclidean incidence identities give
```math
P_F=q-a+L_{add},\qquad
\sum_{P\text{ pocket}}P_P=b+2L_{add}-P_F.
```
The convex hull of the occurrence-counted outer contact walk has perimeter at most its
walk length, so `b>=P_F`. Hence `L_add<=x_B+a` and
```math
\sum_P P_P=x_B+a+L_{add}\le2(x_B+a).
```
These are the actual convex pockets inside `F`; bounded physical contact faces are not
included.

### Exterior-cap perimeter in the Type-II branch

By `C-FULLCORE-NEAR-DISK`, after translating the center of an inscribed disk of `F` to
the origin, there is a radius `r_D` with `B(0,r_D)\subset F` and `r_D/D\to1/2` along
the sequence. Put `R_D=D-r_D`. Every source point `z` satisfies `|z|<=R_D`: for
`z!=0`, the point `-r_D z/|z|` lies in `F` and is at distance `|z|+r_D` from `z`, at
most `D`. Thus `K\subset B(0,R_D)`.

For a loaded-hull chord with outward unit normal `u`, every point `z` on its associated
source-hull arc has `u·z>=r_D` and `|z|<=R_D`. Its radial direction is therefore
within `alpha_D=acos(r_D/R_D)` of `u`. For every source-hull edge on that arc, choose
an outward support normal `n`; because `F\subset K` and `B(0,r_D)\subset F`,
`n·z=h_K(n)>=r_D`, so `n` is also within `alpha_D` of `z`. Each arc edge direction
therefore differs from the chord direction by at most `2 alpha_D`. Projection onto the
chord direction, summed along the convex arc, gives
```math
\operatorname{length}(\text{arc})\le L/\cos(2\alpha_D),
```
where `L` is the chord length. Since `alpha_D->0`, every cap perimeter is at most
`(1+sec(2 alpha_D))L<=3L` for all sufficiently large sources. A positive-area cap
cannot have a unit chord: its source-hull arc contains at least two source-hull sides,
each of length at least one, whereas the projection estimate would make that arc
shorter than two. Therefore positive caps occur only at the `a` nonunit loaded-hull
sides, and
```math
\#\{\text{caps}\}\le a,\qquad
\sum_C P_C\le3L_{add}\le3(x_B+a).
```

Combining the two perimeter estimates, all pocket and cap regions together have total
perimeter at most `5(x_B+a)`, and their number is at most `2a`.

### Packing the boundary collars

For any convex region of perimeter `P`, its radius-`r` boundary tube has area at most
`2rP+pi*r^2`: the outer parallel body adds `rP+pi*r^2`, and erosion by `r` removes at
most `rP` since convex parallel perimeters are nonincreasing (with the empty erosion
case covered by the same area bound).

If a source isolate is within `5/4` of a region boundary, its open radius-`1/2` disk is
contained in that region's radius-`7/4` boundary tube. Those disks are pairwise
disjoint by unit separation. Summing the tube areas over at most `2a` regions and using
the total perimeter bound gives
```math
\frac\pi4N\le
2\frac74\,5(x_B+a)+\pi\left(\frac74\right)^2 2a,
```
so
```math
N\le\frac{70}{\pi}(x_B+a)+\frac{49}{2}a
<48(x_B+a),
```
using `pi>3` and `a<=x_B+a`. If `x_B+a=0`, there are no pockets or positive caps and
`N=0`.

### Location of lower-clause isolate endpoints

The canonical `C-OO-LOWER-BLOCKER-LOCALIZATION` argument rules out bounded-face isolate
endpoints after their common-owner transport, apart from the separately tested unary
rhombus clauses. In a sufficiently large Type-II source,
`D-sqrt(D^2-1)<1/4`, so a pair that becomes a lower equality or violation had old
distance at most `1+s<5/4` because the displacement cloud has diameter `s`.

An outer-pocket isolate is fixed. Its partner in a changed lower clause must move;
fixed pairs keep their old distance, other isolates in that pocket are fixed, and no
core vertex lies in the open pocket. The partner is therefore outside the pocket or
on its boundary. The segment joining the pair crosses the pocket boundary within
distance at most `1+s` of the isolate.

An exterior isolate that moves is an endpoint of a strict-long pair and hence an
extreme point of `K` by `C-LONG-PAIR-ISOLATE-DISPATCH`; it lies on the source-hull arc
of its assigned cap. If an exterior isolate is fixed and has a changed lower clause,
the other endpoint either lies outside that cap or is a moving exterior isolate on
its hull arc. In both cases the isolate is at distance at most `1+s` from the cap
boundary. Thus every isolate endpoint of a lower clause lies in a radius-`5/4` collar
counted by `N`.

## Dependencies, verification, and limits

Canonical dependencies: `C-FULLCORE-NEAR-DISK` for the Type-II near-disk regime;
`C-OO-LOWER-BLOCKER-LOCALIZATION` for the bounded-face transport and outer-face
localization; and `C-LONG-PAIR-ISOLATE-DISPATCH` for the extreme-point property of
moving exterior isolates. The convex-pocket identities are the canonical Section 67
module `C-RHOMBUS-POP`; Section 77 supplies the canonical exterior-cap partition.

The two relevant registered exact certificates were inspected and rerun:

- `research/verify_target_c_forest_isolate_dispatch_2026_10_01.py`: 10,524 finite
  graph packets, 143,852 binary label checks, 59,808 weighted difference systems, and
  the rational upper-exception regression passed. The code proves only those finite
  graph/difference-system statements and rational example, not the analytic cap bound.
- `research/verify_near_unit_face_conflicts_2026_10_01.py`: exact rational
  near-unit, rhombus, isolate-transport, and owner-cycle regressions passed. It does
  not prove the collar geometry or global optimality.

No new numerical verifier is claimed or needed. The proof of the collar estimate is
analytic and uses only the stated canonical convex geometry and unit separation.

Not promoted: the source report's §6 bound on owner counts and its claimed exclusion
of linear usable owner families. That argument needs an independent audit of the
singleton proposal hypotheses and of the owner/witness charging. This result does not
produce O–O moves, site capacity, simultaneous feasibility, or a finite competitor;
it only bounds distinct outer-isolate blockers in the specified Type-II near-disk
scope. C-II and Level I remain open.
