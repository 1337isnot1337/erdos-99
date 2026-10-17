> Generated reading edition · [exact source](../../../docs/reports/target_c_central_phase_block_endpoint_exclusion_2026-09-05.md) · source SHA-256 `86a41a6175b45594be2f90b1cf77bf42c251d14d742a2700830b08e0aa3a73f0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3BCDF54B2667","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C central-phase-block endpoint exclusion

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** repaired equality-case stability / phase-complete trimming  
**Target:** exact optimized two-wall endpoint  
**Status:** LEVEL I STILL OPEN

## 1. Scope and relation to the regression note

The earlier file
`target_c_two_wall_endpoint_exclusion_2026-09-05.md` correctly retracted an argument
that treated all omitted same-phase trains as `o(D)`.  That treatment was false.

The repair below uses a different fact: after selecting **central contiguous blocks**
of the ordered train families, omitted trains in the same center/leaf phases do not
separate the chosen central grid corners at all.  Their contribution is exactly zero.
The entire opposite residual phase is retained as the coherent `Theta(D)` cancellation
term in the trimmed-grid calculation.

## 2. Exact scalar endpoint and equality consequences

Let

`Delta=pi/(2sqrt(3))`,

`G(z)=integral_0^z sqrt(1-3t^2/4) dt`,

and let `r_*` be the unique root

`2G(r_*/2)=Delta`.

Numerically

`r_*=0.932935111451...`,

and put

`a=r_*/2=0.4664675557...`.

Assume for contradiction that a canonical C80–C96 chain-face survivor sequence has

`T/D -> 2+r_*`.

The exact two-side envelope gives the unique leading equality pattern

`q=o(1)`,

`lambda=a+o(1)`,

`mu=a+o(1)`.

Thus both boundary walls saturate their one-side `G(a)` capacity and all positive
quadratic crossing mass outside the chain-centered two-leaf phase star is `o(D^2)`.

As in the valid part of the regression note, saturation implies the following for
every fixed `0<p<a`.

1. After deleting `o(D)` exceptional short rows, the first `pD+o(D)` deepest nested
   rows on either boundary side share a consecutive interval of exact chain tracks of
   length

   `(U(p)-o(1))D`,

   where

   `U(p)=sqrt(1-3p^2/4)`.

2. In each such prefix the two residual projective phases are balanced:

   `(p/2+o(1))D`

   rows belong to each phase.

The second statement follows from the longitudinal part of the wall parallelogram:
if the two cumulative phase counts are `b_pD,c_pD`, then

`d_p^2+3p^2/4+(b_p-c_p)^2/4 <=1+o(1)`,

while saturation gives `d_p>=U(p)-o(1)` and
`U(p)^2+3p^2/4=1`.

## 3. Central-stack order lemma

The key repair is purely topological.

### Lemma CP1 — deepest opposite cap stacks form a central phase block

Let `Q` be one coherent residual train phase.  Every non-chain train in `Q` has both
terminals on one of the two boundary arcs `L,U` from `z` to `a`.  Trains in `Q` are
pairwise noncrossing.

On one side, order the `Q`-trains by decreasing boundary-cap interval.  The cap
intervals are nested.  A train omitted after a deepest prefix lies in the boundaryward
cap of the last retained train.

In the global order of the pairwise noncrossing phase family `Q`, the two side stacks
therefore occur as

`(shallow L ... deep L) | (deep U ... shallow U)`

up to reversing the whole order.  Consequently the union of a deepest prefix from the
L stack and a deepest prefix from the U stack is a **central contiguous block** of
`Q`.

Any omitted `Q`-train lies outside that block and does not separate any two vertices
inside the central strip bounded by the retained extremal `Q`-trains.

### Proof

For a train with both endpoints on `L`, let its `L`-cap be the component cut off next
to the boundary subarc between its terminals.  Pairwise noncrossing proper arcs with
endpoints on one boundary interval have disjoint-or-nested terminal intervals; inside
one phase/side wall the long intervals are nested.  If one terminal interval is
strictly contained in another, its cap is boundaryward of the larger/deeper arc.
Thus deleting the shorter tail of a nested wall deletes only boundaryward tracks.

The same holds on `U`.  An L-cap track and a U-cap track cannot cross.  There is no
third type of `Q`-track: C90 places both terminals of every non-chain residual train on
one of `L,U`.  Hence, after ordering the disjoint `Q` tracks transversely, every
boundaryward L track lies before every deepest L track, every boundaryward U track lies
after every deepest U track, and the two deepest stacks meet across the unique central
region between the L and U cap systems.  This gives the displayed order and the
nonseparation statement by Jordan separation.  QED.

There is an analogous elementary statement for the exact chain family `P`: a
consecutive interval of the linearly ordered disjoint `P` tracks is a central block
relative to its own extremal tracks, and tracks of `P` outside that interval do not
separate vertices in the strip between those extremals.

## 4. Build a phase-complete central grid

Fix

`p=1/5<a`.

On each boundary side take the first `pD+o(D)` deepest rows.  Their common P-intervals
have lengths

`(U(p)-o(1))D`,

with

`U(p)=sqrt(0.97)`.

The intersection of the two P-intervals is consecutive and has size at least

`(M-o(1))D`,

where

`M=2U(p)-1=2sqrt(0.97)-1`.

Call this consecutive center block `A`.

Choose one of the two residual phases, call it `B`.  By prefix phase balance, each
boundary side contributes `(p/2+o(1))D` B-trains.  Their union has

`(p+o(1))D`

trains.  Every one crosses every center train in `A`.

By Lemma CP1, after deleting the `o(D)` exceptional rows this union is a central
contiguous block of the full B-phase family.  Therefore:

- B-phase trains outside the selected block do not separate the central A–B grid
  corners;
- exact P-trains outside the consecutive center block A do not separate those corners.

This is the point missing from the retracted proof: the omitted same-phase populations
need not be small because their contribution to the selected corner displacement is
zero by order.

Let `C` denote the other residual phase.  We do **not** truncate or discard its
possible contribution.  The whole C phase has population

`(a+o(1))D`.

All crossings involving trains outside the three leading phase classes P,B,C are
`o(D^2)` at the exact scalar endpoint.

## 5. Fixed trimming and external error

The A–B subsystem is a complete topological grid with

`|A|=(M-o(1))D`,

`|B|=(p-o(1))D`.

Trim a fixed sufficiently small fraction from both ends of these **central blocks** as
in TG1.  Tracks of the omitted P and B phases remain outside the trimmed central
rectangle by CP1 and contribute zero to its opposite-corner difference.

A train outside P,B,C that separates the chosen diagonal must, by TG1, cross
`Omega(D)` tracks of the A–B grid.  Since all such external crossings total `o(D^2)`,
only `o(D)` external trains can contribute.  Their vector error is `o(D)`.

The C phase is retained exactly.  Coherence writes its total contribution as

`x w+o(D)`

for some `|x|<=aD+o(D)`, where after normalization

`u=(1,0)`,

`v=(1/2,sqrt(3)/2)`,

`w=(1/2,-sqrt(3)/2)`.

Letting the fixed trimming fraction tend to zero after the asymptotic limit gives a
source difference of the form

`M D u + p D v + x w + o(D)`

with `|x|<=aD+o(D)`.

## 6. Exact diameter cost

For real normalized `x`,

`|M u+p v+x w|^2`

`=M^2+Mp+p^2+(M-p)x+x^2`.

The unconstrained minimizer is

`x_*=-(M-p)/2`.

For the present constants,

`a>(M-p)/2`.

Indeed

`a=0.466467...`,

`(M-p)/2=0.384885...`.

So the entire C phase is large enough to realize the worst unconstrained cancellation.
The minimum is therefore

`3(M+p)^2/4`.

Now

`M+p=2sqrt(0.97)-4/5`.

A direct evaluation gives

`3(M+p)^2/4=1.02627...>1`.

For a completely elementary margin, use `sqrt(0.97)>0.9848`; then

`M+p>2(0.9848)-0.8=1.1696`,

and

`3(1.1696)^2/4>1.025`.

Thus, after the arbitrarily small fixed trim and the `o(D)` external error, the chosen
source difference has length strictly greater than `D`.  This contradicts the global
diameter bound.

### Theorem CP2 — optimized scalar endpoint is impossible

No canonical C80–C96 chain-face survivor sequence can satisfy

`T/D -> 2.932935111451...`.

Combining CP2 with the exact scalar envelope gives the strict asymptotic conclusion

`liminf T/D > 2.932935111451...`

for every canonical low-train chain-face survivor sequence.

## 7. What this does and does not prove

This theorem repairs the endpoint exclusion without resurrecting the invalid
cross-wall C91 Cartesian assumption.  The cross-side information is used only to
identify central contiguous train blocks.  The additive corner relation itself comes
from the valid complete-grid TG1 train-coordinate construction.

The theorem still does not rule out the whole interval

`2.932935111451... < T/D < 3`.

Away from exact scalar equality, same-phase rows omitted from a prospective complete
block need not be boundaryward in a sufficiently large central prefix, and complement
atomic mass can enter at positive density.  A quantitative phase-complete stability
theorem is still needed to push the constant substantially toward 3.
