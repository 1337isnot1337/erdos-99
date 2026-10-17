> Generated reading edition · [exact source](../../../docs/reports/target_c_five_arc_eppstein_equality_audit_2026-09-10.md) · source SHA-256 `dbcb61b6d40e4f68b64cf9d5a409e5895720f9b0589f4b512e426ed8d0412517`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-09334C17CD3E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — audit of Eppstein near-equality at the five-arc endpoint

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910`  
**Audits:** `target_c_five_arc_pin_delay_09604_2026-09-10.md`, Section 8 / compact handoff  
**External source checked:** David Eppstein, *Triangle-Free Penny Graphs: Degeneracy, Choosability, and Edge Count*, Theorem 5.2  

## Correction

The five-arc theorem itself, including

```math
\liminf \mu_D\ge z_*>0.9604,
\qquad
10\arcsin z_*-4\pi=z_*/3,
```

is unchanged.

One sentence in its proposed next route is withdrawn: `r_r=o(D)` does **not** by
itself imply that the giant unloaded component is asymptotically quadrangulated or has
nearly minimum outer-face boundary.

Eppstein's bound

```math
e\le2n-\delta-2
```

is proved by induction on the number of vertices. Fix a graph-diameter pair `u,w`.
When the graph has a cycle, Eppstein's degree theorem supplies a degree-at-most-two
non-articulation vertex `v` distinct from `u,w`; deleting `v` removes one vertex and
one or two edges while leaving graph diameter at least `delta`. The theorem follows
inductively. The proof is not an Euler/outer-face equality argument.

Therefore near equality

```math
r_r:=2n_r-\delta_r-2-e_r=o(D)
```

should be interpreted only through that elimination proof: along a suitable recursive
reduction preserving a fixed diameter pair, the total loss from deletions of degree
strictly below two and from other induction slack is `o(D)`. This does not classify
bounded faces as quadrilaterals.

## Valid endpoint data retained

At a hypothetical `mu_D->z_*` endpoint, the preceding report still proves:

```math
\frac{\delta_r}{D}\to z_*,
\qquad
\frac{|A_r|}{D}\to z_*/3,
\qquad
\frac{t_r}{D}\to z_*,
```

for one giant unloaded component, while

```math
R_I/D\to0,
\qquad
s_B/D\to0.
```

Hence almost every one of the giant component's attachment pins uses all three loaded
contact slots into that component. Equality in the projective packing also saturates
the **total available angular measure** of a five-component maximal host.

The latter statement must not be strengthened to "every one of the five host
components contains an actual attachment pin" without an additional argument. A host
component may have zero limiting angular length, and total-measure saturation alone is
not an occupancy theorem.

These endpoint statements do not use an equality classification of Eppstein's theorem.

## 2026-09-11 independent certification and repair

The full load-bearing PR #188 chain has now been independently rederived in
`target_c_pr188_full_dependency_audit_2026-09-11.md`. That audit verifies the exact
ZE/ZT/PC/ZK ledgers, C35--C40 attachment structure, C49 cell disjointness, DB/FS/FSDB,
RP paired-pocket capacity, SC/JS side-cost accounting, RA/TA circle geometry, and FD's
pin-density delay. It also supplies a formal radial flat-side transfer lemma for the
step that RP/RLE previously stated only informally.

The result is:

```math
\boxed{\liminf\mu_D\ge z_*>0.9604}
```

with the original exact bracket `0.9604<z_*<0.961` certified as a valid report-level
Target C theorem.

The separate report
`target_c_attachment_perimeter_three_gap_endpoint_repair_2026-09-11.md` removes the
remaining endpoint ambiguity. It proves that an endpoint attachment limit must wrap
the common FS center; because every gap of the five-component maximal host is longer
than `pi/3`, wrapping forces the actual attachment limit to meet at least three host
components. Three actual inter-component gaps already contradict the direct planar
attachment-perimeter bound

```math
P_A\le4|A|-6.
```

Therefore no endpoint sequence `mu_D->z_*` exists. In particular there is a
nonexplicit absolute `epsilon_AP>0` such that every sufficiently large post-ZF C-II
survivor satisfies

```math
\boxed{\mu_D\ge z_*+\epsilon_{AP}.}
```

This endpoint repair uses neither Eppstein equality structure nor a five-populated-arc
claim.

## Correct next target

The Eppstein near-equality route, if used again, must use its actual inductive
content: a diameter-pair-preserving degree-two elimination with only `o(D)` total
deficit. It must not infer quadrangulation.

For the renormalized-surplus route, the first five-component endpoint is now excluded.
The remaining work is away from that endpoint: higher-surplus five-component states,
higher odd-component phases, and the unrestricted global C-II/contact-isolated-point
obstruction.

```text
CORRECTION TO FD HANDOFF:
  r_r=o(D) does not imply near-quadrangulation.
  Eppstein 2n-delta-2 is an inductive degree-two-removal theorem.
  Five-component host measure saturation does not by itself populate all five hosts.

CERTIFIED SURVIVOR:
  liminf mu_D >= z_* > 0.9604.

2026-09-11 ENDPOINT REPAIR:
  wrapping => at least three occupied host components;
  three host gaps + P_A<=4|A|-6 exclude mu_D->z_*;
  hence mu_D >= z_* + epsilon_AP for some absolute epsilon_AP>0.
```
