> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_rail_deep_attachment_2026-10-02.md) · source SHA-256 `70525a68adcaa926e4c7167639f33f7e5cf4fd93684adcdcc4d39b32bc363d55`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5DAC484CA164","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — threshold rails force two quadratic source caps and deep attachments

```text
diameter-endpoint strip capacity -> quadratic area and source population in
each actual threshold rail hull, plus many macroscopic attachment depths
versus any specified straight row -> target: couple
those actual caps and deep attachments to source stress/face currency or a strict
same-cardinality competitor -> C-II branch exclusion -> Level I only after
every other source branch is covered.
```

**Date:** 2026-10-02.  
**Starting commit:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.  
**State version:** `2026-09-14.audit.51`.  
**Branch:** `swarm/threshold-flux-curvature-20261002`.  
**Mission:** actual contact geometry and positive reactions in the threshold
exact-phase staircase, beyond support-row counting.  
**Classification:** unreviewed candidate, with an exact regression against
interior-pressure-only closure.  
**External literature:** not used.  
**Computation:** exact Fraction certificates; the general proofs do not depend
on enumeration or numerical survival.

**Level I OPEN. C-I CLOSED. C-II OPEN.**

## 1. Authority and inspected inputs

Canonical source interpretation uses:

- [KKT equilibrium and actual diameter endpoints](../theory/01-local-structure.md),
  Theorem 4.1 and Lemma 5.1;
- [C-I normalization](../targets/target-c/56-ci-restored-frontier.md);
- [core rigidity](../targets/target-c/57-zr-zf-rigidity-audit.md), only on the
  nonisolated positive-contact core;
- [full-source geometry](../targets/target-c/58-full-source-geometry-audit.md),
  with every isolated source point retained;
- [finite Oler inequality](../theory/03-oler-shell.md), Lemma 21.1, for the
  new source-population consequence;
- [complete-grid extraction](../targets/target-c/73-pseudosegment-grid-extraction-audit.md),
  [phase collapse](../targets/target-c/74-complete-grid-phase-collapse-audit.md),
  and [hole-stable order](../targets/target-c/76-hole-stable-complete-grid-order-diameter-audit.md).

The October threshold application is conditional on these unpromoted reports:

- [paired staircase](target_c_exact_phase_threshold_paired_staircase_2026-10-01.md);
- [physical forest lift](target_c_exact_phase_threshold_forest_lift_2026-10-01.md);
- [transverse rail saturation](target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md);
- [joint switches and four hosts](target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md).

The remote star-ray axial-reaction report on
`origin/swarm/root/c2-gap-reaction-20261001` and nested-bundle report on
`origin/swarm/sol/gap-stress-cycle-20261001` were inspected at their explicit
scopes. They already give positive bundle reactions, a unimodal pressure profile,
and local train-chart isolation. We do not claim another basis-leaf release.
The three `research/exact-phase-threshold-edgewise-flux-packets-2026-10-02*`
remote branches inspected at startup all pointed to the starting main commit;
no additional packet was imported from them. This statement is a dated snapshot.

## 2. Diameter-endpoint strip capacity

This theorem is independent of minimization, KKT, unit separation, hull
roundness, thrackle structure, and the October extraction chain.

### Theorem 1

Let a finite planar set `P` have diameter `D>0`. Let `Q` be any subset of its
**actual diameter endpoints**: for each `q` in `Q` there is `p` in `P` with
`|p-q|=D`. Let `u` be a unit vector. Suppose `Q` is contained in a strip of
transverse width `t`, and put

```math
x_0=\min_{q\in Q}q\cdot u,\qquad
x_1=\max_{q\in Q}q\cdot u,\qquad L=x_1-x_0.
```

Every `q` in `Q`, with `x=q dot u`, satisfies

```math
\boxed{(x-x_0)(x_1-x)\le 2Dt.} \tag{1}
```

In particular, its projection belongs to the union of the two intervals

```math
\boxed{
[x_0,x_0+\sqrt{2Dt}]\ \cup\
[x_1-\sqrt{2Dt},x_1].}
\tag{2}
```

When `t=0`, this recovers the exact fact that a line contains at most two
distinct actual diameter endpoints of a finite planar diameter-`D` set.

### Proof

The case `L=0` is immediate. Choose `q_0,q_1` attaining the projection
extrema. For `q` with projection `x`, put

```math
\lambda={x-x_0\over L},\qquad
q_*=(1-\lambda)q_0+\lambda q_1.
```

The vectors `q` and `q_*` have equal projection onto `u`. Since both transverse
coordinates lie in the same width-`t` strip,
`|q-q_*|<=t`. Choose an actual diameter partner `p` of `q`. The exact
weighted-square identity gives

```math
\begin{aligned}
D^2
&\ge (1-\lambda)|p-q_0|^2+\lambda|p-q_1|^2\\
&=|p-q_*|^2+\lambda(1-\lambda)|q_1-q_0|^2.
\end{aligned}
\tag{3}
```

Writing `e=q_*-q` and using `|p-q|=D`,

```math
D^2-|p-q_*|^2
=2(p-q)\cdot e-|e|^2\le2Dt.
\tag{4}
```

Also `|q_1-q_0|>=L`, so (3)--(4) yield

```math
(x-x_0)(x_1-x)=\lambda(1-\lambda)L^2\le2Dt.
```

If `s=min(x-x_0,x_1-x)`, the other factor is at least `s`, and therefore
`s^2<=2Dt`. This proves (2). No source point or diameter partner is removed.

## 3. Capacity near a straight contact row

### Theorem 2

Keep the hypotheses on `P,D`. Fix an affine row of markers

```math
z_j=b+j u,\qquad j\in\mathbb Z.
```

For any `d>=0`, the number of distinct integer indices `j` admitting an
actual diameter endpoint `q_j` with `|q_j-z_j|<=d` is at most

```math
\boxed{4\sqrt{Dd}+4d+2.} \tag{5}
```

The markers need not be source points, and the assignment need not be
injective. In particular the bound applies to an actual straight chain of
unit contacts. It also applies to graph attachment distance at most `d`,
because a path of `k` unit contacts has endpoint distance at most `k`.

### Proof

All chosen `q_j` lie in the width-`2d` strip about the marker line. By Theorem 1
their projections occupy two intervals of length at most `2 sqrt(Dd)` each.
The marker projection `b dot u+j` differs from `q_j dot u` by at most `d`,
so the marker projections occupy two intervals of length at most
`2 sqrt(Dd)+2d` each. An interval of length `a` contains at most `a+1`
integer-spaced markers. Adding the two capacities proves (5).

### Corollary 3 — many deep attachments

Suppose `m>=10` distinct markers have assigned actual diameter endpoints.
Put

```math
\boxed{d_*={m^2\over256(D+m)}.} \tag{6}
```

More than `m/2` of those endpoints have distance greater than `d_*` from
their assigned markers. Indeed

```math
4\sqrt{Dd_*}+4d_*+2
\le {m\over4}+{m\over64}+2
<{m\over2}.
\tag{7}
```

Thus if `m>=cD`, these attachment distances are at least

```math
\boxed{{c^2\over256(1+c)}D}
```

for a positive fraction of the markers. The same lower bound applies to
each corresponding unit-contact graph path. The sum of the individual graph
distances is at least `m d_*/2`. This is a sum of distances, **not** a count
of distinct edges or vertices: the paths may overlap.

## 4. Exact local cap geometry

### Theorem 3a — a linear endpoint rail has quadratic hull area

Now also assume `P` is unit-separated. A strip of width `t` contains at most

```math
\boxed{4\sqrt{2Dt}+4t+4} \tag{12}
```

actual diameter endpoints. Hence for any subset `Q` of `r>=8` actual
diameter endpoints, its convex hull `C` has minimum width

```math
\boxed{w(C)>{r^2\over256(D+r)}} \tag{13}
```

and area

```math
\boxed{\operatorname{area}C>{r^4\over2\cdot256^2(D+r)^2}.} \tag{14}
```

#### Proof

Lemma 5.1, or its elementary strict-convexity proof, makes every actual
diameter endpoint an extreme source-hull vertex. Every subset of those
points is therefore in convex position. Partition the endpoints in Theorem 1
according to which projection extreme is nearer. Each group is contained
in a rectangle of side lengths at most `sqrt(2Dt)` and `t`. Its convex hull
has perimeter at most `2(sqrt(2Dt)+t)`. If the group has at least three
points, all are hull vertices and their unit-separated consecutive hull
edges give `number <= perimeter`; if it has at most two points, add a
constant two. Summing gives (12).

Apply (12) to a minimum-width strip of `C`. If its width were at most
`r^2/(256(D+r))`, its endpoint capacity would be at most

```math
{\sqrt2\over4}r+{r\over64}+4<r\qquad(r\ge8),
```

a contradiction. This proves (13).

Choose a diameter segment of `C`, of length `L>=w(C)`. The two triangles
with this common base and third vertices attaining the extreme perpendicular
heights on its two sides have disjoint interiors and lie in `C`. Their
combined area is `L` times the perpendicular width of `C`, divided by two.
Thus `area(C)>=L w(C)/2>=w(C)^2/2`, proving (14).

### Theorem 3b — the geometric rail hull is populated

Suppose in addition `P` is a global minimum-diameter `N`-point source.
Let `Q,C,r` be as in Theorem 3a and `K=conv(P)`. Then

```math
\boxed{
|P\cap C|>
{2\over\sqrt3}\operatorname{area}C-2\pi D+1.
} \tag{15}
```

In particular, if `r>=cD`, `C` has area and actual source population
`Omega(D^2)`. The population counts every source point in `C`, including
contact-isolated points. It is not asserted to be positive-contact core
population or one harmonic attachment cell.

#### Proof

The vertices of `C` are the `r` selected source-hull vertices in cyclic order.
For each edge of `C`, the chord and the corresponding outer boundary arc
of `K` enclose a convex cap. These `r` caps cover `K` outside `C`; their
interiors are disjoint, their areas sum to `area(K)-area(C)`, and their
perimeters sum to `per(K)+per(C)`. A cap can be a degenerate segment.
This is the elementary decomposition of a convex polygon by the noncrossing
chords of its inscribed selected-vertex polygon. Boundary source points may
be counted more than once in the caps, which is harmless for an upper bound.

Apply Oler to the source points in each cap. Their combined population is
at most

```math
{2\over\sqrt3}(\operatorname{area}K-\operatorname{area}C)
+{\operatorname{per}K+\operatorname{per}C\over2}+r.
\tag{16}
```

Canonical full-source geometry uses the strict translated-lattice bound
`D^2<(2sqrt(3)/pi)(N-1)`. Together with isodiametry it gives
`N>(2/sqrt(3)) area(K)+1`. Subtract (16), and use
`per(K),per(C)<=pi D` and `r<=per(C)<=pi D`, to obtain (15).

### Threshold consequence — two disjoint quadratic geometric caps

The unpromoted transverse saturation theorem supplies sets `Q_L,Q_U`, each
of at least `m-1` actual diameter endpoints, on the two internal `A`-host
intervals. They lie in the strict opposite half-planes of the threshold
reference diameter `h_0`. Thus their hulls `C_L,C_U` are disjoint.
Theorems 3a--3b force **each** of these actual geometric hulls to have
quadratic area and quadratic source population when `m=Omega(D)`.

This conclusion needs no affine markers, train-terminal identification,
or shallow-attachment hypothesis. It is stronger than saying that a rail
contains linearly many hull vertices. It does not say that the populations
lie in one complement-dual layer: a train cut can enter a convex rail hull
whose selected hull vertices all have the same layer label. These geometric
caps are not identified with the canonical inactive-container branch.

### Lemma 4 — monotone one-contact ports

Let `p_i=p_0+i u` be a straight unit-contact chain in a triangle-free
unit-separated planar set. At an internal chain vertex, there is at most one
additional contact neighbor strictly below the row and at most one strictly
above it. Write a below-row neighbor as `p_i+w_i`, where `|w_i|=1`.
In coordinates with `u=(1,0)`, its angle lies in
`[4pi/3,5pi/3]`. Whenever below-row neighbors exist at consecutive chain
vertices, their angles are nondecreasing. Above-row contact angles lie in
`[pi/3,2pi/3]` and are nonincreasing along consecutive vertices.

### Proof

Separation from both chain neighbors `p_i+-u` implies
`|w_i dot u|<=1/2`. The permitted below-row angular interval consequently
has length `pi/3`. Two distinct below neighbors must have angular separation
at least `pi/3`; equality would make them and `p_i` an exact unit triangle.
Hence triangle-freeness permits at most one. The upper case is identical.

Consecutive ports cannot be the same source point: that point and the two
consecutive chain vertices would be a unit triangle. For consecutive lower
ports, suppose their angles satisfy `a>b`. Put
`s=sin((a-b)/2)>0` and `h=(a+b)/2`. Their squared separation is

```math
|u+w(b)-w(a)|^2=1+4s(s+\sin h).
\tag{8}
```

Here `s<=1/2` while `sin h<=-sqrt(3)/2`, so (8) is strictly less than one,
which is impossible. Thus `a<=b`. Reversing the sign of the half-angle in
the upper interval proves the asserted upper order. This is a finite pair
distance argument, not an integrated infinitesimal motion.

For an unloaded vertex with neighbors `+-u` and one inward direction `v`,
contact minimality forces a port on the other side. Under `C=C_*` it has
positive stress. Thus this geometric order can be used in an actual KKT
port calculation; it does not identify those ports with diameter vertices.

## 5. Interior pressure alone fails to close the source

The attempted closing lemma was: positive interior rectangle equilibrium
forces seam pressures that cannot support the staircase's unimodal profile.
The precise interior statement is true, but the proposed closure is false.

Consider a **filled consecutive** rectangular contact patch

```math
p_{i,j}=b+i u+\sum_{k<j}v_k,quad
0\le i\le m,\quad0\le j\le n,
```

where `u=(1,0)`, every `v_j` is unit, and its angle `phi_j` lies strictly
between `pi/3` and `2pi/3`. Assume positive contact stresses and equilibrium
at every interior vertex. Let `a_{i,j}` denote the horizontal stress on
`p_{i,j}p_{i+1,j}` and `b_{i,j}` the stress on
`p_{i,j}p_{i,j+1}`. Interior equilibrium gives

```math
\boxed{b_{i,j}\sin\phi_j=q_i>0} \tag{9}
```

independent of `j`, and

```math
\boxed{
a_{i,j}-a_{i-1,j}=q_i(\cot\phi_{j-1}-\cot\phi_j).}
\tag{10}
```

Consequently the pressure on the interior horizontal rows,
`G_i=sum_{j=1}^{n-1}a_{i,j}`, satisfies

```math
\boxed{
G_i-G_{i-1}=q_i(\cot\phi_0-\cot\phi_{n-1}).}
\tag{11}
```

It is monotone, and is constant if the transverse shore is exact phase.
The two boundary rows are excluded from (11), because they have extra
source reactions. If the full actual seam pressure is `A_{i+1}=G_i+E_i`,
the staircase's change from increasing to decreasing pressure forces a
change in `E_i` on at least one tail, but not a contradiction.

Equations (9)--(10) follow by resolving vertex equilibrium along `Ju` and
`u`, respectively; summing (10) telescopes to (11). The four contact
directions at an interior vertex leave four gaps strictly below `2pi/3`,
so a fifth unit contact is impossible. Their convex hull surrounds that
vertex, so it is not an actual diameter endpoint. Thus the no-extra-contact
and no-diameter-load hypotheses hold for a genuine strict-angle filled
patch. **A complete train crossing subgrid need not be filled or consecutive.**
Unselected trains and holes cannot be silently suppressed to obtain this
chart.

### Exact boundary-traction regression

Take `m=3,n=2`, `u=(1,0)`, and `v=(5/13,12/13)`. This is a triangle-free
unit-separated rhombic rectangle. Assign every vertical edge weight one.
Assign the interior horizontal row weight one, and the two boundary rows
weights `(A_i-1)/2`, where

```math
(A_1,A_2,A_3)=(4,6,2).
```

Every interior vertex is in exact equilibrium and all contact weights are
positive. The total seam pressure is exactly the displayed unimodal profile.
The combined bottom/top boundary traction at internal column `i` is
`(A_i-A_{i+1})u`. Moreover the pressure equals the positive staircase packet
with `R_parallel=1,R_03=1,R_02=2,R_12=2`.

More generally any positive seam-pressure profile is realized in this way:
choose a constant interior row weight `c<min_i A_i/(n-1)` and give the two
boundary rows weight `(A_i-(n-1)c)/2`. This proves that interior equilibrium,
contact positivity, and a positive staircase reaction profile alone cannot
exclude the branch.

This regression **does not** realize its boundary tractions by actual
equal-length diameter bars. Its internal boundary-row points are collinear
and cannot be actual diameter endpoints. Full-source vertex equilibrium,
the actual diameter-thrackle, PSD, and global optimality are omitted. These
are exactly the hypotheses a repaired closure must restore.

## 6. Push beyond the failed pressure closure

The new strip-capacity theorem repairs the failed identification of local
boundary tractions with actual diameter carriers. It also yields the two
quadratic populated geometric rail hulls above, without a row-coembedding
assumption.

The unpromoted transverse saturation report gives at least `m-1` distinct
actual diameter endpoints on **each** extreme transverse rail, indexed by
the internal exact-shore layers. If those endpoints are attached to markers
`b+j u` with uniformly `o(D)` Euclidean or contact-path distance, Theorem 2
allows only `o(D)` such layer indices, contradicting `m=Omega(D)`.
Corollary 3 strengthens this: a positive fraction of the assignments have
macroscopic distance, and the sum of individual contact attachment depths
is quadratic.

This is an exact conditional obstruction to a proposed shallow source
co-embedding, not a shallow-depth theorem. The current extraction does not
provide a literal consecutive straight row through the selected layers.
When unselected trains intervene, their displacements belong in the marker
error; when actual loaded endpoints extend outside the rectangle, their
attachments belong in the same error. Neither error may be set to zero.

The result therefore gives a durable alternative for a real source-level
stress argument:

```math
\boxed{
\text{threshold rail saturation}
\Longrightarrow
\text{macroscopic hidden-train displacement or macroscopic attachment depth}
}
```

whenever the comparison to an affine marker row is specified. Local
cap ports cannot supply the required population of actual diameter endpoints.
Any attempted KKT closure must handle the deep continuation, and cannot rely
only on the local grid pressure identities.

## 7. Exact remaining obligation

For the actual retained threshold source, connect the two forced populated
rail hulls to actual positive-contact paths and the loaded-hull/face ledger.
The exact target is to show that both quadratic rail hulls cannot coexist
with the same complete transverse shore unless an exact triangle or strict
source competitor occurs. Their mere disjointness and population do not
prove this: global near-disk packing permits several disjoint quadratic
geometric subsets.

One more concrete pressure route is to construct layer-indexed affine
markers and account for their displacement errors and the positive-contact
paths to the forced rail endpoints. Prove either a sublinear bound on those
errors/depths, or a source-level upper bound on the aggregate quadratic
attachment depth after controlling path overlap. The former contradicts
Theorem 2 immediately; the latter must be tied to the canonical
`sum_r(L_r-2d_r)` and `e_BB-k` currency or to a strict same-cardinality
diameter competitor. A bare sum of overlapping path lengths is insufficient.

No numerical weight floor, universal source row, or simultaneous disjoint
attachment family is asserted. Nonconstant phase, open-cell exact phase,
split-star O–O, inactive-interface, and macroscopic inactive-container
branches remain uncovered.

## 8. Certificates and hostile checks

Run

```text
python3 research/verify_target_c_rectangle_pressure_2026_10_02.py
```

It checks, with Fraction arithmetic, exact pair separation and the full
contact graph of two finite patches, all interior equilibrium equations,
the telescoping pressure identity, the positive unimodal boundary-traction
regression, and the weighted-square identity at actual diameter endpoints
of a square. It does not enumerate all strips or prove optimality. The
general strip and port proofs are mathematical arguments above.

| Claim/check | Classification and boundary |
| --- | --- |
| Theorems 1–2 and Corollary 3 | Unreviewed candidate; arbitrary finite diameter set, actual endpoint hypotheses explicit |
| Theorem 3a | Unreviewed candidate; unit-separated actual diameter endpoints, no minimizer hypothesis |
| Theorem 3b | Unreviewed candidate; global source plus canonical finite Oler and strict translated-lattice comparison |
| Two disjoint quadratic rail hulls | Conditional unreviewed application to unpromoted transverse saturation; not identified with inactive chambers |
| Lemma 4 | Unreviewed candidate; exact finite unit-contact geometry |
| Equations (9)–(11) | Unreviewed candidate; filled consecutive patch only |
| Interior pressure excludes every positive staircase | Rejected by the exact boundary-traction regression |
| Thin local ports can be identified with all actual rail endpoints | Rejected under affine-row/shallow-depth hypotheses by Theorem 2 |
| Private basis-leaf release | Not reused; full diameter rows already isolate the local chart |
| Dropping contact-isolated source points | Not done; all partner and source distance constraints retained |
| Overlapping path-depth sum equals distinct population | Not asserted |
| C-II or Level I closure | Not proved |

**Promotion recommendation:** retain as unreviewed. The geometric theorems
have self-contained proofs, but the threshold application depends on
unpromoted extraction and an explicitly missing affine-row/depth bridge.
No canonical state or prompt change is requested.
