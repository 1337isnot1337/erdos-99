<!-- theorem-state: {"artifact_id":"ART-446B566C87F6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->

> **Destination status (2026-10-16).** This is a source-only historical Target B candidate recovered from commit `12f6833725f281ce39a6d04ebcb45630b3a6768f`; that commit is not an ancestor of the frozen source main and the file is absent from its tree. The exact report is retained because the frozen Target C terminal-cancellation report links it. Its TC1/TC2 claims remain unreviewed and noncanonical, and they are not premises of the destination's canonical Target C face-floor claim. The destination theorem-state remains authoritative.

# Target B: terminal cancellation in the boundary graph

Date: 2026-10-08.
Classification: proved candidate awaiting independent audit/promotion.
Registry status: unreviewed; noncanonical.
Level I: open.

Base: 462456b7b34140ea2c88aec71ffe3e1d5a0a6e6d.
State: 2026-10-08.audit.129.
Route: Target B, jammed pure strict-unit-rhombic disks.

## 1. Claim and its use

Consider any sequence in the scope of canonical
[Section 39](../targets/target-b/01-jammed-rhombic-branch.md).
Keep its notation: \(D\to\infty\), \(T\) physical complete trains,
\(R\) rhombi, \(q\) convex-hull vertices, \(T=\Theta(D)\),
\(q/T\to y\), and the projective train-direction probability measure
\(\mu_T\Rightarrow\mu\). Let \(s\) be the total atomic mass of \(\mu\).

The new candidate is

\[
\boxed{s\le 1-y.}
\tag{TC1}
\]

The canonical estimate is \(s\le1-y/2\). Its separate-end charge does not
use cancellation between the two ends of a short train. TC1 does.

Put \(c=2\sqrt3/\pi\) and \(A=2/\sqrt c=\sqrt{2\pi/\sqrt3}\).
Combining TC1 with canonical Sections 39.1 and 39.3 gives

\[
\boxed{
\liminf {T\over D}\ge 2A,\qquad
\liminf {q\over D}\ge A,\qquad
\liminf {T-q\over D}\ge A,\qquad
\limsup {q\over T}\le{\pi\over\pi+A}.
}
\tag{TC2}
\]

These are necessary conditions on the same source, not an existence claim
for charts, packets, or new point placements. The implication under study is

    paired physical terminals cancel in small boundary components
      -> nonatomic train count >= q-o(D)
      -> the canonical neutral train dimension T-q is >= A D-o(D)
      -> a blocker/coforest rank bound below A D, together with exclusion
         of the stressed equality kernel, would exclude this branch.

The last rank bound and equality exclusion are not proved here.
This is exploratory toward Level I:
it strengthens the quantity in the canonical rank obstruction but does not
establish the joint shell inequality, general-topology extension, or a strict
competitor.

## 2. Canonical inputs and geometric hypotheses

Only the following statements are imported.

1. [Theorem 10.6 and its proof](../theory/01-local-structure.md):
   trains are physical paths of opposite rhombus edges; each has two boundary
   terminals; the crossing graph is simple and triangle-free. A train through
   \(d_\tau\) rhombi joins its terminal midpoints by \(d_\tau\) unit
   displacement segments. Its two directed terminal vectors in the positively
   oriented outer boundary are opposite.
2. Target B Sections 36 and 39: the full source is the vertex set of a
   simply connected strict-unit-rhombic disk; its outer unit-edge walk has
   \(2T\) occurrences; \(T=\Theta(D)\), \(R/D^2\to1/c\), and the scaled
   convex hulls converge to the disk of radius \(1/2\).
3. Section 39.1: the ordered crossing measure has a weak limit supported on
   pairs of atoms of \(\mu\), and \(R/T^2\le s^2/4+o(1)\).
4. Section 39.3: pinned rigidity gives \(q\ge T/2+1\).
5. Sections 40 and 42: \(\dim\mathcal L\ge T-q\), and the backward-flip
   map either has full rank on \(\mathcal L\) or has a nonzero kernel
   contained in a stressed equality subspace for some active bar.

No positive lower bound on stress coefficients is assumed. No source
vertex is removed. A label assigned to a train below does not change its
physical rhombi or its terminal edges.

Let the hull vertices be \(v_1,\ldots,v_q\), in positive cyclic order. The
outer boundary partitions into chains \(\Gamma_i\) from \(v_i\) to
\(v_{i+1}\). Write \(L_i\) for their numbers of unit occurrences and
\(r_i=v_{i+1}-v_i\) for their hull chords. Unit separation gives
\(|r_i|\ge1\). Also \(\sum_i L_i=2T\).

After a common translation, \(K/D\) converges to the radius-\(1/2\) disk.
The hull surface-area measures

\[
\sigma_D={1\over D}\sum_i |r_i|\delta_{n_i}
\Rightarrow {1\over2}\,d\theta
\tag{TC3}
\]

therefore have an atomless limit; \(n_i\) is the outward hull-side normal.
This is the same support-function argument used in Section 39.2.

We also use this immediate convex consequence. If a bounded number of hull
chains have bounded \(L_i\), and their base vertices are \(o(D)\) apart,
then all their outward normals differ by \(o(1)\). Indeed every subsequential
normalized vertex limit is one point \(x\) of the limiting circle, and any
limiting support normal \(n\) satisfies \(x\cdot n=1/2\); this forces
\(n=2x\).

## 3. Separate atomic trains without assuming a convergence rate

There exist subsets \(\mathcal A_D\) of the physical train set such that

\[
{|\mathcal A_D|\over T}\to s,\qquad
{1\over T}\sum_{\tau\in\mathcal A_D}\delta_{\phi_\tau}
\Rightarrow\mu_{\rm at},
\qquad
\sum_{\tau\notin\mathcal A_D}d_\tau=o(D^2).
\tag{TC4}
\]

Here \(\mu_{\rm at}\) is the atomic part of \(\mu\), including all its
countably many atoms. We do not identify this set with a retained
Section-50 component.

To justify TC4, take increasing finite atom sets \(F_j\) exhausting
\(\mu_{\rm at}\), and unions \(U_j\) of neighborhoods of those atoms.
For each fixed \(j\), choose the radii sufficiently small that the
\(\mu\)-mass in \(U_j\) beyond \(F_j\) is at most \(1/j\), their maximum
radius is at most \(1/j\), and their boundaries have zero \(\mu\)-mass.
The crossing-measure limit is supported on atom pairs. Its mass incident
to a train outside \(U_j\) tends to zero as \(j\to\infty\).

For fixed \(j\), weak convergence controls the train mass and crossing
mass of \(U_j\). Choose \(j=j(D)\to\infty\) slowly enough that all these
fixed-\(j\) limits hold to error \(1/j\); put
\(\mathcal A_D=\{\tau:\phi_\tau\in U_{j(D)}\}\).
The finite-atom approximation proves its direction-measure convergence,
and the ordered crossing measure counts
\(\sum_{\tau\notin\mathcal A_D}d_\tau/T^2\) exactly. Since \(T=\Theta(D)\),
this proves the last part of TC4.

Call the complementary trains \(\mathcal N_D\), and put \(N_D=|\mathcal N_D|\).
This notation labels the limiting non-atomic population; an individual
finite train still has a single direction.

TC4 implies that, for some \(\epsilon_D\to0\), all but \(o(D)\) trains
in \(\mathcal N_D\) have their two terminal midpoints at distance at most
\(\epsilon_D D\). Indeed their distances are at most \(d_\tau\); choose
\(\epsilon_D\to0\) slowly and apply Markov to the sum in TC4.
Call the exceptional trains long.

## 4. The boundary multigraph

Make one graph vertex for each hull chain \(\Gamma_i\). For each train in
\(\mathcal N_D\), insert one edge between the chains containing its two
terminal occurrences. Allow loops and parallel edges. All \(q\) vertices
are retained, including isolated ones. Let \(b_D\) be the number of
connected components.

Every connected multigraph has at least its number of vertices minus one
edges, even when it contains loops. Consequently

\[
N_D\ge q-b_D.
\tag{TC5}
\]

We prove \(b_D=o(D)\). This is where both terminals are used together.

Fix integers \(M,L\). There are at most \(q/(M+1)\) components having
more than \(M\) vertices. At most \(2T/(L+1)\) other components contain
a chain with more than \(L\) unit edges. At most \(o(D)\) components
contain a long train. It remains to count components having at most
\(M\) chains, all of length at most \(L\), and containing no long train.

Call these components good. Along any graph edge in a good component,
the base vertices of its two chains are at distance at most
\(\epsilon_D D+2L\). Connectivity puts the bounded number of chains in
an \(o(D)\)-diameter spatial set. Section 2 then puts their normals
within \(o(1)\) of one common normal \(n\).

Summing the hull chords over a component \(\mathcal C\) gives exactly

\[
\sum_{i\in\mathcal C}r_i
=\sum_{\substack{\text{terminal occurrences in }\mathcal C\\
                  \text{train in }\mathcal A_D}} e.
\tag{TC6}
\]

Every train in \(\mathcal N_D\) incident to \(\mathcal C\) has both its
terminals there, by the definition of connected component; its two
directed unit vectors cancel. This includes loops. No terminal belonging
to \(\mathcal A_D\) is canceled without its actual opposite terminal.

All chords on the left have approximately the same positive tangent
direction \(Jn\), have lengths at least one, and have lengths at most
\(L\). For sufficiently large \(D\), their sum has norm at least
\(|\mathcal C|/2\). In particular it does not vanish.

## 5. Countable directions cannot support many good components

For completeness this step uses marked measures, rather than a finite
atom set with an uncontrolled number of direction intervals.

For each good component choose one of its hull-side normals \(n\), and
list the directed \(\mathcal A_D\) terminal vectors on the right of TC6
in boundary order. The list has some length \(r\le ML\). Pass to a
subsequence on which the finite measures of these records, weighted by
\(1/D\), converge for each \(r\). The record spaces are compact finite
products of circles.

The marginal measure of a listed terminal vector is dominated by the
measure of all directed \(\mathcal A_D\) terminals divided by \(D\).
By TC4 and a further subsequence for \(T/D\), this has an atomic limit:
each projective atom gives its two signed unit directions. Thus every
listed-vector marginal, and hence almost every entire finite vector
list, is supported on this countable signed atom set.

The chosen-normal marginal is dominated by \(\sigma_D\): different
components choose different hull sides, and each side has length at
least one. Its limit is therefore atomless by TC3.

Equation TC6 and the common tangent direction show, in the limit, that
the chosen normal is

\[
-J\,{\sum_{j=1}^r e_j\over|\sum_{j=1}^r e_j|}.
\tag{TC7}
\]

The sum is nonzero by the lower bound following TC6. There are only
countably many finite lists of signed atoms. TC7 therefore supports the
normal marginal on a countable set. An atomless measure supported on a
countable set is zero. For \(r=0\), TC6 already rules out good components
for large \(D\).

It follows that the number of good components is \(o(D)\) for each
fixed \(M,L\). The preceding counts now give

\[
\limsup {b_D\over D}
\le \limsup {q/D\over M+1}
  +\limsup {2T/D\over L+1}.
\tag{TC8}
\]

The ratios on the right are bounded. Let \(M,L\to\infty\).
Thus \(b_D=o(D)\). TC5 and \(N_D/T\to1-s\) prove TC1.

## 6. Canonical quantities changed

Set \(x=T/D\). Canonical \(R/D^2\to1/c\) and the atomic Mantel bound,
together with TC1, give

\[
x(1-y)\ge {2\over\sqrt c}=A.
\tag{TC9}
\]

Pinned rigidity gives \(y\ge1/2\). Therefore \(x\ge2A\),
\(xy\ge Ay/(1-y)\ge A\), and \(x(1-y)\ge A\).
Finally \(q\le P\le\pi D\) gives
\(Ay/(1-y)\le\pi\), or \(y\le\pi/(\pi+A)\).
These are TC2. The same argument on every convergent subsequence gives
the displayed liminf/limsup claims without a presumed unique limit.

In particular the canonical first-order-neutral lower bound
\(T-q\) improves from approximately \(0.333829D\) to
\(A D\), approximately \(1.904626D\).

## 7. Scope, regressions, and validation

The simple disk is essential as stated. A train with a terminal on an
inner boundary is not paired within the outer-chain graph automatically.
Exceptional non-rhombic outer edges also enter TC6 as uncanceled
vectors. This proof does not ignore either currency in general sources,
and it supplies no extension to contact-isolated source points.

The circular limiting hull and unit lower separation are essential.
Without the former, a straight hull side can carry positive limiting
surface measure at an atomic normal; without the latter, a linear number
of very short sides need not be dominated by the hull surface measure.
The pinned bent-grid regression lacks the circular globally minimizing
hull hypothesis. Sliding-interval models lacking physical terminal
closure do not contradict TC6.

During this run main advanced to Audit.133. In particular the canonical
Audit.131 one-ended train theorem
charges distinct trains to actual unit loaded-hull sides, retaining the
nonunit-side count in its budget. TC1 instead uses connected components
of all hull chains and cancels both physical ends inside each component.
The Target B full contact complex and the selected Target C positive
core are not identified here. The audit is a scope comparison, not a
premise of TC1. The Target B and Theory-01 input files did not change.

The exact rational script
[verify_target_b_terminal_cancellation_2026_10_08.py](../../research/verify_target_b_terminal_cancellation_2026_10_08.py)
constructs finite strict-rhombic disks, computes physical trains and hull
chains, and checks paired directions, midpoint-distance bounds, every
component cancellation identity, and TC5. It also checks all source pair
lower bounds. These are finite nonglobal fixtures. It does not certify
the marked-measure proof, circular limiting hull, global optimality,
TC1 for an arbitrary source, the shell-stability inequality, or Level I.

## 8. Promotion recommendation and remaining obligation

Audit the diagonal atomic selection, the countable marked-measure
argument, and occurrence-counted terminal pairing before promoting TC1
or TC2. No lifecycle change is made in this run.

Even if promoted, TC1 does not make the coforest blocker rank smaller
than \(T-q\), nor exclude its stressed equality kernel. The next useful
task is to use the same boundary graph
to control simultaneous backward/tangent blockers. Counting active
bars alone is insufficient, and the general topology terms remain.
