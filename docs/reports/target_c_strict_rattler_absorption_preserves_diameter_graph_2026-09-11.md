<!-- theorem-state: {"artifact_id":"ART-AB6D6B8410A2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — strict rattler absorption preserving the diameter graph

**Date:** 2026-09-11  
**Run type:** Target C C-II representative-transfer theorem  
**Status:** unpromoted research report; route-map status unchanged

## LEVEL-I STATUS

STILL OPEN.

The earlier first-contact absorption argument can be strengthened. Starting from
the C65 lexicographic representative, every contact-isolated point can be moved to
a first unit-contact event while remaining strictly below diameter \(D\) from every
other source point. Consequently the entire original diameter graph, not only one
fixed diameter pair, is preserved.

The resulting representative has no contact-isolated source points, but its newly
created contacts need not have positive KKT multipliers. Thus this theorem does
not transfer the C65 positive-core/ZF stack to the new representative.

## 1. Theorem

Let \(A\) be the C65 representative of a hypothetical triangle-free global
minimizer, with diameter \(D\), positive contact core \(C\), and rattler set
\[
R=A\setminus C.
\]

C65 gives, for every \(r\in R\),
\[
1<|r-a|<D\qquad(a\in A\setminus\{r\}).
\tag{SR.1}
\]

Then there exists a triangle-free global minimizer \(A^\circ\) with the same
cardinality and diameter such that:

1. every point of \(A^\circ\) has a unit contact;
2. every original point of \(C\) is fixed;
3. every original contact is preserved; and
4. the actual diameter graph of \(A^\circ\) is exactly the actual diameter graph
   of \(A\), on the original diameter endpoints.

## 2. Strict target inside the diameter disks

### Lemma SR.1

Let \(A\) be a two-dimensional unit-separated configuration of diameter \(D>1\).
Let \(p,c\in A\) satisfy \(|p-c|=1\), and let \(r\in A\) satisfy
\[
|r-a|<D\qquad(a\in A\setminus\{r\}).
\tag{SR.2}
\]
There is a point
\[
y\in\operatorname{int}(\operatorname{conv}A)\cap B(p,1)
\]
such that
\[
|y-a|<D\qquad(a\in A).
\tag{SR.3}
\]

### Proof

Put \(w=c-p\), so \(|w|=1\). If \(|p-a|=D\), then \(|c-a|\le D\) gives
\[
D^2\ge |c-a|^2
=|p-a|^2+2w\cdot(p-a)+|w|^2
=D^2+2w\cdot(p-a)+1.
\]
Hence
\[
w\cdot(p-a)\le-\frac12.
\tag{SR.4}
\]

For \(y_t=p+tw\) and sufficiently small \(t>0\), (SR.4) gives
\[
|y_t-a|^2
=D^2+2t\,w\cdot(p-a)+t^2<D^2
\]
for every diameter partner \(a\) of \(p\). For the finitely many \(a\) with
\(|p-a|<D\), strictness follows by continuity after decreasing \(t\). Also
\(|y_t-p|=t<1\), and \(|y_t-r|<D\) follows from (SR.2).

Choose \(z\in\operatorname{int}(\operatorname{conv}A)\). Every point of the
convex hull is at distance at most \(D\) from every source point. For sufficiently
small \(\varepsilon>0\),
\[
y=(1-\varepsilon)y_t+\varepsilon z
\]
lies in \(\operatorname{int}(\operatorname{conv}A)\cap B(p,1)\). Convexity of the
norm and the strict inequalities for \(y_t\) give
\[
|y-a|\le(1-\varepsilon)|y_t-a|+\varepsilon|z-a|<D
\]
for every \(a\in A\). \(\square\)

## 3. Strict first-contact motion

### Lemma SR.2

Under the hypotheses of Lemma SR.1, if \(r\) is contact-isolated, there is a
replacement \(r'\) such that
\[
A'=(A\setminus\{r\})\cup\{r'\}
\]
is unit-separated and triangle-free, has diameter \(D\), satisfies
\[
|r'-a|<D\qquad(a\in A\setminus\{r\}),
\tag{SR.5}
\]
and gives \(r'\) exactly one unit contact.

### Proof

Use the point \(y\) from Lemma SR.1 and the segment
\[
\gamma(t)=(1-t)r+ty,\qquad 0\le t\le1.
\]
It lies in \(\operatorname{conv}A\). Both endpoints have distance strictly less
than \(D\) from every fixed source point, so convexity of the norm gives (SR.5)
throughout the segment.

Initially \(r\) lies outside every closed unit disk centered at a fixed source
point, while \(y\in B(p,1)\). Thus the segment has a first intersection with the
finite union of those disks. Choose \(y\) outside the finite union of rays from
\(r\) through pairwise intersections of the finitely many unit-circle boundaries.
The first intersection then lies on exactly one unit circle. At that point \(r'\)
has exactly one contact and all other lower-distance inequalities are strict.

All fixed diameter pairs remain unchanged and (SR.5) creates no new diameter pair,
so the diameter remains \(D\). A new unit triangle would contain \(r'\), impossible
because its contact degree is one. \(\square\)

## 4. Global absorption while preserving \(H\)

### Theorem SR.3

Under the hypotheses of Theorem SR, there is a finite sequence
\[
A=A_0,A_1,\ldots,A_m=A^\circ
\]
of triangle-free global minimizers of diameter \(D\) such that the original core
and contacts remain fixed,
\[
H(A_j)=H(A_0)\qquad(0\le j\le m),
\tag{SR.6}
\]
and \(A^\circ\) has no contact-isolated point.

### Proof

Choose a contact edge \(pc\) in the fixed positive core. At each stage select a
currently contact-isolated point \(r\). Its strict diameter inequalities are
maintained inductively: it was isolated in the C65 source, and every previously
moved point was placed with strict distance \(<D\) from all fixed points.

Apply Lemma SR.2 with the fixed edge \(pc\). The moved point acquires one unit
contact, no diameter equality involving it is created, and every fixed diameter
relation is unchanged. No existing contact is lost because only an isolated point
is moved. The number of isolated points decreases by at least one, possibly by two
if the new contact joins two currently isolated points.

After finitely many steps no isolated point remains. The original core contains a
diameter pair, so every final configuration still has diameter exactly \(D\) and is
globally optimal. \(\square\)

## 5. Forest form of the absorbed contacts

The construction has a useful strengthening that does not require the first
contact to be made with the fixed core. At the moment a currently isolated
point is moved, it has no incident contact. The generic first-contact choice
therefore adds exactly one edge incident with that point, and that edge joins
its singleton component to an already existing component (possibly another
currently isolated singleton). Once the point has acquired this edge it is
never moved again. Consequently the edges created during the whole sequence
form a forest when contracted against the original core.

More formally, if \(C\) is contracted to one root, the quotient of the final
contact graph by the original contacts in \(C\) is a rooted forest. Every edge
outside \(C\) is a bridge, and every original rattler is either a vertex of this
forest or is absorbed as the second endpoint of the edge created by a different
rattler. The original diameter graph is still unchanged.

This is stronger than merely producing a no-isolate representative, but it is
not a positive-support statement: the forest edges can all have zero
coordinates in the original KKT stress.

### Proof

At a stage at which \(r\) is selected, \(r\) has no contact edge. Lemma SR.2
replaces it by a point with exactly one contact, and all other points are left
fixed. Thus the new edge contains the previously isolated vertex \(r\), so it
cannot close a cycle in the current contact graph. If the other endpoint was
also isolated, it becomes nonisolated at this step; neither endpoint is ever
selected again. If the other endpoint already belonged to a component, the new
edge attaches the singleton \(r\) to that component. Induction gives a forest
after contracting the original core. Since each step leaves all old contacts
untouched and creates no diameter equality, the diameter graph remains the
original \(H\). \(\square\)

## 6. What this does and does not transfer

The theorem gives a same-\(n\), same-\(D\), triangle-free representative with the
full diameter graph \(H\) unchanged and no contact-isolated points. It therefore
removes one representative-dependent feature from the source-capacity obstruction.

It does **not** imply that the newly created contacts have positive KKT multipliers.
The C65 stress remains a valid equilibrium stress on the original core, but has
zero coordinates on the new contacts. Consequently one cannot infer
\[
C=C_*,\qquad H=H_*,\qquad s_Z=e+h-(2v-2)
\]
for the new full contact graph without a separate transfer theorem.

## 7. Failed closure attempt

Applying the full-source cell-slack decomposition to \(A^\circ\) and then invoking
C-I fails at a precise point: C-I uses contact minimality to force positivity of
every active contact row. The absorbed configuration is contact-richer, so C63 may
release the newly created contacts and return to a representative with rattlers.
Preserving \(H\) does not repair this: the added contacts have zero rows in the
original stress and may be invisible to the promoted response matrix.

## 8. Regression audit

* External rattlers are handled because the strict target lies in the full source
  hull, not necessarily in the force hull.
* Shared diameter endpoints and the complete original diameter graph are retained.
* Repeated outer walks and exceptional faces do not enter the proof.
* Odd shells can be absorbed, but no global-optimality certificate for a shell
  family is produced.
* The one-dimensional force-hull phase is outside C-II.

## 9. Exact remaining obstruction

Turning SR.3 into a Level-I closure requires at least one of:

1. a theorem that a newly created contact must carry positive multiplier;
2. a source-wide packing inequality depending only on \(n,D,H\), not on the
   positive-contact representative; or
3. a monotone contact/diameter selection in which rattler absorption cannot be
   undone by C63 release.

None is currently proved. The C-II branches remain open.
