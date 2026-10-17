> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_support_atlas_obstruction_2026-09-26.md) · source SHA-256 `897e2b4ab1b47b63889c1b2f1c7bcbb1b4cc004ab857bf79d4f3e6bbbdedf6a6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-42BE90DAAF7C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — global loaded-chord exclusion and diameter-support atlas obstruction

**Phase 2 preservation provenance:** PR #591, branch swarm/root/c2-global-variations, audited source head 9bf2b627280a313c3fad8433ade344790ec63205. Preserve its finite loaded-chord exclusion and atlas bounds as unreviewed candidates, with its exact verifier; it does not supply the chart-cover premise, a competitor, or Level I.

**Date:** 2026-09-26<br>
**Repository commit:** `53ab4cac73738c82f6291b41a7ec88a8577c5d55`<br>
**State version:** `2026-09-14.audit.51`<br>
**Branch:** `swarm/root/c2-global-variations`<br>
**Run type:** closing-proof attempt / structural theorem / exact regression<br>
**Target:** alternate source-level route into C-II, both canonical branches<br>
**Classification:** proved candidate awaiting independent audit; noncanonical, unreviewed<br>
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`<br>
**External literature:** no new theorem imported<br>
**Computation:** exact regression/normal-arc checks; not load-bearing for the proof

## LEVEL I STATUS

`STILL OPEN`.

## 1. Starting endpoint and lane

C-II still needs an exact triangle or a strict same-cardinality sub-`D` competitor.
In the full-core branch its preferred metric endpoint is the aggregate detour
`sum_r(L_r-2d_r)` coupled to the loaded-hull and diameter ledgers. The macroscopic
inactive-container branch has the same source-level closure requirement.

This run uses an alternate source-level lane. Its canonical inputs are only the
linear loaded-boundary count in [C30/C34](../targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md).
The first, weaker argument additionally uses the all-source circumradius theorem
[FS.1](../targets/target-c/58-full-source-geometry-audit.md); the strongest result
in §2A needs no circumradius or global-optimality premise.
No harmonic-cell, train, selected-extreme, or full-source rigidity assertion is a premise.
The global chord theorem GC.1 below additionally uses the canonical §63 ledger
only to state its exact frontier consequence; its geometric proof has no
canonical mathematical dependency.

The intended closing chain was

```text
loaded endpoints concentrated in finitely many near-exact lattice charts
 -> diameter-support lattice-shadow bound gives |B|=o(D)
 -> canonical C30/C34 gives 2|B| >= ceil(D)+2
 -> no triangle-free canonical survivor
 -> Level I through the canonical representative reduction.
```

The new theorem proves the middle implication, for both C-II branches. The chart
concentration premise is NOT proved. The actual consequence is a linear population
of loaded endpoints outside every fixed finite near-exact lattice atlas.

The final source-level pivot gives a second, completed chain:

```text
two actual diameter-partner disks in one source
 -> nearby endpoints have supporting normals in a cone of width < 2pi/3
 -> a unit chord cannot span two unit-separated convex-hull sides
 -> c_B=0 also in the macroscopic-container branch
 -> global exact loaded-hull ledger below.
```

This removes an actual geometric subbranch. It does not supply the last
ledger-to-competitor or ledger-to-triangle implication.

### Concurrency check

Open PR #579 (`ed21248321fea8f8e99d257da60ca9e11417b814`) already gives a lattice-shadow
obstruction under concentric inner/outer **disk containment of the loaded hull**,
and applies it to the full-core near-disk branch. Its statement was inspected before
choosing this lane. The present argument instead needs only an annulus containing
the **vertices**. It permits arbitrarily large missing arcs in the loaded hull,
does not require an inscribed disk there, applies in the macroscopic-container
branch, and allows any lattice of minimum spacing at least one. PR #579 is not a
dependency and its proof is not imported. PRs #583--588 address distinct cap/detour
charges. PR #582 kills fixed-index oblique-to-triangular straightening; no such
straightening is used here. PR #578 concerns population/boundary shear bounds.

## 2. First theorem: the vertex-annulus bound

This theorem is valid, but its application AA.3 is quantitatively dominated by
DS.2 below. The annular normal-arc lemma may be reusable outside diameter graphs.

Let `Q` be a convex polygon of diameter at most `D>=1`, with unit-separated
strict extreme vertices (collinear redundant boundary points are not vertices).
Suppose that, after a translation, each vertex `p` satisfies

```math
r\le |p|\le R,
\qquad 0\le r\le R\le D.
```

Write `H=R^2-r^2`. Let `S` be any subset of the vertices within distance
`0<=epsilon<=1/8` of a translated lattice `Lambda` whose nonzero vectors have length
at least one. There is no adjacency requirement on `S`.

For every `1<=M<=D`, set

```math
\alpha=\arcsin(2\epsilon),\qquad T=M+2\epsilon.
```

Then

```math
\boxed{
|S|\le {\pi D\over M}
+48T\sec\alpha
\left[R\tan\alpha+\sqrt{H+M^2/4}\right].
}
\tag{AA.1}
```

If `r=D-R`, define `eta=(2R-D)/D`. Then

```math
\boxed{
{|S|\over D}
\le132(\sqrt\epsilon+\eta^{1/4})+35D^{-1/3}.
}
\tag{AA.2}
```

For every global minimum-diameter source `A`, take its circumcenter `o` and
circumradius `R`. For **any** subset of its actual diameter endpoints within
`epsilon` of one such lattice, canonical FS.1 implies

```math
\boxed{
|S|\le132D\sqrt\epsilon+172D^{7/8}+35D^{2/3}.
}
\tag{AA.3}
```

This is uniform over the lattice shape, orientation and translation, the choice
of endpoints, and the source. The subset can omit arbitrary endpoints, and the
force hull need not contain a macroscopic disk.

### Scope

AA.1 is a finite geometric theorem, not an optimality assertion. AA.3 uses the
actual full-source global optimum only for FS.1. Contact-isolated points remain
in `A`, its circumradius and its diameter. The linear lower bound on loaded
endpoints in the next corollary is used only for the canonical normalized C-II
representative; it is not asserted for every selected stress of an arbitrary optimum.

## 2A. Strongest theorem: actual diameter-support curvature

Let `A` be any finite unit-separated planar source of diameter `D>=1`. Let `S`
be any subset of its actual diameter endpoints. Suppose every point of `S` is
within `0<=epsilon<=1/8` of one translated lattice with minimum spacing at least
one. For `1<=M<=D`, `T=M+2epsilon` and `alpha=arcsin(2epsilon)`,

```math
\boxed{
|S|\le {\pi D\over M}+18T^2+48TD\tan\alpha.
}
\tag{DS.1}
```

In particular,

```math
\boxed{|S|\le128D\sqrt\epsilon+33D^{2/3}.}
\tag{DS.2}
```

Retaining the vector-length dependence gives the stronger small-noise estimate

```math
\boxed{|S|\le136D\epsilon(1+\log(1/\epsilon))+33D^{2/3}.}
\tag{DS.2L}
```

At `epsilon=0`, its noise term is defined by its limit zero. One can take the
smaller noise term from DS.2 and DS.2L. This is a natural logarithm.

No annulus, disk containment of the loaded hull, circumradius estimate, selected
stress, or global-optimality premise is required. The only supporting disks are
the genuine radius-`D` disks centered at diameter partners of the actual endpoints.

### Complete proof of DS.1

The strict-extremality proof in §3.1 uses only actual diameter status; apply it
to `S` and let `P=conv(S)`. For each vertex `p_i` of `P`, choose an actual
diameter partner `y_i` from the **same source** `A`, and set

```math
n_i=(p_i-y_i)/D.
```

For every source point `p_j`, the true diameter constraint `|p_j-y_i|<=D`
gives

```math
n_i\cdot(p_j-p_i)\le-{|p_j-p_i|^2\over2D}.
```

In particular `n_i` is a unit outward supporting normal of `P` at `p_i`.
Applying the same inequality with `i,j` reversed gives the exact quantitative
normal-separation inequality

```math
\boxed{
(n_j-n_i)\cdot(p_j-p_i)\ge {|p_j-p_i|^2\over D},
\qquad |p_j-p_i|\le D|n_j-n_i|.
}
\tag{DS.0}
```

There is no first-order or integrated-motion assertion in DS.0.

Fix a directed nonzero lattice vector `w` of length at most `T`. As in §3.4,
every assigned short side has its outward normal within `alpha` of the normal
perpendicular to `w`. All polygon sides in this normal interval form one chain.
Remove its first and last sides, if present. There are at most two such sides
assigned to `w`, including when the chain has only one or two sides.

Every vertex of the remaining inner chain has both adjacent side normals within
that interval. Its chosen supporting normal `n_i` belongs to the vertex's outward
normal cone, the angular interval between those two adjacent side normals, so
it also lies in the interval of width `2alpha`. Thus the first and last vertices
of the inner chain have

```math
|n_j-n_i|\le2\sin\alpha,
\qquad |p_j-p_i|\le2D\sin\alpha
```

by DS.0. The inner chain is monotone in the tangent coordinate, with slopes at
most `tan(alpha)` in absolute value, including all of its intervening long sides.
Its length is at most `sec(alpha)` times the tangent displacement of its endpoints,
which is at most their Euclidean distance. Consequently its total length is at
most `2D tan(alpha)`.

Every assigned side has length at least `|w|-2epsilon`. It follows that the number
of assigned short sides is at most

```math
2+{2D\tan\alpha\over |w|-2\epsilon}.
```

Using the elementary bounds `F(T)<=9T^2` and AA.7, summing over all possible
directed `w` gives at most `18T^2+48TD tan(alpha)` short sides. There are fewer
than `pi D/M` longer sides because `per(P)<=pi D`. This proves DS.1. If `S`
has fewer than three points, its conclusion follows from `pi D/M>=pi`.

For `epsilon<=1/8`, `T<=5M/4` and `tan(alpha)<=8epsilon/sqrt(15)`. Therefore

```math
{|S|\over D}\le{\pi\over M}+124M\epsilon+29M^2/D.
```

Choose `M=min(epsilon^(-1/2),D^(1/3))`, with `M=D^(1/3)` if `epsilon=0`.
Then `1/M<=sqrt(epsilon)+D^(-1/3)`, `M epsilon<=sqrt(epsilon)`, and
`M^2/D<=D^(-1/3)`. Since `pi+124<128` and `pi+29<33`, DS.2 follows.

### Weighted-angle refinement: complete proof of DS.2L

For each particular vector `w`, the half-width can instead be

```math
\alpha_w=\arcsin{2\epsilon\over |w|-2\epsilon}.
```

The ratio is at most `1/3`, and
`tan(alpha_w)<=3epsilon/[sqrt(2)(|w|-2epsilon)]`. The same chain argument gives
at most

```math
2+{3\sqrt2 D\epsilon\over(|w|-2\epsilon)^2}
```

assigned sides. The disk count and integration by parts give

```math
\sum_{0<|w|\le T}|w|^{-2}
={F(T)\over T^2}+2\int_1^T{F(t)\over t^3}\,dt
\le9+18\log T.
```

Since `|w|-2epsilon>=3|w|/4`, the reciprocal-square sum with these denominators
is at most `16+32 log(T)`. Thus

```math
|S|\le{\pi D\over M}+18T^2+(68+136\log T)D\epsilon,
```

where `48sqrt(2)<68` and `96sqrt(2)<136` were rounded upwards.
Use `T<=5M/4`, `18T^2<=29M^2`, and `log(5/4)<=1/4` to obtain

```math
{|S|\over D}\le{\pi\over M}+29M^2/D
+\epsilon(102+136\log M).
```

For `epsilon>0` take `M=min(epsilon^(-1),D^(1/3))`. Then
`1/M<=epsilon+D^(-1/3)`, `M^2/D<=D^(-1/3)`, and
`log M<=log(1/epsilon)`. The coefficient of the constant noise term is
`pi+102<106<136`, and that of `D^(-1/3)` is `pi+29<33`.
This proves DS.2L. For `epsilon=0` use DS.1 with `M=D^(1/3)` directly.

### Adversarial scope check

The partners `y_i` need not belong to `S` or share any stress. They belong to the
same source, which is essential for `|p_j-y_i|<=D`. The chosen normals need not
be consistent choices at different vertices; each independently belongs to its
own normal cone, and DS.0 holds for every pair of choices. Arbitrary missing
arcs and long sides are retained in the inner chain. Contact-isolated points
are retained in `A`; no source point is moved or deleted. Stars and non-Eulerian
diameter graphs satisfy DS.0 without an ordering of their graph edges.

## 2B. Global loaded-unit-chord exclusion

### Theorem GC.1

Let `A` be any finite unit-separated planar set of diameter `D>=2`. Let `B` be
any subset of the endpoints of its actual diameter pairs. If `p,q` in `B` satisfy
`|p-q|=1`, they are consecutive vertices of `conv(B)` (with the evident segment
interpretation if `|B|=2`). No global optimality or triangle-free hypothesis is
needed for this geometric assertion.

### Complete proof

Every point of `B` is a strict extreme vertex, by §3.1. Choose actual partners
`y,z` for `p,q`, respectively, and let `n_p=(p-y)/D`, `n_q=(q-z)/D`.
These are unit outward supporting normals at `p,q`. Since `y,z` belong to the
same diameter-`D` source,

```math
D|n_p-n_q|
=|(p-q)-(y-z)|\le |p-q|+|y-z|\le1+D.
```

Thus

```math
|n_p-n_q|\le1+D^{-1}\le3/2,
\qquad
\tau:=\angle(n_p,n_q)\le2\arcsin(3/4)<2\pi/3.
\tag{GC.0}
```

For a strictly convex polygon, side normals rotate monotonically around its
boundary, and the normal cone at a vertex is the interval between its adjacent
side normals. Hence one of the two boundary arcs from `p` to `q` has all its
side normals in the shorter normal interval from `n_p` to `n_q`, of width `tau`.
Orient that arc from one endpoint to the other. Its side tangents lie in one
cone of the same width; if it has `N` sides, projecting onto the cone's midpoint
direction gives

```math
1=|p-q|\ge\sum_{j=1}^N\ell_j\cos(\tau/2)
\ge N\cos(\tau/2),
```

since every `ell_j>=1`. If `p,q` were nonconsecutive, both arcs would have at
least two sides. But

```math
2\cos(\tau/2)\ge2\sqrt{1-(3/4)^2}=\sqrt7/2>1.
```

This is a contradiction. Thus `p,q` are consecutive. Only the short-normal arc
is used; no assertion that the other arc has no vertices is made.

The slightly stronger sufficient condition is `D>(1+sqrt(3))/2`, obtained from
`1+D^(-1)<sqrt(3)`; the simple finite threshold `D>=2` avoids a needless sharpness
claim. Nothing here orders edges of the diameter graph into an Euler trail.

### Exact canonical implication

For the canonical triangle-free C-II source, `B` is the actual positive-diameter
endpoint set. GC.1 proves

```math
\boxed{c_B=0,\qquad e_{BB}=q-m_B}
\tag{GC.1}
```

in **both** the full-core and macroscopic-container branches, once `D>=2`.
Here `m_B` is the number of nonunit loaded-hull sides; it is not the outlier count
`m` used in the atlas inequalities.

Canonical §63 gives the exact identity `c_I+s_C+c_B=m_B+k-2`, with
`k=d_H+s_Z`. Therefore, without discarding any boundary-order or component term,

```math
\boxed{
s_C=m_B+k-c_I-2,\qquad
\mu_DD=q+m_B-k-2c_I-4,
\qquad q-m_B\ge Q+2k.
}
\tag{GC.2}
```

The last inequality is the canonical §63 loaded-contact payment. These formulas
were canonical under the full-core near-disk hypothesis via
`C-FULLCORE-LOADED-CHORD`; GC.1 now establishes them on the macroscopic-container
branch too. A recovered, unreviewed source edit claims that canonical Section 75 is
all-phase and gives `c_I=O(D^{2/3})` in the macroscopic-container branch as well.
Under that interpretation the displayed extension also gives
`mu_D=(q+m_B-k)/D+o(1)` in both branches. The scope correction has not been
independently audited and changes no theorem-state or route status.

GC.2 alone gives no upper bound on `mu_D`: the integer ledger assignment
`q=m_B=t`, `k=Q=e_BB=0`, `c_I=1`, `s_C=t-3`, `x_B=t` satisfies the displayed
§63 identities for `t>=4` and gives `mu_D D=2t-6`. This is only a scalar witness,
not a geometric configuration. It kills the attempted inference from chord
elimination alone to a bounded or contradictory surplus.

### Finite direction capacity

The inner-chain argument also gives a direct corollary: the number of unit
loaded-hull sides whose **oriented** side normals lie in an interval of
half-width `alpha<pi/2` is at most `2+2D tan(alpha)`. Remove the first/last sides;
the inner chain has length at most `2D tan(alpha)` and every counted side has
length one. For a union of `J` such intervals this is at most
`2J+2D sum_j tan(alpha_j)`.

Thus a linear `e_BB` population cannot have all its directions in finitely many
vanishing-width phase intervals. This does not close the high-`e_BB` branch:
the canonical phase collapse concerns a selected grid, and does not concentrate
the directions of all loaded unit contacts. Canonical Target B §39 already
has a scoped asymptotic exposed-hull phase theorem; this finite corollary does
not replace its crossing-measure or pure-rhombic-disk hypotheses.

### Source-endpoint hypothesis is essential

The exact unit-separated set

```math
\{(0,0),(1,0),(1/2,1),(1/2,-1)\}
\tag{GC.R1}
```

has diameter two and a nonconsecutive unit chord between `(0,0),(1,0)`.
Those two points are NOT diameter endpoints: only the two points on the vertical
axis realize the diameter. GC.R1 is triangle-free. Thus ordinary convexity and
unit separation alone do not give GC.1. The actual partners `y,z` provide the
new hypothesis that extends the previously near-disk canonical theorem.

## 3. Complete proof of the annular companion

### 3.1 Diameter endpoints are strict extreme vertices

Suppose `p` is an endpoint of an actual diameter pair `py`, with `|p-y|=D`.
If `p=sum_i a_i p_i` is a nontrivial convex combination of other source points,
then

```math
\sum_i a_i|p_i-y|^2-|p-y|^2
=\sum_i a_i|p_i-p|^2>0.
```

The left side is at most zero since every `|p_i-y|<=D`. This contradiction shows
that `p` is a strict extreme vertex of the full source hull. Every subset of
these endpoints remains in strictly convex position: otherwise one point would
be a convex combination of other source points. No three endpoints are collinear.

All actual diameter endpoints satisfy

```math
D-R\le |p-o|\le R.
\tag{AA.4}
```

The lower bound follows from `D=|p-y|<=|p-o|+|y-o|<=|p-o|+R`.
Since the minimum enclosing circle contains a diameter pair, `R>=D/2`; choosing
any source point as a center shows `R<=D`. Thus AA.4 is a vertex annulus, even
when its vertex hull has large missing circular arcs.

### 3.2 Short sides in a normal interval

Consider all sides of a convex polygon whose outward normals lie in one angular
interval of half-width `alpha<pi/2`. Rotate coordinates so its center is the
positive `y` direction. These sides form one boundary chain, possibly across
the cyclic index cut. Along this chain `x` is monotone and the polygonal graph
`y=f(x)` has Lipschitz constant `a=tan(alpha)`. This includes its long sides.

Let `E` be the union of the `x` projections of sides in this chain of length at
most `M`. For every point on such a short side with endpoints `p,q`,

```math
|(1-t)p+tq|^2
=(1-t)|p|^2+t|q|^2-t(1-t)|p-q|^2
\in[r^2-M^2/4,R^2].
\tag{AA.5}
```

Put `H_M=H+M^2/4`. If `x_1<x_2` both belong to `E` and `x_1>=Ra`, then
`|f(x_i)|<=R` and the Lipschitz bound give

```math
\begin{aligned}
|(x_2,f(x_2))|^2-|(x_1,f(x_1))|^2
&\ge x_2^2-x_1^2-2Ra(x_2-x_1)\\
&=(x_2-Ra)^2-(x_1-Ra)^2\\
&\ge(x_2-x_1)^2.
\end{aligned}
```

Both squared radii belong to the interval in AA.5, so
`diam(E intersect [Ra,infinity))<=sqrt(H_M)`. Reversing signs gives the same
bound on `E intersect (-infinity,-Ra]`. The remaining part lies in an interval
of length `2Ra`. Therefore

```math
|E|\le2Ra+2\sqrt{H_M}.
```

The projected short sides have disjoint interiors by monotonicity. The ratio of
side length to its projected length is at most `sec(alpha)`. Consequently the
**total length of short sides**, including sides separated by arbitrarily long
sides in this same normal interval, is at most

```math
\boxed{
\mathcal L_{\rm short}
\le2\sec\alpha\left[R\tan\alpha+\sqrt{H+M^2/4}\right].
}
\tag{AA.6}
```

This is where disk containment is avoided. A long missing arc cannot be replaced
by short edges for free; its interior is outside `E`. No vertex is silently
inserted in the middle of a long side.

### 3.3 Uniform weighted lattice-vector count

Let `F(t)` count the nonzero lattice vectors of length at most `t`. Disjoint
radius-`1/2` disks around lattice points show

```math
F(t)\le4(t+1/2)^2\le9t^2\qquad(t\ge1),
```

while `F(t)=0` for `t<1`. Integration by parts for the step function gives

```math
\sum_{0<|w|\le T}{1\over|w|}
={F(T)\over T}+\int_1^T{F(t)\over t^2}\,dt
\le18T.
```

Since `2epsilon<=1/4` and `|w|>=1`,

```math
\boxed{
\sum_{0<|w|\le T}{1\over |w|-2\epsilon}\le24T.
}
\tag{AA.7}
```

No angle or determinant hypothesis on the lattice is used beyond minimum spacing.

### 3.4 Passing to a nonconsecutive subset

Replace `Q` by `conv(S)`. Its vertices are exactly `S`, they retain unit separation
and the same annulus, and its diameter is at most `D`. Its perimeter is at most
`pi D` by Cauchy's perimeter formula. This takes care of arbitrary interleaving
of lattice-near and lattice-far vertices in the original hull.

If `|S|<=2`, AA.1 follows from `pi D/M>=pi`; assume `|S|>=3` otherwise.
For each vertex `p_i` choose a lattice site `z_i` within `epsilon`.
These sites are distinct because `|p_i-p_j|>=1>2epsilon`. For a directed side
`d_i=p_{i+1}-p_i` of length at most `M`, let `w_i=z_{i+1}-z_i`. Then

```math
0<|w_i|\le T,\qquad |d_i-w_i|\le2\epsilon,
\qquad |d_i|\ge |w_i|-2\epsilon.
```

The angle between `d_i` and `w_i` is at most `alpha=arcsin(2epsilon)`:
its sine is at most `2epsilon/|d_i|<=2epsilon`, and their scalar product is
positive because `|w_i|>=1` and `2epsilon<=1/4`.

For each fixed directed lattice vector `w`, the normals of all assigned short
sides lie in one interval of half-width `alpha`. By AA.6, their number is at most

```math
{2\sec\alpha[R\tan\alpha+\sqrt{H+M^2/4}]\over|w|-2\epsilon}.
```

Sum using AA.7. There are fewer than `pi D/M` remaining sides of length greater
than `M`. The number of sides equals `|S|`. This proves AA.1. Overlap between
different normal intervals merely overcounts length, which is harmless.

### 3.5 Constants and asymptotics

With `r=D-R`, `H=eta D^2`. For `epsilon<=1/8`,

```math
T\le{5M\over4},\quad
\sec\alpha\le{4\over\sqrt{15}},\quad
\sec\alpha\tan\alpha\le{32\epsilon\over15},\quad
\sqrt{H+M^2/4}\le D\sqrt\eta+M/2.
```

Substitution in AA.1, with `R<=D`, yields the slightly rounded bound

```math
{|S|\over D}
\le{\pi\over M}+128M\epsilon+62M\sqrt\eta+31M^2/D.
\tag{AA.8}
```

Set `t=epsilon+sqrt(eta)`. If `0<t<=1`, choose
`M=min(t^(-1/2),D^(1/3))`; if `t=0`, choose `M=D^(1/3)`.
Then `1/M<=sqrt(t)+D^(-1/3)`, `Mt<=sqrt(t)` and `M^2/D<=D^(-1/3)`.
The resulting coefficients are `pi+128<132` and `pi+31<35`.
Use `sqrt(t)<=sqrt(epsilon)+eta^(1/4)` to obtain AA.2.
If `t>1`, the elementary bound `|S|<=pi D` already implies AA.2.

Canonical FS.1 gives

```math
\eta<2\,3^{1/4}D^{-1/2}.
```

Since `3^(1/4)<4/3` and `(13/10)^4>8/3`,
`(2*3^(1/4))^(1/4)<13/10`, and `132*13/10<172`.
This proves AA.3 with all constants retained.

## 4. Canonical consequences in both branches

Let `B` be the positively diameter-loaded endpoints of the canonical normalized
triangle-free C-II source, and `q=|B|`. C30/C34 gives

```math
q\ge(\lceil D\rceil+2)/2.
```

For any collection of `K` translated lattices of minimum spacing at least one,
let `m` count the endpoints farther than `epsilon` from **all** these lattices.
Apply DS.2 to the subset covered by each lattice and use the union bound:

```math
\boxed{
m\ge q-K[128D\sqrt\epsilon+33D^{2/3}].
}
\tag{DS.3}
```

In particular, for fixed `K` and `epsilon_D -> 0`,

```math
m\ge q-o(D)\ge(1/2-o(1))D.
\tag{DS.4}
```

Using DS.2L gives the additional finite inequality

```math
\boxed{
m\ge q-136KD\epsilon(1+\log(1/\epsilon))-33KD^{2/3}.
}
\tag{DS.5}
```

Therefore even a growing atlas covers only `o(D)` endpoints if

```math
K_D=o(D^{1/3}),\qquad
K_D\epsilon_D(1+\log(1/\epsilon_D))=o(1).
\tag{DS.6}
```

For example, `K_D=O(D^(1/4))` and `epsilon_D=O(D^(-1/3))` meet DS.6. The
unweighted-angle DS.2 does not eliminate that regime. This changes the allowed
chart-complexity regime, rather than improving a decimal carrier coefficient.

The lattices themselves may depend on `D`. There is no full-core or loaded-hull
disk-containment hypothesis. For fixed `K`, choose for example
`epsilon<=(1024K)^(-2)` and then `D>=(264K)^3`. Both error terms in DS.3 are
at most `D/8`, so `m>=D/4`.

### Exact-chart complexity

If `S` lies exactly in one lattice, its strictly convex polygon has at most one
directed side in any oriented vector direction. Consequently it has at most
`9M^2` sides of length at most `M`, and at most `pi D/M` longer sides. Choosing
`M=D^(1/3)` gives

```math
|S|\le(9+\pi)D^{2/3}<13D^{2/3}.
\tag{AA.11}
```

Thus an exact lattice atlas covering the entire canonical `B` needs

```math
\boxed{K\ge D^{1/3}/26.}
\tag{AA.12}
```

This is an elementary lattice-polygon bound proved here, not an imported
equality/uniqueness or lattice-optimality theorem. It also does not assume that
different charts co-embed or that their contacts are compatible.

## 5. Scope/dependency audit

| Claim | Status | Dependency / limitation |
| --- | --- | --- |
| AA.1, AA.2, AA.6, AA.7, AA.11 | New proved candidate, unreviewed | Elementary convex geometry and lattice disk count; Cauchy perimeter bound |
| Actual endpoints are strict extreme vertices and satisfy AA.4, DS.0 | New derivation in this report | Every pair distance at most `D`; actual endpoint status |
| FS.1 circumradius bound | Canonical | `58-full-source-geometry-audit.md`, §1; all source points retained |
| `2q>=ceil(D)+2` | Canonical | `03-pinned-block-and-loaded-boundary-frontier.md`, C30/C34 |
| AA.3 | New proved candidate, unreviewed | FS.1; weaker than DS.2 |
| GC.1 geometric chord exclusion and finite direction capacity | New proved candidate, unreviewed | Actual diameter partners in one source; unit separation; `D>=2` for GC.1 |
| GC.2 | New proved candidate, unreviewed | GC.1 + canonical §63 loaded-hull ledger |
| DS.0--DS.2L | New proved candidate, unreviewed | Actual diameter endpoints and minimum-spacing lattice only |
| DS.3--DS.6, AA.12 | New proved candidate, unreviewed | C30/C34; no FS.1 premise |
| Finite near-exact charts cover `B` except `o(D)` points | Unproved closing premise | Not supplied by phase collapse, one carrier, or density |
| Atlas outliers imply strict source diameter decrease | Unproved | No finite integration or separation certificate provided |

The C30/C34 theorem is invoked on its fully force-visible canonical survivor only.
The DS.2 upper bound is valid for any source, but a lower bound
on a particular selected stress's endpoint count is not silently extended there.
No ZR/ZF matrix is extended over isolated points.

## 6. Attempts to close and exact failures

1. **Extend disk-based lattice-shadow counting to all loaded hulls.** Successful:
   first AA.6 used only the vertex annulus. DS.0 then removed even that premise
   and improved the rate by using actual diameter-partner disks. This is not an
   arbitrary prescribed container or an independently constructed response source.
2. **Apply the counting theorem to all source-hull vertices.** False. The exact
   thin-parabola family below has a linear population of strict extreme vertices
   within a vanishing distance of one lattice. Only two are diameter endpoints.
3. **Obtain a finite loaded-endpoint atlas from the harmonic carrier.** Not proved.
   A large phase-collapsed grain is a statement about one grain's contacts and
   train directions. It does not give lattice sites for every loaded endpoint.
   Absolute displacement can accumulate along long trains, and an `O(D)` interface
   population can contain the entire linear endpoint population required here.
4. **Straighten the same lattice indices.** Rejected before use: PR #582 gives an
   exact Pell-family failure. AA.1 moves no source point and constructs no competitor.
5. **Use the chart obstruction as a deformation theorem.** Not justified. It is a
   counting statement. It has no velocity field, no simultaneous compatibility
   assertion and no nonlinear integration step.
6. **Use actual partners to eliminate loaded interior chords.** Successful:
   GC.1 removes the near-disk/global-optimality premise entirely. This is a new
   source-level hypothesis beyond the arbitrary polygon argument.
7. **Close from chord elimination or direction capacity alone.** Failed: the
   scalar witness following GC.2 leaves high surplus, and global concentration
   of all loaded contact directions is not provided by one phase-pure grid.

### Exact thin-parabola regression

For integer `N>=2`, put `epsilon=N^(-2)` and

```math
p_i=(i,i^2/N^4),\qquad -N\le i\le N.
\tag{AA.R1}
```

All `2N+1` points are strict extreme vertices of their hull: consecutive slopes
are `(2i+1)/N^4` and increase strictly, and the closing chord is horizontal at
height `N^(-2)`. All are within `epsilon` of the square lattice. They are unit
separated since distinct `x` coordinates are distinct integers. Their diameter
is exactly `2N`, realized only by `p_{-N},p_N`. Indeed any other pair has squared
distance at most `(2N-1)^2+N^(-4)<4N^2`.

The circle with center `(0,N^(-2))` and radius `N` encloses the family: for
`|i|<=N-1`, squared radius is at most `(N-1)^2+N^(-4)<N^2`. It is the minimum
circle because it contains the diameter pair. Thus its actual diameter endpoints
satisfy the zero-width radius-`N` annulus, while the middle point does not.

This regression does not challenge AA.1; it violates its vertex-annulus hypothesis
when applied to the full hull. It also lacks supporting radius-`D` partner disks
at its middle vertices, as required by DS.0. The endpoint hypothesis must survive
the canonical transfer. It is not a global-optimality example.

### Binding regressions retained

Stars/non-Eulerian diameter graphs and disconnected grains are allowed; no trail
or connected-grain premise occurs. Arbitrary subsets and large missing arcs are
handled by `conv(S)` and AA.6. Contact-isolated points enter FS.1 and are never
discarded. A regular odd contact ring is consistent with DS.3: it has a linear
number of near-lattice outliers, but the result supplies no global-optimality
certificate for that ring. No selected-stress PSD, positive weight floor, matching
mass bound, near-quadrangulation theorem or RSR uniqueness is used.

## 7. Exact remaining closing lemma

**LECC (loaded-endpoint chart concentration).** There are an absolute integer
`K`, a function `epsilon(D)->0`, and a function `b(D)=o(D)` such that every
sufficiently large canonical triangle-free C-II source admits `K` translated
lattices of minimum spacing at least one for which at most `b(D)` actual loaded
endpoints lie farther than `epsilon(D)` from their union.

The more permissive **LECC-G** allows a growing `K_D`, provided it and the error
obey DS.6 and the uncovered population remains `o(D)`. DS.5 contradicts this
weaker concentration premise too. It allows the concrete powers `K_D=O(D^(1/4))`
and `epsilon_D=O(D^(-1/3))`.

DS.3 would contradict LECC in both branches. Neither LECC nor LECC-G is asserted true. This is the
exact missing global theorem for this route; deriving it from a single carrier
would be the same object/scope error this repository forbids. A weaker theorem
covering fewer than `q-(1/2-o(1))D` endpoints does not close this route.

The original detour and macroscopic-container closure obligations are unchanged.

## 8. Computation and certificates

`research/verify_target_c_annular_atlas_2026_09_26.py` uses rational arithmetic to
verify AA.R1, strict convexity, all separation and diameter constraints, the
minimum-circle certificate, weighted lattice-vector counts, and AA.6 on exact
convex polygons over multiple normal sectors. It also checks DS.0 and the
inner-chain normal-cone argument on exact diameter endpoints, including a
non-Eulerian star with each of its three partner choices at the center.
It verifies GC.1 on 378 exact integer sources, 96 loaded unit contacts and 128
partner choices, and verifies every distance and endpoint claim in GC.R1.
The complete analytic proof above
is independent of the finite checks. They certify no global optimum.

## 9. Frontier effect / promotion recommendation

No canonical theorem state changed. The new candidate removes the loaded-hull
disk-containment and annulus hypotheses from the fixed-finite-chart obstruction, extends it
to the macroscopic-container branch, and quantifies exact-chart complexity.
GC.1 additionally eliminates nonconsecutive loaded unit chords in the
macroscopic-container branch and extends the exact `c_B=0` ledger there.
`C-FULLCORE-LOADED-CHORD` remains valid; its near-disk hypothesis is no longer
needed for the geometric chord conclusion once actual endpoint status is used.
This is a candidate scope extension, not a correction/rejection of its proof.
It does not eliminate either entire C-II branch, construct a competitor, or prove
a unit triangle. No claim in PR #579 is rejected; its statements
under their recorded hypotheses remain separate claims.

**Recommendation: unreviewed.** Independently audit GC.0 and the short-normal arc
in GC.1, the finite ledger extension GC.2, DS.0, the deletion of the first
and last sides in the normal-sector chain, the weighted-angle DS.2L refinement,
AA.6 (in particular long gaps), AA.7, and the scope of C30/C34
before any promotion. If accepted, promote only the proved AA/DS statements with the required
manifest/route/prompt transaction. Do not promote LECC or LECC-G.

## 10. Handoff

Strongest structural theorem: GC.1 eliminates loaded interior unit chords for
every unit-separated source with `D>=2`; GC.2 extends the loaded-hull ledger to
the macroscopic-container branch. DS.2L and DS.5 hold in both canonical C-II branches; AA.12 forces
at least `D^(1/3)/26` exact charts to cover all loaded endpoints. Dependencies:
C30/C34 and §63 for the ledger, with no full-core or circumradius premise. Next exact obligation:
LECC-G or a source-preserving competitor that uses the linear atlas-outlier
population. The thin-parabola regression forbids applying the endpoint bound to
arbitrary hull vertices. Read §§2A and 7 of this report, then the two canonical
modules cited in §1; the wider train library is needed only for an attempted
proof of LECC.
