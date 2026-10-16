<!-- theorem-state: {"artifact_id":"ART-E4FDB3C26CA5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — one boundary label funds a robust full-interior oblique refill

**Date:** 2026-10-05. **Checkpoint:** 5194688a.
**Imported main:** 9fbb47f27b33480522c960d63bf3b86681f39f6f.
**State:** 2026-10-05.audit.53.
**Classification:** proved source-replacement candidate awaiting independent audit;
triangular limiting regression. Unreviewed and noncanonical.
**LEVEL I STATUS: STILL OPEN.**

## 1. Exact closing use

Actual unit wall close to a strictly oblique rectangular frame
\(\longrightarrow\) one deleted wall label funds a strict full-interior refill
\(\longrightarrow\) full frame population in every contact-minimal triangle-free
global source \(\longrightarrow\) local Oler residual bounded solely by angular
area excess and wall error \(\longrightarrow\) exclusion when that bound is exceeded.

The previous two-side theorem paid a linear boundary population. Here the
funding cost is one, for every positive oblique angle excess. The tolerance
depends explicitly on that excess. The triangular endpoint has an exact
one-pin displacement gap. No assertion is made that arbitrary canonical
grains, pentagons or macroscopic chambers possess this actual enclosing wall.

## 2. Auxiliary packing with one removed pin

Let \(m,n\ge3\), \(L=m+n\), \(u=(1,0)\), and
\[
v=(c,a)=(\cos\phi,\sin\phi),\quad \pi/3<\phi\le\pi/2,\quad
\delta=1-2c\in(0,1].
\]
Use the full grid frame \(p_{ij}=iu+jv\), fixing all boundary points
except \(p_{1,0}\), which is removed. Keep all \(K=(m-1)(n-1)\) interior
points. Put
\[
s=\frac{\delta}{100L^2},\quad h=\frac{s^2}{100L^3},\quad
\beta=\frac1{10L^3},\quad f_j=j(n-j)(1+\beta j).\tag{O.1}
\]

First move only column \(i=1\):
\[
p^{(1)}_{1j}=p_{1j}-s(n-j)(0,1),\qquad 1\le j<n.\tag{O.2}
\]
Horizontal contacts involving that column lengthen quadratically, with
squared excess at least \(s^2\). Vertical column contacts lengthen
linearly: their increment is \(s(0,1)\) and \(a\ge a_0=\sqrt3/2\).
The missing bottom pin removes the only boundary contact obstructing
this move. Other basis contacts stay unchanged.

Next move the remaining block, keeping that column and every retained
wall point fixed:
\[
r=(1,-c/a),\qquad
p'_{ij}=p_{ij}-h(m-i)f_jr\quad(2\le i<m,\ 1\le j<n).\tag{O.3}
\]
Here \(u\cdot r=1\), \(v\cdot r=0\), and \(|r|=1/a\).
Every horizontal block contact, including to its right wall, has squared
excess at least \(2h\). Vertical block contacts lengthen quadratically.
With \(f_0=f_n=0\), the successive difference \(f_j-f_{j-1}\)
has integer principal part \(n-2j+1\); its correction has magnitude
less than \(1/2\). If that integer is zero, \(n=2j-1\) and the
correction equals \(\beta j(j-1)\ge2\beta\). The endpoint cases
also satisfy
\[
|f_j-f_{j-1}|\ge2\beta.\tag{O.4}
\]
Thus all vertical block contacts, including to top and bottom walls,
have squared excess at least
\[
\boxed{g=4\beta^2h^2
=\frac{\delta^4}{25000000000000L^{20}}.}\tag{O.5}
\]

The largest second-stage displacement is less than \(3hL^3=3s^2/100\).
Each column/block contact already has squared excess at least \(s^2\)
and first-stage length below \(101/100\). The second move reduces its
squared length by less than \(2(101/100)(3s^2/100)<s^2/2\).
All these interface contacts remain strict by more than \(g\).
The column/left-wall and column/column contacts are unchanged in stage two.

Every original nonbasis pair has squared separation at least \(1+\delta\):
the shortest such steps are \(u-v\); all other nonbasis steps have squared
length at least two. Each point moves by less than \(\delta/(50L)\)
over both stages, and every reference pair length is at most \(L\).
Its squared loss is less than \(2\delta/25\), so every original
noncontact remains strict by much more than \(g\). These estimates hold
through both complete motion segments.

All targets stay strictly inside the parallelogram. Their oblique coordinate
changes in stage one are \(s(n-j)(c/a,-1/a)\), and in stage two
\(-h(m-i)f_j(1/a^2,-c/a^2)\). Each coordinate change has magnitude
less than \(1/100\), while interior coordinates started at least one from
the boundary. Each final Euclidean displacement is also less than \(1/100\).

This is an auxiliary packing construction. Its reference points are not
identified with unknown old source interior points. The source proof deletes
all such old interior points and explicitly reuses their labels.

## 3. Robust actual-wall source theorem

Set
\[
\boxed{\eta=\frac{g}{4(L+1)}.}\tag{O.6}
\]
Suppose an actual simple unit-contact cycle \(W\subset A\), with \(2L\)
distinct vertices, is within \(\eta\) pointwise of the ordered reference
frame after one Euclidean isometry. Delete its vertex corresponding to
\(p_{1,0}\). No convexity of the actual cycle is required.

Targets are mutually strict. Their distances to retained actual wall
vertices have squared excess at least \(g/2\), since moving a wall
coordinate by \(\eta\) reduces squared distance by at most
\(2(L+1)\eta\). Targets and their original reference positions remain
inside the actual cycle by positive boundary depth and the interpolation/
winding argument of the
[two-side theorem](target_c_two_side_polynomial_collective_refill_2026-10-05.md).

Every original reference interior position is at least
\(1-\eta\ge19/20\) from every actual wall coordinate, including the
deleted one. An old exterior point is at least one from those coordinates.
Their joining segment crosses an actual unit side. The relaxed crossing
lemma [B.1](target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md)
gives reference/exterior distance at least \(\sqrt{261}/10>151/100\).
Displacement below \(1/100\) leaves every final target farther than
\(3/2\) from every exterior source point. All exterior labels, including
isolates, remain fixed. The deleted wall coordinate is only a separation
reference, not a final source point.

**Theorem O.1.** Every triangle-free contact-minimal global minimizer
with the actual unit cycle above satisfies
\[
\boxed{z=|A\cap\operatorname{int}C_W|\ge K=(m-1)(n-1).}\tag{O.7}
\]
If \(z\le K-1\), delete all enclosed source points and the stated wall
vertex; insert \(z+1\) strict targets and assign the deleted labels
bijectively. Every new lower constraint is strict. Old retained pairs
are unchanged. New points lie in the interior of the old source hull, so
every pair involving them is strictly shorter than the old diameter.
Cardinality is unchanged and the maximum is at most \(D(n)\).
A smaller diameter contradicts global optimality. Equality gives a
triangle-free minimizer with fewer contacts: an actual cycle vertex and
its incident unit contacts disappeared, and no new contact was made.
Contact minimality is contradicted. Every old source point was retained
or explicitly reassigned. No stress theorem is applied to isolates.

## 4. Residual substitution with no linear boundary charge

If the actual wall is convex, define its full-population Oler residual
\[
r_W=A_W/a_0-L+1-z,\qquad a_0=\sqrt3/2.
\]
The reference area is \(mn\sin\phi\); its actual area error is at most
\(2L\eta+L\eta^2\), as in the two-side theorem. O.7 gives
\[
\boxed{r_W\le mn\left(\frac{\sin\phi}{a_0}-1\right)
+\frac{2L\eta+L\eta^2}{a_0}.}\tag{O.8}
\]
This removes the previous \(L-2\) allowance in the same actual framed
source class. It applies to all interior source points, not only isolates.
A framed macroscopic chamber exceeding O.8 is excluded.

The inequalities may be summed over any chosen frames at their exact scopes.
In particular a branch with summed framed residual at least \(\kappa D\),
for a fixed \(\kappa>0\), is impossible if the summed angular area and
area-error terms are \(o(D)\). This is a conditional branch elimination.
It does not identify overlapping local residuals with independent global
currency. The canonical positive \(R_F/D\) floor does not assert that its
residual is captured by these frames. Such capture, or a replacement for
nonframed chambers, remains necessary.

## 5. Triangular endpoint: a finite displacement gap with one missing pin

At \(\phi=\pi/3\), delete only \(p_{1,0}\) and retain all \(K\)
interior labels. For any unit-separated alternative fixing the remaining
wall, write \(\xi_{ij}=p'_{ij}-p_{ij}\) and
\(\rho=\max|\xi_{ij}|\). The alternative need not remain in the frame.

Horizontal original unit contacts give
\(u\cdot(\xi_{i+1,j}-\xi_{ij})\ge-2\rho^2\).
Both ends of each interior horizontal chain are still pinned, so
\(|u\cdot\xi_{ij}|\le2m\rho^2\).
Each interior \(u-v\) diagonal chain has constant \(i+j\ge2\).
The deleted pin has sum one, so both endpoints stay pinned.
The chain length is at most \(\min(m,n)\), yielding
\(|(u-v)\cdot\xi_{ij}|\le2\min(m,n)\rho^2\).
The dual unit-vector basis has lengths \(1/a_0\), hence
\[
\rho\le\frac{2[m+\min(m,n)]}{a_0}\rho^2
\le\frac{2L}{a_0}\rho^2.
\]
Therefore every feasible alternative satisfies
\[
\boxed{\rho=0\quad\text{or}\quad\rho\ge\frac{a_0}{2L}.}\tag{O.9}
\]
Every continuous feasible motion starting at this reference is constant.
Thus an angle-independent one-pin local strictification is false.
Distant disconnected packings are not excluded. The reference contains
unit triangles and is not a Level I counterexample.

An explicit positive pinned stress is also available. Give each original
unit contact involving an interior vertex weight one, except the contacts
from \(p_{1,1}\) to \(p_{0,1}\) and \(p_{2,0}\), whose weights are two.
Their extra vectors sum to the removed vector \(-v\).
Every interior vertex is equilibrated; every weight is positive.
The wall is pinned, not assigned fictitious diameter forces. The finite
gap proof does not infer global optimality from this stress.

## 6. Exact certificate and scope

    python3 research/verify_target_c_one_boundary_pin_oblique_refill_2026_10_05.py

Exact arithmetic in \(\mathbb Q(\sqrt3)\) checks 1,042 two-stage pair
constraints and 11,774 complete guarded source pairs, with 32 interior labels,
one funding wall label per packet and 82 contacts removed. Frames are strictly
oblique, very near triangular and square, with perturbed actual walls.
Every source pair, unchanged cardinality, fixed exterior point and complete
maximum diameter is checked. Four triangular packets separately verify 75
pinned interior vertices and 279 positive stress edges.

No guarded packet is asserted globally optimal. O.1 and the triangular
gap are analytic theorems. The existence of a deficient qualifying actual
wall is not certified, and C-II remains open.
