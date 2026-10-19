# Exact phase motion on an imbalanced two-family rhombic grid

**Classification:** unreviewed finite-family result and regression. It is not a
claim about canonical global minimizers. Level I and Target B remain open.

**Contributor:** OpenAI Codex (GPT-6 Luna xhigh), producing this proof and
checker with AI assistance. **Independent mathematical review:** not performed.
This contribution is offered under Apache-2.0-compatible terms and uses only
the pinned repository sources and original calculations below.

## Question and exact scope

The Target B phase cut gives a real potential on an acyclic retained crossing
graph. On an oriented crossing edge, the direction gap is
`theta = pi/3 + delta`, and the canonical relaxation `v = -x` decreases the
retained `delta`. This note asks whether that local phase relaxation itself
gives a strict finite diameter competitor on an exact phase-imbalanced source.
The downstream quantity is the source diameter `D^2`, with the source
cardinality and every unit-separation constraint fixed. If the phase direction
shortens every active diameter pair, continuity would give a strict finite
competitor; if it does not, this model identifies the exact active-pair
obstruction. A separate full-source deformation tests whether an opposite
phase change can give a finite competitor on this restricted family.

The candidate lemma is for the complete two-family grid

`P_{M,N}(theta) = { i u + j v : 0 <= i <= M, 0 <= j <= N }`,

where `M,N >= 1`, `|u|=|v|=1`, and `pi/3 < theta < pi/2` is their angle. The
`M`-by-`N` rhombic patch has `M` tracks in one direction and `N` in the other,
so its train-crossing graph is `K_{M,N}`. The two train classes have unequal
populations when `M != N`; assigning phase labels 0 and 1 gives the actual
two-class potential: orient each crossing from label 0 to label 1, take
`lambda=0,1`, and take the real potentials `x=0,delta`. Every crossing then has
the positive defect `delta=theta-pi/3`.

## Result

Write `c=cos(theta)`. A source-pair difference has the form `a u + b v`, where
`a,b` are integers, `|a|<=M`, and `|b|<=N`. If both coefficients are nonzero,

`|a u+b v|^2 >= a^2+b^2-2c|ab| >= (1-c)(a^2+b^2) > 1`,

because `0<c<1/2` and `a^2+b^2>=2`. If one coefficient is zero, its length is
an integer and is at least 1. Thus the only unit pairs are the horizontal and
vertical grid edges. The calculation includes every pair among the full source
labels; no labels are removed.

The diameter is

`D(theta)^2 = M^2 + N^2 + 2 M N cos(theta)`,

attained at the two opposite grid corners with difference `M u+N v`. Therefore
the canonical phase relaxation, which lowers `theta` toward `pi/3`, increases
this active diameter. Its derivative is
`d(D^2)/d(theta) = -2 M N sin(theta) < 0`, so `d(delta)/dt < 0` gives
`d(D^2)/dt > 0`. This is an exact active-diameter obstruction to identifying
phase-defect contraction with diameter contraction.

In the opposite direction, increase `theta` continuously to `pi/2`. The
unit-contact edges remain unit, the bound above keeps every other pair at least
1 throughout the path, and the diameter strictly decreases. At the endpoint,
the same labels form a rectangular square-lattice grid with diameter squared
`M^2+N^2`, a strict improvement of `2MN cos(theta)`. Hence every member of
this exact oblique-grid family has a same-cardinality full-source competitor.
The construction is finite and checks every lower and upper pair constraint.

## Exact finite instance and falsification controls

The checker uses `M=2`, `N=1`, `u=(1,0)`, and `v=(7/25,24/25)`. These vectors
have unit length and `cos(theta)=7/25`, so `pi/3 < theta < pi/2` exactly.
There are six source points, seven unit contacts, and two rhombic faces. Its
train graph is `K_{2,1}`, with imbalanced class sizes 2 and 1. Exact pair
enumeration gives:

- old diameter squared `153/25`, with the unique active pair from `(0,0)` to
  `(2,1)`;
- the opposite-corner pair from `(0,1)` to `(2,0)` is initially inactive at
  squared distance `97/25`, grows to `5`, and is still below the old `153/25`
  diameter when it becomes co-active at the perpendicular endpoint;
- the phase-relaxed `theta=pi/3` endpoint diameter squared `7`, which is
  larger than `153/25` (the wrong-sign regression);
- the perpendicular endpoint diameter squared `5`, which is strictly below
  `153/25` by `28/25`;
- all 15 unordered source pairs in each of the three rational configurations
  satisfy distance at least 1. On the entire path to `pi/2`, the displayed
  quadratic lower bound keeps every non-axis difference above 1.
- the train crossing graph is `K_{2,1}` with two edges; the exact contact graph
  is the rectangular grid graph, bipartite by the
  parity of `i+j`, so the source is triangle-free.

`verify.py` checks the rational initial and perpendicular endpoint ledgers,
the exact contact graph, the old active pair, the phase-relaxation sign, and
the path-wide lower-bound controls. A failure of any pair inequality, the
diameter formula, or the wrong-sign control falsifies this instance.

Reproduce from the repository root:

```sh
python research-packages/e99-pass-20261018-homelab-03/verify.py
```

## Comparison, limits, and next lemma

The canonical phase-cut proof already says that defect contraction has no
established active-diameter sign, and its square regression shows active
diameters can block angle contraction. The coherent phase-star/near-extremal
subcases are also already excluded by the promoted PC/CR/PS/NE work. This
contribution is complementary only at the finite-source level: it gives an
explicit exact imbalanced grid, exhibits the wrong sign for the canonical
relaxation, and supplies a full-source competitor in the opposite direction.
It does not extend those prior asymptotic exclusions.

The grid is a finite regression, not a first-order-jammed survivor and not a
global minimizer; the displayed competitor proves it is nonglobal. No claim is
made for incomplete crossing graphs, multiple phase grains, interfaces,
contact isolates added outside the grid, or arbitrary jammed sources. The
result does not prove a uniform theorem for every sufficiently large
cardinality or every global minimizer, and it does not close the Target B shell
inequality.

**Open next question.** For a source with at least three phase classes or
multiple grains, can one choose a source-derived train-angle path whose
derivatives strictly decrease every actual active diameter pair while
preserving all unit contacts? This could change the strict-sub-`D` alternative
in Target B and controls the exact quantity `max_{i<j}|p_i(t)-p_j(t)|^2`.
The changed hypothesis is removal of the exact complete two-family grid
structure. If such a direction exists, the finite-source continuity argument
then gives a competitor; if it does not, an exact nonnegative diameter stress
must be identified. First action: compute the full active-diameter Jacobian on
one multi-grain phase source and compare it with the exact potential direction.
The blocker is a source-wide direction or stress certificate that includes
every train and source label. Do not infer a general conclusion from this
finite grid.

## Source and verification status

Baseline source SHA: `7d0a450fe66991036541023f95c44c064a04b6a8`.
Theorem state: `2026-10-15.publication.2`; priority revision:
`public-frontier.3`; catalogue revision: `public-frontier.9`. The task
catalogue listed `existing_checks: []`; the launch overlap snapshot and live
surfaces were inspected. Open PR #102 proves an abstract Target A source-image
Hall formula and is outside this Target B geometric scope. Discussion #83 was
read; it contains no matching Target B phase-deficit handoff.

Actual checker and repository commands, outcomes, environment, artifact hashes,
and any remaining validation obligations are recorded in the PR handoff.
Required repository-wide theorem-certificate replay is deferred to the merging
agent. This finite result has no theorem-state, route, or priority promotion.
