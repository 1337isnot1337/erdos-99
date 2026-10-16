<!-- theorem-state: {"artifact_id":"ART-5A6933F8BE17","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: convex geodesic rhombus limits are parallelograms

**Date:** 2026-09-30<br>
**Base main:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**State version:** `2026-09-14.audit.51`<br>
**Classification:** proved candidate awaiting promotion; noncanonical.<br>
**Level I:** open. C-II remains open.

## 1. Statement

Consider actual induced harmonic contact graphs in convex attachment polygons
\(P_D\), with full bounded strict-unit-rhombus complexes. Assume
\[
L_D=O(D),\qquad Z_D:=L_D-\operatorname{per}P_D=o(D),\qquad Q_D=o(D),
\tag{1.1}
\]
and \(D^{-1}P_D\to K\) in Hausdorff distance, with \(K\) of positive area.
Assume the canonical stopped-train properties: monotone simple midpoint
trains, unique train per boundary edge direction, intersections only at
crossing rhombi, and a triangle-free train-crossing graph.

Then \(K\) is a centrally symmetric parallelogram.

If additionally the carrier has \(\Omega(D^2)\) rhombi, their total acute
angle defect is \(O(D)\), and \(K=\operatorname{conv}S\) for compact
\(S\subset\partial B(0,1/2)\), no such sequence exists. A cyclic
parallelogram is a rectangle, whereas canonical inverse-phase extraction
forces two positive-length face directions at projective angle \(\pi/3\).

Thus **every** positive-area circle-supported Type-II harmonic carrier pays
a linear amount of \(Z_D+Q_D\), including diameter-one wrapping carriers.
This is a boundary-defect theorem, not a strict-competitor theorem.

## 2. Central symmetry and closeness of the physical outer walk

The finite estimate in
`target_c_train_boundary_symmetry_defect_2026-09-30.md` gives central
symmetry of \(K\), with a self-contained support-function proof.

Every attachment route has chord length \(s\le D\) and length
\(s+z\), with \(0\le z\le Z_D\). It lies in the ellipse of points
whose total distance to its two endpoints is at most \(s+z\). Thus its
distance from its chord segment is at most
\[
O\!\left(\sqrt{DZ_D}+Z_D\right)=o(D).
\tag{2.1}
\]
This bound is uniform over **all** routes. Every old outer terminal midpoint
is consequently within \(o(D)\) of its assigned polygon side. No convergence
rate is postulated: (2.1) supplies exactly the rate needed for the extensions
below.

## 3. Bridges cannot supply positive limiting boundary length

Fix a small angle \(\eta>0\). Formula (2.3) of the symmetry-defect report
shows that only \(Z_D/(1-\cos\eta)=o(D)\) outer unit occurrences are
misaligned by at least \(\eta\) with their assigned oriented polygon side.

A bridge has two occurrences with opposite vectors at the same physical
midpoint. If both were aligned, (2.1) would place this same midpoint within
\(o(D)\) of support lines with nearly opposite normals. Since \(K\) has
positive minimum width, choose \(\eta\) so small that these support strips
are disjoint after normalization. Uniform support convergence then makes
simultaneous alignment impossible for sufficiently large \(D\).

Each bridge therefore has a misaligned occurrence, so there are only
\(o(D)\) bridge occurrences. Nonbridge outer occurrences not facing a
rhombus are at most \(5Q_D=o(D)\). Trains having a non-outer end also number
at most \(5Q_D=o(D)\).

It follows that the normalized direction measure of trains with **two original
outer ends** converges to the tangent boundary-length measure of \(K\).
The ends of each such train are opposite oriented directions, as in the
symmetry-defect proof. There is no stopping at a phase cut or a new boundary.

## 4. Three positive direction families are impossible

Suppose the tangent boundary-length measure of \(K\), modulo \(\pi\),
has at least three support directions. Choose three small disjoint closed
direction intervals \(J_1,J_2,J_3\) with positive mass and separated
endpoints. Choose their endpoints off the atoms of the measure. Central
symmetry gives positive mass also on \(J_i+\pi\).

By Section 3, for some fixed \(c>0\), each interval supplies at least
\(cD\) original trains with two outer ends. Discard the \(o(D)\) trains
having a terminal occurrence misaligned with its host side. Enlarge the
intervals by a fixed sufficiently small angle so all six host-side chains
remain disjoint and occur in order
\[
J_1,J_2,J_3,J_1+\pi,J_2+\pi,J_3+\pi.
\tag{4.1}
\]

### 4.1 Remove end clusters at the six chain junctions

Trim a fixed normalized length \(\varepsilon\) from the ends of each of
the six convex side chains, by discarding a terminal when its closest point
on its host side belongs to a trimmed end. This removes at most
\(C\varepsilon D+o(D)\) selected terminal occurrences. The following
clipped-projection estimate proves this count without a per-route loss.

Let \(u\) be the middle tangent of one chain, whose side directions are
within \(w<\pi/2\) of \(u\). After the fixed-angle alignment deletion,
every selected terminal edge has \(u\)-projection at least
\(c_0=\cos(w+\eta)>0\). An edge having negative \(u\)-projection has
host-side angular cost at least \(1-\sin w\). The total backward
\(u\)-projection of all the chain's routes is consequently at most
\[
B\le Z_D/(1-\sin w)=o(D).
\tag{4.2}
\]
For any projected interval \([a,b]\), clip the scalar position to
\([a-1,b+1]\). A selected unit edge whose midpoint projects into
\([a,b]\) has both endpoints in this enlarged interval and contributes
at least \(c_0\) to the positive clipped variation. Route endpoints are
the consecutive polygon vertices, with nondecreasing \(u\)-projection.
Their clipped endpoint differences therefore telescope over the entire
chain to at most \(b-a+2\). Negative clipped variation is at most \(B\).
Thus the number \(N([a,b])\) of selected occurrences satisfies
\[
c_0N([a,b])\le b-a+2+B.
\tag{4.3}
\]
This uses occurrence multiplicity and holds even with repeated vertices,
bridges, and many short routes.

The projection of a trimmed polygon end has length at most
\(\varepsilon D\). By (2.1), a terminal midpoint assigned there projects
into its \(o(D)\) enlargement. Apply (4.3) to each of the two trimmed
ends of each chain. This gives the claimed
\(O(\varepsilon D)+o(D)\) loss.

Take \(\varepsilon\) small compared with \(c\). Each family still has
\(\Omega(D)\) trains. After this trim, their six normalized boundary
regions are compact and pairwise disjoint. Their separation is fixed and
positive. This includes the case of adjacent straight faces meeting at a
corner; the trim removes the common corner.

### 4.2 Extend to the convex hull and count every new intersection

Join each surviving original terminal midpoint to a closest point of its
assigned polygon side by a straight segment. The segment lies in \(P_D\)
and has length \(o(D)\), uniformly by (2.1). Distinct trimmed terminal
regions remain a fixed positive normalized distance apart. Hence extensions
belonging to distinct regions do not intersect for large \(D\).

A straight extension of length \(\ell\) intersects only \(O(\ell+1)\)
rhombi. Indeed, every such rhombus has diameter at most two, so it lies in
the radius-two tube around the extension. Its area is at least
\(a_0=\sqrt3/2\), and rhombus interiors are disjoint. The tube has area
\(4\ell+4\pi\), giving the explicit bound
\[
\#\{\text{intersected rhombi}\}\le(4\ell+4\pi)/a_0.
\tag{4.4}
\]
Each rhombus contains at most two original train midpoint arcs. Thus each
extension meets only \(o(D)\) original trains. Degenerate intersections
can be resolved by an arbitrarily small perturbation inside the same tube;
the bound counts all rhombi touched, not only transverse crossings.

There are \(O(D)\) surviving trains and therefore \(O(D)\) extensions.
The total number of train pairs whose intersection could be supplied only
by an extension is \(o(D^2)\).

### 4.3 Alternation now gives an actual crossing triangle

For trains in distinct families, their extended paths join alternating
points of the simple convex boundary, by (4.1). The paths lie in \(P_D\),
so they intersect. If their original train midpoint arcs do not intersect,
the intersection must involve an extension, and such pairs total
\(o(D^2)\) by Section 4.2.

Thus all but \(o(D^2)\) pairs between any two of the three linear families
cross in an **original** rhombus. There are \(\Omega(D^3)\) triples with
one member from each family. A missing crossing pair can spoil only
\(O(D)\) triples, so the \(o(D^2)\) missing pairs spoil only
\(o(D^3)\) triples. A pairwise-crossing triple remains, contradicting the
triangle-free train-crossing graph.

This repairs the near-boundary alternation issue explicitly: crossings created
by extending to the hull are paid using the uniform \(o(D)\) extension
length and the exact tube bound. Near-boundary endpoints alone are not used
as a finite crossing theorem.

## 5. Finish the classification and the circle-supported exclusion

The tangent measure of \(K\) has at most two projective support directions.
Positive area requires two. Central symmetry pairs the corresponding
opposite side lengths. A convex body whose boundary-length measure is
supported on those four directions is a parallelogram: its boundary consists
of the four support segments, with no other positive boundary length.

If its extreme points lie on one circle, it is a cyclic parallelogram and
therefore a rectangle. Opposite angles of a cyclic quadrilateral sum to
\(\pi\), while those of a parallelogram are equal; all four angles are
\(\pi/2\).

Under quadratic rhombus population, linear train count, and boundary-order
phase defect, canonical Section 90 and the already proved four-face theorem
force two distinct positive-length face directions of \(K\) at projective
angle \(\pi/3\). A rectangle's two directions have angle \(\pi/2\), a
contradiction. This proves the exclusion for all positive-area
circle-supported limits, without a diameter endpoint restriction.

## 6. Uniform consequence and remaining theorem

Fix a positive carrier-area floor and the canonical uniform perimeter,
train-count, and phase-defect constants. Compactness and the exclusion above
give constants \(\epsilon>0,D_0\) such that every sufficiently large actual
carrier in that class satisfies
\[
\boxed{Z_D+Q_D\ge\epsilon D.}
\tag{6.1}
\]
Otherwise choose carriers with \((Z_D+Q_D)/D\to0\), take a convex
Hausdorff limit of positive area, and apply the theorem. This is an
existential uniform gap for the stated fixed class; neither its value nor
its threshold is claimed effective.

The rooted ledger allows positive linear \(Z,Q\), so (6.1) does not close
the entire full-core branch. The exact new source-level obligation is a
**boundary-defect release theorem**: show that an actual canonical full-core
global minimizer with such a carrier and \(Z+Q\ge\epsilon D\) admits an
\(n\)-point unit-separated competitor of diameter strictly below \(D\).
The entire original population, including isolates, and every diameter
constraint must be included in that replacement.

The inactive-container branch has a separate replacement obligation. No
claim in this report alters or deletes its diameter-carrying core.

## 7. Hostile audit and dependencies

The new ingredients are the uniform ellipse bound, bridge removal by
positive width, occurrence-counted trimming, and the finite tube count for
new crossings. Canonical Sections 61/89 supply the train decomposition and
triangle-free crossing graph; Section 82 supplies induced harmonic contact
graphs and bounded stopping-face capacity. Section 90 is used only for the
final angle contradiction. The earlier symmetry-defect and four-face reports
are proved candidates from this run, not promoted canonical modules.

The proof keeps \(\varepsilon\) and direction cones fixed before taking
\(D\to\infty\). It pays every artificial intersection before invoking
finite triangle-freeness. Vanishing-area limits are excluded. It uses no
Euler trail, stress-weight floor, source-point deletion, or numerical
certificate.

**Promotion disposition:** proved candidate awaiting an independent audit of
the boundary trimming and extension argument; no canonical state changes.
