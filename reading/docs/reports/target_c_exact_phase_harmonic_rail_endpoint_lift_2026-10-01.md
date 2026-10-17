> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_harmonic_rail_endpoint_lift_2026-10-01.md) · source SHA-256 `6552d5867f3d1b08bd5ee7650b75e75f44164abbb59c5f652ff7b64604123481`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-37586000F77D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — actual transverse rails require two loaded endpoints in every gap

**Phase 2 preservation provenance:** PR #594, branch swarm/gap-reaction-cut-20261001, audited source head 02d4cc04e2df2e0f0aa1eb2a9ec3cf21cc53f18f. Preserve as an unreviewed conditional endpoint-fiber result with its finite source regressions; it does not rule out the remaining threshold branch.

`positive source equilibrium -> transverse harmonic components and loaded gap
width -> endpoint-fiber restrictions on the paired staircase -> an additional
source/interface contradiction or finite competitor -> Level I`

**Date:** 2026-10-01
**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`
**Predecessor checkpoint:** `07188f0d6956b0d1ef1bf545bb874add561d8e06`
**State version:** `2026-09-14.audit.51`
**Mission:** put the exact-phase gap tree back on actual source contact rails.
**Classification:** proved candidate awaiting promotion; conditional route application;
exact regression to omitting positive source equilibrium.
**LEVEL I:** OPEN. C-I closed; C-II open.

## 1. Dependencies and exact scope

Canonical inputs are normalized positive source KKT equilibrium, full actual
contact/diameter support on the lexicographic source (`56-ci-restored-frontier.md`),
the unloaded core degree bound from shared local structure, and the strict rhombus
train geometry in shared Theorem 10.6. Let `V` be the positive-contact core and
`B` its actual loaded vertices. Contact-isolated source points remain in the source;
the harmonic statements below concern `V`, not those isolated points.

The route application assumes the **actual** proper O–O train cuts and source
shore labels of `target_c_complete_grid_rank_switching_2026-10-01.md`. Those
inputs are unpromoted. We do not infer their hypotheses from an abstract interval
matrix or a labelled point packet. The two-shore boundary statement uses the
explicit four-host-interval topology proved in the unpromoted
`target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md`.

Remote main advanced to `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec` during this
run; the state lock and manifest did not change. Its threshold staircase and
physical forest lift are research inputs, not promotions. The results below are
proved independently from the stated source hypotheses.

## 2. A source harmonic component theorem

Let the selected cuts be `E_1,...,E_m`. Every edge in their union is a unit
contact parallel to one unit vector `u`. Delete these edges from the positive
contact graph and let `S` be one remaining connected component. Define

```math
y_x=p_x\cdot Ju.
```

Then:

1. `y` is positive-weight harmonic at every vertex of `S` not in `B`;
2. if `y` is nonconstant on `S`, then `B_S=B cap S` contains at least two
   distinct vertices and
   ```math
   \min_{B_S}y=\min_S y<\max_S y=\max_{B_S}y;
   \tag{1}
   
   ```
3. with the actual outward diameter reaction
   `g_x=sum_{xy in H} beta_xy(p_x-p_y)`,
   ```math
   \sum_{x\in S}g_x\cdot Ju=0,
   \qquad
   \sum_{x\in S}y_x(g_x\cdot Ju)
   =\sum_{xz\in C[S]}\alpha_{xz}(y_x-y_z)^2;
   \tag{2}
   
   ```
4. if `y` is constant on `S`, every vertex of `S` is loaded, under the
   canonical unloaded degree-at-least-three hypothesis.

### Proof

Source equilibrium says

```math
\sum_{xz\in C}\alpha_{xz}(p_x-p_z)=g_x.
\tag{3}
```

Every deleted contact has zero `Ju` projection. Thus (3), projected on `Ju`,
retains only the internal edges of `S`. At an unloaded vertex its right side
vanishes. This is positive-weight harmonicity on the finite connected graph.
If the component has no loaded vertex, the finite maximum principle makes
`y` constant. If it has loaded vertices, the maximum principle puts every
internal value between their minimum and maximum. This proves (1), including
the claim that a nonconstant component has two loaded vertices with different
coordinates.

Sum the projected equations over `S`: each internal contact cancels and
each deleted contact has zero projection. Multiply each equation by `y_x`
and then sum: an undirected internal edge contributes exactly
`alpha_xz(y_x-y_z)^2`. These prove (2). No inactive pair is turned into an
active diameter.

If `y` is constant, all internal contacts are parallel to `u`, as are the
deleted contacts incident to `S`. A unit-separated point has at most two
unit contacts parallel to one line, so every vertex of `S` has contact
degree at most two. The canonical unloaded degree bound proves assertion 4.
This last assertion is not needed for the nonconstant-rail endpoint bound.
∎

The component balance in (2) is stronger than balance only after all components
in one gap are aggregated. There is no lower bound on a reaction multiplier or
conductance in this statement.

## 3. Actual train rails lift gap occupancy to transverse width

Suppose the `m` selected trains are ordered, with actual source layer labels
`0,...,m`. A train contact crosses its own selected cut, and other contacts
cross no selected cut. Each selected strict-rhombus train has two physical
rails: the chains of vertices at the two endpoints of its successive parallel
unit edges. The rails lie respectively in gaps `i-1` and `i`.

If train `i` contains `r_i` strict rhombi, each rail has transverse span

```math
L_i=\sum_{F\text{ on train }i}\sin\theta_F>
{\sqrt3\over2}r_i.
\tag{4}
```

In particular, if every selected train crosses all `n` trains of the opposite
retained shore, then `r_i>=n`.

The rail edges are actual unit contacts not parallel to `u`; hence no rail
edge was deleted. Each whole rail lies in one component from Section 2. It
follows that **every gap contains at least two loaded vertices**, and more
precisely

```math
\begin{aligned}
\operatorname{span}_y(B_0)&\ge L_1,\\
\operatorname{span}_y(B_j)&\ge\max(L_j,L_{j+1}) &&(0<j<m),\\
\operatorname{span}_y(B_m)&\ge L_m.
\end{aligned}
\tag{5}
```

Thus an all-crossing opposite shore of size `n` gives

```math
\boxed{q\ge2(m+1),\qquad
\operatorname{span}_y(B_j)>{\sqrt3\over2}n\quad(0\le j\le m).}
\tag{6}
```

### Proof of the rail assertions

Orient the train by increasing `h_u=det(u,p)`, as in Theorem 10.6. Across one
strict rhombus the vector from either endpoint of one train edge to the
corresponding endpoint of the next edge is the same unit transverse side
vector. Its `Ju` projection is `sin(theta_F)>sqrt(3)/2`. At a shared edge the
next rhombus is on the other side, so this orientation continues. The two
endpoint chains therefore have the same strictly increasing transverse
increments, proving (4).

The source cut hypothesis puts all endpoints on one rail in a single gap;
the unit side edges connecting successive endpoints cross none of the
selected cuts. They put the rail in one surviving component. Applying (1)
to that nonconstant component proves its loaded span is at least the rail
span. For an internal gap use either neighboring rail, proving (5). The
gaps are disjoint sets of actual source vertices, so their two loaded
vertices cannot be reused in the one-shore count. ∎

More generally, let `k_j` be the number of nonconstant transverse components
in gap `j`. Then `|B_j|>=2 k_j`. Multiple disconnected rails in a gap can
increase endpoint demand; they are not automatically different components.

## 4. Two exact shores: the valid joint count

If both shores are exact phase, apply Section 3 to each with its own normal.
An internal A-gap loaded vertex lies on an A-host boundary interval; an
internal B-gap loaded vertex lies on a B-host boundary interval. These
host intervals are disjoint in the proper complete-grid topology.
Equivalently, an actual loaded hull vertex cannot have both an internal
A-layer and an internal B-layer.

Hence, for `m,n>=1`,

```math
\boxed{q\ge2(m-1)+2(n-1)=2(m+n-2).}
\tag{7}
```

Combine (7) with each of the separate bounds `q>=2(m+1)` and `q>=2(n+1)`.
Do not add the two extreme-gap counts: an extreme A-gap may contain loaded
vertices counted in internal B-gaps, and conversely.

This does **not** improve the canonical small-defect grid diameter bound
`m+n<=2D/sqrt(3)+O(1)` from Section 76: at the rooted endpoint `q=pi D+o(D)`,
(7) alone gives the weaker `m+n<=pi D/2+o(D)`. It is an actual
endpoint-fiber and component restriction, rather than a closing density
inequality.

## 5. Threshold physical forest and the remaining source bridge

For a threshold paired staircase, select two oppositely oriented actual
diameters per simple gap-tree edge and retain the parallel threshold bar.
This is the `2m+1`-edge bipartite physical forest of the new main report.
The present source theorem requires at least two actual loaded vertices in
**every** gap, with the width in (6). The forest report's aggregate fiber
excess does not alone supply that per-gap width; nor does it ensure these
loaded vertices belong to the selected subforest. Additional actual
diameters can supply endpoints.

The full diameter graph satisfies `q=h+d_H`. Therefore (6) gives

```math
h\ge2m+2-d_H.
\tag{8}
```

In the cyclic `d_H=0` branch this needs at least one diameter beyond the
`2m+1` selected threshold bars. It does not exclude that branch. In the
forest branches `d_H` must be retained. The next credible bridge must
couple the wide actual endpoint fibers and full vertex equilibrium to
the physical staircase/remaining diameter edges, or produce a finite
source competitor outside the frozen witness chart.

## 6. Exact positive-stress regression and missing-equilibrium regression

For the unit square, select the horizontal cut with `u=(1,0)`. The surviving
components are its two vertical rails. Give every unit side weight `1/2`
and both actual diameter diagonals weight `1/2`. This is normalized positive
source equilibrium. Both gap fibers have transverse span one and two loaded
vertices; `q=4`, `h=2`, `d_H=2`.

The stress matrix is

```math
\Omega={1\over2}(1,-1,1,-1)^{\mathsf T}(1,-1,1,-1)
```

in cyclic vertex order, so it is PSD with affine kernel dimension three.
The count (6) is attained; (8) is attained. Dropping `d_H` would incorrectly
assert four diameters for this exact stressed source.

For the six-point unit `2 x 1` rectangular grid, the two horizontal train
cuts are genuine, all seven unit contacts are retained, and the middle gap
has a vertical unit rail. The only
actual diameter endpoints are its four corners. Thus the middle gap has no
loaded vertex. At either middle rail endpoint the vertical contact is the
only contact with nonzero vertical projection. Since that vertex is
unloaded, equilibrium would force this contact's weight to be zero.
Consequently no full-positive-support KKT stress exists. The cut geometry
alone cannot imply (6).

The verifier checks both actual point sets, every pair distance, the exact
square equilibrium/stress matrix, the deleted-contact components, and this
forced-zero obstruction. Neither finite example proves global optimality
for unbounded cardinalities.

## 7. Certificate and closure audit

Run `python3 research/verify_harmonic_rail_endpoint_lift_2026_10_01.py`.
The general component and rail proofs above are analytic; the verifier
checks exact finite regression contracts, not an enumeration of all sources.

All fixed-star/nonconstant-phase, split-star O–O, inactive-interface, and
macroscopic inactive-container branches remain to be settled. The count
and moment identity are not C-II closure. No canonical state is changed.
