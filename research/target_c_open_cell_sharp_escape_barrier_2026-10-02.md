<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "795123f7133d153accb965203d10c95e2297a7c9", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_open_cell_sharp_escape_barrier_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "dcbbcffbfa69c6289bc8efe265e1c0e8f90c6359308f2f87217a9152c7c26581"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: sharp finite escape barriers and the exceptional pivot layer

Date: 2026-10-02. Starting checkout: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec.
Research base: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5.
State version: 2026-09-14.audit.51.
Mission: the open-cell exact-phase branch, its finite escape mechanism, and
the actual diameter edges omitted by the derivative matrix.
Branch: swarm/sol/open-cell-gap-cycles-20261002.

**Classification:** proved candidates awaiting independent audit; the actual-train
applications are conditional on the unpromoted October extraction/chart stack.
The explicit finite source is a regression, not a global minimizer.
**Level I OPEN; C-I CLOSED; C-II OPEN.** No canonical promotion is made.
No external literature is imported.

    sharp shifted-normal barrier -> a nontrivial finite exact-phase chart endpoint
    must escape a specified paired-tree row, and missing diameter rows lie at one
    of the two pivot-adjacent layers -> exclude those escapes/turnover blockers,
    or construct a strict full-source competitor -> C-II only after its other
    branches are covered -> Level I with the original every-minimizer quantifier.

The escape-exclusion implication is an obligation, not a result of this packet.

## 1. State and prior work

Canonical premises, when interpreting a normalized C-II source, are shared
Theory 4.1 (KKT), [Section 56](../docs/targets/target-c/56-ci-restored-frontier.md)
(positive actual support and lexicographic minimalities),
[Section 57](../docs/targets/target-c/57-zr-zf-rigidity-audit.md)
(the mixed rigidity and affine kernel on the nonisolated contact core),
and C-WOODALL (the full actual diameter graph). Isolates are retained in every
finite source-pair constraint. None of the new proofs extends the core kernel
to them.

Unpromoted route premises are:

- [common-star extraction](../docs/reports/target_c_fixed_star_common_witness_pairs_2026-10-01.md);
- [exact gap rank](../docs/reports/target_c_exact_phase_gap_graph_connectivity_2026-10-01.md);
- [proper boundary layers](../docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md);
- the exact finite contact chart in the October rank/shear stack: changing the
  coherently oriented train vectors from u to U_i changes an actual diameter
  vector by the signed sum of U_i-u over its support interval.

PR [#594](https://github.com/1337isnot1337/e-99/pull/594), report
target_c_exact_phase_antitone_paired_gap_tree_2026-10-01.md, already proves a
paired antitone tree and finite isolation **within** an open witness cell. Its
Sections 3--8 were inspected; those conclusions are not claimed as new here.
PR [#597](https://github.com/1337isnot1337/e-99/pull/597), checked at d8391e3c,
also already gives the common-star ray anchor, the pivot-adjacent zero-row
localization, ordered positive axial reactions and a finite exterior-train
far arc. Its far-arc equation is the shifted-normal identity used in Section 4.
Those prior results were found in the later branch inspection and are explicitly
reclassified as reconstructions here; they are not independent new frontier
claims of this packet.

Main's [threshold staircase](../docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md)
already proves the threshold counterpart and exact support incidence.

Section 2 below reconstructs the common-star geometric premise without importing
the reciprocal-force sign-arc argument. Section 3 reconstructs the prior
localization and adds the explicit full-vertex forest accounting (1). Section 4
puts the prior one-cut identity in half-angle form. The new finite consequence
is its recursive application to every coordinate in Sections 5--6, including
the doubled-cell exclusion, rather than only one exterior train or a small
Taylor radius.

For a standalone application one may take the following hypotheses explicitly:

1. A finite planar source has diameter D, with its full actual diameter graph H.
2. Proper disjoint nested crosscuts give the cyclic boundary layer order
   0, 1+, ..., (m-1)+, m, (m-1)-, ..., 1-.
3. Two full-support diameters za, zb share z in layer 0, their other endpoints
   are in layer m, and their projections against Ju have opposite strict signs.
4. All selected cut contacts have the same coherent unit vector u. The actual
   finite contact chart has interval displacements as above.
5. Positive diameter weights give zero virtual work in every selected cut,
   and the nonzero derivative matrix has rank m.
6. In the open-cell application no actual diameter is parallel to u.

The standalone geometric statements use only the applicable hypotheses, not
global optimality. The finite inequality uses only a row vector and the chart.

## 2. A common-star geometric reconstruction of the paired tree

Choose coordinates z=0, u=(1,0), Ju=(0,1). Reverse u and the layers together
if necessary. Write the two witness directions as angles -delta_- and delta_+
with delta_-, delta_+ > 0 and delta_-+delta_+ <= pi/3. This last inequality
follows from |a|=|b|=D and |a-b|<=D.

For every other source point x, diameter feasibility gives

    2 a dot x >= |x|^2,       2 b dot x >= |x|^2.

The vector u is a strictly positive combination of a and b. Thus x dot u>0.
The ray from z in direction u meets the far boundary at a unique point t.
Let L and U be the boundary arcs from z to t, below and above this ray.

Let L_0 be the arc from z to a avoiding b, M the arc from a to b avoiding z,
and U_0 the arc from b to z avoiding a. Convexity places L_0 below the line
za and U_0 above the line zb. Since x dot u>0, their points have respectively
negative and positive transverse coordinates. The point t is in M.

Every selected crosscut separates z from both a and b. Its resolved boundary
ends therefore lie one in L_0 and one in U_0. All of M has layer m. The layer
label is nondecreasing from z to t on each of L and U.

Any diameter not incident with z must have one endpoint on L_0 (including a)
and one on U_0 (including b). Indeed, to meet both witness chords za, zb it
must cross both unless sharing an endpoint. A chord with an endpoint in the
interior of M cannot cross both, and if its other endpoint is a or b it still
cannot cross the other witness. Such a diameter must therefore be incident
with z. The endpoint exceptions a and b give the same L_0--U_0 conclusion.
Here we use the actual diameter-thrackle rule, not a rule for arbitrary chords.

Consequently every transversely nonzero diameter joins the negative bank L to
the positive bank U, with z assigned the required bank role when incident.
In the open cell t is not a diameter endpoint: a diameter incident with t
would have to join z and be parallel to u. In threshold phase only the parallel
zt row can meet t; it is discarded from the transverse derivative matrix.

Orient a nonzero row from its L endpoint to its U endpoint. Its transverse
projection is positive. Its directed gap edge has those same endpoint layers.
Positive virtual work becomes positive directed circulation on the gap graph.

Two directed edges p->q and r->s with p<r and q<s have distinct same-role
endpoints, and their chords do not alternate in the convex boundary order.
They cannot share opposite-role endpoints either: the only bank intersection
usable by a transverse diameter is z in layer 0, whereas such sharing would
give q=r strictly between p and s, or p=s strictly between r and q. Therefore
actual diameter-thrackle geometry gives antitone directed support.

For completeness, positive circulation decomposes into simple directed cycles.
At every cycle vertex the two neighboring layer differences have opposite
signs: nonsharing chords must cross in opposite bank orders; the only shared
opposite-role endpoint is the strict minimum z. Thus a cycle alternates minima
and maxima. Its even and odd bars give two order-reversing bijections between
the minima and maxima. Their composition is order-preserving and hence the
identity on a finite ordered set, whereas in a longer simple cycle it would
be a nontrivial cyclic shift. Every directed simple cycle has length two.

Thus every simple gap edge occurs in both directions. Its unordered interval
support is antitone. For distinct left endpoints a_1<...<a_s, antitonicity
gives

    max B_1 >= min B_1 >= max B_2 >= ... >= max B_s >= min B_s,

where B_i is the set of right endpoints paired with a_i. Hence the number of
simple edges is at most m. Rank m makes the graph connected, so it has exactly
m edges and is a tree T. This rederives the prior paired-tree conclusion under
the stated common-star geometric hypotheses.

All intervals contain one common train index r. The minimum-span edge is
adjacent: otherwise an intervening vertex has a neighbor strictly inside that
edge's span by antitonicity, giving a smaller span. Therefore the adjacent edge
is exactly {r-1,r}; it is unique. Contract it and repeat. Each contraction
deletes one original train coordinate; later edge intervals contain only that
coordinate and coordinates already deleted. This provides the elimination
order used below. In particular r is the pivot of the **whole** row packet.

## 3. Empty-support diameters lie at a pivot-adjacent layer

**Theorem 1.** Under Section 2, every actual diameter with empty selected-shore
support has both endpoints in layer r-1 or both in layer r. At most one of those
two layers can contain such edges.

Proof. Let xy have both endpoint labels j. If a selected diameter has labels
a<b and j<a or j>b, the nested boundary blocks put the endpoints of xy and
that diameter in nonalternating cyclic order. They cannot share an endpoint,
as their layer labels differ. The diameter-thrackle rule is violated. Thus

    max_{ab in T} a <= j <= min_{ab in T} b.

Every support contains r, and the tree has {r-1,r}. The displayed interval is
therefore exactly [r-1,r]. Finally, same-layer diameters in two different layers
have distinct nonalternating endpoints by the same nested boundary order, so
they cannot coexist. This argument includes the two extreme cap layers. QED.

Let H_0 be the empty-support set and H_1=H\H_0. In an open cell all H_1 edges
project to T. In threshold phase the only omitted nonempty parallel row joins
0 to m; that edge is also in T, from the full-span witnesses and pairing.
Pull back the tree's bipartition to actual diameter vertices. H_1 is bipartite
and therefore a forest, since a convex diameter thrackle has no even cycle.

Keep **all q actual diameter vertices** when counting this forest, including
vertices made isolated by deletion of H_0. With h=|H| and d_H=q-h,

    comp(H_1) = d_H + |H_0|.                                  (1)

In the canonical cyclic case d_H=0, the odd cycle forces |H_0|>=1, so

    h >= 2m+1.

Thus the open-cell cyclic branch has the same extra-edge count as the threshold
branch, for a different reason. These are actual H counts, not component counts
of a selected forest or claims about source isolates.

The localization is sharp geometrically. Label a regular unit-side pentagon
in convex order by 0,1,2,2,1, with the layer-0 vertex z and u directed to the
middle of the opposite side. Its full diameter graph is the pentagram, has no
diameter parallel to u, and has paired gap tree {0,2},{1,2}. The remaining
diameter has both endpoints in layer 1=r-1. Reversing the layer labels puts it
in layer r. The formal gap circulation is balanced by the equal pentagon
diameter weights. The script also checks its full positive normalized KKT
equilibrium and PSD scalar stress with exactly the three affine kernel modes.
The proposed cuts are not common-direction actual contact
cutsets; this example verifies geometric sharpness and does not supply that
missing train premise or global optimality at large cardinality.

## 4. Exact shifted-normal escape for a singleton support

**Theorem 2.** Let an old diameter vector r_h have length D and signed singleton
chart support sigma in {+1,-1}. Put

    a_h = sigma r_h dot u,       c_h = sigma r_h dot Ju.

Change that unit cut vector to U(t), where

    U(t) = ((1-t^2)/(1+t^2))u + (2t/(1+t^2))Ju,

and t=tan(theta/2), -pi<theta<pi. Its squared diameter excess is exactly

    |r_h + sigma(U(t)-u)|^2 - D^2
      = 4t [c_h - (a_h-1)t]/(1+t^2).                         (2)

For t having the same sign as c_h, nonexpansion is impossible if a_h<=1.
If a_h>1 it requires

    |t| >= |c_h|/(a_h-1).                                    (3)

Proof. U-u has axial coordinate -2t^2/(1+t^2), transverse coordinate
2t/(1+t^2), and squared norm 4t^2/(1+t^2). Substitute these three values
in 2 sigma r_h dot (U-u)+|U-u|^2. The denominator is positive; the sign
and threshold conclusions follow exactly. QED.

Geometrically the threshold in (3) is the angle of sigma r_h-u, not the
angle of sigma r_h. When a_h>1, subtracting the unit contact vector increases
the absolute transverse-to-axial ratio. This is the extra finite obstruction
missed by an argument considering only derivative signs in the witness cell.

For each paired tree edge e define B_e^+ as the maximum of c_h/(a_h-1) over
its c_h>0 rows with a_h>1; set B_e^+=infinity if any positive row has a_h<=1.
Define B_e^- similarly using -c_h over negative rows. Both are strictly
positive; every tree edge has both signs. The maximum is necessary because
every actual row must be nonexpansive.

## 5. Sharp elimination certificate and the doubled cell

Choose any adjacent-gap contraction order. Associate original coordinate i_k
with tree edge e_k when that edge becomes adjacent after the previous k-1
contractions.

**Theorem 3.** A nontrivial finite chart endpoint weakly shortening every old
diameter, with all angles in (-pi,pi), has a first nonzero coordinate in this
order. If it is positive, its half-angle parameter is at least B_e^+; if
negative, its absolute half-angle parameter is at least B_e^-.

In particular the product of open intervals

    -B_{e_k}^- < t_{i_k} < B_{e_k}^+                          (4)

contains only the zero old-diameter-nonexpansive endpoint.

Proof. Earlier coordinates are exactly zero by the definition of first
nonzero. The original interval of e_k contains only those earlier coordinates
and i_k, so its actual finite displacement is a signed singleton displacement.
Theorem 2 applies to every row of the sign matching t_{i_k}. It gives the
maximum threshold B_e. This is a finite identity, not an integration of a
first-order feasible direction. The product conclusion follows immediately.
Untouched or empty-support diameters cause no omitted displacement. QED.

**Corollary 4 (doubled open cell).** Let the closest global actual diameter
directions bounding the open witness cell be -delta_- and delta_+ relative to
u, with the common-star orientation of Section 2. Then every finite chart
endpoint satisfying

    -2delta_- <= theta_i <= 2delta_+    for all i              (5)

and weakly shortening every old diameter is trivial. This excludes moves
crossing the original witness threshold but staying in its doubled window.

Proof. Take a positive row c_h>0. If a_h<=1, it blocks every positive
half-angle. Otherwise its coherently signed actual vector has positive axial
and transverse components, so its angle phi_h is at least delta_+ by the
absence of actual diameter directions in the open cell. Hence

    c_h/(a_h-1) > c_h/a_h = tan(phi_h) >= tan(delta_+).

For negative rows the same argument gives B_e^->tan(delta_-). The star wedge
has delta_-+delta_+<=pi/3, so all angles in (5) lie strictly between -pi and
pi and tangent half-angles are monotone. Their closed box lies strictly inside
(4). Apply Theorem 3. QED.

There is no uniform positive distance of u from a witness threshold claimed
here. In particular (5) is not a uniform O(1/D) feasibility theorem.

## 6. Attempted closure using the complete opposite shore

Hold the opposite shore fixed. For a crossing rhombus let its original angle
from u to the opposite unit vector be psi_j in (pi/3,2pi/3). In the same
oriented rhombus branch, unit separation of both diagonals requires

    psi_j - 2pi/3 <= theta_i <= psi_j - pi/3.

Because the rectangle is complete, every selected i obeys the common interval

    L := max_j psi_j-2pi/3 <= theta_i <=
    U := min_j psi_j-pi/3.                                   (6)

The interval contains zero and lies inside (-pi/3,pi/3). This is a necessary
condition, not sufficient feasibility for the complete source.

**Conditional finite exclusion.** If a contraction order has

    B_{e_k}^+ > tan(U/2),    B_{e_k}^- > -tan(L/2)             (7)

for every k, then no nontrivial fixed-opposite-shore chart endpoint in this
rhombus branch can weakly shorten every old diameter. This follows by applying
(4) to (6), including their boundary points. Equality in (7) is deliberately
not included: at an exact barrier an old diameter can remain equal.

Condition (7) is not supplied by the canonical state. The exact regression
below tests and rejects the attempted repair that local rhombus feasibility
alone always prevents a sharp-barrier escape. Thus this attack was performed
and falsified, rather than left as an untested closing proposal.

## 7. An actual O--O unit-rhombus cut escapes beyond the barrier

All coordinates are rational. Put

    D=20, u=(1,0), v=(8/17,15/17),
    z=(0,0), p=v, q=u, s=u+v,
    a=(240/13,100/13), b=(240/13,-100/13).

This six-point source is unit-separated. Its exact contact graph is the unit
rhombus z-q-s-p-z; a,b are contact isolates. Its actual diameter set is exactly
{za,zb}, both of length 20. The line parallel to v through u/2 resolves the
non-singleton O--O dual train through the rhombus and separates {z,p} from
{q,s,a,b}. Both old diameter rows have full singleton support and opposite
coefficients c=+/-100/13; the gap graph is a paired tree. Equal positive
formal diameter weights satisfy its transverse virtual-work identity.

Move all right-shore points by

    Delta = (-2/5,-4/5),       U = u+Delta=(3/5,-4/5).

Every old unit contact remains exactly unit. The new rhombus is still strictly
triangle-free: U dot v=-36/85 is strictly between -1/2 and 1/2. Every other
pair remains strictly above 1, and every upper distance is strictly below 20.
The old negative-row barrier is

    |c|/(a_h-1) = 100/227.

The move has t=-1/2, beyond that sharp barrier and beyond the original doubled
cell, since tan(delta_-)=5/12<1/2. The new squared diameter is exactly

    400 - 108/65 = 25892/65 < 400.

The script checks all 15 old and all 15 new source pairs, not just the two
old diameters or the local diagonals. The source lacks full vertex KKT
equilibrium: the diametral vertices a,b are contact-isolated. It is plainly
not a global minimizer. Thus it is **not** a regression against canonical
C-II, positive full-source equilibrium, or Level I; it defeats only a closure
using the paired gap tree, actual contact chart, and local rhombus constraints
without the additional source equilibrium/global information.

## 8. Computation, classification and exact remaining attack

Run python3 research/verify_open_cell_sharp_escape_2026_10_02.py.
It uses Fraction arithmetic (including an exact quadratic-field representation
for the pentagon) to check the singleton polynomial identity, sharp
threshold and negative controls; enumerate paired antitone trees and complete
adjacent elimination; check the pivot-adjacent empty-support localization in
proper cyclic layer orders; and verify every pair of the six-point finite
source above. The analytic proofs in Sections 2--6 establish the general
statements. Finite enumeration is regression evidence, not global optimality.
The script omits extraction of actual trains in a normalized global minimizer,
the opposite-shore full KKT system, full vertex KKT for the six-point moving
source, and any global-optimality certificate for either source.

| Claim | Classification | Limit |
| --- | --- | --- |
| Common-star paired tree | Reconstruction of prior unpromoted candidate | Actual route depends on extraction/chart |
| Pivot-adjacent empty-support layer | Reconstruction of PR #597 | Preserves omitted actual H rows |
| Full-vertex forest accounting (1) | Checked consequence | Include vertices isolated by deleting H_0 |
| Singleton shifted-normal identity | Prior PR #597 identity in half-angle form | Contact-preserving chart only |
| All-coordinate first-escape elimination | Proved candidate awaiting audit | Paired tree and actual finite chart |
| Doubled-cell finite isolation | Proved candidate awaiting audit | No uniform threshold-distance floor |
| Whole rhombus box exclusion under (7) | Conditional | (7) is not canonical |
| Rhombus feasibility universally blocks escape | Rejected by exact regression | Regression omits full KKT/global optimality |

The next concrete source obligation is to rule out the **first escaping paired
edge** of Theorem 3 using actual full vertex equilibrium and all newly active
source pairs, or to make that escape feasible with a strict full-source diameter
improvement. The source-wide escape threshold, rather than merely crossing an
original direction, is now explicit. In the cyclic case the old empty-support
diameters that cannot be dropped are confined to one pivot-adjacent layer.

Allowing the opposite shore to change adds its finite displacement to each
diameter row; the singleton identity (2) then requires that extra term and is
not applied silently. Opening old contacts likewise leaves this chart. Those
two mechanisms remain legitimate alternatives. The nonconstant phase,
split-star O--O, inactive-interface, higher-surplus full-core and macroscopic
inactive-container/exterior-cap branches remain open.

Promotion recommendation: preserve as an unreviewed research packet and seek
an independent audit. No state-version, canonical theorem, or prompt changes.
