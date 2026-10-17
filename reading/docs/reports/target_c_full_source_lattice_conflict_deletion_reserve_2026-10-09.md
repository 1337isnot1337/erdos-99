> Generated reading edition · [exact source](../../../docs/reports/target_c_full_source_lattice_conflict_deletion_reserve_2026-10-09.md) · source SHA-256 `a8e0334ad495eb5e4eefda1d1b4a1a5a1bf3a14e5851ef46e99cd4d2bfca70a2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8C2BF4386344","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# A two-thirds-power global population reserve by lattice conflict deletion

Date: 2026-10-09. Research base:
`0a71e1141c5af3b644dad858d584494556f55c5e`, state
`2026-10-09.audit.181`.

Classification: **proved candidate awaiting independent audit/promotion**.
Artifact lifecycle: unreviewed. This changes no canonical theorem state.

## 1. Exact implication chain

```text
uniform O(r^(2/3)) triangular-lattice disk discrepancy
  -> O(D^(2/3)) candidate difference vectors in a thin outer annulus
  -> O(c^(3/2) D^(2/3)) expected diameter conflicts
     in a disk enlarged by c D^(-1/3)
  -> keep the linear-in-c population gain after deleting conflicts
  -> a strict-sub-D lattice competitor with density + kappa D^(2/3) sites
  -> every global minimizer has g_A >= kappa D^(2/3).
```

No source embedding, unit-contact graph, stress, triangle-free condition,
or container access premise enters this comparison. It is a stronger
candidate population reserve than canonical Audit.165's square-root
reserve. It does not by itself prove that a global minimizer contains
a unit triangle. The comparison packing can contain many such triangles.

## 2. Uniform disk discrepancy, including open and closed boundaries

Let `Lambda` be the unit triangular lattice, with covolume
`a0=sqrt(3)/2`. There is a fixed finite constant `C_disk` such
that, for every translation and every `r>=2`, both open and closed
radius-r disk counts obey

$$
 \left|N_r-\pi r^2/a_0\right|\le C_{disk}r^{2/3}. \tag{2.1}
$$

Only this classical exponent is needed; no sharp Gauss-circle estimate
or explicit optimal constant is claimed.

**Proof included to specify the dependency.** Use a nonnegative smooth
unit-integral function `psi` supported in the open unit disk, and
`psi_t(x)=t^(-2)psi(x/t)`. For a disk of radius `R`, the
divergence theorem and a stationary/nonstationary split of its boundary
give

$$
 |\widehat{1_{B_R}}(\xi)|\le C\sqrt R\,|\xi|^{-3/2}.
$$

Indeed, after rotating the frequency, boundary arcs within angular
distance `eta` of the two stationary tangents have length `O(R eta)`.
On each remaining quadrant the phase derivative has one sign, is
monotone, and has magnitude at least `|xi| eta`. Integration by
parts, including the bounded variation of the normal-coordinate
amplitude, bounds its boundary integral by `O(1/(|xi| eta))`.
The divergence prefactor is `O(1/|xi|)`. Choosing
`eta=(R|xi|)^(-1/2)` proves the estimate when `R|xi|` is large;
the direct perimeter bound covers its remaining bounded range.

The reciprocal lattice is uniformly separated and has `O(T^2)`
points in a radius-T disk. Dyadic summation and smooth bump decay give

$$
 \sum_{k\in\Lambda^*\setminus0}|k|^{-3/2}
                 (1+t|k|)^{-3}=O(t^{-1/2}).
$$

Periodize the smooth compactly supported convolution
`1_(B_R)*psi_t` over the lattice. Its Fourier series converges
absolutely by the preceding estimate, giving, uniformly in translation,

$$
 \left|\sum_{x\in\Lambda+z}(1_{B_R}*\psi_t)(x)
                -\pi R^2/a_0\right|
       \le C\sqrt R\,t^{-1/2}. \tag{2.2}
$$

Sandwich the open and closed disk counts between the convolutions for
radius `r-t` and `r+t`. The inner convolution is supported inside
the open radius-r disk and is at most one; the outer convolution is
one on the closed radius-r disk. Take `t=r^(-1/3)`. The area
errors are `O(rt+t^2)=O(r^(2/3))`, and the Fourier errors in
(2.2) are also `O(r^(2/3))`. This proves (2.1), with a finite
constant independent of the translation. QED.

This reconstructs the disk specialization of the Fourier mechanism in
the local curved-boundary capacity report. Boundary points are not
discarded by an unsupported generic-position assumption: both open
and closed counts satisfy the same bound.

## 3. A thin lens has small translation-averaged conflict cost

For radius `S` and center separation `d<=2S`, put `epsilon=2S-d`.
The intersection of their disks has area at most

$$
 A_{lens}(S,d)\le(4/3)\sqrt S\,\epsilon^{3/2}. \tag{3.1}
$$

To see this, center the disks at `(+d/2,0),(-d/2,0)`.
At abscissa `x` with `|x|<=epsilon/2`, their common half-height
is at most `sqrt(2S(epsilon/2-|x|))`. Integrating this upper
bound over the two half-intervals gives (3.1).

Choose a fixed parameter `0<c<=1`, put

$$
 \delta=cD^{-1/3},\qquad S=D/2+\delta,
 \quad D\ge2.
$$

A pair of lattice sites in the open radius-S disk whose separation
is at least D has a difference vector in

$$
 \mathcal W=\{w\in\Lambda:D\le|w|<D+2\delta\}.
$$

By (2.1), applied with an open inner and closed outer count,

$$
 \begin{aligned}
 |\mathcal W|
 &\le {\pi\over a_0}\{(D+2\delta)^2-D^2\}
       +C_{disk}\{(D+2\delta)^{2/3}+D^{2/3}\}\\
 &\le K_0D^{2/3},\qquad
 K_0=8\pi/a_0+3C_{disk}. \tag{3.2}
 \end{aligned}
$$

We used `D+2delta<=2D`, `c<=1`, and `D>=2`. Difference
vectors of length *exactly* D are included, as strict diameter
below D is needed at the endpoint.

For every `w in W`, (3.1), `S<=D`, and `2S-|w|<=2delta`
give

$$
 A_{lens}(S,|w|)\le(8\sqrt2/3)c^{3/2}. \tag{3.3}
$$

Translate the lattice uniformly over a fundamental parallelogram.
Let `N(z)` count its points in the open radius-S disk, and let
`E(z)` count unordered pairs among these points at distance at
least D. Unfolding the lattice sums gives exactly

$$
 \mathbb EN=\pi S^2/a_0,\qquad
 \mathbb EE={1\over2a_0}\sum_{w\in\mathcal W}
                              A_{lens}(S,|w|).
$$

The factor two removes ordered-pair duplication. All sums are finite,
so no limiting interchange or pointwise Poisson assertion is required
for these expectations. Equations (3.2)--(3.3) imply

$$
 \mathbb EE\le K_1c^{3/2}D^{2/3},\qquad
 K_1={4\sqrt2\over3a_0}K_0. \tag{3.4}
$$

## 4. Keep the population gain by deleting one vertex per conflict

**Theorem 4.1 (strict-diameter lattice competitor).** There are
absolute constants `kappa>0` and `D0` such that, for every
`D>=D0`, some finite unit-separated subset of the triangular
lattice has diameter strictly below D and cardinality at least

$$
 \boxed{\pi D^2/(2\sqrt3)+\kappa D^{2/3}.} \tag{4.1}
$$

The finite constants established above permit `D0=2`; leaving the
onset unnamed does not affect the asymptotic application.

**Proof.** Set `A1=pi/a0`, choose

$$
 c=\min\{1,(A_1/(2K_1))^2\},\qquad
 \kappa=A_1c/2>0.
$$

Then (3.4) and the exact mean count give

$$
 \begin{aligned}
 \mathbb E(N-E)
 &\ge {\pi D^2\over4a_0}
        +(A_1c-K_1c^{3/2})D^{2/3}
        +\pi\delta^2/a_0\\
 &\ge {\pi D^2\over4a_0}+\kappa D^{2/3}. \tag{4.2}
 \end{aligned}
$$

Choose a translation for which the integer `N-E` is at least
its mean. In its finite conflict graph delete one chosen endpoint
of every conflict edge; the union of deleted endpoints has size
at most E. The remaining sites therefore number at least `N-E`.
They retain unit lattice separation, and every remaining pair has
distance strictly less than D, since every pair at distance at
least D was a conflict edge with a deleted endpoint. Equation
(4.2) proves (4.1). Translation can be removed from the retained
configuration without changing any distance. QED.

This is a whole new competitor, not a local modification of an
arbitrary source. Deletion is used only inside that independent
comparison lattice. It does not delete or omit any original
source label in a source-level exchange.

### 4.2 The independent competitor can also be made triangle-free

For every finite lattice subset supplied above, deform the triangular
basis `u,v` from angle `pi/3` to `pi/3+epsilon`, keeping both
basis vectors unit. Choose epsilon positive and sufficiently small
for this finite subset. Differences in directions `u,v` stay unit;
the former unit difference `v-u` becomes strictly longer than one.
All other old lattice differences were strictly longer than one
and remain so by continuity. The strict diameter margin in Theorem
4.1 likewise persists for a sufficiently small positive epsilon.

The new unit-contact graph uses only index differences `(1,0)`
and `(0,1)`, with either sign. It is bipartite by the parity of
the index sum, hence triangle-free. Cardinality is unchanged.
No source-uniform deformation size or global optimality is claimed.

Thus even *triangle-free* comparison packings can have the population
excess in (4.1). A universal density upper bound for all triangle-free
packings cannot close the problem. The missing hypothesis in any
such closing bound must use actual global optimality or the canonical
loaded contact/stress geometry.

## 5. Consequence for every global diameter minimizer

**Theorem 5.1 (candidate stronger global reserve).** With the same
absolute kappa and onset, every planar unit-separated global
n-point diameter minimizer with diameter D satisfies

$$
 \boxed{g_A:=n-1-\pi D^2/(2\sqrt3)\ge\kappa D^{2/3}.} \tag{5.1}
$$

**Proof.** The comparison configuration in Theorem 4.1 has some
integer cardinality M and diameter strictly below D. If `M>=n`,
retaining any n of its sites would contradict global minimum
diameter. Hence `M<=n-1`. Combining that integer inequality
with (4.1) proves (5.1), with no rounding loss. QED.

The same bound transports into the exact canonical full-source Oler
ledger, retaining every isolate:

$$
 \delta_K+O_A=c_0P-a_0g_A
       \le c_0P-a_0\kappa D^{2/3},
 \quad c_0=\sqrt3/4.
$$

This strengthens the sublinear reserve, while the leading allowance
is still of order D. Existing linear face/interface deficits are
not eliminated by this estimate. No conclusion about all global
minimizers having a triangle, no C-II closure, and no Level I
solution is claimed.

As a diameter upper bound, put `d0=pi/(2sqrt(3))` and
`T=sqrt((n-1)/d0)`. For all sufficiently large n, (5.1) yields

$$
 D(n)\le T-c_1T^{-1/3},\qquad
 c_1=\kappa/(2^{5/3}d_0)>0.
$$

Indeed, if `D>T/2`, divide
`d0(T^2-D^2)>=kappa D^(2/3)` by `d0(T+D)`; if
`D<=T/2`, the displayed upper bound already holds for large T.
Thus the constructive improvement below the leading square-root
diameter is of order `n^(-1/6)`. This is a population comparison,
not a classification of the optimal configuration.

## 6. Audit priorities and computation boundary

The bridge to audit is the conflict cost: count *difference vectors*
in the thin annulus, multiply each by its translated-disk lens area,
and include distance-D ties before selecting the independent set.
An upper bound on the outer bank alone is insufficient; the exact
pair expectation supplies the `c^(3/2)` cost that makes a small
fixed parameter profitable. No uniform arithmetic sparsity in
individual circles is assumed.

All universal claims are supplied by the analytic arguments above.
No finite enumeration or numerical optimization is offered as a
proof certificate. The constants are explicit functions of one
finite disk-discrepancy constant, not numerically optimized values.
All assertions remain unreviewed pending independent audit and the
repository's promotion procedure.

## 7. A tight unit-edge shell with one lattice interior is excluded

This section uses one additional literature input. The resulting claim is
also a **proved candidate awaiting independent audit/promotion**. It is
not a crystallization theorem for an arbitrary canonical source.

### 7.1 The literature input and its precise scope

Use the translated-oval discrepancy statement in Martin Huxley's own
[Configurations of Lattice Points, Oberwolfach Report 14/2008,
pp. 703--704, Theorem A](https://ems.press/content/serial-article-files/46159?nt=1).
It states the exponent `131/208` for smooth dilated ovals, with a
translation parameter and an arbitrary fixed planar lattice; it points
to [Exponential sums and lattice points III, PLMS 87 (2003),
591--609](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/S0024611503014485).
Only a fixed circle, or its fixed elliptical image after changing
lattice coordinates, is needed here. Its boundary is smooth with
strictly positive curvature. Fix any

$$
 131/208<\theta<2/3.
$$

The input gives, uniformly in the translation `z`,

$$
 \#\big((z+\Lambda)\cap\overline B(o,r)\big)
  ={\pi r^2\over a_0}+O(1+r^\theta).                 \tag{7.1}
$$

Closed boundaries can equivalently be handled by enlarging the radius
by `r^(-2)` and passing the upper bound to the limit; the resulting area
increment is `O(r^(-1))`. Rotation of this particular lattice causes no
new family of ovals, since the physical domain is a disk. Scaling the
lattice by `lambda>=1` replaces `r` by `r/lambda`. The constant in (7.1)
therefore remains uniform in the scaling, center, and orientation.
The original 2003 full proof was not obtained through the publisher;
the imported statement is the author's primary transcription above.

### 7.2 The exact unit-edge guard

Let F be a convex polygon whose successive vertices are source points
and whose boundary edges all have length one. Every other source point
`x` in F has

$$
 \operatorname{dist}(x,\partial F)\ge a_0=\sqrt3/2. \tag{7.2}
$$

Indeed, a closest boundary point is either a vertex, at distance at
least one, or an interior point of a unit edge. In the latter case
write the projection coordinate as `t in [0,1]` and the perpendicular
distance as h. Separation from both endpoints gives

$$
 h^2\ge\max\{1-t^2,1-(1-t)^2\}\ge3/4.
$$

This includes all retained isolates, independently of contact loading.
It also shows that there are no other source points on these edges.

### 7.3 A quantitative necessary circumradius excess

Suppose a unit-separated global minimizer A has a convex hull F with
q unit boundary edges, and every non-hull source point belongs to one
translated, rotated triangular lattice of spacing `lambda>=1`.
Let R be the radius of any disk containing F. For large diameter D,

$$
 \boxed{R^2-D^2/4\ \ge c D^{2/3}}                 \tag{7.3}
$$

for an absolute `c>0` and sufficiently large onset (depending on the
fixed discrepancy constant). In particular the circumradius cannot
be `D/2+o(D^(-1/3))` in this scope.

**Proof.** By (7.2), the interior source points lie in the eroded body
`F minus a0 B`. If a containing disk is centered at o, the inclusion
`x+a0 B subset F subset B(o,R)` gives `|x-o|<=R-a0`. Equation
(7.1), including the spacing reduction, bounds their number by

$$
 {\pi(R-a_0)^2\over a_0}+O(1+R^\theta).
$$

The convex perimeter inequality gives `q=P(F)<=2pi R`. Consequently

$$
 n\le {\pi R^2\over a_0}+\pi a_0+O(1+R^\theta).   \tag{7.4}
$$

If `R>=D`, (7.3) follows immediately. Otherwise `R=O(D)`, and
Theorem 5.1 and (7.4) yield

$$
 \kappa D^{2/3}\le g_A
 \le {\pi\over a_0}(R^2-D^2/4)+O(1+D^\theta).
$$

Since `theta<2/3`, choose for example `c=a0 kappa/(2pi)` after
increasing the onset. This proves (7.3). QED.

### 7.4 Regular odd unit shells: no radial buffer beyond the guard

For odd `q>=3`, let B be the vertices of the regular q-gon of unit
side. Its circumradius and diameter satisfy exactly

$$
 R={1\over2\sin(\pi/q)},\qquad
 D={1\over2\sin(\pi/(2q))},\qquad
 R^2-D^2/4={1\over16\cos^2(\pi/(2q))}\le1/12.      \tag{7.5}
$$

If every additional source point is inside this polygon and belongs
to one triangular lattice of spacing at least one, the complete source
cannot be a global diameter minimizer for sufficiently large q.
Equation (7.5) contradicts (7.3).

This permits arbitrary translations, rotations, occupied subsets,
and spacing excess tending to zero at any rate. It requires only the
actual unit-edge guard, not a separately imposed one-unit radial
buffer. Thus it goes beyond the buffered family in
`target_c_near_density_shell_global_competitor_2026-09-12.md`.
All extra source labels are counted. Neither one-lattice containment
nor the small circumradius excess is established for a general
canonical C-II source, so this is a scoped exclusion only.

## 8. The approximate stability bridge that would close the fused route

The following is an **unreviewed exploratory obligation**, not a
theorem asserted here:

```text
canonical full-source shell/interface stability
  -> g_A <= C(1+c_I), retaining all contact-isolated labels
  -> g_A = O(sqrt(D)) by the authored attachment-cell count candidate
  -> contradiction with Theorem 5.1's kappa D^(2/3) reserve
  -> no sufficiently large triangle-free global minimizer.
```

An error `O(D^alpha)` with any fixed `alpha<2/3` would likewise suffice.
The exact leading boundary allowance and every grain/interface term
still have to be paid. A small component count does not itself supply
that payment, and no inequality `g_A<=C(1+c_I)` has been proved.
Section 7 verifies this kind of cancellation only in its explicit
unit-edge hull / one-lattice interior scope.

## 9. An explicit asymptotic reserve coefficient

The fixed-disk instance of the literature input in Section 7.1 also
allows a quantitative improvement of Sections 3--5. This does not need
uniformity over translated domains: the difference vectors are counted
in disks centered at the origin. Classification: **proved candidate
awaiting independent audit/promotion**, with the same explicit
literature dependency.

Fix `theta in (131/208,2/3)` and a fixed positive c. Put
`delta=c D^(-1/3)`, `S=D/2+delta`. Write `L_S(s)` for the area of
the intersection of two radius-S disks with centers separated by s.
It is nonincreasing on `[D,2S]` and zero at `2S`. The uniform
near-tangency expansion is

$$
 L_S(2S-d)={4\over3}\sqrt S\,d^{3/2}
                    (1+O(d/S)),\qquad 0\le d\le2\delta. \tag{9.1}
$$

For example, write the lens as twice the circular cap integral
`2 int_0^(d/2) 2sqrt(2St-t^2) dt`; expanding the square root
uniformly gives (9.1), including its coefficient.

The disk count `N(r)=pi r^2/a0+O(1+r^theta)` and Stieltjes
integration by parts give

$$
 \sum_{w\in\Lambda:\ D\le|w|<2S}L_S(|w|)
  ={1\over a_0}\int_D^{2S}2\pi s L_S(s)\,ds
       +O(D^\theta L_S(D)).                         \tag{9.2}
$$

Use the left limit of N at D, so every distance-D tie is included.
The endpoint at `2S` has zero weight. The total variation of `L_S`
is `L_S(D)=O_c(1)`, which justifies the error uniformly across the
shrinking interval. No pointwise count on an individual lattice
circle is substituted for this weighted estimate.

Equations (9.1)--(9.2) imply

$$
 \int_D^{2S} L_S(s)\,ds
     ={32\over15}\sqrt D\,\delta^{5/2}(1+o(1)),
$$

and, for the exact translated-lattice conflict expectation,

$$
 \mathbb EE
  ={32\pi\over15a_0^2}c^{5/2}D^{2/3}+O_c(D^\theta).
                                                               \tag{9.3}
$$

The error from replacing `s` by D and `sqrt(S)` by `sqrt(D/2)`
is smaller than the displayed discrepancy error. The positive
`pi delta^2/a0` term in the population mean can be discarded.
Consequently some translation, followed by at most one deletion
per conflict edge as in Section 4, has strict diameter below D and
population at least

$$
 {\pi D^2\over4a_0}
 +\left({\pi\over a_0}c
            -{32\pi\over15a_0^2}c^{5/2}\right)D^{2/3}
 -C_cD^\theta.                                      \tag{9.4}
$$

Optimize the elementary expression in parentheses. Its maximum is
at

$$
 c_*=(3a_0/16)^{2/3},\qquad
 \kappa_0={3\pi\over5a_0}(3a_0/16)^{2/3}
                      =0.647826\ldots.              \tag{9.5}
$$

Thus every sufficiently large global diameter minimizer obeys

$$
 \boxed{g_A\ge\kappa_0D^{2/3}-C D^\theta,\qquad
  \liminf_{D\to\infty}{g_A\over D^{2/3}}\ge\kappa_0.} \tag{9.6}
$$

The liminf is along any sequence of global minimizers with growing
diameters; the finite bound has one absolute C for the fixed
triangular lattice and chosen theta. The integer comparison is again
`M<=n-1`, not `M<=n`, so no integer loss is hidden in (9.6).

If `T=sqrt((n-1)/(pi/(4a0)))`, the corresponding asymptotic
diameter bound is

$$
 D(n)\le T-{6\over5}(3a_0/16)^{2/3}T^{-1/3}
                    +o(T^{-1/3}).                   \tag{9.7}
$$

Indeed, if the deficit `T-D` is already larger than a fixed multiple
of `T^(-1/3)`, this holds directly. Otherwise `D/T ->1` and dividing
(9.6) by `(pi/(4a0))(T+D)` gives (9.7).
The coefficient in (9.7) is about `0.357165`. These decimals are
illustrations of the exact expressions, not certificates or optimized
upper bounds on all possible competitor constructions.

LEVEL I STATUS: STILL OPEN.
