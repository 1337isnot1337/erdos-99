<!-- theorem-state: {"artifact_id":"ART-087DCFC234A7","canonical":true,"claim_ids":["C-GENERAL-SIX-WALL-FIRST-PROFILE-COMPATIBILITY","C-GENERAL-SIX-WALL-FULL-CHART-PINNING-RATE","C-GENERAL-SIX-WALL-OLER-LIMIT"],"claim_statuses":{"C-GENERAL-SIX-WALL-FIRST-PROFILE-COMPATIBILITY":"canonical","C-GENERAL-SIX-WALL-FULL-CHART-PINNING-RATE":"canonical","C-GENERAL-SIX-WALL-OLER-LIMIT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — Oler localization and first-profile compatibility

**Audit base:** `main` at `f875b4f3a2eb8431f73f0aa88c8bc984858f2fcc`,
state `2026-10-07.audit.80`.

**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at
`8af7e411ae1c1797dbd624c96729c36d3885367e`. This tip added the
first-profile report, exact opposed-profile verifier, and its finite
certificate. A final fetch after the audit found no later source commit; the
separate effective small-slack chart report remains unaudited.

## Exact claims promoted

Fix `M>=3`. Let `W_theta` be a `C^2` family of convex unit-edge polygons
with six labelled sides of `M` edges each, converging to the regular
triangular-lattice hexagon `H_M`. Write `N=3*M^2-3*M+1`.

1. **General-family Oler limit.** For every such fixed family, all sufficiently
   small `theta` placements whose union of the `6M` labelled wall vertices
   and `z` additional points in the closed wall is pairwise unit-separated
   satisfy `z<=N`. If `z=N` along a sequence `theta_n->0`, a relabeled
   subsequence converges to the full radius-`M` triangular lattice `P_M`; the
   additional cloud converges to its strict interior `P_(M-1)`.
2. **Full-chart pinning rate.** In the flat chart `P_M` with its full boundary
   pinned and every interior point moving, the complete moving-involving
   unit-edge matrix has full column rank and a strictly positive equilibrium.
   Every convergent feasible cloud under an `O(theta)` perturbation of the
   boundary therefore moves by `O(theta)`.
3. **First-profile compatibility.** Suppose each side's edge directions have
   first angular rates
   `beta_(k,0)<...<beta_(k,M-1)` relative to its limiting side direction.
   If the union of all `6M` wall vertices and `N` strict-interior points is
   pairwise unit-separated for arbitrarily small positive `theta`, then,
   after one common infinitesimal rigid rotation, all six ordered rate lists
   are identical and have mean zero. Every subsequential
   radial-increment vector is a permutation of this common list, and the
   first cloud velocity is the corresponding rate-sorting field. In
   particular, if two side lists differ, there is a family-dependent
   `theta_0>0` below which no `N`-point cloud exists; the Oler cap then gives
   maximum population `z<=N-1`.

The wall family is fixed while `theta` tends to zero. No threshold uniform in
`M` or among wall families is claimed. Matching first profiles do not identify
the second-order wall data, produce a finite packet, or exclude `z=N`.

## General-family Oler localization

The `6M` wall labels converge to the unit-spaced boundary layer of `H_M`,
and `per(W_theta)=6M`. Consecutive boundary labels are exactly one unit
apart. In the limiting triangular-lattice boundary, any distinct
nonconsecutive labels are at distance at least `sqrt(3)`; since `M` is fixed,
continuity keeps all such wall pairs strictly farther than one for small
`theta`. Thus the wall labels themselves are pairwise unit-separated in the
regime used below. For any feasible placement, their union with the added
points is pairwise unit-separated. Oler gives

`z+6M <= (2/sqrt(3))*area(W_theta)+3M+1`.

The right side converges to `3*M^2+3*M+1=N+6M`, so it is strictly below
`N+6M+1` for all sufficiently small `theta`; integer rounding gives
`z<=N`. This is family-dependent continuity, not a uniform curvature bound.

If `z=N` along `theta_n->0`, compactness gives a unit-separated limiting set
of `N+6M=3*M^2+3*M+1` points in `H_M`, exactly the Oler equality count. The
Thue-Groemer/Oler equality case checked in Audit.74 triangulates the limiting
hexagon into unit equilateral triangles using all points. A limiting boundary
unit edge fixes the triangular-lattice orientation, and propagation across
the connected triangulation fixes every point in the same lattice. `H_M`
contains exactly `P_M`, so the limiting set is all of `P_M`; the `6M` wall
labels are its boundary layer and the added cloud is `P_(M-1)`. This argument
uses only the limiting hexagon and equality count, so it applies to the
general family above, not just the previously specified curved wall.

## Full-chart first-order pinning

Use every unit edge of `P_M` with at least one interior endpoint as a row.
Weight each row one. At every interior lattice site, the six incident
directions sum to zero, hence these weights form an equilibrium on all moving
columns. If a first-order feasible velocity has nonnegative row variations,
their sum is zero, so every row variation is zero.

Triangulate `H_M` into elementary unit triangles. The triangle-adjacency graph
is connected, and every vertex belongs to a triangle. A zero bar-variation
field on one triangle is an infinitesimal rigid motion. Two such motions
agreeing on a shared edge agree everywhere; propagation gives one rigid
motion on the entire chart. It vanishes at the pinned boundary, so it is
zero. Thus the moving-column matrix has full rank.

For the rate statement, let `delta` be the maximum interior displacement and
let the boundary displacement be `O(theta)`. Every old unit-edge inequality
gives a linear row lower bound of order
`-O(theta+delta^2)`. Summing the rows with the positive unit stress leaves
only boundary terms, of order `O(theta)`. Thus each row is also bounded above
by `O(theta+delta^2)`. Full rank supplies a left inverse, so
`delta<=C*(theta+delta^2)`. Since the placements converge to the flat chart,
absorb the quadratic term and obtain `delta=O(theta)`. This proves the
needed scale without assuming that an arbitrary first-order velocity
integrates to a finite motion.

## First-order and second-order profile comparison

Take any sequence of maximum-population clouds with `theta_n->0`. By the
Oler limit and full-chart rate, after relabeling and a subsequence the cloud
positions have expansions `p+theta*d_p+o(theta)` and the boundary vertices
have first velocities `g`.

Let `e_k=exp(i*k*pi/3)`. Summing the zero first variations of the `M` unit
wall edges on each side and then summing over all six sides gives

`sum_k e_k dot g(M*e_k)=0`,

using `e_(k+1)-e_(k+2)=e_k`. For each ring `r=1,...,M-1`, the unit stress on
that ring and on the radial chains from its corners to the wall corners has
positive weights, balances every moving vertex, and has this same boundary
work. The `r=0` stress is the six full radial chains. Therefore every radial
and ring row used by these stresses has zero first variation.

Radial equalities give
`d(r*e_k)=d(0)+alpha_(r,k)*J(e_k)`. Summing the ring rows along a side
shows `alpha_(r,k)` is independent of `k`; the wall side rows give the same
fact at `r=M`. Remove the common translation and the rotation of rate
`alpha_M/M`. Then `alpha_0=alpha_M=0`, and
`t_h=alpha_(h+1)-alpha_h` has `sum_h t_h=0`. The boundary first velocity on
side `k` at index `j` is `J(e_(k+2))*B_(k,j)`, where
`B_(k,j)=sum_(ell<j) beta_(k,ell)` in the normalized frame.

The two remaining nearest-neighbor lower rows in sector `k` give the layer
recurrences

`s_(r,j)>=s_(r-1,j)`,
`s_(r,j)>=s_(r-1,j-1)-t_(r-1)`,

with `s_(r,0)=0`, `s_(r,r)=-alpha_r`, and the wall endpoint
`s_(M,j)=-B_(k,j)`. Following a path with diagonal steps indexed by any
`j`-element subset `I` yields

`sum_(h in I) t_h >= B_(k,j)`.

Since each normalized `beta_k` is strictly increasing and has zero sum,
these are exactly the lower subset inequalities for the permutahedron
`P_k=conv{permutations of beta_k}`. Thus `t in P_k` for every side.

Now use only the six central radial chains in the exact squared-distance
inequalities. With `x_k(theta)` the actual wall corners, telescoping the
edge projections onto the flat side directions gives

`sum_k e_k dot (x_k(theta)-M*e_k)`
`   = -(theta^2/2)*sum_k ||beta_k||^2+o(theta^2)`.

Each radial edge constraint is
`2*e_k dot (delta_out-delta_in)+||delta_out-delta_in||^2>=0`. Summing over
the six chains cancels all interior linear terms and gives

`sum_radial ||delta_out-delta_in||^2`
`   >= -2*sum_k e_k dot (x_k(theta)-M*e_k)`.

After division by `theta^2`, the left side tends to `6*||t||^2`; hence
`6*||t||^2>=sum_k||beta_k||^2`. For each side, `t in P_k` gives
`||t||^2<=||beta_k||^2`, because all permutahedron vertices have that
common norm. Therefore every nonnegative difference
`||beta_k||^2-||t||^2` is zero. Strict convexity of squared norm forces `t`
to be a vertex permutation of each `beta_k`. The side lists are strictly
increasing, so all six lists coincide.

For completeness, the unique minimizing subset of each size is strict when
the rates are distinct. Equality along its recurrence path fixes each
intermediate `s_(r,j)`; as the subset size varies, these paths pass through
every layer site. Thus the full first cloud field is the rate-sorting field
for that permutation. This is a first-order classification only.

If two lists differ, a sequence of `N`-point clouds at arbitrarily small
`theta` would have a subsequence satisfying the equality just proved, a
contradiction. The Oler cap then reduces the population to `z<=N-1` for all
sufficiently small positive curvature in that fixed family.

## Certificate audit and hostile scope checks

The frozen verifier was inspected and rerun; its JSON matches the saved
certificate byte-for-byte (SHA-256
`45b50ab70368c498304f9474e1aafed868063863ae0bfef4697d64abf8c48f1e`). Its
`Q(sqrt(3))` arithmetic checks two `M=4` closed convex unit-wall families,
including a pair of distinct profiles with equal squared norm. It verifies
unit edges, every wall pair, strict convex supports, the finite Oler margin,
and the telescoping corner-work identity for those examples. It does not
search interior clouds or prove the universal profile-matching theorem; the
analytic argument above supplies that implication.

Adversarial scope checks: the Oler equality limit is applied only after
proving the general wall family has the same `H_M` limit and exact equality
count; the `O(theta)` localization uses full-chart equilibrium and rank, not
the one-vacancy theorem outside its scope; the second-order stress uses only
the six radial chains and counts all wall-side rates; equal profile energies
alone are insufficient, but the norm-saturation argument forces actual
permutation vertices. The claim never promotes a feasible wall or cloud to
a globally optimal source and does not infer a packet from first-order
compatibility.

**Verdict: PASS — promote** the general-family Oler limit, full-chart pinning
rate, and first-profile compatibility at the stated scopes. A profile
mismatch removes the top population but supplies no strict packet for the
remaining `z<=N-1` points. Matching first profiles do not control higher
wall coefficients. Arbitrary wall extraction and Target C-II remain open.
