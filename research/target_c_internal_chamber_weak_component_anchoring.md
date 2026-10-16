# Target C — maximal weak-contact components in an internal chamber must anchor to the old core

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only structural reduction for the macroscopic internal-chamber branch.
**Dependencies:** canonical Sections 57, 67, 77 plus elementary rigid-motion genericity.

The contact-saturation theorem shows that the quadratic actual-isolate population of a canonical inactive chamber can be turned into exact unit contacts while preserving the old diameter graph and the entire normalized KKT polytope. This note adds a second normalization inside a **bounded internal inactive chamber**: maximize the number of triangle-free weak contacts while keeping the old positive core fixed.

In that normalization, no weak contact component can float freely in the interior. Every weak component must attach to a boundary vertex of the old positive-contact face. Convexity and triangle-freeness then permit at most one weak attachment edge at each boundary vertex.

Consequently a macroscopic internal chamber with `Omega(D^2)` inactive points and `O(D)` boundary has, after weak-contact maximization, at least one core-anchored weak component containing `Omega(D)` former isolates.

This does not close the chamber branch. It replaces a diffuse rattler picture by a large exact weak-contact component coupled to the fixed old core.

---

## 1. Fixed internal-chamber class

Start from the canonical contact-minimal, then diameter-pair-minimal post-ZF C-II representative `A`. Let `G` be its connected positive-contact core and let

\[
C
\]

be one bounded nonquadrilateral contact face of `G`. Canonical Section 67 proves that `C` is a convex polygon whose boundary sides are unit contact edges of `G`.

Let

\[
Z_C:=A\cap\operatorname{int}C
\]

be the actual contact-isolated source points assigned to this internal chamber. Put `z=|Z_C|`.

Keep every source point of `A\setminus Z_C` fixed. Consider all configurations obtained by moving only the `z` labeled chamber points subject to

1. every moved point remains in `C`;
2. the full source remains unit-separated;
3. the full source remains triangle-free.

The original canonical source is one member of this class, so the class is nonempty.

Every fixed old diameter edge remains present. Conversely every moved point lies in the old convex hull `K=conv(A)`, so no pair distance can exceed `D`. Hence every admissible configuration in this class is automatically another global minimizer of diameter exactly `D`.

Among the attained integer values of the number of unit contacts, choose an admissible configuration `A^max_C` with the maximum value. Such a maximum exists because the set of attained contact counts is a nonempty subset of

\[
\{0,1,\ldots,\tbinom n2\}.
\]

No compactness assertion for the triangle-free subspace is needed.

The fixed old positive core remains in place throughout this normalization. Newly created chamber contacts may be KKT-weak; no force-transfer claim is made.

---

## 2. A floating chamber component can be translated to a new contact

Let `W` be a connected component of the actual unit-contact graph of `A^max_C` which

- contains at least one moved chamber point; and
- contains no fixed old-core vertex.

Since `W` is a full contact-graph component, every distance between a vertex of `W` and a source point outside `W` is strictly greater than one.

### Lemma 2.1 — rigid translation creates a cross-contact before escape

There is an admissible rigid motion of all vertices of `W`, preserving every internal distance of `W`, which ends at a configuration with at least one new unit contact between `W` and its complement and no distance below one.

Moreover the motion can be chosen so that exactly one cross-contact is created at the first-contact time.

### Proof

All vertices of `W` lie in `C`. Since no vertex of `W` is a fixed boundary/core vertex, unit separation from the unit edges of `partial C` puts every vertex of `W` in `int C`.

First apply, if needed, an arbitrarily small generic rigid rotation/translation of `W` inside `int C`. Cross-component distances are all strictly greater than one, so a sufficiently small perturbation preserves unit separation and triangle-freeness. This preliminary genericity can be chosen to remove persistent coincidences among the finitely many prospective cross-contact events.

Now choose a generic translation direction `v` and move the whole finite set `W` by `tv`, increasing `t` from zero. Internal distances and therefore all internal unit contacts are preserved exactly.

Stop at the earlier of

1. the first time some distance between `W+tv` and a source point outside `W` becomes one; or
2. the first time some vertex of `W+tv` reaches `partial C`.

The second event cannot occur strictly before the first. Indeed every side of `partial C` is a unit segment `ab` between fixed old-core vertices. If a moving point approaches an interior point of that side, its distance to at least one of `a,b` becomes `<1` before it reaches the side. If it approaches a boundary vertex, its distance to that vertex tends to zero. By continuity a unit cross-distance is therefore reached first.

Thus a cross-contact occurs while all moving points still lie in `C`. By choosing the rigid-motion path generically in the three-dimensional planar rigid-motion group, the first active cross-contact can be made unique: simultaneous equalities are intersections of two distinct codimension-one contact hypersurfaces and are avoided by a generic one-dimensional path. Internal rigid symmetries were removed by the preliminary perturbation.

Before the first-contact time every cross-distance is `>1`; at the stopping time all are `>=1`. The moved points remain in `C subset K`, so the full diameter is at most `D`, while the unchanged old diameter graph still realizes `D`. Hence the resulting source is admissible and remains a global minimizer. `square`

### Lemma 2.2 — the unique new cross-edge cannot create a triangle

At the stopping configuration of Lemma 2.1, the full source remains triangle-free.

### Proof

Only one new contact edge `xy` is created, with `x in W` and `y notin W`. If a new contact triangle used `xy`, its third vertex `z` would give an old contact path

\[
x-z-y
\]

of length two from `W` to its complement. At least one of those two old edges would already cross the component cut, contradicting that `W` was a connected component of the old actual contact graph. Triangles not using `xy` are unchanged. `square`

Lemmas 2.1--2.2 add one unit contact without deleting any internal contact and remain inside the maximizing class. This contradicts contact maximality.

Therefore:

### Theorem 2.3 — no floating weak component

Every actual contact-graph component of `A^max_C` that contains a moved chamber point also contains an old fixed core vertex.

### Lemma 2.4 — any chamber-to-core contact lands on `partial C`

If a moved point `x in int C` is in unit contact with a fixed old-core vertex `y`, then `y` is a boundary vertex of `C`.

### Proof

The straight-line unit-contact graph of any unit-separated planar source is plane. Indeed, if two distinct unit segments crossed properly, choose on each segment an endpoint no farther than `1/2` from the crossing point. The two chosen endpoints would then be at distance strictly less than one.

If `y` were not a boundary vertex of the face `C`, the segment `xy` would have to leave the face. Since `x` is in its interior, it would either cross a boundary contact edge properly or pass through a boundary vertex before reaching `y`. The first alternative contradicts planarity. In the second, the intermediate boundary vertex lies strictly inside the unit segment `xy` and is therefore at distance less than one from `x`, contradicting unit separation. `square`

Combining Theorem 2.3 with Lemma 2.4 gives the form used below:

\[
\boxed{
\text{after deleting the old core, every weak chamber component has at least one unit-contact edge to a vertex of }\partial C.
}
\tag{2.1}
\]

---

## 3. One boundary vertex can support at most one weak chamber attachment

Let `b` be a boundary vertex of the convex unit-edge polygon `C`. Its two neighboring boundary vertices `b_-` and `b_+` both satisfy

\[
|b-b_-|=|b-b_+|=1.
\]

Let the interior angle of `C` at `b` be `phi<=pi`.

In a triangle-free unit-separated source, any two distinct unit neighbors of the same vertex subtend an angle strictly greater than `pi/3`: if the angle were at most `pi/3`, their mutual distance would be at most one, with equality at `pi/3`; strict separation or equality would respectively fail or create a unit equilateral triangle.

Suppose `b` had `m` additional unit-contact neighbors lying in the chamber sector between the rays `bb_-` and `bb_+`. Ordering all `m+2` neighbor rays inside that sector gives `m+1` consecutive angular gaps, each strictly greater than `pi/3`. Therefore

\[
\phi>(m+1){\pi\over3}.
\tag{3.1}
\]

Since `phi<=pi`, (3.1) implies

\[
\boxed{m\le1.}
\tag{3.2}
\]

Thus:

### Theorem 3.1 — boundary attachment capacity one

Each boundary vertex of an internal convex contact face supports at most one additional unit-contact edge into the chamber in any triangle-free source.

No planarity estimate is used; this is the exact `60`-degree neighbor-angle rule plus convexity.

---

## 4. Macroscopic consequence

Let the internal face have `p` boundary edges/vertices. Since every side is a unit contact,

\[
p=\operatorname{per}(C).
\tag{4.1}
\]

Delete the fixed old-core vertices from the actual contact graph of `A^max_C`, and let

\[
W_1,\ldots,W_s
\]

be the weak components containing the `z` moved chamber points.

Equation (2.1) gives each `W_i` at least one boundary attachment edge. Theorem 3.1 says distinct attachment edges use distinct boundary vertices. Hence

\[
\boxed{s\le p.}
\tag{4.2}
\]

Since the `W_i` partition the `z` chamber points,

\[
\boxed{
\max_i |W_i|
\ge {z\over p}.
}
\tag{4.3}
\]

For a canonical macroscopic internal chamber, Sections 77 and 79 give

\[
z=\Omega(D^2),
\qquad
p=O(D).
\]

Therefore the contact-maximized weak representation contains a boundary-anchored weak component with

\[
\boxed{|W_i|=\Omega(D).}
\tag{4.4}
\]

This component is an exact unit-contact object, not a near-contact graph, while the old diameter-carrying core has not moved.

---

## 5. What this does and does not prove

The theorem eliminates one possible interpretation of the inactive branch:

```text
quadratically many chamber points
+ after contact saturation they remain a diffuse collection of floating weak pieces.
```

After maximizing triangle-free weak contacts inside an internal convex contact face, every weak piece is anchored to the old core, and one anchored weak component is linearly large.

It does **not** prove that

- the weak attachment edge has positive KKT weight;
- the large weak component has quadratic size;
- the weak component contains a cycle;
- the large weak component forces a unit triangle; or
- the internal-chamber branch is closed.

The contact-saturation/KKT-invisibility theorem warns that tree-like weak attachments can remain invisible to first-order stress. The weak-forest density regression warns that leading packing density alone does not eliminate them.

The next useful theorem on this route would have to exploit the large anchored weak component together with contact maximality, for example by ruling out a long bridge/tree decomposition through finite rigid motions, or by proving that a contact-maximal anchored component contains enough cycles to couple back to the old positive core.

---

## 6. Hostile checks

- **Full source retained:** only chamber points move; no point is deleted or duplicated.
- **Global diameter:** all moved points stay in the old convex hull, so diameter never exceeds `D`; unchanged old diameter pairs keep the diameter equal to `D`.
- **First-contact uniqueness:** generic rigid-motion paths avoid simultaneous cross-contact hypersurfaces. The proof does not assume that a predetermined straight translation is generic.
- **Triangle-freeness at the new edge:** disconnectedness of `W` in the full actual contact graph excludes an old two-edge path across the cut.
- **Boundary escape:** every bounded internal face side is an old unit contact edge. Reaching that side without an earlier unit cross-contact is impossible.
- **Core attachment localization:** planarity of the unit-contact graph forces every chamber-to-core unit edge to end at a face-boundary vertex.
- **Convex angle may equal `pi`:** (3.1) is strict, so `phi<=pi` still gives `m<=1`.
- **KKT scope:** no affine-kernel theorem is extended to moved points and no new contact is asserted positive.
- **Exterior caps:** not covered. A convex outer pocket has a noncontact hull chord, so the boundary-escape argument can fail across that chord. This theorem applies only to genuine bounded internal contact faces.

**Disposition:** proof-only inactive-branch structural reduction. C-II remains open.
