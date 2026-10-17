> Generated reading edition · [exact source](../../research/target_c_global_support_reflection_blockers_2026-09-15.md) · source SHA-256 `81ca9df47b243e510e13ad8b397f754bf8ea8a109f2634ce8629188e4d495611`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6ca5b401c636b0987573adacb1838a67cff5b3ee", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_global_support_reflection_blockers_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7b3dd04462a921af0fe4668727d38c18dc0c5dabcab97e07ff0eb9a664cf3729"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — global support-line reflection blockers for every internal outer-route vertex

**Date:** 2026-09-15  
**Status:** proved proof-only source-level reduction; theorem-state authority unchanged  
**Scope:** fully force-visible no-container/full-core Type-II branch; the finite reflection lemma itself needs only the canonical post-ZF support/trapping facts  
**LEVEL I STATUS:** `STILL OPEN`

The shallow-tooth reflection theorem reflects a two-edge tooth apex across its loaded
base. The loaded-base hypothesis is useful for the later quantitative blocker cone,
but it is not needed for the basic source-level reflection alternative.

Canonical Section 67 gives something stronger for every distinguished Section-63
route. Its endpoints are consecutive loaded force-hull vertices and their chord is a
support side of the convex force hull `F`. Every internal route vertex lies strictly
inside `F`. Reflecting **one arbitrary internal route vertex** across that support line
therefore moves it outward while every positive-core point stays on the opposite side.
The elementary reflection identity shows that every old positive contact incident to
the reflected vertex is preserved or lengthened, and at least one is lengthened
strictly.

Consequently every internal outer-route occurrence has an exact finite alternative:

$$
\boxed{
\text{diameter blocker}
\quad\text{or}\quad
\text{exterior contact-isolated reflection witness}.}
$$

No straightness, two-edge tooth, rhombus, phase, KKT coefficient floor, or asymptotic
counting is used in the reflection lemma.

---

## 1. Canonical support geometry

Let

$$
W_i:b_i\leadsto b_{i+1}
$$

be one distinguished Section-63 outer route between consecutive loaded force-hull
vertices. Let `L_i` be the supporting line through the loaded hull side
`[b_i,b_{i+1}]`.

Choose coordinates with

$$
L_i=\{(p,q):q=0\}
$$

and the force hull in

$$
F\subset\{q\ge0\}.
\tag{SR.1}
$$

Canonical Section 67 proves

$$
V(G)\cap\partial F=B,
\tag{SR.2}
$$

where `G` is the positive-contact core and `B=Vert(F)` is the loaded set. Therefore
every physical internal route vertex `x` is unloaded and lies in `int(F)`.

Write

$$
x=(p,h),\qquad h>0.
\tag{SR.3}
$$

and reflect it across `L_i`:

$$
x^-=(p,-h).
\tag{SR.4}
$$

All other source points remain fixed.

---

## 2. Exact reflection identity

For any source point

$$
y=(r,q),
$$

direct expansion gives

$$
\boxed{
|y-x^-|^2-|y-x|^2=4hq.
}
\tag{SR.5}
$$

Thus reflection cannot decrease the distance from `x` to any source point in the
closed inward half-plane `q>=0`, and it strictly increases the distance to every point
with `q>0`.

Every vertex of the positive-contact core lies in `F`. Indeed every unloaded component
is harmonically trapped in the convex hull of its loaded attachment set, hence in
`F`, while every loaded vertex is itself in `F`. Therefore every old positive-contact
neighbor of `x` has `q>=0`.

At least one old unit contact is strictly broken. There are two cases.

1. If one of the two route neighbors of `x` is an internal route vertex, that neighbor
   belongs to `V(G)\setminus B` and therefore has positive height by (SR.2).
2. If both route neighbors lie on `L_i`, then `W_i` is the two-edge route
   `b_i-x-b_{i+1}`. Canonical C26 gives `deg_C(x)>=3`. A third contact neighbor cannot
   be another loaded vertex on `L_i`, because `b_i,b_{i+1}` are consecutive extreme
   vertices of `F`; nor can it be an unloaded vertex on `partial F` by (SR.2). Hence
   that third neighbor has positive height.

So the reflection always removes at least one old actual unit contact from the
canonical positive contact graph.

---

## 3. Lower blockers lie strictly outside the force hull

Call a source point `z` a **strict lower blocker** for this reflection if

$$
|z-x^-|<1.
\tag{SR.6}
$$

The original source is unit-separated, so

$$
|z-x|\ge1.
$$

Equation (SR.5) then rules out `q_z>=0`. Therefore

$$
\boxed{q_z<0.}
\tag{SR.7}
$$

Since the force hull is contained in `q>=0`, every strict lower blocker lies outside
`F`.

Canonical Section 56 says every actual source point outside `F` is contact-isolated in
the contact-minimal representative. Thus every strict lower blocker is an actual
contact-isolated source point.

---

## 4. If the reflected configuration is feasible, contact minimality forces an exterior witness

Suppose there is no strict lower blocker and no source point at distance greater than
`D` from `x^-`. Replacing `x` by `x^-` then gives another unit-separated `n`-point
configuration of diameter at most `D`.

If its diameter were strictly below `D`, global diameter minimality would already be
contradicted. Otherwise it is another diameter minimizer.

The reflection strictly breaks at least one old unit contact by Section 2. The
canonical representative was chosen contact-minimal among diameter minimizers.
Therefore the reflected configuration cannot have strictly fewer actual unit contacts.
It must acquire at least one new unit contact

$$
|z-x^-|=1
\tag{SR.8}
$$

from a source point that was not an old contact neighbor of `x`.

For any point with `q_z>=0`, (SR.5) gives

$$
|z-x^-|\ge|z-x|.
$$

Since an old noncontact has `|z-x|>1`, it cannot become a new unit contact. Hence every
new contact forced by contact minimality satisfies

$$
q_z<0.
$$

It lies outside `F` and is contact-isolated in the original source.

We call either a strict lower blocker (SR.6) or an exact new contact (SR.8) an
**exterior reflection witness**. In both cases

$$
\boxed{
z\notin F,
\qquad z\text{ is contact-isolated in the original canonical source},
\qquad |z-x^-|\le1.
}
\tag{SR.9}

---

## 5. Diameter blockers

Call a source point `y` an **upper/diameter blocker** if

\[
|y-x^-|>D.
\tag{SR.10}
$$

The original diameter constraint gives `|y-x|<=D`. Equation (SR.5) therefore implies

$$
4h q_y
=|y-x^-|^2-|y-x|^2
>0,
$$

so

$$
\boxed{q_y>0.}
\tag{SR.11}

Thus a diameter blocker lies on the inward side of the same loaded support line.

The reflection displacement is exactly `2h`, so triangle inequality also gives

\[
\boxed{
|x-y|>D-2h.
}
\tag{SR.12}

Unlike the two-edge shallow-tooth theorem, no uniform normal cone is asserted here:
an arbitrary internal route vertex need not project to the midpoint of the loaded
side, and its support depth `h` need not be `O(1)`.

---

## 6. Global finite reflection alternative

Combining the preceding sections gives the main statement.

### Theorem SR.1 — support-line reflection blocker theorem

For every internal physical occurrence `x` of every distinguished Section-63 route
`W_i`, reflect `x` across the supporting line of the corresponding consecutive loaded
force-hull side. Then at least one of the following holds:

1. **diameter blocker:** there exists a source point `y` with
   \[
   |y-x^-|>D,
   \qquad q_y>0,
   \qquad |x-y|>D-2h;
   $$
2. **exterior-isolate witness:** there exists a source point `z` with
   $$
   q_z<0,
   \qquad |z-x^-|\le1,
   $$
   and `z` is contact-isolated in the original canonical source.

The theorem is finite and source-preserving. It uses the canonical contact-minimal
tie-break only in the subcase where the reflected point is otherwise feasible and the
diameter remains exactly `D`.

---

## 7. Composition with the current convex straight-event population

The theorem applies to every internal route vertex, so in particular it applies to the
near-30-degree distinct straight-tail family from the current branch. That family has

\[
\boxed{
1.2558820685257019\ldots D-o(D)
}
\tag{SR.13}

distinct physical tails.

Therefore at least that many distinct tail vertices carry a support-line reflection
obstruction of one of the two types in Theorem SR.1.

This is an **incidence** count, not yet a distinct-blocker count. A single exterior
isolate or diameter blocker may in principle witness multiple route tails. The old
shallow-tooth perimeter proof obtained injectivity and a fixed cap-perimeter cost from
the special two-edge geometry; those properties are not silently imported here.

---

## 8. Frontier effect

The support-line theorem removes one conceptual restriction from the reflection route:
reflection is not a tooth-only mechanism. Every internal positive outer-route vertex
can be pushed through its associated loaded support line while all positive-core unit
constraints move in the safe direction.

The remaining quantitative problem is now explicit:

- **exterior branch:** control reuse of a contact-isolated source point across convex
  route reflections, or extract a source-hull perimeter/cap cost from a large family of
  such witnesses;
- **diameter branch:** turn the pairs in (SR.12) into a normal-aligned or bounded-reuse
  near-diameter family, using route depth/convex-pocket geometry.

A useful continuation should exploit the newly proved convexity of every Section-63
pocket chain. It should not assume the two-edge tooth foot-interiority lemma for a
longer route.

**C-II remains open.**
