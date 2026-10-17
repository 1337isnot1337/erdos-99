> Generated reading edition · [exact source](../../../docs/reports/target_c_shell_contact_capacity_2026-09-05.md) · source SHA-256 `db33ffec05830e5ba9acfe599e79425291cd2c065c8a358d1ef35a638a1cd872`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E2D3D51EAA28","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C103: finite shell-contact capacity

**Date:** 2026-09-05  
**Repository base:** C102 branch after `0c5b582e`  
**Status:** LEVEL I STILL OPEN  
**Depends on:** C77 `B=2T`, Target B perimeter saturation (24.2), C92 train-surplus floor, C95 outer-pocket localization, C101 triangle-free chord-dissection count

C101 bounds the rank of one simultaneous triangle-free activation family by shell area. There is a second, purely metric capacity bound that applies to the **entire collection** of new triangle-free unit contacts that can ever be created while all original pure-rhombic contacts are retained. It uses only the original indentation-pocket boundary excess `B-P`.

The key observation is elementary: replacing a disjoint old boundary subchain of length `r` by a new unit chord shortens that boundary path by exactly `r-1`, and the resulting path must still be at least as long as the convex-hull chord joining its endpoints.

## 1. Fix the original pure-rhombic disk

Let the original strict-rhombic contact disk have outer unit-edge boundary length `B` and convex-hull perimeter `P`.

Partition the original shell into the convex indentation pockets between consecutive convex-hull vertices. For one such pocket, write

- `R` for the number of old unit edges on its boundary chain;
- `L` for the length of its convex-hull closing chord.

Then

`sum R = B`,

`sum L = P`.

C77 gives exactly

`B=2T`.

## 2. Every later triangle-free new contact stays in an original pocket

Suppose a finite deformation or sequence of deformations preserves every original unit contact and remains unit-separated and triangle-free.

Any newly created unit segment cannot cross an original unit-contact edge and cannot pass through an original source vertex, by the C95 crossing argument. Therefore its relative interior lies in one face of the **original** contact graph.

If it lay in an original bounded face, that face is one strict unit rhombus. A new unit diagonal would immediately create a unit equilateral triangle. Hence every triangle-free new unit contact lies in one of the original outer indentation pockets.

All such new unit segments are pairwise noncrossing, regardless of when they activate, because any two unit segments in a unit-separated source cannot cross properly.

Thus the full eventual set of added triangle-free contacts in each original pocket is one noncrossing chord family on the original boundary vertices.

## 3. Maximal chords and the boundary-shortening inequality

Fix one original pocket. Take the maximal added chords with respect to containment of their old-boundary intervals. Their intervals are pairwise interior-disjoint.

Let their old boundary lengths be

`r_1,...,r_t`.

Each maximal chord has length one. Replace every corresponding old subchain by that unit chord. The resulting polygonal path still joins the two convex-hull vertices of the original pocket. Its length is

`R-sum_i r_i+t`

`=R-sum_i(r_i-1)`.

By the triangle inequality, every path between those two hull vertices has length at least their Euclidean distance `L`. Therefore

`R-sum_i(r_i-1) >= L`.

Hence

### Lemma C103.1 — pocket shortening budget

`boxed: sum_i(r_i-1) <= R-L.`

Summing over all original indentation pockets gives

### Theorem C103.2 — global shortening budget

`boxed: sum_maximal (r_i-1) <= B-P.`

This is exact and finite; no asymptotic argument or area estimate is used.

## 4. Convert shortening to total contact count

Under one maximal chord with old boundary length `r_i`, all added triangle-free unit contacts nested beneath it form a noncrossing dissection of the convex unit-edge polygon bounded by the old `r_i`-edge subchain plus the maximal unit chord.

C101 proves that a triangle-free dissection of this polygon contains at most

`floor((r_i-1)/2)`

added unit chords total, including the maximal root.

Therefore the **entire eventual set** of added triangle-free unit contacts, across arbitrary sequential activation times, has cardinality

`N_C <= sum_i floor((r_i-1)/2)`

`<= (1/2)sum_i(r_i-1)`

`<= (B-P)/2`.

Thus:

### Theorem C103 — finite shell-contact capacity

While preserving all original contacts of a pure-rhombic disk, any triangle-free global-minimizer continuation can create at most

`boxed: N_C <= (B-P)/2`

new unit-contact pairs in total.

The total Jacobian rank of all such new contact equalities is also at most `(B-P)/2`.

Using C77 `B=2T`,

`N_C <= T-P/2`.

Target B (24.2) gives for every global minimizer

`0<=pi D-P<pi sqrt(3)/2`.

Therefore:

### Corollary C103.3 — asymptotic contact-capacity coefficient

If `x=T/D`, then

`boxed: N_C/D <= x-pi/2+o(1).}`

The error is actually `O(1/D)` from the explicit perimeter deficit.

## 5. Comparison with the old flat: useful algebra but no live-range closure

C102 bounds the total number of newly available diameter equalities in the same low-train chain-face phase by

`N_D/D <= 2x-4-2Delta_2+o(1)`.

Hence the total **cardinality** of all harmless new active rows that can be accumulated while preserving the original pure-rhombic contacts is at most

`(3x-4-2Delta_2-pi/2+o(1))D`.

C94's original tangent space has dimension at least

`(2+2Delta_2-x-o(1))D`.

The formal cardinality separation

`2+2Delta_2-x > 3x-4-2Delta_2-pi/2`

is equivalent to

`x < (6+4Delta_2+pi/2)/4`

`=2.7995987638...`.

However C91/C92 already force every currently surviving chain-face sequence to satisfy

`x >= 2+Delta_2+10^(-4)`

`=2.9069996821...`.

Therefore the raw C103 cardinality-vs-C94 dimension comparison is **vacuous on the current live range**. C103 remains a genuine finite structural theorem, but it does not remove a surviving asymptotic phase by itself.

There is a second, independent obstruction to using the count naively: C94 only supplies a linear subspace in the tangent cone and integrates each vector direction-by-direction. It does not produce one common smooth `k`-manifold that can be followed until all possible boundary equations are encountered. Even if the numerical ranges overlapped, a separate continuation theorem would still be required.

## 6. Frontier

C103 replaces the old shell-nesting ambiguity by an exact perimeter capacity:

`N_C <= (B-P)/2`.

For the actual live interval

`2.9069996821... <= T/D < 3`,

this contact capacity is still too large to close C94 after the current diameter budget is included. The next useful gain must therefore come from at least one of:

1. a substantially sharper bound on **new diameter rank** than raw Hopf--Pannwitz edge slack;
2. a contact-capacity theorem using more than perimeter/noncrossing planarity;
3. a direct geometric contradiction from the C98--C100 paired diameter structure; or
4. a separate argument that eliminates the narrow high end of the low-train phase.

The most promising of these is (1), because the old diameter graph is already a near-spanning straight-line thrackle with highly ordered common-cut structure.
