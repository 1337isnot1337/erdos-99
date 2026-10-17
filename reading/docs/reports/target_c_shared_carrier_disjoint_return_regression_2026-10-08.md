> Generated reading edition · [exact source](../../../docs/reports/target_c_shared_carrier_disjoint_return_regression_2026-10-08.md) · source SHA-256 `cc5a6310450c8ffd5b701fe71e25b637f654109784fde06270ebd0f8b728e3ec`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-64CD1558FB7C","canonical":false,"claim_ids":["C-SHARED-CARRIER-DISJOINT-RETURN-COST-REGRESSION"],"claim_statuses":{"C-SHARED-CARRIER-DISJOINT-RETURN-COST-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C: a small common carrier need not support many disjoint returns

Date: 2026-10-08.
Run base: `09d1665e37af3907c099959138187e3eb5e62698`.
Canonical comparison: `0ce9dc0ac674c5018f0fc271c0263d9d10e09936`,
theorem state `2026-10-08.audit.137`.
At this frozen source snapshot, the construction was awaiting independent audit and was not yet registered. Its later independent audit is recorded in [Audit.186](../audits/target_c_shared_carrier_disjoint_return_independent_audit_2026-10-09.md); the theorem manifest now records the precise artificial-pin scope as a regression. Level I and C-II remain open.

Rechecked after rebasing onto
`023917ace0719d0050664a8a08fed1eb5cdb2013`, state
`2026-10-08.audit.139`. The two newly promoted audits add a scoped
support hub and reduced-cardinality exterior-cap motions; they do not
alter this regression or supply its missing actual-loaded hypotheses.

## 1. The implication being tested

The candidate [train-bank report](target_c_train_cut_hull_bank_2026-10-08.md)
proves two different facts on its canonical source:

1. counted train ends share a contact carrier with at most
   `sum_N d_tau + 2T` edges;
2. an endpoint-specific separator argument gives many vertex-disjoint
   returns in the full contact graph.

These facts do not put the disjoint paths in that carrier or bound their
total length by the carrier's edge count.
The proposed bridge being tested was:

    small shared physical carrier + positive pinned rigidity
      -> many disjoint returns with the same small edge budget
      -> independently paid train-return population.

The first implication is false in the explicitly weaker artificial-pin
setting below. The regression is train-rich: it has quadratic strict
rhombus population, only linear rhombus area excess, strictly positive
pinned equilibrium, and full pinned infinitesimal contact rigidity.
It is not a counterexample to a theorem using actual diameter loads and
global minimum-diameter optimality.

## 2. Exact rational family

For every integer `m>=12` let
$$
r_m={\lfloor m/\sqrt3\rfloor+2\over m},\qquad
v_m=\left({1-r_m^2\over1+r_m^2},{2r_m\over1+r_m^2}\right),
\qquad u=(1,0).
$$
The integer in the numerator can be computed as
`isqrt(3*m*m)//3 + 2`; thus no numerical square-root decisions enter
the coordinates.
For a rational parameter `t` let `R(t)` be rotation by `2 arctan(t)`:
$$
R(t)={1\over1+t^2}
\begin{pmatrix}1-t^2&-2t\\2t&1-t^2\end{pmatrix}.
$$
Define
$$
t_j={m+1-2j\over100m^2},\quad
v_j^-=R(t_j)v_m,\quad v_j^+=R(-t_j)v_m,\quad
V_j^\pm=\sum_{\ell=1}^jv_\ell^\pm,\quad V_0^\pm=0.
\tag{SR1}
$$
The symmetry `t_{m+1-j}=-t_j` gives
$$
V_m^-=V_m^+.
\tag{SR2}
$$

The labels are
$$
\{(i,j):0\le i\le m-1,\ 0\le j\le m\}
\ \cup\
\{(i,j):m+1\le i\le2m,\ 0\le j\le m\}
\ \cup\ \{(m,0),(m,m)\}.
$$
Their physical positions are `iu+V_j^-` on the left and
`iu+V_j^+` on the right. The two middle labels use the common endpoint
coordinates in SR2. There are
$$
n_m=2m(m+1)+2
\tag{SR3}
$$
source points.

The artificial pin set `B_m` consists of every source label with
`i=0`, `i=2m`, `j=0` or `j=m`. It has `6m` labels. These pins are a
specified boundary condition, not a claimed actual diameter-endpoint set.

## 3. All lower distances and actual contacts

For all `m>=12` the increments satisfy
$$
{1\over4}<(v_j^\pm)_x<{1\over2},\qquad
(v_j^\pm)_y>{4\over5},\qquad |v_j^\pm|=1.
\tag{SR4}
$$
Here
$$
{1\over\sqrt3}+{1\over m}<r_m<
{1\over\sqrt3}+{2\over m}.
$$
The base angle is strictly above `pi/3` by at least
`32/(25m)`, while the rotations have absolute angle below `1/(50m)`.
The upper bound `r_m<3/4`, together with this rotation bound, gives
the first lower bound in SR4; the remaining bounds follow from the
first-quadrant unit-circle coordinates.
Also
$$
|V_j^\pm-jv_m|<{1\over50}.
\tag{SR5}
$$

Within one grain, labels with row difference at least two have vertical
distance greater than `8/5`. With row difference one, a same-column
pair is an intended unit contact; the short adjacent-column diagonal
has squared length `2-2(v_j^\pm)_x>1`. All other one-row pairs are
farther apart. Same-row separations are positive integers.

Across the two grains the column difference is at least two. For row
difference at most one, SR5 gives horizontal separation greater than
`2-1/2-1/25>1`. For row difference at least two it gives vertical
separation greater than `8/5-1/25>1`.
For the two middle labels, every comparison belongs to one grain with
the same endpoint `V_0` or `V_m`; the preceding within-grain tests
apply.

Consequently the actual unit contacts are precisely the pairs whose
indices differ by one horizontally or vertically and both labels are
present. They form a bipartite graph under index-sum parity, so there
is no unit triangle. No contact isolate is present.

The two grains contain
$$
R_4=2m(m-1)
\tag{SR6}
$$
strict unit rhombi. Each has area `(v_j^\pm)_y>sqrt(3)/2`.
The base-angle departure from `pi/3` is `O(1/m)`, as are the individual
rotation angles. Therefore
$$
\sum_{\text{rhombi}}\left(\operatorname{area}
 -{\sqrt3\over2}\right)=O(m).
\tag{SR7}
$$
The middle gap is one convex, possibly collinear at its two cap
midpoints, bounded contact face with `2m+4` sides and area `O(m)`.

## 4. Strictly positive pinned equilibrium

Orient each vertical edge upwards. Give it the positive stress weight
$$
b_j^\pm={1\over(v_j^\pm)_y}.
$$
At an unpinned vertex in row `j` the difference of its weighted
vertical neighbor vectors is
$$
\beta_j^\pm u,\qquad
\beta_j^\pm=
{(v_{j+1}^\pm)_x\over(v_{j+1}^\pm)_y}
 -{(v_j^\pm)_x\over(v_j^\pm)_y}.
\tag{SR8}
$$
The left increment angles strictly decrease, hence `beta_j^->0`;
the right increment angles strictly increase, hence `beta_j^+<0`.

For the horizontal edge from column `i` to column `i+1` in an
interior row, use
$$
a_{i,j}^-=(m-1-i)\beta_j^-
\quad(0\le i\le m-2),
\qquad
a_{i,j}^+=(i-m)(-\beta_j^+)
\quad(m+1\le i\le2m-1).
\tag{SR9}
$$
These are strictly positive. Their horizontal force difference is
`-beta_j^\pm u`, including the one-sided contact at each inner wall.
It cancels SR8 exactly. Every top and bottom horizontal edge can have
weight one because its endpoints are pinned.

Thus every contact has positive weight and every unpinned source point
is in exact equilibrium. The reactions at `B_m` are unrestricted
artificial-pin reactions. They are not certified as sums of actual
diameter-edge forces.

## 5. Full pinned contact rank

Let a pinned infinitesimal bar flex have velocity zero on `B_m`.
Every horizontal row runs from an outer pin to the inner wall.
Horizontal contact equations make the x-velocity constant along that
row, hence zero. After this, every vertical equation has nonzero
y-coefficient by SR4. The pinned bottom row then makes the y-velocity
zero up each column.

This also exhibits an explicit square triangular minor: one
horizontal row per free point, ordered from its pinned outer side,
then one downward vertical row per free point, ordered from bottom
to top. There are `2|A_m\setminus B_m|` distinct selected rows and
all pivots are nonzero. The pinned rigidity matrix has full column rank.

## 6. The common carrier and its two-path bottleneck

There are `2(m-1)` horizontal-edge trains, each crossing `m` rhombi,
and `2m` vertical-edge trains, each crossing `m-1` rhombi. The four
horizontal cap edges incident to no rhombus are singleton trains.
Therefore
$$
T=4m+2.
\tag{SR10}
$$
Choose all nonsingleton trains as `A` and the four singleton trains
as `N`. Each inner-face terminal recipient reaches the outer boundary
through a singleton. The literal `N` rails have no edges. The shared
carrier `K_N` is the union of the outer boundary walk and the
middle-face boundary walk. It contains
$$
|E(K_N)|=8m\le2T.
\tag{SR11}
$$
Every selected inner terminal has a unit-contact return in this carrier.

Now choose one matched terminal vertex on each of the distinct
left-hand vertical-edge trains indexed by `j+1`, for
$$
X_m=\{(m-1,j):\lceil m/3\rceil\le j\le\lfloor2m/3\rfloor\}.
\tag{SR12}
$$
Each such train has an actual horizontal contact rail of `m-1`
edges. There are `|X_m|=m/3+O(1)` chosen roots.

In `K_N` the left inner wall is a simple contact chain that meets
`B_m` only at its bottom and top vertices. Deleting these two pin
labels separates `X_m` from `B_m`. Two disjoint wall paths exist,
one to each pin. Thus the endpoint-inclusive contact minimum cut and
maximum number of vertex-disjoint returns in `K_N` are exactly two.

In the full contact graph, the horizontal rows from `X_m` to column
zero are `|X_m|` vertex-disjoint returns to distinct pins. This is
the maximum possible count because there are only `|X_m|` roots.
Every full-contact path from `(m-1,j)\in X_m` to any pin must change
an index until `i` is `0` or `2m`, or `j` is `0` or `m`. Every
contact changes one index by one. Consequently every such return
has at least `floor(m/3)` unit steps, so any full set of disjoint
returns has total length at least
$$
|X_m|\lfloor m/3\rfloor=\Omega(m^2).
\tag{SR13}
$$
The disjoint returns therefore cannot be charged once to the `8m`
carrier edges.

## 7. Explicit failure of global optimality and source hypotheses

The two opposite corners `(0,0)` and `(2m,m)` have horizontal
separation greater than `9m/4` by SR4. Hence
$$
D_m^2>{81\over16}m^2>2n_m\qquad(m\ge12).
\tag{SR14}
$$
A square-grid crop of `n_m` unit-separated points has squared
diameter at most `2(ceil(sqrt(n_m))-1)^2<2n_m`. It is a strict
whole-source smaller-diameter competitor.
Thus every member of this family is nonglobal.

Moreover `D_m/m -> sqrt(7)` and `n_m/D_m^2 -> 2/7`. Its diameter
normalization is far below the global near-disk packing density.
Its two flat boundary rows contain many nonextreme artificial pins;
in particular `(m,0)` is pinned and is not a convex-hull vertex.
The verifier finds only two actual diameter endpoints in each tested
case, rather than the `6m` artificial pins.

The family does not satisfy canonical mixed contact/actual-diameter
rigidity, actual loaded-hull incidence, full-source KKT stress, global
roundness, or minimum-diameter optimality. It does not contradict the
candidate long-terminal separator theorem, the canonical loaded-return
theorems, or Level I.

The earlier
[positive pinned face-tail regression](../audits/target_c_positive_pinned_face_tail_independent_audit_2026-10-08.md)
already separates pinned rigidity from global optimality using a
long-face polygon without quadratic rhombus bulk. The present
construction addresses the different attempted implication combining
a train-rich common carrier with many disjoint contact returns.

## 8. Certificate and resulting proof obligation

Run

```text
python3 research/verify_target_c_shared_carrier_disjoint_return_2026_10_08.py
```

At `m=12,16,24` the exact `Fraction` certificate checks 919,727
full-source pairs, 1,848 strict rhombi, 3,910 positive contact weights,
the explicit triangular pinned minors, and both contact flow problems.
The carrier capacities are `2,2,2`; full-contact capacities are
`5,5,9`. It independently identifies actual diameter endpoints and
verifies a strict square-grid competitor.
The infinite-family conclusions SR7 and SR13 use the analytic proof
above; finitely many successful runs do not establish an asymptotic
claim by themselves.

No canonical theorem or frontier changes. The remaining bridge must
use the actual source hypotheses to supply independently paid
returns, an outside-region population gain, or a feasible full-source
finite replacement. It cannot silently identify the edge budget of a
shared carrier with the total cost of vertex-disjoint full-contact
returns.
