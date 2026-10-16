<!-- theorem-state: {"artifact_id":"ART-66604DAC7DB4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sublinear post-ZF surplus forces a macroscopic force-hull gap

**Date:** 2026-09-09  
**Repository base:** `be9cbfb78cbda059fb4c2581118b236729cfad84` plus ZI/ZJ/ZP on this branch  
**Run type:** quantitative stability reduction  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

The exact zero-surplus report excludes `e_BB=s_C=0`, but a stability theorem is needed
for small positive surplus. This report proves the first quantitative stability step.

Let

\[
G:=\operatorname{area}(F)-
\sum_r\operatorname{area}(\operatorname{conv}A_r)\ge0
\]

be the C49 attachment-cell area gap. The attachment hulls have pairwise disjoint
interiors. Combining their graph-diameter control with C67 shows that sublinear
loaded-loaded/pinned-stress surplus forces `G` to contain a fixed positive fraction of
`D^2`.

The planar defect bounds then localize that macroscopic uncovered area: either the
portion of the outer contact face inside the force hull has quadratic area, or one
bounded nonquadrilateral contact face has linear perimeter. Thus the low-surplus
post-ZF branch is not diffuse; it is forced directly into the old macroscopic
outer-shell / giant-cavity geometry.

## 1. Attachment-cell area upper bound

Use the notation of the post-ZF incidence bridge. Put

\[
k=d_H+s_Z,
\qquad
L=6-3k+e_{BB}+3s_C.
\tag{1.1}
\]

ZI proves

\[
\sum_r\delta_r\le L.
\tag{1.2}
\]

For each unloaded component C44's elementary contact-path argument gives

\[
\operatorname{diam}(A_r)\le\delta_r+2.
\tag{1.3}
\]

By the planar isodiametric inequality,

\[
\operatorname{area}(\operatorname{conv}A_r)
\le\frac\pi4(\delta_r+2)^2.
\tag{1.4}
\]

C49/C36-C38 give pairwise disjoint interiors of the attachment hulls, so their area
sum is at most `area(F)` and defines the nonnegative gap `G` above.

Summing (1.4), using `sum delta_r^2 <= L^2`, `c_I<=q`, and `q<=pi D`, gives

\[
\begin{aligned}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
&\le\frac\pi4
\left(L^2+4L+4c_I\right)\\
&\le\frac\pi4L^2+\pi L+\pi q\\
&\le\boxed{
\frac\pi4L^2+\pi L+\pi^2D.
}
\tag{1.5}
\]

This estimate is unconditional within the post-ZF C-II branch; it does not assume a
near-minimal boundary.

## 2. Theorem ZG — quantitative force-hull gap

Canonical C67 gives

\[
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
\boxed{a_0:=\frac12\sin(1/4)}
=0.1237019796\ldots .
\tag{ZG.1}
\]

Let a post-ZF sequence satisfy

\[
\lambda:=\limsup_{D\to\infty}
\frac{e_{BB}+3s_C}{D}.
\tag{ZG.2}
\]

Since `k>=0`, (1.1) gives

\[
\limsup L/D\le\lambda.
\]

Subtract (1.5) from the C67 lower bound.

### Theorem ZG

\[
\boxed{
\liminf_{D\to\infty}\frac G{D^2}
\ge
 a_0-\frac\pi4\lambda^2.
}
\tag{ZG.3}
\]

In particular, if

\[
e_{BB}+s_C=o(D),
\]

then

\[
\boxed{
\liminf\frac G{D^2}
\ge a_0
=rac12\sin(1/4)>0.
}
\tag{ZG.4}
\]

More generally `G` is forced to have positive quadratic density whenever

\[
\lambda<2\sqrt{a_0/\pi}
=\sqrt{\frac{2\sin(1/4)}\pi}
=0.396\ldots .
\tag{ZG.5}
\]

### Proof

Divide (1.5) by `D^2`. The linear terms tend to zero and the quadratic term has
limsup at most `(pi/4)lambda^2`. Since

\[
G=\operatorname{area}(F)-
\sum_r\operatorname{area}(\operatorname{conv}A_r),
\]

C67 gives ZG.3. The corollaries are immediate. `square`

## 3. Localizing a quadratic gap into the contact-face geometry

Let

- `A_bnd` be total area of bounded contact faces;
- `H_out:=area(F)-A_bnd>=0` be the portion of the force hull lying in the outer
  contact face;
- `A_exc` be the total area of bounded nonquadrilateral contact faces.

Every bounded quadrilateral is a strict unit rhombus and has area at most one.
C49's charging proof says every quadrilateral face without a loaded vertex is
contained in one harmonic attachment hull. A loaded vertex has at most three contact
edges and one exterior sector, so at most `2q` quadrilateral faces are lost from that
cell charging.

Consequently the area not charged to the attachment cells is bounded by

\[
\boxed{
G\le H_{out}+A_{exc}+2q.
}
\tag{3.1}
\]

The additive `2q` is only `O(D)`.

The post-ZF face inequality in the survivor direction gives

\[
b+Q\le2h\le2q,
\]

where `Q=sum_exc(deg F-4)`. Since every exceptional bounded face has degree at least
five,

\[
f_{exc}\le Q,
\]

and its total perimeter satisfies

\[
K_{exc}:=\sum_{F\ exc}\deg F
=Q+4f_{exc}
\le5Q
\le10q
\le10\pi D.
\tag{3.2}
\]

C51 says each bounded face is a simple strictly convex unit-edge polygon. Hence the
isoperimetric inequality gives

\[
\operatorname{area}(F_i)
\le\frac{k_i^2}{4\pi}
\]

for an exceptional face of perimeter `k_i`.

## 4. Corollary ZG.1 — outer-shell / giant-face dichotomy

Suppose along a post-ZF sequence

\[
G\ge gD^2
\]

for some fixed `g>0` and all sufficiently large indices. Then, after passing to a
subsequence, at least one of the following holds:

1. **macroscopic outer-face area**
   \[
   \boxed{H_{out}\ge(g/3)D^2;}
   \tag{ZG.6}
   \]
2. **giant bounded defect face:** there is a bounded nonquadrilateral face of perimeter
   \[
   \boxed{k_{max}\ge c_gD}
   \tag{ZG.7}
   \]
   for an explicit constant `c_g>0` (for example any asymptotic constant below
   `2g/15` is valid with the crude bounds used here).

### Proof

By (3.1), for large `D` the `2q=O(D)` term is below `(g/3)D^2`. If `H_out` is also
below `(g/3)D^2`, then

\[
A_{exc}\ge(g/3)D^2
\]

for large `D`.

Let `k_max` be the largest exceptional-face perimeter. Then

\[
A_{exc}
\le\frac1{4\pi}\sum_i k_i^2
\le\frac{k_{max}}{4\pi}\sum_i k_i
\le\frac{k_{max}}{4\pi}(10\pi D)
=\frac52 k_{max}D.
\]

Thus

\[
k_{max}\ge\frac{2g}{15}D.
\]

This proves the dichotomy. `square`

### Sublinear-surplus specialization

If `e_BB+s_C=o(D)`, ZG.4 supplies any fixed `g<a_0` eventually. Hence every such
post-ZF survivor has either

\[
H_{out}=\Omega(D^2)
\]

or one bounded exceptional contact face of perimeter `Omega(D)`.

This reproduces the old macroscopic cavity geometry from a new source: not from an
assumed quadratic rattler count, but directly from the exact post-ZF stress/incidence
ledger plus the C67 two-dimensional force-hull carrier.

## 5. Relation to the force-bulk frontier

C52 already absorbs the **population** contained in bounded defect faces into a
source-capacity estimate with only an outer-boundary correction. It does not exclude a
geometrically giant bounded face or a macroscopic outer-face region. ZG therefore does
not close Level I.

The new chain is

```text
post-ZF sublinear e_BB+s_C
 -> ZI: sublinear total harmonic-component graph diameter
 -> attachment-cell area = o(D^2)
 -> C67: G = Omega(D^2)
 -> C42/C51: macroscopic outer-face area or one linear-perimeter defect face.
```

Together with ZP, the same sublinear-surplus branch also has quadratic
contact-isolated population. Thus both the missing **population** and the missing
**area** are forced into macroscopically visible cavity/shell geometry.

## 6. Regression audit

- **Regular odd shell:** `e_BB=q`, so ZG's sublinear specialization does not apply.
- **Exact zero-surplus triangulation:** there `G=0` by the triangulation partition,
  which contradicts ZG/C67; this recovers ZQ from a complementary viewpoint.
- **One giant cavity:** explicitly retained as ZG.1 branch 2.
- **Outer shell with dense invisible points:** explicitly retained as ZG.1 branch 1.
- **Many tiny exceptional faces:** cannot carry `Omega(D^2)` uncovered area under the
  `O(D)` total exceptional perimeter bound.

## 7. Exact next target

The low-surplus route is now reduced to one macroscopic container theorem:

> **Post-ZF cavity exclusion.** Exclude a lexicographically normalized triangle-free
> global minimizer with `e_BB+s_C=o(D)` in which either the force-hull outer-face area
> is `Omega(D^2)` or one convex bounded nonquadrilateral contact face has perimeter
> `Omega(D)`, while the source has the quadratic isolated population forced by ZP.

The complementary route remains to convert `e_BB+3s_C=Omega(D)` directly into the
face inequality or a response defect.

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| attachment-cell area bound (1.5) | proved | C49 disjoint cells + ZI + isodiametric inequality. |
| quantitative `G` lower bound | proved | C67 minus (1.5). |
| sublinear surplus -> `G=Omega(D^2)` | proved | ZG.4. |
| macroscopic gap -> outer/giant-face dichotomy | proved | C49 charging + post-ZF face-perimeter budget + C51 convexity. |
| either cavity geometry impossible | not proved | This is the remaining global capacity theorem. |
| Level I | still open | Linear-surplus and cavity branches remain. |

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let L=6-3(d_H+s_Z)+e_BB+3s_C. ZI gives sum delta_r<=L.
C49 attachment cells are disjoint and diam(A_r)<=delta_r+2, hence
  sum area(conv A_r)
    <= (pi/4)L^2 + pi L + pi q
    <= (pi/4)L^2 + pi L + pi^2 D.
C67 gives area(F)/D^2 >= a0-o(1), a0=(1/2)sin(1/4).
Therefore, if lambda=limsup(e_BB+3s_C)/D,
  liminf G/D^2 >= a0-(pi/4)lambda^2.
In particular e_BB+s_C=o(D) => G>= (a0-o(1))D^2.

C49/C42/C51 then imply:
  either outer-contact-face area inside F is Omega(D^2),
  or one bounded nonquadrilateral contact face has perimeter Omega(D).

Together with ZP, sublinear surplus also forces n-v=Theta(D^2) isolated population.
Next target: exclude these macroscopic cavity/shell geometries using exact global
minimum-diameter capacity, or attack the complementary linear e_BB/s_C branch.
```
