> Generated reading edition · [exact source](../../../docs/reports/target_c_cumulative_activation_dissection_2026-09-05.md) · source SHA-256 `ad566abd4dd389a2300b703c30111d6947f3f300266529192bf9dd8d0bbd6264`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2072179EE533","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: cumulative activation dissection

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-adjacent-cut-transition-2026-09-05`  
**Status:** LEVEL I STILL OPEN

## 1. Purpose

Main commit `7911d4b5` proves an additive `sqrt(3)/2` shell-area charge for **simultaneous** new unit contacts inside the C95 outer indentation pockets. The same dissection argument does not actually require simultaneous activation.

What matters is coexistence: if previously activated contacts are retained as exact unit contacts, then at any later triangle-free realization the entire accumulated family is a noncrossing chord family in the current indentation pockets of the preserved original pure-rhombic disk.

This removes the time-order/nesting loophole for any monotone exact-active continuation.

## 2. Static cumulative theorem

Fix a pure unit-rhombic contact disk `R` on a unit-separated source `A`, and let `K=conv(A)`. Assume the source is triangle-free.

Let `N` be **any** set of additional source pairs of distance exactly one, disjoint from the original rhombic-disk contact edges. No assumption is made about when the pairs in `N` became unit.

### Theorem CA1 — cumulative outer-contact charge

Every edge of `N` lies in the outer face of the preserved rhombic disk. Inside each current convex indentation pocket, the edges of `N` form a noncrossing chord family. If `M=|N|`, then

`area(K)-area(R) >= M sqrt(3)/2`.               (CA1)

Equivalently,

`M <= 2[area(K)-area(R)]/sqrt(3)`.              (CA2)

### Proof

Take `xy in N`.

A straight unit segment between unit-separated source points cannot cross an original unit-contact edge, and cannot pass through a third source point. Therefore its relative interior lies in one face of the original rhombic contact graph.

If that face were a bounded rhombus, `xy` would be one of its diagonals. A unit rhombus diagonal together with either adjacent unit side pair gives a unit equilateral triangle, contrary to the hypothesis. Hence every `xy in N` lies in the original graph's outer face.

Since `xy subset K`, the C95 convexification argument places it inside one of the current convex indentation pockets between the preserved outer unit-edge chain and the current hull chord.

Any two edges of `N` are unit segments in the same unit-separated source, so their relative interiors cannot cross. Thus, in each pocket, the whole family is a noncrossing chord family.

Now apply the chord-dissection proof of main commit `7911d4b5` to the entire family in that pocket. If a pocket contains `M_C` additional unit chords, they dissect it into `M_C+1` convex cells. Exactly one cell is incident with the hull chord. Every other cell is bounded only by original unit edges and chords from `N`, hence is a convex equilateral polygon. Triangle-freeness forces at least four sides, and Oler (21.10) gives area at least `sqrt(3)/2` for each such cell.

The `M_C` charged cells have disjoint interiors. Summing inside the pocket gives at least `M_C sqrt(3)/2`; summing over the disjoint indentation pockets gives (CA1). QED.

## 3. Consequence for a sequential exact-active continuation

Suppose a continuation starts from the C94 pure-rhombic chain face and satisfies all of the following until some time `t`:

1. every original rhombic-disk unit contact remains exactly unit;
2. every new unit contact activated earlier is thereafter imposed as an exact equality;
3. the source remains unit-separated, has diameter `D`, and remains triangle-free.

At time `t`, let `M(t)` be the number of accumulated new unit contacts. CA1 applies to the current realization, regardless of the activation times:

`G(t):=area(K(t))-area(R(t)) >= M(t) sqrt(3)/2`. (CA3)

Thus sequential nesting is not free. The cumulative family is charged exactly as if all of its chords had appeared simultaneously.

The remaining issue in the activation route is therefore **not** temporal disjointness. It is whether one can continue inside successively lower-dimensional exact-active strata while preserving all newly activated contacts, and whether the available shell capacity is small enough relative to the original tangent-flat dimension.

## 4. Universal pure-rhombic numerical cap

There is a simple finite cap on the size of a cumulative family, although it is not yet strong enough to close Target C.

Let `T` be the number of train tracks of the preserved pure rhombic disk. Its outer boundary has `2T` unit edges, and Euler gives the number of rhombi

`F=n-T-1`.

Every strict triangle-free unit rhombus has area strictly greater than

`a_0=sqrt(3)/2`.

Hence

`area(R)>a_0(n-T-1)`.

For a global minimum-diameter source, the standard strict comparison with the asymptotic hexagonal construction gives

`D^2 < (2sqrt(3)/pi)n`

in the canonical sufficiently-large regime. By the isodiametric inequality,

`area(K)<=pi D^2/4 < a_0 n`.

Therefore

`G=area(K)-area(R) < a_0(T+1)`.

Combining with CA2 yields

### Corollary CA2 — cumulative-contact cap

`M < T+1`.                                      (CA4)

This cap is exact at the coefficient level available from bare area and is too weak by itself: at the current `T/D=2.9346` threshold it allows about `2.9346D` cumulative contacts, whereas C94's exact tangent flat has dimension only about `0.8792D` after the current endpoint bound is inserted.

So a rank argument cannot close the problem using CA4 alone.

## 5. Interaction with new diameter activations

The common-cut C96/C97 endpoint saturation gives much less room for **new diameter** edges than for new contacts. If

`q=2D+2+s`,

then the selected common-cut family already contains `2D+1` diameter edges, while Hopf--Pannwitz gives at most `q` source diameter edges in total. Therefore the total number of diameter edges outside the selected family is at most

`q-(2D+1)=s+1`.

At the repaired `T/D=2.9346` threshold, C82 gives

`s/D <= 0.0554006358...+o(1)`,

so only about `0.055401D` off-selected diameter edges are available.

This makes diameter events scarce, but CA4 shows that harmless contact events still have enough raw capacity to absorb the current tangent dimension. A closing activation theorem must therefore improve the **contact** charge beyond bare pocket area, or prove that most successive contact equalities are not independent on the C94 train-angle flat.

## 6. Frontier

The activation route is now reduced to a sharper question:

> Along a triangle-free monotone exact-active continuation, can `Omega(D)` linearly independent new unit-contact equalities accumulate while all original rhombi remain strict and while only `O((q-2D))` new diameter equalities are available?

The cumulative dissection gives a fixed geometric resource for such a continuation, but the bare resource bound `M<T+1` does not yet beat the tangent-flat dimension.