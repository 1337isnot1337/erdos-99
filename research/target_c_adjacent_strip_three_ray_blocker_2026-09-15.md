<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "212ae32edbc862464028cbdf48c2f20698217488", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_strip_three_ray_blocker_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "baad88165914b734b333001a86866a441e6b96dcb6cb56f24158b36d5898819c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — an adjacent strip has a three-ray blocker certificate

**Date:** 2026-09-15  
**Status:** proof-only finite/source-level structural strengthening  
**Scope:** the adjacent O--O strip-opening reduction in the canonical contact-minimal full-core Type-II representative  
**Dependencies:** adjacent-strip opening reduction; positive relative-interior KKT stress; uniqueness of a planar diameter pair in one projective direction  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The adjacent-strip theorem reduces every moving upper-distance constraint to a finite switching caterpillar.  For local blocking, even that forest is much larger than necessary.

Let `R` be one adjacent source layer.  Orient the two boundary train contact vectors from outside `R` into `R` and call them

\[
a,b,\qquad |a|=|b|=1.
\]

For each switching actual diameter edge, orient the diameter vector from its endpoint outside `R` to its endpoint inside `R` and write

\[
r_h=Dd_h,\qquad |d_h|=1.
\]

Translating `R` by `v` sends the two boundary contact vectors to `a+v,b+v` and every switching diameter vector to `Dd_h+v`.

The canonical survivor has the following finite obstruction.

### Theorem TR — three-ray / antipodal-two-edge blocker

1. If
   \[
   a+b\ne0,
   \]
   then there is a subset of at most three rays from
   \[
   \boxed{\{a,b\}\cup\{-d_h:h\in H_{sw}\}}
   \tag{TR.1}
   \]
   whose convex hull contains the origin.  At least one selected ray is a switching-diameter ray.  Hence the failure of a strict first-order contact-opening / diameter-shortening strip translation has a certificate using at most **three switching diameter edges**, and often only one or two.

2. If
   \[
   b=-a,
   \]
   then the first-order contact cone is degenerate, but the finite problem is stronger: every canonical survivor contains two switching diameter edges `h_+,h_-` with opposite transverse signs
   \[
   \boxed{
   d_{h_+}\cdot Ja>0,
   \qquad
   d_{h_-}\cdot Ja<0.
   }
   \tag{TR.2}
   \]
   A switching diameter parallel to `a` cannot replace this pair; there is at most one such diameter edge and a second-order axial correction bypasses it.

3. Independently of the two cases, the exact KKT strip resultant
   \[
   Aa+Bb
   =D\sum_{h\in H_{sw}}\beta_hd_h,
   \qquad A,B>0,\ \beta_h>0,
   \tag{TR.3}
   \]
   admits a planar compressed certificate:
   - if `Aa+Bb!=0`, its direction lies in the cone of at most two switching diameter directions;
   - if `Aa+Bb=0`, the zero resultant lies in the convex hull of at most three switching diameter directions.

Thus the `<1763` switching caterpillar is globally useful for finite support and cyclic order, but the actual planar obstruction to strip translation is controlled by at most three diameter directions.

---

## 1. Strict first-order opening/shrinking directions

For a small translation `v`, the boundary contact squared-length changes are

\[
|a+v|^2-1=2a\cdot v+|v|^2,
\]

\[
|b+v|^2-1=2b\cdot v+|v|^2.
\tag{TR.4}
\]

For a switching diameter edge,

\[
|Dd_h+v|^2-D^2
=2D d_h\cdot v+|v|^2.
\tag{TR.5}
\]

Suppose there were a vector `w` satisfying the strict homogeneous inequalities

\[
a\cdot w>0,
\qquad
b\cdot w>0,
\qquad
-d_h\cdot w>0
\quad(h\in H_{sw}).
\tag{TR.6}
\]

Then for all sufficiently small `s>0`, the translation

\[
v=sw
\]

would strictly open both boundary contact families and strictly shorten every switching old diameter.  By the strict-slack part of the adjacent-strip theorem, all old strict noncontacts would stay above one and all old strict nondiameter pairs would stay below `D`.  Every nonswitching old diameter is unchanged exactly.

The translated source would therefore have diameter at most `D` and strictly fewer unit contacts, contradicting global/contact minimality exactly as in the strip-opening theorem.

Hence no `w` satisfies (TR.6).

---

## 2. Planar separation gives a three-ray certificate when `a+b!=0`

Put

\[
\mathcal N
:=\{a,b\}\cup\{-d_h:h\in H_{sw}\}.
\]

For a finite set of nonzero vectors in `R^2`, the following alternatives are equivalent by strict separation:

- there exists `w` with `n dot w>0` for every `n in N`;
- the origin does **not** belong to `conv(N)`.

Section 1 excludes the first alternative.  Therefore

\[
0\in\operatorname{conv}\mathcal N.
\tag{TR.7}
\]

Caratheodory's theorem in dimension two gives vectors

\[
n_1,n_2,n_3\in\mathcal N
\]

with

\[
0\in\operatorname{conv}\{n_1,n_2,n_3\}.
\tag{TR.8}
\]

Some of the three may be redundant, so the witness can have size one or two.

If `a+b!=0`, the two contact rays alone cannot contain the origin in their segment: for unit vectors

\[
0\in[a,b]
\]

would force `b=-a`.  Thus every certificate (TR.8) contains at least one switching-diameter ray.

Since there are only two contact rays in the entire set, at most three switching diameter edges appear in the certificate.  More precisely the only nondegenerate witness types are

```text
{a,b,-d1},
{a,-d1,-d2} or {b,-d1,-d2},
{-d1,-d2,-d3},
```

with lower-cardinality degeneracies allowed.

This proves part 1 of Theorem TR.

---

## 3. Exact antipodal boundaries require a second-order argument

Now assume

\[
b=-a.
\]

Put

\[
n:=Ja.
\]

The two contacts cannot both open strictly at first order because their linear terms are opposite.  But they can open simultaneously at second order.

Write a small strip translation as

\[
v=x a+y n.
\]

Then the two boundary contact conditions are

\[
2x+x^2+y^2>0,
\qquad
-2x+x^2+y^2>0.
\tag{TR.9}
\]

Set

\[
y=t,
\qquad
x=\kappa t^2
\tag{TR.10}
\]

for fixed

\[
-{1\over2}<\kappa<{1\over2}.
\]

For all sufficiently small nonzero `t`, both inequalities (TR.9) are strict.

Write a switching diameter direction as

\[
d_h=c_ha+s_hn.
\]

Its squared-length change is

\[
2D(c_h\kappa t^2+s_ht)
+t^2+\kappa^2t^4.
\tag{TR.11}
\]

If `s_h!=0`, the sign for sufficiently small `t` is governed by `s_ht`.

Suppose all nonzero transverse values `s_h` had one sign.  Choose the sign of `t` so

\[
s_ht<0
\]

for every nonzero `s_h`.  Then all such diameter edges shorten for sufficiently small `|t|`.

It remains to handle switching edges with

\[
s_h=0.
\]

Such an edge is parallel to the boundary contact projective direction `a`.  A finite planar source has at most one unordered diameter pair in a prescribed projective direction: if two distinct diameter segments were parallel, orienting them alike and comparing the two cross-distances forces them to coincide.  Hence there is at most one zero-transverse switching diameter.

If none exists, take `kappa=0` and all switching diameters shorten.

If the unique zero-transverse direction is `d_h=a`, choose

\[
-{1\over2}<\kappa<-{1\over2D}.
\]

Then its leading `t^2` coefficient in (TR.11) is

\[
1+2D\kappa<0.
\]

If instead `d_h=-a`, choose

\[
{1\over2D}<\kappa<{1\over2},
\]

and the leading coefficient is again negative.

These fixed choices of `kappa` do not affect the already-strict linear shortening of the nonzero-transverse edges when `|t|` is sufficiently small.

Thus, if all nonzero `s_h` had one sign, there would be a finite translation opening both boundary contact families and shortening every switching diameter.  The adjacent-strip theorem would contradict canonical minimality.

Therefore a survivor must contain two switching diameters with opposite transverse signs, proving (TR.2).

---

## 4. Exact KKT strip balance

Let `alpha_e>0,beta_h>0` be the relative-interior KKT multipliers, normalized by

\[
\sum_H\beta_h=1.
\]

Let

\[
A=\sum_{e\in\tau_i}\alpha_e,
\qquad
B=\sum_{e\in\tau_{i+1}}\alpha_e.
\]

Orient both boundary contact vectors from outside the strip into the strip, as above.  Summing equilibrium over all vertices of the strip cancels every internal force and gives

\[
\boxed{
Aa+Bb
=D\sum_{h\in H_{sw}}\beta_hd_h.
}
\tag{TR.12}
\]

This is the strip-oriented version of subtracting the two Section-157 cut resultants.

If

\[
F:=Aa+Bb\ne0,
\]

then `F/D` belongs to the positive cone generated by the switching unit directions `d_h`.  Conic Caratheodory in `R^2` says every vector in a finitely generated cone is generated by at most two generators.  Hence there are switching edges `h_1,h_2` and coefficients `lambda_1,lambda_2>=0` such that

\[
\boxed{
F=D(\lambda_1d_{h_1}+\lambda_2d_{h_2}).
}
\tag{TR.13}
\]

If `F=0`, divide (TR.12) by the positive switching mass

\[
B_{sw}:=\sum_{h\in H_{sw}}\beta_h.
\]

Then `0` is a convex combination of the switching directions `d_h`.  Ordinary planar Caratheodory gives at most three switching directions whose convex hull contains zero.

If only two distinct diameter directions sufficed, they would have to be antipodal.  That would give two distinct parallel diameter pairs in one projective direction, impossible by the same parallel-diameter uniqueness lemma.  Therefore a nontrivial zero-resultant certificate uses three directions unless the switching set has degenerated to one actual diameter pair with impossible positive zero sum.

This proves part 3.

---

## 5. Interaction with the ordered switching forest

The separate switching-order theorem gives more topology than Theorem TR uses:

- the switching graph is a caterpillar forest;
- if both left- and right-switch orientations occur, all middle endpoints lie on one outer-boundary arc;
- the right-switch endpoints form a prefix and the left-switch endpoints a suffix, with at most one common hub.

Theorem TR says that, despite a possible support of more than one thousand switching edges, the failure of a strict first-order strip translation is already visible in at most three diameter directions, and the exact KKT strip force is generated by at most two switching directions unless the strip resultant vanishes exactly.

This produces a genuinely finite next target: classify the possible one-, two-, and three-edge blocker patterns inside the audited prefix/hub/suffix caterpillar order.

The most promising cases are now explicit:

```text
non-antipodal boundary contacts:
    <=3 ray first-order witness;
    nonzero KKT resultant -> <=2 effective switching directions.

exact antipodal boundary contacts:
    finite obstruction requires two actual switching edges
    with opposite transverse signs.
```

No C-II closure is claimed.  The remaining task is to exclude these few-edge geometric patterns or convert one into a finite same-cardinality replacement.

**Disposition:** proved proof-only three-ray / antipodal-two-edge blocker reduction. C-II and Level I remain open.
