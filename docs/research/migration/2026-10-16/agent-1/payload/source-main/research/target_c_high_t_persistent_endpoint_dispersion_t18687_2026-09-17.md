# Target C-II — persistent high-`t` stress has equivalent endpoint dispersion

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening  
**Scope:** the persistent full-span diameter set in the growing high-`t` cusp chain through `t=(q-k)/D<=1.8687`  
**Dependencies:** persistent-stress plateau theorem; quantitative parallel-diameter uniqueness; canonical C67/DB.3 separation of distinct actual diameter directions  
**Certificate:** `research/verify_target_c_high_t_persistent_endpoint_dispersion_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The persistent-stress theorem leaves three asymptotic regimes according to the persistent KKT mass `p_D` and the normalized cut-resultant magnitude `a_D`. Its exact identity

\[
p_D-a_D={1\over2}\sum_{h\in P_D}\beta_h\|v_h-u_D\|^2
\]

is stated in direction space. This note converts it into source geometry.

For every persistent diameter bar, orient its two physical endpoints `(x_h,y_h)` so that

\[
y_h-x_h=Dv_h,
\qquad |v_h|=1.
\]

Then the weighted angular dispersion of the persistent stress is quantitatively equivalent, up to universal constants, to the weighted Euclidean dispersion of the two endpoint populations. In the coherent positive branch this has a further consequence: all but `o(1)` of the persistent KKT mass is carried by only `o(D)` actual diameter edges, and those stress-carrying edges have their two endpoint classes in two `o(D)`-radius clusters.

Thus PS1 is no longer merely an angular statement. It reduces to an asymptotically single-diameter **stress core**. PS2 and the positive-mass part of PS0, by contrast, retain macroscopic endpoint dispersion.

---

## 1. Finite setup

Fix one source of diameter `D` and its persistent full-span set `P=P_D`. Put

\[
p:=\sum_{h\in P}\beta_h>0,
\qquad
V:=\sum_{h\in P}\beta_h v_h,
\qquad
a:=\|V\|.
\tag{PE.1}
\]

When `a>0`, write `V=a u`; the formulas below do not require choosing `u` when `a=0`.

Define the beta-weighted endpoint barycenters

\[
\bar x:={1\over p}\sum_h\beta_h x_h,
\qquad
\bar y:={1\over p}\sum_h\beta_h y_h.
\tag{PE.2}
\]

The orientation convention immediately gives

\[
\boxed{
\bar y-\bar x={D\over p}V,
\qquad
\|\bar y-\bar x\|=D{a\over p}.
}
\tag{PE.3}
\]

So the ratio `a/p` is exactly the normalized length of the effective segment joining the two endpoint barycenters.

---

## 2. Exact pairwise direction energy

Because every `v_h` is a unit vector,

\[
\begin{aligned}
Q
&:=\sum_{h,k\in P}\beta_h\beta_k\|v_h-v_k\|^2\\
&=\sum_{h,k}\beta_h\beta_k
  \bigl(2-2v_h\cdot v_k\bigr)\\
&=2p^2-2\left\|\sum_h\beta_hv_h\right\|^2.
\end{aligned}
\]

Hence

\[
\boxed{Q=2(p^2-a^2).}
\tag{PE.4}
\]

This is the pairwise form of the one-center variance identity in the persistent-stress theorem.

---

## 3. Diameter geometry transfers direction energy to endpoint energy

For two persistent edges `h,k`, let

\[
z:=x_k-x_h.
\]

The source has diameter `D`, so the two cross-distances satisfy

\[
\|z+Dv_k\|=\|y_k-x_h\|\le D,
\]

\[
\|Dv_h-z\|=\|y_h-x_k\|\le D.
\]

Squaring and adding gives

\[
2\|z\|^2+2D z\cdot(v_k-v_h)\le0.
\]

Equivalently,

\[
\left\|z+{D\over2}(v_k-v_h)\right\|
\le {D\over2}\|v_k-v_h\|.
\tag{PE.5}
\]

Therefore

\[
\boxed{
\|x_h-x_k\|\le D\|v_h-v_k\|,
\qquad
\|y_h-y_k\|\le D\|v_h-v_k\|.
}
\tag{PE.6}
\]

This is the quantitative parallel-diameter inequality, used here with the actual signed orientations supplied by the persistent cut.

There is also a converse estimate at the level needed for second moments. Since

\[
D(v_h-v_k)
=(y_h-y_k)-(x_h-x_k),
\]

we have

\[
D^2\|v_h-v_k\|^2
\le2\bigl(\|x_h-x_k\|^2+\|y_h-y_k\|^2\bigr).
\tag{PE.7}
\]

Define the beta-weighted pairwise endpoint energy

\[
E:=\sum_{h,k}\beta_h\beta_k
\left(\|x_h-x_k\|^2+\|y_h-y_k\|^2\right).
\tag{PE.8}
\]

Equations (PE.6)--(PE.7), summed with weights `beta_h beta_k`, give

\[
{D^2\over2}Q\le E\le2D^2Q.
\]

Using (PE.4),

\[
\boxed{
D^2(p^2-a^2)
\le E
\le4D^2(p^2-a^2).
}
\tag{PE.9}
\]

Thus directional cancellation and endpoint dispersion are quantitatively equivalent for persistent actual diameter bars.

---

## 4. Barycentric endpoint-variance equivalence

For any weighted point family with total weight `p`,

\[
\sum_{h,k}\beta_h\beta_k\|x_h-x_k\|^2
=2p\sum_h\beta_h\|x_h-\bar x\|^2,
\tag{PE.10}
\]

and identically for the `y` endpoints. Therefore

\[
E=2p\sum_h\beta_h
\left(\|x_h-\bar x\|^2+\|y_h-\bar y\|^2\right).
\tag{PE.11}
\]

Normalize by `pD^2` and put

\[
\Sigma
:={1\over pD^2}\sum_h\beta_h
\left(\|x_h-\bar x\|^2+\|y_h-\bar y\|^2\right),
\qquad
\rho:={a\over p}.
\tag{PE.12}
\]

Then (PE.9)--(PE.11) give the finite two-sided estimate

\[
\boxed{
{1\over2}(1-\rho^2)
\le\Sigma
\le2(1-\rho^2).
}
\tag{PE.13}
\]

This is the main conversion theorem. In particular, `rho->1` if and only if the normalized beta-weighted endpoint variance tends to zero.

A useful tail form follows immediately. Let `mu_h=beta_h/p`. For every `eta>0`,

\[
\boxed{
\sum_{h:\ \|x_h-\bar x\|^2+\|y_h-\bar y\|^2\ge\eta^2D^2}
\mu_h
\le {2(1-\rho^2)\over\eta^2}.
}
\tag{PE.14}
\]

No individual multiplier lower bound is used.

Conversely, each endpoint and its corresponding barycenter lie in the convex hull of one diameter-`D` source, so

\[
\|x_h-\bar x\|\le D,
\qquad
\|y_h-\bar y\|\le D.
\tag{PE.15}
\]

Thus the normalized squared product-distance in (PE.12) is at most `2`. Any fixed positive lower bound on `Sigma` therefore forces a fixed positive fraction of the normalized persistent KKT mass to remain at a macroscopic endpoint distance. Explicitly, for `0<tau<Sigma`,

\[
\boxed{
\mu\left\{
{\|x_h-\bar x\|^2+\|y_h-\bar y\|^2\over D^2}\ge\tau
\right\}
\ge {\Sigma-\tau\over2-\tau}.
}
\tag{PE.16}
\]

---

## 5. PS1 compresses to a sublinear actual-diameter stress core

Now return to the coherent positive persistent branch of the growing high-`t` chain. There

\[
p_D\to p>0,
\qquad
a_D\to p,
\qquad
e_D:=p_D-a_D\to0.
\tag{PE.17}
\]

The persistent-stress identity gives, for the common resultant direction `u_D`,

\[
e_D={1\over2}\sum_{h\in P_D}\beta_h\|v_h-u_D\|^2.
\tag{PE.18}
\]

If `e_D=0`, positivity forces every persistent signed direction to equal `u_D`. Canonical C67/DB.3 says distinct actual diameter edges have distinct projective directions, so in that exact case `P_D` contains only one positive-weight edge.

Assume `e_D>0` and put

\[
\theta_D:=e_D^{1/3}.
\tag{PE.19}
\]

Let

\[
K_D:=\{h\in P_D:\angle(v_h,u_D)<\theta_D\}.
\tag{PE.20}
\]

For a direction at angle at least `theta_D`,

\[
\|v_h-u_D\|^2
=4\sin^2(\angle(v_h,u_D)/2)
\ge4\sin^2(\theta_D/2).
\]

Hence (PE.18) gives

\[
\sum_{h\notin K_D}\beta_h
\le {e_D\over2\sin^2(\theta_D/2)}.
\tag{PE.21}
\]

Since `0<theta_D<=1` and `sin(theta/2)>=theta/pi`,

\[
\boxed{
\sum_{h\notin K_D}\beta_h
\le {\pi^2\over2}e_D^{1/3}
=o(1).
}
\tag{PE.22}
\]

So `K_D` carries `p_D-o(1)` persistent KKT mass.

C67/DB.3 gives pairwise projective direction separation

\[
\delta_D=2\arcsin{1\over2D}\ge {1\over D}.
\tag{PE.23}
\]

All projective directions in `K_D` lie in an arc of length at most `2theta_D`. Therefore

\[
\boxed{
|K_D|
\le1+{2\theta_D\over\delta_D}
\le1+2D e_D^{1/3}
=o(D).
}
\tag{PE.24}
\]

This is a support statement, not merely a weighted angular statement.

Finally choose any reference edge `h_* in K_D`, which exists for all sufficiently large `D` because `p_D->p>0` while the discarded mass in (PE.22) tends to zero. Every `h in K_D` has ordinary signed angle at most `2theta_D` from `v_{h_*}`. Equation (PE.6) then gives

\[
\boxed{
\|x_h-x_{h_*}\|,
\|y_h-y_{h_*}\|
\le2D\sin\theta_D
\le2D e_D^{1/3}
=o(D).
}
\tag{PE.25}
\]

Thus in PS1 there are two actual source-point clusters, centered at the endpoints of one persistent diameter edge, with radius `o(D)`, containing the endpoints of an `o(D)`-edge persistent core carrying `p_D-o(1)` KKT mass.

The exponent `1/3` is only a balanced choice: a cone radius `e_D^alpha`, `0<alpha<1/2`, gives core cardinality `O(D e_D^alpha)` and discarded mass `O(e_D^{1-2alpha})`.

---

## 6. The three stress regimes become three endpoint regimes

Write `rho_D=a_D/p_D` whenever `p_D>0`.

### PE0 — vanishing resultant with positive persistent mass

If `a_D->0` while `p_D->p>0`, then `rho_D->0`. Equation (PE.13) gives

\[
\boxed{\liminf\Sigma_D\ge {1\over2}.}
\tag{PE.26}
\]

So a positive persistent mass cannot cancel to zero while its two endpoint populations collapse into submacroscopic clusters. Persistent directional cancellation requires macroscopic endpoint dispersion.

If `p_D->0`, there is no positive persistent mass to which this normalization applies; that is the separate PS0 subcase already isolated by the parent theorem.

### PE1 — coherent positive plateau

If `0<a=p`, then `rho_D->1`. Hence

\[
\boxed{\Sigma_D\to0,}
\tag{PE.27}
\]

and (PE.22)--(PE.25) strengthen this to the actual-edge stress core

```text
p_D-o(1) persistent KKT mass
+
o(D) persistent actual diameter edges
+
two o(D)-radius endpoint clusters
+
cluster centers are themselves the endpoints of one actual diameter edge.
```

### PE2 — dispersed positive plateau

If `0<a<p`, then

\[
\rho_D\to{a\over p}<1.
\]

Equation (PE.13) gives

\[
\boxed{
\liminf\Sigma_D
\ge {1\over2}\left(1-{a^2\over p^2}\right)>0.
}
\tag{PE.28}
\]

Thus the positive angular-variance currency of PS2 is automatically a positive macroscopic endpoint-dispersion currency. By (PE.16), a fixed positive fraction of the normalized persistent KKT mass must remain a fixed positive fraction of `D` away from the endpoint barycenter pair.

---

## 7. Interaction with the uniform-cusp chain

The high-`t` survivor now has a sharper positive-plateau fork.

In PE1, more than `r_D/2` uniformly finite cusp reactions use pairwise disjoint fresh switching supports of total KKT mass `o(1)`, while the macroscopic persistent resultant is carried, up to `o(1)` stress mass, by an `o(D)` family of almost coincident actual diameter edges whose endpoints live in two `o(D)` source clusters.

In PE2, the persistent stress cannot be spatially localized: its beta-weighted endpoint variance is `Theta(D^2)` after normalization by its positive mass. This gives a direct endpoint quantity to charge against the force-hull/perimeter and high-`t` rectangle currencies, rather than an abstract angular variance.

In the positive-mass PE0 branch, the cancellation is even more spatially spread by (PE.26).

This is genuine progress but not a closure. The remaining PE1 target is now a compatibility theorem between

1. an asymptotically two-cluster, sublinear persistent diameter stress core crossing every selected row; and
2. an unbounded family of uniformly finite fresh cusp reactions embedded in the same linear near-triangular ladder.

For PE2/positive-mass PE0, the target is to charge the quantitative endpoint dispersion from (PE.28)/(PE.26) against existing global endpoint, perimeter, or cell-angle budgets.

---

## 8. Scope audit

- The endpoint orientation is the signed orientation already used in the persistent cut resultant. No projective reorientation is made inside the pairwise identities.
- The upper endpoint estimate (PE.6) uses only the diameter bound on the two cross-distances; it is valid for these signed orientations.
- The lower estimate (PE.7) is only the triangle inequality applied to the difference of the two diameter displacement vectors.
- `bar x,bar y` are weighted barycenters, not necessarily source points. The PE1 cluster centers in (PE.25), however, are actual source points because they are endpoints of the reference diameter edge `h_*`.
- PE1 gives `o(D)` cluster radii, not `O(1)` radii. No convergence rate for `e_D=p_D-a_D` is available.
- No lower bound on an individual KKT multiplier is assumed or proved.
- The `o(D)` edge-count conclusion uses the canonical C67/DB.3 direction-separation theorem in addition to stress coherence.
- None of PE0/PE1/PE2 alone produces an exact unit triangle or a strict sub-`D` competitor.

**Disposition:** proved a finite two-sided equivalence between persistent stress-direction variance and persistent endpoint variance, and strengthened PS1 to an `o(D)` actual-diameter stress core with two `o(D)` endpoint clusters carrying all but `o(1)` of the persistent KKT mass. C-II and Level I remain open.
