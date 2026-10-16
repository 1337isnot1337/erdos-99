<!-- theorem-state: {"artifact_id":"ART-71609BC9B8F6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C prefix-fiber split budget

**Date:** 2026-09-04  
**Repository base:** research branch; endpoint-overlap audit corrected 2026-09-04  
**Run type:** exact combinatorial consequence of C87 + C96  
**Target:** near-spanning common-cut diameter forest  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

The `2D` selected C87 paired staircase diameters are indexed by a side `L/U` and a prefix level `k in {0,...,D}` at each endpoint. C83 prefix levels are not unique physical vertices. In particular, a selected endpoint at level `0` need not be the chain endpoint `z`, and a selected endpoint at level `D` need not be `a`.

This note gives the exact bookkeeping for physical splitting and endpoint reuse. It also records the resulting upper split budget from C96.

## 2. Selected endpoint fibers

Let `G_P` be the C87 staircase tree on prefix levels `0,...,D`. It has exactly `D` edges. For every simple edge `{a,b}`, choose the two C87 physical diameter pairs in the two arc orientations. Call the resulting `2D`-edge source graph `H_pair`.

For every side `X in {L,U}` and prefix level `k`, let

`n_(X,k)`

be the number of distinct physical selected endpoints on arc `X` at prefix level `k`.

Every prefix level has positive tree degree, so

`n_(X,k)>=1`.

Define the split excess

`S = sum_(X,k)(n_(X,k)-1)`.

Thus `S=0` means one selected physical endpoint per side-level fiber; it does **not** mean those endpoint-level vertices are necessarily `z` or `a` at levels `0,D`.

## 3. Cross-side endpoint overlap

The arcs `L,U` meet only at `z,a`. Hence the only possible physical vertex counted in two side-level fibers is `z` between `(L,0),(U,0)` or `a` between `(L,D),(U,D)`.

Let

`o in {0,1,2}`

be the number of these endpoints that occur in selected edges in **both** side fibers. Then the number of distinct physical vertices incident to `H_pair` is exactly

`v_pair=2(D+1)+S-o`.

Every selected edge crosses the C87 common train `tau_r`, so `H_pair` is a subgraph of the C90/C96 forest `H_(tau_r)`. Therefore `H_pair` is a forest. If `c_pair` is its number of nontrivial components,

`c_pair=v_pair-2D`

`=2+S-o`.

In particular

`S<=c_pair`.

This is the correct physical version of the doubled prefix-tree lift.

## 4. Add the literal chain diameter

Let

`r0 in {0,1,2}`

be the number of literal chain endpoints among `{z,a}` that occur somewhere as vertices of `H_pair` at all. Necessarily

`o<=r0`.

Now add the chain diameter `h0=za`. The graph

`H_0=H_pair union {za}`

still lies inside the common-cut diameter forest. It has

`2D+1`

edges and

`v_0=v_pair+(2-r0)`

vertices. Hence its number of nontrivial components is exactly

`c_0=v_0-(2D+1)`

`=3+S-o-r0`.

The forest condition additionally forbids `z,a` from already lying in the same component of `H_pair` when both are present.

### Lemma FSB.1 — exact selected-plus-chain component count

`c_0=3+S-o-r0`.

This formula resolves the apparent double-cover cycle issue. If both lifted copies use `z,a` in both side fibers, two endpoint identifications can indeed create a cycle and require splitting. But C87 does not force that reuse pattern: selected level-`0,D` endpoints can be different hull vertices.

## 5. Compare with the complete common-cut forest

Write, as in C96,

`m_r=2D+1+e_r`

and let `c_r` be the number of nontrivial components of the complete common-cut diameter forest `H_(tau_r)`.

Starting from `H_0`, the complete graph adds `e_r` edges, possibly together with new incident vertices. Each added edge can merge at most two old components, so

`c_0<=c_r+e_r`.

C96 gives

`q-(2D+2) >= e_r+(c_r-1)`,

or

`e_r+c_r<=q-(2D+1)`.

Thus

`3+S-o-r0 <= q-(2D+1)`.

Equivalently:

### Theorem FSB — exact overlap-sensitive split budget

`S <= q-2D-4+o+r0`.

Since `o+r0<=4`, the clean universal consequence is

`S<=q-2D`.

This is the bound used in later asymptotic arguments.

At the minimum endpoint count `q=2D+2`, the exact inequality becomes

`S+2<=o+r0`.

Thus a completely unsplit model `S=0` is possible only if the selected paired graph reuses enough of the literal chain endpoints. One legal combinatorial pattern is `r0=2,o=0`: `z` occurs in only one level-0 side fiber, `a` in only one level-D side fiber, the two lifted prefix-tree copies remain separate, and the chain edge joins their components. This is the true minimum-slack unsplit model.

## 6. Low-train consequence

C82 gives, for `x=T/D`,

`q/D <= 2x-2(1+Delta)+o(1)`.

Therefore

`S/D <= 2x-2(2+Delta)+o(1)`.

If `x=2+Delta+delta`, then

`S/D<=2delta+o(1)`.

In the full C94 low-train phase `x<3+o(1)`,

`S/D <=2-2Delta+o(1)`

`=0.1862006358...+o(1)`.

Every side-level fiber split consumes at least one unit of `S`. Hence at least

`D+1-S`

prefix levels are double-unsplit, asymptotically at least

`(2Delta-1-o(1))D`

throughout the low-train phase.

## 7. Regression note

An earlier revision of this report incorrectly asserted that level `0` and level `D` selected endpoints are automatically the literal chain endpoints `z,a`, and from that claimed `S>=2`. That assertion is false: prefix level records which `P` trains separate the vertex, not uniqueness of the physical hull vertex in the endpoint gaps. The exact overlap-sensitive formula above replaces that claim.

## 8. Frontier effect

The useful surviving statement is

`S<=q-2D`,

with the sharper exact relation involving `o,r0`. A closing argument must force more physical side-level splitting than this budget allows, or rule out the endpoint-reuse patterns permitted by the minimum-slack model through equal-length diameter geometry, unit separation, or KKT weights.
