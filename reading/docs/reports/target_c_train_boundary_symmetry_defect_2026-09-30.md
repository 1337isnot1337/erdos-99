> Generated reading edition · [exact source](../../../docs/reports/target_c_train_boundary_symmetry_defect_2026-09-30.md) · source SHA-256 `0b0627492b71585bd0624c04a238937b88aa24e5e8a4e4663472c0403aded87e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F7054E268EE0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: finite train-boundary symmetry defect

**Date:** 2026-09-30<br>
**Base main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; noncanonical.<br>
**Level I:** open. C-II remains open.

## 1. Finite theorem

Use the canonical induced harmonic contact graph on $`I\cup A`$, its
convex attachment polygon $`P=\operatorname{conv}A`$, its occurrence-counted
outer walk of length $`L`$, and its full bounded strict-unit-rhombus complex.
Let $`p=\operatorname{per}P`$, $`Z=L-p\ge0`$, and let $`Q`$ be the
bounded nonquadrilateral degree excess. Orient the outer walk with the
bounded region on its left.

Let $`\nu_P`$ put mass equal to each polygon side's length at its oriented
unit tangent direction. Let $`\sigma(u)=-u`$. For measures on the unit
direction circle define
```math
d_{\rm BL}(\mu,\nu)=
\sup_{\|f\|_\infty\le1,\ \operatorname{Lip}(f)\le1}
\left|\int f\,d(\mu-\nu)\right|,
```
using chord distance for the Lipschitz bound. Then exactly
```math
\boxed{
d_{\rm BL}(\nu_P,\sigma_\#\nu_P)
\le 2\sqrt{2LZ}+2Z+20Q.
}
\tag{1.1}
```

This bounds physical boundary length and occurrence mass. It makes no
conversion from exceptional vertices to exceptional incidences.

## 2. Proof of the finite estimate

### 2.1 Physical train ends are antipodally paired

Opposite rhombus edges are parallel. Orient every physical rhombus-boundary
occurrence with its rhombus on the left, including hole boundaries. The two
ends of a stopped train have opposite oriented unit tangent vectors.
To see this, orient the train along its strictly increasing transverse
coordinate: it enters the first terminal edge into the left face and exits
the last from the left face. Opposite-edge gluing preserves this orientation.
Consequently the direction-counting measure of **all** physical train ends
is invariant under $`\sigma`$.

Write this end measure as $`N_{\rm out}+N_{\rm exc}`$, according as an
end faces the old outer face or a bounded nonquadrilateral face. Canonical
Sections 82 and 89 give
```math
N_{\rm exc}(\mathbb S^1)\le5Q.
```
Therefore
```math
\|N_{\rm out}-\sigma_\#N_{\rm out}\|_{\rm TV}
\le2N_{\rm exc}(\mathbb S^1)\le10Q.
\tag{2.1}
```

Let $`M`$ count all oriented outer-walk unit-edge occurrences. An outer
occurrence not counted in $`N_{\rm out}`$ either belongs to a bridge,
or faces a bounded nonquadrilateral face on its other side. Bridge
occurrences pair as opposite traversals of the same physical edge, so their
measure is exactly $`\sigma`$-invariant. The remaining occurrences number
at most $`5Q`$. Thus
```math
\|M-\sigma_\#M\|_{\rm TV}\le20Q.
\tag{2.2}
```
There is no assumption that the outer walk is simple, or that bridges are
sublinear. Their two orientations cancel exactly in this measure comparison.

### 2.2 Transfer unit occurrences to convex side length

Split the outer walk at the distinguished exterior attachment occurrences,
in cyclic order. For route $`W_i`$, let $`\ell_i`$ be its unit occurrence
count, let $`s_i`$ be its endpoint chord length, and let $`u_i`$ be that
oriented chord's unit direction. Its edge vectors $`z_e`$ satisfy
```math
\ell_i-s_i=\sum_{e\in W_i}(1-u_i\cdot z_e),\qquad
\sum_i(\ell_i-s_i)=Z.
\tag{2.3}
```
For a test function in (1.1),
```math
\begin{aligned}
\left|\int f\,d(M-\nu_P)\right|
&\le\sum_i\sum_{e\in W_i}|z_e-u_i|+Z\\
&\le\sqrt{L\sum_i\sum_{e\in W_i}|z_e-u_i|^2}+Z\\
&=\sqrt{2LZ}+Z.
\end{aligned}
\tag{2.4}
```
The last identity is $`|z_e-u_i|^2=2(1-u_i\cdot z_e)`$.
Apply (2.4) to $`f`$ and $`f\circ\sigma`$, and insert (2.2) between
the two comparisons. This proves (1.1).

## 3. Zero-defect limit classification

Suppose $`L_D=O(D)`$, $`Z_D=o(D)`$, $`Q_D=o(D)`$, and
$`D^{-1}P_D\to K`$ in Hausdorff distance, where $`K`$ has positive area.
Then $`K`$ is centrally symmetric, up to a translation.

Here is the compactness argument explicitly. Rotate tangent measures to
outward-normal measures and let $`h_D`$ be the support function of
$`D^{-1}P_D`$. Hausdorff convergence gives uniform convergence
$`h_D\to h_K`$. In the distributional sense the normal boundary-length
measure is
```math
\mu_D=h_D''+h_D.
```
For polygons this follows by differentiating on the intervals where one
vertex supports and recording the derivative jump, which is exactly the
side length. Equivalently, for every smooth periodic test function,
```math
\int f\,d\mu_D=\int_0^{2\pi}h_D(f''+f)\,d\theta.
```
Uniform support convergence therefore gives weak convergence to
$`\mu_K=h_K''+h_K`$. Formula (1.1), divided by $`D`$, makes this limit
measure invariant under $`\theta\mapsto\theta+\pi`$.

Hence $`g(\theta)=h_K(\theta)-h_K(\theta+\pi)`$ solves
$`g''+g=0`$. Its distributional solutions are
$`a\cos\theta+b\sin\theta`$. Translating by $`(a/2,b/2)`$ removes
this difference. The translated support function is $`\pi`$-periodic,
which is exactly central symmetry.

Only weak convergence of finite measures and uniform support convergence
are used. No convergence rate or finite equality is inferred.

## 4. Circle-supported consequences

Suppose additionally $`K=\operatorname{conv}S`$, where
$`S\subset\partial B(0,1/2)`$ is compact. Every extreme point of $`K`$
belongs to $`S`$. If the center of symmetry were $`c\ne0`$, an extreme
point $`x`$ and its reflection $`2c-x`$ would both have norm $`1/2`$.
Subtracting their squared norms gives
```math
c\cdot x=|c|^2.
```
Thus all extreme points, and hence the entire convex body, would lie on one
line, contradicting positive area. Therefore the symmetry center is zero.
Antipodal extreme points have distance one, so
```math
\boxed{\operatorname{diam}K=1,\qquad 0\in\operatorname{int}K.}
\tag{4.1}
```

Consequently a positive-area circle-supported carrier of normalized
diameter strictly below one cannot have both $`Z_D=o(D)`$ and
$`Q_D=o(D)`$. Neither can a positive-area cap-type carrier, even when
its diameter tends to one: a full-dimensional centrally symmetric body
centered at zero cannot be contained in a half-plane through zero.

This strengthens the three-gap endpoint exclusion in
`target_c_geodesic_train_boundary_four_face_obstruction_2026-09-30.md`.
Its general four-face theorem remains valid and supplies additional phase
information; the new central-symmetry classification needs no phase-bin
extraction or angular-defect hypothesis.

In particular the current unpromoted rooted stability package's
$`d_w/D\to\lambda_1<1`$, $`Z_w=o(D)`$, $`Q_w=o(D)`$, and positive
carrier area are already contradictory. No separate complement-gap equality
classification is needed for this application.

## 5. What remains

The finite estimate allows linear defects. After scaling it reads
```math
d_{\rm BL}(\nu_K,\sigma_\#\nu_K)
\le2\sqrt{2\ell z}+2z+20q_{\rm exc}
```
along subsequences with normalized currencies
$`\ell=L/D`$, $`z=Z/D`$, and $`q_{\rm exc}=Q/D`$. It gives a necessary
payment for asymmetry; it does not show that the available rooted payment is
insufficient throughout the positive-defect regime.

The surviving zero-defect possibility is a positive-area centrally symmetric
diameter-one wrapping limit. This report does not classify its complete train
crossing structure. A proposal that every such limit is a parallelogram needs
an additional argument: train ends are close to the hull, but their original
midpoints need not lie exactly on its boundary. Alternation of near-boundary
endpoints alone is not a finite intersection theorem.

Likewise the two-half-disk groups can consist of many cap cells and their
defining diameter-scale cells can have vanishing area. The cap consequence
applies to a positive-area actual carrier with sublinear **local** defects;
group area cannot silently supply that local hypothesis. The positive-defect
two-half-disk regime and the macroscopic-container branch remain open.

## 6. Audit and dependencies

The analytic proof uses canonical Sections 61/89 for stopped rhombus trains,
Section 82 for induced harmonic graphs and the $`5Q`$ stopping-face capacity,
and the distinguished outer attachment ordering used in Sections 61 and 101.
The boundary measure calculation is proved above and imports no literature
or computational certificate.

The audit retained bridges and repeated occurrences, checked outer edges
without rhombus neighbors, treated hole ends by physical incidence, used
distributional support functions for nonsmooth limits, and excluded
vanishing-area limits explicitly. No KKT coefficient floor or full-source
affine-kernel extension is assumed. Contact-isolated source points are retained.

**Promotion disposition:** finite estimate and limit classification are proved
candidates awaiting independent promotion. The rooted application is conditional
on its unpromoted stability input. No canonical status changes in this report.
