> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_sparse_cusp_certificate_2026-09-15.md) · source SHA-256 `2dd8104171f40abaa9c0a4f9d3b89b1a4f15308b1435a2d7c2fd3f32a5efd453`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ef2c3cdff4a0df12db0c7307639f4fd5d4598945", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_sparse_cusp_certificate_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "16d82984012cfd16b68ef0cb23023d7750e92d503f15ed4ee0a109d2ecc057e7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — sparse three-row certificate for a two-cut diameter cusp

**Date:** 2026-09-15  
**Status:** proof-only exact source-level structural theorem  
**Scope:** any two complete outer-to-outer stopped trains in the full-core Type-II normalized source; phase-close corollary for the audited adjacent-cut backbone  
**Dependencies:** exact arbitrary O--O finite multishear; relative-interior positive KKT stress; response-free O--O cut resultants; parallel-diameter uniqueness  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The adjacent-cut finite-cusp theorem bounds the number of diameter rows whose support
changes between two neighboring O--O cuts.  First-order stationarity is much sparser
than that full exceptional set suggests.

For **any two** O--O train-shear coordinates, the positive KKT stress writes zero as a
positive combination of their active-diameter gradient vectors.  Since those gradients
live in `R^2`, Carathéodory reduces the entire first-order diameter cusp to at most
three actual diameter rows.

This is a first-order certificate only.  It does not delete the remaining active
rows from the finite nonlinear max problem and does not claim that a global KKT stress
can be supported on three diameter pairs.

---

## 1. Two-cut shear gradients

Let `tau_1,tau_2` be two complete O--O trains.  Use the audited exact multishear shore
splits and contact vectors `u_1,u_2`.  For an arbitrarily oriented actual diameter pair

$$
h=xy,
\qquad
r_h=p_y-p_x,
\qquad |r_h|=D,
$$

put

$$
\sigma_{hi}
=\mathbf 1_{S_i}(y)-\mathbf 1_{S_i}(x)
\in\{-1,0,1\}.
$$

Under the exact two-coordinate placement,

$$
r_h(\theta_1,\theta_2)
=r_h+
\sigma_{h1}(R_{\theta_1}u_1-u_1)
+
\sigma_{h2}(R_{\theta_2}u_2-u_2).
\tag{SC.1}
$$

Therefore the gradient at the original source of the squared diameter-row length is

$$
\boxed{
g_h
:=\nabla_{\theta}|r_h(\theta)|^2\big|_{0}
=
2\bigl(
\sigma_{h1}r_h\cdot Ju_1,
\sigma_{h2}r_h\cdot Ju_2
\bigr)
\in\mathbb R^2.
}
\tag{SC.2}
$$

Rows with `sigma_h1=sigma_h2=0` are unchanged by the two-cut multishear and have
`g_h=0`.  A row crossing at least one selected cut will be called **visible**.

---

## 2. Positive KKT stationarity in the shear plane

Let `beta_h>0` be a relative-interior normalized KKT diameter stress.  For cut `i`,
the response-free KKT resultant is

$$
A_i u_i
=\sum_h\beta_h\sigma_{hi}r_h,
\qquad A_i>0.
\tag{SC.3}
$$

Dot (SC.3) with `Ju_i`:

$$
\sum_h\beta_h\sigma_{hi}r_h\cdot Ju_i=0.
\tag{SC.4}
$$

Using (SC.2) in both coordinates gives the exact vector identity

$$
\boxed{
\sum_{h\in H}\beta_h g_h=0.
}
\tag{SC.5}
$$

This is KKT stationarity restricted to the exact two-train contact-preserving shear
plane.  No response inequality and no inactive-distance slack estimate is used.

Section 157 gives, for each O--O cut, crossing diameter rows with both signs of
`r_h dot Ju_i`.  Hence at least one visible row has nonzero gradient.  Let

$$
H_*:=\{h\in H:g_h\ne0\}.
$$

All rows outside `H_*` contribute zero to (SC.5).  Since every `beta_h` is positive,

$$
B_*:=\sum_{h\in H_*}\beta_h>0.
$$

Normalize

$$
\lambda_h={\beta_h\over B_*}
\qquad(h\in H_*).
$$

Then

$$
\lambda_h>0,
\qquad
\sum_{h\in H_*}\lambda_h=1,
\qquad
\sum_{h\in H_*}\lambda_h g_h=0.
\tag{SC.6}
$$

Thus

$$
\boxed{0\in\operatorname{conv}\{g_h:h\in H_*\}.}
\tag{SC.7}
$$

---

## 3. Carathéodory leaves at most three actual diameter rows

Carathéodory's theorem in `R^2` applied to (SC.7) gives a subset

$$
\{h_1,\ldots,h_k\}\subseteq H_*,
\qquad
2\le k\le3,
$$

and coefficients

$$
\mu_j>0,
\qquad
\sum_{j=1}^k\mu_j=1,
$$

such that

$$
\boxed{
\sum_{j=1}^k\mu_j g_{h_j}=0.
}
\tag{SC.8}
$$

Positivity of all displayed coefficients is obtained by choosing an inclusion-minimal
Carathéodory subset.  A one-row subset is impossible because every chosen gradient is
nonzero.

Hence:

### Theorem SC.1 — sparse first-order cusp certificate

For every pair of O--O train-shear coordinates in the normalized full-core source,
first-order KKT stationarity of all actual diameter rows has a certificate using only
**two or three actual diameter pairs**.

If `k=2`, the two nonzero gradient vectors are exactly antiparallel.  If `k=3`, the
origin lies in the relative interior of their gradient triangle.

The theorem does **not** say that the original KKT multiplier vector vanishes outside
these rows.  The `mu_j` are a new two-dimensional convex certificate, not a replacement
full equilibrium stress.

---

## 4. Visible tangent rows are separately rigid

A visible row can have `g_h=0`, but such a row is strongly constrained.

If

$$
\sigma_{hi}\ne0
$$

and `g_h=0`, then

$$
r_h\cdot Ju_i=0,
$$

so the diameter segment is projectively parallel to the train contact direction
`u_i`.

A diameter-bounded planar set contains at most one unordered diameter segment in any
projective direction.  Therefore, for each selected train direction, there is at most
one such tangent visible diameter row.

If a row crosses **both** selected cuts and `u_1,u_2` are not projectively parallel,
then `g_h=0` would force the nonzero vector `r_h` to be parallel to two distinct
projective directions, which is impossible.  Thus a doubly visible tangent row can
exist only when the two train directions are exactly projectively equal, and then it is
the unique diameter segment in that direction.

These tangent rows do not enter the nonzero-gradient Carathéodory certificate (SC.8),
but they are the only first-order-flat visible diameter rows that a higher-order local
analysis must treat separately.

---

## 5. Adjacent phase-close row types

Apply the theorem to the audited adjacent same-phase O--O pair from the balanced
triple-small theorem.  Choose

$$
s\in\{+1,-1\}
$$

so that

$$
|u_1-su_2|
\le d_{\mathbb{RP}^1}(u_1,u_2)
< {21200\over D}+o(D^{-1}).
\tag{SC.9}
$$

Use transformed shear coordinates

$$
(\theta_1,\eta_2),
\qquad
\eta_2=s\theta_2,
$$

and correspondingly write

$$
\widetilde g_h=(g_{h,1},s g_{h,2}).
$$

For a diameter row spanning both adjacent path cuts, the interval-support orientation
has

$$
\sigma_{h1}=\sigma_{h2}=\varepsilon_h\in\{+1,-1\}.
$$

Hence

\[
\begin{aligned}
|\widetilde g_{h,1}-\widetilde g_{h,2}|
&=2|r_h\cdot J(u_1-su_2)|\\
&\le2D|u_1-su_2|\\
&<42400+o(1).
\end{aligned}
\tag{SC.10}

Thus every spanning gradient lies in a fixed-width diagonal strip.

A switching row has exactly one nonzero split incidence, so its transformed gradient
lies on one coordinate axis:

\[
(a,0)
\quad\text{or}\quad
(0,b).
\tag{SC.11}

Consequently the sparse certificate (SC.8) for the live adjacent pair uses at most
three vectors, each belonging to the explicit union

```text
horizontal axis
union vertical axis
union { (a,b): |a-b| < 42400+o(1) }.
```

The `<1800` Pareto theorem can separately be used when one needs a bound on the total
number of switching rows.  The present theorem instead says that only two or three
actual rows are needed to certify first-order KKT balance in the two-cut shear plane.

---

## 6. Why this does not yet close the cusp

The reduction is first-order.  Other active diameter rows still exist and can obstruct
a finite nonlinear move even though they are unnecessary for the convex stationarity
certificate.  In particular:

- a tangent visible row has zero first derivative and can be a second-order blocker;
- rows outside the sparse certificate can become maximal away from the origin;
- the merged inactive-slack repair still forbids treating a prescribed `1/D` shear as
  a uniformly feasible full-source move without additional lower-distance control.

What has changed is the finite classification target.  At the first-order level the
adjacent-cut cusp is not an arbitrary `<1800`-row balance.  It is one of three small
geometric types:

1. two antiparallel nonzero diameter gradients;
2. three nonzero diameter gradients whose triangle contains the origin; or
3. either of the above together with at most one tangent diameter row per selected
   projective train direction.

These rows are actual edges of the convex diameter thrackle.  A next closing theorem
can therefore combine this sparse gradient geometry with the finite convex-thrackle
patterns, rather than classify all switching rows at once.

**Disposition:** proved proof-only sparse first-order cusp certificate. C-II and Level I
remain open.
