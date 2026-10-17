> Generated reading edition · [exact source](../../../../docs/targets/target-c/01-force-hull-and-shear.md) · source SHA-256 `19a6693901b4aabc881a52365430014be76fea3b7021bd1e0b6479fd58787841`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — canonical force-hull and shear frontier

This module is the authoritative compact state for Target C. Full proofs are in the
audited addenda linked by `README.md`; the statements below record only the promoted
results needed to continue the route.

**LEVEL I STATUS: STILL OPEN.**

**Controlling update (2026-09-09):**
[C-I restoration](56-ci-restored-frontier.md) supersedes this module's older
claims that universal selected-stress PSD and Gate C-I are open. The exact
C53/C63 dependency audit closes C-I and supplies a representative with full actual
contact and diameter support. C-II remains open. Hull saturation below and secondary
diameter-count minimization are different normalizations and must not be silently
imposed simultaneously. Interior isolated points cannot be dropped.

**Additional promoted integrator update (2026-09-09):** the
[shared ambient-force/cap module](../../theory/04-ambient-force-and-cap-transport.md)
gives near-minimal circumradius for every selected force hull, uniform
`P_*=2D-O(sqrt(D))`, vanishing `O(D^(-1/4))` shared-endpoint diameter angles,
and a two-sided exterior-population/area law. The older fixed-angle ceiling below
remains valid but is asymptotically superseded. No post-ZF numerical consequence
or matching classification is promoted by this update.

## 1. Normalization

Let `A` be a triangle-free global `n`-point minimizer with diameter `D=D(n)`. Work
with a contact-minimal representative and then apply contact-preserving diametral hull
saturation. The resulting representative may be chosen so that

- the nonisolated contact core and its unit-contact graph are unchanged;
- every point on the convex-hull boundary is a genuine diameter endpoint; and
- every diameter endpoint is a convex-hull vertex.

The nonisolated contact core already contains a pair at distance `D`.

For the active unit contacts `C` and diameter pairs `H`, use signed fixed-diameter
first variations

`phi_e(v) >= 0`

for feasible critical velocities: contacts lengthen and diameter pairs shorten.
Write

`K_D(A) = { v : phi_e(v) >= 0 for all e in C union H }`.

## 2. Maximal KKT support and force hull

Let the normalized KKT polytope consist of nonnegative contact/diameter multipliers
satisfying vertex equilibrium and `sum_H beta_h = 1`. Let

`C_*` and `H_*`

be the unions of the positive supports over all normalized KKT stresses. The maximal
support can equivalently be obtained from one relative-interior point of the KKT
polytope.

The associated force-visible vertex set has a canonical convex hull `F(A)`, the
**force hull**. The promoted force-hull theorem gives the same convex hull from the
positive contact support and positive diameter endpoints of any maximal-support KKT
stress. Its diameter is `D`.

For the canonical C-II representative with (D\ge9), the promoted
[zero-transfer equality exclusion](../../reports/target_c_zero_transfer_additive_promotion_2026-09-11.md)
also gives `min_{e ne f} K_{ef}<0`. Equality would force a diagonal transfer
kernel, then an additive circular-planar resistance metric, and finally a
source-preserving SEPq separator whose degree violates C26/C35. This applies
before any (s_Z=0) or Woodall diameter-topology split and retains
contact-isolated source points.

The force-hull branch of interest is two-dimensional: the one-dimensional force-hull
phase is canonically excluded for every global minimizer with `D>1`.

## 3. Critical-cone duality

For every active constraint `e`,

`e in C_* union H_*`

if and only if

`phi_e(v)=0 for every v in K_D(A)`.

Hence strong constraints are precisely the active constraints frozen throughout the
fixed-diameter critical cone. Every weak active constraint is strict in some critical
direction, and there exists one critical velocity making **all** weak active
constraints strict simultaneously.

This is an exact first-order statement. It does not by itself integrate to a finite
same-diameter path.

## 4. Diameter shear and finite integration

For `h=ij in H_*`, every critical velocity satisfies zero radial first variation, so
there is a unique angular rate

`omega_h(v) = J(p_i-p_j) dot (v_i-v_j) / D^2`.

Let `Omega(v)` be the vector of these rates modulo the common-rotation direction.

If a relative-interior critical velocity has `Omega(v)=0`, subtracting the common
infinitesimal rigid rotation makes every strong diameter pair fixed to first order and
in fact fixed along the resulting straight motion. All weak contacts lengthen and all
weak diameter pairs shorten. For sufficiently small positive time this produces a
finite family of global minimizers of the same diameter in which every weak active
constraint is strict.

Therefore a contact-minimal representative with a weak unit contact cannot admit such
a zero-shear release.

## 5. Exact separator alternative

If no relative-interior critical velocity has zero shear, finite-dimensional cone
duality produces a nonzero angular functional on `H_*`, with coefficients `gamma_h`
satisfying

`sum_{h in H_*} gamma_h = 0`,

whose virtual work is strictly positive on the relative interior of `K_D(A)`. The
same functional is represented by a nonnegative combination of the ordinary signed
active-constraint rows, and that nonnegative radial carrier uses at least one weak
active constraint.

Statically, a surviving weak-contact obstruction is therefore exactly a
zero-resultant, zero-total-torque tangential load on the strong diameter chords carried
by nonnegative radial active forces.

This is the canonical Target C-I obstruction. There is no unidentified first-order
bulk locking left.

## 6. Connected positive support

For **every** normalized KKT stress, its positive unit-contact graph has exactly one
nontrivial connected component. The proof uses componentwise reaction balance,
strict outward-normal location of positive diameter reactions, planarity of unit
contacts, and the audited noncrossing-partition lemma.

The unique positive component contains both endpoints of every positive diameter edge
and therefore has Euclidean diameter exactly `D`.

In the triangle-free case it is a connected triangle-free penny graph. Consequently
its graph diameter is at least `ceil(D)`, and Eppstein's bound gives

`|C_+| <= 2 |V(C_+)| - ceil(D) - 2`.

Thus the force-carrying network is one macroscopic full-diameter object, not a union of
small stressed islands.

## 7. Reciprocal force polygon and response

Kron reduction of the positive contact network to its loaded boundary gives a
circular-planar Dirichlet response. Maxwell reciprocity constructs a convex reciprocal
force polygon `F*` whose boundary edge vectors are the positive diameter reactions.
The primal force hull `F` and reciprocal polygon satisfy the exact mixed-area identity

`2 V(F,F*) = D^2`.

The reciprocal perimeter `P_* = per(F*)` satisfies

`sqrt(3) D <= P_* <= 2D`.

The upper endpoint is the positive-diameter matching phase. The lower endpoint is the
equal-weight equilateral three-diameter phase. Global minimum-diameter packing excludes
the lower endpoint for all sufficiently large sources and in fact gives a uniform
asymptotic gap above it.

The response-matrix and reciprocal-polygon identities are canonical. The promoted
September 9 audit additionally establishes the actual selected-stress comparison
`Lambda-L_H>=0`. This is not a generic planar-network comparison without affine
equilibrium and the consistently oriented diameter-thrackle hypotheses.

## 8. Contact bridges, block collapse, common route, and straight-chain suppression

Let `uv` be a bridge of the positive unit-contact graph for one normalized KKT stress.
Removing it splits the graph into components `S,T`. The positive diameter-reaction
vertices on each side form complementary cyclic intervals of the force-hull boundary,
and the exact cut law is

`sum_{b in B_S} g_b = alpha_uv (u-v)`.

Expanding the reactions in the positive diameter graph gives the sharper diameter-cut
flow identity

`alpha_uv (u-v)
   = sum_{bk in H_+, b in B_S, k in B_T} beta_bk (b-k)`.

Hence every positive contact bridge separates the endpoints of at least one positive
diameter edge.

The corresponding reciprocal boundary arc closes by the diagonal

`Delta z = alpha_uv J(u-v)`.

The diagonal is perpendicular to the primal bridge and has length exactly
`alpha_uv`. The side resultant has line of action through the bridge endpoint. For any
pairwise disjoint collection of oriented bridge-side components,

`sum alpha_bridge <= P_* <= 2D`.

In particular all leaf bridges together carry at most `2D` of the total positive
contact stress `D^2`. More generally every bridge-tree frontier is an `O(D)` stress
cut. Therefore a positive fraction `eta D^2` of bridge stress forces bridge-tree
unit-edge depth at least `eta D/2`.

There is also an exact bridge-side virial identity. If `S` is the side containing `u`,
then

`sum_{xy in C_+[S]} alpha_xy
    = sum_{b in B_S} (b-u) dot g_b`.

Writing `s_b=sum_{bk in H_+} beta_bk`, the diameter support inequality gives

`sum_{xy in C_+[S]} alpha_xy
    >= (1/2) sum_{b in B_S} s_b |b-u|^2`.

Thus positive diameter mass far from the bridge endpoint has a quadratic internal
stress cost.

The local equilibrium along a bridge corridor is rigid. A positive-contact vertex
with no positive diameter reaction cannot have degree one. If it has degree two, its
two unit contacts are exactly antiparallel and have equal stress. Thus every maximal
run of unloaded degree-two vertices is an exact straight unit chain carrying constant
stress.

The stronger two-terminal collapse theorem removes a larger loophole. Any connected
positive-contact region with no positive diameter reaction and exactly two
positive-contact edges leaving it is, regardless of its assumed internal branching or
cycles, an exact straight constant-stress unit chain. The proof sums force and torque
to make the two terminal loads equal, opposite, and collinear, then projects equilibrium
perpendicular to that line. The resulting positive weighted graph Laplacian has zero
Dirichlet energy, forcing every vertex of the region onto the same line.

Delete all positive-contact bridges and contract the remaining components to the
bridge-block tree `T`. Every leaf block contains positive diameter reaction. Every
reaction-free degree-two block is only one unloaded degree-two vertex, so every
nontrivial reaction-free block has bridge-tree degree at least three. After suppressing
those neutral degree-two vertices, the structural bridge tree has at most

`2 |B_+| - 2 <= 2 pi D - 2`

nodes and at most

`2 |B_+| - 3 <= 2 pi D - 3`

maximal bridge corridors. Each such corridor is an exact straight constant-stress unit
chain. The bound uses `|B_+| <= per(F) <= pi D`.

For every `h=bk in H_+`, let `P_h` be the unique path in `T` between the blocks
containing `b` and `k`. Any two such paths intersect: shared diameter endpoints give a
shared terminal block; disjoint diameter edges cross as a geometric thrackle, so their
four hull endpoints alternate, and two vertex-disjoint plane contact paths cannot join
the two alternating pairs. Tree Helly therefore gives a common block on every
positive-diameter terminal path.

Root `T` at any such common block `X_*`. No positive diameter edge is internal to any
branch of `T-X_*`. For a descendant bridge `e`, let

`w_e = sum_{b below e} s_b`.

Then `w_e` is exactly the `beta`-mass of positive diameter edges crossing that bridge
cut, and

`alpha_e <= D w_e`.

The rooted masses have the exact layer-cake identity

`sum_{e in E(T)} w_e
   = sum_{b in B_+} s_b d_T(tau(b),X_*)`.

Hence if bridge stress is at least `eta D^2`, the probability measure with atom
`s_b/2` at each positive diameter endpoint has mean bridge depth at least `eta D/2`
from the common hub. This is only a weighted-mean statement: it does not by itself
force a fixed positive fraction of the endpoint mass to lie at depth `Omega(D)`.

The complete common intersection

`I_* = intersection_{h in H_+} P_h`

has additional rigidity. It is a path. Every internal node of `I_*` is reaction-free:
a positive diameter edge incident to a loaded vertex there starts at that block and
cannot traverse both sides of the common path. An internal node also has no side
branch: C20 forces a loaded endpoint somewhere in that side branch, whose positive
diameter path again could not traverse both sides of `I_*`. Thus every internal node
has degree exactly two in the whole bridge-block tree and C22 collapses it to one
neutral vertex.

Consequently, if `I_*` contains `L>=1` bridge edges, those bridges form one exact
straight constant-stress unit contact chain and

`L <= D`.

Moreover every positive diameter edge crosses every bridge cut in `I_*`. Hence if
`I_*` contains a bridge, `H_+` is bipartite. Since every diameter-graph cycle is odd,
`H_+` must then be a forest. Contrapositively, every phase in which `H_+` contains a
cycle has `I_*` equal to one common bridge block; no positive contact bridge is
traversed by every positive diameter pair.

The forest phase is more rigid still. Fix any bridge of `I_*` and list its two loaded
sides as complementary boundary intervals

`A=(a_1,...,a_p), B=(b_1,...,b_q)`

in the same cyclic direction. Every positive diameter edge joins `A` to `B`. If
`a_i b_j` and `a_k b_l` are vertex-disjoint with `i<k`, the diameter-thrackle property
forces the chords to cross, which is equivalent to `j<l`. This order monotonicity
forbids any diameter vertex from having three non-leaf neighbors: the middle of three
ordered non-leaf neighbors has a second edge that inverts against one of the two outer
edges. Since `H_+` is already a forest, the non-leaf induced subgraph of each connected
component is a path. Thus

`H_+ = disjoint union of caterpillar trees`

in the common-bridge phase.

Suppressing unloaded degree-two vertices in the full positive contact graph gives the
plane structural skeleton from C21. Every skeleton edge `E` is a straight segment of
positive integer length `L_E`, carries one constant stress `alpha_E`, and

`sum_E L_E alpha_E = D^2`.

At an unloaded skeleton vertex the incident unit-direction stress vectors balance;
at a reaction vertex they sum to the canonical boundary reaction `g_b`. A bridge
skeleton chain repeats one and the same reciprocal diagonal until a structural event
changes the cut data.

The articulation branch therefore has two sharper phases. If the common route contains
a bridge, the positive diameter graph is a common-cut caterpillar forest and every
positive diameter pair crosses one universal straight contact-chain core, with the
remaining weighted depth in rooted side branches. If `H_+` has a cycle, the universal
route is a single bridge block, pushing the obstruction toward the two-edge-connected
reciprocal-response phase. Complementary boundary intervals do **not** force the
positive diameter edges crossing one bridge cut to share an endpoint; order-reversing
crossing matchings remain a live cancellation regression.

## 9. Second-order angular reduction

For a relative-interior weak-release critical direction and its direction-dependent
second-order KKT multiplier, write `kappa_e` for the angular rate of each zero-radial
unit contact and `omega_h` for each supported diameter chord. After removing the
weighted common angular mean `bar_omega`, the promoted second-order theorem gives the
weighted variance inequality

`(1/D^2) sum_C alpha_e (kappa_e-bar_omega)^2
    <= sum_H beta_h (omega_h-bar_omega)^2`.

This is support- and velocity-specific: the second-order multiplier may depend on the
critical direction and need not use all of `H_*`.

The theorem turns the nonlinear obstruction into a quantitative comparison between
angular strain in the connected positive contact network and shear of the diameter
support. It does not prove the reverse comparison.

## 9A. Three-edge response-inertia reduction

The response reductions in C30-C32 give an exact finite endpoint audit for one
selected normalized stress. If the positive diameter endpoints span two dimensions,
Schur reduction and the two affine response identities imply

`nu_-(Omega_s) <= rank(L_H)-2 <= |H_s|-2`.

For a three-edge diameter forest, the only possible non-affine negative mode is the
scalar

`rho_s = sum_h beta_h R_eff(h) - 2`,

with the three nonzero conjugated response eigenvalues `1, 1, rho_s`. Thus
`rho_s > 1` is exactly the PSD obstruction for this support.

C31 proves `Omega_s >= 0` for a three-edge forest on four force-hull endpoints, and
gives `rho_s < 1` when the source is triangle-free. C32 proves `Omega_s >= 0` for
the five-endpoint path-plus-edge topology, giving `rho_s <= 1`. The K6
half-turn/Kalmanson lemma now proves `rho_s <= 1` for the remaining convex
six-endpoint matching. Thus every three-edge forest has no negative response mode.
These are selected-stress statements: they do not prove that a direction-dependent
second-order multiplier has maximal support, and they do not establish a general
PSD/Loewner comparison.

C33 gives an exact six-endpoint regression: affine-kernel and nonpositive
off-matching response signs alone do not force the defect to be PSD. Its matrix is
not asserted to be a circular-planar unit-contact response; in fact it violates an
exact circular minor. K6 shows that the actual circular-planar response has no
negative mode for the three-edge convex matching; the remaining C-I work must use
support selection, equality analysis, larger diameter supports, or global hypotheses.

The selected-stress convex six-terminal matching is now closed: for any strictly
convex six-gon in cyclic order with opposite matching diameter support, half-turn
averaging of the response matrix and one circular-planar resistance/Kalmanson
inequality give `rho_s <= 1`, hence `Omega_s >= 0`. No central symmetry
or regularity is required. EQ6 now shows that equality forces an additive
effective-resistance metric, but electrical equivalence does not identify the
physical contact graph with a one-hub star. CONC6 further forces the weighted
boundary barycenter into all three matching chords, so equality requires a common
interior chord point. SEP6 adds a source-preserving C-II consequence: the
star-equivalent response has zero every two-by-two circular minor, so the actual
contact graph has no two disjoint terminal paths. Gallai's T-path formula then
forces a separator incident to at least six contacts if unloaded, or five if it is
loaded; C26/C35 exclude both possibilities. Thus `rho_s=1` is impossible in the
fully force-visible six-terminal branch. The result is recorded in the promoted
K6 addendum
[target_c_convex_six_matching_kalmanson_2026-08-31.md](../../reports/target_c_convex_six_matching_kalmanson_2026-08-31.md),
and the equality-separator proof in
[target_c_six_matching_star_separator_2026-08-31.md](../../reports/target_c_six_matching_star_separator_2026-08-31.md).

TP5 supplies the initial complementary non-additive topological reduction. CR4
sharpens it using the connected quotient of a deleted separator: in fully
force-visible C-II, C26/C35 and Gallai's T-path theorem give
`nu_(B_+)(C) >= (|B_+|-1)/4`; pairing a maximum path packing yields at least
`floor((|B_+|-1)/8)` pairwise terminal-disjoint strict circular minors. By C34 this
is at least `floor(ceil(D)/16)`. The result is a count of strict response
witnesses, not a uniform lower bound on their numerical sizes, so it does not yet
close the response defect. It is recorded in
[target_c_terminal_path_packing_connected_refinement_2026-08-31.md](../../reports/target_c_terminal_path_packing_connected_refinement_2026-08-31.md).

The quantitative transport cannot come from circular planarity and degree caps alone.
A bounded-degree cycle-with-leaves network can converge electrically to a star while
retaining the CR4-linear family of strict minors, with arbitrarily small aggregate
minor mass. This regression omits unit-contact geometry, KKT equilibrium, and the
`q=Omega(D)` diameter scale; those hypotheses must be used together in any response
gap theorem. It is recorded in
[target_c_near_star_response_minor_regression_2026-08-31.md](../../reports/target_c_near_star_response_minor_regression_2026-08-31.md).

The C35 regular-hexagon Kalmanson audit is subsumed by C50. Its star-response equality
example remains useful: `rho=1` is genuinely realizable by a connected
circular-planar response, so semidefiniteness alone does not provide the exact affine
kernel required by finite integration. C50 isolates the same equality boundary for
every strictly convex six-endpoint matching and, via the Kalmanson split cone,
classifies it at response level as a weighted-star metric with concurrent matching
chords. C50.2 now closes that equality for the actual triangle-free unit-contact
network: zero order-two circular minors force a one-vertex separator with at least
six incident contact edges, impossible in a triangle-free unit graph. Thus the
selected three-edge six-endpoint response has `rho<1`; this remains a selected-stress
statement and does not supply maximal KKT support or close C-I.

### 9B. Four-pair opposite-matching contraction

C51 proves a new four-edge response subcase. Let eight strictly convex cyclic
force-hull terminals be paired by the opposite matching
`H={04,15,26,37}`, with positive diameter weights `beta_i`. If `Q` is the
pair-incidence matrix, `K=Q^T Lambda^+ Q`, and the circular-planar response obeys
the affine identity `Lambda P=L_H P`, then

`B^{-1}-K >= 0`,

where `B=diag(beta_i)`. Equivalently, both non-affine response modes are at most
the threshold one, so the selected boundary defect `Lambda-L_H` and the full
selected Schur defect are positive semidefinite. The proof uses the strict convex
opposite-chord orientation, the exact Kalmanson monotonicities
`K_ik<=K_jk` for `i<j<k`, and a two-by-two factorization of the affine-kernel
defect. Unequal chord scales are retained through the positive factors
`gamma_i=a_i beta_i`; no equal-length or regular-octagon assumption is present.

C51 is still selected-support-specific. It does not prove a PSD/Loewner comparison
for an arbitrary diameter support, select the direction-dependent maximal KKT
multiplier, or close the C-I shear-separator alternative.

## 10. Global diameter geometry

Target C imports global packing bounds into the diameter graph itself.

### 10.1 Reuleaux triple exclusion

Three pairwise diametral points trap the whole configuration in their Reuleaux
triangle. Comparing finite-packing lower bounds with the global upper bound on `D(n)`
excludes such a triple for every sufficiently large minimizer; the audited report gives
an explicit threshold `n >= 362`.

### 10.2 Shared-endpoint angle bound

If two diameter chords `by` and `bz` share the endpoint `b`, their angle `theta`
satisfies the explicit bound

`theta < [D(5*pi/6-sqrt(3)) + 4*pi/3 + pi/(2D)]/(D+1)`.

Hence

`limsup theta <= 5*pi/6 - sqrt(3) = 50.7607988... degrees`.

This applies to the full diameter graph, not merely to positive KKT diameter edges.

### 10.3 Diameter-cycle girth

Any diameter-graph cycle is odd and determines a Reuleaux polygon of width `D` that
contains the entire source. Firey-Sallee area extremality plus the global packing
bound yields

`q > pi D / sqrt(12(2D+1))`

for a diameter cycle of length `q`. In particular `q = Omega(sqrt(D))`.

Thus fixed and slowly growing diameter cycles are impossible in a sufficiently large
global minimizer.

## 11. Exact Target C gates

Target C has two logically separate gates.

### C-I. Closed by exact finite release

The [promoted restoration audit](56-ci-restored-frontier.md) establishes universal
selected-stress PSD and the convergent C63 correction. A weak unit contact in a
contact-minimal triangle-free global source would admit a finite same-D release
without any new unit contact, a contradiction. Thus `C=C_*`. This proof does not
need to produce a zero-shear velocity; it bypasses that older sufficient mechanism.

### C-II. Fully force-visible contradiction

Assume `C=C_*`. Then the nonisolated part of the unit-contact graph is one connected
full-diameter positive network inside a two-dimensional force hull, with the reciprocal mixed-area
identity, force-perimeter restrictions, second-order angular inequality, explicit
diameter-star angle bound, diameter-cycle girth theorem, and Section-8 articulation
reduction.

C34 adds the exact endpoint budget

`2 |B_+| >= ceil(D)+2`,

and hence `|H_+| >= (ceil(D)+2)/4`, by identifying `B_+` with the nonisolated source
diameter endpoints and comparing the canonical pinned-core rank lower bound with
Eppstein's connected triangle-free penny-graph upper bound. This is a C-II reduction,
not a contradiction: it gives no individual diameter-weight lower bound.

There are now two principal C-II subbranches, with the bridge branch itself split by
the common-route core.

1. **Bridge transport.** A nonnegligible fraction of contact stress lies on bridges.
   All positive diameter terminal paths have a common intersection `I_*`.
   - If `I_*` contains a bridge, then `I_*` is one exact straight constant-stress unit
     contact chain of length at most `D`, and `H_+` is a common-cut caterpillar forest:
     every component has one alternating diameter spine plus leaves, ordered
     monotonically across the fixed cut. The remaining weighted hub depth lies in
     C22-C23 rooted side branches. The live theorem is a **caterpillar/common-route
     transport theorem** excluding this phase by global packing, angle accumulation,
     reciprocal cut forces, or a strict sub-`D` competitor.
   - If `I_*` is one block, this includes every positive-diameter cycle phase. The
     bridge tree still has the C23 scalar endpoint flow, but the common obstruction is
     concentrated in one bridgeless block and naturally joins the next subbranch.
2. **Two-edge-connected stress bulk.** Almost all normalized contact stress lies in
   two-edge-connected triangle-free penny blocks, or the common diameter-route core is
   already one dominant bridgeless hub block. Attack this phase through the
   circular-planar response, reciprocal mixed area, full Maxwell reciprocal/lifting,
   face structure, or the angular variance theorem; bridge combinatorics alone no
   longer apply.

The common endpoint remains:

> **Force-visible contradiction theorem.** No sufficiently large triangle-free global
> minimizer can satisfy the fully force-visible Target C normal form.

## 12. Level I closure

With C-I restored and proved, proving the complete C-II exclusion rules out every
sufficiently large triangle-free global minimizer. Contact-isolated source points
and all genuine C-II alternatives must remain in its quantifiers.
That proves the affirmative Level I statement of Erdős Problem #99 independently of
Target A and Target B.

Target C is therefore a genuine third endgame, not an auxiliary lemma collection.
