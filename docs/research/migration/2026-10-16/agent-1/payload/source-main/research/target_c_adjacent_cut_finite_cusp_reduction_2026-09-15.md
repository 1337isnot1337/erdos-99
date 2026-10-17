# Target C-II — the triple-small adjacent pair reduces opposite shear to finitely many large first-order diameter rows

**Date:** 2026-09-15  
**Status:** proof-only finite/source-level reduction  
**Scope:** the adjacent pair supplied by `target_c_adjacent_cut_triple_small_2026-09-15.md`  
**Dependencies:** exact arbitrary O--O finite multishear; exact laminar interval support; triple-small adjacent-pair theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The triple-small theorem produces consecutive outer-to-outer cuts `tau_i,tau_{i+1}` with projective train-direction gap `O(D^{-1})` and at most `O(1)` actual diameter rows whose interval incidence changes between the two cuts.

The newly merged exact finite multishear theorem lets us use the two train coordinates at finite amplitude.  Choosing opposite coefficients, with the sign adjusted for the projective orientation, cancels the first-order motion of every diameter row spanning both cuts up to the inverse-`D` phase error.

This gives a clean finite-cusp normal form.

### Theorem FC — finite large-derivative cusp set

For every sufficiently large member of the live `t<=1.844` branch there are consecutive smallest-leaf O--O cuts `tau,tau'`, unit contact vectors `u,u'`, and a sign

\[
s\in\{+1,-1\}
\]

such that

\[
\boxed{|u-su'|<{21200\over D}+o(D^{-1}),}
\tag{FC.1}

and the exact two-coordinate contact-preserving multishear with scalar direction

\[
(\theta_\tau,\theta_{\tau'})=(t,-s t)
\tag{FC.2}

has the following active-diameter first derivatives at `t=0`:

1. at most `21200+o(1)` actual diameter rows have derivative of the natural `O(D)` scale;
2. every other actual diameter row has
   \[
   \boxed{
   \left|{d\over dt}|r_h(t)|^2\Big|_{0}\right|
   <42400+o(1);
   }
   \tag{FC.3}
   \]
3. the total KKT multiplier of the `O(D)` rows is
   \[
   \boxed{< {21200\over D}+o(D^{-1});}
   \tag{FC.4}
   \]
4. consequently their KKT-weighted total absolute first-derivative contribution is less than
   \[
   \boxed{42400+o(1).}
   \tag{FC.5}

For a finite amplitude scaled as

\[
t={\xi\over D}
\]

with fixed `xi`, every non-switching actual diameter squared length changes by `O(D^{-1})`, uniformly, while only the bounded switching set can change by `O(1)`.

Thus the live adjacent-pair obstruction to a finite opposite shear is reduced to a bounded set of diameter max-function cusps.  No claim is made that these cusps can yet be assigned a common decreasing sign.

---

## 1. Choose the projective sign before choosing the opposite shear

The triple-small theorem gives projective angle

\[
\eta=d_{\mathbb{RP}^1}(u,u')
<{21200\over D}+o(D^{-1}).
\tag{FC.6}

Choose `s in {+1,-1}` so that the ordinary oriented angle between `u` and `s u'` equals `eta`.  Then

\[
|u-su'|=2\sin(\eta/2)\le\eta,
\]

which proves (FC.1).

Use the exact finite multishear with coefficients

\[
c_\tau=1,
\qquad
c_{\tau'}=-s.
\tag{FC.7}

The sign choice avoids any unsupported assumption that the nested shore orientation makes the two unit contact vectors point in the same Euclidean direction.

---

## 2. Laminar interval support gives only three row types

For consecutive cuts on one laminar path, an actual diameter interval can meet the pair in exactly one of three ways:

1. neither cut;
2. both cuts; or
3. exactly one cut.

Rows of type 3 are precisely the diameter edges whose incidence changes at the internal boundary between `tau` and `tau'`.  The triple-small theorem gives

\[
\boxed{\#\{\text{type-3 rows}\}<21200+o(1),}
\tag{FC.8}

and normalized KKT multiplier sum

\[
\boxed{
\sum_{h\text{ type 3}}\beta_h
<{21200\over D}+o(D^{-1}).
}
\tag{FC.9}

For the exact multishear, the first relative-displacement coefficient of a diameter row is

\[
A_h=\sum_{j\in I_h}c_jJu_j.
\tag{FC.10}

A type-1 row has `A_h=0`.

A type-2 row has

\[
A_h=J(u-su'),
\]

so by (FC.1)

\[
|A_h|<{21200\over D}+o(D^{-1}).
\tag{FC.11}

A type-3 row has either `A_h=Ju` or `A_h=-sJu'`, hence

\[
|A_h|=1.
\tag{FC.12}

---

## 3. First squared-length derivatives

Every active diameter vector has length `D`.  The exact multishear derivative is

\[
{d\over dt}|r_h(t)|^2\Big|_0
=2r_h\cdot A_h.
\tag{FC.13}

For type 1 it vanishes.

For type 2, (FC.11) gives

\[
\left|2r_h\cdot A_h\right|
\le2D|A_h|
<42400+o(1),
\]

which proves (FC.3) for every non-switching row.

For type 3 the coarse bound is

\[
|2r_h\cdot A_h|\le2D.
\tag{FC.14}

There are only the bounded number (FC.8) of such rows.  Multiplying (FC.14) by the positive KKT weights and using (FC.9),

\[
\sum_{h\text{ type 3}}
\beta_h
\left|{d\over dt}|r_h(t)|^2\Big|_0\right|
\le
2D\sum_{h\text{ type 3}}\beta_h
<42400+o(1).
\]

This proves (FC.4)--(FC.5).

---

## 4. Finite amplitude `t=xi/D`

The exact multishear expansion for one active diameter row is

\[
|r_h(t)|^2
=D^2+2t\,r_h\cdot A_h
+t^2\bigl(|A_h|^2-r_h\cdot B_h\bigr)
+O(t^3),
\tag{FC.15}

where

\[
B_h=\sum_{j\in I_h}c_j^2u_j.
\]

For the present two coordinates, uniformly for every row,

\[
|B_h|\le2.
\tag{FC.16}

Take `t=xi/D` with fixed `xi`.

For a type-2 row, the linear term is `O(D^{-1})` by (FC.3), while

\[
t^2\bigl(|A_h|^2-r_h\cdot B_h\bigr)
=O(D^{-1}).
\]

The exact trigonometric multishear formula makes the omitted remainder `O(D^{-2})` uniformly for fixed `xi`.

Thus every type-2 diameter squared length changes by

\[
O(D^{-1}).
\tag{FC.17}

Type-1 rows are unchanged exactly.  A type-3 row can have an `O(1)` linear change under this scaling, but there are at most `21200+o(1)` such rows.

---

## 5. Why this is the correct current obstruction

KKT stationarity forbids treating the small total multiplier of the switching rows as if they were absent from the max constraint.  A diameter edge with tiny positive multiplier is still an exact active upper-distance constraint.

The present theorem therefore does **not** infer a diameter-decreasing direction from (FC.4).  What it proves is the stronger normal form needed for a finite blocker analysis:

```text
exact two-cut contact-preserving finite motion
+ all but O(1) diameter rows have only O(1) first derivative
+ after t=O(1/D), all but O(1) diameter rows move only o(1) in squared length
+ the O(1) exceptional rows have total beta mass O(1/D).
```

A closure now needs a genuine theorem about that finite switching set: a thrackle sign restriction, a local endpoint exchange, or enough additional adjacent shear coordinates to satisfy its finitely many cusp inequalities.  Merely averaging by KKT multiplier is insufficient.

**Disposition:** proved proof-only finite-cusp reduction. C-II and Level I remain open.
