<!-- theorem-state: {"artifact_id":"ART-4C5B829B3C39","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Level I — full-source Voronoi triangle-slack budget

**Date:** 2026-10-11  
**Base commit:** `ab6dd333`; independent branch checkpoint `9a30feac`  
**State version:** `2026-10-10.audit.234`  
**Route:** global full-source geometry, outside the A/B/C source reductions  
**Classification:** proved candidate awaiting promotion; unreviewed report  
**Level I:** OPEN

This argument applies to every global minimizer and retains every original label,
including contact isolates. It does not assume a large stressed core, a lattice
chart, an ear cover, or a regular boundary. No other worker's solution is used.
The packing comparison and finite Oler inequality are the only packing inputs.

The exact endpoint remains eventual vanishing of the global triangle-slack maximum
Gamma_n(D(n)) defined in the preceding independent report. The result here is a
finite quantitative estimate and a full-source cell budget, not that vanishing.

## 1. Statements

Put

\[
 a_0=\sqrt3/2,\qquad a=\pi/(2\sqrt3),\qquad
 T(A)=\min_{i<j<k}\bigl(|p_i-p_j|^2+|p_i-p_k|^2+|p_j-p_k|^2-3\bigr).
\]

**Candidate theorem A.** Every planar unit-separated global n-point diameter
minimizer A with D=D(n)>=4096 satisfies

\[
 \boxed{T(A)<3312/D.}
\tag{1}
\]

Thus Gamma_n(D(n))<=3312/D(n) in that regime. This gives no equality-to-zero
claim; a sequence of positive slacks can obey (1).

**Candidate theorem B.** If D>=8192, A contains at least floor(n/150)
pairwise label-disjoint triples such that every squared side length lies in

\[
 [1,1+6624/D].
\tag{2}
\]

These are approximate triangles, not asserted unit-contact triangles. In particular
a contact-isolated original point can belong to one of these triples.

The proof supplies the more informative finite inequality (10) below. Its closing
chain would require an additional boundary-payment theorem:

```text
an exact source-wide payment for the exceptional/clipped Voronoi cells
  -> zero residual in the unaffected original cells
  -> an original unit equilateral triangle, contradicting triangle-freeness.
```

That payment is not proved here. Replacing it by an O(D) error loses the exact
conclusion. The present results are global progress toward that endpoint, not a
claim that approximate triangles settle it.

## 2. A quantitative polygon lemma

Let V be a bounded convex polygon containing the radius-1/2 disk about the origin.
Suppose every vertex has radius at least

\[
 r_\gamma=\sqrt{3+\gamma}/3,\qquad \gamma\ge0.
\]

Set

\[
 x_\gamma=\arccos\frac{1}{2r_\gamma},\qquad
 F(\gamma)=\frac{\pi\tan x_\gamma}{4x_\gamma}.
\]

Then

\[
 \operatorname{area}V\ge F(\gamma),\qquad
 F(\gamma)\ge a_0+\gamma/36\quad(0\le\gamma\le1).
\tag{3}
\]

For gamma=0, equality in the first bound requires the regular hexagon with
inradius 1/2 and circumradius 1/sqrt(3).

### Sector proof

For consecutive vertex vectors v,w put R=|v|, S=|w|, and let theta in (0,pi)
be their central angle. The supporting line of edge vw has distance at least
1/2 from the origin. Its squared distance is

\[
 h^2=\frac{R^2S^2\sin^2\theta}{R^2+S^2-2RS\cos\theta}
 \le RS\cos^2(\theta/2),
\]

using R^2+S^2>=2RS. Consequently

\[
 RS\ge\max\left\{r_\gamma^2,\frac1{4\cos^2(\theta/2)}\right\},
\]

and the sector-triangle area is at least

\[
 g_\gamma(\theta)=
 \max\left\{\frac{r_\gamma^2}2\sin\theta,
                    \frac14\tan(\theta/2)\right\}.
\]

The two terms agree at theta=2x_gamma. The first term divided by theta
decreases on (0,2x_gamma], and the second divided by theta increases on
[2x_gamma,pi). Thus

\[
 g_\gamma(\theta)/\theta\ge
 \frac{\tan x_\gamma}{8x_\gamma}.
\]

Sum the sector angles to 2pi to prove the first bound in (3). At gamma=0,
equality forces every theta=pi/3, R=S=1/sqrt(3), and all edge line distances
1/2, giving the stated hexagon.

For the second bound, write gamma=(9/4)sec^2(x)-3. On 0<=gamma<=1,
pi/6<=x<pi/4. Direct differentiation gives

\[
 \frac{d}{dx}\frac{\pi\tan x}{4x}
 =\frac{\pi}{4x^2}(x\sec^2x-\tan x).
\]

Since

\[
 x\sec^2x-\tan x=\int_0^x2u\sec^2u\tan u\,du\ge2x^3/3,
 \qquad \frac{d\gamma}{dx}=(9/2)\sec^2x\tan x\le9,
\]

we have F'(gamma)>=pi*x/54>=pi^2/324>1/36. Also F(0)=a_0.
Integrating proves (3). No numerical trigonometric evaluation is a certificate
for this derivative bound; the inequalities above are its analytic proof.

### Periodic packing consequence

For any unit-separated planar packing with a full-rank translational period
lattice and all triple slacks at least gamma>=0, every full Voronoi cell is
bounded and satisfies (3). The mean cell area is the
reciprocal of the point density rho, so

\[
 \rho\le1/F(\gamma)\le1/(a_0+\min\{\gamma,1\}/36).
\]

Every triangle-free periodic packing has a positive minimum triple slack: after
using periodicity, only finitely many triples with a bounded total squared length
need be considered, and all have positive slack. Its density is therefore
strictly below 1/a_0. The gap is not uniform over triangle-free periodic
packings. Oblique unit lattices with angle tending to pi/3 show that neither
gamma nor the density deficit has a uniform positive lower bound. This
consequence uses actual packing sites, not a reference lattice chart.

## 3. Voronoi radius from an original triple

If three points lie on a circle of radius r centered at z, then

\[
 \sum_{i<j}|p_i-p_j|^2
 =9r^2-|\textstyle\sum_i(p_i-z)|^2\le9r^2.
\tag{4}
\]

Thus any triple with triangle slack at least gamma has circumradius at least
r_gamma. At a vertex of a bounded Voronoi cell of a unit-separated set, at
least three noncollinear sites are equidistant from that vertex. If those sites
are original labels and all their triple slacks are at least gamma, (4) gives
the vertex-radius hypothesis of (3). The cell contains the radius-1/2 disk
about its site by unit separation. Hence (3) applies to it.

This handles cocircular degeneracies: choose any noncollinear triple among
the equidistant original sites. No generic Delaunay assumption is needed.

## 4. Saturation without losing original labels

Let K=conv(A), P=per(K), and |A|=n. First,

\[
 n\ge aD^2.
\tag{5}
\]

Indeed translation-averaging a unit triangular lattice of covolume a_0 in an
open radius-sqrt(a_0*n/pi) disk gives some translate with at least n points.
Their finite diameter is strictly below twice the disk radius. This is a valid
global comparison, giving the weaker (5) immediately. It does not identify the
comparison packing with A or any of its points.

For the stated large-D regimes K is two-dimensional: a collinear unit-separated
set has at most D+1 labels, incompatible with (5) for D>=4096.

Extend A, inside the same K, to an inclusion-maximal unit-separated set B. Such
a finite extension exists since Oler bounds its cardinality. Let m=|B|-n.
Canonical Oler (shared theory, Lemma 21.1), the isodiametric inequality, and
P<=pi D give

\[
 m\le\operatorname{area}K/a_0+P/2+1-n\le P/2+1\le\pi D/2+1.
\tag{6}
\]

Maximality means every point of K is at distance strictly less than one from
some B-site. The added sites are auxiliary objects, not source labels and not
assumed to respect original triangle slack. Their possible effects are charged
explicitly below.

Call an original label good if it has distance at least one from boundary K
and distance greater than two from every added site. Its full Voronoi cell in B
is bounded and lies inside K. Otherwise a segment from its site to a point of
the cell outside K would cross boundary K at a cell point at distance at least
one from the site, contradicting the strict saturation cover.

At every vertex of that cell, the common closest-site radius is strictly below
one, because the vertex lies in K. Every neighboring site is within distance
less than two of the original site. Therefore no added site participates at
such a vertex. All defining triples consist entirely of original labels.

## 5. Finite exceptional-label count

At most 25 unit-separated sites fit in any radius-two disk, by comparing their
disjoint radius-1/2 disks with the enclosing radius-5/2 disk. Since an added
site itself occupies one of those 25 places, it has at most 24 original sites
within distance two. Thus proximity to the m additions excludes at most 24m
original labels.

The number of original labels at boundary distance less than one is at most

\[
 8P/\pi+1\le8D+1.
\tag{7}
\]

To see this, their disjoint radius-1/2 disks lie in the outer radius-1/2 parallel
body of K but outside the inner radius-3/2 erosion. The area of this region is
at most 2P+pi/4. The outer part has area P/2+pi/4 by Steiner's formula. The
inner strip has area at most (3/2)P, by integrating the perimeters of inner
parallel bodies, each at most P; the same inequality holds if the erosion
is empty. Divide by pi/4 to obtain (7).

If b is the actual number of excluded original labels, (6)--(7) imply

\[
 b\le(12\pi+8)D+25<46D\qquad(D\ge4096).
\tag{8}
\]

The constants are deliberately coarse. This is a count of original labels,
not a claim that additions, boundary cells, and contact isolates coincide.

## 6. An exact local-slack budget

For each good original site p, let gamma_p be the minimum triangle slack among
all noncollinear original triples containing p at a vertex of its B-Voronoi cell.
This is a nonempty finite set of triples. Put eta_p=min(gamma_p,1).

The good cells have disjoint interiors, lie in K, and by (3)--(4) have area at
least a_0+eta_p/36. Consequently

\[
 \boxed{
 a_0(n-b)+\frac1{36}\sum_{p\text{ good}}\eta_p
 \le\operatorname{area}K.
 }
\tag{9}
\]

Define the full-source excess g_A=n-aD^2 and the isodiametric deficit
J_K=pi D^2/4-area(K). Combining (9) with a_0*a=pi/4 gives

\[
 \boxed{
 \sum_{p\text{ good}}\eta_p
 \le36\{a_0(b-g_A)-J_K\}\le36a_0b.
 }
\tag{10}
\]

Both quantities on the right use the entire original source. In particular
canonical stronger population reserves can be inserted into (10), at their
own recorded scopes, but are not needed in this proof.

If the original source has no unit triangle, every gamma_p is strictly
positive. This forces a strictly positive exceptional-cell allowance; it does
not contradict the O(D) bound (8). The exact source-wide boundary payment
needed to turn this positivity into a contradiction is still absent.

## 7. Proofs of the two global conclusions

For D>=4096, (5), (8), and a>3/4 give n-b>=n/2. Let gamma=T(A) and
eta=min(gamma,1). Every good gamma_p>=gamma, so (10) implies

\[
 \eta\le\frac{36a_0b}{n-b}
 <\frac{72a_0\,46D}{aD^2}
 =\frac{3312(3/\pi)}D<\frac{3312}D<1.
\]

Thus gamma<1 and (1) follows. This also covers minimizers already containing
a unit triangle, for which gamma=0.

For D>=8192 set tau=6624/D<1. Here b<=n/4. By (10) and a_0<a,

\[
 \#\{p\text{ good}:\eta_p>\tau\}
 \le\frac{36a_0b}{\tau}<\frac{a_0D^2}4<\frac n4.
\]

At least n/2 good original labels therefore have gamma_p<=tau. For each such
label choose an attaining triple. It has three original labels, includes p,
and all its squared sides are at most 1+tau because each squared side is at
least one and their total excess is at most tau.

A fixed label belongs to at most 25 of these chosen triples: the labels p
choosing them lie within distance sqrt(1+tau)<2 of that label. A greedy
label-disjoint selection therefore removes at most 75 chosen triples per
selection. It retains at least floor(n/150) triples, proving (2).

## 8. Dependencies, verification, and limits

- `docs/problem/statement.md`: exact global quantifiers and source definition.
- `docs/theory/03-oler-shell.md`, Lemma 21.1: canonical finite Oler inequality.
- Translated-lattice averaging: directly proved in Section 4 above.
- Isodiametric and convex parallel-body formulas: standard finite planar
  geometry; all normalizations are displayed above.
- No KKT, stress, source-core, lattice extraction, or unreviewed route theorem
  is a premise.

`research/verify_level_i_voronoi_triangle_slack_2026_10_11.py` constructs exact
rational-coordinate Voronoi cells, checks every original pair and triple in its
finite fixtures, checks the defining equidistant triples at every cell vertex,
and certifies the area margin in (3) using rational or Q(sqrt(3)) comparisons.
It also checks the rational constant budgets for (1)--(2). These are finite
certificates for examples and arithmetic, not a computation over all minimizers.
The analytic arguments establish the stated universal candidate bounds.

**Remaining Level I gap:** (1) and (2) permit strictly positive slacks tending
to zero. Source-wide boundary/exceptional-cell payment or a compatible global
repacking is required to force an actual unit triangle. Neither the full-core
nor the macroscopic inactive-container branch is closed by these estimates.
