> Generated reading edition · [exact source](../../../docs/reports/target_c_stress_transversal_reinsertion_2026-09-12.md) · source SHA-256 `63e2b083df2c1e3040dedc45cf75214e51046c727c57b44a5b20872b4799348c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D6561B4BB738","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: stress-transversal deletion and protected reinsertion

**Date:** 2026-09-12

**Repository commit:** `c638e48eeb203d2144f238cb68636252ee9e90a2`

**State version:** `2026-09-12.audit.44`

**Run type:** closing-proof attempt with exact regressions

**Target:** C-II, primarily the inactive-container branch

**Starting status:** C-I closed; C-II and Level I open

**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`

**External literature search:** not used; canonical repository inputs only

**Computation:** `research/verify_target_c_stress_transversal_reinsertion.py`

## 1. Endpoint and dependency lock

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

The new results below are **proved candidates awaiting promotion**. This report is
an **unreviewed** artifact, not an independent audit or a canonical promotion.

The proposed implication chain is

```text
delete a transversal of ALL normalized KKT stresses
  + reinsert the deleted population with strict cross separation and diameter slack
-> no normalized stress on the retained source
-> feasible strict first-order diameter descent, with an explicit finite integration
-> same-n strict sub-D competitor
-> contradiction to global optimality.
```

The exact new finite bound is at most `s_Z+1` deleted core vertices in the canonical
normal form. This replaces the sufficient but potentially larger task of moving a
vertex cover of every actual diameter edge. It does not establish the reinsertion
premise, nor does it by itself exclude a C-II branch.

Only these canonical inputs are used:

- Shared theory `01-local-structure.md`, Theorem 4.1: the normalized nonnegative
  contact/diameter KKT equations and their virial identity.
- Target C Section 64, especially (64.3): the canonical stress polytope has affine
  dimension `s_Z=e+h-(2v-2)`. Its proof uses the Section-57 core rank and full support.
- Shared theory `03-oler-shell.md`, Lemma 21.1: finite convex-container Oler bound.
- Target C Sections 79--80: the full-source inactive-container/full-core split,
  used only to locate the unresolved reinsertion premise, not to prove it.

Section 95 is a proof-only warning, not a premise: protected changes to isolates
alone can leave all old stresses intact. The theorem below explicitly deletes core
vertices and proves finite descent instead of inferring release from one zero
multiplier. No imported theorem from an unpromoted report is used.

## 2. A small simultaneous stress transversal

Let `A` be a finite unit-separated planar set of diameter `D>1`. Let `C,H` be its
actual contact and diameter pairs. Define

```math
\mathcal P(A)=\{(\alpha,\beta)\ge0:
 R_C^T\alpha-R_H^T\beta=0,\quad\sum_H\beta=1\}.
```

Here a rigidity row applied to a velocity is
`(p_i-p_j) dot (v_i-v_j)`, without the inessential factor two.
Suppose `P(A)` is nonempty and has affine dimension `d`.
The virial identity gives `sum alpha=D^2`; thus `P(A)` is a compact polytope.

### Proposition 2.1: at most d+1 selected diameter rows suffice

There is a set `J subset H`, `|J|<=d+1`, such that

```math
\{x\in\mathcal P(A):\beta_e(x)=0\text{ for every }e\in J\}=\varnothing.
\tag{2.1}
```

**Proof.** Start with the nonempty face `F=P(A)`. Choose any `x in F` and a
diameter coordinate `e` with `beta_e(x)>0`; normalization guarantees one. Replace
`F` by `F intersect {beta_e=0}` and record `e`. This is either empty or a proper
face of `F`, since `beta_e>=0` on `F` and is not identically zero there. A nonempty
proper face has smaller affine dimension: otherwise its affine hull would be that
of `F`, on which `beta_e` would vanish identically. At most `d` nonempty reductions
lead to a point; one further chosen coordinate makes the intersection empty.
No previously chosen coordinate can be selected again. This proves (2.1).

Equivalently, on the compact polytope,

```math
\min_{x\in\mathcal P(A)}\sum_{e\in J}\beta_e(x)>0.
\tag{2.2}
```

This positive number is source-dependent. No uniform multiplier floor is claimed.

### Proposition 2.2: deleting endpoints removes every stress

Choose **either** endpoint of each edge in `J`, and let `S` be the set of chosen
vertices, with repetitions suppressed. Then `|S|<=d+1`, and the retained set
`R=A\S` has no normalized nonnegative equilibrium stress on its inherited
contact rows and inherited length-`D` rows.

**Proof.** Any such retained stress extends to a stress of `A` by assigning zero
to every removed row. Equilibrium at each deleted vertex is then zero, and
normalization is unchanged. Every `e in J` was removed, so the extension violates
(2.1). This proves the assertion. If no length-`D` pair remains, a strict smaller
diameter has already been obtained for `R`.

Further point deletion cannot restore a normalized stress: extend by zeros once
more. In particular, a set `Z` of original isolates may also be removed for
repacking. Their population must still be restored in the final competitor.

### Canonical consequence

Section 64 supplies `d=s_Z`. The chosen vertices are diameter endpoints and hence
belong to the nonisolated core: a positive diameter load at a contact-isolated
vertex is impossible, while the canonical full-support stress loads every actual
diameter edge. Consequently there is a set

```math
S\subset V,\qquad |S|\le s_Z+1
\tag{2.3}
```

with the deletion property. This covers the cyclic and forest diameter branches
and arbitrary `s_Z>=0`; no contact-isolated source point was identified with a
core point or discarded from the final cardinality.

When `s_Z=0`, the full-support normalized stress is unique. Deleting **any** core
vertex removes a positive incident contact row, so extension by zeros would
contradict that unique full-support stress. Thus in this case any single core
vertex, not merely a chosen diameter endpoint, suffices.

The face argument can also be run on the projected polytope of diameter
coordinates. If its affine dimension is `d_H^{proj}`, the bound is
`d_H^{proj}+1<=s_Z+1`. This notation is distinct from the Woodall defect `d_H`.

## 3. Absence of stress gives finite strict descent

### Proposition 3.1: exact velocity alternative

For a retained configuration `R`, let `C_R` be its unit pairs and `H_R` its
length-`D` pairs. If there is no normalized nonnegative equilibrium stress on
these rows, there is a velocity `u` with

```math
R_{C_R}u\ge0,\qquad R_{H_R}u\le-\mathbf1.
\tag{3.1}
```

When `H_R` is empty, take `u=0` and use the existing strict diameter gap.

**Proof.** The finite linear-inequality alternative applied to (3.1) says that its
infeasibility would give `alpha,beta>=0` with

```math
R_{C_R}^T\alpha-R_{H_R}^T\beta=0,
\qquad \sum\beta>0.
```

Dividing by `sum beta` gives the forbidden normalized stress. This is the mixed
strict/weak alternative, not the assertion that a single omitted stress row is
releasable. The alternative follows by separating the right-hand side from the
polyhedral cone consisting of the image of the velocity map plus its slack
orthant; the separating functional is nonnegative on that orthant. Its strictly
negative pairing with the right-hand side gives `sum beta>0`.

For the straight motion `p_i(t)=p_i+t u_i`, each old unit pair satisfies

```math
|p_i(t)-p_j(t)|^2
=1+2t R_{ij}u+t^2|u_i-u_j|^2\ge1\quad(t\ge0).
\tag{3.2}
```

Every old diameter pair has a strictly negative first derivative, so its squared
length is `<D^2` for all sufficiently small positive `t`. All other distances
have the necessary strict initial slack, preserved for sufficiently small `t`
because there are only finitely many pairs. This proves an actual finite
unit-separated motion to diameter `<D` for the retained points. Neither PSD nor a
uniform velocity/step-size bound is needed.

## 4. Protected reinsertion closes the same-cardinality gap

### Theorem 4.1: stress deletion plus guarded reinsertion

Let `S` satisfy Proposition 2.2. Let `Z subset A\S` be any set to be repacked;
in the intended application its members are original contact isolates. Set

```math
R=A\(S\cup Z),\qquad k=|S|+|Z|.
```

Suppose there is a `k`-point set `B` such that

```math
1\le|b-b'|<D\quad(b\ne b'\in B),\qquad
1<|b-r|<D\quad(b\in B,r\in R).
\tag{4.1}
```

Then there is a unit-separated **n-point** configuration of diameter strictly
smaller than `D`.

**Proof.** Delete `S cup Z`, apply Proposition 3.1 to `R`, and hold the newly
inserted set `B` fixed during the retained-source motion. Internal distances of
`B` remain feasible, including any exact unit contacts. The strict cross bounds
in (4.1) survive for all sufficiently small positive time. The old retained unit
pairs remain separated by (3.2), and every retained diameter pair shortens.
Choose a common positive time for the finitely many constraints. All pair
distances are then at least one and strictly below `D`. The number of points is
`|R|+|B|=|A|`. The triangle status of the competitor is immaterial to a strict
minimum-diameter contradiction.

The relocation need not be connected to the old source by a feasible path.
Global optimality compares feasible terminal configurations. The only continuous
motion asserted is the proved retained-source motion after guarded replacement.

If `W subset int(conv A)` is a region at distance strictly greater than one from
`R`, any unit-separated `k` points in `W` satisfy (4.1). Indeed an interior point
of a positive-area convex body of diameter `D` has distance `<D` from every point
of that body. To see this, extend its ray away from the other point a positive
distance while remaining in the body; equality at the interior point would then
give a distance greater than `D`.

### Exact reserve formulation

Define `pack_1(W)` as the maximum cardinality of a unit-separated finite subset
of the bounded region `W`. This maximum exists as an integer, including for open
`W`: a disk-area bound makes the set of attainable integers finite. For a fixed
protected region `W` and repacked isolate set `Z`, put

```math
\operatorname{reserve}(W,Z)=\operatorname{pack}_1(W)-|Z|.
```

Let `tau(A)` be the minimum number of core vertices whose deletion eliminates all
normalized stresses. For a protected region usable for the chosen minimizing
deletion set, the exact sufficient condition is

```math
\operatorname{reserve}(W,Z)\ge\tau(A),\qquad
\tau(A)\le s_Z+1.
\tag{4.2}
```

If `W` is protected from every non-repacked point of the original source, it is
usable for every choice of `S`. The simpler uniform sufficient condition is then
`reserve(W,Z)>=s_Z+1`. At `s_Z=0`, **one spare protected packing site** suffices.
This is an integer-capacity premise, not a consequence asserted from an `O(D)`
error estimate.

Conversely, for a global minimizer every such usable protected region must obey
the **necessary** capacity bound

```math
\operatorname{pack}_1(W)\le |Z|+|S|-1.
\tag{4.4}
```

Combining with the lattice averaging argument below gives the finite necessary
area bound `area(W)<=a_0(|Z|+|S|-1)`. These are consequences for the same source
and the same deletion set, not upper bounds for an unrelated container.

For completeness a directly usable sufficient area test, requiring no convexity,
is

```math
\operatorname{area}(W)>a_0(|Z|+|S|-1),\qquad a_0=\sqrt3/2.
\tag{4.3}
```

Average the number of points of a translated unit triangular lattice in bounded
measurable `W` over a fundamental parallelogram. Tiling and translation of the
integrals give average `area(W)/a_0`. Under (4.3) some translate has at least
`|Z|+|S|` points; choose that many. This argument works for open protected regions
and allows internal unit triangles. It does not control guard erosion or prove
(4.3) for a source chamber.

## 5. Exact regression: dense contact-free containers can have zero reserve

**Classification: regression, with a proof; not a C-II source counterexample.**

Let `L` be the unit triangular lattice with coordinates
`(i+j/2, sqrt(3) j/2)`. For an integer `m>=1`, let `H_m` be the regular hexagon
with the six axial vertices

```math
(m,0),(0,m),(-m,m),(-m,0),(0,-m),(m,-m).
```

Its lattice points have `max(|i|,|j|,|i+j|)<=m`, and their number, area, and
perimeter are

```math
N_m=3m^2+3m+1,\quad |H_m|=\frac{3\sqrt3}{2}m^2,
\quad P(H_m)=6m.
```

Set

```math
s_m=1+\frac1{100m^2},\qquad
t_m=1+\frac1{200m^2},\qquad
W_m=\operatorname{int}(s_m H_m).
```

The `N_m` points of `t_m(L intersect H_m)` lie strictly inside `W_m` and have
mutual distances at least `t_m>1`. In particular, all are contact-isolated and
there is no unit triangle. Yet Oler applied to the **closed** container gives

```math
\begin{aligned}
\operatorname{pack}_1(W_m)
&\le 3m^2s_m^2+3ms_m+1\\
&=N_m+\frac3{50}+\frac3{100m}+\frac3{10000m^2}
<N_m+1.
\end{aligned}
```

Integer cardinality and the displayed packing prove

```math
\boxed{\operatorname{pack}_1(W_m)=N_m.}
\tag{5.1}
```

These containers have quadratic area/population, linear perimeter, and
`area(W_m)-a_0 N_m=O(m)`, but **zero** packing reserve. Strict absence of unit
contacts does not change this.

This kills an attempted inference from just those container properties to one
spare site. It does not embed the hexagon into a canonical source chamber,
establish global diameter optimality, or exclude source-specific use of the
outside core. In particular it leaves open exactly the coupling needed in (4.2).

## 6. Exact finite test of the entire deletion/reinsertion mechanism

**Classification: regression/test example, not a global-minimizer theorem.**

Take the `4m` integer points on the boundary of `[0,m]^2`, for even `m>=6`, and
one original isolated point `(m/2,m/2)`. The source has diameter `sqrt(2)m`.
Its only contacts are successive horizontal/vertical boundary edges; its only
diameter pairs are the two corner diagonals. It has the normalized stress

```math
\alpha_e=m/2\quad\text{on all }4m\text{ contacts},\qquad
\beta_1=\beta_2=1/2.
```

It is unique: equilibrium at intermediate side points makes each side's contact
multiplier constant; corner equilibrium equates the two incident side constants
to `m` times the corresponding diagonal multiplier; propagation around the
square equates all four side constants. Normalization fixes them as displayed.
The isolated point has no rows.

Delete corner `(m,m)` and the original isolate. Insert the **two** points
`(m/2-1,m/2)` and `(m/2+1,m/2)`, restoring all `4m+1` points. Apply to retained
boundary points the straight motion

```math
(x,y)\longmapsto(x+t y,y+t x),\qquad 0\le t\le\frac1{10m},
\tag{6.1}
```

while fixing the inserted pair. Every retained contact has zero first derivative
and positive quadratic separation. The remaining diagonal has squared length
`2m^2(1-t)^2`, so it strictly shortens. The script checks **every** pair over the
entire interval, and the strict final diameter, using rational arithmetic for
even `m=6,...,24`.

This is not the canonical full-rank core: for large `m` the square frame has many
mechanisms. It tests the general `d=0` theorem, not the formula `d=s_Z` outside its
canonical hypotheses. It also explicitly repacks an original isolate and moves a
core vertex, unlike protected isolate-only contact creation.

### A multiple-stress negative control

The unit regular hexagon plus its center has twelve contacts (six rim edges and
six spokes) and three diameter pairs. This is a test of the general stress
argument; it contains unit triangles and is **not** a C-II source.

Write `a` for the rim contact weight and `beta_0,beta_1,beta_2` for the diameter
weights. Tangential equilibrium at the six rim vertices forces every rim
weight to equal `a`; their radial equations then force the spoke at vertex `i`
to have weight `2 beta_{i mod 3}-a`. Opposite spokes have the same weight, so
center equilibrium is automatic. Thus the entire normalized stress polytope is

```math
a\ge0,\qquad \beta_j\ge a/2,\qquad \sum_{j=0}^2\beta_j=1.
```

Its four vertices are the rim stress `(a=2/3,beta_j=1/3)` and three straight
diameter-chain stresses `(a=0,beta=e_j)`. To verify exhaustiveness, put
`gamma_j=beta_j-a/2>=0`; then `sum gamma_j+3a/2=1` is a simplex.
The normalized dimension is three and its diameter projection dimension is two.

Deleting the center leaves the rim stress. Deleting any one rim vertex leaves
two diameter-chain stresses. Hence **every single-point deletion leaves a
stress**. Deleting the center and any one rim vertex removes all four extreme
supports and therefore every normalized stress. Its stress deletion number is
exactly two. Two selected diameter-coordinate-zero faces still leave the third
chain stress; all three are required for the selected-coordinate construction.

The script verifies the distances and equilibrium exactly in `Q(sqrt(3))`.
This negative control rejects dropping the unique-stress hypothesis from the
single-vertex corollary. It also distinguishes the best vertex deletion number
from the sufficient selected-diameter-coordinate bound.

## 7. Failed closing steps and exact remaining lemma

No branch has been eliminated. The finite support-to-motion bridge is supplied,
but its source-preserving application remains conditional on protected capacity.

The next possible closing theorem for Type I is:

> Every sufficiently large canonical triangle-free global minimizer in the
> inactive-container branch admits a stress-deleting core set `S`, a repacked
> source set `Z`, and a set `B` of size `|S|+|Z|` satisfying (4.1).

Proving the stronger protected reserve bound (4.2) would suffice. The hexagon
regression requires such a theorem to use a **source-specific interaction with
the diameter core**, not merely quadratic density, absence of contacts, or
linear Oler slack. Multiple containers may be used if all cross distances among
their replacement populations are checked together; individual capacity bounds
alone are not a simultaneous packing theorem.

For Type II, `n-v=o(D^2)` need not provide even one suitable container. The
Section-104 macroscopic carrier bound is not an insertion site or a finite
deformation. That branch remains unchanged.

The abstract simplex `beta>=0, sum beta=1` in dimension `d` needs all `d+1`
coordinate-zero faces for an empty intersection: omitting a coordinate leaves
its unit vertex. Thus dimension alone cannot lower the **selected-coordinate**
bound to `d`. This is not a sharpness claim for planar source vertex deletion;
several selected edges can share a vertex, and geometric stress polytopes may
have more structure than arbitrary simplices.

## 8. Claim audit and branch ledger

| Claim/branch | Classification or outcome | Exact limit |
| --- | --- | --- |
| At most `d+1` diameter coordinates meet every stress | Proved candidate awaiting promotion | Finite nonempty normalized stress polytope |
| At most `s_Z+1` core vertices suffice canonically | Proved candidate awaiting promotion | Uses canonical Section 64 |
| Stress-free retained set has finite strict descent | Proved candidate awaiting promotion | All retained active rows included |
| Guarded reinsertion yields a same-n strict competitor | Proved candidate awaiting promotion | Requires all of (4.1) |
| Type I closes from the new mechanism | Conditional | Protected capacity not proved |
| Quadratic contact-free population forces a spare site | Rejected attempted inference | Exact hexagonal-container regression |
| Cyclic/forest `s_Z=0` | Still open | One spare protected site would suffice |
| `s_Z>0` | Still open | `tau(A)<=s_Z+1`, reserve not bounded below |
| Contact-isolated source points | Retained in cardinality | `|B|=|S|+|Z|` |
| Full-core Type II | Still open | No protected replacement supplied |
| Whole-source Level I | Still open | Neither global branch closed |

Checks against binding regressions: this argument uses no local-optimum/global-
optimum identification, no full-source affine-kernel extension, no co-embedding
of independent optima, no multiplier floor, no Euler-trail assumption, no FB4,
no Reuleaux-cap placement, and no equality-uniqueness import. A single selected
stress with a missing coordinate is explicitly insufficient. Feasible
integration is proved for the complete retained system, and every deleted point
is replaced before the diameter contradiction is claimed.

## 9. Computation and promotion disposition

Run:

```sh
python3 research/verify_target_c_stress_transversal_reinsertion.py
```

The script uses exact `Fraction` arithmetic. It verifies source stresses, every
pairwise constraint over the full simultaneous motion interval, strict final
diameter, finite hexagon counts and the rational Oler gap, and abstract simplex
face sharpness. It also checks the four explicit stresses and all single-vertex
deletions in the regular-hexagon-plus-center negative control. The report supplies
the general proofs. Passing does not prove
global optimality, the canonical geometry of the examples, protected capacity in
a C-II source, or Level I closure.

Recorded certificate output: 20,940 whole-interval pair checks across ten square
sources; least final squared-separation margin `1/57600`; least squared-diameter
improvement `119/50`; twelve hexagonal-container checks with Oler increment at
most `903/10000`; 510 simplex coordinate-face intersections; all seven
single-vertex deletions in the multiple-stress negative control retain stress.

The theorem-state checker also passes using the existing validation environment
`/tmp/e99-cii-validation-20260911/bin/python`; the system Python lacks `jsonschema`.

Pre-publication remote comparison: `origin/main` advanced to `07f1f64` with the
post-104 reconciliation and proof-namespace cleanup. Its state version and the
canonical dependencies used here remain audit.44. No new proof-only result from
that reconciliation is imported into this argument.

**Promotion recommendation: unreviewed.** Preserve the proof draft and exact
certificate; request no automatic theorem-state promotion. No canonical input
is corrected or superseded, and the active prompt/state version stay unchanged.

Next reads: this report, canonical Section 64, canonical Sections 79--80, and
the exact chamber/source interface relevant to a proposed packing of (4.1).
