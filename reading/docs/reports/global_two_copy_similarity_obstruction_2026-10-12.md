> Generated reading edition · [exact source](../../../docs/reports/global_two_copy_similarity_obstruction_2026-10-12.md) · source SHA-256 `b74d8e057fdeb64e3b26eb760058b4165ea68cf86e7d7efd814ab2dde9beb982`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D6643C9DCA8D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Global two-copy similarity replacement: an infinite obstruction

**Claim classification:** regression. **Artifact lifecycle:** unreviewed;
noncanonical. **Level I:** open. This report supplies no global minimizer.

**Run base:** `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
**State version:** `2026-10-10.audit.234`.
**Target:** the whole-problem Level I quantifier, through a full-source strict
diameter competitor. No C-II stress or chart theorem is assumed.

## 1. Mechanism tested and disposition

The proposed mechanism was to offer each source label a choice between two
arbitrary similarity copies of the source, then select all choices
simultaneously. Pairwise feasibility is a Boolean constraint problem, so it
avoids assuming that separate exchanges can be combined. Nevertheless, the
following infinite family defeats the entire mechanism while admitting an
explicit strictly smaller-diameter replacement of the complete source.

The implication chain being tested was

`triangle-free global source -> feasible two-copy selection -> same-cardinality
strict-sub-D competitor -> contradiction`.

The first arrow cannot follow merely from triangle-freeness, quadratic
population, or even asymptotically optimal leading density. The family below
is nonglobal; it does not disprove the version with genuine global optimality
as a hypothesis. It shows that such a version needs to use that hypothesis.

## 2. Infinite full-source family

Let q be any odd integer at least 33. Choose rational numbers p_q with

    pi < p_q <= 22/7,       p_q -> pi,

and put

    a = q/(2p_q),  rho = floor(a)-4,  s = 1+1/q,
    R = 1/(2 sin(pi/q)),   a0 = sqrt(3)/2.

Let Lambda be the unit triangular lattice with basis (1,0),
(1/2,sqrt(3)/2). Form A_q from the q vertices of the regular unit-side
q-gon centered at the origin and **every** point of s Lambda in the closed
disk of radius rho. Every interior label is retained.

Since pi < p_q, R >= q/(2pi) > a and rho <= a-4 < R-4.
Thus every rim-interior distance exceeds four. Interior distances are at
least s>1. Rim unit contacts are exactly the cycle C_q, so A_q is
unit-separated and triangle-free, and all interior labels are contact
isolates. Its complete actual diameter graph is the rim cycle with step
(q-1)/2, because this step is coprime to q. Its actual diameter is

    D_q = 2R cos(pi/(2q)) = cos(pi/(2q))/sin(pi/q).

Indeed, every pair incident to an interior point has distance at most
2R-4. The elementary bound below gives D_q>2R-2, so these pairs are not
actual diameter pairs. There are no omitted active upper constraints.

The lattice disk population estimate from its Voronoi cells gives

    |A_q| ~ (pi/a0) R^2 ~ (pi/(4a0)) D_q^2.

Here p_q->pi, rho=a+O(1), and s->1. Thus these are triangle-free sources
with the optimal leading planar packing coefficient, not just thin rims.
They are still nonglobal, as the next section proves by a full replacement.

## 3. An explicit complete-source strict competitor

Take the **fixed-phase** packet

    X_q = Lambda intersect closed_disk(a-1).

We prove that X_q has more points than A_q. The unit triangular lattice
has Voronoi cell area a0 and covering radius b=1/sqrt(3). For every r>=b,
and every lattice spacing t>0, its disjoint Voronoi cells give

    |Lambda intersect disk(r)| >= pi(r-b)^2/a0,
    |t Lambda intersect disk(r)| <= pi(r/t+b)^2/a0.

The first inequality covers disk(r-b) by cells whose centers lie in
disk(r); the second contains all counted cells in disk(r+t*b).
Consequently, writing N for the interior isolate count,

    |X_q|-(N+q)
      >= (pi/a0)[(a-1-b)^2-(a-4+b)^2]-q
       = (pi/a0)(3-2b)(2a-5)-q.

We have b<3/5, a0<7/8, pi>3, q=2p_q a<=44a/7, and
a>=7q/44>=21/4. These inequalities imply

    |X_q|-|A_q| > (212a-1080)/35 >= 33/35 > 0.

Select any |A_q| points of X_q. They are mutually at least unit distance
apart, and their complete diameter is at most 2a-2. On the other hand,
sin x<=x and cos x>=1-x^2/2 give

    D_q >= q/pi-pi/(8q) > q/p_q-p_q/(8q)
        = 2a-p_q/(8q) > 2a-2.

This is a strict, same-cardinality, whole-source competitor. It replaces
the rim and every interior isolate, and checks lower and upper constraints
for the entire replacement using lattice integrality and the common disk.
No density approximation is being used as an optimality certificate.

For the earlier identification of the actual diameter graph, put
x=pi/(2q). The inequalities 1-cos x<=x^2/2 and
sin(2x)>=4x/pi give

    2R-D_q = (1-cos x)/sin(2x) <= pi^2/(16q) < 2.

The sine bound follows from concavity on [0,pi/2]. This proves the required
strict margin over every isolate-involving upper pair.

## 4. Why every two-copy similarity selection fails

Let T_0,T_1 be arbitrary planar similarities with scale factors
sigma_0,sigma_1>0. Offer label i the two sites T_0(p_i),T_1(p_i),
and select exactly one site for **every** label. Translations, rotations,
and reflections are unrestricted. Suppose the selected full source were
unit-separated and had diameter strictly below D_q.

If both scale factors are at least one, every rim diameter edge must have its
endpoints in different copies. This would two-color the odd diameter
cycle, which is impossible.

If both scale factors are strictly below one, every rim contact edge must
have its endpoints in different copies. This would two-color the odd
contact cycle, also impossible.

In the remaining case, let copy 0 be noncontracting and copy 1 be strictly
contracted. Labels assigned to copy 0 must be an independent set in the
diameter cycle; labels assigned to copy 1 must be an independent set in
the contact cycle. Each independent set has at most (q-1)/2 labels.
Their union therefore contains at most q-1 of the q rim labels, a
contradiction. Exchanging the copy names gives the other mixed case.

These arguments use only within-copy distances. Cross-copy feasibility
cannot repair the contradiction. The arbitrary quadratic isolate cloud
is included throughout and cannot repair a contradiction on the rim.

## 5. Exact certificates and limits

Run:

    python3 research/verify_global_two_copy_obstruction_2026_10_12.py

The verifier uses integer arithmetic and fractions. Machin's identity
and alternating-series remainders supply p_q with interval width below
q^-3. Integer quadratic forms enumerate the entire interior cloud and
the entire fixed-phase competitor for q=33,65,129,257. A lattice site's
squared norm is m^2+mn+n^2; every nonzero lattice difference has squared
norm at least one. The packet's common rational disk bounds every pair.
It also checks implication cycles proving the two-copy Boolean formula
infeasible for all four scale-factor cases, at odd q from 5 through 1025
in the listed sample. The infinite proof is Sections 2--4, not enumeration.

The report proves no global source or Level I result, no obstruction to
three or more copies, and no obstruction to general affine maps that
expand some directions. All claims remain unpromoted.

## 6. Global attempt ledger and next obligation

Several different mechanisms were considered before this one:

- Full boundary-layer replacement has a precise retained-count bottleneck;
  area density alone does not pay every deleted actual diameter endpoint.
- First-order affine contraction is already blocked by existing regressions;
  it does not justify nonlinear full-source replacement.
- Convex area deficit alone cannot improve circumradius error from order
  sqrt(D) to order D^(1/3). An exact geometric regression is given below;
  it asserts no unit-separated source or global minimizer.
- Source-wide selective isometries fail automatically on an odd diameter
  cycle; allowing one contracted copy does not remove the obstruction.

The last failure is now exact and holds at unbounded quadratic cardinality.
It rules out a broad elementary replacement mechanism; it does not narrow
the mission to a small exceptional chart.

**Next global obligation:** obtain a same-cardinality strict-sub-D packet
from genuine global optimality in a triangle-free source without restricting
the packet to two similarity copies or silently replacing the source's
finite population requirement by its leading density. The canonical
Level I claim and all A/B/C open endpoints remain unchanged.

## 7. Independent roundness regression

For each integer M>=5, set D=M^2, t=M/4, and prescribe the support function

    h(theta)=D/2+t cos(3theta).

Its curvature radius is h+h''=D/2-8t cos(3theta)>0, so it defines a smooth
strictly convex body. Its width is h(theta)+h(theta+pi)=D, hence its
diameter is exactly D and its perimeter is pi D. The support-function area
formula gives

    area = (1/2) integral(h^2-h'^2) = pi D^2/4-4pi t^2
         = pi D^2/4-pi D/4.

Its threefold rotational symmetry forces its circumcenter to the origin.
The boundary's squared radius, writing c=cos(3theta), is

    D^2/4+Dtc+t^2(9-8c^2).

This is increasing for -1<=c<=1 because Dt-16t^2>0. Thus the circumradius
is exactly D/2+t. The area deficit pi D/4 is smaller than
(sqrt(3)/4)pi D, while the circumradius excess sqrt(D)/4 is not O(D^(1/3)).
Therefore those area/perimeter data, even at the constants of the
canonical full-source geometric bound, do not yield the proposed stronger
circumradius rate. The example is a convex body, not a packing or an
optimal configuration. This auxiliary claim is classified as a regression.

## 8. Literature near miss: sequential free-position propagation

Schurmann's [2006 original paper](https://ems.press/content/serial-article-files/25994?nt=1),
Definition 1 and Theorem 2 (pp. 395--396), treats a fixed smooth convex
container and packing families with two uniform controls: bounded difference
vectors have finitely many accumulation points after isometries, and affine
spans of unit neighbors stay a fixed positive distance from their center
unless they contain it. Propositions 2--4 (pp. 398--401) use these controls
to seed and propagate free positions, eventually placing all labels inside
the old center hull. This is a useful whole-source mechanism, with additional
hypotheses; it is not a theorem about arbitrary triangle-free diameter
minimizers.

Our family fails both controls, by direct calculation. Its rim unit-contact
directions are an equally spaced angular grid, which accumulates on the
entire unit circle as q grows. Applying a separate isometry to each source
does not change that conclusion. At any rim vertex, the line through its
two unit neighbors has positive distance

    R(1-cos(2pi/q)) = sin(pi/q) = 1/(2R)

from the vertex. This distance tends to zero. The interior isolates add no
unit neighbors. Thus triangle-freeness and optimal leading density supply
neither uniform control. No theorem from that paper is imported into the
canonical ledger, and no free-region seed is asserted for global sources.

## Preservation and bounded independent review (2026-10-15)

Exact source: `refs/heads/research/global-replacement-20261012` at `dc2ee46429fc8ad87602c9b85f9af5c900b3fb40`.
This artifact was absent from the maintenance baseline main and has a distinct
mechanism from the open attainment/matching/global drafts. Original source
authors and attribution remain in that commit. OpenAI Codex inspected the
elementary proof and replayed the exact finite checker while preserving this
checkpoint; that is AI-assisted review, not independent human peer review.
The lifecycle remains unreviewed and no canonical theorem is promoted.

Import changes are trailing-whitespace normalization, regenerated lifecycle
metadata, this provenance paragraph, and a fail-closed optimization guard in the
checker. Python optimization disables assertions, so the checker now refuses
`-O` instead of printing unchecked success. No mathematical input was changed.
Historical literature comparisons were not re-audited during preservation and
are not newly admitted canonical dependencies.

A bounded reviewer assignment is to check all four scale-factor cases, the odd
contact/diameter cycles and the strict same-cardinality lattice count, retaining
every isolate. Independently verify the implication paths in the finite Boolean
certificates. No assertion about three copies, arbitrary affine maps or general
replacement is made. The missing Level I implication would have to use genuine
global optimality to produce a strict competitor beyond two similarity copies;
this family is explicitly nonglobal.
