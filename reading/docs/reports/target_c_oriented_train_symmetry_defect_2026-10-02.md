> Generated reading edition · [exact source](../../../docs/reports/target_c_oriented_train_symmetry_defect_2026-10-02.md) · source SHA-256 `7f33c92cec76e3bb0ea8a2fd7b7844a8b4a592935b4b94a7d42fa9cf38cfebb4`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-AD4B2D443169","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — oriented train pairing forces a quantitative carrier asymmetry defect

**Date:** 2026-10-02<br>
**Starting local HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`<br>
**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Preceding checkpoint:** `bbc24541824adee25874a8149dd43e3c3c17b7f6`<br>
**State version:** `2026-09-14.audit.51`<br>
**Remote main inspected:** `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec`; the state lock, route map, and prompt are unchanged.<br>
**Mission:** push the source-face/cap reduction into actual harmonic-carrier boundary geometry.<br>
**Classification:** proved candidate awaiting promotion; conditional rooted-ledger application; exact regression.<br>
**Level I:** OPEN; C-I CLOSED; C-II OPEN.<br>
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.<br>
**Literature:** no theorem imported.

```text
oriented physical train-end pairing -> asymmetry of the actual carrier boundary
is paid by its own Q and Z -> a circle-supported wrapping carrier of diameter
lambda<1 has a strictly positive defect -> excludes the zero-defect rooted
endpoint; closing C-II still requires elimination of the positive-defect regime
or a source-preserving competitor, and the other global branches.
```

This is not a Level I proof. The positive-defect regime is explicitly retained.

## 1. Source objects and dependencies

Let `J` be the induced contact graph of one unloaded harmonic component and
its loaded attachment set `A`. Canonical
[Section 82](../targets/target-c/82-harmonic-cell-near-quadrangulation-audit.md),
using `C-ATTACH-CURRENCY`, makes `J` connected, plane, and triangle-free,
puts every vertex of `J` in `P=conv(A)`, and makes every attachment a
vertex of `P`. Thus `P` is exactly the contact graph's convex hull.
Let `L` be its occurrence-counted outer contact walk, let `f` count its
bounded nonquadrilateral faces, and put

```math
Q=\sum_{F\text{ nonquad}}(\deg F-4),\qquad
Z=L-\operatorname{per}(P)\ge0,
\qquad E=Q+4f\le5Q.
\tag{1}
```

All bounded four-faces are actual strict unit rhombi. We rederive the
oriented pairing from these rhombi, rather than promote a train-end theorem
from an unreviewed report. Physical face occurrences are retained at bridges
and repeated vertices. Source isolates stay outside the matrix and local
contact graph; this argument deletes none from the full source.

For the asymptotic circle application, use canonical Type-II annular
convergence and [Section 88](../targets/target-c/88-harmonic-wrapping-diameter-audit.md).
After division by the source diameter `D`, the attachments converge to a
compact subset `S` of the radius-`1/2` circle, with `0 in conv(S)` and
`diam(conv(S))=lambda<1`. Positive area is assumed for the macroscopic
application. The rooted ledger and its equation defining `lambda_1` are
**unpromoted** inputs from
[rooted defect stability](target_c_wrapping_root_defect_stability_2026-09-30.md).

## 2. Exact oriented outer-boundary imbalance

Orient the outer contact walk counterclockwise, with its contact-domain side
on the left. For each directed unit edge occurrence use its right-hand
unit normal. Let `nu` be the sum of point masses at these normal directions;
its mass is `L`. For any measure `mu` let `mu^op` be its translate by `pi`.

**Lemma 1.** The actual boundary satisfies

```math
\boxed{\|\nu-\nu^{op}\|_{TV}\le2E.}
\tag{2}
```

**Proof.** Opposite edges in each strict unit rhombus have the same contact
direction. Join their two physical face-side occurrences. Each complete
train has two ends: continuing through rhombi strictly increases the
transverse height in one orientation, so cannot cycle. A contact edge has
at most two incident rhombi, so there is no train branching.

For a train with both ends outer, the two terminal directed outer edges
are opposite vectors. This follows already in one rhombus; continuing
across a shared edge reverses the two face orientations and preserves the
end relation. A singleton outer bridge contributes its two opposite
outer occurrences as well. Hence every O–O train's contribution to `nu`
is antipodally symmetric.

All unmatched outer occurrences come from trains with a bounded
nonquadrilateral end. There are at most `E` such occurrences, by the
occurrence-counted sum of bounded nonquadrilateral degrees. The difference
of their positive measure and its antipodal image has total variation at
most twice their count. This proves (2). It requires neither global O–O
transfer nor a fixed star, and does not merge repeated outer occurrences.
QED.

Unlike a projective direction measure, `nu` retains the orientation of the
physical outer walk. Passing to projective directions first would erase
precisely this additional equality.

## 3. Boundary route excess controls the convex boundary measure

Let `mu_P` be the normal-direction measure of the convex polygon `P`:
each side contributes its length at its outward normal. Its mass is
`per(P)`. The outer walk can be partitioned into routes between one
selected occurrence of each convex-hull vertex in cyclic hull order.
This occurrence selection is valid for the outer boundary of a connected
plane graph: resolve it in a small regular neighborhood; the extreme
vertices occur in their hull order, while repeated visits stay in the
intervening routes. Equivalently it is the same boundary-order convention
used by the canonical harmonic-cell route ledgers.

For a route of length `ell`, chord length `d`, and oriented chord unit
vector `q`, its directed unit edges `e_k` satisfy

```math
\sum_ke_k=dq,\qquad
\sum_k|e_k-q|^2=2(\ell-d).
\tag{3}
```

Summing the route excesses gives exactly `Z`. Consequently, for a
function `phi` on the direction circle with sup norm at most `a` and
angular Lipschitz constant at most `b`,

```math
\boxed{
\left|\int\phi\,d(\nu-\mu_P)\right|
\le {\pi b\over2}\sqrt{2LZ}+aZ.
}
\tag{4}
```

Indeed angular distance between unit vectors is at most `(pi/2)|e-q|`.
Replace each route's edge mass by `ell` copies of its chord direction,
then remove the excess `ell-d` mass. Cauchy–Schwarz and (3) give (4).
All route occurrences are used once; bridge or articulation backtracking
is charged to `Z` rather than discarded.

## 4. An explicit support-function inverse

Define the continuous antiperiodic kernel `K` by

```math
K(t)={ (\pi-2t)\sin t-\cos t\over4\pi}
\quad(0\le t\le\pi),\qquad K(t+\pi)=-K(t).
\tag{5}
```

The endpoint values fit. Direct differentiation, including the derivative
jumps at `0,pi`, gives the distribution identity

```math
K''+K={1\over2}(\delta_0-\delta_\pi)-{1\over\pi}\cos t.
\tag{6}
```

Its first sine and cosine coefficients vanish, by direct integration.
The nonzero Fourier coefficients are those of the antiperiodic inverse
on odd modes `n>=3`; explicitly

```math
K(t)={1\over\pi}\sum_{j\ge1}
{\cos((2j+1)t)\over1-(2j+1)^2}.
```

The series is absolutely convergent and
`sum_(j>=1)1/[4j(j+1)]=1/4`. Also differentiating (5) bounds its slope.
Thus

```math
\boxed{\|K\|_\infty\le {1\over4\pi},\qquad
\operatorname{Lip}(K)\le {\pi+1\over4\pi}.}
\tag{7}
```

Let `h` be the support function of `P`. For a polygon, `h''+h=mu_P`:
on each vertex-normal interval `h` is a sine/cosine solution; at a side
normal its derivative jump is the side length. This proves the identity
directly without an external reconstruction theorem.

Put `g=mu_P-mu_P^op`. Its first Fourier modes vanish because the oriented
side vectors of a closed polygon sum to zero. Equations (6) therefore
give `R=K*g` with `R''+R=g`. Since
`h(t)-h(t+pi)` satisfies the same equation, their difference is a first
harmonic:

```math
h(t)-h(t+\pi)=R(t)+2c\cdot(\cos t,\sin t)
\tag{8}
```

for one vector `c`. Combining (2), (4), and (7) yields

```math
\boxed{
\|R\|_\infty
\le {E+Z\over2\pi}
 +{\pi+1\over4}\sqrt{2LZ}.
}
\tag{9}
```

To check the factors, the term `K*(nu-nu^op)` is at most `2E/(4pi)`.
The two differences between `nu` and `mu_P` each cost (4). Their summed
square-root coefficient is
`pi Lip(K) <= (pi+1)/4`; their excess-mass coefficient is `1/(2pi)`.

## 5. Circle-supported wrapping forbids zero asymmetry

First suppose exactly that the vertices of `P` lie on a circle of radius
`rho`, centered at zero, with `0 in P`. Let `d=diam P`.
At the radial direction `e=x/rho` of any vertex `x`,

```math
h(e)=\rho,\qquad h(-e)\le d-\rho,
```

because width is at most diameter. Equation (8) gives

```math
R(e)\ge2\rho-d-2c\cdot e.
```

Take a convex combination of the vertex directions equal to zero, which
exists because `0 in P`. Its average right side is `2rho-d`; therefore

```math
\boxed{\|R\|_\infty\ge2\rho-d.}
\tag{10}
```

For Type-II annular attachment sequences, divide by `D` and pass to the
circle-supported wrapping limit. Supports and normal measures converge
in their distribution identity; convolution with continuous `K` converges
uniformly since perimeter masses stay bounded. Apply (10) to the limit.
Combining (9)--(10), with `rho/D->1/2`, gives the new necessary defect law

```math
\boxed{
(1-\lambda-o(1))D
\le {Q+4f+Z\over2\pi}
 +{\pi+1\over4}\sqrt{2LZ}.
}
\tag{11}
```

In particular, `Q=o(D)` and `Z=o(D)` force `lambda=1`.
This is independent of phase extraction, global O–O transfer, diameter
tree labels, KKT weight floors, and whether local trains end on globally
inactive interfaces. It retains the exact local quantities `Q,Z`.

There is also a direct structural interpretation. Under those zero-defect
hypotheses, (8)--(9) make the limiting support function centrally symmetric
after translation. A positive-area centrally symmetric polygon with every
extreme point on the radius-`1/2` circle must have that circle's center as
its symmetry center: if its center is `c`, equality of the radii of `x`
and `2c-x` gives `c dot x=|c|^2` for every extreme point; a nonzero `c`
would put them on one line. Its diameter is consequently one. The
quantitative proof (11) needs only wrapping and avoids inferring a rate
from near equality.

## 6. Conditional composition with the rooted ledger

Let `Delta(lambda)=pi/2-lambda-4lambda sqrt(1-lambda^2)` on the current
rooted branch. The unpromoted rooted defect stability report gives

```math
Q_{\rm tot}+Z_{\rm tot}\le2\Delta(\lambda)D+o(D).
```

Use the same macroscopic wrapping carrier in (11). Its local quantities
are bounded by these sums; `f<=Q`, and
`L=per(P)+Z<=pi lambda D+2Delta D+o(D)`. Hence every such survivor obeys

```math
\boxed{
1-\lambda
\le {5\over\pi}\Delta(\lambda)
 +{\pi+1\over2}
 \sqrt{\Delta(\lambda)\bigl(\pi\lambda+2\Delta(\lambda)\bigr)}.
}
\tag{12}
```

At `lambda=lambda_1`, the exact root equation gives `Delta=0`, whereas
`1-lambda_1>0`. Thus the rooted zero-defect endpoint is impossible under
its own harmonic-carrier hypotheses, without restricting to one global
O–O/star branch. The right side increases and the left side decreases
on `[lambda_1,1)`; the derivative of `Delta` is positive there. The
exact verifier certifies failure of (12) at the rational value

```math
\lambda=0.9891349.
```

Therefore this conditional composition gives the safe strict improvement
`liminf lambda>0.9891349` (a stronger real threshold is the first crossing
of (12)). The quantitative constant is secondary to the local law (11).

This does **not** imply all surviving carriers have `lambda=1`: for
larger `lambda`, the rooted ledger permits positive linear `Q` and `Z`,
and (12) is compatible. Those defects, multi-grain transfer, corridors,
source isolates, and the other C-II branches remain. No Level I or
canonical-state change is claimed.

## 7. Failed shortcut and exact regression

The attempted claim that a circle-supported polygon of diameter less than
one cannot have two pairs of parallel opposite sides separated projectively
by `pi/3` is false. On the radius-`1/2` circle take the six angles

```
20, 100, 140, 220, 260, 340 degrees.
```

The consecutive gaps alternate `80,40` degrees. The six side normals
are at `0,60,120,180,240,300` degrees, giving three opposite parallel
pairs and inverse-phase directions. There are no antipodal vertices;
its diameter is `cos(pi/18)<1`. Opposite sides have unequal lengths
`sin(pi/9)` and `sin(2pi/9)`. It is their **mass imbalance**, which the
oriented physical train pairing measures, that prevents a zero-defect
unit-rhombus realization. Existence of parallel chord directions alone
does not do so.

This is a convex support regression, not a unit-contact framework or
global minimizer. It preserves the exact failure that led to (2).

## 8. Computation, audit, and exact remaining gap

[verify_target_c_oriented_train_defect_2026_10_02.py](../../../docs/research/migration/2026-10-16/shards/04/evidence/research/verify_target_c_oriented_train_defect_2026_10_02.py)
uses exact rational alternating-series bounds for pi, exact rational
square-root enclosures, and the integer eighteen-cycle support data.
It checks the Green-kernel symbolic identities and first modes,
the strict failure of (12) at `0.9891349`, and the opposite-chord regression.
No floating-point sign is load-bearing. The finite checks do not establish
the source train pairing or the rooted ledger; those have analytic proofs
or explicitly named dependencies above.

| Assertion | Classification | Audit boundary |
| --- | --- | --- |
| Oriented outer measure imbalance at most `2(Q+4f)` | Proved candidate | Physical occurrences, including singleton bridges |
| Route excess bound (4) | Proved candidate | Hull-order occurrence selection, no route omitted |
| Explicit kernel and defect law (11) | Proved candidate | Circle-supported wrapping; local carrier quantities |
| Rooted inequality (12) | Conditional | Unpromoted rooted stability ledger |
| Parallel chord directions alone force antipodes | Rejected | Six-angle exact support regression |
| Local geodesic defect law closes C-II | Rejected conclusion | Positive linear defects remain compatible |

The next attack must use (11) in the positive-defect regime, with the
actual phase-end/corridor population and rooted payments coupled rather
than counted independently. The concrete obstruction is that the right
side of (12) grows faster than `1-lambda` once the available rooted
defect becomes positive. An improved closing inequality must retain
which physical ends spend `Q` versus `Z`, or construct the strict
same-cardinality competitor. Replacing (11) by a new scalar constant
does not remove that source obligation.

Promotion recommendation: **unreviewed**, pending independent audit of
the oriented train pairing, hull-route selection, and support-function
bridge; do not modify the canonical frontier on this branch.

## 9. Next attack performed: a flat macroscopic carrier has a rectangular limit

The zero-defect conclusion can be pushed beyond diameter asymmetry by
using the actual one-time crossing and triangle-free crossing theorem
[shared Theorem 10.6](../theory/01-local-structure.md). The exact
hull-to-hull result in its Corollary 10.7 motivates the limiting argument
but does not by itself prove it for near-geodesic outer walks.

**Theorem 7 (rectangular flat-carrier limit).** Consider the same
macroscopic circle-supported carrier sequence, now allowing `lambda=1`.
Assume `Q/D->0`, `Z/D->0`, and a positive limiting area. Then its convex
limit is a rectangle. Except for `o(D^2)` rhombi, in the iterated
small-direction-window sense, its actual rhombi have side directions
approaching the two perpendicular rectangle directions. If its rhombus
count is bounded below by `c D^2`, then

```math
\boxed{A_4/R_4\to1.}
\tag{13}
```

Here the counts are for this carrier, not the full source.

**Proof of the geometric limit.** Parameterize the normalized outer
walks on `[0,1]` at constant speed `L/D`. They are uniformly Lipschitz
and remain in their convex hulls. Pass to a uniformly convergent
subsequence with convex hull limit `P_0`. The limit visits every extreme
point of `P_0`, and its length is at most `per(P_0)`. A closed curve has
length at least its convex-hull perimeter; equality for a positive-area
hull traverses the convex boundary once. One direct verification is to
integrate projection total variation: each direction costs at least twice
the hull width; equality in the perimeter formula leaves no backtracking
in any projection, hence the convex boundary. Orientation is inherited
from the resolved outer walk.

The limit thus traverses `partial P_0` once. Its speed is at most
`per(P_0)`; since its length equals that value, its speed is equal to it
almost everywhere. The approximating derivatives converge weakly in
`L^2` and their norms converge to the limit norm. Therefore they converge
strongly in `L^2`. This proves convergence of the **joint position and
oriented tangent distribution**, not only the marginal direction
measure. In particular, any positive limiting tangent mass in a small
angular arc is realized, except for `o(D)` edges, at the corresponding
ordered boundary portion of `P_0`.

Lemma 1 makes `P_0` centrally symmetric. Let `T_0` be the support of its
projective tangent measure. Choose two distinct directions in `T_0`,
and small angular arcs about them and their antipodes. The joint
convergence and `E=o(D)` provide actual O–O tracks whose two terminal
occurrences lie in the corresponding two ordered outer-boundary portions.
Both ends can be chosen good: the number of bad edge occurrences is
`o(D)`, whereas each fixed positive-mass arc supplies a linear count.
For an atom on a polygon side, choose occurrences away from its corners;
for non-atomic support, choose disjoint boundary portions with positive
mass. Singleton bridges cannot be selected this way because their two
ends coincide spatially, whereas opposite portions of a positive-area
convex body are separated.

The two actual tracks have alternating boundary ends, so cross. Their
directions therefore have projective separation strictly greater than
`pi/3`. Shrinking the arcs shows that any two distinct directions of
`T_0` are separated by at least `pi/3`. On the projective circle there
can be at most three such directions. If there are three, they are
equally spaced by `pi/3`. Selecting one good actual O–O track from each
of their arcs makes every pair alternate and cross, contradicting the
exact triangle-free track-crossing graph. Consequently `T_0` has at
most two directions.

Positive area requires two. The centrally symmetric convex body with
normal measure supported on two projective directions is a
parallelogram: reconstruct its four ordered edge vectors from that
measure. All its extreme points lie on the limiting circle, so it is
a rectangle. This proves the geometric claim.

**Proof of (13).** The total local stopped-train count is `O(D)`, since
twice that count is the outer plus bounded nonquadrilateral endpoint
capacity. All non-O–O trains have a bounded end, so there are `o(D)` of
them. By the joint/marginal convergence, for each sufficiently small
fixed direction window, all but `o(D)` trains have directions in the
two windows around the perpendicular rectangle directions, after
taking the source limit then shrinking the windows.

Shared Theorem 10.8 bounds a track's rhombus count by
`2 diam(P)/sqrt(3)=O(D)`. The exceptional trains therefore account for
`o(D^2)` rhombi in the same iterated-limit sense. Trains in one small
window cannot cross each other; almost every remaining rhombus has one
direction from each perpendicular window, so its area tends to one.
The lower bound on `R_4/D^2` converts the negligible exceptional
population into the ratio (13). QED.

This proof does not identify a layer label with a physical vertex and
does not infer that nearly convex edges are exactly hull edges. The
joint position/tangent step is essential to applying the alternating
endpoint argument, rather than quoting Corollary 10.7 outside its scope.

## 10. Consequence for Type-II near-minimum-area rhombi, including lambda=1

In the canonical full-core Type-II regime, the global strict-rhombus
area/count asymptotics give

```math
A_4-{\sqrt3\over2}R_4=o(D^2).
```

Each summand is nonnegative. Hence the same absolute error is `o(D^2)`
for any carrier subset. If its count is `Omega(D^2)`, it has
`A_{4,J}/R_{4,J}->sqrt(3)/2`. This contradicts (13). Thus **no
macroscopic near-minimum-area Type-II carrier can have both local
`Q=o(D)` and `Z=o(D)`, even when its normalized diameter tends to one**.

For every fixed lower carrier area and rhombus-filling fraction in the
stated Type-II scope, compactness gives an absolute positive lower
bound on `(Q+Z)/D`; no numerical value for this additional bound is
claimed. This is stronger than merely excluding the `lambda_1`
zero-defect endpoint, but still does not defeat a positive linear
defect budget.

The remaining quantitative task is to couple this necessary
nonrectangular train population to the specific rooted payments.
The source can spend linear `Q` or linear route detour `Z`; the current
ledger permits such spending away from its equality endpoint. Closing
requires a bound that exceeds that ledger for every `lambda<1`, or a
finite release in the actual positive-defect/corridor geometry. The
separate split-star, inactive-interface, and other Level I branches
remain part of the original objective.
