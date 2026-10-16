<!-- migration-source: path=docs/reports/target_c_nearcircle_diameter_star_collapse_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e1a3a09fb36ded3134f3389de9bb12d2232b91ca; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — near-circle convergence collapses every diameter star to sublinear degree

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** asymptotic convex-geometry / diameter-support theorem  
**Target:** PR #119 UF near-circle branch after LC  
**Depends on:** DC Hausdorff disk convergence, C65 complete actual diameter support, convex perimeter-measure convergence  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C18 gives a universal linear upper bound on the degree of one diameter star. In the PR #119 small-outer-walk branch the force hull is much more rigid: after scaling by `D` it converges to the diameter-one disk.

This forces every exact diameter star to collapse into a vanishing angular neighborhood of the unique antipode of its center. Since the loaded force-hull perimeter measure converges to the nonatomic circular measure, such a vanishing boundary arc contains only `o(D)` unit-separated loaded terminals.

Therefore

\[
\boxed{
\Delta(H)=o(D),
}
\tag{NS.1}
\]

where `H` is the **complete actual diameter graph** supplied by C65.

Consequently a disk-scale harmonic attachment block containing `Theta(D)` loaded terminals cannot send all of its mandatory diameter incidences through a bounded number of opposite-side star centers.

---

## 1. Every diameter pair becomes antipodal

Normalize the force hulls by `D` and translate as in DC:

\[
F_j/D_j\longrightarrow B_{1/2}
\]

in Hausdorff distance.

Let `uv` be any actual diameter pair. Then

\[
|u-v|=D_j.
\]

After normalization, choose any convergent subsequence

\[
u_j:=u/D_j\to u_\infty,
\qquad
v_j:=v/D_j\to v_\infty.
\]

Both limits lie in `B_{1/2}`, while

\[
|u_\infty-v_\infty|=1.
\]

The only two points of the radius-`1/2` disk at mutual distance one are antipodal boundary points. Hence

\[
u_\infty,v_\infty\in\partial B_{1/2},
\qquad
v_\infty=-u_\infty.
\]

A compactness contradiction makes this uniform.

### Lemma NS.1 — uniform antipodal localization

Let `angle_j(u,v)` denote the smaller error from antipodality in the disk-centered polar angle. Then

\[
\boxed{
\sup_{uv\in H_j}
|\pi-\angle(u,v)|\longrightarrow0.
}
\tag{1.1}

\]

Otherwise a sequence of diameter pairs with error bounded below would have a non-antipodal limit pair at distance one in `B_{1/2}`, impossible.

---

## 2. All partners of one terminal occupy a vanishing boundary arc

Fix a loaded terminal `z`. Every diameter partner `a` of `z` is antipodal to `z` up to the uniform error in NS.1. Therefore all partners of `z` lie in one force-hull boundary arc whose disk-centered angular length is

\[
\eta_j=o(1)
\tag{2.1}
\]

uniformly in the choice of `z`.

Equivalently, if `J_j(z)` is the smallest disk-angle interval containing all diameter partners of `z`, then

\[
\boxed{
\sup_z |J_j(z)|\to0.
}
\tag{2.2}
\]

This sharpens the fixed positive C18 star cone width only in the near-circle branch.

---

## 3. Vanishing angular arcs have `o(D)` force-hull length

For a convex body `K`, let `sigma_K` be its perimeter measure indexed by outer normal angle. Hausdorff convergence of planar convex bodies implies weak convergence of their perimeter measures.

For the normalized force hulls,

\[
\sigma_{F_j/D_j}
\Longrightarrow
\sigma_{B_{1/2}},
\]

and the limiting measure is the nonatomic uniform circular perimeter measure.

A standard uniform-nonatomicity consequence is:

### Lemma NS.2

If `I_j` is any sequence of angular intervals with

\[
|I_j|\to0,
\]

then

\[
\boxed{
\sigma_{F_j/D_j}(I_j)	o0
}
\tag{3.1}
\]

uniformly over the location of `I_j`.

### Proof

If not, there are intervals `I_j` of length tending to zero carrying mass at least `epsilon>0`. Pass to a subsequence whose centers converge to an angle `theta`. For every fixed neighborhood `U` of `theta`, eventually `I_j subset U`. Portmanteau then gives limiting mass at least `epsilon` at `theta` after shrinking `U`, contradicting that the circular limit measure has no atoms. `square`

The same conclusion holds for boundary-arc length indexed by polar angle because the normalized convex curves converge to the circle and their tangent/normal angle parametrizations differ by a vanishing uniform perturbation away from a set of perimeter measure tending to zero. Alternatively one may use arclength parametrizations of convex curves: Hausdorff convergence plus perimeter convergence gives uniform convergence of normalized arclength parametrizations, and the disk limit is uniformly continuous.

Thus the actual force-hull boundary length contained in any partner arc `J_j(z)` is

\[
\boxed{o(D_j)}
\tag{3.2}
\]

uniformly in `z`.

---

## 4. Unit separation converts arc length into degree

List the distinct diameter partners of `z` in their order along the convex force hull:

\[
a_1,\ldots,a_d,
\qquad d=\deg_H(z).
\]

All lie in `J_j(z)`. The force-hull boundary arc from `a_i` to `a_{i+1}` has length at least the Euclidean chord length, and unit separation gives

\[
|a_i-a_{i+1}|\ge1.
\]

Therefore

\[
d-1
\le
\operatorname{length}_{\partial F_j}J_j(z).
\tag{4.1}
\]

Using (3.2), uniformly in `z`,

\[
\boxed{
\max_z\deg_H(z)=o(D_j).
}
\]

This proves NS.1.

---

## 5. Consequence for the LC macroscopic attachment block

Let `I_*` be the LC/CH macroscopic harmonic component and let

\[
A_*\subset B_+
\]

be its distinct loaded attachment set.

At the UF crossover LC gives

\[
|A_*|
\ge(0.7591662335-o(1))D.
\]

For every fixed population parameter with LC lower endpoint `mu<1`, the attachment cell has diameter below `D` asymptotically, so there is no diameter edge with both endpoints in `A_*`.

Every terminal in `A_*` is incident to at least one actual diameter edge by C65. Hence the number of diameter incidences leaving `A_*` is at least `|A_*|`.

Let

\[
N_H(A_*)
:=\{b\notin A_*:\exists a\in A_*,\ ab\in H\}.
\]

NS.1 gives

\[
\max_b\deg_H(b)=o(D),
\]

so

\[
|A_*|
\le
\sum_{b\in N_H(A_*)}\deg_H(b)
\le
|N_H(A_*)|\,o(D).
\]

Therefore

\[
\boxed{|N_H(A_*)|\to\infty.}
\tag{5.1}
\]

More precisely,

\[
|N_H(A_*)|
\ge
\frac{|A_*|}{\Delta(H)}
\to\infty.
\tag{5.2}
\]

A greedy matching argument also gives a diameter matching between `A_*` and its complement whose size tends to infinity.

This is not yet a linear matching: without a quantitative rate in the disk convergence, `Delta(H)=o(D)` may still be much larger than one.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| every diameter pair tends uniformly to antipodal geometry | proved | compactness + uniqueness of disk antipodes |
| every diameter star angular span tends to zero | proved | all partners localize near same antipode |
| vanishing partner arc has `o(D)` boundary length | proved | weak perimeter-measure convergence to nonatomic circle measure |
| `Delta(H)=o(D)` | proved | unit separation along partner arc |
| LC macroscopic block needs infinitely many opposite carriers | proved | every attachment terminal has a diameter edge, no internal diameter pair when `mu<1` |
| linear number of opposite carriers | not proved | no rate for star collapse |
| Level I | still open | a slowly growing family of star centers remains possible |

---

## 7. Next target

NS identifies the exact missing quantitative input:

> obtain a boundary-order rate for antipodal localization from the source's boundary-order packing defect.

The global Wegner theorem on PR #131 and the near-circle completion-shell estimates are natural candidates. A rate such as

\[
\Delta(H)=O(D^{1-\epsilon})
\]

would already force a polynomially growing family of opposite carriers; an `O(1)` star bound in the UF endpoint would force a linear diameter matching across the giant attachment block and interact strongly with ZT/NM.

No such rate is claimed here.
