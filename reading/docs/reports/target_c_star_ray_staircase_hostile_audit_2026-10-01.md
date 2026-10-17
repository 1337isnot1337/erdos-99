> Generated reading edition · [exact source](../../../docs/reports/target_c_star_ray_staircase_hostile_audit_2026-10-01.md) · source SHA-256 `13fe456659b5766b7fced94fcd28efd9c95a1d8ae3d03f1a9ee825af77b12226`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-554A319E0457","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: independent hostile audit of the star-ray staircase

**Phase 2 preservation provenance:** PR #597, branch swarm/root/c2-gap-reaction-20261001, audited source head c89adbcd2e008e1d01141fa38ff54b1bcae85678; the embedded independent hostile audit originated in merged PR #602 at head 004fdd2c0ccd9b3cffcd5aa5a16840d77d2b372d. Retain its exact audit scope and regressions; repository artifact status remains unreviewed.

Date: 2026-10-01.
Audited packet: [PR #597](https://github.com/1337isnot1337/e-99/pull/597).
Starting commit: `87375fe03cb9eff3f903c4110fc81457e8c16b26`.
State version: `2026-09-14.audit.51`.
Audit branch: `swarm/audit/star-ray-20261001`.
Mission: independently audit the ray-anchor extension, directed cycles, original
axial reactions, and universal representative order in equations (8)--(9).
Classification: completed independent audit; **audited-working under the explicit
geometric hypotheses; conditional for the C-II application**. This report's
repository lifecycle remains unreviewed until an explicit ledger registration.
Level I OPEN; C-I CLOSED; C-II OPEN. No canonical state is changed.

```text
star-ray hypotheses + actual projected positive balance + full train rank
  -> doubled antitone staircase + strictly positive original axial bundles
  -> actual cut-contact unimodality ONLY if the actual contact-cut law is supplied
  -> unresolved: exclude/deform that full source using the transverse train shore
  -> strict same-cardinality sub-D competitor / exact triangle / Level I consequence
```

The final source-level implication is absent. The geometric theorem survives this
audit. Its realizable regressions do not satisfy the actual source contact-cut law
or full KKT equilibrium.

## 1. Authority and exact audit scope

The audited proof is
[`target_c_star_ray_staircase_reactions_2026-10-01.md`](target_c_star_ray_staircase_reactions_2026-10-01.md).
Canonical status and source scope were checked against `docs/STATE.md`,
`docs/state/theorem-state.yaml`, the Target C route/current files and these modules:

| Canonical input | Role in this audit |
| --- | --- |
| [Section 56](../targets/target-c/56-ci-restored-frontier.md) | Contact-minimal, then diameter-pair-minimal representative; C-I restored; no full-support claim for arbitrary representatives |
| `C-ZRF`, [Section 57](../targets/target-c/57-zr-zf-rigidity-audit.md) | Mixed rigidity only on the nonisolated positive-contact core; isolates remain in the source |
| `C-FS-GEOM`, `C-FSD`, [Section 58](../targets/target-c/58-full-source-geometry-audit.md) | Actual extreme diameter endpoints, convex-thrackle geometry, global source star aperture and support dispersion |

The following are unpromoted and remain hypotheses of the C-II application:

- [local witness-cell extraction](target_c_local_witness_cell_2026-10-01.md);
- [global complete-grid train cuts and rank](target_c_complete_grid_rank_switching_2026-10-01.md);
- [joint switch/boundary-layer interpretation](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md);
- [graphic rank/connectivity](target_c_exact_phase_gap_graph_connectivity_2026-10-01.md).

Their statements and supplied proofs were inspected to locate the dependency
boundary. This audit proves the new geometric bridge under the explicit hypotheses
1--5 of PR #597. It does not certify every earlier train-shear, outer-face disk,
fixed-star extraction or complete-grid lemma used by those unpromoted reports.
In particular, the cyclic boundary layer order is an explicit premise here. An
outer walk with repeated vertices is not silently replaced by a convex-hull order.

No older C87 straight-chain argument, Euler-trail assertion, literature import,
finite-motion integration, or positive lower multiplier bound is used.

## 2. Independent ray-anchor proof

Let the two actual diameter witnesses be `vp-`, `vp+`, with rays strictly
straddling `u` and opening less than `pi/3`. Their partners and `v` have extreme
layer values `m` and `0`, respectively. The ray from `v` along `u` enters the
interior tangent cone of the convex hull and crosses `p-p+`. Its exit `z` therefore
lies on the partner-to-partner boundary subarc that avoids `v`. That subarc lies
in layer `m` by the assumed cyclic layer order. No source point is added at `z`.

An actual diameter not incident to `v` must meet each witness: properly if
vertex-disjoint, or at its partner if it shares that partner. It cannot be `p-p+`,
whose length is `2D sin(theta/2)<D`. The two intersection points lie on the two
opposite sides of the interior ray in the witness sector. The intervening diameter
subsegment crosses the positive ray. The intersection cannot be `v`, since an
extreme hull vertex cannot lie in the interior of a source chord. It lies in
`[v,z]` by convexity.

The supporting line through `v,z` intersects the hull exactly in `[v,z]`, with
the segment interior in the hull interior. A nonparallel diameter meeting the
line therefore has endpoints on opposite sides, or one endpoint at `z`.
An actual diameter parallel to the line would need both extreme endpoints on it,
so the only possibility is `vz`. If `z` is auxiliary, that diameter does not exist.

Thus the two hull arcs `L,U` from `v` to `z` contain the two physical ends of every
nonzero row. Their layers increase from `0` to `m`. An edge incident to `v` is
assigned to the appropriate arc closure; `v` and `z` are the only points common
to those closures. This proves the claimed extension for an open witness cell as
well as for a threshold cell. No actual diameter parallel to `u` is required.

## 3. Independent positive-circulation and staircase proof

For endpoint layers `a<b`, the row is
`(n_h dot Ju) 1_(a,b]`. Discrete differences take its interval indicator to
`e_a-e_b`. Consequently the projected balance `beta^T M=0` is exactly a positive
directed circulation when the physical lower end points toward the physical upper
end and its flow is `beta_h |n_h dot Ju|`. The sign of the layer increment accounts
for the orientation reversal; an original multiplier is not replaced by a
rescaled multiplier in any later axial-force calculation.

Consider a simple directed cycle with distinct levels `k_i` and physical edges
`L_(k_i) U_(k_(i+1))`. Proper crossing of consecutive disjoint bars reverses the
two arc orders, so consecutive layer increments have opposite signs. If two bars
share an endpoint across the arc closures, that endpoint is `v` or `z` and its
level is an extreme; the same sign alternation follows. Thus the cycle is even.

Its minima `a_i` and maxima `b_i` are distinct. The physical edges `L_(a_i) U_(b_i)`
have disjoint endpoints and cross pairwise, so their matching reverses order.
The other half of the cycle also gives an order-reversing matching. Their
composition is an order-preserving permutation of the finite set of minimum
levels; such a permutation fixes every level. That composition is also the
cyclic shift, forcing just one minimum and hence a two-cycle.

A finite positive circulation decomposes into simple cycles by following positive
flow to a repeated vertex and subtracting its minimum flow. Every subtraction
removes an edge, so it terminates. Every used interval therefore has both physical
orientations and equal total transverse flow in the two orientations.

For two distinct intervals `(a,b),(c,d)` with `a<c`, the positive physical bars
would have nonalternating endpoints if `b<d`; those bars have distinct endpoints,
so this is impossible. Thus `b>=d`. All intervals share a cut index `r`, connecting
the gap parts `{0,...,r-1}` and `{r,...,m}`. The elementary antitone counting bound
gives at most `m` distinct cells: within each left-coordinate block the number of
right coordinates is at most its range plus one; those ranges telescope, yielding
at most `(m-r)+r=m`.

Full row rank gives connectivity on `m+1` vertices and at least `m` simple edges.
Equality follows. Order these cells by increasing left and decreasing right
coordinate. Changing both coordinates between consecutive cells separates all
earlier endpoints from all later endpoints and disconnects the graph. Skipping a
coordinate leaves that gap vertex isolated. Consequently the cells form the unit
staircase from `(0,m)` to `(r-1,r)` and there are exactly `m` of them.

This is the collapsed graph. Each cell has at least two distinct physical bars,
so the full support contains at least `2m` nonzero rows and is not a simple tree.
A spanning-tree leaf supplies no private full-system diameter row. Stars and paths
in the collapsed graph are allowed, and no diameter Euler path is inferred.

## 4. Determinant proof of original axial positivity

The convex-order determinant step can be made explicit. Suppose four endpoints
`A,B,C,E` occur in positive hull order and the actual bars `AC`, `BE` cross at `X`.
Write `X-A=t(C-A)` and `X-B=s(E-B)`, with `t,s>0`. Since `A,B,X` is positively
oriented,

```math
0<\det(B-A,X-A)=ts\det(C-A,E-B).
```

If two relevant bars share one endpoint, the corresponding determinant is the
positive area determinant of the remaining hull triangle. It is strict because
three distinct extreme vertices cannot be collinear. This establishes the direction
order without assuming monotone axial coordinates on the hull arcs.

For a cell `(a,b)`, its positive physical vector `L_a -> U_b` has angle `alpha`
and its reverse physical vector `L_b -> U_a` has angle `gamma`, both in `(0,pi)`.
The cyclic order is `L_a,L_b,U_b,U_a`; the determinant argument gives `alpha<gamma`
for every pair of representatives, including the shared `v` or `z` cases.

With the original positive transverse flow `f_h=beta_h D sin(angle_h)`, the
original layer-oriented axial resultant is

```math
R_{ab}=\sum_+f_h\cot\alpha_h-\sum_-f_h\cot\gamma_h.
```

The two flow masses are equal and positive. Product-coupling their normalized
measures expresses this resultant as their common mass times an average of
`cot(alpha)-cot(gamma)>0`. Therefore `R_ab>0`. This proves original axial
positivity, rather than positivity of an independently reweighted toy stress.

If the actual contact-cut law is supplied, it gives
`A_i=R_0+sum_(a<i<=b) R_ab`, where `R_0>=0` is the optional `vz` contribution.
For `i<r`, the difference `A_(i+1)-A_i` is the positive sum of bundles starting
at gap `i`; for `i>=r`, `A_i-A_(i+1)` is the positive sum ending there. Connectivity
makes every relevant sum nonempty. Strict unimodality follows. Without the actual
contact-cut law, these are only formal diameter cut masses.

## 5. Universal representative order and a sharper angular budget

For consecutive staircase cells, one layer coordinate changes strictly and the
other stays fixed. Compare any positive physical representatives. If the fixed
coordinate labels distinct source endpoints, proper crossing forces the required
endpoint order inside that same layer. If it labels the same endpoint, the shared
endpoint triangle gives the same strict determinant. Applying the argument in
the reverse order to the negative representatives gives

```math
\alpha_1<\cdots<\alpha_m<\gamma_m<\cdots<\gamma_1
```

for **every** selection of one bar in each orientation bundle. A common layer
does not prescribe an order among its vertices; crossing supplies that order
when needed. This addresses the strongest quantifier in equation (8).

The projective direction-spacing bound also survives re-derivation. For shared
endpoints, partner separation gives `2D sin(epsilon/2)>=1`. For disjoint bars,
orient the two vectors at their minor projective angle `epsilon`, and denote
the midpoint difference by `d`. The two far cross-distances have squared average

```math
|d|^2+D^2\cos^2(\varepsilon/2)\le D^2.
```

The two near cross-distances have squared average
`|d|^2+D^2 sin^2(epsilon/2)>=1`. Combining them gives the stronger disjoint bound
`epsilon>=2 asin(1/(sqrt(2)D))`. In particular every distinct pair of actual
diameter directions has spacing at least

```math
\delta_D=2\arcsin(1/(2D)).
```

Every positive angular difference appearing above is at least `delta_D`, even if
its minor projective representative is its complement. Hence the PR's equation (9),
`Theta_t>=Theta_1+2(t-1) delta_D`, follows.

There is also a small additional bound, classified as a **proved candidate awaiting
promotion**. Apply the spacing bound to the central pair `alpha_m,gamma_m`, as well
as the other `2(m-1)` increments. Since `Theta_1=pi-gamma_1+alpha_1`,

```math
\boxed{\Theta_1+(2m-1)\delta_D\le\pi,\qquad
       (2m-1)\delta_D<\pi.}
```

If the central pair has distinct endpoints, replace that central `delta_D` by
`2 asin(1/(sqrt(2)D))`. These inequalities improve the finite angular budget; they
do not contradict a retained shore of size `c_*D` with small `c_*`. No global
closure is obtained from them.

## 6. New exact regressions beyond the original seven-point source

Classification: **regression**. Put `s=sqrt(42)`, `t=sqrt(165)`, `D=13`, `u=(1,0)`.
Use the nine points

```math
\begin{split}
v&=(0,0),&p^\pm&=(12,\pm5),\\
L_1&=(6,-s),&U_1&=(6,s),\\
L_2&=(7,-s),&U_2&=(7,s),\\
L_3&=(8,s-t),&U_3&=(8,t-s).
\end{split}
```

Their strict hull order is `v,L1,L2,L3,p-,p+,U3,U2,U1`. All 36 pair distances
lie in `[1,13]`. The only unit contacts are `L1L2,U1U2`. The six actual diameters
are `vp-,vp+,L1U2,L2U1,L1U3,L3U1`. Assign levels `0` to `v`, `1` to `L1,U1`,
`2` to `L2,U2`, and `3` to the remaining points. Weights `beta=1/6` give exact
projected balance, rank three, and staircase cells

```math
(0,3),\quad(1,3),\quad(1,2).
```

Their axial resultants are `4,2/3,1/3`; their formal cut masses are
`4,5,14/3`, realizing a strict interior peak. The direction order is checked by
exact determinants. The witness ray exits at the auxiliary midpoint `(12,0)`.

Coarsening levels `2,3` to one level gives an `m=2` example with two representatives
in each orientation of the `(1,2)` bundle. All four choices satisfy the universal
order. Thus neither same-layer multiplicity nor an interior staircase peak supplies
a counterexample to the audited lemma.

Adding the tenth point `z=(13,0)` preserves the two unit contacts and six nonparallel
diameters and adds the single parallel diameter `vz`. Strict hull convexity and all
45 pair-distance constraints hold. The exit is now an actual source point. Equal
weights `1/7` give formal three-cut masses `37/7,43/7,41/7`; both the three-layer
and coarsened two-layer checks pass.

These sources explicitly fail the missing source assumptions. The first contact
cut is empty, but its formal diameter mass is positive; for the three-cut assignment
the last contact cut is also empty. The actual cut-contact counts are `0,2,0`,
not the positive formal masses. Thus **no contact multipliers** can supply the
claimed actual cut law for these layer assignments. Moreover `v` has no unit
contact and both incident nonparallel diameter vectors have axial component `12`.
Every positive weighting leaves an unbalanced axial force at `v`. This is a
full-source KKT obstruction, not merely a failure of the equal test weights.

These are feasible triangle-free sources, not global minimizers. Their complete
transverse train grids, mixed rigidity and global-optimality certificates do not
exist in this audit. They reject the stronger implication
`projected circulation + labeled staircase -> actual source KKT/cut equilibrium`.

## 7. Computation and adversarial checks

The original packet's exact script was rerun successfully. Its 21-distance source
regression and 33,866 simple-graph checks reproduce the reported output.

The independent certificate is
[`verify_target_c_star_ray_hostile_audit_2026_10_01.py`](../../../research/verify_target_c_star_ray_hostile_audit_2026_10_01.py).
It uses exact rational arithmetic in `Q(sqrt(42),sqrt(165))`. Sign decisions use
rational radical enclosures certified with integer square roots; no floating-point
distance or determinant is used. All four source/layer combinations pass, including
all representative choices, exact rank, projected cancellation, original axial
resultants, strict convexity, actual edge sets and the source-KKT/cut-law failures.

It also enumerates every directed simple cycle on two through eight ordered gap
vertices, counting cycles up to cyclic rotation. The necessary endpoint relation is
`(a-c)(b-d)<=0` for every pair of physical arcs `L_a U_b`, `L_c U_d`. It inspects
`1,5,20,84,409,2365,16064` cycles respectively, totaling 18,948. Only the
`choose(n,2)` two-cycles survive for each `n`; no longer cycle survives. This is
an independent finite hostile check, not the proof for arbitrary gap populations.

Commands:

```sh
python3 research/verify_target_c_star_ray_staircase_2026_10_01.py
python3 research/verify_target_c_star_ray_hostile_audit_2026_10_01.py
python3 tools/build_artifact_index.py --write --write-headers
/tmp/e99-gap-reaction-venv/bin/python tools/check_theorem_state.py --base-ref 87375fe0
git diff --check
```

All checks pass. The theorem-state checker uses the existing dependency environment;
the bare system interpreter lacks `jsonschema`. The generated artifact update adds
one unreviewed report entry/header and changes no theorem manifest or state view.

No local/jammed source is called globally optimal. Equal-layer and zero-transverse
diameter rows remain in the source even when removed from `M`. The auxiliary ray
exit is never counted as a source point. No active row is inferred from a near-active
pair, and no infinitesimal deformation is claimed to integrate.

## 8. Disposition and exact remaining gap

| Claim | Audit disposition | Exact limit |
| --- | --- | --- |
| Ray anchor in an open witness cell | audited-working | Explicit full-span bracing star and cyclic layer order |
| Two-cycle circulation and doubled staircase | audited-working | Positive projected balance and full derivative rank |
| Original axial resultant `R_ab>0` | audited-working | Actual original diameter weights, with transverse bundle balance |
| Strict actual cut-contact unimodality | conditional | Requires the actual source contact-cut law; projected balance does not supply it |
| Universal representative order and cone widening | audited-working | Convex equal-diameter chord geometry; no axial-coordinate monotonicity assumption |
| Sharpened angular budget | proved candidate awaiting promotion | Same explicit geometric hypotheses |
| Nine-/ten-point sources | regression | Geometry and projected balance hold; actual source KKT/cut law fail |
| Complete C-II application | conditional | Unpromoted train/extraction chain and actual transverse shore remain to be audited/used |
| C-II or Level I settlement | not proved | Other global branches survive |

No substantive defect was found in PR #597's explicit geometric theorem.
Recommendation: retain it as audited-working with its scope attached; do not promote
a universal C-II conclusion. The new angular budget is a separate proved candidate.
This branch makes no theorem-state lifecycle or frontier promotion.

The next obligation is to prove that the **actual** complete transverse train shore,
full vertex KKT equilibrium and source lexicographic minimality contradict this
labeled staircase, or construct a finite source-preserving strict sub-`D` competitor.
The formal masses in realizable projected examples cannot substitute for that law.
Nonconstant-phase TB1, split-star O--O, inactive-interface and macroscopic inactive
container/exterior-cap branches remain open.

Read next: the audited packet and its four October 1 dependency reports listed in
Section 1, with the actual contact-cut law and complete transverse shore kept explicit.
