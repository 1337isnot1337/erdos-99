<!-- theorem-state: {"artifact_id":"ART-5B7651756EB4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact two-geodesic central-face corridor regression

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.49
**Run type:** exact finite regression / adversarial audit
**Target:** Target C-II / Level I
**Starting status:** canonical full-core central-face reduction; aggregate detour/payment closure open
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used for the result
**Computation:** used: docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_central_face_two_geodesic_corridor.py

## LEVEL I STATUS

STILL OPEN

This report gives both an exact finite triangle-free contact complex whose convex
empty face has two long unit-contact geodesic sides and only a constant-width
corridor between them, and a quadratic near-optimal-density embedding of the same
phenomenon. It is a regression against a local central-face closure, not a global
minimizer and not a disproof of Erdős Problem #99.

## 1. Starting canonical endpoint

In the sharp full-core interface branch, the canonical reduction permits one convex
loaded-interface face F_* with

\[
k_{F_*}=2D+o(D),
\]

whose two long boundary paths have lengths \(D+o(D)\), are near-geodesic, and lie
on opposite sides of a graph-free central corridor. A tempting implication was

    two long unit-contact sides of one empty convex face
        -> a unit equilateral triangle, or a fixed linear area loss
        -> C-II closure.

The constructions below reject that implication at the exact finite geometric scope.
Its corridor width is 9/10, its two long sides have exactly m unit edges, and every
source pair not on the displayed contact cycle is strictly farther than one. The
face degree is 2m+4, so its degree excess is 2m, while its area and diameter are
both linear in m.

The valid implication chain is only

    central-face near-geodesics
        -> no local fixed-width triangle/area contradiction
        -> any closure must use the half-disk populations, source-cardinality
           exchange, actual diameter graph, or a global strict-decrease theorem.

## 2. Exact corridor construction

Fix an integer \(m\ge2\). Set

\[
h=\frac9{10},\qquad s=\frac12,
\]

and define two horizontal unit chains

\[
A_i=(i,0),\qquad B_i=(i+s,h),\qquad 0\le i\le m.
\]

Put

\[
d^2=s^2+h^2=\frac{53}{50},\qquad
t=\sqrt{1-\frac{d^2}{4}}=\sqrt{\frac{147}{200}},\qquad
r=\frac td=\sqrt{\frac{147}{212}}.
\]

The two additional vertices are

\[
C_L=\left(\frac14-hr,\frac h2+\frac r2\right),\qquad
C_R=\left(m+\frac14+hr,\frac h2-\frac r2\right).
\]

Let

\[
V_m=\{A_0,\ldots,A_m,B_0,\ldots,B_m,C_L,C_R\}.
\]

The contact edges are

\[
A_iA_{i+1}\ (0\le i<m),\qquad
B_iB_{i+1}\ (0\le i<m),
\]

\[
C_LA_0,\ C_LB_0,\ C_RA_m,\ C_RB_m. \tag{CF.1}
\]

They form one simple cycle, in the cyclic order

\[
A_0,A_1,\ldots,A_m,C_R,B_m,B_{m-1},\ldots,B_0,C_L. \tag{CF.2}
\]

The bounded face of this cycle is the convex polygon
\(F_m=\operatorname{conv}V_m\). The two paths
\(A_0\leadsto A_m\) and \(B_0\leadsto B_m\) are the long sides of the face.

## 3. Complete exact proof

### 3.1 The connector vertices give the four end contacts

The vector from \(A_0\) to \(B_0\) is \((s,h)\), of length \(d\in(1,2)\).
The standard two-circle intersection formula gives the two points at unit distance
from both endpoints:

\[
\frac{(s,h)}2\pm\frac td(-h,s).
\]

With the plus sign this is \(C_L\), and with the minus sign it is
\[
\left(\frac14+hr,\frac h2-\frac r2\right),
\]
so \(C_R=(m,0)+(\frac14+hr,\frac h2-\frac r2)\). Therefore all four
edges in the second line of (CF.1) have length exactly one.

The inequalities

\[
\frac45<r<\frac{21}{25} \tag{CF.3}
\]

are exact: after squaring, they reduce to
\(16/25<147/212<441/625\). Define

\[
\alpha=\frac14+hr,\qquad \beta=\frac h2-\frac r2.
\]

Then

\[
C_R=(m+\alpha,\beta),\qquad C_L=(1/2-\alpha,h-\beta),
\]

and (CF.3) gives

\[
0<\beta<\frac1{20},\qquad \frac{19}{20}<\alpha<1. \tag{CF.4}
\]

The successive cross products of the boundary edge vectors in (CF.2) are positive.
At the four non-collinear turns they are, in cyclic order,

\[
\beta,\qquad \alpha h-\frac\beta2,\qquad h-\beta,\qquad
\alpha h-\frac\beta2.
\]

The first and third are positive by (CF.4), and
\[
\alpha h-\frac\beta2>
\frac{19}{20}\frac9{10}-\frac1{40}>0.
\]
All other turns are collinear along one of the two chains. Hence \(F_m\) is convex,
and (CF.2) is its boundary cycle.

### 3.2 Exact unit separation and contact graph

Distances within either chain are integer horizontal distances, so distinct points
in one chain are at least one apart, with equality only for consecutive vertices.

For \(A_i\) and \(B_j\), put \(k=j-i\in\mathbb Z\). Then

\[
|A_i-B_j|^2=h^2+(k+s)^2
\ge\frac{81}{100}+\frac14=\frac{53}{50}>1. \tag{CF.5}
\]

For \(C_L\), its distances to \(A_0\) and \(B_0\) are one. As \(i\) or \(j\)
is increased from zero, the horizontal component of the corresponding difference
has strictly increasing absolute value, so all distances from \(C_L\) to
the points \(A_i\) with \(i\ge1\) and \(B_j\) with \(j\ge1\) are strictly greater
than one. The same argument, after reflection/translation, applies to \(C_R\),
whose only unit contacts are \(A_m\) and \(B_m\).

Finally, \(|C_L-C_R|>1\) for \(m\ge2\), because their horizontal separation is
\(m+2hr>2\). Thus the only unit contacts in \(V_m\) are exactly (CF.1).
The contact graph is the cycle (CF.2), so it is triangle-free. In particular
\(V_m\) contains no unit equilateral triangle.

### 3.3 Long geodesic sides and empty corridor

Each of the two paths
\[
A_0,A_1,\ldots,A_m
\quad\text{and}\quad
B_0,B_1,\ldots,B_m
\]
has exactly \(m\) unit edges and endpoint chord exactly \(m\). They are geodesics,
not merely asymptotically geodesic. The distance between the two long chains is at
least \(\sqrt{53/50}>1\) by (CF.5), so there is no contact edge or unit triangle
crossing the corridor.

The corridor width is the fixed value \(h=9/10\), close to the
triangle-free rhombic limiting width \(\sqrt3/2\).

The bounded face has

\[
|V_m|=2m+4,\qquad k_{F_m}=2m+4,\qquad Q_{F_m}=k_{F_m}-4=2m. \tag{CF.6}
\]

Its area is \(hm+O(1)\), since it is the region between two horizontal segments
of length \(m\) together with two fixed-size end pieces. Thus the linear face
degree and linear corridor area are exact in scale, with no quadratic obstruction.

For completeness, set \(\alpha,\beta\) as above. The farthest pair is \(C_LC_R\),
and

\[
\operatorname{diam}(V_m)^2=(m+2hr)^2+r^2. \tag{CF.7}
\]

This follows by checking the six non-collinear convex-hull vertices
\(A_0,A_m,C_R,B_m,B_0,C_L\); the horizontal and vertical coordinate ranges make
the two connector vertices the extreme pair. In particular,
\(\operatorname{diam}(V_m)=m+2hr+O(1/m)\).

## 4. Quadratic near-optimal-density embedding

The preceding cycle has only linear population. The same obstruction is not an
artifact of that scale. We now place it as a genuine bounded empty face inside a
quadratic, near-disk, nearly optimal-density source.

For \(R\) large, set

\[
\theta_R=\frac\pi3+R^{-2},\qquad
u=(1,0),\qquad v=(\cos\theta_R,\sin\theta_R),\qquad
\Lambda_R=\mathbb Zu+\mathbb Zv.
\]

Let

\[
W_R=\Lambda_R\cap\overline B(0,R),\qquad m_R=\lfloor R/10\rfloor,
\]

and delete the open central segment of the \(j=0\) lattice row:

\[
\widetilde W_R
=W_R\setminus\{iu:-m_R<i<m_R\}. \tag{CF.8}
\]

All removed points lie in the interior of the disk for large \(R\). The four
boundary chains of the resulting hole are

\[
C_L=-m_Ru,\quad L_i=iu-v\ (-m_R\le i\le m_R),\quad C_R=m_Ru,
\]
\[
U_i=iu+v\ (-m_R\le i\le m_R),
\]

in the cyclic order

\[
C_L,L_{-m_R},\ldots,L_{m_R},C_R,
U_{m_R},\ldots,U_{-m_R},C_L. \tag{CF.9}
\]

In lattice coordinates \((i,j)\), this is the affine image of the rectangle
\([-m_R,m_R]\times[-1,1]\), with precisely its interior integer points
\((i,0)\), \(-m_R<i<m_R\), removed. Consequently (CF.9) is the boundary of a
convex empty face of the straight-line contact graph.

For \(R\) large, \(0<\cos\theta_R<1/2\). For a nonzero lattice difference,

\[
|au+bv|^2=a^2+b^2+2ab\cos\theta_R\ge1,
\]

with equality only for \((a,b)=(\pm1,0),(0,\pm1)\). This follows by the two
cases \(ab\ge0\) and \(ab<0\), writing the latter as
\((|a|-|b|)^2+2|ab|(1-\cos\theta_R)\). Therefore \(\widetilde W_R\) is
unit-separated. Its contact graph uses only the four directions \(\pm u,\pm v\),
so the parity coloring \((i,j)\mapsto i+j\pmod2\) makes it bipartite and
triangle-free.

The hole boundary contacts are

\[
C_LL_{-m_R},\quad L_iL_{i+1},\quad L_{m_R}C_R,
\quad C_RU_{m_R},\quad U_iU_{i-1},\quad U_{-m_R}C_L.
\]

The two long sides have \(2m_R\) unit edges and endpoint chord \(2m_R\), hence
are exact geodesics. For \(k=i-j\),

\[
|L_i-U_j|^2=|ku-2v|^2=k^2+4-4k\cos\theta_R.
\tag{CF.10}
\]

The minimum over integral \(k\) is \(5-4\cos\theta_R>3\), so no contact crosses
the corridor. The end contacts do not make a triangle because the corresponding
opposite side points differ by \(2v\).

A fundamental lattice parallelogram has area \(\sin\theta_R\). Comparing disk
area with the union of cells meeting the disk gives

\[
|W_R|=\frac{\pi R^2}{\sin\theta_R}+O(R).
\tag{CF.11}
\]

The removed segment has \(2m_R-1=O(R)\) points, while
\(\sin\theta_R=\sqrt3/2+O(R^{-2})\). Thus

\[
|\widetilde W_R|=\frac{2\pi}{\sqrt3}R^2+O(R).
\tag{CF.12}
\]

The points \(\lfloor R\rfloor u\) and \(-\lfloor R\rfloor u\) remain, so

\[
2R-O(1)\le\operatorname{diam}(\widetilde W_R)\le2R.
\tag{CF.13}
\]

Writing \(D_R=\operatorname{diam}(\widetilde W_R)\), this yields

\[
\boxed{
|\widetilde W_R|=\frac{\pi}{2\sqrt3}D_R^2+O(D_R),
\qquad D_R=2R+O(1).
}
\tag{CF.14}
\]

The deleted segment does not affect the near-disk hull estimate. The same
fundamental-cell comparison supplies a lattice point within a fixed distance of
every radius-\(R\) support point; a point in the deleted segment has norm at most
\(m_R\), so it cannot be the only such support point. Hence

\[
B(0,R-O(1))\subseteq\operatorname{conv}(\widetilde W_R)
\subseteq B(0,R). \tag{CF.15}
\]

This is a quadratic, near-disk, near-optimal-density triangle-free source containing
a bounded empty face with two long geodesic sides. It is still only a regression:
the deleted-row boundary does not supply global minimum-diameter optimality, and
the boundary vertices are not asserted to satisfy the canonical KKT equilibrium.


## 5. Scope and exact obstruction

This is an explicit finite planar source, not an abstract graph. It preserves all
source points, has exact unit separation, has a convex empty face, and has no unit
equilateral triangle. It nevertheless lacks the global hypotheses needed for C-II:

- the first displayed cycle has only \(O(D)\) points; the quadratic embedding has
  the near-optimal count (CF.14), but it is not a canonical two-component harmonic
  source;
- it has no certified positive-contact harmonic interiors on both sides of the hole;
- it supplies no global minimum-diameter certificate for its cardinality;
- it has no contact-minimal/diameter-pair-minimal relation to a larger source; and
- it does not pay or realize the canonical loaded-hull, Section-122, or Section-123
  ledgers.

Therefore the regression does not contradict any canonical C-II theorem. It rejects
only the local bridge

\[
\text{two long empty-face geodesics}
\Longrightarrow
\text{exact unit triangle or fixed positive face-area gap}.
\]

The remaining source-level bridge must couple the corridor to the quadratic source
populations, the actual diameter graph/KKT response, or a finite same-cardinality
strict-\(D(n)\) deformation. Near-geodesicity and face degree alone are insufficient.

## 6. Proof-obligation ledger

### Canonical trusted inputs

- C-FULLCORE-NEAR-DISK, including the sharp central-face reduction in its stated
  full-core scope.
- C-AGGREGATE-TWO-ARC-DETOUR and C-AUGMENTED-CELL-DEFECT-BUDGET, which remain
  the active global full-core currency.

### New proved result

- The exact finite two-geodesic corridor construction (CF.1)--(CF.7), with its
  complete pairwise-distance and convexity proof.

### Regression / rejected implication

- The local implication “long empty-face geodesics force a triangle or a fixed
  linear area loss” is rejected at the finite contact-complex scope.

### Unresolved obligations

- Couple the central corridor to the two positive-density carrier populations.
- Upper-bound the actual aggregate outer-walk detour, construct a strict
  source-preserving sub-\(D(n)\) competitor, or force an exact unit triangle.
- Exclude the macroscopic inactive chamber/exterior-cap branch.

## 7. Regression checks

| Regression/correction | Result | Exact reason |
|---|---|---|
| Unit separation | pass | Formula (CF.5) and monotonic connector-coordinate checks |
| Triangle-freeness | pass | Exact contact graph is one cycle |
| Convex face | pass | All non-collinear boundary cross products are positive |
| Two long geodesics | pass | Both side paths have \(m\) unit edges and chord \(m\) |
| Empty central corridor | pass | All cross-chain distances are \(\sqrt{53/50}>1\) |
| Global optimality | not claimed | No lower-bound/certificate supplied |
| Quadratic full-core population | not claimed | Deliberately a local regression |
| Contact-isolated-source handling | pass | Every displayed vertex is retained; none is deleted |

## 8. Literature imports

None. Every geometric statement is proved directly from the coordinates.

## 9. Computation

The companion command is

    python3 docs/research/migration/2026-10-16/shards/01/support/research/verify_target_c_central_face_two_geodesic_corridor.py

It represents all coordinates as exact affine expressions in
\(r=\sqrt{147/212}\) and checks every squared pair distance as an exact element of
\(\mathbb Q(r)\) for \(2\le m\le32\). It verifies the contact list, positivity of
the convex-turn cross products, and the exact diameter formula (CF.7). The
all-\(m\) proof above is analytic; the script is a finite certificate, not a
numerical global-optimization search.

## 10. Promotion recommendation

regression/rejection only. Do not promote to the theorem-state manifest. The result
blocks a local closure but does not advance a canonical branch by itself.

## 11. Handoff

1. Strongest new result: an exact convex empty-face cycle with two length-\(m\) unit
   geodesics, fixed 9/10 width, and no unit triangle.
2. Canonical dependency chain: central-face reduction in C-FULLCORE-NEAR-DISK
   plus the active Section-122/123 endpoint; the construction is a regression
   against a local use of that endpoint.
3. Exact remaining lemma: a quadratic-population corridor capacity/deformation
   theorem coupled to the actual global minimizer.
4. Binding dead route: face degree, near-geodesicity, or a fixed corridor-width
   argument alone.
5. Files to read next: docs/targets/target-c/122-aggregate-two-arc-detour-audit.md,
   docs/targets/target-c/123-augmented-cell-defect-budget-audit.md, and
   docs/targets/target-c/85-train-boundary-interface-currency-audit.md.
