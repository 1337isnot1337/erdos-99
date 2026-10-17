> Generated reading edition · [exact source](../../../docs/reports/target_c_leaf_fan_hostile_audit_2026-10-02.md) · source SHA-256 `08398710b37e34285ea8b524678b66b33d4ebc04a07559ba2827f6800b5284df`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2841003AB64C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_leaf_fan_hostile_audit_2026-10-02.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ccbabaad3e187d3a3554c541837a634179a37561; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C: hostile leaf-fan audit and round positive-stress regression

**Date:** 2026-10-02
**Starting commit:** `75aac1464f80ca91256e96dc70ca0c865e0b3b0e`
**State version:** `2026-09-14.audit.51`
**Branch:** `swarm/sol/leaf-fan-audit-20261002`
**Mission:** hostile audit of the outer-walk fan fork and inward-spoke KKT fork; test whether positivity, mixed rigidity, and short-arc geometry close the stress-flat branch.
**Classification:** new results are proved candidates awaiting independent audit/promotion; the explicit family is a regression. This report makes no promotion.
**External literature:** none.
**Computation:** exact rational interval certificate in `research/verify_target_c_leaf_fan_reuleaux_regression_2026_10_02.py`.

**LEVEL I STATUS: STILL OPEN. C-I CLOSED; C-II OPEN.**

```text
inward-spoke containment + full-stress fan audit
 -> distinct unloaded source vertices / exact loaded-hull contact currency
 -> a global population, stress-transfer, or source-preserving competitor bridge
 -> C-II contradiction; the final bridge is not proved here
```

## 1. Authority and dependencies

The audit used `AGENTS.md`, `CONTRIBUTING.md`, `docs/STATE.md`, the theorem manifest,
`docs/problem/statement.md`, `docs/KNOWLEDGE_MAP.md`, the Target C route map and current
frontier, `docs/RESEARCH_WORKFLOW.md`, and the current prompt registry/prompt.
Canonical inputs actually used are:

- C-ZRF, `docs/targets/target-c/57-zr-zf-rigidity-audit.md`: full actual contact and
  diameter support in the normalized source, but scalar affine kernel and mixed
  rigidity only on the nonisolated contact core; `h>=ceil(D)`.
- C-LOADED-HULL, `docs/targets/target-c/63-loaded-hull-slack-audit.md`: the
  occurrence-counted identity `x_B=sum_i(ell_i-1)`.
- C-WOODALL, the exact topology entry in the manifest: caterpillar forest or one odd
  cycle with pendant leaves.
- C-FS-GEOM, `docs/targets/target-c/58-full-source-geometry-audit.md`: full-source
  circumradius and perimeter bounds. These are checked against the regression, not
  used to claim its global optimality.
- Canonical maximal-support KKT definitions, loaded-terminal degree constraints, and
  positive-contact connectivity in `docs/targets/target-c/01-force-hull-and-shear.md`.

The two audited inputs are unpromoted:
`research/target_c_leaf_fan_outerwalk_fork_2026-10-02.md` and
`research/target_c_leaf_fan_inward_spoke_kkt_fork_2026-10-02.md`.
All source points, including contact-isolated points if present in a canonical source,
remain present throughout. The explicit regression happens to have no contact isolates.

## 2. Audit disposition of the existing fork

The consecutive same-carrier leaf-block proof is valid: an edge at an intervening
loaded vertex would have to cross two leaf diameters, putting its other endpoint in
two disjoint hull arcs, unless it shares their carrier. The Woodall matching argument
correctly couples isolated K_2 components with core-path matching. Thus

`S>=h-3nu`, `A>=max(0,h-3nu-x_B)`, and
`A+x_B+3nu>=h>=ceil(D)`

survive audit. The run count is at most `nu+x_B`, so the long-run lower bound survives.

There is one correction. Equations (14) and (17) of the outer-walk report write
`A=D-o(D)` from the lower bound on A. Their cited premises give only

`A>=D-o(D)`.

No upper bound `A<=D+o(D)` is proved. Replace both equalities with lower bounds. The
conclusions `g->infinity`, `g=Omega(sqrt(D))` under `x_B=O(sqrt(D))`, and the
spoke/stress-flat fork need only the lower bound and remain valid. Section 5's phrase
“D-o(D) exact good fan contacts” can safely mean “at least D-o(D)”. The regression
below shows that even the geometric, full-stress, rank, and roundness premises do not
supply this missing upper bound. It does not refute a hypothetical stronger theorem
about global minimizers with an additional population argument.

The inward cone, injectivity, KKT equations, variation bound, and square-root fork
also survive audit. The short-arc step can be made explicit. All fan partners lie on
one radius-D circle and have pair distances at most D, so all minor angular
separations are at most pi/3. Choose one angle as zero; all others lie in
[-pi/3,pi/3]. If both signs occur, their extreme difference is less than pi, hence is
the minor separation and is at most pi/3. Thus the whole set lies on an ordinary
arc of width at most pi/3. Convex order agrees with angular order, and a chain of k
unit chords spans angle `2k asin(1/(2D))<=pi/3`. This justifies the monotonic-sine
step in the injectivity proof. It does not imply a unit triangle except in the stated
adjacent shared-neighbor case.

## 3. Stronger inward-spoke containment

**Claim (proved candidate awaiting promotion).** Let D>1 and let a,p_-,p,p_+ be source
points satisfying `|a-p_j|=D`, `|p-p_-|=|p-p_+|=1`, with p the middle point on the
short circular arc. If z is a third unit neighbor of p in a diameter-D unit-separated
source, then z lies strictly inside `conv{a,p_-,p_+}`. Consequently z is not an endpoint
of any actual diameter pair. For a triangle-free fan, its third neighbors are distinct
unloaded vertices of the positive-contact core.

**Proof.** Use the audited notation `eps=1/(2D)`, `tau=sqrt(1-eps^2)`,
`u=(p-a)/D`, and an orthogonal unit t. Relative to a, the three triangle vertices are

`a=(0,0)`, `p_-=(D-eps,-tau)`, `p_+=(D-eps,tau)`.

Write `p-z=ru+st`. The cone theorem gives

`r>=c=(eps+sqrt(3)tau)/2`, `|s|<=sqrt(1-r^2)`, `r<=1`.

The point z has coordinates `(D-r,-s)`. Its radial coordinate is strictly between
0 and D-eps because `D>1` and `r>=c>eps`. The remaining strict triangle condition is

`|s| < tau(D-r)/(D-eps)`.

For `r>=c`, `Dr>1`. Indeed `Dc=(1+sqrt(3)sqrt(4D^2-1))/4>1` for D>1.
The derivative of `sqrt(1-r^2)/(D-r)` has the sign of `1-Dr`, so its maximum over
[c,1] is at c. With `s_D=(tau-sqrt(3)eps)/2=sqrt(1-c^2)`,

`c+(D-eps)s_D/tau = D/2+sqrt(3)/(4tau) < D`,

because `D tau=sqrt(D^2-1/4)>sqrt(3)/2`. Hence
`s_D/(D-c)<tau/(D-eps)`, proving strict containment.

Any endpoint x of an actual diameter edge xy is uniquely exposed in direction x-y:
for every other source point w,

`2(x-y).(w-x)+|w-x|^2<=0`.

Thus it is an extreme point of the full source hull. The strictly interior z cannot be
such an endpoint. Positivity follows from `C=C_*` in the canonical representative.
Injectivity is the already audited exact fan argument. QED.

This improves the spoke-rich alternative to distinct actual unloaded attachments;
it does not bound their number or imply that they transfer force into a quadratic grain.

## 4. Exact round Reuleaux family

**Claim (regression).** For odd q>=5 and integer k>=2, there is an explicit
triangle-free unit-separated source with N=qk points and diameter

`D=1/[2 sin(pi/(2qk))]`,

whose full diameter graph is an odd q-cycle with k-1 pendant leaves at each carrier,
whose full contact graph is the convex N-cycle, and which has positive full-support
normalized KKT stress, PSD scalar stress with precisely the three affine modes, and
mixed rigidity rank `2N-3`. Every pendant fan has k-2 good fan contacts. The family
need not, and for q=k>=5 does not, minimize diameter globally.

### 4.1 Construction and actual diameter graph

Put `alpha=pi/q`, `Delta=alpha/k`, `r=(q-1)/2`,
`R=D/[2 cos(alpha/2)]`, and

`v_i=R(cos(2pi i/q),sin(2pi i/q))`, `i mod q`.

Join each consecutive core pair v_i,v_(i+1) by the outward convex circular arc of
radius D centered at `v_(i+r+1)`. Its central angle is alpha. Subdivide it into k
steps of central angle Delta and retain all subdivision points, identifying shared
core endpoints. These q arcs and their corner turns alpha form a convex closed
curve: arc turns total pi and corner turns total pi.

For every outward normal on an arc, its opposite supporting point is the center
core vertex, whose normal cone is exactly the opposite alpha-wide interval. This
follows directly from the displayed regular-core angles and odd q. Thus the two
support lines are distance D apart in every direction; the continuous body has
constant width and diameter D. An internal arc point has exactly its arc center as
a diameter partner. Core vertices have exactly two core partners at cyclic difference
r (and the internal points on the opposite arc). The full actual H is consequently
one odd q-cycle with k-1 pendant leaves per carrier. No inactive source pair is made
active by assumption.

The maximum matching is exactly q: the q core vertices cover H, while one pendant
edge at each carrier gives a matching of size q. Hence `nu=q`, `h=N`.

### 4.2 Unit separation and exact contact graph

A consecutive subdivision chord has length `2D sin(Delta/2)=1`. On one arc all
other subdivision distances exceed one by strict monotonicity of sine.

For two points on adjacent arcs, measured from their shared core vertex, their chord
lengths A,B are at least one unless one point is that core vertex. The angle between
the two successive directed chord vectors is

`alpha+(t+s)/2<=2alpha<pi/2`,

where t,s<=alpha are their central travels from the corner. Thus, if both points are
strictly off the corner, their distance squared is
`A^2+B^2+2AB cos(alpha+(t+s)/2)>2`. If one is the corner, equality one occurs only
for its immediate subdivision neighbor.

Every arc stays in the polar sector between its two core endpoints. Along the arc,
`|p|` is between D-R and R, and its polar angle is strictly increasing (the signed
cross product with its velocity is `D(D-R cos theta)>0`). Two nonadjacent arcs have
polar separation at least `2pi/q=2alpha` in the smaller direction. The radial
minimum used next is legitimate: since `alpha<=pi/5`,

`R cos(2alpha) <= D-R`,

which is equivalent to `cos^2(alpha)<=cos(alpha/2)`. Hence for radii in
`[D-R,R]` and angular separation at least `2alpha`, the squared distance is
nondecreasing in either radius; its minimum occurs at both radii `D-R` and
angle `2alpha`. Their source points therefore have distance at least

`2(D-R)sin(pi/q)`
`= [2cos(alpha/2)-1] sin(alpha/2)/sin(alpha/(2k))`
`>= (sqrt(3)-1)sqrt(3)=3-sqrt(3)>1`.

All contacts are therefore exactly the consecutive convex boundary edges. The
contact graph is C_N and is triangle-free. Every point is a nonisolated source point.
All loaded-hull intervals have length one: `x_B=0`, and

`A=q(k-2)`, `g=k-2`

on each same-carrier pendant run. The endpoints of each run connect through the
boundary cycle; no interior inward spoke or third contact occurs.

### 4.3 Positive full-support equilibrium

Put `beta=1/N` on every actual diameter edge and `lambda=D^2/N` on every contact.
At an internal arc point, the exact chord decomposition gives

`lambda[(p-p_-)+(p-p_+)]= (lambda/D^2)(p-a)=beta(p-a)`.

At a core carrier, symmetry makes both reactions radial from the common origin.
The two contact forces have total magnitude
`2lambda sin((alpha+Delta)/2)`. The diameter-force magnitude is

`beta D [2cos(alpha/2)+sin((alpha-Delta)/2)/sin(Delta/2)]`
`=2lambda sin((alpha+Delta)/2)`.

This uses the elementary finite cosine sum over its k-1 leaf partners and
`1/D=2sin(Delta/2)`. Thus every source vertex is in equilibrium and all coefficients
are positive. The diameter mass is exactly one.

### 4.4 PSD with exactly the affine kernel

Let `Omega=lambda L_C-beta L_H`. Eliminate all internal arc points. For one arc its
internal tridiagonal block is

`lambda[2cos(Delta) I - adjacency(P_(k-1))]`.

Its eigenvalues are `2lambda[cos(Delta)-cos(jpi/k)]>0`, j=1,...,k-1. Thus the
whole eliminated block is positive definite.

The off-diagonal Schur entry between an arc's two core endpoints is
`-a`, where `a=lambda sin(Delta)/sin(alpha)>0`, by the tridiagonal determinant
recursion `det T_j=sin((j+1)Delta)/sin(Delta)`.
The only other Schur off-diagonal entries connect the carrier to these endpoints,
which are precisely the edges of the core diameter q-cycle. Rotational symmetry,
row-sum zero, and exact affine equilibrium give the Schur matrix

`S=a L_(boundary q-cycle)-b L_(step-r q-cycle)`,
`b/a=sin^2(pi/q)/cos^2(pi/(2q))`.

On Fourier mode j its eigenvalue divided by 4a is

`sin^2(pi j/q)-[sin^2(pi/q)/cos^2(pi/(2q))]sin^2(pi r j/q)`.

For j=1,q-1 it is zero. For j=2,...,q-2, the first sine square is strictly greater
than `sin^2(pi/q)`, while the second is at most `cos^2(pi/(2q))` (q odd).
Hence it is strictly positive. Constants give the third zero mode. Schur congruence
proves `Omega>=0`, `rank Omega=N-3`, and
`ker Omega=span{1,P_x,P_y}` on this whole contact core.

### 4.5 Full mixed rigidity

Each subdivided arc together with its carrier is a chain of nondegenerate triangles
with sides (D,D,1), each sharing a diameter edge with its successor. It is rigid.
Two such rigid fan panels share a full core diameter edge; the panel-incidence graph
is a q-cycle with cyclic step r+1, connected because `gcd(r+1,q)=1`. A mixed bar flex
therefore gives the same Euclidean infinitesimal motion on every panel. Thus the
actual mixed rigidity matrix has rank `2N-3`. This proof requires no global-minimum
assumption, no C63 integrator, and no incident-diameter Euler-path inference.

### 4.6 Arbitrarily round square-root regime; explicit failure of global optimality

Take q=k odd and let q tend to infinity. Then

`D~q^2/pi`, `nu=q~sqrt(pi D)`, `x_B=0`,
`A=q(q-2)=(pi+o(1))D`, `g=q-2=Theta(sqrt(D))`.

The source circumradius satisfies

`R-D/2 = (pi/16)+o(1)`,

and its perimeter is N with `pi D-N=O(1/N)`. Thus the canonical full-source
circumradius and perimeter conclusions by themselves do not exclude this source.
It has all the local stress, PSD, rank, and fan properties above, yet its population
is only `N=(pi+o(1))D` rather than quadratic.

It is explicitly nonglobal. The q-by-q triangular-lattice grid
`{i(1,0)+j(1/2,sqrt(3)/2):0<=i,j<q}` has the same q^2 points and diameter
`sqrt(3)(q-1)<q^2/pi<D`. The first strict inequality holds for q>=5, for example
using `pi<22/7`, `sqrt(3)<7/4`, and `q^2>(11/2)(q-1)`.

This regression kills any proposed leaf-fan contradiction that uses only the listed
geometry, full-support equilibrium, PSD affine nullity, mixed rigidity, square-root
matching, and full-source roundness estimates. It does not refute a theorem retaining
global population, global minimality, the complete harmonic tiling, or the canonical
quadratic-core/source-extraction hypotheses.

## 5. What the audit does and does not close

The two published local fan reductions survive with the corrected population lower
bound. The inward fork now yields distinct *unloaded* attachments. The stress-flat
branch has a much stronger exact hostile regression than a lone local fan: all
vertices satisfy positive KKT equilibrium and both canonical rank conclusions.
A rank argument cannot force extra interior fan ports under just these premises.
The two boundary ports are present in the regression and transmit the fan stress.

No global branch is eliminated. Split-star O--O, inactive interfaces, macroscopic
inactive containers/exterior caps, nonconstant-phase blockers, and the remaining
full-core branches are still open. Contact-isolated source points may not be omitted
from any attempt to add a global population bridge.

## 6. Exact next obligation

Prove a source-level transfer theorem which excludes the displayed Reuleaux shell by
using the quadratic population that a true large global minimizer must retain:
for the low-x_B, nu=O(sqrt(D)) branch, the fan stress-flat segments or their distinct
unloaded spokes must couple to a quadratic actual source grain in a manner that
forces either an exact unit triangle or a same-cardinality strict sub-D competitor.
The coupling must control all remaining source points and inactive constraints; the
round shell alone supplies no such coupling. That theorem is not proved here.

## 7. Certificate scope and audit table

The verifier constructs finite q=k=5,7,9 members and q=5,k=2,11 members with rational interval bounds for
all trigonometric quantities. It certifies every strict inactive-pair gap, exact graph
counts and matching witness/cover, the connected triangle-panel rigidity witness,
strict Schur Fourier eigenvalue gaps, and the smaller same-cardinality grid margin.
Contact and diameter equalities, the KKT identities, and the infinite-family claims
are proved above; an interval containing zero is never treated as proof of equality.

| Claim | Classification | Disposition |
|---|---|---|
| Leaf consecutivity and `A+x_B+3nu>=h` | audited-working in this audit; unpromoted | proof survives |
| `A=D-o(D)` from the stated lower bound | rejected inference | replace by `A>=D-o(D)` |
| Inward cone, injectivity, KKT transport/fork | audited-working in this audit; unpromoted | proof survives |
| Third neighbors strictly interior and unloaded | proved candidate awaiting promotion | full proof in Section 3 |
| Long stress-flat fans contradict positive KKT/PSD/full rank/roundness | regression | Sections 4.1--4.6 disprove this broadened local claim |
| Round Reuleaux shells are global minimizers | rejected | explicit smaller same-cardinality grid |
| C-II or Level I closure | not claimed | global transfer remains open |
