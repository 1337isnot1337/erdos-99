> Generated reading edition · [exact source](../../../docs/reports/target_c_activation_rank_area_2026-09-05.md) · source SHA-256 `d00712f15a371dae7080b643f6563c0798a5238f0ef691d4c9bd45a18d6b7f95`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CCF1A07A22A5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C101: activation-rank versus shell-area theorem

**Date:** 2026-09-05  
**Repository base:** C100 branch after `c9bbcef0`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** Oler-shell equation (21.11), C95 contact-activation pocket localization

C95 shows that every triangle-free first new unit contact along an exact active-face continuation lies in an old outer indentation pocket and closes a convex subpocket of area at least `c_0(r-1)`, where `r` is the length of the old unit-edge boundary subchain and `c_0=sqrt(3)/4`. The remaining loophole was nesting: simultaneous first-contact subpockets need not be disjoint.

Nesting is not only harmless; triangle-freeness makes it quantitatively sparse. Under one maximal activation chord, all nested simultaneous activation chords form a noncrossing dissection of a convex unit-edge polygon with no triangular face. Euler counting then bounds the entire chord family by half the old boundary length. Combined with C95's Oler charge, this yields a factor-two rank/area theorem.

## 1. Laminar maximal activation pockets

Fix one old indentation pocket. At a simultaneous first-contact time, the new unit chords are pairwise noncrossing by C95. Their endpoint intervals on the old unit-edge boundary chain are therefore laminar: two such intervals are disjoint up to endpoints, or one is contained in the other.

Call a new chord **maximal** if its old-boundary interval is not properly contained in another activation interval in the same old pocket.

Across all old indentation pockets, let the maximal activation chords have old boundary-chain lengths

`r_1,...,r_t`.

C95 gives `r_i>=3` in the triangle-free case. The corresponding maximal convex subpockets have pairwise disjoint interiors: different old pockets are disjoint, and within one convex pocket maximal noncrossing chord intervals are disjoint rather than nested.

Every nonmaximal activation chord lies inside exactly one maximal activation subpocket.

## 2. One maximal root gives a unit-edge polygon

Fix a maximal activation chord `xy` whose old boundary subchain is

`x=v_0,v_1,...,v_r=y`.

The old chain has `r` unit edges and the new chord `xy` also has length one. C95 proves that the region `C_xy` enclosed by this chain and `xy` is convex.

Therefore its boundary is a convex polygon with

`N=r+1`

vertices and **every boundary edge has length one**.

Every simultaneous activation chord nested under `xy` is a noncrossing diagonal of this polygon, also of length one.

Let `d` be the number of such nested activation chords excluding the maximal root `xy`. These `d` noncrossing diagonals dissect the polygon into `d+1` polygonal faces.

## 3. Triangle-free dissection count

Every edge of every dissection face is a unit segment: it is either an old boundary contact, the maximal new chord, or a nested new contact.

If one dissection face were triangular, its three vertices would be pairwise joined by unit segments. They would form a unit equilateral triangle, forbidden in the hypothetical survivor.

Hence every face has degree at least four.

Sum face degrees. Boundary polygon edges are counted once and internal diagonals twice, so

`N+2d >= 4(d+1)`.

Thus

`d <= (N-4)/2=(r-3)/2`.

The total number `a_r` of simultaneous activation chords in this maximal family, including the root chord itself, satisfies

### Lemma C101.1 — triangle-free activation sparsity

`boxed: a_r <= 1+floor((r-3)/2)=floor((r-1)/2).`

In particular

`a_r <= (r-1)/2`.

This is sharp at the purely planar level for quadrangulations of even-sided unit-edge polygons; no claim is made that every such combinatorial quadrangulation has a compatible unit-separated geometric realization.

## 4. Shell-area charge

C95 / Oler-shell (21.11) gives for each maximal triangle-free activation subpocket

`area(C_i) >= c_0(r_i-1)`.

The maximal subpockets are interior-disjoint and all lie in the pre-existing shell defect region of total area

`G=area(K)-area(R)`.

Therefore

`G >= sum_i area(C_i) >= c_0 sum_i(r_i-1)`.

By Lemma C101.1 the total number of simultaneous new unit-contact equations is at most

`sum_i floor((r_i-1)/2) <= (1/2)sum_i(r_i-1)`.

The Jacobian rank of a family of scalar equations is at most its cardinality. Hence:

### Theorem C101 — activation-rank versus shell area

For any simultaneous triangle-free first-contact family appearing from a pure-rhombic disk,

`boxed: rank_train(activation family) <= G/(2c_0) = (2/sqrt(3))G.`

Equivalently, if simultaneous triangle-free new unit contacts are to eliminate `k` independent train-angle directions, then necessarily

`boxed: G >= 2c_0 k = (sqrt(3)/2)k.`

This factor two is forced by the absence of triangular cells in the noncrossing unit-chord dissection. It is stronger than the earlier support/rotation estimate `rank<=G/c_0`.

## 5. C94 numerical consequence

In C94's low-train phase the exact active-face tangent flat has dimension at least

`k >= (pi/sqrt(3)-1-o(1))D`

`=(0.8137993642...-o(1))D`.

If a first boundary event were to block that flat using triangle-free new unit contacts alone, C101 would force

`G/D >= (sqrt(3)/2)(pi/sqrt(3)-1)-o(1)`

`=(pi-sqrt(3))/2-o(1)`

`=0.704770...-o(1)`.

Thus the old nesting loophole has been replaced by a much stronger linear shell requirement.

## 6. What remains

C101 closes the **nested-contact rank** loophole quantitatively. It does not yet close Level I because a continuation can also be blocked by new diameter equalities, and a mixed contact/diameter boundary can share the burden.

C102 combines this theorem with the diameter-graph edge budget. Any further improvement can come from either a sharper bound on newly activated diameter rank or an upper bound on the shell defect available in the same low-train chain-face phase.
