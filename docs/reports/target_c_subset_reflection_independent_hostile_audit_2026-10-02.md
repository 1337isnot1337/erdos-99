<!-- theorem-state: {"artifact_id":"ART-ED87C16728B2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- independent hostile audit of subset reflections

Date: 2026-10-02. Audited packet: PR
[614](https://github.com/1337isnot1337/e-99/pull/614), exactly
`a36a12d60e768ddd68ec3db8267621e22765432e`.
State version: `2026-09-14.audit.51`.
Audit branch: `audit/c2-subset-reflection-20261002`.
Run type: independent proof/scope audit and exact regression.
Active prompt: [current Target C continuation](../prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md).
External literature imports: none. Computation: exact rational certificates and
small finite graph enumeration.

**Level I and C-II remain open.**

Disposition: the packet's finite statements **PASS at the explicit nonempty
cutset, narrow-span, empty-cell scope**. The source application remains
**conditional** on its unpromoted train/cutset extraction and multishear identity.
The packet's geometric/aggregate-force regression is valid. Section 3 below adds
an **unreviewed candidate** structural reduction of a strongly connected
open-cell block; Section 4 adds an exact **regression** with actual contacts and
a complete transverse grid. No canonical promotion is made.

```text
subset reflection -> exact contact preservation and finite old-diameter signs
 -> strong-connectivity obstruction
 -> paired antitone gap tree and physical rail splitting
 -> closing theorem still needs both-shore/full-source KKT and strict-pair control.
```

## 1. Authority and audit boundary

The authority files, exact global quantifiers, live Target C route, named active
module scopes, workflow, and current prompt were inspected before selecting the
new bridge. Detailed dependencies of this audit are:

| Input | Authority and use |
| --- | --- |
| [C-I normal form](../targets/target-c/56-ci-restored-frontier.md) | Canonical: contact-minimal then diameter-pair-minimal representative; positive relative-interior support. |
| [ZR/ZF](../targets/target-c/57-zr-zf-rigidity-audit.md) | Canonical, restricted to the nonisolated core; no full-source extension is used. |
| [Diameter thrackle / C-WOODALL](target_c_woodall_diameter_topology_2026-09-10.md), Section 1 | Canonical: diameter endpoints are extreme; vertex-disjoint diameter bars cross; a bipartite diameter subgraph is a forest. |
| [Laminar exact shear](../../research/target_c_laminar_multitrain_interval_shear_2026-09-15.md) | Unpromoted: the physical ordered contact cutsets and full-source layer coordinates are hypotheses here. |
| [Multishear hostile audit](../../research/target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md), Sections 2, 6--7 | Proof-only audited scope: sign-correct cut resultant and finite translation superposition. |
| [Witness-cell extraction](target_c_local_witness_cell_2026-10-01.md) | Unpromoted: full-support common star witnesses are explicit hypotheses of Section 3. |
| [Four-host joint-switch theorem](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md) | Unpromoted: used only for the conditional transverse-rail conclusion. |

This audit does not promote the extraction ancestry or independently certify its
population constants. It audits the finite bridge with the required geometry
supplied as hypotheses. No other open PR supplies a premise.

## 2. Audit of the packet

### 2.1 Exact reflection and displacement

For selected cuts `I`, the resultant `U=sum u_i` is nonzero because their coherent
angular span is less than `pi/2`. With `e=U/|U|`, `w=Je`, and `a_i=u_i dot w`,
the selected increments `-2a_i w` reflect the unit vectors and sum to zero.
Every old contact changes by exactly its own cut increment, or is unchanged.
This step requires each contact to cross at most one selected cut, as the packet
states; arbitrary ordered partitions do not supply that property.

Writing `T=sum_{a_i>0}a_i=-sum_{a_i<0}a_i`, every prefix and every interval sum
lies in `[-T,T]`. The pair-relative bound is therefore `2T=sum |a_i|`, not twice
that quantity. The packet's displacement estimate is correct.

### 2.2 Finite sign threshold

Let `alpha<mu<beta` be the selected extremes and resultant angle, and put
`g=min(mu-alpha,beta-mu)`. The old actual diameter directions are outside the
open interval containing these extremes. In projective angular distance this
gives `|r dot w|>D sin g`, including diameters at the actual cell boundaries.
No condition on the reflected directions is needed.

On whichever side of `mu` has angular width `g`, each sine magnitude is at most
`sin g`, and at most `k-1` terms occur. Hence `2T<=2(k-1)sin g`. For a nonzero
relative displacement `lambda w` and `D>=k-1`,

\[
|\lambda|\le2T\le2(k-1)\sin g\le2D\sin g<2|r\cdot w|.
\]

The strict final inequality handles equality at `D=k-1`. Therefore
`lambda(2 r dot w+lambda)` has the sign of `lambda(r dot w)`.
The packet's linear threshold and exact full-endpoint work sign pass.
The verifier checks examples; the general statement is proved by this inequality.

### 2.3 KKT fork and one-axis classification

The signed cut identity gives the exact finite work identity

\[
\sum_h\beta_h r_h\cdot\Delta_h
=-2\sum_{i\in I}A_i a_i^2<0.
\]

Positive contact mass on every selected cut is required for strictness. If no old
diameter lengthens and every previously strict pair remains in `(1,D)`, the
endpoint has the same contact graph and fewer diameter pairs, or diameter less
than `D`. Triangle-freeness is preserved because the contact graph is unchanged.
The contact/diameter lexicographic contradiction and slack witnesses pass.
There is no asserted feasible interpolation.

For a fixed unit displacement axis `w`, contact preservation at cut `i` is
`d_i(d_i+2u_i dot w)=0`. Fixed exteriors force the selected changed-cut resultant
to be perpendicular to `w`. Under the same narrow-span hypothesis it is nonzero,
so the reflection axis is its direction. This proves the classification.

One hypothesis should be stated explicitly if Theorem 4 is reused outside actual
train scope: **every indexed cut has an old contact across it**. Otherwise the
quadratic equation cannot be imposed at an empty cut. For example, three points
`(0,0),(10,0),(20,0)` in layers `0,1,2` have no contacts. Translating only the
middle point by `(0,1)` fixes the exteriors and preserves all old contacts but is
not a subset reflection for `u_1=(1,0)`, `u_2=circle(1/100)`. Along the vertical
axis the permitted reflection increments are zero or negative, so cannot sum to
zero nontrivially. The certificate checks this exactly. This is a scope warning,
not a counterexample for nonempty actual stopped-train cuts.

The narrow-span assumption is also necessary for the proof of nonzero `U`;
an arbitrary family with opposite directions can have `U=0`. The theorem is not
an unrestricted classification of contact-preserving motions.

### 2.4 Gap obstruction and original regression

No positive work means `x_head<=x_tail` on every signed gap edge. Strong
connectivity makes `x` constant; a nonzero fixed-exterior motion cannot satisfy
this. Applying the same argument to `-x` yields negative work as well. The finite
sign theorem then supplies both strict diameter signs. No KKT hypothesis enters
this graph argument.

The original rational star regression passes independently: all nonstar pairs
are strictly between `1` and `D`, cut weights are positive, the resultant
telescopes, the derivative matrix has rank `m`, and prefix domination proves the
formal scalar cut form positive. Its lack of actual contacts and vertex KKT is
correctly disclosed. The exact nonpermutation example creates three fresh phase
directions. The original certificate was rerun successfully.

## 3. A sharper open-cell structural reduction

**Classification: unreviewed candidate, with a complete proof below.**

Assume the packet's ordered proper crosscuts and an open cell `J`. Additionally
assume two full-support actual diameters `vp^-`, `vp^+` from one common source
vertex `v`, with coherent ray directions bounding `J`. Relabel the layers so
`v` is in layer `0` and both other endpoints are in layer `m`. Choose `e` inside
`J` and set `w=Je`. Suppose the signed gap graph on all `m+1` layers is strongly
connected. No exact-phase or KKT-circulation hypothesis is imposed.

Then:

1. every simple directed gap cycle has length two;
2. every unordered gap edge has both physical orientations;
3. the collapsed simple gap graph is an antitone spanning tree with `m` edges,
   containing `{0,m}`; all its support intervals contain one common cut;
4. its interval lengths sum to `m(m+1)/2`;
5. selecting one actual bar in each orientation gives `2m` distinct diameter
   bars, all crossing that common cut, with total A-support incidence `m(m+1)`;
6. the selected physical graph `F` is a caterpillar forest. If it has `c(F)`
   nontrivial components and `n_j` selected vertices in layer `j`, then

\[
|V(F)|=2m+c(F),\qquad n_0\ge1,\qquad n_j\ge2\ (1\le j\le m),
\]

and hence

\[
\boxed{(n_0-1)+\sum_{j=1}^m(n_j-2)=c(F)-1.}
\tag{A}
\]

Under the additional four-host complete transverse-shore hypothesis, each
internal A-layer `1,...,m-1` has selected endpoints on both extreme B rails.
Each such rail therefore contains at least `m-1` selected diameter endpoints.

### Proof

Intersect the ray from `v` in direction `e` with the convex source-hull boundary
again at `q`. It falls in the boundary arc between `p^-` and `p^+` not containing
`v`. An actual diameter with a non-witness endpoint in the open arc
`(p^-,p^+)` cannot cross both witness diameters: whichever of the two remaining
boundary arcs contains its other endpoint, one witness is not crossed. Shared
endpoints only exempt that one witness. The diameter-thrackle rule therefore
excludes such a diameter. Also `vq` is not a diameter because its direction is in
the empty cell. Thus `q` is not an actual diameter endpoint, even if it is a
source vertex.

Split the hull boundary at `v,q` into arcs `L,U`. Convexity puts their open arcs
in opposite half-planes of the line in direction `e`; label `U` the positive
`w` side. Every actual diameter lies between these arcs, allowing `v` as a
shared endpoint. Each selected crosscut separates `v` from both witnesses, so
its terminals cannot lie between `p^-` and `p^+`. It has one terminal on each
of `L,U`; their layer orders are nondecreasing from `v` toward `q`, and `q` is
in layer `m`. The positive transverse orientation is exactly `L_a -> U_b`.

For a simple directed cycle, physical bars therefore have the form
`L_{k_i}U_{k_{i+1}}`. Two consecutive vertex-disjoint bars must cross. Since
layer order is monotone along both arcs, successive layer differences have
opposite signs. If consecutive bars share a source endpoint, that endpoint lies
on both arcs; it must be `v`, whose layer `0` is a strict minimum. Thus cycle
levels alternate strict minima `a_i` and maxima `b_i`.

The even bars give a strictly order-reversing bijection `a_i -> b_i`: their
endpoints have distinct layer labels and cannot coincide, so crossing gives
strict reversed order. The odd bars similarly give an order-reversing bijection
`b_i -> a_{i+1}`. Their composition is an order-preserving permutation of a
finite ordered set, hence the identity, while it is also the cyclic shift.
Only one minimum and one maximum can occur. Every simple directed cycle has
length two.

Every edge of a finite strongly connected directed graph lies in a simple
directed cycle. Consequently every unordered gap edge has both orientations,
represented by distinct physical bars `L_aU_b` and `L_bU_a` for `a<b`.
For two simple edges `(a,b),(c,d)` with `a<c`, the bars `L_aU_b,L_cU_d`
would be disjoint and noncrossing if `b<d`. Hence `b>=d`: the family is antitone.
All half-open intervals `(a,b]` intersect pairwise. One-dimensional Helly gives
one common cut index.

To count edges, list distinct left endpoints `a_1<...<a_s`, and let `B_i` be
their right-neighbor sets with minimum `t_i` and maximum `M_i`. Antitonicity
gives `t_i>=M_{i+1}`. Therefore

\[
|E|\le\sum_i(M_i-t_i+1)\le M_1-t_s+s\le m,
\]

because `M_1<=m` and `t_s>=a_s+1>=s`. Connectivity gives at least `m` edges,
so equality holds throughout and the simple graph is a tree. The two common
witnesses supply `{0,m}`. Equality also gives
`a_i=i-1`, `B_i={t_i,...,t_{i-1}}`, and
`t_0=m>=t_1>=...>=t_s=s`. Summing `b-(i-1)` over those intervals telescopes to
`m(m+1)/2`. Doubling gives the physical support-incidence count.

All selected bars cross one proper cut, making `F` bipartite. The diameter
thrackle theorem excludes even cycles, so `F` is a forest; the canonical
straight-line thrackle classification makes its components caterpillars.
Forest counting gives `|V(F)|=2m+c(F)`. Every positive layer is incident with
a simple tree edge and has a selected endpoint on each of `L,U`. They are
distinct because these arcs meet only at `v,q`, and `q` is not a diameter
endpoint. Layer zero is occupied. Subtracting `1+2m` proves (A).

Finally the four-host theorem puts every hull endpoint with internal A-layer
on an A-host interval, where the B-layer is `0` or `n`. The two arcs carry
opposite A-host intervals, proving the conditional rail statement. QED.

This extends the structural mechanism of the
[threshold paired-staircase report](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md)
to a strongly connected nonconstant open-cell block. The parallel reference
diameter is replaced by two common star witnesses; strong connectivity replaces
the exact-phase positive circulation. Neither old theorem is imported as a
premise. The physical selected-edge count is `2m`, not the threshold report's
`2m+1`, and equation (A) has `c(F)-1` rather than `c(F)+1`.

## 4. Actual contacts and a complete transverse grid still allow the obstruction

**Classification: exact regression to co-embedding plus A-aggregate-force
closure; not a regression to full-source KKT or global optimality.**

Retain the packet's `D=100m`, star points `p_j,n_j`, directions `u_i`, and
positive diameter coefficients `gamma_j^+,gamma_j^-`, for every `m>=2`.
Write `S_a=sum_{i<=a}u_i`, `S_0=0`, and set

\[
b=(8/17,15/17),\qquad q_{a,t}=S_a+t b\quad(0\le a,t\le m).
\tag{B}
\]

Add this entire actual contact grid to the source, identifying `q_{0,0}=v`.
Give `q_{a,t}` A-layer `a`, and retain A-layer `j` for `p_j,n_j`. Give grid
points B-layer `t`, all upper fan points B-layer `m`, and lower fan points
B-layer `0`. All source points are retained.

The contact graph consists exactly of adjacent row and column edges. For each
`i`, `0<u_i dot b<1/2`, so every crossing is a strict triangle-free unit
rhombus. If a grid pair differs by at least two B-steps, its transverse
separation exceeds one; if it differs by zero B-steps and at least two A-steps,
its longitudinal separation exceeds one. With one B-step, opposite one-step
A-diagonals have squared length `2-2u_i dot b>1`; at least two A-steps again
give longitudinal separation greater than one. These bounds exclude every
extra unit contact.

Each fan point is at distance at least `D-2m>1` from the grid. For a fan unit
ray `r`, every row increment has `r dot u_i>1/4` and `r dot b>1/4`. For
`q=q_{a,t}!=0`, write `l=a+t<=2m`; then

\[
|Dr-q|^2-D^2\le-\tfrac12Dl+l^2<0.
\]

Grid-grid distances are below `D`, and the old fan-fan distances retain the
packet's bounds. Thus the actual diameters are still exactly the `2m` star
bars. All actual contact and diameter claims are checked pair by pair in the
independent certificate, not inferred from a selected list of edges.

The A-train midpoint curves of this embedded grid are pairwise disjoint; the
B-train midpoint curves are pairwise disjoint; every A-curve crosses every
B-curve once. They terminate on the grid's outer contact-face boundary. Extend
them through its contact-free exterior to the source hull, preserving cyclic
terminal order. The A-terminals occupy the two fan arcs in the order of the
indices `j`; the B-terminals occupy the left grid rail and the hull interval
between the two innermost fan points. Noncrossing extensions with these orders
exist in the intervening disk regions. They give the indicated physical layers
and the same four alternating host intervals. No contact edge is crossed by an
extension. The actual A-cut contact edges are exactly its `m+1` row edges;
the actual B-cut contacts are exactly its `m+1` column edges.

Assign each A-cut edge mass `(m-i+1)/(m+1)`, positive. Its total actual contact
reaction is then `(m-i+1)u_i`, matching the packet's positive diameter
resultant. This supplies genuine contact cutsets and A-cut aggregate balance,
not merely fictitious contact vectors. Arbitrary positive B-contact masses
can be assigned, but they will not satisfy source KKT.

The A gap graph is still the bidirected star and is strongly connected. Every
nonzero subset reflection preserves **all actual grid contacts** and has both
strict diameter signs. Its derivative rank and formal A-cut quadratic form are
unchanged. It realizes the Section-3 tree and equation (A) with `c(F)=1`.
The complete transverse grid therefore does not by itself remove the obstruction.

### The exact missing transverse identity

For every B-cut the positive diameter resultant is the same vector

\[
R_B=\sum_j\gamma_j^+p_j.
\]

It is in the cone of the upper star rays, of aperture at most `2 atan(1/10)`
above the positive horizontal axis. The actual B-contact direction `b` lies
above `pi/3`. Hence `det(b,R_B)<0` and no positive scalar `A_B` satisfies
`A_B b=R_B`. The certificate verifies this nonzero determinant exactly.
There is also no vertex KKT at any fan point: it has no contacts and exactly
one positive diameter force. Full source stress/PSD is absent.

The source is not globally optimal. Its population is `N=(m+1)^2+2m`; a unit
square lattice with side `m+2` holds at least `N` points and has squared diameter
`2(m+2)^2<D^2`. Taking any `N` of those points is a strict competitor.
Near-disk geometry, a canonical quadratic-density source, both-shore common
star bracing, and the asymptotic source star-degree bound are not supplied.

## 5. Certificate and validation

The independent certificate is
[verify_target_c_subset_reflection_hostile_audit_2026_10_02.py](../../research/verify_target_c_subset_reflection_hostile_audit_2026_10_02.py).
It uses exact rational arithmetic for `m=2,3,4,5,6,7,8,12,16` and checks:

- 81,249 source pairs, identifying exactly 1,332 actual contact edges across
  the packets and 603 actual strict rhombi;
- every actual diameter and positive A-cut balance, derivative rank, formal
  scalar prefix domination, and the exact failure of B-cut KKT;
- 472 subsets, exhaustive for `m<=8`, and 6,860 full finite diameter signs;
- the empty-cut scope regression;
- every connected antitone `m`-edge family for `m<=6`, yielding respectively
  `1,2,4,8,16,32` trees and verifying the common-cut and incidence identities.

These finite checks do not prove the Section-3 general theorem; its proof is
above. Nor do they encode source optimality, full vertex equilibrium, or a
canonical population/near-disk branch. The missing hypotheses are tested as
failures, not silently discarded.

Commands and final repository checks are recorded in the audit PR. The system
Python lacks `jsonschema`; theorem-state validation uses the existing
`/tmp/e99-gpt6-theorem-venv/bin/python`. This environment change does not alter
mathematical inputs.

## 6. Frontier effect and remaining obligation

The audited finite packet survives with its stated actual train scope. The
nonempty-cut condition should travel with its classification theorem. A strongly
connected common-witness block now has an exact paired antitone tree, a common
cut load of `2m` bars, and the physical splitting identity (A), even with
nonconstant phases. This is a structural narrowing, not a diameter descent.

A closing statement must exclude or release that paired antitone tree **under
simultaneous actual A- and B-cut resultants, full vertex KKT, the source
core/geometry/population constraints, and every strict-pair constraint**. Adding
an embedded strict-rhombus grid while using only the A-cut resultant is
insufficient by Section 4. The transverse force identity is a concrete required
bridge, not an optional strengthening.

The one-axis family cannot yield a release on the strongly connected block.
An internal-A to internal-A bar has both endpoints on extreme B rails and remains
unchanged under fixed-exterior B reflections. A successful motion must handle
those bars, open or replace contacts, or leave the fixed-exterior two-shore class.
The inactive-interface, split-star, macroscopic-container and higher-defect
branches remain uncovered.

Promotion recommendation: **audited-working at the explicit finite scope** for
the original packet; preserve the new structural reduction as an **unreviewed
candidate** and the contact-grid construction as a **regression**. No manifest
theorem, route map, current prompt, or state version is changed by this audit.
