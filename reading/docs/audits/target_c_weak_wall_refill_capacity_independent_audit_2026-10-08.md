> Generated reading edition · [exact source](../../../docs/audits/target_c_weak_wall_refill_capacity_independent_audit_2026-10-08.md) · source SHA-256 `737faeb951908c6a5c089ed765f32089bf0b752de11f01aacb1bda02306ab807`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-048ECDDE436D","canonical":true,"claim_ids":["C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION","C-NONCONTACT-WALL-WEAK-SHIELD","C-POST-DESCENT-WEAK-WALL-REFILL","C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER"],"claim_statuses":{"C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION":"regression","C-NONCONTACT-WALL-WEAK-SHIELD":"canonical","C-POST-DESCENT-WEAK-WALL-REFILL":"canonical","C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: weak-wall refill and capacity plateau

**Date:** 2026-10-08
**Audit base:** `origin/main=16bd9e89cbe32796ff322c48fb433198223e25f9`, state `2026-10-08.audit.164`.
**Frozen source branch:** `research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f`; this branch was 8 main-only / 24 branch-only commits at refresh.
**Candidate commit:** `26023ad2acc40aafe3cb831fdc0bcb3bd7ca97ae`.
**Source report SHA-256:** `469dd25fb153daf1753f58de49e49c00214e4136c016bb54fa0f84b5b4ad3f6c`.
**Source verifier SHA-256:** `260f1778df34941ecbdb48c7bf992552896aa9ecf6ac5e2dd4b8b388d21c358d`.

The report and verifier hashes were the same at the candidate commit and the refreshed branch tip. No later source commit was mixed into this audit. Open research PRs at refresh were #737 (owner-order, updated 2026-10-07) and #668 (deep-port route, updated 2026-10-05). All 17 remote `research`, `proof`, and `swarm` refs were compared with main; their tips and ahead/behind counts are recorded in Audit cycle 169 of the integration ledger.

## Verdict

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Closed-guard source-wall shield and disjoint-wall packet compatibility | PASS | Promote `C-NONCONTACT-WALL-WEAK-SHIELD` |
| Strict reduced-source endpoint plus enough wall packet sites | PASS | Promote `C-POST-DESCENT-WEAK-WALL-REFILL` |
| A nonwall label cannot cross a continuously moving short-side wall | PASS | Promote `C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER` |
| Flat near-triangular grid-wall capacity plateau | REGRESSION VALID | Promote `C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION` |

These statements give no source-extraction theorem, no packet construction, and no finite motion from a canonical C-II minimizer. C-II and Level I remain open.

## 1. Exact wall shield

Let `A` be a finite unit-separated set, and let `Q` be a simple polygon whose distinct cyclic vertices belong to `A`. Suppose every side has length at most `L<=sqrt(3)`. Call `x` a weakly guarded interior point if `x` lies in `int(Q)` and `|x-v|>=1` for every wall vertex `v`.

For any source point `q` outside `int(Q)`, a weakly guarded `x` satisfies `|x-q|>=1`. If `q` is a wall vertex this is the guard. Otherwise `q` cannot lie in the relative interior of a wall side: for a side `[a,b]` of length at most `sqrt(3)`, any such point is within `sqrt(3)/2<1` of one endpoint, contradicting source separation.

Take the first exit `z` of segment `[x,q]` from `Q`. If `z` is a wall vertex, both distances to it are at least one, unless `q=z`, which is the direct wall-vertex case. If `z=(1-t)a+tb` is in the interior of a side, then both `x` and `q` are at least one from `a,b`. The exact identity

```math
|w-z|^2=(1-t)|w-a|^2+t|w-b|^2-t(1-t)|a-b|^2
```

gives

```math
|x-z|,|q-z|\ge\sqrt{1-L^2/4}\ge\tfrac12.
```

The two lengths add along `[x,q]`, so `|x-q|>=2 sqrt(1-L^2/4)>=1`. Equality is allowed. No convexity is used.

If `Q_i` have pairwise disjoint interiors and each packet `Y_i` is internally unit-separated and weakly guarded from every vertex of `Q_i`, then the packets are jointly unit-separated. Every vertex of `Q_i` lies outside `int(Q_j)`; the one-wall result first places each point of `Y_j` at least one from all vertices of `Q_i`, and the same first-exit calculation in `Q_i` gives `|x_i-x_j|>=1`. Shared boundary vertices cause no problem because they are guarded. The proof does not imply strict clearance or permit strictification by dilation.

This extends the strict-guard theorem `C-NONCONTACT-WALL-STRICT-SHIELD` to weak guards, including exact wall contacts, and retains its multiwall scope. It does not weaken the `sqrt(3)` side threshold.

## 2. Correct finite post-descent replacement implication

Let `A_0` be an `n`-point global diameter minimizer of diameter `D`. Delete `r` labels and move every retained label to a unit-separated set `A` of size `n-r` and diameter `D'<D`. Let `Q_1,...,Q_m` be simple polygons with pairwise disjoint interiors, distinct source vertices in `A`, and every side of length at most `sqrt(3)`. Put `S_i=A intersect int(Q_i)`. For each `i`, let `Y_i` be a finite internally unit-separated packet in `int(Q_i)` whose points are weakly guarded from every vertex of `Q_i`.

If

```math
\sum_i |Y_i|\ge r+\sum_i |S_i|,
```

then

```math
A'=(A\setminus\bigcup_i S_i)\cup\bigcup_iY_i
```

contains at least `n` unit-separated points. The cardinality count is exact: the old `S_i` are removed first; packet interiors are disjoint from each other and from the retained points. Therefore `|A'|=|A|-sum_i|S_i|+sum_i|Y_i|`, even if a packet reuses an old interior coordinate. Unit separation follows from the shield above. Each polygon interior lies in the convex hull of its vertices, so all of `A'` lies in `conv(A)`, whose diameter is `D'`. Selecting any `n` points gives an `n`-point unit-separated set of diameter at most `D'<D`, contradicting global minimality.

The statement is an implication with an actual reduced endpoint and packets as hypotheses. It does not construct either one. It does not require newly opened contacts, triangle-freeness, or a separate upper-pair check once the full reduced set `A` already has diameter below `D`.

## 3. Moving-wall crossing barrier

Consider a continuous motion of a finite unit-separated labelled set. A fixed subset of labels forms a simple polygon throughout the motion, and every side remains strictly shorter than `2`. No other label can cross this wall. If a label changed from the interior to the exterior, continuity would give a first time when it lies on the wall. At a vertex it coincides with a distinct wall label; in the relative interior of a side of length `ell<2`, it is within `ell/2<1` of at least one endpoint label. Either case violates unit separation. Simplicity throughout ensures the inside/outside status can change only through such a boundary event.

This is a label-preservation barrier for an already existing feasible motion. It does not supply a continuation of a first-order descent, preserve simplicity without a hypothesis, or prove compatibility among several moving wall interiors.

## 4. All-order flat-wall capacity plateau

For every integer `M>=2`, let

```math
\tau=\frac1{100M^3},\quad c=\frac{1-\tau^2}{1+\tau^2},\quad s=\frac{2\tau}{1+\tau^2},\quad
u=(1,0),\quad v=\left(\frac{c-\sqrt3s}{2},\frac{s+\sqrt3c}{2}\right).
```

Thus the angle between `u,v` is `theta=pi/3+2 arctan(tau)`. Since `tau<=1/800`, `c>1-2/800^2` and `s<2/800`; hence `cos(theta)=(c-sqrt(3)s)/2>(1-2/800^2-2sqrt(3)/800)/2>49/100`. Also `c<1` and `s>0`, so `cos(theta)<1/2`. Define

```math
G_M=\{iu+jv:0\le i,j\le M\},\qquad q=(-2,-2),\qquad r=(10M,0),\qquad A_M=G_M\cup\{q,r\}.
```

For integer differences `(a,b)`, squared grid distances are `a^2+b^2+2ab cos(theta)`. If one difference is zero, the squared distance is the square of the other integer. If `a,b` have the same sign and are both nonzero this exceeds one. If they have opposite signs, it equals `(abs(a)-abs(b))^2+2 abs(a b)(1-cos(theta))>1`, since `cos(theta)<1/2`. Hence the only grid contacts are the adjacent `u` and `v` steps; their graph is bipartite and triangle-free. Grid coordinates have nonnegative coordinates, so `|q-(iu+jv)|^2>=8`; also their first coordinate is at most `M(1+cos(theta))<3M/2`, so their distance from `r` is greater than `17M/2`. Thus `q,r` are separated from the grid and contact-isolated.

The grid-pair squared distances are at most `3M^2`: when the coordinate differences have the same sign use `2 cos(theta)<1`, and for opposite signs discard the nonpositive cross term. Also

```math
|q-(iu+jv)|^2=(i+j\cos\theta+2)^2+(j\sin\theta+2)^2\le3M^2+10M+8,
```

using `0<cos(theta)<1/2` and `0<sin(theta)<1`. The maximum squared distance from `r` to the grid is `100M^2`, attained at the origin. For the latter, squared distance is convex on the grid parallelogram and its four corner values are `100M^2`, `81M^2`, `(101-20 cos(theta))M^2`, and `(82-18 cos(theta))M^2`, all at most `100M^2`. Meanwhile

```math
|r-q|^2=D_M^2=(10M+2)^2+4.
```

Thus `r q` is the unique actual diameter pair. Its endpoints have no unit contacts, so stationarity forces the multiplier on `r q` to be zero. A contact-only nonnegative equilibrium is also zero: dotting force balance with the point coordinates gives a fixed-sign sum of contact multipliers times their squared lengths, hence all contact multipliers vanish. The source has no normalized nonnegative KKT diameter stress. It is not globally optimal: `n=(M+1)^2+2` points from the square lattice fit in `M+2` columns and `M+1` rows because `(M+2)(M+1)-n=M-1>=1`; their squared diameter is at most `(M+1)^2+M^2<D_M^2`.

Delete `r` and scale every retained point by `L=1+t`, where `0<t<=1/(10M^2)`, and call the resulting set `A_t`. All retained distances become strictly greater than one. Since `3M^2+10M+8<=10M^2` for `M>=2` and `L^2<2`,

```math
\operatorname{diam}(A_t)^2\le L^2(3M^2+10M+8)<20M^2<D_M^2.
```

Use the `4M` boundary labels of the scaled grid as the wall `Q_t`, with each consecutive wall edge of length `L<sqrt(3)`. Its interior contains exactly `S=(M-1)^2` retained grid points, strictly guarded from all wall vertices.

For any weakly guarded, internally unit-separated packet `Y` in this parallelogram, `Y` together with the `4M` wall vertices is unit-separated in the closed convex parallelogram. The finite Oler inequality [Lemma 21.1](../theory/03-oler-shell.md) gives

```math
|Y|+4M\le \frac{2}{\sqrt3}L^2M^2\sin\theta+2LM+1.
```

Here `(2/sqrt(3))sin(theta)=c+s/sqrt(3)<=1+2tau`. Subtracting `(M+1)^2` from the right side leaves at most

```math
M^2(2t+t^2)+2\tau M^2(1+t)^2+2Mt
\le \frac15+\frac1{400}+\frac1{50}+\frac1{10}
=\frac{129}{400}<1.
```

The first term bound uses `t<=1/(10M^2)` and `M>=2`; the second uses `(1+t)^2<2`; and the last uses `M>=2`. Integer rounding yields `|Y|+4M<=(M+1)^2`, hence `|Y|<=S`. The old interior grid attains `S`, so the weak packet capacity is exactly `S` for every `M>=2` and every `t` in the interval. Refilling the one deleted label together with all `S` old interior labels requires `S+1` sites; this fixed wall has no spare site.

This is an unbounded family of triangle-free strict reduced endpoints with phase error `O(M^-3)` and all old contacts strictly opened, but every source is nonglobal and lacks normalized KKT stress. It refutes the inference that small phase error and strict contact opening alone force extra capacity at a specified flat wall. It does not refute the canonical global-source theorem, a different wall, several walls, or a larger relocation.

## 5. Certificate audit and scope

The frozen verifier uses exact rational arithmetic in `Q(sqrt(3))`, with no floating tolerances. It checks every source, endpoint, and square-lattice-competitor pair; the exact contact and diameter graphs; triangle-freeness; wall lengths and guards; and the Oler rounding for `M=4,6,8,12` at the endpoint `t=1/(10M^2)`. I reran it from the frozen source snapshot. Additional exact calls to its `fixture` function for `M=2,3,5` also passed. These finite checks corroborate the algebra but do not prove the all-`M`, all-`t` bounds, arbitrary-packet capacity, or nonglobality of every member; those conclusions follow from the analytic inequalities above.

| Claim | Dependencies | Limitation |
| --- | --- | --- |
| `C-NONCONTACT-WALL-WEAK-SHIELD` | First-exit geometry | Weak separation may be exact; no strictification |
| `C-POST-DESCENT-WEAK-WALL-REFILL` | `C-NONCONTACT-WALL-WEAK-SHIELD` | Actual reduced endpoint and all packet capacities are hypotheses |
| `C-UNIT-SEPARATED-MOVING-WALL-CROSSING-BARRIER` | None | No motion is constructed |
| `C-NEAR-TRIANGULAR-WALL-CAPACITY-PLATEAU-REGRESSION` | `C-NONCONTACT-WALL-WEAK-SHIELD`; finite Oler inequality | Nonglobal examples only; no canonical C-II conclusion |

No claim is made that the located stress-deletion candidate in the source report produces a suitable endpoint or that a canonical source admits one of these packets. The C-II finite-move/payment obligation and Level I remain open.

## Integration transaction

Audit.169 promotes the four exact claims above in state `2026-10-08.audit.165`. The promotion PR and protected validation are recorded in Audit cycle 169 of the integration ledger after merge.
