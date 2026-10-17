> Generated reading edition · [exact source](../../../docs/reports/target_c_contact_activation_pockets_2026-09-01.md) · source SHA-256 `1cd7582744d276450fac6feccc598ed5e236d5a973c96a95c1ea0f6b7802a6c7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-54E8C067589A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C95: contact-activation pocket localization

**Date:** 2026-09-01  
**Repository base:** `3ee2bdf0` (main after C94 / PR #99)  
**Status:** LEVEL I STILL OPEN

C94 leaves a macroscopic exact active-face tangent flat in the low-train pure-rhombic
chain branch. The missing step is to understand what can stop a finite continuation of
such a motion before a 60-degree rhombus appears.

C95 localizes every harmless first unit-contact activation. A new unit segment cannot
cross an old unit-contact edge or pass through another source point. Hence it lies in
one face of the old contact graph. If that face is a bounded unit rhombus, the new
edge is a unit diagonal and immediately creates a unit equilateral triangle.

Therefore every **triangle-free** new unit contact must lie in the outer face. Since
the chord lies inside the convex hull, it closes a subpocket of one of the convex hull
indentation pockets from the Oler-shell decomposition. If its old boundary subchain has
`r` unit edges, triangle-freeness forces `r>=3`, and the convex-pocket Oler inequality
gives the quantitative charge

`area(pocket) >= c_0(r-1) >= 2c_0=sqrt(3)/2`.

Thus the activation-boundary loophole in C94 is entirely an **outer-pocket** loophole,
with a fixed area charge for each individually localized first contact.

---

## 1. Unit contact segments cannot cross

Let `ab` and `cd` be two unit segments in a unit-separated source, and suppose their
relative interiors cross at `o`. Choose the shorter endpoint piece on each segment:

`min(|a-o|,|b-o|)<=1/2`,

`min(|c-o|,|d-o|)<=1/2`.

Let the corresponding endpoints be `x in {a,b}` and `y in {c,d}`. Because the two
segments cross with distinct directions,

`|x-y| < |x-o|+|o-y| <=1`,

contradicting unit separation.

Hence two unit-contact segments have disjoint interiors unless they share an endpoint.
This argument applies equally to an old contact and a newly activated unit pair.

## 2. A new unit segment cannot pass through a third source point

Let `xy` be a new unit pair, `|x-y|=1`. If a third source point `v` lay in the
relative interior of the straight segment `xy`, then

`0<|x-v|<1`,

again contradicting unit separation.

Therefore the relative interior of a new unit segment meets neither an old contact
edge nor an old source vertex.

## 3. Face localization

The old unit-contact graph of a pure rhombic disk is a connected plane straight-line
graph with a simple outer boundary. Remove its embedded edges and vertices from the
plane. The relative interior of the connected segment `xy` cannot cross this embedded
graph, so it lies in one face. Its endpoints lie on the boundary of that same face.

If the face is bounded, it is one of the strict unit-rhombus faces. Since `xy` is new,
`x,y` are not adjacent boundary vertices. They are therefore the opposite vertices of
the rhombus.

### Theorem C95.1 — bounded-face activation forces a triangle

If a new unit contact first appears inside a bounded face of the old pure-rhombic
contact graph, then the source contains a unit equilateral triangle.

Indeed, one rhombus diagonal `xy` has length one, and either of the two boundary
vertices adjacent to both `x` and `y` has unit distance to each. Thus the three points
form a unit equilateral triangle.

Consequently, along a triangle-free deformation preserving all old unit contacts,
every first new unit contact lies in the old **outer face**.

## 4. Outer activations lie in one convex indentation pocket

Let `K` be the convex hull of the source and let `R` be the closed region covered by
the pure rhombic disk. The straight segment `xy` lies in `K` by convexity. Its relative
interior lies in the outer face, hence in `K\R`.

The Oler-shell decomposition partitions `K\R` into the convex indentation pockets
between consecutive convex-hull vertices. Each such pocket is bounded by one outer
unit-edge chain of the rhombic disk and the corresponding hull chord. Distinct pockets
have disjoint interiors.

Because the connected relative interior of `xy` is contained in `K\R`, it lies in one
such convex pocket `C`. Both endpoints are vertices on the unit-chain part of
`partial C`.

The chord `xy` divides `C` by a line segment between two of its boundary vertices.
The component adjacent to the intervening unit-edge subchain is the intersection of
`C` with one closed half-plane and is therefore convex. Call it `C_xy`.

If that old subchain has `r` unit edges, then `C_xy` is a convex pocket bounded by
those `r` unit edges and the new chord of length one.

## 5. Quantitative pocket charge

The pocket vertices are source points and hence unit-separated. Lemma 21.3 / equation
(21.11) in the Oler-shell module gives, for a convex pocket bounded by `r` unit edges
and a closing chord of length `L`,

`area(C_xy) >= c_0(r-L)`,

where

`c_0=sqrt(3)/4`.

Here `L=1`, so

`area(C_xy) >= c_0(r-1)`.

If `r=2`, the old two-edge chain plus the new unit chord is already a unit
equilateral triangle. Therefore a triangle-free activation has `r>=3` and

### Theorem C95 — triangle-free activation pocket charge

Every first new unit contact that appears along a triangle-free deformation of a pure
rhombic disk closes a convex outer subpocket satisfying

`area(C_xy) >= 2c_0 = sqrt(3)/2 = 0.8660254037...`.

This entire subpocket lies in the pre-existing shell area defect

`G=area(K)-area(R)`.

No assumption about the new contact being a hull edge is used.

## 6. Simultaneous activations

Several new unit pairs may activate at the same first parameter. Their straight unit
segments are pairwise noncrossing by Section 1, so they form an outerplanar chord
family inside the old indentation pockets. C95 gives the stated charge for each
individual chord's localized subpocket.

The subpockets can be nested, so their areas cannot be added without a new disjointness
or rank-selection theorem. C95 therefore does **not** yet turn C94's
`Omega(D)`-dimensional active flat into `Omega(D)` shell area.

## 7. Frontier effect

C94's finite-continuation obstruction is now sharply classified:

- a first bounded-face unit activation solves the problem immediately by creating a
  unit triangle;
- a triangle-free first unit activation must close a convex outer indentation
  subpocket and consumes at least `sqrt(3)/2` of already-existing shell area;
- a new diameter-pair activation remains the other harmless first-event type.

The next target is an **independent-pocket activation theorem**: extract
`Omega(D)` nonnested first-contact pockets, or prove that a lower-dimensional nested
pocket family cannot bound the `Omega(D)` exact active-face tangent flat from C94.
A second viable route is to combine repeated new-diameter events with the universal
`|H|<=q` cap until a contact activation is forced.