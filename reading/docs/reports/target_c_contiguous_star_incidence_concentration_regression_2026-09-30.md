> Generated reading edition · [exact source](../../../docs/reports/target_c_contiguous_star_incidence_concentration_regression_2026-09-30.md) · source SHA-256 `eb45f85ef22f83e642cc6a4b966ca3bd27142433e0ba0fa4bf396f29b1d826a7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1305569AD66E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: concentrated incidence in near-disk contiguous diameter stars

**Date:** 2026-09-30<br>
**Base main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Classification:** regression, with an analytic proof; noncanonical.<br>
**Level I:** open. C-II remains open.

## Claim ruled out

Near-disk geometry, nearly maximal loaded-hull perimeter and vertex population,
an exact diameter-V cover, and contiguous diameter stars do **not** imply that
a sublinear set of diameter vertices has sublinear total degree. They also do
not imply an absolute degree bound, an $`O(\sqrt D)`$ degree bound, or any
fixed sublinear power bound on the maximum degree.

This regression is a shell, not a global minimizer or a harmonic rhombic core.
It does not refute a theorem whose additional hypotheses genuinely use those
source structures.

## Exact family

Let $`p\ge9`$ be odd, let $`D=p^3`$, and put
```math
\rho_p=\frac{D}{2\cos(\pi/(2p))},\qquad
c_j=\rho_p(\cos(2\pi j/p),\sin(2\pi j/p)).
```
Let $`K_p=\bigcap_j\overline B(c_j,D)`$. Between consecutive vertices
$`c_i,c_{i+1}`$, the boundary of $`K_p`$ is the minor radius-$`D`$ arc
centered at $`c_{i+(p+1)/2}`$. Its central angle is $`\pi/p`$.

Put
```math
\delta_D=2\arcsin\frac1{2D},\qquad
r=\left\lfloor\frac{\pi}{p\delta_D}\right\rfloor,
\qquad \beta=\frac{\pi}{pr}\ge\delta_D.
```
Subdivide each of the $`p`$ boundary arcs into $`r`$ equal angular steps
$`\beta`$, and take all their endpoints as the finite source $`A_p`$.
Shared arc endpoints are counted once. Thus $`q=|A_p|=pr`$.

The exact properties are
```math
\operatorname{diam}A_p=D,\quad
\min_{x\ne y\in A_p}|x-y|\ge1,\quad h=q,
```
```math
R_D=m_D=d_H=0,
\qquad \deg_H(c_j)=r+1,
\qquad \deg_H(x)=1\quad(x\notin\{c_j\}).
```
In particular, for the corner set $`X_p=\{c_0,\ldots,c_{p-1}\}`$,
```math
|X_p|=p=o(D),\qquad
\sum_{v\in X_p}\deg_H(v)=p(r+1)=q+p=(\pi+o(1))D.
```
Every star is contiguous; the graph is an odd cycle with pendant leaves.

## Proof of the geometry

### Boundary arcs and constant width

The regular $`p`$-gon has largest chord $`D`$, attained from each vertex
to its two opposite neighbors. Hence every $`c_j`$ belongs to $`K_p`$.

For the stated arc centered at $`c`$, write its endpoint unit rays as
$`u_1,u_2`$, separated by $`\pi/p`$. An intermediate unit ray is
$`u=a u_1+b u_2`$, with $`a,b\ge0`$ and $`a+b\ge1`$. For every other
center $`c_j`$, endpoint membership in its disk gives
```math
u_i\cdot(c_j-c)\ge\frac{|c_j-c|^2}{2D}\quad(i=1,2).
```
The same inequality holds for $`u`$. Thus the entire arc belongs to all
the disks, and to the boundary of the disk centered at $`c`$.

At an interior arc point $`x=c+Du`$, the outward support direction is
$`u`$. At $`c`$, the two disks centered at the arc's endpoints give
supporting directions $`-u_1,-u_2`$; their positive cone includes $`-u`$.
Therefore $`x`$ maximizes and $`c`$ minimizes projection in direction $`u`$,
and the width is exactly $`D`$.

Around the boundary, the normal rotates by $`\pi/p`$ on every arc and
by $`\pi/p`$ at every corner. These arcs and corner cones cover all
support directions. The preceding antipodal pairing proves width $`D`$
in every direction, and hence diameter $`D`$. It also identifies the whole
boundary as the stated cyclic arc chain.

### Separation

Two samples on the same arc have distance at least
$`2D\sin(\beta/2)\ge1`$.

For samples on adjacent arcs, other than their common corner, each has
arc distance at least one from that corner. The tangent directions along
the intervening boundary chain lie in a cone of width at most $`3\pi/p`$.
Projection onto its middle direction gives distance at least
```math
2\cos\frac{3\pi}{2p}\ge\sqrt3>1.
```
If one sample is the common corner, the same-arc bound applies.

For nonadjacent arcs the minor polar-angle separation is at least
$`2\pi/p`$. All boundary points have radial distance at least
$`D-\rho_p`$, since the disk of that radius is contained in every defining
disk. Their distance is therefore at least
```math
2(D-\rho_p)\sin(\pi/p)>1\qquad(p\ge9, D=p^3).
```
For example $`D-\rho_p>D/3`$ and $`\sin(\pi/p)\ge2/p`$ give the
explicit lower bound $`4p^2/3`$.

### Full diameter graph

An interior arc point has a unique outward normal on $`K_p`$, so its only
diameter partner is its arc center. Each corner has the two opposite
corners as partners, together with the $`r-1`$ interior samples on the
arc it centers. There are no other diameter pairs: a diameter chord must
be a pair of opposite support points of the constant-width body. The corner
cones pair precisely with their opposite arcs, as proved above.

The corner-corner diameter edges form one odd cycle, since
$`\gcd(p,(p-1)/2)=1`$. There are $`p(r-1)`$ pendant edges. Thus
$`h=p+p(r-1)=pr=q`$, and every corner has degree $`r+1`$.

The exact-contiguity theorem in
`target_c_exact_diameter_star_contiguity_2026-09-30.md` now gives
$`R_D=m_D=0`$ and a diameter-V cover of every hull side.

## Simultaneous endpoint properties

All hull sides have the same length
$`s=2D\sin(\beta/2)=1+O(p/D)`$. Moreover
```math
q=\pi D-O(p),\qquad
P_F=2qD\sin\frac{\pi}{2q}=\pi D-O(D^{-1}),
```
so $`P_F-q=O(p)=o(D)`$. The radial sandwich
```math
\overline B(0,D-\rho_p)\subset K_p\subset\overline B(0,\rho_p)
```
has normalized thickness $`O(p^{-2})`$. The sampled hull has the same disk
limit, since its arc sagitta loss is $`O(D\beta^2)=O(D^{-1})`$.

Thus $`D^{-1}F_p`$ tends to the radius-$`1/2`$ disk in Hausdorff distance,
while $`q/D\to\pi`$, $`h/D\to\pi`$, $`s\to1`$, and the diameter-V
cover is exact. Yet a sublinear corner population carries linear degree mass.
Here the maximum degree is $`\Theta(D^{2/3})`$.

Replacing $`D=p^3`$ by $`D=p^L`$, for any fixed integer $`L>1`$, gives
maximum degree $`\Theta(D^{1-1/L})`$ with the same conclusions. This rules
out any universal fixed exponent strictly below one from these shell
hypotheses alone. It does not rule out an $`o(D)`$ maximum-degree theorem.

## Exact finite audit

`research/verify_diameter_star_contiguity.py` uses integer/Fraction arithmetic
and cross-product direction sorting. It checks all 4,017 subsets of size at
least three of a $`4\times3`$ integer grid (934 have a two-dimensional loaded
hull), plus an exact rational non-star fan of diameter degree 81. All
contiguity, adjacency-count, and hull-side-cover checks pass. This finite
enumeration is an audit of examples, not the proof of the universal theorem
or of the analytic asymptotic family above. It contains no odd-cycle case;
the analytic proof covers that case.

## Consequence and remaining obligation

The re-entrant incidence set is empty by the contiguity theorem. Concentrated
incidence can still live on ordinary star centers. Any train/star closure must
use the actual harmonic carrier, source contacts, stress, or global optimality
to bound that concentration or to force a paid source defect.

Neither this shell nor the finite audit is a triangle-free global minimizer
certificate. No original source point is deleted or replaced in any claimed
application. No canonical branch is declared closed.
