> Generated reading edition · [exact source](../../../docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md) · source SHA-256 `306324fb6318bebeecfee91b6bf47fa42995089638fc13c3205d6f01a7224d72`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C59E9469EA46","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99: zero transfer, rigidity, and narrow diameter paths

**Date:** 2026-09-09

**Base:** `7838f6c0aabe0e3d63369bda804643c3c7833426`

**Type:** proof draft and adversarial audit, not a canonical promotion

**Level I status:** STILL OPEN

This report proves two finite statements: a zero-transfer/additive-resistance
theorem and a sharp narrow-path theorem. It also records their consequences under
the explicitly stated later Target C inputs. The global problem is not settled.
The audit and remaining branches are in
[the campaign ledger](campaign_ledger_2026-09-09.md).

**Publication reconciliation.** Fetching `origin/main` brought the independently
written [near-path report](target_c_near_diameter_path_unloaded_core_2026-09-09.md)
and [C53 dependency audit](target_c_c53_sign_and_ci_dependency_audit_2026-09-09.md).
Their 15-degree path theorem and short weighted-Robinson PSD proof overlap the
corresponding arguments below; these are parallel derivations, not additional new
advances. The dependency audit also proves convex-deformation connectedness
explicitly and rejects the purported pentagon sign counterexample because its
orientation and ordering used different projective cuts. Its correction agrees
with the consistently oriented enumeration here. Theorem Z and its stated
consequences are separate from those overlapping results. The invalid force-bulk
promotion fetched at the same time was already withdrawn upstream; no bound on
the invisible population is assumed in this report.

The subsequent merged [C-I restoration module](../targets/target-c/56-ci-restored-frontier.md)
now promotes the PSD/integration and lexicographic normal-form inputs. This removes
the former authority conflict for those inputs, not the separate C56 and Theorem Z
audits needed for ZR/ZF. The [consolidated review](campaign_zero_transfer_defect_review_2026-09-09.md)
records the resulting dependency status and the still-open global branches.

## 1. Zero transfer forces an additive resistance metric

### Theorem Z

Let a connected positive circular-planar electrical network have terminal set
`B`, placed at distinct vertices of a strictly convex polygon. Let `H` be a
simple graph on `B`, with no isolated vertices, whose straight chords pairwise
cross or share an endpoint. Suppose `H` has `m>=3` edges. Orient and order these
edges in a common open projective half-plane, and let `Q` be their incidence
matrix. If `R=Lambda^+` and

```math
K=Q^{\mathsf T}RQ
```

is diagonal, the effective-resistance metric on **all** of `B` is additive:

```math
W_{bc}=r_b+r_c\quad(b\ne c),\qquad r_b\ge0.
\tag{Z1}
```

The assertion includes disconnected diameter graphs. It is stronger than
componentwise additivity of a zero-transfer star forest.

### Proof

The circular-planar resistance split theorem gives

```math
W=\sum_A\lambda_A\delta_A,\qquad \lambda_A\ge0,
\tag{Z2}
```

where `A` is a nonempty proper circular interval of terminals and `delta_A` is
one between the two shores and zero within a shore. For
`z_A=Q^T 1_A`, centering the resistance matrix gives

```math
K=\sum_A\lambda_A z_Az_A^{\mathsf T}.
\tag{Z3}
```

This also follows from the weighted spanning-two-forest formula for effective
resistance. Two disjoint trees in a disk cannot have alternating terminal sets;
their nontrivial terminal partition is a circular split.

For any ordered three chords `e<f<g`, the interval-sign inequalities are

```math
z_g(z_e-z_f)\le0,\qquad z_e(z_g-z_f)\le0.
\tag{Z4}
```

These are C53.T. Their complete endpoint-type check is audited in Section 5.
Because `K` is diagonal, for `r<i` we have

```math
0=K_{ri}-K_{r,i+1}
 =\sum_A\lambda_A z_r(z_i-z_{i+1}).
```

Each summand is nonnegative by (Z4), so every positive split has
`z_r(z_i-z_{i+1})=0`. Similarly, for `r>i+1`,

```math
0=K_{ir}-K_{i+1,r}
 =\sum_A\lambda_A z_r(z_i-z_{i+1}),
```

where every summand is nonpositive. Thus, for every positive split and every gap,

```math
z_i\ne z_{i+1}\quad\Longrightarrow\quad
\operatorname{supp}z\subseteq\{i,i+1\}.
\tag{Z5}
```

Apply this at **all** gaps. If `z` is not constant, choose a gap where it changes.
By (Z5) its support has size at most two. If it has size two, both entries at
that gap are nonzero. Since `m>=3`, there is a neighboring gap between one of
those entries and a zero outside the pair. Applying (Z5) there excludes the
other nonzero entry, a contradiction. Consequently every positive split vector
is zero, a singleton, or constant. In the last case it is `1` or `-1`, and its
contribution to `K_{0,m-1}` is positive. The other possibilities contribute zero
to that entry. Since `K_{0,m-1}=0`, constant nonzero splits cannot occur.

It remains to recover the terminal split, rather than identify edge coordinates
with terminal coordinates without proof. A nontrivial circular split with `z=0`
has no `H` edge between its shores. Since every terminal is incident to `H`, each
shore then contains an entire edge. These two chords cannot cross or share an
endpoint: they lie on disjoint circular intervals. This contradicts the thrackle
hypothesis.

If `z` has singleton support, exactly one `H` edge crosses the split. Both shores
cannot contain an internal edge, for the same reason. On a shore with no internal
edge, every terminal must be incident to the unique crossing edge. That shore
therefore consists of one terminal. Every positive split in (Z2) is a singleton
terminal split. Collecting its nonnegative weights proves (Z1). QED.

### Exact invariant change

```math
K=B_H^{-1}
\Longrightarrow W\text{ additive on the complete terminal set}
\Longrightarrow\text{SEPq degree contradiction if }|B|\ge6.
```

The existing C56.7 conclusion allowed one-edge or two-adjacent-edge split support.
Applying its equality condition at every gap eliminates the two-edge option.
The final shore argument is needed to get additivity on all terminals.

### Small-support limits

The condition `m>=3` cannot be deleted by this proof. For two crossing edges on
four cyclic terminals, a four-cycle with equal conductances has diagonal transfer
between the two opposite pairs, while its resistance metric is not additive.
For unit conductances, adjacent resistances are `3/4` and opposite resistances
are `1`. Additivity would give both opposite-pair and adjacent-pair sums equal;
instead these are `2` and `3/2`.

The terminal-cover hypothesis is also essential. Add an unselected terminal on
an edge of an additive-star network. Its additional split may have `z=0` and
need not be a singleton split of the enlarged terminal set.

## 2. Consequences for later Target C normal forms

This section explicitly uses the later C53, C54, C56, C63, and C65/C86 results.
They are not treated as authoritative merely because they have larger numbers.
Section 5 audits the mathematical mechanisms; the route-map conflict is recorded
in the ledger. The statements below have these dependencies, rather than silently
changing the older route map's gates.

### Corollary ZC: zero transfer is excluded in the large C-II branch

In the contact-minimal, fully force-visible C-II source, choose a relative-interior
normalized KKT stress. If `D>=9`, C34 gives

```math
2q\ge\lceil D\rceil+2,
```

so `q>=6` and `m=|H_+|>=3`. The actual positive contact graph is connected and
circular-planar with terminal set `B_+`. All terminals are extreme and all
diameter chords form a thrackle. If this stress were C56-Z, Theorem Z would make
its resistance metric additive. SEPq would give a contact vertex incident to at
least `q` edges if unloaded, or `q-1` if loaded. These contradict the respective
contact-degree bounds `5` and `3`. Thus C56-Z is impossible for this stress.

Notice that this is a theorem about the **relative-interior C-II stress**. It
does not exclude every non-maximal selected stress by borrowing C34 for that
smaller support.

### Corollary ZR: maximal scalar stress rank

Under the same hypotheses the scalar stress matrix on the `v` nonisolated core
vertices has

```math
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad \operatorname{rank}\Omega=v-3.
\tag{ZR1}
```

Proof: ZC excludes C56-Z, so C56-G says that the edge defect has nullity two.
On the zero-sum terminal space set

```math
Y=\Lambda^{-1/2}QB_H^{1/2}.
```

The matrices `I-Y^T Y` and `I-YY^T` have the same multiplicity of the zero
eigenvalue, namely two, by the singular-value decomposition. Congruence identifies
the latter with `Lambda-L_H` on that space. Restoring constants adds one kernel
dimension. Schur elimination of the positive contact Laplacian's interior block
preserves nullity. The three displayed affine coordinate functions are already in
the stress kernel by equilibrium, and they are independent because the force hull
is two-dimensional. This proves (ZR1).

### Corollary ZF: rigidity of a lexicographically minimal C-II core

Choose, among contact-minimal triangle-free global minimizers, one with the least
number of diameter pairs. Then, under C53/C54/C63, for `D>=9` the framework on its
nonisolated core with both contact and diameter pairs treated as bars is
infinitesimally rigid. In particular, writing `e` for the number of contacts and
`h` for the number of diameter pairs,

```math
e+h\ge2v-2.
\tag{ZF1}
```

Proof: C63 integrates every relative-interior critical velocity by an `O(t^2)`
correction. Contact minimality eliminates weak contacts; minimizing diameter-pair
count eliminates weak diameter rows in precisely the same way. For any critical
velocity `u`, use the integration construction on all active rows. At sufficiently
small displacement no inactive row can activate. Therefore no active contact or
diameter pair can be lost, by the two minimality choices. The resulting points
`p+x(t)`, with `x(t)=tu+O(t^2)`, preserve every active length exactly.

Sum the signed squared-length identities with the relative-interior stress.
Since `Omega p=0`,

```math
0=\sum_C\alpha_e(|(p+x)_e|^2-1)
 -\sum_H\beta_h(|(p+x)_h|^2-D^2)
 =\sum_{k=1}^2x_k^{\mathsf T}\Omega x_k.
```

PSD and division by `t^2` give `Omega u_k=0` for both coordinates. By ZR,
`u_i=b+Ap_i`. Each active diameter has zero radial first variation, so
`r^T(A+A^T)r=0` on at least three distinct projective directions. A nonzero
homogeneous quadratic in two variables has at most two projective zeros.
Thus `A+A^T=0`, and `u` is Euclidean on the core. Conversely, every infinitesimal
bar flex is critical. This proves infinitesimal rigidity.

The bar rigidity matrix has rank `2v-3` and has a nonzero signed KKT dependence
between its rows. Hence it has at least `2v-2` rows, proving (ZF1). Isolated
points are not counted in `v`; they are not mistakenly made rigid by this proof.

Combining (ZF1) with the canonical penny-graph bound
`e<=2v-delta-2` yields the additional necessary condition

```math
h\ge\delta\ge\lceil D\rceil.
\tag{ZF2}
```

### Corollary ZB: pure rhombic disk exclusion

Under the same audited later-C inputs, there cannot be an unbounded sequence of
contact-minimal triangle-free global minimizers whose complete contact graph is
a pure simply connected strict-rhombic disk on all source points.

Proof: Fix a cardinality for which this class is nonempty and, within the class
of contact-minimal pure-disk representatives, minimize the number of diameter
pairs. The integer minimum exists without a compactness assumption. The C63
small local constructions cannot create any new contacts; contact minimality
therefore preserves every contact. They preserve the embedded pure disk for
sufficiently small displacement. Consequently the diameter-count argument in ZF
applies within this class, rather than replacing the pure disk by an unrelated
global minimizer.

Let `R,T,q` denote rhombi, trains, and hull vertices. The exact identities are

```math
v=R+T+1,\qquad e=2R+T=2v-T-2,\qquad h\le q.
```

Equation (ZF1) implies `h>=T`, hence `q>=T`. But the audited exposed-hull
theorem in Target B Section 39 gives along every such unbounded sequence

```math
\liminf\frac{T-q}{D}
\ge\frac{4-\pi\sqrt{2\sqrt3/\pi}}
 {2\sqrt{2\sqrt3/\pi}}>0.
```

Its positive leading coefficient makes `T>q` for all sufficiently large members,
a contradiction. Here an asymptotic estimate is used only with a fixed linear
margin, not to resolve a one-integer equality with an uncontrolled error. QED.

This conclusion covers every coherent phase regime **within this pure canonical
class**. It does not establish that an arbitrary global minimizer, or even every
jammed source, has this topology. Exceptional faces, several rhombic components,
and isolated points remain outside the conclusion.

## 3. A sharp narrow-path theorem independent of KKT

### Theorem P

Let `A` be a finite planar set of diameter `D>0`, containing `z=(0,0)` and
`a=(D,0)`. Suppose a polygonal path in `A` joins `z` to `a` and every oriented
edge makes angle at most `theta<pi/12` with the positive horizontal direction.
No internal path vertex is incident to a diameter pair of `A`.

More precisely, for `x=(t,h)` with `0<t<D`, put `m=min(t,D-t)` and suppose
`|h|<=r m`, where `0<=r<2-sqrt(3)`. Then for every `y in A`,

```math
|x-y|^2\le D^2-Dm\left(\frac12-\sqrt3r-\frac{r^2}{2}\right)<D^2.
\tag{P1}
```

Proof: `y` belongs to the intersection of the two radius-`D` endpoint disks, so
`|y_2|<=sqrt(3)D/2`. With `x_0=(t,0)`, the exact convex-combination identity is

```math
|x_0-y|^2
=(1-t/D)|z-y|^2+(t/D)|a-y|^2-t(D-t).
```

Thus

```math
|x-y|^2\le D^2-t(D-t)+\sqrt3D|h|+h^2.
```

Since `t(D-t)=m(D-m)`, `m<=D/2`, and `|h|<=rm`, the deficit from `D^2` is at
least `Dm[1/2-sqrt(3)r-r^2/2]`. The bracket is positive exactly in the stated
nonnegative range. Along the path all horizontal increments are positive. Summing
the slope bound separately from each endpoint gives
`|h|<=tan(theta) min(t,D-t)`, proving the theorem. QED.

### Sharp triangle-free packing regression at equality

Let `M>=2` be an integer, `c=cos(pi/12)`, `s=sin(pi/12)`, and set

```math
x_j=(jc,js)\quad(0\le j\le M),
\qquad x_{M+j}=((M+j)c,(M-j)s)\quad(0\le j\le M).
```

Adjoin `y=(Mc,-sqrt(3)Mc)`. The diameter is `D=2Mc`. The four corners
`x_0,x_M,x_{2M},y` have all pairwise distances at most `D`; in particular
`|y-x_M|=M(s+sqrt(3)c)=2Mc=D`. All other points lie on the two upper corner
segments, so their distances are at most `D` by convexity. Consecutive path
distances are one; nonconsecutive path points have horizontal separation at least
`2c>1`. The vertical separation of `y` from the path is at least
`sqrt(3)Mc>1`. Thus the contact graph is exactly a path, with no unit triangle.
Its internal apex is a diameter endpoint and all path edges have angles exactly
`+pi/12` or `-pi/12`.

These sets are not globally optimal. They have `n=2M+2` and
`D^2=M^2(2+sqrt(3))>3M^2`, whereas the triangular-lattice bound gives
`D(n)^2<(2sqrt(3)/pi)(2M+1)<(6/5)(2M+1)<3M^2` for `M>=2`.
No global-optimality counterexample is being claimed.

### Proposition N: exact approximation without attainment

For every fixed `n>=3`, the infimum of diameter over unit-separated triangle-free
`n`-point configurations with minimum distance **exactly one** equals `D(n)`.
In fact configurations with exactly one unit pair attain diameters arbitrarily
close to `D(n)` from above (or equal to it if an appropriate optimum exists).

Proof: Take any global minimizer `p_1,...,p_n`. Its minimum distance is one,
since otherwise uniform contraction improves its diameter. Set
`p_i(t)=p_i+t(2^i,0)`. For any two different unordered pairs, the difference of
their squared-distance polynomials in `t` has nonzero quadratic coefficient:
the numbers `|2^i-2^j|` are distinct for distinct pairs, as follows by factoring
out the largest power of two. Thus only finitely many nonzero values of `t`
produce any distance tie. For all sufficiently small positive `t`, all pair
distances are distinct and their minimum `d(t)` tends to one. Divide every
coordinate by `d(t)`. The normalized configuration is unit-separated with a
unique unit pair, is triangle-free, and has diameter tending to `D(n)`. The
reverse infimum inequality is the definition of `D(n)`. QED.

This disproves any proposed positive diameter gap separating **all** triangle-free
feasible sets from `D(n)`, even at one fixed cardinality and even after requiring
minimum distance exactly one. It is not a disproof of Problem #99: the infimum
need not be attained in the triangle-free subset. The original question concerns
exact attainment, which neither asymptotic approximation nor taking a limit
preserves. This argument does not assert that its approximants are jammed or have
the same active graph as the original minimizer.

### C102 implication and its limit

C100's separator path has angle bound `arcsin((1-b)/b)` when the primary diameter
weight is `b`. If

```math
b>\frac1{1+\sin(\pi/12)},
\tag{P2}
```

Theorem P makes every internal path vertex non-diametral. In a fully visible core
it is consequently an unloaded, nonextreme vertex. This removes that particular
uncertainty from the near-chain frontier. It does **not** infer degree four from
an almost-straight path: degree-five rhombic stars can have nearly opposite rays.
Nor does it turn `k-D=O(D(1-b)^2)` into the exact equality `k=D`.

## 4. Exact computation

Run [the standard-library verifier](../../../research/campaign_2026_09_09_exact.py):

```sh
python3 research/campaign_2026_09_09_exact.py
```

It verifies:

- 228174 chord/interval instances on integer convex polygons with 3 through 8
  vertices, including every projective cut of each triple;
- all `{-1,0,1}` all-gap equality signatures for 3 through 8 edges;
- all 273 noncrossing unit-resistance trees on six cyclic terminals, for a fixed
  three-edge crossing matching: diagonal transfer occurs in exactly the six
  terminal-centered stars; it also checks the two-edge four-cycle exception;
- every pair distance in the sharp packing family for `M=2,...,25`, exactly in
  `Q(sqrt(3))`, including the full unit-contact graph and apex diameter.

The proof for all `M` is above; the finite runs check transcription and omitted
pairs. No floating-point certificate is used by these statements.

## 5. Audit of the later C dependencies

### C53 interval signs

Three pairwise intersecting distinct convex chords have only five endpoint
types: triangle, star, crossing-ended path, a shared pair crossed by a third edge,
and a three-edge matching. Representatives in cyclic vertex labels are
`01,12,02`; `01,02,03`; `02,03,13`; `02,03,14`; and `03,14,25`.
Convex deformation cannot interchange projective chord directions: parallel
disjoint chords cannot cross, and parallel incident chords would put three convex
vertices on a line. For each representative, walking an interval's two endpoints
around the cyclic order, for the three projective cuts, gives only

```
--- --0 --+ -00 -0+ -++ 0-- 0-0 00- 000 00+ 0+0 0++
+-- +0- +00 ++- ++0 +++
```

where signs denote `-1,0,1`. Substitution proves (Z4). The rational-polygon
enumeration is an additional check, not a replacement for endpoint classification.

### C53 PSD: a shorter weighted-Robinson proof

The affine response identity gives `M1=Mt=0` for a symmetric matrix with
`M_ij=-gamma_i gamma_j K_ij` off the diagonal, positive `gamma`, and strictly
increasing `t`. Let `D_0` be first differences and `T_0` their cumulative right
inverse with first coordinate zero. Set

```math
H_0=D_0\Gamma^{-1}MT_0.
```

For `k<i` and `k>i`, respectively, its off-diagonal entries are

```math
-(\sum_{r\le k}\gamma_r(K_{ir}-K_{i+1,r})),\qquad
\sum_{r>k}\gamma_r(K_{ir}-K_{i+1,r}).
```

Both are nonpositive by Robinson monotonicity. Also
`H_0(D_0t)=0` with `D_0t>0`. Positive diagonal similarity therefore makes `H_0`
a matrix with nonpositive off-diagonal entries and zero row sums. Gershgorin's
theorem puts its eigenvalues in the closed right half-plane.

Since `M1=0`, `H_0` represents `Gamma^{-1}M` on the quotient by constants.
All its eigenvalues are real: `Gamma^{-1}M` is similar to the symmetric matrix
`Gamma^{-1/2} M Gamma^{-1/2}`. The eigenvalues are therefore nonnegative, including
the missing constant eigenvalue zero, proving `M` PSD. The singular-value and
Schur congruences used in ZR give the full stress PSD. This proof retains unequal
positive weights and does not assume that a raw long-range cross-cut coupling has
a prescribed sign.

The one-dimensional support case is a straight unit-contact chain between diameter
endpoints. Its stress inequality is Cauchy-Schwarz along that chain. Combined with
canonical positive-support connectivity, these arguments establish the arbitrary
displacement PSD hypothesis used by C63 for every normalized stress, rather than
just for one selected stress or for critical velocities.

### C56 kernel simplicity

The complete weighted proof is in
[C56](target_c_minimum_transfer_kernel_collapse_2026-08-31.md), Sections 2–3.
The decisive checks are these. Put `c=min_{i!=j}K_ij` and `A_ij=K_ij-c`.
Then

```math
L_A=M-c(G\Gamma-\gamma\gamma^{\mathsf T}),\qquad G=\sum_i\gamma_i.
```

Centering `t` in the weighted mean gives eigenvalue `-cG`, so `c<=0`.
If `c=0`, the energy sum with distinct `t_i` makes every off-diagonal `K_ij`
zero. If `c<0`, PSD of `M` makes `-cG` the positive Fiedler value of `L_A`,
and `A` is irreducible. The plateau argument in C56.1–3 proves its simplicity:
a second Fiedler vector would give, by rotation with the strictly increasing
one, a nondecreasing Fiedler vector with a proper constant interval. Comparing
the equations at the plateau endpoints forces equal similarities to every outside
vertex. Replacing all within-interval similarities by the endpoint minimum gives
an invariant within-interval mean-zero eigenspace at `mu`; the two Rayleigh tests
in C56.14–16 give `lambda_2<mu`. Hence **every** Fiedler vector is constant on
that interval, contradicting the strict vector. No unweighted-to-weighted inference
is left implicit in this argument.

### C63 integration

Write strong signed constraints exactly as `g(x)=A_*x+Q_*(x)`. Every nonzero
`lambda>=0` with `lambda^T A_*=0` has positive total diameter coefficient: a pure
nonnegative unit-contact stress vanishes on taking its scalar product with the
configuration. It therefore normalizes to a KKT stress, and the PSD proof gives
`lambda^T Q_*(x)>=0` for **every** displacement `x`.

Farkas consequently makes `A_* y>=-g(x)` feasible at every iterate. The fixed
matrix Hoffman bound supplies a solution with
`||y||<=H ||g(x)_-||`. For a constant `L`,

```math
\|Q_*(x+y)-Q_*(x)\|
\le L(\|x\|\|y\|+\|y\|^2).
```

Starting at `x_0=tu`, `A_*u=0`, gives violation `O(t^2)`. Choose `t` so small
that all iterates within `2t||u||+O(t^2)` have contraction factor below `1/2`.
The sum of corrections is then `O(t^2)` and the iterates converge to a feasible
point `tu+O(t^2)`. A relative-interior critical velocity has strictly positive
linear slack at every weak active row, so these survive the correction; inactive
rows retain their original strict slack. This proves the finite release, not just
the existence of second-order jets. Contact minimality gives C-I closure, and
the additional diameter-count minimization gives the version needed in ZF.

Hoffman's constant may depend arbitrarily on this finite source. No uniform rate
in `D` is used. The iteration tests all equilibrium multipliers and therefore does
not replace direction-dependent second-order stresses by one selected stress.

## 6. Dependencies and promotion status

- Theorem Z: the finite circular-planar resistance split theorem, and the fully
  checked C53.T chord-sign lemma. No global packing hypothesis is used.
- ZC: Theorem Z, canonical C34 endpoint count and SEPq separator, and the C-II
  contact-degree bounds.
- ZR: ZC and the audited C53/C56 kernel calculation.
- ZF: ZR, the audited C63 integration, and the stated lexicographic minimality.
- ZB: ZF, exact pure-disk Euler counts, and Target B Section 39.
- Theorem P and its sharp family: the displayed elementary distance identities.

External sources checked for exact hypothesis fit:

- Stefan Forcey, *Circular Planar Electrical Networks, Split Systems, and
  Phylogenetic Networks*, [arXiv:2108.00550](https://arxiv.org/abs/2108.00550),
  Theorem 4.2 in the author manuscript: a connected positive circular-planar
  response gives a Kalmanson resistance metric and nonnegative circular split
  representation. Only this direction is used; arbitrary Kalmanson metrics are
  not asserted to be electrical.
- The fixed-matrix Hoffman theorem used by C63 is Proposition 1 of Peña, Vera,
  and Zuluaga, [arXiv:1905.02894](https://arxiv.org/abs/1905.02894). The matrix is
  fixed, the feasible right-hand side varies, and no uniformity across sources
  is claimed.
- SEPq retains its exact circular-minor and Gallai dependencies as proved in
  [the existing separator report](target_c_additive_response_separator_obstruction_2026-08-31.md).

**Hold as report.** No route map or prompt is silently rewritten by this file.
The proposed promotion should distinguish the two new finite theorems from the
normal-form consequences, and explicitly resolve the older C route map against
the audited C53–C63 mechanism. Even if all these consequences are promoted, the
general topology and isolated-source-point branches remain open.
