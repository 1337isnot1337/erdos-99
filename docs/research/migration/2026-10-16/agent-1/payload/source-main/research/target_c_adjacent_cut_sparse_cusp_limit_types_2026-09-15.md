# Target C-II — three asymptotic hard-cusp types for adjacent phase-close cuts

**Date:** 2026-09-15  
**Status:** proof-only asymptotic structural theorem  
**Scope:** the audited adjacent same-phase O--O pair and the sparse two/three-row cusp certificate  
**Dependencies:** `target_c_adjacent_cut_sparse_cusp_certificate_2026-09-15.md`; balanced triple-small inverse-`D` phase gap; laminar interval support  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The sparse-cusp theorem reduces first-order KKT balance in the two-cut shear plane to
at most three nonzero diameter-row gradients.  The adjacent train directions differ by
only `O(D^{-1})` projectively.  Consequently any sparse cusp whose effective slopes
grow without bound has only three possible leading-order geometries.

After passing to a subsequence, a hard cusp is one of:

1. **spanning antipodal pair:** two diameter rows spanning both cuts, with opposite
   leading transverse derivatives;
2. **single-boundary antipodal pair:** two switching rows on the same cut, with
   opposite leading transverse derivatives; or
3. **one-plus-two mixed triangle:** one spanning diameter row and one switching row at
   each of the two boundaries, with both switching signs opposite the spanning sign.

Every other three-row combination degenerates to one of the two-row cases or requires
all effective slopes to remain bounded.

This converts the first-order hard cusp from an arbitrary finite diameter-thrackle
pattern into three explicit local patterns.

---

## 1. Transformed coordinates

Let `tau_1,tau_2` be the adjacent O--O pair from the balanced triple-small theorem.
Choose

\[
s\in\{+1,-1\}
\]

so that

\[
|u_1-su_2|
<{21200\over D}+o(D^{-1}).
\tag{LT.1}
\]

For an actual diameter row `h`, let

\[
g_h=(g_{h1},g_{h2})
\]

be its two-cut squared-length gradient from the sparse-cusp theorem.  Use transformed
coordinates

\[
\widetilde g_h=(g_{h1},s g_{h2}).
\tag{LT.2}
\]

For a row spanning both adjacent path cuts, interval support gives the same split sign
on both coordinates.  Therefore

\[
\boxed{
|\widetilde g_{h1}-\widetilde g_{h2}|
<42400+o(1).
}
\tag{LT.3}
\]

For a switching row, exactly one split incidence is nonzero, so

\[
\widetilde g_h=(a,0)
\quad\text{or}\quad
(0,b).
\tag{LT.4}
\]

Rows invisible to both cuts have zero gradient and never appear in the sparse nonzero
certificate.

---

## 2. Sparse certificate and hard/soft dichotomy

For every source in the survivor sequence, choose an inclusion-minimal sparse
certificate

\[
\sum_{j=1}^{k_D}\mu_{j,D}\widetilde g_{j,D}=0,
\qquad
2\le k_D\le3,
\qquad
\mu_{j,D}>0,
\qquad
\sum_j\mu_{j,D}=1.
\tag{LT.5}
\]

Put

\[
M_D:=\max_j|\widetilde g_{j,D}|.
\tag{LT.6}
\]

There are two regimes.

### Soft sparse cusp

If `M_D=O(1)` along a subsequence, then every diameter row needed to certify
first-order KKT balance has bounded squared-length derivative despite the diameter
scale `D`.  This is already a stronger localization than the full active set and is
left as a separate branch.

### Hard sparse cusp

Assume instead

\[
M_D\to\infty.
\tag{LT.7}
\]

Normalize

\[
v_{j,D}:={\widetilde g_{j,D}\over M_D}.
\]

After passing to a subsequence, all `v_{j,D}` and all `mu_{j,D}` converge.  Remove any
indices whose limiting coefficient is zero, and then remove any zero limiting vectors
that do not affect the limiting balance.  The remaining limiting certificate is
inclusion-minimal, has positive coefficients, and contains at least two nonzero
vectors.

Equation (LT.3) divided by `M_D` shows that every spanning-row limit lies on the
**diagonal line**

\[
L_d=\{(x,x):x\in\mathbb R\}.
\tag{LT.8}
\]

Every switching-row limit lies on one of the coordinate axes

\[
L_x=\{(x,0)\},
\qquad
L_y=\{(0,y)\}.
\tag{LT.9}
\]

Thus the limiting positive convex certificate has at most three nonzero vectors in

\[
L_d\cup L_x\cup L_y.
\tag{LT.10}

The rest is an elementary finite classification.

---

## 3. Two-vector certificates

Two nonzero vectors with positive coefficients sum to zero if and only if they are
antiparallel.

A nonzero diagonal vector cannot be antiparallel to a nonzero axis vector.  A nonzero
horizontal vector cannot be antiparallel to a nonzero vertical vector.

Therefore every two-vector hard certificate is exactly one of:

### Type D2 — spanning antipodal pair

\[
(a,a),
\qquad
(-b,-b),
\qquad a,b>0.
\tag{LT.11}
\]

Both certificate rows span the two adjacent cuts and have opposite leading transverse
signs.

### Type X2/Y2 — one-boundary antipodal pair

\[
(a,0),
\qquad
(-b,0),
\tag{LT.12}
\]

or the vertical analogue, with `a,b>0`.

Both certificate rows switch at the same boundary and have opposite leading
transverse signs.

No other two-row hard type exists.

---

## 4. Three-vector certificates

Consider an inclusion-minimal positive three-vector certificate.

### Three diagonal vectors

They are collinear.  If their convex hull contains zero, two of them already have zero
in their convex hull.  This contradicts inclusion minimality.

### Three axis vectors

If both coordinate axes occur, then whichever axis occurs only once contributes the
only nonzero entry in that coordinate and cannot be canceled.  If only one axis
occurs, the vectors are collinear and again reduce to a two-vector certificate.

Thus no inclusion-minimal three-axis certificate exists.

### Two diagonal vectors and one axis vector

Suppose the axis is horizontal.  Write

\[
\lambda_1(a,a)+\lambda_2(b,b)+\lambda_3(c,0)=0
\]

with all coefficients positive and `c ne0`.  The second coordinate gives

\[
\lambda_1a+\lambda_2b=0.
\]

Substitution into the first coordinate leaves

\[
\lambda_3c=0,
\]

impossible.  The vertical case is identical.

### One diagonal vector and two vectors on the same axis

The coordinate perpendicular to that axis receives a contribution only from the
nonzero diagonal vector, so it cannot vanish.  Impossible.

### One diagonal, one horizontal, one vertical

This is the only remaining possibility.  Write

\[
\lambda_d(a,a)
+\lambda_x(b,0)
+\lambda_y(0,c)=0.
\tag{LT.13}
\]

All coefficients are positive and all three vectors are nonzero.  Therefore

\[
\lambda_x b=-\lambda_d a,
\qquad
\lambda_y c=-\lambda_d a.
\tag{LT.14}
\]

Hence `b` and `c` have the sign opposite to `a`.

This gives:

### Type DXY3 — mixed spanning/switch triangle

One certificate row spans both cuts.  One switches only at the first boundary and one
switches only at the second boundary.  The two switching transverse derivatives have
the same leading sign, opposite to the leading sign of the spanning row.

No other inclusion-minimal three-row hard type exists.

---

## 5. Geometric interpretation

For a diameter row crossing a selected cut,

\[
{g_{hi}\over2D}
=\sigma_{hi}\,{r_h\over D}\cdot Ju_i
\]

is its signed transverse sine relative to the train contact direction.

Thus the three hard types have a direct diameter-thrackle interpretation:

- **D2:** two actual diameter chords crossing both adjacent cuts with opposite
  transverse orientation;
- **X2/Y2:** two actual diameter chords entering/leaving at the same dual boundary with
  opposite transverse orientation;
- **DXY3:** one spanning diameter chord together with one switching chord at each end
  of the intervening strip; both switching chords have transverse sign opposite the
  spanning chord.

All certificate rows are actual edges of the convex diameter thrackle.  The next
structural obligation can therefore be posed as a finite geometry problem for these
three patterns.

---

## 6. Scope and non-conclusions

- The theorem classifies only the **leading-order first-order certificate** after
  normalizing by its own largest gradient scale `M_D`.
- If `M_D=O(1)`, the soft sparse-cusp branch remains and is not folded into the three
  hard types.
- Other active diameter rows can still obstruct a nonlinear finite move even though
  they are not needed in the sparse first-order certificate.
- The result uses no prescribed `1/D` deformation amplitude and is unaffected by the
  inactive-slack repair.
- No lower bound on the KKT multiplier of any certificate row is obtained.

**Disposition:** proved proof-only hard-cusp classification.  C-II and Level I remain
open.
