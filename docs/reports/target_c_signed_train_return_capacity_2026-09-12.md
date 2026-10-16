<!-- theorem-state: {"artifact_id":"ART-37E4039C2418","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — signed train-return capacity

**Date:** 2026-09-12  
**Repository commit:** `bd7bede30ec0620bed0abaa5a26912e54e437dd7`  
**State version:** `2026-09-12.audit.44`  
**Run type:** closing-proof attempt / new structural bridge  
**Target:** C-II, full-core branch  
**Classification:** proved candidate awaiting promotion; artifact remains unreviewed  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** not used

## LEVEL I STATUS

**STILL OPEN. C-II remains open.** No new canonical result is declared here.

## 1. Locked endpoint and implication chain

The canonical full-core branch has locally rhombus-saturated harmonic cells, exact
physical train endpoints, inverse-phase train shores, and the Section-104 explicit
carrier bound. The inactive-container branch remains independent and open.

This run tests a constraint not used in the two-shore, one-host-per-shore argument:
the two physical boundary ends of each train have **opposite oriented edge vectors**.
Projective endpoint counts discard this return requirement.

```text
signed train-return capacity
 -> lower bound for the SAME cell's actual route excess
 -> contradiction if that bound exceeds its Section-82/104 route budget
 -> exclusion of that C-II regime (not all of C-II without a global budget bridge).
```

At zero route excess this gives a new structural conclusion: two distinct projective
train atoms require at least four distinct oriented corridor directions. Three
corridors cannot support them, regardless of their angular separations. This is
stronger as a conditional geometric statement than checking the particular three
Section-101 chord directions against a sixty-degree separation. Its application to
that already-excluded endpoint does not advance the canonical numerical frontier.

The original checkout changed during bootstrap. Its state changes from `617a9ca` to
the commit above were compared explicitly. Research then moved to an isolated
worktree. Later PRs and their improved constants are not premises of this report.

## 2. Finite oriented-return theorem

Let \(\mathcal R\) be a finite edge-to-edge complex of strict unit rhombi from the
canonical contact embedding. Components and holes are allowed. A physical boundary
edge means an edge incident to exactly one retained rhombus. Orient every such edge
with its incident rhombus on its left. Boundary occurrences, not merely endpoint
vertices, are the objects counted below.

Let \(\mathcal T\) be any chosen set of \(k\) complete trains of this complex. The
trains must be continued to the physical boundary of the complex; stopping at an
arbitrary phase-bin cut and treating the artificial cut as an outer route is invalid.

Choose directed unit-edge walks \(W_1,\ldots,W_m\) of lengths \(\ell_j\), with
nonzero displacements \(z_j\), and write

\[
 q_j=z_j/|z_j|,\qquad
 E=\sum_j(\ell_j-|z_j|),\qquad Q=\{q_1,\ldots,q_m\}.
\]

Every endpoint called **good** must be assigned injectively to a walk edge occurrence
with exactly its physical-boundary orientation. All other selected train endpoints
are bad. Let \(b\) be their number. Different selected endpoints may not use the
same walk occurrence. The walks can include additional edges that end no selected
train. Occurrence multiplicity, including any bridge traversal, is retained.

### Theorem SR — signed return bound

Set

\[
 \delta(Q)=2-\max_{i,j}|q_i-q_j|\ge0.
\]

Then

\[
 \boxed{E\ge \delta(Q)\,(k-b)_+.} \tag{SR.1}
\]

More precisely, choose either unit orientation \(u_\tau\) of each train's parallel
edges and define

\[
 w_Q(u)=\max_j q_j\cdot u-\min_j q_j\cdot u.
\]

For the set \(\mathcal T_{gg}\) of trains with two good ends,

\[
 \boxed{E\ge\sum_{\tau\in\mathcal T_{gg}}(2-w_Q(u_\tau)).} \tag{SR.2}
\]

The summands are independent of the choice of sign of \(u_\tau\). Neither estimate
requires a phase cut, a complete grid, a sixty-degree limiting angle, or a KKT weight
bound.

### Proof: opposite boundary orientations

Orient the parallel edges of a train by a unit vector \(u\). Its centerline moves
strictly in the coordinate \(\det(u,x)\), by canonical Theorem 10.6. At its initial
end, the incident rhombus is on the positive side of the line directed by \(u\), so
the physical boundary orientation is \(u\). At its terminal end, the incident rhombus
is on the negative side, so that orientation is \(-u\). This local argument also
applies to holes and disconnected complexes. There are exactly two ends per train.

Write the directed unit steps of walk \(j\) as \(v_{j,r}\). Exactly, not just to
first order,

\[
 \ell_j-|z_j|=\sum_r(1-q_j\cdot v_{j,r}). \tag{SR.3}
\]

Every summand is nonnegative. If the two ends of a train are assigned to walks
\(i,j\), their combined contribution is

\[
 (1-q_i\cdot u)+(1+q_j\cdot u)
 =2-(q_i-q_j)\cdot u
 \ge2-w_Q(u)\ge\delta(Q). \tag{SR.4}
\]

Injectivity permits summation without spending an occurrence twice. Discard all
other nonnegative walk contributions to get (SR.2). Each train not in
\(\mathcal T_{gg}\) consumes at least one bad endpoint, hence
\(|\mathcal T_{gg}|\ge(k-b)_+\). This proves (SR.1). In particular, two endpoints
on the same directed walk cost exactly two units of projection loss. \(\square\)

### Sharpness and limitations

For fixed host directions and a free train direction, the algebraic minimum in
(SR.4) is exactly \(2-|q_i-q_j|\), attained when \(u\) is parallel to
\(q_i-q_j\). This is sharp for the local endpoint-cost relaxation. No assertion is
made that an arbitrary optimizing assignment is realized by a C-II source.

The theorem gives no positive universal constant if two host directions are
antipodal. In particular, replacing the oriented \(q_j\) by projective directions
is false. A square's bottom and top boundary edges have opposite orientations and
zero route excess, although their projective directions coincide.

## 3. Zero-excess corridors must supply antipodal returns

Consider a sequence of complexes with scale \(D\to\infty\). Suppose the number
of designated directed routes is a fixed finite \(m\), their directions converge
to \(q_1,\ldots,q_m\), and their total excess is \(o(D)\).

Suppose a chosen family of complete trains has size at least \(\eta D\),
\(\eta>0\), all its projective directions converge uniformly to one projective
direction \([u]\), and only \(o(D)\) of its endpoints are bad.

### Corollary AR — antipodal return necessity

Both \(u\) and \(-u\) belong to \(Q\).

Indeed, all but \(o(D)\) of the family's trains have two good endpoints. Uniform
convergence, continuity of \(w_Q\), and (SR.2) imply

\[
 2-w_Q(u)=0.
\]

For unit vectors, each scalar product lies in \([-1,1]\). Width two therefore
requires a host with scalar product one and a host with scalar product minus one,
which are precisely \(u\) and \(-u\). \(\square\)

### Corollary FC — four-corridor obstruction

Under the same route assumptions, two linear train families with distinct limiting
projective directions and \(o(D)\) bad endpoints each require at least four distinct
limiting oriented host directions. Thus \(m\le3\) is impossible.

Apply AR to both families. Distinct projective directions give disjoint antipodal
pairs. This uses the fact that the trains themselves return; counting an arbitrary
linear collection of boundary edges does not give this conclusion.

### Application to the already-canonical Section-101 endpoint exclusion

Canonical Section 90 supplies two linear families of complete local trains with
limiting projective directions separated by \(\pi/3\). Canonical Sections 101–102
give three principal complement routes of total excess \(o(D)\), and show that
only \(o(D)\) endpoints of either family lie off these routes: exceptional faces,
nonprincipal routes, and exceptional teeth have sublinear endpoint capacity, while
fixed-phase ends disperse on the curved dense tooth arc.

Physical rhombus boundary edges on these outer routes use the induced outer-face
walk orientation with the bounded rhombus on the left. Restricting to that assignment
therefore meets SR's orientation hypothesis. If an outer walk also traverses an edge
with no rhombus on its left, that occurrence is not assigned an endpoint.

FC now contradicts the existence of the two families. This supplies an alternative
structural closing bridge for the endpoint, without computing its three pairwise
projective chord separations. It does not reclassify or strengthen the canonical
Section-102 carrier theorem by itself.

## 4. A uniform three-corridor area bound — no phase extraction

The signed return constraint can be summed over **all crossings**, avoiding the
small constants from selecting two particular inverse-phase shores.

### Lemma TW — exact two-direction, three-host optimization

Let \(u,v\) be unit vectors at projective angle
\(\varphi\in(0,\pi/2]\), and let \(a,b>0\). Among sets \(Q\) of at most three
unit host vectors,

\[
 \min_Q\{a(2-w_Q(u))+b(2-w_Q(v))\}
 =a+b-\sqrt{a^2+b^2+2ab\cos\varphi}. \tag{TW}
\]

To prove this, replace \(v\) by its negative if necessary so \(u\cdot v\ge0\).
The weighted sum of widths is the sum of four support maxima for the four vectors
\(au,-au,bv,-bv\). Assign each maximum to a realizing host. At most three hosts
force at least two of these four vectors into the same group. The triangle
inequality shows that such a pair loses at least

\[
 a+b-\sqrt{a^2+b^2+2ab\cos\varphi}
\]

from the unconstrained total \(2(a+b)\). A pair of opposite vectors loses \(2a\)
or \(2b\), no less; a cross pair has its smallest loss at the acute orientation.
Additional groupings cannot recover this loss, again by the triangle inequality.
The bound is attained by hosts
\((au+bv)/|au+bv|,-u,-v\). This proves (TW) and its sharpness as a host relaxation.

In particular, for any three hosts and two crossing strict-rhombus trains,

\[
 (2-w_Q(u))+(2-w_Q(v))\ge 2-\sqrt3=:c_{ret}>0, \tag{TW.1}
\]

since their projective angle is strictly greater than \(\pi/3\). No limiting
phase theorem is used here.

### Theorem AT — three-corridor area transport

Use SR with at most three walks. Assume the complex lies in a convex container of
diameter \(d\). Retain any trains with two good ends, and let \(A_{gg}\) be the
sum of areas of rhombi whose **both** trains are retained. Then

\[
 \boxed{d E\ge(2-\sqrt3) A_{gg}.} \tag{AT.1}
\]

If SR selects all trains, \(A_4\) denotes the full rhombic area, and \(b\) counts
all bad physical endpoints, then also

\[
 \boxed{E\ge(2-\sqrt3)(A_4/d-b)_+.} \tag{AT.2}
\]

**Proof.** Write \(\delta_\tau=2-w_Q(u_\tau)\ge0\). Multiply (TW.1) at every
retained-retained crossing by the area of its rhombus and sum. The result is

\[
 c_{ret} A_{gg}
 \le\sum_{\tau\ retained}\delta_\tau
       \sum_{R\in\tau,\ R\ retained-retained}\operatorname{area}(R)
 \le d\sum_{\tau\ retained}\delta_\tau
 \le dE.
\]

The middle inequality is the exact transverse-span bound from Section 89: the sum
of areas along a complete train is its transverse endpoint displacement, at most
\(d\). SR.2 supplies the last inequality. Every excluded train uses at least one
bad endpoint, so there are at most \(b\) such trains. Their total incident rhombic
area is at most \(bd\), and every rhombus not counted in \(A_{gg}\) meets one of
them. Thus \(A_{gg}\ge(A_4-bd)_+\). This proves (AT.2). \(\square\)

This is a finite area-to-route-excess inequality on the actual embedding. It is not
just a population extraction result. Bad-end capacity cannot be dropped: four
straight sides can bound an arbitrarily large strict-rhombus parallelogram with
zero excess, but using only three sides makes an entire linear train family bad.

### Theorem DP — diffuse bad directions cannot hide quadratic area

Suppose all trains are selected. Call a train bad if at least one of its ends is
bad, count it only once, and let \(M_{bad}(\varepsilon)\) be the largest number of
bad trains in any closed projective direction interval of angular length
\(\varepsilon\). Let \(T\) be the full train count and
\(\Delta=\sum_R(\varphi_R-\pi/3)\) the angular defect. For
\(0<\varepsilon<\pi/6\),

\[
 A_{gg}\ge A_4-2T M_{bad}(\varepsilon)-\Delta/\varepsilon. \tag{DP.1}
\]

For a fixed other train, bad trains crossing it at angle in
\((\pi/3,\pi/3+\varepsilon]\) lie in two projective direction intervals of length
\(\varepsilon\). They supply at most \(2M_{bad}(\varepsilon)\) crossings, since
two complete trains cross at most once. Summing over all other trains overcounts,
which is harmless. Rhombi at larger angle number at most \(\Delta/\varepsilon\).
Every rhombus has area at most one. These observations prove (DP.1).

Combining with AT gives the exact finite inequality

\[
 \boxed{dE\ge c_{ret}
 (A_4-2T M_{bad}(\varepsilon)-\Delta/\varepsilon)_+.} \tag{DP.2}
\]

Consequently, if \(d\le D\), \(T=O(D)\), \(\Delta=O(D)\), \(A_4\ge cD^2\)
for fixed \(c>0\), and

\[
 \lim_{\varepsilon\downarrow0}\limsup_{D\to\infty}
 {M_{bad}(\varepsilon)\over D}=0, \tag{DP.3}
\]

then three routes cannot have excess \(o(D)\). First fix \(\varepsilon\), take
the large-\(D\) limit in DP.2, and then decrease \(\varepsilon\). This order of
limits is essential; no uniform microscopic convergence rate is asserted.

Condition (DP.3) is an explicit new obligation, not an automatic consequence of
many candidate endpoints. It concerns all bad trains in a direction window, not
only a chosen shore. No application beyond the proved hypotheses is claimed here.

## 5. Exact dependencies and frontier effect

| Input / claim | Lifecycle | Use |
| --- | --- | --- |
| `docs/theory/01-local-structure.md`, Theorem 10.6 | canonical | Complete train paths, monotonicity, two physical ends |
| `C-HARMONIC-TRAIN-BUDGET`, Section 89 | canonical | Local train objects and boundary occurrence convention |
| `C-DENSE-PHASE-CORE`, Section 90 | canonical | Two linear inverse-phase families for the endpoint application |
| `C-WRAP-COMPLEMENT-CHORD`, Section 101 | canonical | Endpoint support and route saturation |
| `C-PHASE-CORRIDOR-ENDPOINT-EXCLUSION`, Section 102 | canonical | Off-principal endpoint dispersion, not its final angle contradiction |
| SR, AR, FC, TW, AT, DP | proved candidates awaiting promotion | New signed-pairing and area-return bridge; no independent audit yet |
| Universal source exclusion from these inequalities | conditional | Requires a new all-regime route/endpoint budget theorem |

The finite return and area transport inequalities are new proposed theorem content. The already-excluded
endpoint stays excluded; no constant is advertised as improved. The main sharpening
is a necessary **oriented antipodal corridor structure**, which remains meaningful
outside the particular Section-101 extremal gap profile.

## 6. Exact remaining obligation

A sufficient new all-regime Type-II theorem would provide, on an actual harmonic
cell of every sufficiently large survivor, designated directed routes and a family
of complete trains such that

\[
 \sum_{\tau\in\mathcal T_{gg}}(2-w_Q(u_\tau))
 >\sum_j(\ell_j-|z_j|). \tag{RC}
\]

Here both sides must be bounded independently from the canonical source data, with
all non-route endpoints charged and no artificially cut train treated as complete.
SR would then exclude that survivor. Currently this comparison is established only
in a previously excluded endpoint regime; it is **not** known for all Type II.

AT and DP sharpen the available route to (RC): it suffices to certify, on the same
cell and with at most three directed routes,

\[
 (2-\sqrt3)
 (A_4-2T M_{bad}(\varepsilon)-\Delta/\varepsilon)>dE. \tag{RC-area}
\]

This formulation uses the entire retained rhombic area rather than two extracted
families. The unproved part is a source-specific upper bound on the directional
bad-end profile and on the actual route excess, valid outside the small-slack
regime. Neither the existence of three appropriate routes nor that bound is claimed
for a general C-II survivor.

In particular, the existence of a long carrier, many cavities, or many candidate
train ends does not establish (RC). General survivors can have linear exceptional
endpoint capacity and linear route excess. The macroscopic inactive-container
branch also remains: no SR argument moves, replaces, or deletes its old core.

## 7. Regression and scope audit

| Binding issue | Result |
| --- | --- |
| Source versus abstract response object | All applications use the actual cell's rhombi and walks; arbitrary assignments are only relaxations |
| Simultaneous compatibility | Endpoint injection is imposed, not inferred from one-at-a-time feasibility |
| Boundary-order losses | Bad endpoints and actual route excess remain explicit in SR |
| Projective/oriented ambiguity | Unit square rejects projective replacement of host directions |
| Holes and bridge multiplicity | Local side-of-edge proof; count assigned physical occurrences exactly once |
| Contact-isolated source points | Retained throughout; no assertion on their stress or kernel |
| Local geometry versus global optimality | SR is finite geometry; global optimality enters only through named canonical applications |
| Near equality versus exact unit triangle | No near-equilateral face is promoted to an exact triangle |

## 8. Literature and computation

No literature theorem is imported. The general proofs above are analytic. An exact
finite certificate for orientation, return pairing, and projection accounting will
be recorded separately; it cannot certify a global minimizer or the missing (RC).

## 9. Promotion recommendation and handoff

**Unreviewed.** Preserve the result for independent audit. Do not change the state
version or current C-II gate on the basis of this alternative endpoint proof.

Read Theorem 10.6, Sections 89, 90, 101, 102, and this report when auditing. The next
new work is an all-regime, source-specific bound in (RC), not a recount of arbitrary
projective endpoints. Any complete C-II resolution must also close Type I.
