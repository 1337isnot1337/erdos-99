<!-- theorem-state: {"artifact_id":"ART-71FCD49E88D1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: uneven convex bending and exact wall packets

Date: 2026-10-06. Authority: `35f5843ab9f5d11327d0f4cc803ed00707806ae7`,
state `2026-10-06.audit.65`. Classification: **proved candidate awaiting
independent audit** for the packet and endpoint; **regression** for the
corner proposal. No result is promoted. C-II and Level I remain open.

The implication is

`two near-triangular wall direction families with arbitrary small convex
bending -> strict explicit packet -> exact old-population bound ->
full-source contact-loss exchange`.

This extends the uniform-curvature wall theorem. The two opposite side
pairs may have independent bending profiles. It does not classify every
canonical chamber or substitute reciprocal coordinates for source sites.

## 1. Bending profiles and closed actual unit walls

Fix `M>=8` and `u dot v=c in (0,1/2)`. For each of the two side families
choose a strictly increasing real sequence

\[
a_0<a_1<\cdots<a_{M-1},\qquad a_j=-a_{M-1-j}.\tag{1}
\]

The symbol `a_j` denotes an angular-rate profile; write `a_* = sqrt3/2`
for the triangular-lattice area constant. The four side bases are
`u,v,-u,-v`. On each side use the vectors `Rot(a_j theta)w`, with
the first profile on `u,-u` and the second on `v,-v`.

Antisymmetry makes each transverse sum zero, so the side chords are
`L_u u,L_v v,-L_u u,-L_v v`. The polygon closes. For sufficiently small
positive `theta`, all its direction gaps are positive and less than
`pi`, and it is a strictly convex actual unit wall `F_theta` with `4M`
vertices. At zero it limits to the `M` by `M` oblique parallelogram.
All nonconsecutive wall pairs have strict limiting separation because
`c<1/2`; that remains true at sufficiently small positive angle.

## 2. Local turn is dominated by the outward bow

For one profile define

\[
B_i=-\sum_{j=0}^{i-1}a_j,
\qquad d_i=a_i-a_{i-1}>0,
\quad 1\le i\le M-1,
\qquad B_0=B_M=0.
\]

At side vertex `i`, the old position has derivative `-B_i Jw`.
The bow sequence satisfies the exact discrete boundary equation

\[
2B_i-B_{i-1}-B_{i+1}=d_i.
\]

Its Green function is

\[
G_{ij}=\frac{\min(i,j)(M-\max(i,j))}{M},\qquad
B_i=\sum_{j=1}^{M-1}G_{ij}d_j.
\tag{2}
\]

Consequently

\[
B_i\ge\frac{i(M-i)}M d_i.
\]

For `3<=i<=M-3` and `M>=8`,

\[
\boxed{B_i>\frac32 d_i.}\tag{3}
\]

The strict margin is independent of how unevenly the curvature is
distributed: `i(M-i)/M>=3-9/M>3/2`. No return path, route length,
terminal occurrence or defect count is charged in this estimate.

On each side select the vertices
`i in {3,6,9,...} cap [3,M-3]`. Their total number is

\[
|\mathcal B|=4\lfloor(M-3)/3\rfloor.
\]

Their two incident directions have angular gap `d_i theta`. Let `n_i`
be the inward bisector normal and set

\[
h_i=3\sin(d_i\theta/2),\qquad x_i=q_i+h_i n_i.
\]

Each old neighboring contact opens exactly to
`1+3sin(d_i theta/2)^2` in squared length. The root derivative is

\[
x_i'(0)=(-B_i+\tfrac32d_i)Jw.
\tag{4}
\]

It therefore remains outward of the limiting straight side to first
order while moving inward relative to its own old wall vertex. This
provides the clearance missing from a turn count alone.

## 3. Strict interior packet

Let `mu` be the minimum, over both profiles, of all the positive numbers
`B_i` and all selected `B_i-3d_i/2`. Choose

\[
\lambda=\frac{\min(1,\mu)}{100M}>0,
\quad \ell=1+2\lambda\tan(\theta/2),
\quad o=\tfrac12(L_u u+L_v v).
\]

Use the `(M-1)^2` sites

\[
z_{ij}=o+\ell[(i-M/2)u+(j-M/2)v],
\qquad 1\le i,j\le M-1.\tag{5}
\]

Their mutual distances are all strict: basis differences have length
`ell>1`, and every nonbasis limiting grid difference is longer than one
because `c<1/2`. The sites are strictly inside the limiting wall, so
interior containment persists.

The side chord and center have zero derivative at zero, by (1).
Every limiting unit wall-to-site distance is a first-row basis pair.
Its half-squared-length derivative is

\[
B_i\sqrt{1-c^2}
 +\lambda\{c(i-M/2)+(1-M/2)\},\tag{6}
\]

up to the side's rotation and sign changes. The second term has absolute
value at most `3M lambda/4`, and the first is at least
`mu sqrt3/2`. Hence it is positive. For a selected root-to-first-row
pair, replace `B_i` by `B_i-3d_i/2`. The same positive estimate follows
from (3). All other wall/site and root/site pairs have strict limiting
lower margins.

Each root is inside the actual wall: its bisector step points strictly
inward through both incident supports and, for small angle, through
every same-side support; the other three side supports have positive
limiting slack. All nonneighbor wall/root pairs remain strict by their
limiting margins. The selected old vertices and roots have pairwise
distance greater than two: same-side separation is at least three
steps, adjacent-side roots are at least three steps from the corner,
and opposite-side separation limits to at least `M sqrt(1-c^2)>2`.

Thus (5) plus all selected roots is an explicit strict packet after
those wall vertices are deleted. Every statement holds for each fixed
`M,c` and pair of profiles at sufficiently small positive angle. The
proof does not give a source-independent angle or robustness radius.

## 4. Exact cardinality and full-source endpoint

If additionally

\[
\operatorname{area}(F_\theta)<a_*(M^2+1),\tag{7}
\]

Oler and the integer count give `z<=(M-1)^2` for the entire actual old
interior population, with no assumption on its positions or contacts.
Assign its labels to distinct sites (5), and replace every selected
wall label by its root. This changes no source cardinality.

The complete-wall shield protects every inserted interior site against
every retained exterior point. The individually verified one-deleted-
vertex convex-wall shield protects each root. Every new-new and
new-wall distance is strict by Section 3. All inserted points are in
the old full-source hull interior, so every upper pair involving one
is strictly below `D`; all retained old-old pairs are unchanged.

No contact is created, and at least `2|mathcal B|` distinct old wall
contacts disappear. The new contact graph remains triangle-free.
Global minimality or contact-minimality is contradicted exactly as in
the preceding exact-capacity theorem. In particular every canonical
completion containing such a wall is excluded, regardless of its
interior collar.

For every fixed profile pair and `M`, (7) holds at zero when `c<1/2`
is sufficiently close to `1/2`. Continuity and the positive packet
interval give a nonempty intersection at positive curvature. Thus this
is an infinite family of excluded chamber geometries, with arbitrary
fixed uneven bending profiles and area of order `M^2`.

## 5. Regression scope and remaining inference

The Green-function condition is essential to this packet proof. A root
chosen very close to a side corner can have `B_i<=3d_i/2`; its first-row
clearance would then be negative. This kills a rule selecting every
wall vertex from its turn alone. Restricting the bank to indices in
`[3,M-3]` supplies the strict margin without any assumption of uniform
curvature.

The exact eight-step profile `(-101,-5,-3,-1,1,3,5,101)` gives
`B_1=101`, `d_1=96` and `B_1-3d_1/2=-43`. Its corner-adjacent root
has distance below one from the first interior site, although that old
site is strictly separated from the old wall vertex. The verified middle
bank on the same wall still passes. This is a source-pair regression
against that extra corner proposal, not global optimality or a failure
of the strengthened middle-bank packet.

A general canonical face need not have two dominant side direction
families, repeated opposite profiles, this rounded area bound or this
source coordinate chart. A leading-area saturation theorem does not
supply these hypotheses. Three-direction walls and generic convex
chambers need their own certified packets or a separate geometric
contradiction. Full-core coupled train closure remains open. No
exhaustive C-II branch is declared eliminated here.

## 6. Exact verifier

`research/verify_target_c_uneven_wall_exact_packet_2026_10_06.py` checks
rational profile packets, including curvature concentrated at one middle
vertex and independent opposite-side profile pairs. It verifies (2) for
every side index, the selected strict margin, all old/new source pairs,
unit wall edges, strict convexity and containment, exact root contact
opening, the shoelace area bound, and every moved-involving upper pair.
The analytic shields, Oler and arbitrary sufficiently-small-angle
existence are not established by sampling these packets.
The four packets check 27,936 old and 27,936 new pairs, 68 exact Green
identities and 304 integer old-population cases; the corner lower failure
is also exact.
