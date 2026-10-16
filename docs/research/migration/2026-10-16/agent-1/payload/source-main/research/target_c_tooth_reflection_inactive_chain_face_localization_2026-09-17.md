# Target C-II — the reflection inactive chain stays in one contact face

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the linear inactive-chain reduction  
**Scope:** non-anchored FREE reflection modules after the linear inactive near-unit chain theorem  
**Dependencies:** linear inactive-chain theorem; planar straight-line unit-contact graph; C65 full contact visibility  
**Certificate:** `research/verify_target_c_tooth_reflection_inactive_chain_face_localization_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The linear inactive chain cannot wander across the positive contact network. A simple four-point inequality gives a sharp crossing threshold:

\[
\boxed{
\text{if a source segment }AB\text{ crosses a unit contact }CD,
\text{ then }|AB|\ge\sqrt3.
}
\tag{FL.1}
\]

Every parent edge in the reflection chain has original length

\[
|z_jz_{j+1}|
<1+h_*+o(1)
=1.3347479843\ldots+o(1)
<\sqrt3.
\]

Therefore no chain edge crosses any unit contact edge. It also cannot pass through a contact-core vertex, because a source vertex in the interior of a segment would force that segment to have length at least two.

Hence the complete linear chain lies in **one face of the original unit-contact graph**. In particular, for every fixed `lambda<1/2`, a non-anchored FREE module forces one contact face whose support-depth span is at least

\[
\boxed{\lambda D-O(\sqrt D).}
\tag{FL.2}
\]

A bounded quadrilateral unit-contact face has diameter at most two, so for large `D` this face cannot be one of the ordinary quadrilateral grains. It must be either a bounded exceptional contact face or the outer contact face.

Thus the reflection branch now plugs directly into the canonical exceptional-face / inactive-chamber geometry rather than merely producing a free rattler path somewhere in the source.

---

## 1. Crossing a unit contact costs at least `sqrt(3)`

Let `C,D` be source points with

\[
|C-D|=1.
\]

Let `A,B` be two other source points, and suppose the open segments `AB` and `CD` cross at `P`.

Write

\[
P=(1-t)C+tD,
\qquad 0<t<1.
\]

For any point `X`, the exact weighted variance identity is

\[
(1-t)|X-C|^2+t|X-D|^2
=|X-P|^2+t(1-t)|C-D|^2.
\tag{FL.3}
\]

Apply this first with `X=A`. Source separation gives

\[
|A-C|,|A-D|\ge1.
\]

Since `|C-D|=1`, (FL.3) yields

\[
|A-P|^2
\ge1-t(1-t)
\ge\frac34.
\tag{FL.4}
\]

Thus

\[
|A-P|\ge\frac{\sqrt3}{2}.
\]

The same argument gives

\[
|B-P|\ge\frac{\sqrt3}{2}.
\]

Because `P` lies in the open segment `AB`,

\[
|A-B|=|A-P|+|P-B|
\ge\sqrt3.
\]

This proves (FL.1). Equality is attained by the two opposite equilateral apexes over the midpoint of `CD`, so the threshold is sharp.

---

## 2. Chain edges are strictly below the crossing threshold

The linear inactive-chain theorem gives, uniformly along the parent chain,

\[
1<|z_j-z_{j+1}|
\le1+t_D,
\]

where

\[
t_D\le h_*+o(1),
\qquad
h_*={\sqrt{303}\over52}.
\]

Numerically,

\[
1+h_*=1.334747984337100\ldots,
\qquad
\sqrt3=1.732050807568877\ldots .
\]

Hence for all sufficiently large `D`,

\[
\boxed{|z_j-z_{j+1}|<\sqrt3.}
\tag{FL.5}
\]

By (FL.1), no parent edge crosses a unit contact edge.

A parent edge also cannot pass through a third source point `v`. If

\[
v\in(z_j,z_{j+1}),
\]

then source separation gives

\[
|z_j-v|\ge1,
\qquad
|v-z_{j+1}|\ge1,
\]

so

\[
|z_j-z_{j+1}|
=|z_j-v|+|v-z_{j+1}|
\ge2,
\]

contradicting (FL.5).

Thus every open parent segment avoids the entire embedded contact graph.

---

## 3. One chain lies in one contact face

Every chain vertex is fully inactive in the original source, so it is not a vertex of the nonisolated contact core. It therefore lies in the interior of a unique face of the straight-line contact embedding.

The open segment from `z_j` to `z_{j+1}` crosses no contact edge and contains no contact vertex. Hence its two endpoints lie in the same contact face.

Consecutive parent edges share the inactive vertex `z_j`, so induction along the chain shows that all vertices and all parent segments lie in one and the same face `F_chain`.

Therefore

\[
\boxed{
\{z_0,\ldots,z_\ell\}\subset F_{chain}.
}
\tag{FL.6}
\]

The support-depth span of this face is at least that of the chain endpoints. From the linear-chain theorem,

\[
a_{z_0}=O(\sqrt D),
\qquad
a_{z_\ell}>\lambda D.
\]

Hence

\[
\boxed{
\operatorname{span}_N(F_{chain})
\ge\lambda D-O(\sqrt D).
}
\tag{FL.7}

This is (FL.2).

---

## 4. Ordinary quadrilateral grains are excluded

If `F_chain` were a bounded quadrilateral contact face, its boundary would consist of four unit edges.

Any two boundary vertices are joined along the boundary by a path of at most two unit edges, so their Euclidean distance is at most two. The whole face lies inside the convex hull of its four boundary vertices; the diameter of that convex hull is attained by a pair of vertices. Therefore

\[
\operatorname{diam}(F_{chain})\le2.
\tag{FL.8}
\]

But (FL.7) gives

\[
\operatorname{diam}(F_{chain})
\ge\lambda D-O(\sqrt D),
\]

which exceeds two for all sufficiently large `D`.

Thus

\[
\boxed{
F_{chain}\text{ is a bounded exceptional contact face or the outer contact face.}
}
\tag{FL.9}

The reflection FREE branch therefore cannot hide its macroscopic inactive chain inside the near-rhombic quadrilateral grain sea.

---

## 5. Frontier effect

Combining the current reflection reductions gives the following effective alternative for every slow-scale selected module:

```text
EXACT-BRAID
    actual source diameter localized to the module caps

or

MACROSCOPIC INACTIVE FACE
    one original contact face contains a fully inactive chain
    of length Omega(D)
    support-depth span lambda D - O(sqrt D), any fixed lambda<1/2
    every consecutive original distance < 1.334748+o(1)
    face is exceptional bounded or outer
```

This is a stronger interface with the canonical inactive-chamber branch than the bare linear-chain statement. Any further FREE-branch closure can now use the geometry and Oler budget of one specific exceptional/outer contact face.

**Disposition:** proved the sharp `sqrt(3)` contact-crossing threshold and localized every reflection-induced linear inactive chain to a single macroscopic contact face, excluding ordinary quadrilateral grains. C-II remains open.
