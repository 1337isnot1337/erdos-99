> Generated reading edition · [exact source](../../../docs/reports/target_c_mixed_side_ferrers_capacity_2026-09-04.md) · source SHA-256 `247b39567b7e95a8558cce078ebd4f8c419e20050475a2ab3672bb40b2dfe3f4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-35BB456B4F43","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_mixed_side_ferrers_capacity_2026-09-04.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=28d4ef364eb1f54f0a1c1d12892a5c89476a3a04; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C mixed-side Ferrers capacity

**Date:** 2026-09-04  
**Repository base:** research branch after `e7a03582`  
**Run type:** exact geometric refinement of C91-C92  
**Target:** pure-rhombic C80-C96 chain-face branch  
**Status:** LEVEL I STILL OPEN

## 1. Main result

Let

`Delta=pi/(2sqrt(3))`.

C91 split the residual train population into four walls: two residual phase
neighborhoods times the two boundary sides `L,U`. The phase split was needed there to
ensure that the vector sum across an all-ones train rectangle has length almost equal
to the number of residual rows.

There is a stronger phase-free estimate. Once short rows are deleted, all residual
rows on one boundary side are mutually noncrossing and nested. More importantly, the
boundary side fixes the sign of their transverse train vectors. Every train crossing a
chain train makes an angle strictly greater than `pi/3`, so a same-side mixed-phase
sum has transverse magnitude at least `sqrt(3)/2` per row.

This collapses the four C91 walls to two mixed walls, with a weaker but still strong
circular profile.

### Theorem M1 — improved chain-face train surplus

Every asymptotic canonical pure-rhombic C80-C96 chain-face survivor satisfies

`liminf T/D > 2.919`.

No phase-coherence estimate is used inside a wall; the proof uses only C77 train
triangle-freeness, C90 boundary-side localization, the exact C80 chain, and the C91
Cartesian/parallelogram argument.

## 2. Topological orientation of a non-chain train

Let

`h0=za`, `u=(a-z)/D`,

and let `P={tau_1,...,tau_D}` be the exact C80 chain trains. As in C87, split the convex
boundary at `z,a` into arcs `L,U`, both ordered from `z` to `a`, and choose the sign of
`Ju` toward `U`.

Every `tau_j in P` separates `z` and `a`, so it has one terminal on each of `L,U`.
Orient `tau_j` from its `L` terminal to its `U` terminal. In the C77 convention its
unit transversal can then be taken to be exactly `u`: along that orientation the
`Ju` coordinate increases.

Now let `sigma notin P`. C90 proves that both terminals of `sigma` lie on one of the
two arcs, say `U`. Let `C_sigma` be the boundary cap between those terminals contained
in `U`. Orient `sigma` so that this cap lies to the left of the oriented track, and
let `v_sigma` be its C77 unit transversal, pointing from the right side of `sigma` to
the left side. Thus `+v_sigma` points from the side containing `L,z,a` into the cap.

If a chain train `tau_j` crosses `sigma`, its `U` terminal lies inside `C_sigma`; its
`L` terminal lies outside. Hence, along the `L`-to-`U` orientation, `tau_j` crosses
`sigma` from right to left. C77's crossing-orientation rule gives

`det(u,v_sigma)>0`.

If instead both terminals of `sigma` lie on `L`, choose the analogous cap orientation.
A chain train then leaves the cap on its way from `L` to `U`, so

`det(u,v_sigma)<0`.

At every actual train crossing, C77 gives strict acute projective angle greater than
`pi/3`. Consequently

`|det(u,v_sigma)| > sqrt(3)/2`

for every non-chain train `sigma` that crosses a chain train.

### Lemma M2 — same-side transverse sign

After orienting every non-chain train into its `L`- or `U`-boundary cap,

- all `U`-side train vectors have `Ju` projection greater than `sqrt(3)/2` whenever
  they cross `P`;
- all `L`-side train vectors have `Ju` projection less than `-sqrt(3)/2` whenever
  they cross `P`.

This statement is independent of which of the two projective `60-degree` phase
neighborhoods the train belongs to.

## 3. Long residual rows on one side are nested even across phases

For a residual train `sigma`, let

`J_sigma subseteq {1,...,D}`

be its consecutive interval of chain trains crossed by `sigma`, as in C91.

Suppose two residual trains `sigma,rho` satisfy

`|J_sigma|>D/2`, `|J_rho|>D/2`.

Then the two intervals overlap, so there is a chain train `tau_j` crossing both.
If `sigma` and `rho` crossed each other, the three train tracks

`tau_j, sigma, rho`

would be pairwise crossing. C77 proves that the train-intersection graph is
triangle-free. Therefore `sigma` and `rho` do not cross.

If their terminals lie on the same boundary side, two noncrossing proper arcs with
both endpoints on that boundary interval cut off subintervals that are either disjoint
or nested. Their chain-crossing intervals inherit the same relation. Since both have
length greater than `D/2`, they cannot be disjoint.

### Lemma M3 — two mixed Ferrers walls

After deleting rows with at most `D/2` chain crossings, all remaining residual trains
on `U` form one nested wall, and all remaining residual trains on `L` form one nested
wall. No phase subdivision is needed.

## 4. Circular profile for one mixed wall

Take one of the two side walls and sort its rows by decreasing chain interval length,

`d_1>=d_2>=...>=d_b`.

For the first `j` rows, nesting gives a common set of `d_j` exact chain trains, hence a
complete `d_j x j` train rectangle. Use the same additive-grid construction as C91.
The chain displacement is

`U=d_j u`,

so `|U|=d_j`.

Orient each residual train vector `v_k` into its common boundary side as in Lemma M2,
and put

`V=sum_(k=1)^j v_k`.

All summands have the same sign of transverse projection. Therefore

`|V| >= |Ju dot V| > (sqrt(3)/2) j`.

The four grid corners are source vertices. Both parallelogram diagonals are source
differences, so their lengths are at most `D`. The parallelogram law gives

`|U|^2+|V|^2 <= D^2`.

Hence

`d_j^2 + (3/4)j^2 < D^2`.

Thus, if the wall has `lambda D+o(D)` rows, its total chain-crossing count obeys

`e_wall/D^2 <= G(lambda)+o(1)`,

where

`G(lambda)=integral_0^lambda sqrt(1-3t^2/4) dt`.

The function `G` is concave on the relevant interval. If the two side walls together
contain at most `sD+o(D)` long rows, Jensen gives

`e_long/D^2 <= C(s)+o(1)`,

where

`C(s)=2G(s/2)`.

For later use,

`C'(s)=sqrt(1-3s^2/16)`.

Also, from `sqrt(1-z)<=1-z/2`,

`G(lambda)<=lambda-lambda^3/8`,

so

`C(s)<=s-s^3/32`.

## 5. Leading atomic mass bookkeeping

Pass to a subsequence with

`x=T/D`, `r=x-2`.

C87 gives `q/D>=2+o(1)`. The Target B Section 39 exposed-hull bound used in C92 then
implies that the total atomic train population outside the exact `D` chain trains is
at most

`rD+o(D)`.

The total leading rhombus crossing count is

`Delta D^2+o(D^2)`.

Relative to the exact chain phase, only the two projective phase points at `+-pi/3`
can carry positive-density crossings with the chain atom. Let `sD+o(D)` be the total
atomic population on those phase points that actually carry a positive limiting edge
to the chain atom. Call exact-`P` crossings to those trains **good** and let their
coefficient be `g`:

`e_good=gD^2+o(D^2)`.

All remaining non-chain atomic trains have population at most

`(r-s)D+o(D)`.

There is no positive-density crossing edge between two of the `sD` good-phase
populations: if both `+pi/3` and `-pi/3` are joined to the chain atom, an edge between
them would make a triangle in the limiting train-crossing graph; within one phase
there are no crossings. Therefore every leading crossing that does not use one of the
exact `P` trains has at least one endpoint in the remaining `(r-s)D` population.

The crude complete-graph capacity is enough:

`e_bad <= r(r-s)D^2+o(D^2)`.

Hence

`g >= Delta-r(r-s)`.

## 6. Short-row deletion and the necessary mixed-wall inequality

The `sD+o(D)` good-phase residual trains have at most `sD^2+o(D^2)` possible
incidences with `P`. Thus their missing incidence coefficient is at most

`s-g`.

Delete every such residual train crossing at most `D/2` chain trains. For each deleted
row its number of present chain incidences is at most its number of missing ones.
Therefore all deleted rows together contribute at most

`(s-g)D^2+o(D^2)`

good crossings.

By Lemma M3 the remaining rows form only the two mixed side walls, and Section 4 gives
capacity at most

`C(s)D^2+o(D^2)`.

Consequently

`g <= C(s)+(s-g)`,

or

`2g <= C(s)+s`.

Combining with the bad-crossing lower bound yields the necessary condition

`H_r(s):=C(s)+s-2Delta+2r(r-s) >=0`.

## 7. Uniform contradiction for r<=0.919

Assume

`r<=0.919`.

Because `0<=s<=r`,

`H_r'(s)=sqrt(1-3s^2/16)+1-2r`.

Use `sqrt(1-z)>=1-z` for `0<=z<=1`:

`H_r'(s) >= 2-2r-3r^2/16`.

The right side is decreasing on this range, and at `r=0.919` it is

`0.0036448...>0`.

Thus `H_r` is increasing in `s`, so

`H_r(s)<=H_r(r)=C(r)+r-2Delta`.

Using the elementary upper bound from Section 4,

`H_r(r) <= 2r-2Delta-r^3/32`.

This expression is increasing for `r<1`, hence it is at most its value at `0.919`.
Using the safe numerical bound

`Delta>0.90689`,

we get

`H_r(r)
 < 1.838-1.81378-0.919^3/32
 = -0.0000347... <0`.

This contradicts the necessary condition `H_r(s)>=0`.

Therefore no asymptotic canonical survivor has

`x=T/D <= 2.919`.

This proves Theorem M1.

## 8. Numerical location of this specific capacity threshold

For orientation only, solving the exact scalar equation

`C(r)+r=2Delta`

gives

`r=0.919347127...`,

or

`x=2.919347127...`.

That numerical root is not promoted as the theorem; the certified statement above is
the clean strict bound `T/D>2.919`.

## 9. Frontier effect

The four-wall phase cancellation that limited C91 is not real once wall membership is
organized by boundary side and C77's crossing orientation is retained. The remaining
survivor has at least

`0.0121003... D`

more trains than the original C89 endpoint lower bound.

The same scalar argument cannot reach `T/D=3`; the mixed-side capacity becomes large
enough before then. The next additional input should be C78's per-train degree/width
bound or the C93/C96 simultaneous staircase-caterpillar structure.
