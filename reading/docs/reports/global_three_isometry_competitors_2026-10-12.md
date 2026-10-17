> Generated reading edition · [exact source](../../../docs/reports/global_three_isometry_competitors_2026-10-12.md) · source SHA-256 `11ddb9d39f44e9513831e7d40ca55693b62f8c187542c777a48a22f04788fc73`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6CBDCF3FFA63","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Three rigid motions and an unbounded full-source replacement benchmark

**Date:** 2026-10-12.
**Baseline:** `de0c978a`, based on `ab6dd333`.
**State version:** `2026-10-10.audit.234`.
**Target:** independent global full-source endpoint route.
**Classification:** proved candidate awaiting promotion; artifact unreviewed.
**LEVEL I STATUS: STILL OPEN.**

## 1. Global implication and changed mechanism

The [preceding report](global_discrete_isometry_blocker_closure_2026-10-12.md)
proved that a binary common-isometry dictionary cannot strictly shorten an
odd actual diameter cycle. This is a complete topology obstruction, not a
failed numerical trial. The next mechanism permits at least three rigid
motions, including rotations, and checks the entire endpoint. The intended
chain remains

```text
extract a simultaneous dictionary assignment on the actual full source
 -> every pair lies in [1,D)
 -> strict same-cardinality diameter competitor
 -> global contradiction.
```

This report supplies a certified nonlocal three-state example with a PSD
KKT stress at the old source, and an unbounded full-source row-replacement
benchmark. Neither is asserted to be a new example of nonglobality. The
regular heptagon's nonglobality already has a canonical regression in
Audit.122. The new data give a particularly simple three-isometry endpoint
with rational motion parameters. The benchmark checks that the mechanism
can rearrange whole quadratic populations rather than only small faces.
No universal extraction theorem is obtained.

## 2. Exact dictionary criterion for arbitrarily many states

For a unit-separated source with `n>=2`, let `T_0,...,T_{k-1}` be Euclidean
isometries, common to every source label.
For each label `i`, create `k` alternatives `(i,a)`. Join all alternatives
of one label into a clique, and join `(i,a)` to `(j,b)` exactly when

$$
|T_a p_i-T_b p_j|<1\quad\text{or}\quad
|T_a p_i-T_b p_j|\ge D. \tag{1}
$$

A full-source strict competitor exists in this dictionary if and only if
this graph has an independent transversal containing one alternative
from each label. This follows by checking every selected pair, as in the
two-state proof. It is a finite exact decision formulation, not a claim
of polynomial-time solvability for arbitrary `k`.

Every old actual diameter pair must receive different states, since a
common isometry preserves that pair. Hence `k` must be at least the
chromatic number of the original diameter graph. Three states remove
the parity obstruction for an odd cycle. Proper diameter coloring still
does not check any lower pair or any old non-diameter upper pair.

## 3. Rational-isometry endpoint for the regular unit heptagon

Let `c=cos(2*pi/7)`, `s=sin(2*pi/7)`, and

$$
R=(2-2c)^{-1/2},\qquad
p_j=R(\cos(2\pi j/7),\sin(2\pi j/7)),\quad0\le j<7.
$$

The source has seven unit contacts in a cycle, no unit triangle, and seven
diameter pairs joining indices differing by three modulo seven. Its
diameter squared is

$$
D^2={1-\cos(6\pi/7)\over1-c}>5. \tag{2}
$$

For rational `q`, define the exact rotation

$$
U(q)={1\over1+q^2}
\begin{pmatrix}1-q^2&-2q\\2q&1-q^2\end{pmatrix}.
$$

Use `T_0` identity and `T_a(p)=U(q_a)p+t_a` with

| State | `q_a` | `t_x` | `t_y` | Labels |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 1 | `80223303/1000000000` | `570658219/500000000` | `-3437473/20000000` | 1,2,3 |
| 2 | `49087849/200000000` | `104067187/100000000` | `131086831/1000000000` | 4,5,6 |

The exact certificate proves, for every mixed-state pair,

$$
|T_a p_i-T_b p_j|^2>{1000005\over1000000}>1,
$$

and for every endpoint pair,

$$
|p'_i-p'_j|^2<{4477\over1000}<5<D^2. \tag{3}
$$

Four old same-state unit contacts remain exactly unit. All other endpoint
pairs have strict lower slack. All seven labels are retained, and the new
contact graph is two three-vertex paths plus the retained isolated label
0. The resulting diameter is below `sqrt(4477/1000)`, whereas the old
diameter exceeds `sqrt(5)`. These rational bounds suffice; no floating
endpoint value is a proof premise.

### The old PSD stress and its limitation

Assign `beta=1/7` to each old diameter pair and `alpha=D^2/7` to each old
unit edge. They are positive, `sum beta=1`, and `sum alpha=D^2`.
The cyclic Laplacians applied to the position vectors have factors
`2(1-c)` and `2(1-cos(6*pi/7))`, so equilibrium follows from (2).

For `Omega=alpha L_C-beta L_H`, Fourier eigenvalues are

$$
\lambda_l={2\over7}
\left[D^2(1-\cos(2\pi l/7))
 -(1-\cos(6\pi l/7))\right].
$$

Modes `0,1,6` have eigenvalue zero. The certificate proves
`lambda_2=lambda_5>8/5` and `lambda_3=lambda_4>23/10`.
Thus `Omega` is PSD with rank four and affine kernel. This fact does not
certify old globality; (3) disproves it directly. It does not extend the
source to a global-minimizer example or supply an original-source move
for arbitrary canonical C-II configurations.

### Certification independent of discovery

The certificate isolates the unique root of
`8c^3+4c^2-4c-1=0` in `(1/2,1)` by rational bisection. The derivative is
at least six there. This is `cos(2*pi/7)` by the seventh-root-of-unity
identity and `2*pi/7<pi/3`. It computes rigorous rational intervals for
`s`, `R`, and all coordinates with integer-square-root enclosures.
Exact identities handle preserved unit lengths; rational interval margins
handle all other source and endpoint pairs and the positive eigenvalues.
There is no floating arithmetic in this independent certificate.

## 4. Whole quadratic-population benchmark

Let the source be the complete `m by m` unit square grid, `m>=6`:
`p_ij=(i,j)`, `0<=i,j<m`. Apply the row-dependent common translations

$$
T_j(p)=p+\left({j\bmod2\over2},
 (\sqrt3/2-1)j\right). \tag{4}
$$

Every one of the `m^2` labels stays. Within a row the separation is an
integer at least one. Between adjacent rows the horizontal separation is
at least `1/2` and the vertical separation is `sqrt(3)/2`, so the distance
is at least one. Between rows differing by at least two the vertical
separation alone exceeds one. Thus all full-source lower constraints hold.

For any endpoint pair the horizontal separation is at most `m-1/2` and
the vertical separation is at most `(sqrt(3)/2)(m-1)`. Therefore

$$
\operatorname{diam}(P')^2
\le(m-1/2)^2+{3\over4}(m-1)^2
=2(m-1)^2-{m^2-6m+4\over4}
<\operatorname{diam}(P)^2. \tag{5}
$$

The last numerator is positive for every `m>=6`. The asymptotic upper
ratio is `sqrt(7/8)`. This is a single complete-source construction for
an unbounded cardinality family, rather than an assertion about a
selected patch inside an unknown larger source. The dictionary has `m`
states; constant dictionary size for arbitrary sources is not proved.
The endpoint has triangles, which are allowed in a strict competitor.

Equation (5) is an elementary benchmark, not a novelty claim over existing
lattice-density competitors or the canonical embedded-wall exclusions.
It does not authorize insertion into an arbitrary surrounding source:
additional outside pairs would require their own full-source check.

## 5. Validation and search limits

Commands:

```bash
python3 research/verify_global_three_isometries_2026_10_12.py
python3 research/explore_global_three_isometries_2026_10_12.py --rotations --output /tmp/three-isometries.json
```

Discovery used seed `20261012`, all 21 three-group partitions properly
coloring the heptagon's old diameter cycle, and random SLSQP starts.
Three translations alone produced no improving candidate in 500 starts;
that is **not** an impossibility proof. Allowing rotations found a
candidate at zero-based trial 8. The independent rational parameters and
certificate above supply the mathematical result.

The exact checker verifies all 21 source pairs, all 21 endpoint lower
bounds, all 21 strict upper bounds, four preserved exact units, and 15
strict mixed-state pairs. It also verifies every old and endpoint pair
in finite row benchmarks. The all-`m` conclusion comes from the proof of
(4)--(5), not from those finite checks.

The 2026-10-15 preservation audit reproduced the rotated discovery at trial
8 with 21 patterns and independently reran the rational certificate. The
checker now refuses optimized Python, validates the complete seven-label
state, replays its JSON rational parameters, and rejects truncated-label
and all-identity motion mutations. Its preserved-unit assertions use the
analytic regular-polygon/isometry identities, not interval inclusion alone.
See the [source and dirty-worktree audit](global_discrete_replacement_preservation_2026-10-15.md#dirty-three-state-extension).

## 6. Lifecycle and exact remaining global theorem

All endpoint, conflict-transversal and stress claims are proved candidates
awaiting promotion in this **unreviewed** artifact. The benchmark is a
verified construction with explicitly limited scope. No canonical theorem
state or active prompt changes, and no source extraction is claimed.

The next global obligation remains: extract from every sufficiently large
triangle-free global minimizer a compatible full-source assignment, or
an independent same-cardinality packing of strictly smaller diameter.
Dictionary size, rotations, all inactive upper/lower pairs, and all
isolates must be controlled. The odd-cycle obstruction is removed by
three states, but the compatibility/extraction theorem remains open.
