<!-- theorem-state: {"artifact_id":"ART-3AB276514CCC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: physical payment for every blocked odd-shell wall proposal

Date: 2026-10-06. Authority: `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`,
state `2026-10-05.audit.62`. Classification: **proved candidate awaiting
independent audit** for the new one-vertex payment; **regression** for
the constructed filled shells. No promotion. C-II and Level I remain open.

The regular-shell stress and dense-filling obstruction are prior work:
shared theory, Section 14 of `docs/theory/02-nonlinear-and-regressions.md`.
This report uses that family to test the new convex one-vertex shield.
It does not rediscover the shell as a disproof. Its global optimality is
not assumed; the fillings constructed below have strict competitors.

The implication being composed is

`one inward wall site per loaded vertex -> a full-source lexicographic
competitor unless blocked -> distinct isolate/physical-pair payment ->
independent whole-source competitor when the full population count pays it`.

## 1. Exactly checked source normalization data

Let `q>=65` be odd, `alpha=pi/q`, and

\[
 R={1\over2\sin\alpha},\qquad
 v_j=R(\cos(2j\alpha),\sin(2j\alpha)).
\]

The regular polygon has unit boundary sides, diameter
`D_q=2R cos(alpha/2)=1/(2sin(alpha/2))`, and actual diameter graph
`j -> j+(q-1)/2`, an odd cycle with `q` edges. All other wall pair
distances are strictly between one and `D_q`. Put any additional source
points strictly inside the polygon, unit-clear from every wall vertex
and strictly separated from one another. They are contact isolates;
every pair involving one of them is strictly below `D_q`.

The known normalized ring stress is

\[
 \alpha_e=D_q^2/q\quad(e\in C),\qquad
 \beta_h=1/q\quad(h\in H).
\tag{1}
\]

It has every actual contact and diameter coefficient positive. The
isolates have zero stress coordinates and are still retained in the
source. Their free coordinates are not assigned a core affine kernel.

For clarity, the following Fourier verification checks the stronger
nonisolated-core algebraic properties rather than appealing only to KKT
equilibrium. Write `s=sin(alpha/2)`, `c=cos(alpha/2)` and
`k=(q-1)/2`. The stress eigenvalue in mode `l` is

\[
 \lambda_l={4\over q}
 \left[D_q^2\sin^2(l\alpha)-\sin^2(lk\alpha)\right].
\]

For even `l`, this is

\[
 {4\over q s^2}\sin^2(l\alpha/2)
 \left[\cos^2(l\alpha/2)-s^2\right],
\tag{2}
\]

and for odd `l`, it is

\[
 {4\over q s^2}\cos^2(l\alpha/2)
 \left[\sin^2(l\alpha/2)-s^2\right].
\tag{3}
\]

Within `1<=l<=q-1`, these are positive except at `l=1,q-1`.
Together with the constant mode, the core stress is PSD with exactly
the three affine scalar kernel modes. Its core rank is `q-3`.

For mixed bar rigidity, use radial/tangential velocity coordinates
`a_j,b_j`. A bar of step `t` imposes

\[
 \sin(t\alpha)(a_j+a_{j+t})
 +\cos(t\alpha)(b_{j+t}-b_j)=0.
\]

After removing nonzero Fourier phase factors and the factor `i`, the
determinant of the two Fourier rows for steps `1,k` factors, for
even `l=2m`, as

\[
 (-1)^{m+1}2c\sin(l\alpha/2)
 [\cos^2(l\alpha/2)-s^2],
\tag{4}
\]

and for odd `l=2m+1`, as

\[
 (-1)^{m+1}2c\cos(l\alpha/2)
 [\sin^2(l\alpha/2)-s^2].
\tag{5}
\]

Only translation modes `1,q-1` and rotation mode `0` remain. Thus the
actual contact/diameter framework on the core has rank `2q-3`. The
verifier checks the factor identities exactly as Laurent polynomials,
not as floating ranks. These properties do not prove global optimality.

## 2. A finite wall site whose upper constraints are already safe

For each wall vertex define

\[
 x_j=(1-2/R^2)v_j,\qquad \epsilon=|x_j-v_j|=2/R.
\tag{6}
\]

Here `R>10`. The point is strictly inside the polygon: its inward
radial depth `2/R` exceeds `R(1-cos(alpha))`.
For every other wall vertex `v_i`,

\[
 |x_j-v_i|^2=(1-2/R^2)|v_j-v_i|^2+4/R^2
 \ge1+2/R^2>1.
\tag{7}
\]

Thus `x_j` is in the one-deleted-vertex packet region `W_{F,v_j}`
of the new convex shield theorem. If no interior isolate has distance
at most one from it, delete `v_j` and insert `x_j`. The shield checks
every exterior source point; (7) checks every retained wall vertex;
the hypothesis checks every interior isolate. The inserted point is
strictly interior to the source hull, so every new upper pair is below
the old global `D`. Cardinality is unchanged and no contact is created.
The two unit wall contacts at `v_j` disappear. This contradicts canonical
contact minimality even if other old diameter pairs remain unchanged.

There are no inactive-upper exceptions to hide in this endpoint. The
old diameter graph is cyclic, and the new point's interior-hull upper
bound is a finite full-source check. All possible failures of this
specific replacement are interior-isolate lower blockers.

## 3. An isolate pays at most one side or one vertex

Let `z` be a source isolate inside the polygon, with
`|z-v_i|>1` for every wall vertex. Suppose it blocks one or more sites
`x_j`, meaning `|z-x_j|<=1`. Put `r=R-2/R`, `t=|z|` and `h=R-t`.
Blockage implies `t>=r-1>0` and `h<=1+2/R`.

A closest angular wall vertex is at angle at most `alpha` from `z`.
Its separation gives

\[
 1< h^2+2Rt(1-\cos\alpha)
 \le h^2+{1\over2(1+\cos\alpha)}<h^2+1/3.
\]

Hence `h>4/5`. Blocked sites lie on one circular arc of the radius-`r`
circle, of width below `pi`. If two blocked sites were nonadjacent in
wall order, their arc separation would be at least `4alpha`. At least
one would be at angle at least `2alpha` from the radial direction of `z`.
Its unit-distance requirement would imply

\[
 (h-2/R)^2+{(R-h)(R-2/R)\over R^2}\le1,
\]

or

\[
 h^2-5h/R+2/R^2+2h/R^3\le0.
\tag{8}
\]

But `R>=10`, `h>4/5` give

\[
 h^2-5h/R+2/R^2+2h/R^3
 >h(h-1/2)>0,
\]

a contradiction. Therefore an isolate blocks at most two sites; if two,
they are the endpoints of one actual unit wall side. This is a physical
multiplicity bound, not an arbitrary matching assignment.

If every site (6) fails, the source consequently has at least

\[
 \boxed{|Z_{\rm block}|\ge(q+1)/2}
\tag{9}
\]

distinct interior isolates in the radial collar
`4/5<R-|z|<=1+2/R`. Each counted pair is genuinely near-unit:
`1<|z-v_j|<=1+2/R` by the triangle inequality. A blocker used twice
pays only one source point and exactly two physical lower pairs.

In the regular ring there are no O--O trains. All `q` contact trains
are singleton outside-to-bounded trains of the one `q`-sided face.
Equation (9) therefore cannot be charged to an O--O terminal bank.
The exceptional degree bank is `Q-f=q-5`, which is linearly large.
It is not numerically exceeded by the demand (9).

## 4. The physical lower obstruction can be realized exactly

Set `delta=1/(100R^2)`. On each matching wall edge `(v_0,v_1)`,
`(v_2,v_3)`, ..., `(v_{q-3},v_{q-2})`, put its interior circle
intersection point at distance `1+delta` from both endpoints:

\[
 z_j=\left[R\cos\alpha-
 \sqrt{(1+\delta)^2-1/4}\right]n_{j+1/2}.
\tag{10}
\]

Here `n_{j+1/2}` is the radial unit direction of that wall-side midpoint.
At the unmatched vertex put

\[
 z_*=(R-1-\delta)n_{q-1}.
\tag{11}
\]

All these points are strictly separated from all wall vertices and
from one another, and are strictly inside the polygon. Each point
(10) blocks exactly its two matching endpoint proposals, and (11)
blocks exactly the unmatched one. Thus `(q+1)/2` actual contact
isolates realize equality in (9).

The geometry is valid for every odd `q>=65`. The matching pair points
have common radius greater than `R-2` and angular gaps at least
`4alpha`, so their pairwise distance exceeds
`2(1-2/R)cos(alpha)>1`. The singleton has radius above `R-2` and
angular distance at least `3alpha` from any matching midpoint. For
`alpha<1/10`, `sin(3alpha/2)>(7/5)sin(alpha)`, giving squared distance
above `(49/25)(1-2/R)^2>1`. Its own wall clearance and the matching
points' nearest-wall clearance are `1+delta` by construction.
The sine inequality follows directly from
`sin(3alpha/2)>=3alpha/2-(3alpha/2)^3/6>(7/5)alpha`
and `sin(alpha)<=alpha` in this range.

For (10), its inward radial projection from either wall endpoint is
`1/(4R)+sqrt((1+delta)^2-1/4)cos(alpha)>4/5`. Moving that endpoint
inward by `2/R` therefore reduces the point's squared distance below
one. Formula (11) blocks by the direct distance `1+delta-2/R<1`.
The multiplicity theorem rules out any additional blocked sites.

This is an exact physical obstruction family to automatic one-vertex
clearance, retaining the source points that cause failure. It is not a
family of global minimizers.

## 5. Compose immediately: the constructed dense filling is not global

Add a translated triangular lattice of spacing `ell=1+q^-2` inside the
open disk of radius `R-3`, choosing exactly

\[
 N_q=\left\lfloor{\pi(R-3)^2\over a_0\ell^2}\right\rfloor,
 \qquad a_0=\sqrt3/2.
\tag{12}
\]

Translation averaging supplies that many sites. They are strictly clear
of the wall and collar isolates by radial gaps greater than one, and
strictly separated internally by `ell>1`. Every source point is retained
in the cardinality

\[
 n_q=q+(q+1)/2+N_q=\Delta_2D_q^2+O(D_q).
\]

The macroscopic interior population is quadratic, the only actual unit
contacts are the wall cycle, and every proposal (6) is still blocked.
The PSD/core-rigidity conclusions of Section 1 remain unchanged.

Nevertheless a whole-source independent packet excludes this constructed
family. Put `rho_q=pi D_q^2/(4a_0)`. Since `q<2pi R`,
`R^2sin^2(alpha/2)<1/12`, and `4/5<a_0<1`,

\[
 \rho_q-n_q
 \ge \pi\left[(6/a_0-3)R-(9+1/12)/a_0\right]-1/2
 \ge\pi(3R-545/48)-1/2>0.
\tag{13}
\]

Choose a disk radius strictly below `D_q/2` and triangular lattice
spacing strictly above one, both close enough to their limiting values
that the translated-lattice mean exceeds `n_q-1`. Some translate then
has at least `n_q` sites. Select that many. Their mutual distances are
strictly above one and their diameter is strictly below `D_q`.
Delete the entire old source and use this packet. There is no old-site
refill assumption, uninspected boundary guard or cardinality loss.

Thus even a dense physical collar realizing all lower blockers, positive
actual KKT data, PSD affine core kernel and full mixed core rank can be
globally beaten. No such local data constitutes a disproof.

## 6. The exact remaining capacity problem

The deficit in (13) uses the particular deep filling (12). It does not
bound an arbitrary optimal packing of the rest of the macroscopic chamber.
Additional boundary-order population could remove that deficit. A
canonical regular-ring survivor would need both of the following:

1. A blocker cover of every wall proposal, with the sharp physical
   multiplicity and collar constraint in Section 3.
2. Enough further interior population that the full-source independent
   lattice packet no longer pays cardinality, while every one-deleted-wall
   packet also has capacity at most the old interior population.

For an actual interior population `z`, the convex shield would contradict
the source if any `W_{F,v}` had strict packet capacity at least `z+1`.
Alternatively, any complete independent sub-`D` packet of size `q+z`
would contradict it. Neither universal packet statement has been proved.
The one-chart boundary-loss report from September is unreviewed and does
not supply an arbitrary-interior or multigrain capacity theorem.

The payment (9) kills sources with fewer than `(q+1)/2` near-wall
isolates, and (13) kills the explicit blocked dense filling. It does
not kill all large-degree chambers, exterior caps, or the general
macroscopic-container branch. The full-core coupled-motion problem also
remains open. No exhaustion or Level I closure is claimed.

## 7. Exact verifier

[The verifier](../../research/verify_target_c_odd_shell_single_vertex_barriers_2026_10_06.py)
uses directed rational intervals with exact Machin-series bounds for `pi`
and alternating Taylor bounds for the initial small sine/cosine angles.
It reuses the local interval helpers of the capped-wall verifier.

For `q=65,101,201`, it checks all wall/collar source pairs, actual
diameter pairs, every root/blocker relation, the matching/singleton
multiplicity, and the certified translation-average population deficit.
The three cases have 293, 772 and 3350 points after the analytically
certified deep filling. The lattice translations are certified by the
proved averaging theorem, not enumerated coordinate files. There are
61680 wall/collar source-pair checks and 27597 blocker-pair checks.

It also checks 820 exact Laurent-polynomial stress/rigidity factor
identities for eight odd cardinalities. Positivity and exact rank follow
from the angular ranges in (2)--(5); they are not inferred from numerical
matrix ranks or interval eigenvalues.
