> Generated reading edition · [exact source](../../research/target_c_contact_saturation_no_isolates.md) · source SHA-256 `66e3742efb3238b5aa2c2491bf4f9b94c95d0e11739b7f7ad9e42c0257b1ef84`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — triangle-free minimizers admit a contact-saturated no-isolate representative

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proof-only research theorem.
**Dependencies:** Sections 1--3 use only global diameter minimality, convexity of the source hull, and finiteness. Section 4 additionally uses the canonical post-ZF fact that every actual diameter endpoint lies in the nonisolated positive-contact core.

The canonical C-II normalization minimizes unit contacts, because that is what makes every actual active contact strong. That normalization may contain contact-isolated source points, and the macroscopic-container branch exploits exactly that possibility.

There is a different legitimate normalization in the opposite direction. If any triangle-free global minimizer exists, then there also exists a triangle-free global minimizer of the same cardinality and diameter with **no actual contact-isolated source points**. More strongly, every contact-isolated point can be saturated one at a time while staying inside the old convex hull, preserving global diameter and triangle-freeness, and adding exactly one unit contact at each step.

For the canonical post-ZF source, the moves can also be chosen to create no new diameter pair. Then the old positive KKT core and diameter graph are literally unchanged. The new contacts form a forest, and leaf elimination shows that **every** normalized KKT stress of the saturated source assigns zero weight to every new forest edge. Thus the full normalized KKT polytope is unchanged after the obvious zero-extension/restriction identification.

A quadratic actual-isolate population can therefore be converted, at fixed global diameter and with the force system untouched, into a quadratic exact KKT-invisible unit-contact forest. This is a whole-population strengthening of the obstruction behind proof-only Section 95.

---

## 1. Generic first contact inside the old hull

Let `A` be a finite noncollinear unit-separated planar set and put

```math
K:=\operatorname{conv}A,
\qquad D:=\operatorname{diam}A=\operatorname{diam}K.
```

Fix `x\in A` such that

```math
|x-y|>1\qquad(y\in A\setminus\{x\}).
\tag{1.1}
```

For the unchanged source points put

```math
U:=\bigcup_{y\in A\setminus\{x\}} B(y,1),
```

where the disks are closed. By (1.1), `x\notin U`.

### Lemma 1.1 — one-contact hull motion

There is a point `x'\in K` and a segment path from `x` to `x'` contained in `K` such that

```math
|x'-y_0|=1
```

for exactly one `y_0\in A\setminus\{x\}`, while

```math
|x'-y|>1\qquad(y\ne x,y_0).
\tag{1.2}
```

Along the open path before `x'`, all distances to `A\setminus\{x\}` are strictly greater than one.

### Proof

Choose one unchanged source point `y`. Since `K` is two-dimensional, every sufficiently small neighborhood of `y` has a positive-area intersection with `K`. Hence there are points of

```math
K\cap\operatorname{int}B(y,1)
```

in a two-dimensional wedge of `K`; in particular `K\cap\operatorname{int}U` has positive area.

The set of points lying on two distinct unit-circle boundaries

```math
\partial B(y_i,1)\cap\partial B(y_j,1),\qquad i\ne j,
```

is finite: each pair contributes at most two points. Therefore the set of rays from `x` through any such multiple-circle point is finite.

Choose

```math
z\in K\cap\operatorname{int}U
```

so that the segment direction from `x` to `z` is not one of those finitely many exceptional ray directions. Convexity gives `[x,z]\subset K`.

Parameterize the segment by `p(t)=(1-t)x+tz`, `0\le t\le1`. Since `x\notin U` and `z\in\operatorname{int}U`, there is a first time

```math
t_*:=\min\{t:p(t)\in U\}\in(0,1).
```

Put `x'=p(t_*)`. By first entry, `x'\in\partial U`, every unchanged source point is at distance at least one from `x'`, and all those distances were strictly greater than one for `t<t_*`.

If two distinct source points were at distance one from `x'`, then `x'` would be one of the finitely many multiple-circle points. The segment ray would then be one of the excluded exceptional rays. Hence exactly one unit circle is met at `x'`, proving (1.2). `square`

The only role of noncollinearity is to make the choice of a generic target `z` immediate. Target C is already in the two-dimensional force-hull regime.

---

## 2. Saturating one contact-isolated point preserves global optimality

Assume now that `A` is a triangle-free **global** minimum-diameter source of cardinality `n`, so

```math
\operatorname{diam}A=D(n)=D.
```

Apply Lemma 1.1 to a contact-isolated point `x`, and set

```math
A':=(A\setminus\{x\})\cup\{x'\}.
```

All unchanged pair distances remain at least one. Lemma 1.1 gives the same for pairs involving `x'`, with exactly one new unit contact. Thus `A'` is unit-separated.

Because `x'\in K` and every unchanged point also lies in `K`,

```math
\operatorname{diam}A'
\le\operatorname{diam}K
=D.
\tag{2.1}
```

But `D=D(n)` is the global minimum over all unit-separated `n`-point sources, so (2.1) must be equality:

```math
\boxed{\operatorname{diam}A'=D.}
\tag{2.2}
```

Hence `A'` is another global minimizer.

Only one new unit-contact edge is created. Since `x` had no old unit contacts, a unit-contact triangle involving `x'` would require at least two new contacts incident to `x'`. There is exactly one. All triangles avoiding `x'` would already have existed in `A`. Therefore

```math
\boxed{A'\text{ is triangle-free}.}
\tag{2.3}
```

Finally,

```math
|C(A')|=|C(A)|+1.
\tag{2.4}
```

No source point is deleted, no diameter comparison is asymptotic, and no KKT statement is used.

---

## 3. Finite saturation theorem

### Theorem 3.1 — no-actual-isolate triangle-free representative

If there exists a noncollinear triangle-free global minimum-diameter `n`-point source, then there exists one with no contact-isolated source point.

More strongly, starting from any such source `A`, repeated applications of Section 2 terminate after at most `n` steps at a triangle-free global minimizer `A^sat` satisfying

```math
\boxed{\deg_{C(A^{sat})}(x)\ge1\quad\text{for every }x\in A^{sat}.}
\tag{3.1}
```

At each step the global diameter remains exactly `D(n)`, the number of source points remains `n`, triangle-freeness is preserved, and the number of unit contacts increases by exactly one.

### Proof

A Section-2 move changes only a contact-isolated point and gives it exactly one unit neighbor. Every old contact between unchanged source points remains unchanged. Hence the number of contact-isolated vertices drops by at least one and no previously nonisolated vertex becomes isolated.

There are finitely many source points, so after at most `n` moves no contact-isolated point remains. Section 2 proves every intermediate source is still a triangle-free global minimizer of the same cardinality and diameter. `square`

### Corollary 3.2 — contact-maximal normalization

Among the triangle-free global minimizers, choose one whose number of unit contacts is maximal. Such a maximum exists because the set of attained contact counts is a nonempty subset of the finite integer set

```math
\{0,1,\ldots,\tbinom n2\}.
```

Then that representative has no contact-isolated source point.

This is an immediate consequence of (2.4).

---

## 4. Canonical post-ZF strengthening: preserve the old force core and diameter graph

Now start from the canonical contact-minimal, then diameter-pair-minimal post-ZF C-II representative. Let

- `V` be its nonisolated positive-contact core;
- `H` be its full actual diameter-edge set; and
- `Z` be its actual contact-isolated source points.

Canonical Section 57 records that every endpoint of an actual diameter edge is loaded by the relative-interior stress and therefore belongs to `V`. Hence

```math
\boxed{x\in Z\Longrightarrow |x-y|<D\text{ for every }y\in A\setminus\{x\}.}
\tag{4.1}
```

### Lemma 4.1 — diameter-safe first contact

For `x\in Z`, the point `x'` in Lemma 1.1 can be chosen so that in addition

```math
|x'-y|<D\qquad(y\in A\setminus\{x\}).
\tag{4.2}
```

### Proof

For each unchanged source point `y`, the old hull satisfies

```math
K\subseteq B(y,D).
```

The polygon `K` meets the circle `\partial B(y,D)` in finitely many points: each straight side has at most two intersections with the circle, and `K` has finitely many sides. Taking the union over the finite source gives a finite set

```math
E_D:=K\cap\bigcup_{y\ne x}\partial B(y,D).
```

In the generic-ray construction of Lemma 1.1, exclude also the finitely many rays from `x` through points of `E_D`. The target set `K\cap\operatorname{int}U` still has positive area, so such a generic target exists. The resulting segment contains no point of `E_D`, and in particular its first unit-contact point `x'` satisfies (4.2). `square`

Apply Lemma 4.1 one isolate at a time. The old point `x` was incident to no diameter edge by (4.1), and the new point `x'` is incident to none by (4.2). Thus the actual diameter-edge set `H` is unchanged at every saturation step.

Likewise, every old positive-contact vertex and every old positive-contact edge keeps its old position and length. Any normalized KKT stress of the old canonical source extends to the saturated source by retaining every old multiplier and assigning weight zero to every new forest contact. Normalization is unchanged because the diameter weights are unchanged.

### Theorem 4.2 — force-core-preserving saturation

The canonical post-ZF triangle-free global minimizer can be transformed into another triangle-free global minimizer `A^sat` of the same cardinality and diameter such that

```math
\boxed{H(A^{sat})=H(A).}
\tag{4.3}
```

Every old normalized KKT stress extends to a normalized KKT stress of `A^sat` by giving all new contacts weight zero.

### 4.1 The new contacts form a forest

At each saturation step the moved vertex has actual contact degree zero immediately before the move, and exactly one new contact edge is added. Adding an edge incident to an isolated vertex cannot create a contact-graph cycle. Hence the set `F_new` of all newly created contacts is a forest.

If the initial isolate population is

```math
z:=|Z|
```

and `m` saturation moves are performed, each move removes at most two isolated vertices: the moved isolate and, only when its unique blocker was also isolated, that blocker. Since saturation ends with no isolates,

```math
2m\ge z.
```

Exactly one new edge is created per move, so

```math
\boxed{|F_{new}|=m\ge\lceil z/2\rceil.}
\tag{4.4}
```

Because the old contact-minimal C-I representative has no weak actual contacts, its old actual contact graph is the positive core together with the isolated vertices `Z`. Consequently the final actual contact graph is the old positive core plus a forest of new edges. Every tree of that forest is either attached to the old core at one vertex or remains a separate tree. No new edge can create a second attachment of an existing tree: its moved endpoint is isolated at the moment of insertion, so it can only attach that singleton to one pre-existing vertex/component.

### 4.2 Leaf elimination forces every new multiplier to vanish

Take an **arbitrary** normalized KKT stress of the saturated source, not necessarily one inherited from the old source. The actual diameter graph is still the old `H`, so no vertex of `Z` carries a diameter multiplier.

Consider one tree component `T` of `F_new`.

- If `T` is disjoint from the old core, every vertex of `T` is an old contact isolate and has no old contact edge or diameter edge.
- If `T` is attached to the old core, it has exactly one old-core root. Every other vertex of `T` is an old contact isolate and has no old contact edge or diameter edge.

Choose a leaf of `T` that is not the old-core root. Its KKT equilibrium equation contains exactly one possibly nonzero row from `F_new` and no diameter load. The contact vector on that edge is nonzero, so its multiplier must be zero.

Delete that zero-weight leaf edge from the force-balance calculation and repeat. Inductively every edge of `T` has zero multiplier. This works for every tree component, so

```math
\boxed{\alpha_e=0\qquad(e\in F_{new})}
\tag{4.5}
```

in **every** normalized KKT stress of `A^sat`.

After the forest multipliers vanish, the remaining equilibrium and normalization equations are exactly those of the old canonical source on the unchanged old contact and diameter rows. Conversely every old normalized stress extends by zero on `F_new`. Therefore zero-extension/restriction gives a bijection

```math
\boxed{
\mathcal K(A^{sat})\cong\mathcal K(A)
}
\tag{4.6}
```

between the normalized KKT stress polytopes.

In particular the positive KKT support, old core `V`, stress matrix `Omega_V`, diameter graph `H`, and every old stress coefficient are unchanged. The added contacts are not merely zero in one inherited stress; they are **KKT-invisible in every stress**.

Combining (4.4) and (4.5), a macroscopic inactive-container population `z=Omega(D^2)` can be converted, without changing the old force system or diameter graph, into

```math
\boxed{Omega(D^2)\text{ exact unit contacts carried by a KKT-invisible forest}.}
\tag{4.7}
```

This is a whole-population strengthening of proof-only Section 95: first-contact creation can fail to alter the normalized KKT polytope even after the entire actual-isolate population has been saturated.

---

## 5. Relation to the canonical C-II split

The theorem changes the interpretation of the macroscopic-container obstruction but does not by itself close it.

The canonical contact-minimal normalization has the decisive property that every actual contact is a strong KKT row. That is what permits C-I, ZR/ZF, and the exact post-ZF ledgers. Saturation destroys that equality between the actual contact set and positive KKT support, while (4.6) proves that the force system itself is unchanged.

Therefore Theorems 3.1 and 4.2 do **not** justify any of the following:

- extending `ker Omega_V=span{1,P_x|_V,P_y|_V}` to the newly saturated points;
- deleting the canonical macroscopic-container branch from audit.44;
- treating every new unit contact as positive-force support;
- concluding that C-II is closed.

What they do prove is the following exact alternative research route:

```text
canonical triangle-free global survivor
    -> same D, same n, same old H and exactly the same normalized KKT polytope,
       but no actual contact isolates;
    -> the former isolate population is carried by a KKT-invisible unit-contact forest.
```

Thus the macroscopic-isolate branch is not intrinsically a problem of finding first contacts. It is a **global-minimality problem for a macroscopic exact weak-contact forest that is invisible to first-order force transfer**. Any successful chamber closure must use the forest geometry to reconfigure the old diameter-carrying core, or use an additional normalization beyond the KKT system.

The separate weak-forest density regression shows that near-triangular packing density alone cannot do this.

---

## 6. Hostile checks

- **Diameter:** moving the isolated point inside the old convex hull gives the exact bound `diam(A')<=D`; global minimality then forces equality.
- **Old diameter graph:** in the canonical post-ZF source, an actual contact isolate is not a diameter endpoint. The generic ray is additionally chosen to avoid the finite diameter-equality set in the polygonal hull, so no new diameter edge is created.
- **Unit separation:** the path stops at the first entry into the union of closed unit disks, so no distance can drop below one.
- **Simultaneous first contacts:** excluded by choosing a segment ray avoiding the finite set of pairwise unit-circle intersection points.
- **Triangle creation:** exactly one new unit edge is added; therefore no new triangle can contain the moved point.
- **Cardinality/source retention:** one source point is moved, not deleted or duplicated.
- **One-root property:** a new edge always has an isolated moved endpoint. Once a former isolate enters a nontrivial new tree it is no longer eligible to move, so that tree can never later acquire a second old-core attachment.
- **KKT leaf peeling:** every nonroot forest vertex is an old actual contact isolate, hence has no old contact row and, by canonical Section 57, no diameter row. After child multipliers are shown zero, its parent edge is the only remaining possible force and must also have zero multiplier.
- **KKT polytope claim:** (4.6) is exact because `H` and every old row are unchanged, every new multiplier is forced zero, and normalization uses the unchanged old diameter weights.
- **Proof-only Section 95:** compatible and strengthened. Section 95 gives local examples where contact creation fails to change the active force system; Theorem 4.2 gives a whole-population saturation for which the entire normalized KKT polytope provably stays unchanged.

**Disposition:** proof-only structural normalization theorem. C-II remains open.
