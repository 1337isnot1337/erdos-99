<!-- theorem-state: {"artifact_id":"ART-DB8EB678ED28","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — oblique ordered-grid regression

**Date:** 2026-09-12  
**Status:** **regression against a carrier-only closure; not a theorem about global minimizers**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Candidate implication tested

The live Route-C idea can be stated as

    large ordered train grid
    + O(1/D) rhombus-angle defect
    + O(D) boundary/interface defect
    + near-triangular rhombic density
    -> exact unit equilateral triangle.

The exact canonical quantity is the unit-contact graph of the harmonic carrier. The
desired contradiction would be an exact unit triangle, or a source-preserving strict
sub-D competitor. This report shows that the displayed carrier-only implication is
false. A missing global-minimality hypothesis must do real work.

## 2. Exact family

For \(m\ge3\), choose integers \(p,q\) with \(q=m\) and

\[
3(p-1)^2\le q^2<3p^2.
\tag{OG.1}
\]

Put

\[
t={p\over q},\qquad
c={1-t^2\over1+t^2},\qquad
s={2t\over1+t^2}.
\tag{OG.2}
\]

Then \(c,s\) are rational, \(c>0\), and \(c<1/2\). Let

\[
u=(1,0),\qquad v=(c,s),
\]

and take the finite source

\[
P_m=\{iu+jv:0\le i,j\le m\}.
\tag{OG.3}
\]

The certificate research/target_c_oblique_ordered_grid_regression.py constructs \(p\)
as the least integer satisfying the strict right inequality in (OG.1) and checks all
claims using integer arithmetic and fractions.Fraction.

## 3. Exact unit-contact graph and triangle exclusion

For an integer difference \((a,b)\), the squared Euclidean length is

\[
\|au+bv\|^2=a^2+2cab+b^2.
\tag{OG.4}
\]

If \(ab\ge0\) and both coordinates are nonzero, then (OG.4) is at least
\(a^2+b^2\ge2\). If \(ab<0\), write \(A=|a|\), \(B=|b|\). Since \(0<2c<1\),

\[
\|au+bv\|^2
=A^2+B^2-2cAB
=(A-B)^2+2AB(1-c)>1
\tag{OG.5}
\]

for \(A,B\ge1\); the equality case \(A=B=1\) is strictly greater than one because
\(c<1/2\). If one coordinate is zero, equality to one occurs exactly for the four
vectors \((\pm1,0),(0,\pm1)\).

Therefore the complete unit-difference set of the finite patch is exactly

\[
\{\pm u,\pm v\}.
\tag{OG.6}
\]

The unit-contact graph is the Cartesian grid on indices \(\{0,\ldots,m\}^2\). It is
bipartite under the parity of \(i+j\), so it has no triangle at all, in particular no
unit equilateral triangle.

This is an exact finite conclusion, not a floating-point near-triangle assertion.

## 4. Every carrier-level feature survives

The patch has \(m^2\) bounded unit rhombi. Each is strict because its short diagonal
has length

\[
|u-v|=\sqrt{2-2c}>1,
\tag{OG.7}
\]

whereas the long diagonal is larger. Its two train directions are \(u\) and \(v\),
and the two families are complete: there are \(m+1\) parallel \(u\)-trains and
\(m+1\) parallel \(v\)-trains, with every pair crossing once. The outer interface has
exactly \(4m\) unit-edge occurrences. Thus the train grid is linear-by-linear and the
boundary/interface budget is \(O(m)\).

The diameter is attained by the opposite corners because \(c>0\):

\[
D_m^2=m^2|u+v|^2=m^2(2+2c).
\tag{OG.8}
\]

The rhombic area is

\[
A_{4,m}=m^2s.
\tag{OG.9}
\]

Writing \(a_0=\sqrt3/2\), the area excess above the equilateral value is only boundary
order. Indeed

\[
s^2-{3\over4}=(1/2-c)(1/2+c),
\]

and \(s+\sqrt3/2>1\), so

\[
0<A_{4,m}-a_0m^2<m^2(1/2-c).
\tag{OG.10}
\]

Minimality in (OG.1) gives

\[
1/2-c={3p^2-q^2\over2(q^2+p^2)}
<{3p\over q^2+p^2}< {3\over q}={3\over m}.
\tag{OG.11}
\]

Consequently

\[
0<A_{4,m}-a_0m^2<3m=O(D_m),
\qquad
\theta_m-\pi/3=O(1/m)=O(1/D_m),
\tag{OG.12}
\]

where \(\theta_m=\arccos c\). The last estimate follows from
\(\cos(\pi/3)-\cos\theta_m\ge(\sqrt3/2)(\theta_m-\pi/3)\) on
\([\pi/3,\pi/2]\).

Thus this exact family simultaneously has

    quadratic strict-rhombus area;
    complete ordered train grids with linear shores;
    O(1/D) angle defect on every rhombus;
    O(D) boundary/interface length and total area defect;
    no unit equilateral triangle.

It also makes the Section-116 two-arc expression explicit:

\[
L+P_{\rm exc}-2d
=4m-2m\sqrt{2+2c},
\tag{OG.13}
\]

which is positive and linear in \(m\); the exact Section-116 lower bound is compatible
with it. Therefore the ordered grid and the zero-host detour currency do not create
an exact contact by themselves.

## 5. What the regression does and does not prove

It proves a finite negative statement:

> no proof can close C-II from the displayed carrier-level properties alone.

It does **not** produce a counterexample to Erdős #99. The patches are not claimed to
be global minimum-diameter configurations for their cardinalities. In fact their
parallelogram boundary is not the near-disk global-hull geometry, and the missing
global-minimality comparison is precisely the point.

It also does not invalidate the canonical ordered-grid theorem, the phase-defect
ledger, or the Section-116 transport inequality. It invalidates only the unqualified
upgrade from those carrier facts to an exact triangle.

## 6. Route effect

Route C is reduced to a sharper, genuinely source-level obligation:

    near-triangular ordered rhombic carrier
    + full-source global minimality
    -> exact triangle or a disconnected strict-diameter replacement.

The next attempted bridge must therefore use one of the following facts absent from the
regression:

1. the global near-disk source hull and all actual diameter constraints;
2. a source-preserving finite reconfiguration, including the attachment boundary;
3. an exact comparison with a same-cardinality competitor of smaller diameter; or
4. a theorem transferring carrier area/interface slack into the actual KKT response.

The regression is **not canonical** and does not change the theorem-state manifest.
