> Generated reading edition · [exact source](../../../docs/reports/target_c_odd_shell_gap_regression_2026-10-01.md) · source SHA-256 `939fbcccf749ce37e5a7bb0720c223722a31490755d645db09d65389648e46c3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C2A71BAD69E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — regular odd shells realize the remaining gap and CROSS data

**Date:** 2026-10-01<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Prior checkpoint:** `f697b9de`<br>
**State version:** `2026-09-14.audit.51`<br>
**Mission:** hostile test of the exact-phase geometry after support-cap localization.<br>
**Classification:** regression; auxiliary identities are proved candidates awaiting promotion.<br>
**Level I:** OPEN; C-II OPEN.<br>
**External literature:** none.<br>
**Certificate:** [exact verifier](../../../docs/research/migration/2026-10-16/shards/04/evidence/research/verify_target_c_odd_shell_gap_regression.py).

```text
actual exact-phase unit-cut compatibility + one-sided gap/CROSS normal form
-> eliminate the actual source branch by a finite competitor or contradiction
-> Level I only after all other global branches are covered.
```

This report proves that deleting the first hypothesis from this chain is invalid.
The shell crosscuts below are deliberately geometric crosscuts, not actual
exact-phase contact trains. No global-minimizer counterexample is asserted.

## 1. Unbounded analytic family and exact layer data

Let `s>=1`, `q=4s+1`, `theta=pi/q`, and

$$
R={1\over2\sin\theta},\qquad
p_j=R(\cos(2j\theta),\sin(2j\theta)),\quad j\in\mathbb Z/q\mathbb Z.
$$

The source is unit-separated. Its only contacts are the `q` polygon sides;
its contact graph is a triangle-free cycle. Its actual diameter is

$$
D=2R\cos(\theta/2)={1\over2\sin(\theta/2)}.
\tag{1}
$$

The diameter graph has exactly the edges

$$
H=\{\{j,j+2s\}:j\in\mathbb Z/q\mathbb Z\}.
\tag{2}
$$

These statements follow from strict increase of the circle chord length with
cyclic distance `1,...,2s`. Since `gcd(2s,4s+1)=1`, (2) is one odd cycle;
every diameter vertex has degree two. It is the full actual diameter graph,
not a selected matching or a virtual thrackle.

Use `u=(1,0)` and vertical crosscuts at positive x-coordinates between the
successive values

$$
0<R\cos(2s\theta)<\cdots<R\cos(2\theta)<R.
$$

There are `s+1` cuts and `s+2` layers. Assign every left-half-plane vertex
to layer 0, assign `p_0` to layer `s+1`, and assign the right pair
`p_j,p_{-j}` to layer `s+1-j`, for `1<=j<=s`. Each cut is a proper
crosscut of the convex polygon. They are nested, and their endpoint-support
rows are exact intervals.

Every diameter with different endpoint labels joins layer 0 to a positive
layer. Exactly one diameter has equal endpoint labels:

$$
\{p_s,p_{-s}\},\quad\text{in layer 1}.
\tag{3}
$$

Indeed the diameter neighbors of `p_j`, `1<=j<s`, have signed indices
`j-2s` and `j+2s-q=-(2s+1-j)`, both in the left half-plane. For `j=s`,
one neighbor is `p_{-s}` and the other is `p_{-(s+1)}`. Reflection gives
the other half of the same calculation. The two diameters incident to
`p_0` join it to `p_{2s},p_{-2s}`, both in layer 0.

Thus the gap graph on `0,...,s+1` is a star as a simple graph, with
parallel branches: two rows for layer 1, four for each layer `2,...,s`,
and two for the exterior layer `s+1`. It has `4s` nonzero rows and

$$
\operatorname{rank}M=s+1.
\tag{4}
$$

To see (4), every nonempty row is a nonzero multiple of the prefix indicator
`1_[1,g]`, and every `g=1,...,s+1` occurs. Those prefix indicators have a
triangular determinant-one basis. No diameter is horizontal: equality of
two distinct regular odd polygon vertices' y-coordinates would require
their angles to sum to `pi` modulo `2pi`, impossible for odd `q`.

The two full-span rows share the actual endpoint `p_0` and have opposite
strict transverse signs. Their directions bracket `u` in one open global
diameter-direction cell. The cell width is `pi/q`; no diameter direction
lies inside it. The common-star support directions are exterior exactly as
in the [support-cap theorem](target_c_exact_phase_support_caps_2026-10-01.md).

## 2. Positive axial reactions and a linear CROSS family

Give every diameter weight `beta=1/q`. At an internal layer, orient each
switching diameter toward that layer. Reflection in the x-axis exchanges
the two middle vertices and their incident switching edges, so all
transverse contributions cancel exactly. Every exterior endpoint is in
the left half-plane and every middle endpoint in the right half-plane.
Thus every switching vector has a positive x-component, and the exact
weighted resultant is

$$
G_i=g_i u,\qquad g_i>0.
\tag{5}
$$

There are opposite strict transverse signs in every packet. The internal
same-layer edge (3) contributes equal and opposite endpoint forces and
cancels from the layer balance. Equations (4) and (5) give a full-rank
geometric gap matrix with a positive transverse circulation. Every internal
gap is left-only and occupies both middle boundary arcs.

For each `j=1,...,s-1`, choose the mirrored pair

$$
h_j^+=\{p_j,p_{j-2s}\},\qquad
h_j^-=\{p_{-j},p_{-j+2s}\}.
\tag{6}
$$

All `2(s-1)` bars have mutually disjoint endpoints: their middle indices
are `+/-1,...,+/-(s-1)` and their exterior indices are
`+/-(s+1),...,+/-(2s-1)`. Consequently every two selected bars cross
properly, by actual diameter geometry (or by their explicitly alternating
cyclic endpoint order).

The inward vectors of each mirrored pair sum to a positive axial vector.
Multiplying both by one positive scalar makes their sum equal to the entire
packet's `G_i` in (5). Hence these are exact positive two-bar compressions
of the actual diameter stress, not unweighted geometric pairs. There are

$$
s-1=(\pi/4+o(1))D
$$

fully vertex-disjoint, force-carrying CROSS bundles. Thus even a **linear**
complete crossing family of such pairs is possible in the remaining
geometric normal form.

## 3. Actual full-support KKT stress and exact PSD kernel

The regression also has an actual positive KKT stress for its unit-contact
cycle and full diameter cycle. Give every unit side weight

$$
\alpha=D^2\beta.
\tag{7}
$$

At vertex `p_j`, the contact-neighbor displacement sum is
`2(1-cos(2theta))p_j`. The diameter-neighbor displacement sum is
`2(1+cos(theta))p_j`. Since

$$
D^2={1+\cos\theta\over1-\cos(2\theta)},
$$

equilibrium holds with all contact and diameter multipliers strictly positive.
The sum of the diameter weights is one. Summing this actual equilibrium over
the chosen layer gives (5); the actual crossing contacts have an axial
resultant, although their individual directions are not the exact-phase
two-boundary-train directions.

Let `L_d` be the circulant graph Laplacian with edges `{j,j+d}`. The scalar
stress matrix is

$$
\Omega=\beta(D^2L_1-L_{2s}).
\tag{8}
$$

On Fourier mode `k`, its eigenvalue divided by `4 beta` is

$$
D^2\sin^2(k\theta)-\sin^2(2sk\theta).
$$

Because `2s theta=pi/2-theta/2`, for `1<=k<=q-1` the ratio of the second
square to the first is

$$
\begin{cases}
1/(4\sin^2(k\theta/2)),&k\text{ odd},\\
1/(4\cos^2(k\theta/2)),&k\text{ even}.
\end{cases}
$$

For odd `k`, the denominator is minimized only at `k=1`; for even `k`,
only at `k=q-1`. Both maximal ratios equal `D^2`. Hence

$$
\Omega\succeq0,\qquad
\ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad\operatorname{rank}\Omega=q-3.
\tag{9}
$$

These identities are actual source-level stress facts. They do not make the
shell a global minimizer, and no canonical theorem is invoked backwards.

## 4. Mixed rigidity and strict local minimality, not global minimality

For completeness the mixed contact/diameter framework is infinitesimally rigid
for this entire family. This auxiliary result is not needed for the gap
regression, but rules out an attempted repair using abstract mixed rigidity.

Identify the plane with the complex numbers and put `zeta=exp(2i theta)`.
Write an arbitrary velocity as `w_j=sum_k a_k zeta^(kj)`. The bar equation
for edges of step `d` is the vanishing of

$$
\operatorname{Re}\{(\zeta^{-d}-1)\zeta^{-j}(w_{j+d}-w_j)\}.
$$

For nonzero Fourier frequency `k-1`, equating it and its conjugate, then
dividing a common nonzero factor, gives

$$
\sin(kd\theta)a_k+
\sin((2-k)d\theta)\overline{a_{2-k}}=0.
\tag{10}
$$

Indices on `a` are taken modulo `q`; the integer sine expression is valid
also for negative `2-k`. Use (10) for `d=1,2s`. Its determinant is

$$
\delta_k=\sin(k\theta)\sin((2-k)2s\theta)
-\sin(2sk\theta)\sin((2-k)\theta).
$$

Up to a sign, it factors as

$$
\begin{cases}
4\cos(k\theta/2)\cos((2-k)\theta/2)
\cos(\theta/2)\sin((k-1)\theta/2),&k\text{ odd},\\
4\sin(k\theta/2)\sin((2-k)\theta/2)
\cos(\theta/2)\cos((k-1)\theta/2),&k\text{ even}.
\end{cases}
$$

It is nonzero for `3<=k<=q-1`. For the paired indices `k=0,2`, (10)
forces `a_2=0` and leaves `a_0` arbitrary, giving translations. For
frequency zero, `k=1`, the bar equation requires `Re(a_1)=0`, giving
rotation. Thus

$$
\operatorname{rank}R_{C\cup H}=2q-3.
\tag{11}
$$

Full-support positive KKT equilibrium makes every fixed-diameter critical
velocity have zero first variation on all active contacts and diameters:
the weighted sum is zero while each signed variation has one feasible
sign. Equation (11) makes that velocity Euclidean. Fix a translation and
the direction of one polygon side to remove Euclidean motions. If distinct
feasible sources of diameter at most `D` converged to the shell, divide
their gauge-fixed displacement by its norm and take a subsequence. Its
unit limiting velocity would be a nonzero gauge-fixed critical velocity,
contradicting (11). The shell is therefore an isolated strict local
minimum modulo Euclidean motions.

It is explicitly **not global** for all `q>=21`. Choose any `q` points
from an integer `ceil(sqrt(q))` by `ceil(sqrt(q))` square grid. Its diameter
is at most `sqrt(2)(ceil(sqrt(q))-1)<sqrt(2q)`. Equation (1) gives
`D>q/pi`; for `q>=21`, `q>2pi^2`, so `sqrt(2q)<q/pi<D`.
This supplies a strict same-cardinality competitor. No unbounded global
counterexample is hidden in this construction.

## 5. Exact omitted hypothesis and consequences for the next bridge

The vertical cuts are not actual exact-phase unit-train cuts. In the unit
polygon every side has a different projective direction, every stopped
train is a singleton, and there are no strict rhombus faces. The boundary
contact vectors of a layer are not just `u,-u`; an individual cut shear
does not preserve all contact first variations. There is no linear by
linear actual complete O–O rhombus rectangle or quadratic contact core.

Thus the false closing claim rejected here is:

> Connected exact-phase-form interval rows, actual convex diameter geometry,
> positive axial packet reactions, linear disjoint CROSS pairs, positive
> full KKT support, PSD affine stress kernel, and mixed rigidity alone are
> incompatible for large diameter.

They are compatible for every shell in this unbounded family. A valid next
lemma must use the **actual contact-train cutsets and their transverse
complete grid**, or another consequence of global minimum-diameter packing.
Replacing that coupling by geometric crosscuts is precisely the failed step.

For the current source branch, the remaining obligation is to exclude the
linear one-sided CROSS packet family when its boundary vectors are actual
two-train unit contacts and every boundary train crosses the same linear
transverse family in strict rhombi. This report has tested the weaker
geometry/stress version and refuted it; it has not tested away the genuine
source/grid hypothesis.

Split-star O–O, nonconstant phase, inactive interfaces, and macroscopic
inactive containers/exterior caps remain separate. No canonical state changes.

## 6. Computation and adversarial audit

Command:

```sh
python3 research/verify_target_c_odd_shell_gap_regression.py
```

Observed output:

```
PASS integer certificates: 64 shells, 8384 vertices, 2016 disjoint CROSS bundles
PASS cyclotomic certificate: q=5, stress_rank=2, mixed_rank=7, gap_rank=2
PASS cyclotomic certificate: q=9, stress_rank=6, mixed_rank=15, gap_rank=3
PASS cyclotomic certificate: q=13, stress_rank=10, mixed_rank=23, gap_rank=4
PASS cyclotomic certificate: q=17, stress_rank=14, mixed_rank=31, gap_rank=5
PASS cyclotomic certificate: q=21, stress_rank=18, mixed_rank=39, gap_rank=6
```

The discrete verifier uses integer cyclic-distance and layer data. Exact
algebraic checks use `Q(zeta_q)` with SymPy 1.12; the y-coordinate is
multiplied by `i`, an invertible column scaling that preserves the real
rigidity rank after complexification. All rank and equilibrium operations
are exact. The script performs no floating-point sign or PSD decision;
those inequalities have the analytic proofs above.

| Question | Result |
| --- | --- |
| Are the bars actual maximum-distance pairs? | Yes; maximal cyclic chord distance, not a drawn scaffold |
| Can the gap graph be connected with all gaps one-sided? | Yes; a star with parallel rows and full rank |
| Can the odd diameter cycle survive the bipartite gap graph? | Yes; exactly one same-layer diameter supplies the odd-cycle defect |
| Does positive equilibrium force a triangle? | No; actual contact graph is a cycle |
| Do PSD affine nullity and mixed rigidity force global optimality? | No; an explicit grid beats all members with `q>=21` |
| Are the chosen cuts actual complete exact-phase trains? | No; this is the essential omitted hypothesis |
| Does the certificate prove Level I false? | No; the unbounded family is explicitly nonglobal |

## 7. Next attack performed: two transverse geometric shores also survive

The first regression has one shore. One could still conjecture that coupling
two transverse *geometric* shores, common fixed stars, inverse-diameter phase
separation, and the joint switch budget eliminates it. The following refinement
refutes that repaired geometric claim too.

Take `q=12t+1`, hence `s=3t`, and put `L=floor(q/100)`. Use the first `L`
positive-projection crosscuts from Section 1, and a rotated copy whose axial
direction points to vertex `j=2t+1`. The two directions have angle

$$
\phi={2\pi(2t+1)\over q}={\pi\over3}+{5\pi\over3q},
\qquad \pi/3<\phi<\pi/2.
$$

Thus their separation is strictly above `pi/3` with inverse-`D` phase defect.
The two bracing stars are distinct actual diameter vertices `p_0,p_j`.

All chosen cut projections are positive and less than `R/8`: the last
threshold is below `R sin(2pi L/q)<2pi LR/q<=pi R/50<R/8`.
For one cut of projection `a` in direction `u` and one of projection `b`
in direction `v`, their intersection `z` satisfies

$$
|z|^2={a^2+b^2-2ab\cos\phi\over\sin^2\phi}
\le {R^2\over24}.
$$

The regular polygon has inradius `R cos(pi/q)>R/2`, so every intersection
lies in its interior. Every pair of opposite-shore crosscuts crosses, each
shore is internally disjoint, and this gives a linear by linear complete
**geometric** rectangle with `L=(pi/100+o(1))D`.

Coarsen the original layer map by replacing labels greater than `L` with
`L`. On each shore every nonempty diameter row still joins gap 0 to a
positive gap; every positive gap occurs. Each gap matrix has rank `L`,
each internal gap is left-only, the common-star witness pair has full
support, and the actual uniform diameter stress has positive axial
balance by the polygon's reflection symmetry about that axis. The four
host intervals and the joint per-edge switch bound also hold. The exact
integer verifier independently checks the latter bound for 56 shells.

These crossings are not unit rhombi. No crossing center is asserted to be
the center of an actual source face; no extra source or scaffold is merged
into the shell. This distinction is exactly what the repaired geometric
claim omitted. Adding the genuine transverse contact rectangle remains an
essential, unproved bridge.

**Disposition:** preserve both one-shore and two-shore shells as regressions
against geometry/stress-only closure. Actual unit-contact cutsets and their
rhombus faces must be used in the next lemma; no theorem promotion is requested.
