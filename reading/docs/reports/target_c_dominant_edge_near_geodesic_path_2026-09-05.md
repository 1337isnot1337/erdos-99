> Generated reading edition · [exact source](../../../docs/reports/target_c_dominant_edge_near_geodesic_path_2026-09-05.md) · source SHA-256 `9698be32382322296f941c5a50478e72e105b8ad3e0537fc1a4d6027a05fb964`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-31B8ED355D27","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C dominant-edge near-geodesic contact path

**Date:** 2026-09-05  
**Depends on:** `target_c_dominant_diameter_geodesic_flow_2026-09-05.md`, C98  
**Status:** LEVEL I STILL OPEN

## Theorem

Let `za` be a source diameter edge of KKT weight

`beta=1-eta > 1/2`.

Then the positive contact graph contains a simple `z`-to-`a` path `P` with `m` unit edges such that

`m-D <= 2D eta/(1-2eta)`.

Writing

`u=(p_a-p_z)/D`

and orienting the unit edge directions of `P` from `z` to `a` as `e_1,...,e_m`, the same path satisfies

`sum_(j=1)^m |e_j-u|^2 <= 4D eta/(1-2eta)`.

Consequently, for every fixed `theta>0`, the number of path edges whose angle from `u` is at least `theta` is at most

`D eta / [(1-2eta) sin^2(theta/2)]`.

In particular, if `beta=1-o(1)` then there is a simple contact path from `z` to `a` with

`m=D+o(D)`,

`sum_j |e_j-u|^2=o(D)`,

and only `o(D)` edges outside any fixed cone about the diameter direction.

## Proof

The dominant-edge flow theorem gives a cycle-free `z`-to-`a` contact flow with path decomposition

`f=sum_P x_P P`,

value

`F=D(2beta-1)=D(1-2eta)`,

and total weighted path excess

`sum_P x_P[m(P)-D] <= 2D^2 eta`.

Divide by `sum_P x_P=F`. At least one path has excess no larger than the weighted mean:

`m(P)-D <= 2D eta/(1-2eta)`.

For every `z`-to-`a` unit-edge path one has the exact identity

`sum_j e_j=D u`,

hence

`sum_j |e_j-u|^2 = 2[m(P)-D]`.

This gives the second inequality. If an edge makes angle at least `theta` with `u`, then

`|e_j-u|^2=4 sin^2(angle(e_j,u)/2) >=4 sin^2(theta/2)`.

Divide the total directional-energy bound by this amount to obtain the bad-edge count. `square`

## Interface with C97

C97 excludes the exact equality model in which a diameter pair is joined by a straight `D`-edge contact chain inside the pure rhombic train regime. C98 plus the theorem above now gives the quantitative precursor:

> the single-port near-zero branch contains a diametral contact path with sublinear length excess and sublinear fixed-angle defect count.

The remaining stability theorem must show that a C97-compatible terminal twist or an escape from the pure-rhombic topology costs a non-sublinear amount of this path defect, contact capacity, shell area, or response defect. No such lower bound is claimed here.
