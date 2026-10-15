<!-- theorem-state: {"artifact_id":"ART-24DBD0FF7980","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: one corner and one vacant target site give a strict packet

Date: 2026-10-06. Authority: `147158251175c6bcb76690a3cb7a7f3d9091050e`,
state `2026-10-06.audit.69`. Classification: **proved candidate awaiting
independent audit**. No promotion, general chamber classification,
complete container closure or Level I result is claimed.

The implication is

`specified three-direction curved unit wall + interior count at least
two below the rounded maximum -> one corner deletion and an explicit
nonaffine strict packet -> full-source contact-loss contradiction`.

The omitted center is a site of the replacement chart. No old source
point is silently discarded: every deleted source label is assigned a
distinct new point, and the full source cardinality is preserved.

## 1. Wall and limiting replacement chart

Fix `M>=3` and let `F_theta` be the six-sided convex unit wall with `M`
unit vectors on each side, successive vector angles
`(2j-M+1)theta` relative to that side's triangular direction. Its six
corner positions are `L(theta)e_k`, with `e_k=Rot(k pi/3)u` and
`L=sum_j cos((2j-M+1)theta)`. For small positive angle the wall is
strictly convex, unit-separated and triangle-free.

Put `R=M-1` and use the limiting triangular interior grid

\[
P_R=\{iu+jv:\ |i|,|j|,|i+j|\le R\},
\quad u=(1,0),\quad v=(1/2,\sqrt3/2).
\]

Delete its central site from the **target chart**, leaving

\[
\boxed{|P_R\setminus\{0\}|=3M^2-3M=:N-1,
\qquad N=3M^2-3M+1.}\tag{1}
\]

Delete the old wall corner in direction `e_0` in the eventual source
exchange. At zero, five retained wall corners supply unit guard pairs
to the corresponding five inner corner sites `R e_k`. Every other
wall-to-chart unit pair involves a noncorner wall vertex.

## 2. No positive equilibrium survives the missing corner and center

Consider the finite homogeneous row system consisting of all unit pairs
of `P_R\setminus{0}` and the five unit guard pairs to the stationary
retained outer corners. A nonnegative dependence among those gradient
rows is a nonnegative contact equilibrium at every moving chart site.
There are no other pinned rows in this homogeneous system.

We prove that such a dependence is zero. On the radius-`R` hexagon,
every noncorner boundary site's edges to interior sites point strictly
into one half-plane. Its two boundary edges are tangent. Projecting
equilibrium on the outward normal forces all the interior edge weights
at this site to zero, and its two boundary weights are equal. Thus each
side has a constant weight.

At a boundary corner, the difference of its two ring weights is its
tangential force component: radial chain and retained corner-guard rows
are radial. They must therefore be equal. All six sides have a common
weight. At the corner in direction `e_0` there is no outer guard. All
its remaining gradients have positive outward radial projection. Its
ring and inner radial weights must vanish. Thus the common ring weight
is zero, and the outgoing radial weight on this ray is zero.

Peel that radius layer. Edges at its noncorner sites already have zero
weight. Only radial corner chains can transmit a guard weight to the
next layer. The same half-plane and tangential argument makes that
layer's ring weights equal. On the missing-guard ray its outward chain
weight is zero, so its ring and inward chain weights again vanish.
Continue through every layer. At radius one the central site is absent,
so there is no inward chain. Its zero ring weights force the weights
on **all** six outward radial chains to zero. Propagating outward sets
all five guard weights to zero. Every gradient row now has zero weight.

This argument covers `R=2` directly; it neither treats weak diagonal
pairs as bars nor assumes an affine velocity field. The peeling applies
to the complete actual unit-neighbor graph of the limiting chart.

## 3. A strictly opening direction exists

Let `a_l` be the homogeneous gradient row vectors in the full moving-site
coordinate space. Section 2 says zero is not in their convex hull. Take
the closest point `d` of that compact convex hull to zero. The projection
inequality gives

\[
a_l\cdot d\ge|d|^2>0\qquad\text{for every }l.
\tag{2}
\]

Thus every chart unit pair and every retained corner guard strictly
opens to first order. A sufficiently close rational approximation in
triangular axial velocity coordinates preserves all these finite strict
inequalities.

At noncorner wall vertex `i` on side direction `w`, the old wall
velocity is `-i(M-i)Jw`. Each limiting unit pair to an interior chart
point has positive half-squared-length derivative against this wall
alone equal to `sqrt3 i(M-i)/2`. Scale the direction from (2) by a
sufficiently small positive constant. All these noncorner guard
derivatives then remain positive, while every homogeneous derivative
stays strictly positive. This supplies one fixed velocity field `d_i`
such that

\[
p_i(\theta)=p_i+\theta d_i
\tag{3}
\]

strictly separates every formerly unit chart pair and every formerly
unit retained wall guard for small positive `theta`. Every other lower
pair has a strict limiting margin. All chart sites are strictly inside
the limiting wall, so their interior containment persists as well.

Consequently (3) is a strict packet of `N-1` sites inside `F_theta`,
clearing every original wall vertex except the deleted corner. This is
an existence proof for every fixed `M` and sufficiently small positive
angle. It gives no uniform curvature threshold across `M`. For exact
rational parameter arithmetic, use `t=tan(theta/2)` and replace (3) by
`p_i+2t d_i`; this has the same first derivative and the finite endpoint
is directly checkable.

## 4. Full-source exchange and the exact remaining population cases

Suppose an actual triangle-free normalized global source contains this
complete wall and `z` source points strictly inside it. Their positions
and mutual contacts are arbitrary. If

\[
\boxed{z\le N-2,}\tag{4}
\]

delete those `z` interior labels and the one wall corner. Assign them
to exactly `z+1<=N-1` of the strict packet sites.

The canonical one-deleted-vertex exterior shield checks every retained
exterior source point, including contact isolates. Every packet point
is inside the full old source hull, so all its upper pairs are strictly
below `D`; retained old-old pairs are unchanged. No new unit contact
is created, and at least the two old corner wall contacts disappear.
The source remains triangle-free and cardinality is unchanged. Global
minimality or contact-minimality is contradicted.

If also

\[
\operatorname{area}(F_\theta)<a_*(3M^2+1),
\quad a_*=\sqrt3/2,
\tag{5}
\]

finite Oler applied to all wall and interior points gives
`6M+z<3M^2+3M+2`, hence `z<=N`. The area tends to `3a_* M^2`, so (5)
holds at sufficiently small positive angle. Composing the exact packet
with this **upper** population bound leaves only

\[
\boxed{z\in\{N-1,N\}}\tag{6}
\]

for any canonical completion in this wall class. Thus a population
deficit of at least two has been spent as an actual source exchange.
The two maximum-count cases are not excluded here. The packet is
constructed separately from the area bound; no area-only capacity
argument is used.

## 5. Binding scope and next attack

The previous smooth affine corner barrier used the full `N`-site grid
and all six corner guards. The new chart removes a target site and an
actual source corner guard, destroys the positive equilibrium stresses,
and uses independent nonaffine velocities. Those are explicit changed
hypotheses. The old barrier and the nested-stress necessary inequalities
for the full chart remain valid.

The finite heptagon global regression is outside this wall geometry.
There is only one deleted wall guard, so the two-deletion exterior
regression is not bypassed. Every interior and exterior source label is
counted. A canonical chamber is not proved to have this chart or this
curvature onset.

Immediately attack `z=N-1` and `z=N`: either construct a larger strict
or exact-contact packet paying the full contact ledger, prove that such
triangle-free clouds cannot occupy this actual wall, or move enough
actual diameter endpoints to obtain a strict global improvement. A
local packet argument must not turn its limiting triangular grid into
an asserted old source. The general macroscopic-container and full-core
branches also remain open.

## 6. Exact finite certificates

Rational axial velocities for `M=3,4,6` are stored in
`research/target_c_one_corner_vacancy_velocity_certificate_2026_10_06.json`.
They were discovered with floating linear programs; no solver result is
accepted without exact reconstruction.

`research/verify_target_c_one_corner_vacancy_packet_2026_10_06.py` checks
every limiting unit-pair first variation exactly, constructs positive
rational-angle walls and the full nonaffine packets in `Q(sqrt3)`, and
checks strict containment, every new lower pair, every retained wall
guard and every new upper pair against the actual wall-source diameter.
It also checks a complete same-cardinality wall-plus-center endpoint,
contact loss and all integer old-population choices allowed by (4).
This certifies finite packets. The no-stress peeling, strict separation
argument, universal exterior shield and arbitrary-M onset are analytic.
