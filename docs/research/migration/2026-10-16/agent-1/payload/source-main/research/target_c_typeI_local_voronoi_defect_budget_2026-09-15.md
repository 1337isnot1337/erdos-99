# Target C-II — every deep Type-I ball has only boundary-order Voronoi defect

**Date:** 2026-09-15  
**Status:** proof-only local stability strengthening for the Type-I macroscopic-container branch  
**Scope:** either audited Type-I inactive container  
**Dependencies:** `target_c_typeI_local_hall_density_2026-09-15.md`; canonical unit covering of the depth-one container; Mazel--Stuhl--Suhov minimal Voronoi-cell theorem  
**External theorem:** A. Mazel, I. Stuhl, Y. Suhov, *Minimal Area of a Voronoi Cell in a Packing of Unit Circles*, arXiv:2211.03255 (2022)  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The local Hall theorem forces triangular-density population in every protected Type-I ball.  There is a matching local **geometric defect budget**.

Let `C` be one audited Type-I macroscopic inactive container and `Z` its assigned contact-isolated source population.  Write

\[
a_0={\sqrt3\over2}.
\]

For `z in Z`, let `V_z` denote its ordinary Euclidean Voronoi cell with respect to the finite point set `Z`.

The external Voronoi theorem of Mazel--Stuhl--Suhov states, after scaling their minimum center distance `2` normalization down by a factor `2`, that every bounded Voronoi cell in a point packing of minimum distance at least one has area at least

\[
\boxed{a_0={\sqrt3\over2}.}
\tag{VD.1}
\]

Equality occurs only for the perfect regular hexagonal cell, equivalently when the corresponding six neighboring centers form the unit regular hexagon.  Since the canonical set `Z` is contact-isolated in the full source, every pair of distinct points of `Z` has distance **strictly** greater than one.  Thus every bounded `V_z` in the present setting satisfies

\[
\boxed{|V_z|>a_0.}
\tag{VD.2}
\]

The main theorem below shows that the sum of these positive defects is nevertheless only boundary order in every deep ball.

---

## Theorem VD — local Voronoi defect budget

Let `r>1` and choose

\[
x\in C_{-(r+2)}.
\]

Put

\[
Z_r:=Z\cap\overline B(x,r),
\qquad
N_r:=|Z_r|,
\]

and for `z in Z_r` define

\[
\delta_z:=|V_z|-a_0.
\]

Then:

1. every `V_z`, `z in Z_r`, is bounded and satisfies
   \[
   \boxed{V_z\subseteq\overline B(z,1)\subseteq\overline B(x,r+1);}
   \tag{VD.3}
   \]
2. the local Hall theorem gives
   \[
   \boxed{
   N_r\ge {\pi(r-1)^2\over a_0};
   }
   \tag{VD.4}
   \]
3. every defect is positive, and their total satisfies
   \[
   \boxed{
   0<\sum_{z\in Z_r}\delta_z\le4\pi r.
   }
   \tag{VD.5}
   \]

Consequently, for every `eta>0`,

\[
\boxed{
\#\{z\in Z_r:\delta_z\ge\eta\}
\le {4\pi r\over\eta}.
}
\tag{VD.6}
\]

In particular, putting

\[
\eta_r:={8a_0r\over(r-1)^2},
\tag{VD.7}
\]

at least half of the centers in `Z_r` have

\[
\boxed{
|V_z|\le a_0+\eta_r
=a_0+O(r^{-1}).
}
\tag{VD.8}
\]

Thus every protected mesoscopic Type-I ball contains `Theta(r^2)` Voronoi cells whose average area defect from the triangular-lattice cell is `O(1/r)`; only boundary-order total defect is available.

---

## 1. A deep isolate has covering radius at most one in its full Voronoi cell

Canonical Type-I exchange saturation gives the exact unit covering

\[
C_{-1}
\subseteq
\bigcup_{w\in Z}\overline B(w,1).
\tag{VD.9}
\]

Fix

\[
z\in Z_r.
\]

Because `x in C_{-(r+2)}` and `|z-x|<=r`,

\[
\operatorname{dist}(z,\partial C)>2.
\tag{VD.10}
\]

Suppose for contradiction that there is

\[
p\in V_z,
\qquad |p-z|>1.
\]

The Voronoi cell `V_z` is convex and contains its center `z`.  Choose a point `q` on the segment `[z,p]` with

\[
1<|q-z|<
\min\{|p-z|,\operatorname{dist}(z,\partial C)-1\}.
\tag{VD.11}
\]

Then `q in V_z` by convexity, while (VD.10)--(VD.11) give

\[
q\in C_{-1}.
\]

By (VD.9), some `w in Z` satisfies

\[
|q-w|\le1<|q-z|,
\]

contradicting `q in V_z`.

Therefore

\[
V_z\subseteq\overline B(z,1).
\]

This proves the first containment in (VD.3); the second follows from `|z-x|<=r`.  In particular `V_z` is bounded, so the scaled Mazel--Stuhl--Suhov theorem applies.

---

## 2. Hall density supplies the interior-center count

Apply the exact local Hall inequality to the closed ball

\[
E:=\overline B(x,r-1).
\]

Since `x in C_{-(r+2)}`, certainly

\[
E\subset C_{-1}.
\]

The Hall neighborhood satisfies

\[
N_Z(E)
\subseteq
Z\cap\overline B(x,r)=Z_r.
\]

Hence

\[
\pi(r-1)^2
=\operatorname{area}E
\le a_0|N_Z(E)|
\le a_0N_r.
\]

This proves (VD.4).

---

## 3. Sum the disjoint Voronoi cells

Distinct ordinary Voronoi cells have disjoint interiors.  By (VD.3), every `V_z` with `z in Z_r` lies inside the same radius-`r+1` disk.  Therefore

\[
\sum_{z\in Z_r}|V_z|
\le
\pi(r+1)^2.
\tag{VD.12}
\]

The scaled Mazel--Stuhl--Suhov theorem gives

\[
|V_z|\ge a_0.
\]

Moreover equality would force six Voronoi-neighbor centers at exact unit distance from `z`.  This is impossible because `Z` consists of actual contact isolates, so every distinct pair in `Z` has distance strictly greater than one.  Hence

\[
\delta_z>0.
\tag{VD.13}
\]

Now use (VD.4):

\[
\begin{aligned}
\sum_{z\in Z_r}\delta_z
&=
\sum_{z\in Z_r}|V_z|-a_0N_r\\
&\le
\pi(r+1)^2-\pi(r-1)^2\\
&=4\pi r.
\end{aligned}
\]

This proves (VD.5).

Equation (VD.6) is Markov's inequality applied to the nonnegative defects.  For (VD.8), (VD.4) and (VD.7) give

\[
{4\pi r\over\eta_r}
={\pi(r-1)^2\over2a_0}
\le {N_r\over2}.
\]

Therefore at most half of `Z_r` have defect at least `eta_r`, so at least half satisfy (VD.8). `square`

---

## 4. Equality stability becomes a local phase problem

The external theorem has a unique equality class: the perfect regular hexagonal Voronoi cell.  Standard compactness therefore gives the following qualitative corollary.

Fix `eps>0`.  Among bounded Voronoi cells of minimum-distance-one point packings which are contained in the unit disk about their center, there is a number

\[
\delta_{hex}(\varepsilon)>0
\]

such that

\[
|V_z|<a_0+\delta_{hex}(\varepsilon)
\]

forces `V_z`, after a rotation about `z`, to lie within Hausdorff distance `eps` of the regular hexagonal equality cell.

Indeed, otherwise a sequence of counterexample cells has a Hausdorff-convergent subsequence inside the unit disk.  The limiting cell still comes from a minimum-distance-one limiting packing locally, has area `a_0`, and is therefore the unique regular hexagonal equality cell by Mazel--Stuhl--Suhov.

Combining this qualitative modulus with (VD.6) shows:

\[
\boxed{
\text{for each fixed }\varepsilon>0,
\text{ all but }O_\varepsilon(r)
\text{ cells in }Z_r
\text{ are }\varepsilon\text{-hexagonal.}
}
\tag{VD.14}
\]

The orientation of the good hexagons is not yet proved coherent.  That is now the precise local frontier: convert the `O_eps(r)` cell-defect budget into a bounded-perimeter decomposition of the deep container into coherent triangular-lattice phase grains, and then feed one sufficiently large grain into a finite Kuperberg-type exchange or an exact-contact contradiction.

---

## 5. Scope audit

- Voronoi cells are taken with respect to the actual isolate set `Z`, not the positive core or an auxiliary lattice.
- The unit covering (VD.9) is the audited Type-I source-level covering theorem; no infinite-plane saturation hypothesis is inserted.
- The external Voronoi theorem is used only after (VD.3) proves the relevant finite-set cell is bounded.  Its minimum-distance normalization is scaled from `2` to `1` exactly.
- Strict contact isolation is used only to rule out the equality case; no uniform positive cell-area gap is claimed.
- The local Hall count is applied to a closed ball wholly inside `C_{-1}`.
- No affine-kernel or KKT statement is extended to isolate coordinates.
- The result does not yet force one common lattice phase, an exact unit contact, an exact unit triangle, or a spare packing site.

**Disposition:** proved proof-only local Voronoi-defect budget for the Type-I branch, conditional only on the stated external minimal-cell theorem.  C-II and Level I remain open.
