> Generated reading edition · [exact source](../../../docs/reports/global_vertex_factor_relocation_2026-10-12.md) · source SHA-256 `a6d34bcadceef3087ebd91529fc987e8b7053ad295d4f7a1f68ad3393cddae57`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4CA365892A3F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global vertex-factor relocation: a finite obstruction and the dimension gap


Source-main artifact frozen at `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; original working-note SHA-256: `e418340ca198a9e7bb497290c45ff482e65f7f3e38e3c22ae7126867b8cc6195`. Earlier source-history versions are not imported.
This source AI audit is retained as provenance; no independent exact-head
AI-agent mathematical audit or canonical promotion is claimed. The degree-product
barrier and alternating-graph mechanism overlap PR #960 at its frozen head
`c75e519426e3a88839567411fe3381160f3aa3cb`; the full planar classification,
nine/four-label realization failures and seven-label inversion competitor are
additional source evidence. Neither PR is used as a canonical premise.

Vertex scaling and length-cross-ratio cancellation are established background:
Bobenko, Pinkall and Springborn, [*Discrete conformal maps and ideal hyperbolic
polyhedra*](https://msp.org/gt/2015/19-4/gt-v19-n4-p07-s.pdf), Geometry & Topology
19 (2015), Sections 2.3 and 2.5, especially Proposition 2.5.1. That paper treats
triangulated metrics. The all-pair planar conclusion here is proved explicitly
in Section 6; it is not inferred from edgewise scaling on a mesh.

The preserved checker now emits the actual directed cycle and rational edge
weights instead of returning only a walk length, replays their JSON form,
distinguishes uniform versus emitted witness support, and rejects corrupted
weights, states and edge colors. It also refuses optimized Python. These are
computational/provenance repairs; the mathematical fixtures are retained.


**Date:** 2026-10-12  
**Repository base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`  
**State version:** `2026-10-10.audit.234`  
**Target:** independent whole-source Level I argument  
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`  
**Classification:** noncanonical, unreviewed candidates and exact regressions; consequential promotion requires the destination independent exact-head AI-agent mathematical audit  
**LEVEL I STATUS:** STILL OPEN.

## 1. Global mechanism being tested

The proposed route was a simultaneous finite relocation of every source label:

```text
triangle-free global minimizer
  -> planar vertex-factor relocation preserving every lower pair bound
     and making every upper pair bound strict
  -> same-cardinality strict-sub-D competitor
  -> contradiction
```

A vertex-factor relocation prescribes distances

$$
d'_{ij}=s_i s_j d_{ij},\qquad s_i>0.
\tag{1}
$$

Möbius maps, inversions and similarities give this form, including at finite
displacements far from the source. The investigation is exploratory until the
first arrow is proved. The report settles an obstruction for the entire family
and exhibits an exact obstruction to realizing its abstract relaxation in the
plane. It uses only the problem definition and elementary distance geometry;
no Target C stress, core, train, source-chart or lattice theorem is a premise.

All source labels, including contact isolates, are retained. None of the
regression sources below is asserted to be a large global minimizer.

## 2. A finite degree-balance obstruction

Let A be any finite unit-separated planar source of diameter D. Let C be its
actual unit-contact graph and H its actual diameter graph. Suppose there are
nonnegative edge weights a on C and b on H with

$$
\sum_C a_e=\sum_H b_e=1,
\qquad
\sum_{e\in C:e\ni i}a_e=
\sum_{e\in H:e\ni i}b_e\quad\hbox{for every source label }i.
\tag{2}
$$

**Candidate theorem.** Every vertex-factor distance array (1) whose contact
distances are at least one has some diameter-edge distance at least D. In
particular no feasible planar realization of (1) has diameter below D.

**Proof.** Put u_i=log(s_i). The incidence balance cancels every vertex factor:

$$
\sum_H b_{ij}\log d'_{ij}-\sum_C a_{ij}\log d'_{ij}
=\log D.
$$

The second sum is nonnegative. The first sum is at most the logarithm of the
largest transformed diameter-edge distance. This proves the assertion. The
proof has no infinitesimal, local-minimum or positive-stress hypothesis.

For a complex Möbius map f(z)=(az+b)/(cz+d), with ad-bc nonzero and no source
label at its pole,

$$
|f(z_i)-f(z_j)|=
\frac{|ad-bc|\,|z_i-z_j|}{|cz_i+d|\,|cz_j+d|}.
$$

Take s_i=sqrt(|ad-bc|)/|cz_i+d|. Complex conjugation preserves distances,
so the same result covers anti-Möbius maps. Scaling is already included.

### Exact alternatives for the abstract active constraints

Exactly one of the following holds:

1. the certificate (2) exists;
2. there is a real vertex potential u with u_i+u_j>=0 on C and
   u_i+u_j<=-1 on H.

This is the finite Farkas alternative for the unsigned edge-incidence matrices.
In an infeasibility certificate the contact and diameter weight sums agree,
because summing vertex incidence counts each edge twice; the diameter sum is
positive and can be normalized to one. Conversely (2) directly contradicts
such a potential. A sufficiently small positive constant added to all u_i
makes every contact sum positive while keeping every diameter sum negative.

Thus, in the absence of (2), d'_{ij}=exp(t(u_i+u_j))d_{ij}, for sufficiently
small t>0, satisfies *every* pair bound strictly: former contacts exceed one,
former diameter pairs fall below D, and every inactive pair keeps its finite
margin by continuity. This is a distance-array statement. Neither metric
realizability nor planar realizability follows from it.

## 3. Global circular-shell obstruction, with arbitrary interior labels

For a regular unit odd q-gon, q>=5, put k=(q-1)/2. Its q cyclic contact edges
and q step-k diameter edges each have degree two at every shell vertex. Give
each edge weight 1/q. These are the weights (2).

Consequently **no Möbius or anti-Möbius transformation, inversion, similarity,
or other full-pair vertex-factor relocation can improve its diameter while
preserving unit separation**. Adding any feasible source labels at or inside
the shell leaves the certificate intact whenever the shell diameter remains
the full-source diameter. Extra labels have zero certificate weight; they are
still present and all their pair constraints must hold in a feasible image.

This is stronger than preservation of a radius multiset. It permits the radii,
center and individual angular positions to change. It is also independent of
local rigidity and KKT stress. A unit square has the same certificate, with
contact weights 1/4 and diagonal weights 1/2.

The conclusion does not say that circular shells with dense interiors are
globally optimal. It blocks an entire class of finite transformations on
those sources, including transformations beyond a local barrier.

## 4. Exact full-pair failure of the abstract relocation

### Nine-label example: even the triangle inequality can fail

Use the 3 by 3 square grid. Assign s_i=9/10 on even checkerboard sites and
s_i=10/9 on odd sites. All twelve contact lengths remain one. Checking all
36 pairs gives

$$
\min d'^2=1,\qquad \max d'^2=40000/6561<8=D^2.
$$

Yet the two opposite edge-midpoint sites have prescribed distance 200/81,
while each is at distance one from the center. The triangle-inequality excess
is 38/81. There is no metric realization in any Euclidean dimension.

### Four-label example: a genuine three-dimensional metric still fails in the plane

Let A=0, B=u, C=u+v, E=v, with |u|=|v|=1 and u dot v=3/7.
The four cyclic edges are unit contacts; the diagonal squared lengths are
20/7 and 8/7, both greater than one. This is triangle-free.

Set r=19/20 and use vertex factors (r,1/r,r,1/r) in cyclic order. All four
contacts remain one. The transformed diagonal squared lengths are

$$
L^2=130321/56000,\qquad S^2=1280000/912247.
$$

All six transformed pair distances are at least one and at most L, and
L^2<20/7. Every triangle inequality holds, because there is an explicit
three-dimensional realization:

$$
A'=(-L/2,0,0),\quad C'=(L/2,0,0),\quad
B'=(0,S/2,h),\quad E'=(0,-S/2,h),
$$

where h^2=1-(L^2+S^2)/4>0. All four cyclic edges have length one.

There is no planar realization: four distinct planar vertices with these
four unit cycle edges form a rhombus and hence must have diagonal squared
lengths summing to four. Here L^2+S^2<4. This example survives the addition of
all metric triangle inequalities to the relaxation.

The source also lacks (2): the vertex potential (-1,1,-1,1) has contact sums
zero and sum -2 on the unique diameter edge. Thus the active-constraint
alternative does not supply a planar move.

## 5. Verification and lifecycle

Run:

```bash
python3 research/verify_global_vertex_factor_relocation_2026_10_12.py
```

The script uses exact rational arithmetic. It checks degree certificates for
odd cycle sizes 5, 7, 43 and 101 with 132 additional zero-weight labels, the
unit-square certificate, all 36 square-grid pairs and all six rhombus pairs,
the exact triangle-inequality failure and the positive three-dimensional
height/planar diagonal defect. The cycle checks certify incidence balance,
not a geometry or global optimum for the added labels. The general claims
are proved above, rather than inferred from finite instances.

| Claim | Classification | Exact effect |
| --- | --- | --- |
| Degree-balance obstruction at every finite displacement | Proved candidate awaiting promotion | Blocks a whole family of global relocations |
| Incidence alternative | Proved candidate awaiting promotion | Completely characterizes the abstract active constraints |
| Nine-label nonmetric array | Regression | Full pair bounds do not imply a metric |
| Four-label three-dimensional array | Regression | Metric feasibility does not imply planar feasibility |
| A plane competitor from incidence separation alone | Rejected | The realization step is missing |

No theorem-state promotion is made. The generated artifact lifecycle remains
unreviewed. No global optimum, unit-triangle conclusion or Level I closure
is certified.

## 6. Complete planar realization classification

**Candidate theorem.** Let p_1,...,p_n and q_1,...,q_n be two ordered sets of
distinct planar points, n>=3. If positive s_i satisfy

$$
|q_i-q_j|=s_i s_j|p_i-p_j|\quad\hbox{for all }i\ne j,
$$

then one Möbius or anti-Möbius map sends every p_i to q_i. Conversely every
such map with no source point at its pole has this distance factorization.
No noncollinearity, general position, common circle or source-contact
assumption is needed.

**Proof.** Regard the plane as the complex plane. Normalize the first three
points of each set by a Möbius map to 0, 1 and infinity. Write the normalized
remaining points as z_i and w_i. If d denotes source distances, then

$$
|z_i|=\frac{d_{i1}d_{23}}{d_{i3}d_{12}},\qquad
|z_i-1|=\frac{d_{i2}d_{13}}{d_{i3}d_{12}}.
$$

Every vertex factor cancels in these ratios, so |z_i|=|w_i| and
|z_i-1|=|w_i-1|. Hence w_i is either z_i or its complex conjugate. In addition,

$$
|z_i-z_j|=
\frac{d_{13}d_{23}d_{ij}}{d_{12}d_{i3}d_{j3}}
=|w_i-w_j|.
$$

Again all vertex factors cancel. If two normalized points have nonzero
imaginary parts, conjugating exactly one changes their squared mutual
distance by four times the product of their imaginary parts, which is
nonzero. Therefore all nonreal normalized points make the same choice.
Real normalized points are fixed by either choice. The entire normalized
configuration agrees by identity or conjugation; composing with the inverse
normalizations proves the assertion. For n=3 there are no remaining points
and the same composition sends the ordered triples. The converse is the
distance formula in Section 2.

Thus prescribing n arbitrary vertex factors provides **no additional planar
freedom** beyond conformal relocation. The all-pair requirement is essential;
factorizing only contact and diameter distances is a different problem.

### A complete pole test, including every inactive pair

Up to a Euclidean similarity or reflection, a non-affine Möbius map is an
inversion with some pole x not equal to a source point. Put

$$
g_i(x)=|p_i-x|^2,\quad
R_{ij}(x)=\frac{d_{ij}^2}{g_i(x)g_j(x)},\quad
m(x)=\min_{i<j}R_{ij}(x),\quad M(x)=\max_{i<j}R_{ij}(x).
$$

After scaling to minimum separation one, its squared diameter is M(x)/m(x).
Hence a feasible strict-sub-D vertex-factor image exists exactly when
some pole satisfies M(x)<D^2 m(x). A similarity alone cannot improve a
source whose minimum separation is already one. Equivalently, every pair
of unordered pairs e=(i,j), f=(k,l) must satisfy

$$
d_{ij}^2 g_k(x)g_l(x)
<D^2 d_{kl}^2 g_i(x)g_j(x).
\tag{3}
$$

These are strict quartic polynomial inequalities in the two pole coordinates,
with the additional restrictions g_i(x)>0. This is a finite semialgebraic
decision problem for the **entire realized class**, without discarding
inactive upper constraints or contact-isolated source points. It is not a
decision procedure for unrestricted repacking. Effective exact decision on
a particular numeric input requires exact real-closed-field input data, for
example algebraic coordinates. For arbitrary source reals, (3) is an exact
quantified feasibility criterion; no oracle-free numerical decision is claimed.

## 7. The obstruction is an alternating closed walk

The certificate (2) exists if and only if C and H contain an alternating
closed walk, with contact and diameter edges alternating. Vertices and edges
may repeat in the source walk. This is not the invalid inference from
consecutive incident diameter states to a source Euler trail.

Construct a directed graph with two states (i,C) and (i,H) at each source
label. Every contact ij gives arcs (i,C)->(j,H) and (j,C)->(i,H).
Every diameter pair ij gives arcs (i,H)->(j,C) and (j,H)->(i,C).
A directed cycle gives an alternating closed source walk with m edges of
each type. Give each edge its number of occurrences divided by m; these
are the weights (2).

Conversely assign weight a_ij to each directed contact arc and b_ij to each
directed diameter arc. Equation (2) says that incoming and outgoing weights
agree at every state. A nonzero finite nonnegative circulation contains a
directed cycle: start on a positive arc and keep following positive arcs;
balance prevents a dead end, and eventually a state repeats. Removing
repetitions produces a directed cycle of length at most 2n. Consequently
the obstruction and a short exact rational certificate can be found in
O(n+|C|+|H|) time.

For an alternating walk with m edges of each type, the product

$$
\frac{\prod_{\text{diameter occurrences}}d_{ij}}
     {\prod_{\text{contact occurrences}}d_{ij}}
$$

is invariant under vertex factors. Its original value is D^m. In a feasible
placement of diameter D'<D its value would be at most D'^m, so it must
change. More quantitatively, for any attempted vertex potential u and a
feasible strict competitor, at least one certificate edge satisfies

$$
\left|\log\frac{d'_{ij}}{d_{ij}}-u_i-u_j\right|
\ge\tfrac12\log\frac{D}{D'}.
$$

This follows by subtracting the two weighted residual averages in (2).
It applies to arbitrary feasible competitors, even those outside the
vertex-factor family: it measures a distortion they must introduce.

## 8. A complete full-source inversion competitor

Take the five rod sites (x,0), -2<=x<=2 with integer x, and the two additional
labels (0,7/5), (0,-7/5). The seven-label source is unit-separated, has
diameter four and exactly four unit contacts, all on the rod. The additional
labels are strict contact isolates. Every feasible affine map has diameter
at least four: the rod's unit step must retain length at least one, so its
four-step endpoint distance is at least four.

Invert about x=(0,10), then scale by sqrt(104*101). The inversion identity
gives all 21 pair distances exactly. The final minimum squared separation is
one and the final maximum squared distance is

$$
202/13<16,
$$

an improvement of 6/13 in squared diameter. Every isolate-involving pair
remains strictly above one. No label is deleted. This is an actual planar
competitor; its coordinates are rational times one common square root.
It shows that the tactic can beat affine resistance with a finite nonlinear
map. Neither source is claimed to be globally optimal, and a seven-label
example does not settle any eventual quantifier.

The expanded verifier also checks the complete pole-distance formula on this
source, exact Möbius and anti-Möbius cross-ratio identities on a six-label
configuration, and alternating-walk certificate extraction on the earlier
cycle and square fixtures. It confirms no alternating certificate on the
square-grid or rhombus regression. Finite checks support the general proofs;
they do not replace them.

## 9. Global consequence and next obligation

The entire plane-realizable vertex-factor strategy has now been classified.
Balanced sources block it at every finite displacement, even when a more
general repacking improves their diameter. The abstract incidence alternative
cannot bypass this obstruction by supplying n independent scaling variables:
if its full-pair array is planar, it is already Möbius or anti-Möbius.

New classification, alternating-walk and pole-test claims are proved
candidates awaiting promotion. The verifier and generated lifecycle remain
unreviewed; the canonical state remains Level I OPEN / C-II OPEN.

The next global obligation is to construct, for every sufficiently large
triangle-free global minimizer possessing an alternating certificate, a
same-cardinality planar competitor that changes its alternating distance
product while checking every pair. Sources without that certificate can be
tested by (3), but absence of the certificate does not prove the pole system
feasible. There is no general strict competitor for either case yet. The
source report and exact checker remain unreviewed candidates; this text does not
restore the withdrawn global K-prime-over-D chart or q=O(D^(4/5)) inference.
