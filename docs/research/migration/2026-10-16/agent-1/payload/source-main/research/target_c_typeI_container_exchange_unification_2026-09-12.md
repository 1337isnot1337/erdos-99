# Target C — both Type-I inactive containers are exchange-saturated and carry deep near-unit isolate matchings

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only extension of the audited inactive-exchange route; theorem authority unchanged.  
**Dependencies:** canonical Sections 80, 81, 87; audited-working `inactive-exchange-saturation.md` for the lexicographic exchange principle.

Canonical Section 80 leaves two geometric forms of the Type-I macroscopic-container branch:

1. an internal inactive chamber inside the force hull; or
2. an exterior cap between the force hull and the full source hull.

The internal case already has exact finite exchange saturation and canonical deep
inverse-diameter near-matchings. The exterior case was left separate. This note removes
that asymmetry.

An actual macroscopic exterior cap satisfies the same local hypotheses needed by the
exchange and matching arguments. Consequently **either** Type-I container contains a
quadratic contact-isolated packing which is finitely exchange-saturated and has linearly
many deep vertex-disjoint pairs at distance `1+O(1/D)`. For fixed depth greater than
one, closing any such pair can be blocked first only by another isolate in the same
container.

This does not yet produce the required density-increasing finite repacking. It reduces
both Type-I alternatives to one purely inactive local packing problem.

---

## 1. Exterior-cap data from canonical Section 80

Let `C=K_*` be the macroscopic exterior cap selected in canonical Section 80. Write

\[
A_C:=\operatorname{area}C,
\qquad
P_C:=\operatorname{per}C,
\qquad
Z_C:=A\cap(C\setminus F),
\qquad z_C:=|Z_C|.
\]

Along the Type-I exterior-cap subsequence, Section 80 gives fixed constants
`alpha,P_0,zeta>0` such that, for all sufficiently large `D`,

\[
\boxed{
A_C\ge\alpha D^2,
\qquad
P_C\le P_0D,
\qquad
z_C\ge\zeta D^2.
}
\tag{1.1}
\]

Every point of `Z_C` is an actual contact-isolated source point. The interiors of the
exterior caps are disjoint and partition `K\setminus F` up to their closing chords.
Hence every source point not assigned to `Z_C` lies outside `int(C)`; points on a
closing chord or cap boundary are harmless for the depth estimates below.

Section 80 defines the cap slack

\[
\sigma_C^{ext}
:={A_C\over a_0}+{P_C\over2}-1-z_C
\ge0,
\qquad a_0={\sqrt3\over2},
\tag{1.2}
\]

and the sum of all exterior-cap slacks is `O(D)`. In particular the selected cap has

\[
\sigma_C^{ext}=O(D).
\tag{1.3}
\]

For the isolate set alone, the canonical Section-81 slack is

\[
\sigma_C
:={A_C\over a_0}+{P_C\over2}+1-z_C
=\sigma_C^{ext}+2.
\tag{1.4}
\]

Therefore

\[
\boxed{\sigma_C=O(D).}
\tag{1.5}
\]

So the exterior cap satisfies exactly the convex-body / isolate-only-slack hypotheses
of the canonical near-matching theorem.

---

## 2. A macroscopic exterior cap has linear inradius

Let `r(C)` be the inradius of the convex cap. For `0<t<r(C)`, convex inner-parallel
coarea gives

\[
A_C-\operatorname{area}(C_{-t})
=\int_0^t\operatorname{per}(C_{-s})\,ds
\le tP_C.
\tag{2.1}
\]

Letting `t\uparrow r(C)` and using that the terminal inner parallel body has zero
planar area gives

\[
A_C\le r(C)P_C.
\]

Thus (1.1) implies

\[
\boxed{
r(C)\ge {A_C\over P_C}\ge {\alpha\over P_0}D.
}
\tag{2.2}
\]

In particular, every fixed-depth inner parallel body `C_{-w}` exists for all
sufficiently large `D`. Moreover (2.1) gives

\[
\operatorname{area}(C\setminus C_{-w})\le wP_C=O_w(D),
\]

so

\[
\boxed{
\operatorname{area}(C_{-w})=\Omega(D^2)
}
\tag{2.3}
\]

for every fixed `w>0`.

No separate exterior-cap hull-stability theorem is needed: quadratic area plus linear
perimeter already supplies the required linear inradius.

---

## 3. Exact strict exchange saturation for an exterior cap

The finite exchange proof used for an internal chamber depends only on convex depth,
not on which side of the force hull the container lies.

### Theorem 3.1 — cap unit covering

For every sufficiently large exterior Type-I survivor,

\[
\boxed{
C_{-1}\subseteq
\bigcup_{z\in Z_C}\overline B(z,1).
}
\tag{3.1}
\]

### Proof

Suppose `x in C_{-1}` satisfies `|x-z|>1` for every `z in Z_C`. Any source point
`a notin Z_C` lies outside `int(C)`. The segment from `x` to `a` meets `partial C`, so

\[
|x-a|\ge\operatorname{dist}(x,\partial C)>1.
\]

Thus `x` is strictly farther than one from every source point. Delete any nonisolated
contact vertex `v` of the positive core and insert `x`. Cardinality is unchanged;
unit separation is strict; `x in C subset K=conv(A)`, so diameter is at most `D` and
therefore exactly `D(n)` by global minimality. The deleted vertex had at least one
unit contact and the inserted point has none. This contradicts contact minimality.
`square`

The same argument gives the full finite version.

### Theorem 3.2 — protected `k -> k+1` obstruction

For every finite `W subseteq Z_C`, there is no set

\[
Y\subset C_{-1},
\qquad |Y|=|W|+1,
\tag{3.2}
\]

such that

\[
|y-y'|>1
\quad(y\ne y'\in Y),
\qquad
|y-z|>1
\quad(y\in Y,\ z\in Z_C\setminus W).
\tag{3.3}
\]

Indeed every retained source outside the cap interior is automatically farther than
one from `Y`, and replacing `W` plus one nonisolated contact vertex by `Y` contradicts
contact minimality exactly as above.

Thus the exterior cap is finitely exchange-saturated in the same strict sense as the
internal inactive chamber.

---

## 4. The loaded lexicographic exchange also extends to exterior caps

Let `v` be a source vertex with both positive contact degree and positive active
diameter degree. Let `W subseteq Z_C` be finite and let

\[
Y\subset C_{-1},
\qquad |Y|=|W|+1.
\]

Assume the replacement

\[
A':=(A\setminus(W\cup\{v\}))\cup Y
\]

is unit-separated and triangle-free. Let `c_new` be the number of new unit contacts
incident to `Y`.

Every point of `C_{-1}` lies in `int(C)`, and `int(C) subset int(K)` because `C subset K`
is a positive-area convex body. Hence the audited lexicographic interior lemma applies:
for every old `x in K` and new `y in Y`,

\[
|x-y|<D.
\]

The new points create no active diameter pair. Therefore exactly the same
contact-count / diameter-pair argument as in `inactive-exchange-saturation.md` gives:

\[
\boxed{
c_{new}>d_C(v).}
\tag{4.1}
\]

for every such replacement. More generally, the audited multi-vertex form extends
unchanged: if a finite deleted core set `U` loses at least one active diameter pair,
a same-cardinality interior cap repacking cannot have new-contact count at most the
number of old contacts incident to `U`.

Since loaded contact degree is at most three in the post-ZF structure, a triangle-free
protected `k -> k+1` cap repacking that creates at most three contacts would already
contradict the lexicographic normalization whenever one suitable loaded vertex is used
as the exchanged core vertex.

---

## 5. Canonical near-matching theorem applies verbatim to the exterior cap

Canonical Theorem 81.1 is stated for **any** convex body `C` containing a specified
contact-isolated set `Z`, with isolate-only slack

\[
\sigma={A\over a_0}+{P\over2}+1-|Z|.
\]

For `0<epsilon<=1` it gives

\[
\nu_\epsilon
\ge {3A\over8a_0}\epsilon-{\sigma\over2},
\tag{5.1}
\]

where `nu_epsilon` is the maximum matching number among pairs of isolates at distance
at most `1+epsilon`.

Apply this with the exterior cap data (1.1), (1.5). Choose a fixed `K>0` sufficiently
large that

\[
{3\alpha K\over8a_0}
-
{S\over2}>0,
\]

where `sigma_C<=SD` eventually. With `epsilon=K/D`, (5.1) yields

\[
\boxed{
\nu_{K/D}=\Omega(D).
}
\tag{5.2}
\]

Thus the macroscopic exterior cap has linearly many vertex-disjoint actual isolate
pairs satisfying

\[
\boxed{
1<|x-y|\le1+{K\over D}.
}
\tag{5.3}
\]

The strict lower bound follows because all cap points in `Z_C` are contact-isolated.

---

## 6. The deep matching theorem also extends to the exterior cap

Fix any physical depth `w>0`. Exactly as in canonical Section 87, radius-`1/2` disks
centered at cap isolates in the width-`w` boundary strip are disjoint and lie in

\[
C_{+1/2}\setminus C_{-(w+1/2)}.
\]

Steiner plus inner-parallel coarea gives

\[
|Z_C\cap U_w|
\le {4(w+1)P_C\over\pi}+1
=O_w(D).
\tag{6.1}
\]

In (5.1), increase the fixed numerator constant `K=K_w` until the coefficient of
`D` in the matching lower bound exceeds the boundary-strip coefficient in (6.1).
Because the matching is vertex-disjoint, at most `|Z_C cap U_w|` matching edges have a
boundary-strip endpoint. Therefore there are constants `K_w,c_w>0` such that

\[
\boxed{
\#\{xy:\ 1<|x-y|\le1+K_w/D,
\quad
\operatorname{dist}(\{x,y\},\partial C)\ge w\}
\ge c_wD.
}
\tag{6.2}
\]

The pairs are vertex-disjoint.

For `w>1`, the pair-closing segment is contained in the convex body `C_{-w}`. Moving
one endpoint toward its mate by at most `K_w/D`:

- stays in `C subset K`, so it cannot violate the diameter upper bound;
- remains farther than one from every source point outside `int(C)` for all sufficiently
  large `D`; and
- therefore cannot first hit the positive contact core, a different exterior cap, an
  internal inactive chamber, or any other unassigned source point.

Hence:

### Corollary 6.1 — exterior-cap first blockers are cap isolates

For each of the `Omega_w(D)` deep pairs, if the chosen mate does not reach unit distance
first, the first unit-distance blocker is another contact-isolated source point assigned
to the **same exterior cap**.

This is the exact exterior analogue of canonical Corollary 87.2.

---

## 7. Unified Type-I normal form

Combining the existing internal-chamber theorems with Sections 1–6 above gives the
following proof-only unification.

Every Type-I macroscopic inactive-container survivor has one actual convex container
`C_*`, internal or exterior, and an assigned contact-isolated set `Z_*` such that

\[
\boxed{
\operatorname{area}(C_*)=\Omega(D^2),
\quad
|Z_*|=\Omega(D^2),
\quad
\operatorname{per}(C_*)=O(D),
\quad
\sigma_*=O(D),
\quad
r(C_*)=\Omega(D).
}
\tag{7.1}
\]

Moreover:

1. `C_{*,-1}` is unit-covered by `Z_*`;
2. no protected strict finite `k -> k+1` repacking exists there;
3. the loaded lexicographic version forbids any triangle-free `k -> k+1` repacking
   whose new-contact budget fits the deleted loaded core vertex;
4. for every fixed `w>1`, there are `Omega_w(D)` vertex-disjoint deep isolate pairs
   at distance `1+O_w(1/D)`; and
5. the straight closing motion of each such pair can be blocked first only by another
   isolate in the same container.

Thus the macroscopic-container branch no longer splits structurally into an internal
case with deep matching and an exterior case without it. Both reduce to the same
finite local obligation:

> prove a protected density-increasing repacking of a near-capacity convex isolate
> packing, possibly allowing the small contact budget paid by deleting one or several
> loaded core vertices.

The scaled triangular-lattice regression remains binding: strict gaps can be much
smaller than `1/D`, and independent first-contact motions need not yield a valid
`k -> k+1` move. A collective finite exchange is still required.

---

## 8. Hostile checks

- **Slack convention:** Section 80's exterior slack has `-1-z_C` because its local
  Oler set includes the two closing-chord endpoints. The isolate-only Section-81 slack
  is exactly `sigma_C^{ext}+2`; the difference is constant and does not affect `O(D)`.
- **Unassigned sources:** cap interiors partition `K\setminus F`; every source not
  assigned to the selected cap is outside its open interior. Fixed positive depth
  therefore protects against all such points.
- **Inradius:** no circularity is used. The linear inradius follows directly from
  `A_C=Omega(D^2)`, `P_C=O(D)`, and convex inner-parallel coarea.
- **Diameter:** every moved or inserted point remains in the old full source hull `K`,
  whose diameter is `D`.
- **Diameter-pair lexicography:** points of `C_{-1}` are interior to `K`, hence create
  no diameter pair by the audited interior lemma.
- **Triangle-free comparison class:** the loaded-exchange conclusion explicitly
  assumes the replacement is triangle-free.
- **Cardinality:** every exchange removes and inserts the same total number of source
  points.
- **Core affine kernel:** no contact-isolated coordinate is added to the Section-57
  affine kernel.

**Disposition:** proof-only branch unification. C-II and Level I remain open.
