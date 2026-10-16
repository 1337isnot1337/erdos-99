<!-- theorem-state: {"artifact_id":"ART-B9401F4A74F3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — diameter-first rigidity transfer and quadratic joint blockers

```text
canonical finite release -> diameter-first triangle-free source with ZR/ZF
-> safe joint contact gains and quadratic lower deficits
-> a finite lower repair respecting every old and inactive upper constraint
-> fewer diameter pairs or a strict same-cardinality competitor -> Level I.
```

**Date:** 2026-10-02.
**Starting shared checkout:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
**Fetched research base:** `3bad7c12bf5133665be466d0396362108fadef2c`.
**State version:** `2026-09-14.audit.51`.
**Mission:** audit the reverse-order source selection, then repair actual finite
joint swap blockers. No open coordination issue or PR assigned this mission.
**Branch:** `swarm/source-stress/diameter-first-20261002`.
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.
**Classification:** proved candidates awaiting independent audit and promotion;
artifact lifecycle **unreviewed**. Finite examples below are **regressions**.
**LEVEL I / C-II:** **STILL OPEN / OPEN**. No canonical state is changed.

## 1. Dependencies and the earlier reverse-order source

Canonical inputs actually used are:

1. [C53/C63 restoration](target_c_c53_orientation_and_ci_restoration_2026-09-09.md),
   Sections 4–7: PSD for every normalized source stress and convergent finite
   weak-row release/integration, before either count is minimized.
2. [Target C 01](../targets/target-c/01-force-hull-and-shear.md), Sections 2, 3,
   and 6: relative-interior support, critical-cone duality, and connected
   positive contact support spanning a diameter; the already imported
   Eppstein bound on the same connected triangle-free penny graph.
3. [C-ZTA](target_c_zero_transfer_additive_promotion_2026-09-11.md): the
   interval-split/SEPq proof of zero-transfer exclusion.
4. [C-ZRF](../targets/target-c/57-zr-zf-rigidity-audit.md), Sections 1 and 3:
   the source-independent spectral and Schur steps of ZR. The finite
   normalization needed for Section 4 is rechecked below.

No result in PR #622 or #623 is a premise. All source points, including contact
isolates, are retained in the arguments and pair tests.

The reverse-order selection and a narrower safe-contact theorem already occur
in `target_c_diameter_first_normal_form_2026-10-02.md` on the unmerged research
branch `origin/swarm/gap-reaction-cut-20261001`, inspected at `02d4cc04`.
That report is unreviewed. Section 2 below independently rederives its selection
and supplies the previously missing pinned-rank, ZR, and ZF hypothesis audit.
Section 3 removes its separate old-pair length/projection and displacement-cloud
assumptions. Section 4 is a new sharp finite deficit bound.

The earlier universal-rigidity statement in
`target_c_zr_full_kernel_rigidity_2026-09-09.md` is acknowledged; universal
rigidity of the ordinary canonical source is not claimed as new here.

## 2. Reverse-order selection retains the rigid-core inputs

### Theorem DF

Suppose a triangle-free global minimizer exists at cardinality n. Among such
minimizers choose A first minimizing the number h of actual diameter pairs,
then minimizing the number e of unit contacts. For D=D(n)>=9:

* `C=C_*` and `H=H_*`;
* the nonisolated contact core V is connected and contains every actual
  diameter endpoint;
* for a relative-interior normalized source stress,
  `Omega_V >= 0` and `ker Omega_V = span{1,P_x|V,P_y|V}`;
* `rank R_(C union H)[V]=2v-3`, `e+h>=2v-2`, and
  `h>=delta>=ceil(D)`;
* if q is the number of diameter endpoints and c_I the number of components
  after deleting them, then
  `e-e_BB>=2(v-q)+c_I` and `2q>=delta+c_I+e_BB+2`.

The source has the global comparison property: a triangle-free, unit-separated
same-cardinality A' with diameter at most D and fewer diameter pairs is
impossible, even when A' gains unit contacts. This does not identify the
auxiliary source with the canonical contact-first representative.

### Proof: selection and local minimality

Both successive minima exist because the attainable counts are nonempty sets
of nonnegative integers. No closedness claim about the triangle-free locus is
needed. Apply canonical C63's finite release to all weak active rows. Initially
inactive pairs stay strict; the new contact graph is a subgraph of C, so the
source stays triangle-free. Global minimality forces its diameter to be D.
A weak diameter would reduce the first minimum. In its absence, a weak contact
would reduce the second. Thus every actual active row is strong.

More generally, any sufficiently nearby feasible source creates no new active
pair. Its active sets are subsets of the original sets. Diameter-first and
then contact-second minimality force both sets to remain identical. This is
precisely the local active-length preservation used by canonical ZF; it is
independent of the order of the two minima.

### Proof: pinned rank and the boundary count before ZR

Let B be the actual diameter endpoint set. Full support and source equilibrium
put every vertex of B in V. Connected positive-support theory makes C[V]
connected and of Euclidean diameter D. Its graph diameter delta is at least
ceil(D).

Pin B and set all contact-isolate velocities to zero. If an expansive contact
velocity u is nonzero on V, the straight motion `p+t u` preserves every actual
diameter exactly and satisfies every old contact inequality: its squared
length is `1+2t r.u_ij+t^2|u_ij|^2`. Initially inactive pairs retain strict
slack for sufficiently small positive t. Connectivity and the pinned vertices
ensure some relative contact velocity is nonzero; that contact opens, at
first or second order. No new active pair appears. The diameter count stays
fixed and the contact count falls, contradicting the second minimum.

Consequently the pinned expansive cone is zero. The pinned contact rigidity
matrix has rank `2(v-q)`, and `e>=2(v-q)`. Eppstein gives
`e<=2v-delta-2`, hence `2q>=delta+2`. In particular D>=9 implies q>=6.
This avoids using ZF's conclusion to justify its own diameter-direction count.

For the sharper inequality delete the zero rows corresponding to e_BB.
At each unpinned component, positive contact equilibrium gives a nonzero
left-kernel relation supported on its internal and boundary contact rows.
Different components have disjoint row supports, so these c_I relations are
independent. The remaining row rank is still `2(v-q)`. Therefore
`e-e_BB>=2(v-q)+c_I`, and Eppstein gives the stated boundary count.

An unloaded contact vertex has degree at most five by unit separation and
triangle-freeness. It has degree at least three: positive equilibrium excludes
degree one; at degree two it is the midpoint of two antipodal unit neighbors,
and a small perpendicular motion opens both contacts while leaving B fixed.
A loaded vertex has at most three contacts, because its unit directions lie
in an inward angle strictly smaller than pi and are separated by more than
pi/3. These are the degree hypotheses needed for SEPq.

### Proof: transfer of ZR and ZF

Reapply the proof of C-ZTA, rather than importing its contact-first statement
without checking hypotheses. Its PSD edge defect, legal diameter orientation,
interval-split sign inequalities, and circular-planar contact response use only
the actual selected source stress. If the least off-diagonal transfer is zero,
the strictly ordered slope energy forces all off-diagonal transfers to vanish.
The audited split argument makes the resistance metric additive, and SEPq
then produces a contact separator of degree at least q (unloaded) or q-1
(loaded). The degree caps above and q>=6 exclude it. Thus the least transfer
is negative. No global contact-first comparison occurs in this argument.

Canonical C-ZRF Section 1's weighted Robinson/Fiedler argument now gives edge
defect nullity two; its Section 3 Schur/SVD argument gives exactly the three
affine scalar kernel modes on V. Neither step uses the order of source
selection.

Extend an arbitrary mixed bar flex on V by zero at every isolate. C63
integrates it as `x(t)=t u+O(t^2)` at fixed diameter. The local preservation
proved above keeps every old active length exact. Pair these squared-length
identities with the relative-interior stress. Equilibrium removes the linear
terms and PSD gives

`x_1(t)^T Omega_V x_1(t)+x_2(t)^T Omega_V x_2(t)=0`.

Divide by t^2. Both coordinate fields of u belong to the affine kernel, so
`u_i=b+M p_i`. There are at least three actual diameter bars with distinct
projective directions, because q>=6 and distinct diameter segments cannot be
parallel. Their zero radial variations force the homogeneous quadratic
`r^T(M+M^T)r` to have three projective zeros; it vanishes identically.
Thus u is Euclidean, the mixed rank is `2v-3`, and the nonzero full-support
row dependence gives `e+h>=2v-2`. Eppstein then gives h>=delta.

Finally, any A' as in the global comparison property either has smaller
diameter, contradicting global optimality, or has diameter D and contradicts
the first count minimum. New contacts do not affect this comparison. ∎

### Exact scope of this transfer

This verifies the full-support, pinned-rank, positive degree, ZR, ZF, and
source-count inputs. Purely geometric/combinatorial extraction theorems may
be applied when their other hypotheses are separately established on this
source. It does not transfer a proof that invokes an arbitrary distant
contact-count-reducing competitor which creates new diameter pairs. It does
not assert the fixed-star chart on every source, a quantitative conductance
floor, or a full-source affine kernel. Isolates contribute zero stress rows
and keep their free coordinates.

## 3. Safe joint equality contacts without old-vector assumptions

### Theorem SC

Partition a finite triangle-free unit-separated source into rigidly translated
owners and fixed points. Every moving owner i has
`Delta_i=a_i v_i`, where `a_i>0`, `|v_i|=1`. Assume

`a_i<=a_*`, `|v_i-v|<=kappa`, and `mu=a_*/2+kappa<1/2`

for one common unit vector v. Assume every old unit contact remains unit for
every binary selection of owners. Take a unit-separated final binary pattern.
Suppose every newly unit pair has two distinct selected moving owners i,j,
and both corresponding singleton pair states have distance at least one.
Then the final source is triangle-free. Its graph of new unit contacts is
a disjoint union of paths.

Neither `|r|<=5/4`, an old projection bound, nor a displacement-cloud bound
is assumed. Singleton feasibility is pairwise; the entire singleton source
need not be feasible.

### Proof

First `kappa<1/2` gives
`v_i.v_j>=1-2kappa^2>0`. An old contact between two distinct moving owners
would have the same squared length in all four binary states. Their mixed
difference is `-2 Delta_i.Delta_j`, a contradiction. Thus such old contacts
do not exist.

For a new final contact, orient its unit vector as
`s=r+Delta_i-Delta_j`. Its singleton states are `s+Delta_j` and `s-Delta_i`.
Their lower feasibility gives

`s.v_j>=-a_j/2`, `s.v_i<=a_i/2`, hence `|s.v|<=mu`.             (SC.1)

Unit vectors with projection on v between -mu and mu lie in two opposite
arcs, each of angular width `2 arcsin(mu)<pi/3`. Two on the same arc are
less than one apart; two on opposite arcs are more than one apart. Two new
edges therefore cannot be sides of a unit triangle.

If a triangle has exactly one new edge xy, its common old unit neighbor z
cannot belong to a moving owner: one old edge would join two distinct moving
owners. Thus z is fixed. Binary preservation of xz gives
`(x-z).v_i=-a_i/2`; after the move its unit vector has projection a_i/2
on v_i, and absolute projection at most mu on v. The same holds for yz.
The preceding two-arc argument rules out a unit distance between x and y.
A triangle with no new edge was already absent.

At a vertex, two new neighbors on the same longitudinal side would have
distance less than one, violating final unit separation. Hence there is at
most one new neighbor on each side. Orient every new edge toward increasing
projection on `Jv`. A directed cycle cannot increase that coordinate, and an
undirected cycle would have a vertex minimal in it with two outgoing edges.
Therefore the new graph is a disjoint union of paths. ∎

The owner graph can have cycles after source vertices are identified. The
earlier owner-cycle regression remains binding.

## 4. A sharp quadratic depth bound for strict joint overlaps

### Theorem QD

Let two owners move by `a v` and `b v`, with a,b>0. Orient their original
pair vector as r. Assume `|r|>1`, and that both singleton pair vectors
`r+a v` and `r-b v` have norm at least one. Set
`s=r+(a-b)v`. Then

`|s|^2 > 1-min(a,b)|a-b|`.                                (QD.1)

In particular a=b gives no joint overlap. If a,b<=epsilon, every strict
joint squared deficit eta is less than epsilon^2/4. The coefficient 1/4
is sharp as a supremum under these hypotheses.

### Proof

For a>=b, s is the convex combination

`s=(b/a) r+((a-b)/a)(r+a v)`.

The exact squared-norm interpolation identity subtracts `b(a-b)` from
the weighted endpoint squared norms. They are at least one and the first
is strictly greater than one with positive weight, giving (QD.1).
For b>=a use the segment from r to `r-b v` and obtain `a(b-a)`.
Writing the larger amplitude as x and the smaller as y gives
`y(x-y)<=x^2/4<=epsilon^2/4`.

For sharpness take a=2b, `s=(c,0)`, `r=(c,-b)`, and
`sqrt(1-b^2)<c<1`. The old and a-singleton lengths are strictly above
one; the b-singleton has vector `(c,-2b)` and is also feasible. Let c
decrease to `sqrt(1-b^2)`. The joint deficit tends to b^2=a^2/4. ∎

### Almost parallel axes

If the displacements are `a v_i,b v_j`, put
`theta=|v_i-v_j|` and `e_0=min(a,b)theta`. The same segment argument
produces an auxiliary s_0 with

`|s_0|>sqrt(1-min(a,b)|a-b|)`, `|s-s_0|<=e_0`.

Whenever the displayed square root exceeds e_0,

`|s|>sqrt(1-min(a,b)|a-b|)-e_0`.                         (QD.2)

Thus `a,b<=epsilon`, `theta<=omega`, and `epsilon^2/4<1` give the
squared-deficit bound

`eta<epsilon^2/4+2 epsilon omega`,                       (QD.3)

provided `epsilon omega<sqrt(1-epsilon^2/4)`.
In an actual narrow swap-axis family with both epsilon and omega of order
1/D, joint overlaps have squared depth of order 1/D^2. This is conditional
on that axis-width hypothesis, not a claim about every TB1 packet.

For a strict overlap `|s|^2=1-eta`, singleton feasibility additionally gives

`s.v_i<=a/2-eta/(2a)`, `s.v_j>=-b/2+eta/(2b)`.

In particular `|s.v|<=a_*/2+kappa` when `|s|<=1`. The same transverse
belt used for safe equalities controls strict overlaps.

## 5. Exact certificates and failed repair

The standard-library Fraction verifier
[verify_diameter_first_joint_depth_2026_10_02.py](../../research/verify_diameter_first_joint_depth_2026_10_02.py)
checks actual full-source distances, contacts, and triangles in the following
finite packets. None is a global minimizer or an actual stopped-train chart.

1. A four-point two-dimer packet with a=1/100, b=9/10. All old contacts
   survive all binary states; the final new contact is safe. Its original
   pair violates both older bounds `|r|<=5/4` and `|r.v|<=1/8`.
2. A rational nonparallel two-dimer packet with
   `Delta_1=(-1/5000,1/1000)`, `Delta_2=(1/5000,2/1000)` and final new
   pair vector `(1,0)`. This checks the theorem beyond exactly parallel axes.
3. Sharpness packets obtained from the rational unit-circle point
   `x=(1-t^2)/(1+t^2)`, `b=2t/(1+t^2)`, with a=2b and
   `c=x+(1-x)/k`. The strict deficit approaches b^2 as k increases.
4. An eight-point packet with owners A,B,C,A in one longitudinal row,
   each base point carrying its own vertical unit dimer. Put
   `c=1-1/10^8`, amplitudes `(1,3,5)/1000`, and base points
   `(j c,-a_owner(j))` for j=0,1,2,3. All singleton source states and
   the original are unit-separated; all old contacts survive all eight
   binary states. Selecting all owners creates only the six strict
   adjacent-row overlaps. Each has quadratic depth `1-c^2`.

Packet 4 disproves a proposed second move: assigning one small common axial
translation xi_i to each owner cannot repair these overlaps. If the adjacent
longitudinal orders are retained, the three base-row constraints require

`xi_B-xi_A>=1-c`, `xi_C-xi_B>=1-c`, `xi_A-xi_C>=1-c`.

Their sum is impossible. This strengthens the earlier disjoint-matching
owner-cycle warning to a connected conflict path with nonempty, exactly
preserved contacts. It does not prove such a return occurs under actual O-O
ownership. That missing geometric hypothesis is kept explicit.

## 6. Repaired owner order: graphical actual cuts

The preceding packet lacks actual stopped-train ownership. The following
graphical-cut lemma is valid, but the attempted application to the strict
blocker cone below has a coordinate reversal. It remains useful only when a
separate source argument supplies the stated transverse-crossing inequality.

### Lemma GO

Let ordered, disjoint cuts in one strip be graphs `x=g_k(y)` on the same
interval I, with each g_k L-Lipschitz and `g_k(y)<g_(k+1)(y)`. Give each
point off the cuts the slab label equal to the number of cuts to its left.
If p,q have heights in I and

`x_q-x_p > L |y_q-y_p|`,

then the slab label of q is at least that of p. If their labels differ, the
inequality is strict. Thus a family of such pairs, oriented toward increasing
x, induces an acyclic graph on distinct slab owners.

**Proof.** If q had the smaller label, some cut would have
`x_p>g_k(y_p)` and `x_q<g_k(y_q)`. This would imply
`x_q-x_p<g_k(y_q)-g_k(y_p)<=L|y_q-y_p|`, a contradiction. Distinct labels
therefore strictly increase along every owner arc, excluding a cycle. ∎

The common-strip hypothesis is meaningful for actual rhombus trains. A
stopped-train centerline crosses each strict rhombus between midpoints of
opposite edges in its fixed unit direction u_k. The centerline step is along
the other side direction. Its angle with u_k is strictly between pi/3 and
2pi/3. Orienting the train consistently makes all steps have positive
projection on Ju_k: adjacent rhombi lie on opposite sides of their shared
u_k edge, so the sign cannot reverse. Consequently it is a graph over Ju_k
with slope magnitude less than `1/sqrt(3)`. If all u_k are within angular
rho<pi/3 of one unit u, all these cuts are graphs over Ju with Lipschitz
constant at most `tan(pi/6+rho)`.

This statement concerns the actual centerline through its rhombi. It does
not extend its graph beyond its two actual endpoints or cross a stopped
nonrhombic face. Application of GO still requires that all relevant source
points lie in a common height interval covered by the separating cuts, and
that actual owner labels agree with the resulting slab labels.

For a train centerline written as a graph over `Ju`, GO's coordinates are
`x=p.u` and `y=p.Ju`. Its directed crossing hypothesis is therefore

`r.u > L |r.Ju|`                                        (GO.1)

after orienting the pair toward increasing transverse coordinate. The strict
pure joint overlaps from Section 4 satisfy the opposite cone: for their
original unit-separated pair,
`|r.v|<=nu=5a_*/2+kappa` and, when `nu<1`,
`|r.Jv|>=sqrt(1-nu^2)`. Thus the previously stated inequality
`sqrt(1-nu^2)>L nu` does **not** imply GO; it says the pair is predominantly
longitudinal along the train chart rather than transverse across its cuts.

Accordingly this audit rejects the claimed application of GO to the proved
joint-blocker cone. GO itself remains correct. To use it here, a separate
source theorem would have to produce blocker pairs with the actual transverse
crossing inequality `|r.v|>L|r.Jv|`, plus common-height coverage and correct
slab ownership. No such theorem is proved in this report.

## 7. Next repair attack: a protected diameter blocks axial corrections

The owner cycle is not removed by GO under the blocker cone proved above.
Independently, the following finite theorem identifies a second exact
obstruction without replacing diameter rows by an unlabelled gap graph.

### Lemma PA

At a post-swap placement let owners be indexed 0,...,m. Suppose there is an
old unit contact crossing each adjacent interface, oriented from owner i-1
to owner i with current vector c_i, and `c_i.u>=c_0>0` for one unit axis u.
Suppose an unchanged old actual diameter has endpoints in owners 0 and m,
has current length D, and its vector r from 0 to m satisfies `r.u>=0`.
Translate owner i additionally by `xi_i u`, with
`|xi_i-xi_(i-1)|<2c_0`. If every listed contact remains at least one and
the listed diameter remains at most D, then all xi_i are equal.

**Proof.** With t=xi_i-xi_(i-1), the contact squared change is
`2(c_i.u)t+t^2`. Its nonnegativity says t>=0 or t<=-2(c_i.u).
The size assumption excludes the second alternative. Thus the xi_i are
nondecreasing. Let T=xi_m-xi_0>=0. The diameter squared change is
`2(r.u)T+T^2`, positive unless T=0. Upper feasibility forces T=0,
and monotonicity then forces every xi_i to be equal. ∎

An additional common translation does not repair any lower overlap. Thus a
small purely axial owner correction is impossible under these actual vector
and endpoint hypotheses, even if the joint conflict owner graph is acyclic.
The verifier checks the exact three-owner unit chain, with the outer pair
as the protected diameter, for all 125 potentials in its stated rational
grid. This is a nonglobal finite packet corroborating PA's universal proof.

For the fixed-star complete shore, the common witness rows are unchanged by
an internal block transposition, but PA must not be invoked until their
endpoint owner labels and oriented axial projection are actually checked.
Full interval support alone does not establish `r.u>=0`. This audit does
not discard that label condition, turn a source train into a virtual cut,
or assert PA eliminates the entire nonconstant-phase branch.

### Why a uniform quadratic residual bound does not supply a closing repair

Even if a separate source argument supplies an acyclic owner order, owner
corrections along the axis can be forbidden by PA. More general corrections
also need a source-dependent size estimate. Here is a
finite necessary bound which tests that issue directly.

Suppose the same adjacent unit contacts have vectors
`c_k=(cos(theta_k),sin(theta_k))`, `|theta_k|<=rho<pi/2`.
Write c=cos(rho). Consider pairwise disjoint owner intervals [a_j,b_j],
j=1,...,J, each carrying a strict joint overlap with vector s_j oriented
from a_j to b_j, `|s_j|^2=1-eta_j`, `s_j.u>=c_L>0`, and
`|s_j.Ju|<=mu`. Let N be the number of adjacent steps outside those
intervals. Translate owners additionally by `z_i=(X_i,Y_i)`, with
`z_0=z_m=0` and `|z_i|<=gamma`. If the listed old contacts and overlap
pairs all become lower-feasible, then

`sum eta_j <= 4J(mu gamma+gamma^2)/c_L`
`             +4N tan(rho) gamma+4N gamma^2/c`.          (RB.1)

**Proof.** For overlap j, lower feasibility gives

`X_b-X_a >= eta_j/2 - 2mu gamma/c_L - 2gamma^2/c_L`,

because its longitudinal projection is at most one and positive, its
transverse projection at most mu, `|Y_b-Y_a|<=2gamma`, and
`|z_b-z_a|^2<=4gamma^2`. An adjacent old contact gives

`X_k-X_(k-1) >= -tan(theta_k)(Y_k-Y_(k-1))`
`                 - |z_k-z_(k-1)|^2/(2 cos(theta_k))`.

Sum the overlap interval increments and all complementary adjacent
increments. Disjointness makes their sum `X_m-X_0=0`. Bound each
complementary transverse term by `2tan(rho)gamma`, and each quadratic
term by `2gamma^2/c`. Rearranging gives (RB.1). ∎

For J,N=O(D), mu,rho=O(1/D), and c,c_L bounded away from zero,
the right side is `O(gamma+D gamma^2)`. If a linear disjoint family has
total squared deficit at least a positive multiple of 1/D, any such repair
requires `gamma=Omega(1/D)`. Uniform `gamma=O(1/D^2)` corrections cannot
repair it. No lower bound on the total deficit or disjoint interval family
is proved for the actual surviving source. Inactive gaps can be arbitrarily
small. Conversely this inequality does not prohibit repairs at the original
swap amplitude, ownership changes, or phase rotations.

This destroys the proposed inference that pointwise quadratic overlap depth
alone makes a uniformly quadratic full-source correction available. The
remaining upper feasibility and actual blocker load are still load-bearing.

## 8. Frontier effect and remaining obligations

The auxiliary source now has a checked ZR/ZF/pinned-rank input package. Safe
joint equality contacts can be allowed using only singleton pair feasibility
and a common displacement cone. Strict joint overlaps are smaller than the
general inverse-diameter proximity bound, but remain genuine obstructions.

The attempted owner-translation repair fails even when the source conflict
graph is a path. The attempted graphical-cut application does **not** remove
that return: actual train cuts are graphs over `Jv`, while the proved blocker
pairs are nearly parallel to `Jv`, so GO's directed crossing inequality is
reversed. GO remains only a conditional lemma pending a separate transverse
crossing theorem. Independently, PA blocks a small axial correction under
its protected-diameter hypotheses, and RB quantifies a separate failure of
uniform quadratic repairs when a linear deficit load is present. An
actual-source closure must resolve the owner return, vector labels, and
endpoint coverage, or use a second move changing ownership or phases. It
must preserve every old diameter inequality and handle strict inactive
upper pairs; an order bound on lower pairs alone is insufficient.

The transferred rigid-core inputs do not close TWO-SIGN, exact-phase positive
circulation, split-star O-O, inactive interfaces, macroscopic inactive
containers/exterior caps, or the non-fixed-star full-core branches. No Level I
quantifier is weakened and no source isolate is omitted.

Promotion recommendation: independently audit DF, SC, QD, PA, and RB
separately, and retain GO only as the abstract conditional graph lemma. Its
application to the Section 4 blocker cone is rejected above.
Their present artifact status remains unreviewed. The local pinned and Schur
arguments, not the finite computations, are load-bearing for DF.
