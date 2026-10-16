<!-- theorem-state: {"artifact_id":"ART-1005F2079C1B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_nearchain_interior_and_vertex_defects_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=698daa3829458359e6a5f49d9d89b1b959a63e65; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős #99 — near-chain interior localization and exact vertex-defect regressions

**Date:** 2026-09-09
**Base:** `d4c46e65ee2f7a1be449532132ad6bf4c32c4f63`, with prior user edits preserved
**Run type:** structural theorem and adversarial regression
**Target:** conditional C100–C102 near-chain branch
**External web search:** not used; no new literature imported
**Computation:** `research/nearchain_vertex_regressions.py` (exact symbolic arithmetic)

## LEVEL I STATUS

**STILL OPEN.** These are conditional branch advances and exact local regressions,
not a proof that the C100 hypotheses hold for every global minimizer. In particular
they do not repair C53/C63 or the force-bulk error identified in the previous audit.

## 1. Starting endpoint and implication chain

C102 proposes recovering the C97 degree-four strip by proving that sufficiently
many near-chain vertices are non-extreme. We test that precise implication:

```text
near-chain source-hull interiority
  -> absence of diameter reactions at most path vertices
  -> [NOT VALID] degree four and a C97 strip
  -> terminal-prefix contradiction.
```

The first arrow can be proved quantitatively: only O(sqrt(D)) path vertices need
be discarded, even if the dominant-stress defect tends to zero very slowly.
The second arrow is false from the stated local data. Exact positive-equilibrium
degree-three and degree-five rhombic patches below show why.

We also improve the C102 total-angular-variation constant and quantify the
near-equilateral equality well at every interior degree-five path defect.

## 2. Source-hull localization theorem

Let K be a compact convex planar body of diameter D. Suppose, for one center o,

\[
B(o,D/2-2h)\subseteq K\subseteq B(o,D/2+h),\qquad 0<h<D/4.
\]

Let `z=x_0,...,x_k=a` be a unit-edge polygonal path in K whose endpoints satisfy
`a-z=D u`, `|u|=1`. Suppose every oriented edge e satisfies

\[
e\cdot u\ge c=\sqrt{1-\rho^2},\qquad |e\cdot Ju|\le\rho,
\qquad 0\le\rho<1.
\]

Put R=D/2+h and

\[
\gamma=\frac{D}{4R}-\frac\rho c.
\]

**Theorem 1.** If gamma>0, every path vertex with

\[
\boxed{\min(j,k-j)>\frac{3h}{c\gamma}}
\]

belongs to the interior of K. If the path lies in a diameter-D point
configuration with convex hull K, such a vertex is not an endpoint of any
diameter pair.

### Complete proof

Write `x_j=z+p u+y Ju`. Forward projection gives

\[
p\ge cj,\qquad D-p\ge c(k-j).
\]

The transverse projections of the whole path sum to zero. Therefore

\[
|y|\le\rho\min(j,k-j)\le\frac\rho c\min(p,D-p).
\]

Set l=min(p,D-p), and w=z+p u. By the exact squared-norm identity for a convex
combination of z and a,

\[
|w-o|^2\le R^2-p(D-p)=R^2-l(D-l).
\]

For 0<=q<=R^2, `sqrt(R^2-q)<=R-q/(2R)`. Since l<=D/2,

\[
|x_j-o|\le |w-o|+|y|
\le R-\frac{l(D-l)}{2R}+\frac\rho c l
\le R-\gamma l.
\]

The hypothesis on j gives gamma*l>3h. Thus
`|x_j-o|<R-3h=D/2-2h`, proving strict interiority.

If an interior point x were at distance D from another source point q, a small
extension of the ray qx beyond x would still lie in K and would have distance
greater than D from q. This contradicts diam(K)=D. Square.

### Global-minimizer specialization

Section 155 of `docs/targets/target-a/08-prescribed-phase-alignment.md` supplies
the displayed concentric inclusions for the **actual source hull**, with

\[
h=3^{1/4}\sqrt D.
\]

Only its source-hull conclusion is used: there is no identification with an
independent scaffold, smaller optimum, or force hull.

If D>=64*sqrt(3) and rho<=1/4, then h/D<=1/8,

\[
c\gamma=\frac{cD}{4R}-\rho
\ge\frac{\sqrt{15}}{10}-\frac14>\frac18.
\]

Hence all vertices with `min(j,k-j)>24h` are strictly interior. There are at most
`2 floor(24h)+2` remaining vertices. In the C100 regime rho=(1-b)/b tends to zero,
these hypotheses eventually hold, and a consecutive block of `k-O(sqrt(D))`
vertices has no diameter reaction. This conclusion does **not** say that these
vertices are interior to the contact-graph disk: that disk can have concave
boundary deep inside the convex source hull.

## 3. Sharper bounded-variation constant

Assume precisely the force-stack hypotheses of C102: ordered nested separator
trains have unit directions a_j and forces

\[
F_j=A_j a_j=bD u+G_j,\quad A_j>0,\quad
|G_j|\le D\eta,\quad \eta=1-b,
\]

and every residual diameter contributes a fixed vector on one interval of
indices. Set G_0=G_(k+1)=0 and a_0=a_(k+1)=u. Suppose b>1/2.

**Theorem 2.** Both the chordal variation and the total smaller-angle variation
of the extended direction sequence satisfy

\[
\boxed{\operatorname{TV}_{\rm chord}(a)
\le\operatorname{TV}_{\rm angle}(a)
\le\frac{2\eta}{2b-1}.}
\]

### Complete proof

Each residual interval creates at most two force jumps, with total length at
most twice its diameter weight times D. Thus the polygonal interpolation of the
extended force sequence has length at most `2D eta`.

Every interpolated force lies in the convex ball `B(bD u,D eta)`. Its norm is
at least `D(b-eta)=D(2b-1)>0`. Along any differentiable segment F(t), the
angular derivative of F(t)/|F(t)| has magnitude

\[
\frac{|\det(F(t),F'(t))|}{|F(t)|^2}
\le\frac{|F'(t)|}{D(2b-1)}.
\]

The smaller angle between segment endpoint directions is no larger than this
integrated angular length. Summing proves the angular bound. A chord of the
unit circle is no longer than its smaller arc, proving the chordal bound.
Square.

This replaces C102's bounds `4 eta/(2b-1)` (chordal) and
`2 pi eta/(2b-1)` (angular), under exactly the same force-stack hypotheses.
It neither requires nor proves universal PSD. Establishing those force-stack
hypotheses for every source remains a separate matter.

## 4. Degree-five defects concentrate in the equality well

Consider an internal vertex of a path in the **interior of a strict unit-rhombic
contact disk**. Assume all unit contacts are the disk edges and there is no unit
equilateral triangle. Every rhombus angle is strictly between pi/3 and 2pi/3.
Let tau<pi/3 be the smaller turn between the oriented incoming and outgoing
path edges.

**Theorem 3.** Such a vertex has degree four or five. At degree five, exactly
three incident faces lie in the larger path sector. If their angles at the
vertex are theta_1,theta_2,theta_3, then

\[
\sum_{r=1}^3(\theta_r-\pi/3)=\tau,
\qquad
0<\sum_{r=1}^3(\sin\theta_r-\sqrt3/2)\le\tau/2.
\]

Consequently, along a path satisfying Theorem 2, the sum of these three-face
area surpluses over all its interior degree-five vertices is at most

\[
\boxed{\eta/(2b-1).}
\]

Faces are counted with multiplicity in this statement.

### Complete proof

At an interior disk vertex the incident angles sum to 2pi. Three angles each
less than 2pi/3 cannot suffice, and six angles each greater than pi/3 are
impossible. Thus the degree is four or five.

The path rays split the full angle into pi-tau and pi+tau. At degree five,
neither sector can contain only one angle: that angle would be at least
pi-tau>2pi/3. The split is therefore two angles and three angles. The three
angles have sum greater than pi, so they occupy the larger sector. Subtracting
three copies of pi/3 gives the first identity.

Each theta_r is in (pi/3,2pi/3), so its sine exceeds sqrt(3)/2. Concavity of sine
on [0,pi] gives
`sin(theta)<=sqrt(3)/2+(theta-pi/3)/2`. Sum and use the identity. Finally sum the
selected vertex turns, which are bounded by the path's total angular variation,
and apply Theorem 2. Square.

This is an **upper** bound on defect area, not the missing lower bound. It
explains how many non-degree-four defects could be arbitrarily cheap. It must
not be reversed or converted into a bound on their number without another
hypothesis.

## 5. Exact regression: arbitrarily small turn at a degree-five interior vertex

For any 0<epsilon<=1/100, put theta=pi/3+epsilon and let v_0,...,v_4 be the
unit vectors of respective angles

\[
0,\quad\theta,\quad2\theta,\quad3\theta,\quad4\theta.
\]

Take the eleven points

\[
0,\quad v_i,\quad s_i=v_i+v_{i+1}\quad (i\bmod5).
\]

Their contact graph consists exactly of the five spokes `0-v_i` and the ten
edges `v_i-s_i-v_(i+1)`. It is triangle-free and bounds a disk of five strict
unit rhombi. The center is an interior degree-five vertex.

The path `v_3,0,v_0` has turn 3epsilon and graph length two. It is a shortest
contact path between its endpoints, and their Euclidean distance is
`2 cos(3epsilon/2)`, tending to two.

### Every distance and strict inequality

The cyclic gaps between rays are theta,theta,theta,theta,phi, where
`phi=2pi/3-4epsilon`. All lie strictly between pi/3 and 2pi/3. Thus the five
parallelograms occupy disjoint angular wedges at 0 and are nondegenerate strict
rhombi.

At epsilon=0, the fifteen stated edge pairs have distance one. The five
additional pairs `(v_0,v_1),(v_1,v_2),(v_2,v_3),(v_3,v_4),(0,s_4)` also have distance one.
Every other pair has squared distance at least two. The adjacent-pair list and
all 55 pair comparisons are verified exactly over Q(sqrt(3)) by the script.

For positive epsilon the fifteen edges stay unit. The four extra ray pairs have
distance `2 sin(theta/2)>1`, and `|s_4|=2cos(phi/2)>1`.
Each ray moves by at most 4epsilon from its zero-parameter position, and each
s_i by at most 8epsilon. Thus every other pair has distance at least
`sqrt(2)-16epsilon>1`; the last inequality follows from `(29/25)^2<2`.
No pair is omitted. The stated contact graph is bipartite,
with shores `{0,s_i}` and `{v_i}`, so it contains no unit triangle.

### Strictly positive equilibrium at the center

Let gamma_i be the cyclic angle from v_i to v_(i+1), put
`t_i=tan(gamma_i/2)`, and set

\[
\alpha_i=t_{i-1}+t_i>0.
\]

The elementary identity
`t_i(v_i+v_(i+1))=-J(v_(i+1)-v_i)` telescopes to
`sum alpha_i v_i=0` exactly. All coefficients stay bounded away from zero as
epsilon tends to zero. Thus even a positive local stress floor does not force
degree four. The limiting configuration acquires unit triangles; strict
triangle-freeness supplies no uniform angle gap.

In fact the area excess of **all five** incident faces tends to zero, not just
the three selected in Theorem 3:

\[
0<4\sin\theta+\sin\phi-5\sqrt3/2\le4\epsilon.
\]

For the upper bound apply the tangent-line bounds for sine at pi/3 and 2pi/3;
the four theta terms contribute at most 2epsilon and the phi term at most
2epsilon. Thus a uniform positive area charge per degree-five vertex fails
even with positive local equilibrium weights bounded away from zero.

**Missing global hypotheses:** no full-configuration KKT stress is claimed;
the path endpoints are not the patch's diameter pair; global minimum diameter
is not claimed. This refutes the local degree-four implication, not C-II.

## 6. Exact regression: non-extreme degree-three vertex on a concave disk boundary

For 0<delta<=1/100, let v_0,v_1,v_2 have unit lengths and angles

\[
0,\quad\pi-\delta,\quad3\pi/2-\delta/2.
\]

Take the six points `0,v_0,v_1,v_2,v_1+v_2,v_2+v_0`. They form two strict
unit rhombi sharing the edge `0-v_2`. The vertex 0 is on their concave boundary:
its interior disk angle is pi+delta. The path `v_1,0,v_0` turns by delta.

There are exactly seven permanent unit pairs. At delta=0 all other eight pairs
have squared distance at least two, as checked exactly by the script. Ray
displacement is at most delta, and sum displacement at most 2delta. Thus these
other distances remain at least `sqrt(2)-4delta>1`, using `(26/25)^2<2`.
There are no new contacts or unit triangles.

Set `alpha_0=alpha_1=1` and `alpha_2=2sin(delta/2)>0`. The ray sum with these
weights is exactly zero. The three rays are not collinear, so 0 is strictly
inside their convex hull despite being a contact-disk boundary vertex.

Again, these are local stress data, not a global KKT certificate. The example
isolates the difference between convex-source-hull interiority and contact-disk
interiority, which must not be suppressed in using Theorem 1.

## 7. Branch ledger update and exact remaining theorem

The historical [campaign ledger was excluded from the release corpus](../research/migration/2026-10-16/scientific-reconciliation.md) because it is a branch/status record; the current route is tracked in the [Target C frontier](../targets/target-c/CURRENT.md), and its exact force-bulk regression remains in the [dedicated audit](target_c_force_bulk_and_correction_audit_2026-09-08.md).
This continuation changes only the following conditional branches:

| Branch / hypotheses | Canonical input and target quantity | Attempted closure and status | Regression / next exact attack |
| --- | --- | --- | --- |
| C100 near-chain in a sufficiently large global source | Source shell inclusions; uniform edge cone | **Reduced to sharper theorem:** all but O(sqrt(D)) path vertices have no diameter reaction | Must still control contact-disk boundary and degree-five vertices |
| C102 nested force stack, b>1/2 | Interval-supported residual loads | **Reduced to sharper theorem:** total angular variation <=2(1-b)/(2b-1) | Small positive variation is not zero |
| Recover degree four from source interiority, small turn, and local positive stress | Proposed C97 stability shortcut | **Disproved by exact regression** | Eleven-point degree-five patch; six-point degree-three concave patch |
| Count degree-five vertices by fixed positive face-area cost | Strict rhombic disk and small-turn path | **Disproved by exact regression** | Entire five-face star has area excess <=4epsilon, with local stress weights bounded below |
| Uniform C97 stability with all actual global hypotheses retained | Conditional C65 pure-disk source, full contact/diameter visibility | **Reduced to the theorem below**, not closed | Local regressions omit full diameter support and global optimality |

A precise sufficient remaining statement for this branch is:

> **Uniform dominant-diameter exclusion.** There exist absolute b_*<1 and D_*
> such that every triangle-free global minimizer of diameter D>=D_* which
> satisfies the actual C65 fully visible, pure simply connected strict-rhombic
> source hypotheses has beta_h<=b_* for every diameter edge h and every
> relative-interior normalized KKT stress to which C98 applies.

This would contradict the C98 near-zero phase's `beta_h=1-o(1)`. It would not
by itself settle the other C-II phases, C-I, or establish the missing C65
normalization. Theorem 1 removes one source-boundary obstruction, while the
regressions show exactly why a local degree-four substitute cannot prove this
uniform exclusion. No claim of logical independence from the whole repository
is made.

## 8. Adversarial checks and repository handoff

- The hull theorem uses the actual source hull, not the possibly thin force hull.
- Its conclusion is strict interiority, with explicit margins and endpoint counts.
- The two local regressions check every pair, not only prescribed edges.
- Local positive equilibrium is never identified with a global normalized stress.
- The degree-five area estimate is multiplicity-weighted and has the correct
  inequality direction. It cannot count vertices in a vanishing equality well.
- No O(D) or O(sqrt(D)) term is discarded in an exact global contradiction.
- The C53 interval-sign failure and C63 correction obstruction remain binding.
- Regular shells, strained monomers, and near-star responses are not claimed
  excluded by this report. No universal response-rank/PSD assertion is used.

**Reproduction:** `python3 research/nearchain_vertex_regressions.py` verifies
55 pair comparisons in the first limiting patch and 15 in the second, the
permanent contact graphs, and the exact rational safety margins. The analytic
proof above handles every positive parameter in the stated intervals.

**Promotion recommendation:** hold as an unpromoted report pending independent
audit. If promoted, update C55's third proposed mechanism to distinguish source
hull interiority from degree-four-strip recovery, index the two local regressions,
and replace C102's variation constants. Do not promote C65 or C-I by association.
No canonical route map or existing user edit was changed by this continuation.
