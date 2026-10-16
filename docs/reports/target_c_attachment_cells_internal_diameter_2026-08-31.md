<!-- theorem-state: {"artifact_id":"ART-7C4F88AC9523","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C46: at most three harmonic attachment cells contain an internal full-diameter edge

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** Reuleaux-triple exclusion, C35-C36, C43, planar diameter-thrackle geometry  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

For an unpinned harmonic component `I_r`, let `P_r=conv(A_r)` be its C43 attachment cell. Call a full core diameter edge **cell-internal** to `r` when both endpoints lie in `A_r`.

For every sufficiently large source for which a diameter triangle is excluded,

`#{r : P_r contains a cell-internal full diameter edge} <= 3`.

Thus, except for at most three harmonic response cells, every full diameter partner of every attachment vertex lies outside that same attachment cell.

## 1. Internal diameter chords from distinct cells cannot be vertex-disjoint

Let `r!=s`, and let `ac` be a full core diameter edge with `a,c in A_r`, while `bd` is a full core diameter edge with `b,d in A_s`.

If the two edges have four distinct endpoints, the planar diameter-thrackle theorem says the two straight chords cross properly.

But `ac subset P_r`, `bd subset P_s`, and C43 gives disjoint polygon interiors. Two convex polygons with disjoint interiors cannot contain properly crossing vertex chords: a non-boundary chord crosses through the polygon interior, while a proper crossing of a boundary side locally enters the corresponding interior. Hence a proper chord crossing forces an interior intersection.

Contradiction. Therefore any cell-internal diameter edge from `P_r` and any one from `P_s` share at least one loaded endpoint.

## 2. Four pairwise-intersecting graph edges are a star or triangle

Suppose four distinct cells each contain an internal diameter edge, and choose one edge from each. By Section 1 these four 2-element endpoint sets are pairwise intersecting.

A pairwise-intersecting family of graph edges has one of two forms:

1. all chosen edges share one common vertex; or
2. the distinct chosen edges are contained in the three edges of one triangle.

Indeed, after choosing distinct edges `ab,ac`, any further edge meeting both either contains `a` or is `bc`. If `bc` occurs, every edge meeting all three is one of `ab,ac,bc`.

## 3. Both alternatives are impossible for four cells

In the triangle alternative, `ab,ac,bc` are all full diameter edges, so `a,b,c` are three pairwise diametral source points. Target C's Reuleaux-triple theorem excludes this for all sufficiently large minimizers (canonical explicit threshold `n>=362`).

Hence the four chosen edges would have to share one loaded vertex `b`. Then `b in A_r` for all four cells. Membership in `A_r` requires at least one unit contact from `b` into component `I_r`, and distinct components require distinct contact edges. C35 gives `deg_C(b)<=3` for every loaded vertex. Thus one loaded vertex cannot belong to four attachment sets.

Contradiction.

## 4. Theorem C46

For every sufficiently large fully force-visible Target C survivor,

`#{r : exists uv in H^circ with u,v in A_r} <= 3`,

where `H^circ` is the full source diameter graph restricted to the nonisolated contact core.

## 5. Response interpretation

C38 says that near the C33 boundary minimum almost every loaded vertex belongs to exactly one of `o(D)` noncrossing attachment cells. C46 says that all but at most three of those cells must export their full-diameter coupling to other cells or to the exceptional loaded set.

Thus the near-minimal C11 geometry has a contact-local / diameter-nonlocal split:

- contact response is harmonic inside pairwise interior-disjoint cells;
- full-diameter coupling is forced across those cells except for at most three of them.

This is a concrete target for the identity `Lambda P_B=L_H P_B`.

## Regression audit

- One cell may contain many internal diameter edges; C46 bounds the number of cells, not the number of edges.
- Two or three cells may contain internal diameter edges through a common loaded pin; loaded contact degree three allows this.
- Three triangle edges are globally excluded only in the sufficiently large regime, exactly as stated.
