<!-- theorem-state: {"artifact_id":"ART-6EB3D5F41D00","canonical":true,"claim_ids":["C-PENTAGON-WALL-DISJOINT-BULK"],"claim_statuses":{"C-PENTAGON-WALL-DISJOINT-BULK":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — quadratic train bulk survives disjoint terminal pentagon walls

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** c7466005. **State:** 2026-09-14.audit.51.
**Classification:** canonical in `2026-10-05.audit.54` as `C-PENTAGON-WALL-DISJOINT-BULK`; the low-endpoint-defect pentagon-pair localization was rederived independently in the promotion audit rather than imported from the deleted automation branch. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Statement and exact purpose

Let \(\mathcal P\) be any family of complete actual stopped trains whose
two terminal occurrences are on bounded physical unit pentagons. Let
\(P=|\mathcal P|\), and let \(R_{PP}\) count strict rhombi whose two
crossing trains both belong to \(\mathcal P\). Set

\[
K=250,\qquad c_K=\frac1{(K+1)^2}
\left(\frac K{K+1}\right)^{2K}>0.
\]

**Theorem W.1.** There is a subfamily \(\mathcal A\subseteq\mathcal P\)
such that all its terminal pentagon walls have pairwise disjoint source
vertex sets, including the two walls belonging to one train, and

\[
\boxed{R(\mathcal A)\ge
c_K\left[R_{PP}-(4+K/2)P\right]_+.}
\tag{W.1}
\]

Here \(R(\mathcal A)\) counts **actual** strict-rhombus crossings of
selected trains. In particular, if \(P=O(D)\) and
\(R_{PP}=(\Delta_2-o(1))D^2\), then

\[
R(\mathcal A)\ge(c_K\Delta_2-o(1))D^2.
\tag{W.2}
\]

This supplies genuine quadratic crossing currency together with separate
terminal source walls. It removes global terminal-wall reuse from this
train subfamily. Selected train interiors still cross; they are not
disjoint crosscuts and do not form a dual-tree deformation chart.

The intended implication is

\[
\text{pentagon-to-pentagon quadratic bulk}
\ \Longrightarrow\ \text{wall-disjoint macroscopic train family}
\ \Longrightarrow\ \text{separate source walls for a collective replacement}.
\]

The last step remains unproved. No activation is claimed.

## 2. Source hypotheses and dependencies

Use the canonical triangle-free C-II positive-contact core, with every
original source point retained. Physical pentagons are bounded actual
contact faces, not hull pockets or completion cells. Their walls have
five actual unit edges and five distinct source vertices.

The stopped-train geometry supplies a simple triangle-free crossing
graph and monotone transverse projection. A train crossing one strict
unit rhombus advances at least \(a_0=\sqrt3/2\) in a consistently oriented
normal to its contact direction. This is the same elementary projection
step used in
[Section 69.6](../targets/target-c/69-coherent-grain-interface-audit.md).
The canonical local unit-separation bound gives contact degree at most
five: six unit neighbors would have all angular gaps equal to \(\pi/3\)
and would already contain a unit triangle.

No reciprocal-rank premise is needed for Theorem W.1. If a train had
both ends on the same pentagon, it would enter the self-overlap class
removed below. Repeated endpoint pairs are likewise allowed in the
finite incidence argument, counted by their terminal occurrences. The
separate [positive reciprocal candidate](target_c_positive_reciprocal_internal_train_graph_2026-10-05.md)
excludes those multiplicities in the canonical source class, but this
thinning result does not depend on its independent acceptance.

## 3. Remove trains whose own two walls overlap

Every pair of vertices on a unit pentagon is joined by a wall path of
at most two unit edges, so their Euclidean distance is at most two.
The same bound holds from a wall vertex to any wall edge midpoint by
convexity of the norm.

Suppose the terminal pentagons of a train share a source
vertex \(v\). Both terminal edge midpoints are within distance two of
\(v\), hence their mutual distance is at most four. If the train crosses
\(r_\tau\) rhombi, monotone projection gives

\[
a_0r_\tau\le4.
\]

Since \(5a_0>4\), necessarily \(r_\tau\le4\). Remove all such trains
from \(\mathcal P\). At most \(4P\) crossing edges are lost, even if
both ends of a lost crossing are removed. Singleton trains cause no
problem. No source vertex or source constraint is deleted.

## 4. Global wall-conflict graph has bounded degree

For each remaining train, its support is the union of its two disjoint
five-vertex terminal walls. Make a conflict graph: two trains conflict
when these source-vertex supports intersect.

At one source contact vertex, at most five physical pentagonal faces
are incident, because face occurrences around it are bounded by contact
degree. A physical pentagon has five terminal train occurrences, so at
most \(5\cdot5=25\) trains have a terminal pentagon containing this
vertex. A ten-vertex support therefore meets at most \(10\cdot25=250\)
trains. In particular the conflict degree is at most \(K=250\). This
deliberately generous bound includes all shared-face and shared-vertex
reuse and repeated face-side occurrences.

The number of strict-rhombus crossing edges whose two trains conflict
is at most the number of conflict edges, at most \(KP/2\). Delete these
crossings only from the auxiliary counted graph. The number of remaining
nonconflicting crossings is at least

\[
R'=\left[R_{PP}-(4+K/2)P\right]_+.
\tag{W.3}
\]

The use of simplicity here is explicit: one train pair contributes at
most one actual rhombus crossing.

## 5. Thin without losing quadratic bulk

Choose each remaining train independently with probability
\(p=1/(K+1)\). Retain a chosen train only if none of its conflict
neighbors was chosen. The retained family has pairwise disjoint terminal
source walls.

For a nonconflicting crossing pair \(\tau,\sigma\), retaining both
requires choosing these two trains and not choosing any vertex in
\(N(\tau)\cup N(\sigma)\). Neither selected endpoint belongs to this
neighborhood union. Its size is at most \(2K\), so the exact probability
is at least

\[
p^2(1-p)^{2K}=c_K.
\]

By linearity of expectation, the expected retained crossing count is
at least \(c_KR'\). Some outcome attains at least that count. This
proves (W.1). No independence between different crossing events is
assumed; overlapping neighborhoods only improve the displayed bound.

## 6. Macroscopically long, wall-disjoint source trains

Under (W.2), the canonical total train bound is \(T\le3\pi D\).
Define fixed positive constants

\[
\gamma=\frac{c_K\Delta_2}{12\pi},\qquad
\rho=a_0\gamma.
\]

Eventually \(R(\mathcal A)\ge(c_K\Delta_2/2)D^2\). Discard trains with
fewer than \(\gamma D\) crossings in this selected graph. At most
\(3\pi\gamma D^2=(c_K\Delta_2/4)D^2\) crossings are lost. Thus the
remaining wall-disjoint family \(\mathcal L\) satisfies

\[
R(\mathcal L)\ge\frac{c_K\Delta_2}{4}D^2,
\qquad |\mathcal L|\ge\sqrt{c_K\Delta_2}\,D,
\tag{W.4}
\]

where the cardinality bound is Mantel applied to its actual crossing
graph. Every retained train had at least \(\gamma D\) crossings before
the final discard, hence its complete source midpoint path crosses at
least that many rhombi. Its terminal edge midpoints obey

\[
|x_\tau-y_\tau|\ge a_0\gamma D=\rho D.
\tag{W.5}
\]

The inequality uses monotone source projection, not reciprocal length.
The midpoint endpoints are actual source contact-edge midpoints; their
wall vertices lie within bounded distance. No loaded endpoint is
inferred from a bounded-face endpoint.

## 7. Application after current-main hull depletion

The audit.54 promotion audit independently rederives the elementary occurrence bound originally recorded on commit `cae7122a`:

\[
M-P\le2m_B+u_B+6(Q-f).
\]

It follows directly by assigning every non-pentagon-pair depleted train
one bad outer or degree-at-least-six terminal occurrence. Different
trains have different chosen occurrences. Its load-bearing premise is
the independently audited current-main #699 hull depletion theorem.
We import no additional authority from the branch's merge status.

Thus under \(m_B,u_B,Q-f=o(D)\), the current-main depleted quadratic
bulk lies on pentagon-pair trains up to \(o(D^2)\) lost crossings.
Theorem W.1 applies and yields (W.4)–(W.5), even if the pentagon-pair
premise allows both ends on one pentagon.

## 8. Audit limits and verifier

The exact rational
[incidence verifier](../../research/verify_target_c_pentagon_wall_disjoint_bulk_2026_10_05.py)
enumerates 1,656 Bernoulli outcomes and checks 47 nonconflicting pair
probabilities, the full support-disjointness test, bounded vertex/face
incidence, and the thinning constant. Its rosters are abstract incidence
packets, not geometric source embeddings. The monotone source projection
argument and asymptotic transfer are analytic proofs above.

The quadratic bulk retained here cannot be used for second depletion:
second depletion requires a family carrying \(o(D^2)\) rhombi. Nor does
wall disjointness give a uniform finite shear radius. All selected trains
can interact through their interiors, and all unselected contacts and
all diameter constraints still have to be respected by any replacement.
Contact creation alone still does not imply positive force activation.
