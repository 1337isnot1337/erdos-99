> Generated reading edition · [exact source](../../../docs/reports/target_c_actual_cut_finite_competitor_regression_2026-10-01.md) · source SHA-256 `96930e0cf234a648b053907e607a85583e48425b2017487cd37761b307779d5c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A26010C0F210","canonical":false,"claim_ids":["C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION"],"claim_statuses":{"C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C: an actual cut source with a finite competitor beyond its local barrier

**Date:** 2026-10-01

**Starting main:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`

**Previous checkpoint:** `63c610f0`, branch `swarm/root/c2-gap-cut-20261001`

**State:** `2026-09-14.audit.51`

**Classification:** registered regression in `2026-10-05.audit.60` as `C-ACTUAL-CUT-FINITE-BARRIER-REGRESSION`. Level I OPEN; C-I CLOSED; C-II OPEN.

```text
actual-source cut substitution -> certify every source-pair distance -> strict
same-cardinality diameter competitor. This source is not a global minimizer.
```

The [previous report](target_c_exact_phase_finite_barrier_and_coembedding_regression_2026-10-01.md)
gave an abstract finite move past a full-rank local barrier. The following
construction strengthens it to an actual unit-separated source with actual
nested contact cuts, and checks all source pairs. It retains no claim of
canonical C-II source existence.

## 1. Exact family, every real D >= 13

Put `u=(1,0)` and

$$
 c=391/409,\qquad s=120/409,
 \quad v_1=(c,s),\ v_2=(c,-s),\ v_3=(c,s).
$$

Define `q_0=0` and `q_j=sum_{i=1}^j(v_i-u)`. Use the three interval
packets

$$
 ([1,2],d_{12})=([1,2],(4/5,3/5)),
$$
$$
 ([2,3],d_{23})=([2,3],(3/5,4/5)),
 \qquad ([1,3],d_{13})=([1,3],(12/13,5/13)).
$$

For a packet `[a,b]` and each sign `eta in {-1,+1}`, write
`d_eta=(d_x,eta d_y)` and set

$$
 z_{ab}=-{q_{a-1}+q_b\over8},
 \quad p^-_{ab,\eta}=z_{ab}-{D\over2}d_\eta,
 \quad p^+_{ab,\eta}=z_{ab}+{D\over2}d_\eta.          \tag{1}
$$

Give these points labels `a-1` and `b`, respectively. Add the four chain
points `p_j=(j-3/2,0)`, with label `j`, for `j=0,1,2,3`.
These are sixteen distinct actual source points.

The contact graph has exactly the three chain edges `p_{j-1}p_j`. The
diameter graph has exactly the six pairs in (1), each of length `D`.
All twelve diameter endpoints are contact-isolated. Define nested subsets

$$
 S_i=\{p:\operatorname{label}(p)\ge i\},\qquad i=1,2,3.
$$

Every original contact crosses exactly one `S_i` and is oriented as `u`
from outside into the subset. These are actual contact cutsets. They are
not claimed to be the canonical global stopped O--O rhombic trains.

## 2. Exact finite competitor

Move each point of label `j` by `q_j`. Every chain edge is replaced by
`v_j`, so all three old contacts remain exactly unit. Every diameter pair
has the interval change

$$
 p^{+\prime}_{ab,\eta}-p^{-\prime}_{ab,\eta}
 =Dd_\eta+q_b-q_{a-1}.                              \tag{2}
$$

The old derivative matrix in the three independent train-angle coordinates
is exactly the full-rank matrix of the previous report. Weights `1/6`
give positive aggregate transverse virtual-work cancellation. The axial
cut totals and their nonzero differences are also unchanged.

**Proposition.** For every real `D>=13`, the old source is unit-separated
with diameter `D`, the new source is unit-separated with diameter `<D`,
and the old and new contact graphs are both exactly the three-edge chain.

**Proof certificate.** The coordinates of every point in both sources
have the form `Da+b` for rational vectors `a,b`. Each squared pair distance
therefore has a rational quadratic polynomial

$$
 P(D)=AD^2+BD+C.
$$

For every one of the 120 source pairs, the verifier forms `P_old-1`,
`P_new-1`, `D^2-P_old`, and `D^2-P_new`. For every required nonnegative
polynomial it checks

$$
 A\ge0,\qquad 26A+B\ge0,\qquad P(13)\ge0,
$$

with the last inequality strict whenever that source pair is required to
remain strict. These inequalities prove monotonicity and positivity on
the entire real ray `D>=13`; this is not finite sampling in `D`.
Original diameter polynomials are identically `D^2`; old and new contact
polynomials are identically one. All other required inequalities are
strict at 13 and remain strict on the ray. This proves the proposition.

At `D=13` the new squared diameter is exactly

$$
 {28248541\over167281}=169-{21948\over167281}<169.
$$

The smallest new noncontact squared distance at this diameter is
`61741/32720>1`. The certificate uses rational arithmetic only.

All old diameter endpoints are extreme points: an endpoint attaining the
maximum distance cannot be a nontrivial convex combination of other
source points, by strict convexity of squared distance. The six old
diameter segments form a genuine convex diameter matching, hence a
diameter thrackle. No separate scaffold is substituted for this source.

## 3. Failed construction before the center correction

Setting all `z_ab=0` realizes the old diameter vectors on one circle, but
the same full move is not feasible. At `D=13`, one previously strict pair
then acquires squared length `3481549/20450>169`. The six original
diameters still shorten. Thus testing old active rows alone would have
given a false full-source competitor.

The factor `-1/8` in (1) moves the initial chord centers enough to restore
the inactive-pair slack while preserving all six old diameter lengths.
The new construction checks every pair rather than inferring feasibility
from the active diameter list.

## 4. Exact missing canonical hypotheses

This family is **not** a Level I disproof. It has fixed cardinality 16
while its diameter can grow arbitrarily. The proposition explicitly
exhibits a strict competitor, so none of its old sources is globally
minimum-diameter.

It also fails full-source positive KKT equilibrium. At a diameter endpoint
there are no contacts and exactly one diameter edge. A strictly positive
diameter multiplier creates a nonzero force that no contact force can
balance. The aggregate identity `beta^T M=0` in the three cut coordinates
is therefore weaker than vertex-by-vertex KKT equilibrium. Canonical
`C-ZRF` is not available here; the loaded vertices are outside the contact
core. The positive-contact connected core, canonical mixed rigidity,
and the complete O--O rhombic grid are not encoded.

The regression now rules out the following **noncanonical** implication:

> Actual source cutsets, all actual diameter vectors, convex-thrackle
> geometry, full rank of the selected derivative matrix, and positive
> aggregate transverse/axial cut identities imply that no finite move
> inside the original empty direction cell can strictly improve diameter.

An actual-source proof must use more than those data. Full vertex KKT
equilibrium and the canonical contact-train embedding remain available
inputs for a repaired lemma; this regression does not refute that lemma.

## 5. Verification, dependencies, and remaining attack

Run `python3 research/verify_exact_phase_gap_finite_barrier.py`. Its second
part certifies the complete source family and finite competitor on the
real ray `D>=13`. It omits global optimality, full-source positive KKT/PSD,
and the canonical stopped-train embedding.

Construction and arithmetic are new and self-contained. The connection
to the canonical source uses only its normalization and `C-ZRF` scope
as a boundary on what may be concluded, not as a premise of the family.

Exact next obligation: exploit full-source vertex equilibrium or the
actual complete-grid/train embedding to forbid the kind of finite escape
that is possible above. A graph-only circulation theorem or a check of
only old active diameters does not supply it.

Registered in audit.60 as a regression rather than a candidate C-II source. Fixed-star, split-star, inactive-interface, and macroscopic-container branches remain open.
