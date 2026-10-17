> Generated reading edition · [exact source](../../../docs/reports/target_c_common_cut_fan_capacity_2026-09-04.md) · source SHA-256 `51009bf561dace0286cb81432cdde8b83ae2967ec85f05553a535ab86fce41f7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-07BD26F9A0A1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C common-cut fan-capacity audit

**Date:** 2026-09-04  
**Repository base:** `89c17412`  
**Run type:** exact structural lemma / route limitation  
**Target:** C96 near-spanning common-cut caterpillar  
**Status:** LEVEL I STILL OPEN

## Purpose

C96 gives one chain train `tau_r` whose complete crossing diameter graph is a
caterpillar forest with at least `2D+1` edges and therefore at least `2D+2`
diameter endpoints. A natural next attempt is to show that repeated reuse of one
endpoint by many of those diameter edges is too expensive angularly.

This note proves the sharp elementary fan-capacity inequalities available from the
existing global shared-endpoint angle theorem C18 and unit separation. They are useful
local constraints, but their global sum is too weak to improve C96's endpoint floor.
Thus a closing theorem must use more than diameter degree/fan counting alone.

## 1. Finite shared-endpoint angular width

Let `A` be a global minimum-diameter unit-separated source of diameter `D`, and let
`b` be incident to at least one diameter pair. Define

`N_D(b)={y in A: |b-y|=D}`

and `d_D(b)=|N_D(b)|`.

C18 proves that if `y,z in N_D(b)` are distinct, then their angle at `b` is strictly
less than

`Theta_D = [D(5*pi/6-sqrt(3)) + 4*pi/3 + pi/(2D)]/(D+1)`,

whenever this is below the elementary `pi/3` bound. Put, uniformly,

`W_D=min(pi/3,Theta_D)`.

Every pair of distinct diameter partners also obeys unit separation. If the angular
separation of the rays `by,bz` is `theta`, then

`|y-z|=2D sin(theta/2)>=1`.

Hence

`theta >= delta_D := 2 asin(1/(2D))`.

Ordering all rays from `b` inside their C18 angular interval gives

`(d_D(b)-1) delta_D < W_D`.

Therefore:

### Lemma F1 — diameter fan capacity

For every diameter endpoint `b`,

`d_D(b) <= ceil(W_D/delta_D)`.

In particular, since `delta_D=1/D+O(D^-3)` and

`W_D -> theta_infty := 5*pi/6-sqrt(3)=0.8859430704...`,

`d_D(b) <= (theta_infty+o(1))D`.

So one source point cannot support more than about `0.885944D` diameter partners.
This is stronger than the raw unit-circle bound coming only from the elementary
`60 degree` diameter-star width.

## 2. Exterior-normal localization

The same argument has a global convex-hull form that does not use C18.

Fix a diameter pair `by`. For every `x in A`, the diameter condition gives

`|x-y|^2 <= |b-y|^2=D^2`.

Writing `r=y-b`, expansion yields

`(x-b) dot r >= |x-b|^2/2`.

Thus `b-y=-r` is a strict outward normal of `conv(A)` at `b`. In particular every
diameter endpoint is an exposed convex-hull vertex, and all rays from `b` to its
diameter partners, after reversal, lie in the exterior normal cone at `b`.

Let `alpha_b` be the angular width of that normal cone, i.e. the exterior angle of the
convex hull at `b`. For any subset of `d` diameter edges incident to `b`, ordering
their directions and using the same unit-separation estimate gives

`(d-1) delta_D <= alpha_b`.

Summed over distinct convex-hull vertices,

`sum_b alpha_b = 2*pi`.

Therefore:

### Lemma F2 — global diameter-fan budget

Let `F` be any forest contained in the complete diameter graph. If `m=|E(F)|` and
`c` is the number of nontrivial connected components, then

`(m-c) delta_D <= 2*pi`.

Proof. If `d_F(b)` is the degree in `F`, then

`(d_F(b)-1)delta_D <= alpha_b`

at every nonisolated vertex. Sum over the nonisolated vertices. A forest with `m`
edges and `c` nontrivial components has `v=m+c` incident vertices, so

`sum_b(d_F(b)-1)=2m-v=m-c`.

The sum of the corresponding exterior angles is at most `2*pi`. This proves the
claim.

## 3. Apply to the C96 common-cut caterpillar

Let `H_(tau_r)` be the C96 complete diameter graph crossing the common chain train.
Write

`m_r=|E(H_(tau_r))|`, `c_r=# nontrivial components`.

C96 gives

`m_r>=2D+1`

and proves that `H_(tau_r)` is a caterpillar forest. Lemma F2 therefore supplies

`(m_r-c_r) delta_D <= 2*pi`.

At the C96 minimum `m_r=2D+1`, `c_r=1`, the left side is

`2D delta_D = 4D asin(1/(2D)) = 2+O(D^-2)`,

well below `2*pi`.

Thus the global angular budget has a factor larger than three of slack in precisely
the near-spanning regime that C96 asks us to eliminate. Lemma F1 also permits a
single caterpillar vertex to have linear degree, so a leaf-rich endpoint-reuse phase
is not excluded locally either.

### Corollary F3 — degree-only C96 closure fails

C18 plus unit separation, even when supplemented by the exact convex-hull normal-cone
sum, does **not** force an endpoint count stronger than C96's

`q>=2D+2`.

Any improvement must exploit additional structure: the C87 paired staircase order,
the C93 secondary-train separation budget, equal-length diameter geometry across two
ordered hull arcs, KKT weights, or the C94 exact-active-face flat.

This is a limitation of this proof mechanism, not a construction of a global
minimizer realizing equality.

## 4. Exact next obligation

The most economical next target is an incidence-capacity theorem coupling the C87
staircase and C90 caterpillar descriptions. C93 supplies

`D(D+1)`

selected-diameter/non-chain-train separation incidences. A useful theorem must show
that a secondary train cut carrying many of these selected diameters incurs a
quantitative loss that cannot be hidden by high-degree caterpillar vertices.

A degree bound alone cannot provide that loss; the ordered positions of the selected
staircase intervals have to enter.
