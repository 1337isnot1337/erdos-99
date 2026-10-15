<!-- theorem-state: {"artifact_id":"ART-8D6670C16785","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C43: harmonic attachment hulls have disjoint interiors

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C36-C38 and convex geometry  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

For each unpinned component `I_r`, C36 gives a distinct loaded attachment set `A_r subset B_+` with

`I_r subset P_r := conv(A_r)` and `|A_r|>=3`.

C43 proves

`int(P_r) cap int(P_s) = empty` for `r!=s`.

Consequently

`sum_r area(P_r) <= area(F)`.

Thus the harmonic response components are localized in pairwise interior-disjoint convex cells whose vertices are loaded force-hull vertices.

## 1. Proper crossing is impossible

Fix `r!=s`. Suppose the polygon boundaries of `P_r` and `P_s` cross properly. Then an edge `ac` of `P_r` and an edge `bd` of `P_s` cross in their relative interiors. Since all four endpoints are vertices of the same convex force hull, the endpoints occur in alternating cyclic order on `partial F`.

But `a,c in A_r` and `b,d in A_s`, contradicting C36's noncrossing attachment theorem. Hence the two polygon boundaries have no proper crossing.

## 2. Containment is impossible

If two convex polygons have intersecting interiors and no proper boundary crossing, one is contained in the other. Suppose `P_s subset P_r`.

Every point of `A_s` is an extreme vertex of `F=conv(B_+)`. If `b in A_s\A_r`, then `b` cannot lie in `conv(B_+\{b})`, hence cannot lie in `conv(A_r)=P_r`, contradiction. Therefore `A_s subset A_r`.

Since `|A_s|>=3`, the two distinct unpinned components share at least three distinct loaded attachment vertices. Restrict the C37 incidence graph to the two interior nodes and any three shared loaded vertices. This gives a connected bipartite plane subgraph with `q=3`, `c=2`, `e=6`, while C37 gives `e<=q+2c-2=5`. Contradiction.

Therefore containment is impossible.

## 3. Theorem C43

The only remaining possibility is pairwise disjoint interiors:

`int(conv A_r) cap int(conv A_s) = empty` for `r!=s`.

Since every `P_r subset F`, finite additivity gives

`sum_r area(P_r) <= area(F)`.

Cells may share one or two loaded vertices or a common boundary chord; the theorem only asserts disjoint interiors.

## 4. Near-minimal interpretation

In the C33 near-minimal phase, C38 says all but `o(D)` loaded vertices belong to exactly one attachment set. C43 upgrades the earlier noncrossing-hypergraph picture to an actual nonoverlapping convex-cell decomposition, up to the same sublinear exceptional boundary set.

## Regression audit

- Two cells sharing one or two loaded vertices are allowed.
- Three shared loaded vertices are impossible by C37.
- Nested attachment cells are excluded by extremality plus C37.
- The theorem concerns harmonic attachment hulls, not arbitrary bridge-block convex hulls.
