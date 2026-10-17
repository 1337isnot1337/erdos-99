> Generated reading edition · [exact source](../../../docs/audits/target_c_section106_full_geometric_hostile_audit_2026-09-12.md) · source SHA-256 `1db8706809fc6836f1ebac35487fb215232ebb61a0197653bbc795b033c98087`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-137EDD228F25","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 106 full geometric hostile audit

**Date:** 2026-09-12  
**Verdict:** **PASS as a proof-only theorem.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit extends the narrower arithmetic audit of
`docs/targets/target-c/106-strong-phase-shore-quantitative-gap-audit.md`.
It checks the inherited geometric steps that the first Section-106 audit deliberately
left out: the enlarged stability window, countable route exhaustion, train-end
provenance, macro/micro leakage decomposition, tangent-window counting, and the final
projective-direction contradiction.

The conclusion is that Section 106 is mathematically sound at proof-only scope.  Its
explicit coefficient

$$
\mu_{11}=0.9760410429297387484\ldots
$$

is a valid carrier-diameter lower bound in the full-core Type-II branch, conditional on
the canonical Section-103 common-cap contradiction and the independently audited
Section-104 technical lemmas.  It does not close C-II.

## 1. The Section-103 constants apply on the whole Section-106 window

Section 106 assumes

$$
0\le \sigma(\theta)\le1.2\times10^{-5}.
$$

Canonical Section 103 records the explicit fixed neighborhood

$$
\theta\le\theta_8+0.03
$$

on which the unique wrapping carrier has area greater than `0.1905D^2` and one may use

$$
R_D\ge0.18D^2,
\qquad T_D\le6D,
\qquad \sum_R\delta_R<5.317D.
$$

Since Section 106 has

$$
\theta-\theta_8\le{4\over15}\sigma<3.2\times10^{-6},
$$

its entire contradiction window lies more than four orders of magnitude inside the
certified Section-103 neighborhood.  There is no continuity-modulus gap here.

## 2. The Section-104 complement-gap stability remains valid

The Section-104 proofs of

$$
0\le\delta\le{10\over3}\sigma,
\qquad
0\le x_2,x_3,\tau\le{13\over3}\sigma
$$

use only three fixed smallness barriers after the scalar chain is established:

1. the coarse `delta=0.1` concavity cost is greater than `0.0326`;
2. the transfer derivative is uniformly greater than `0.30` on `0<=delta<=0.1`;
3. the adjacent-span argument needs `tau<phi`.

At `sigma=1.2e-5`, the right sides above are below `4e-5` and `5.2e-5`, while
`phi` is about `0.877`.  All three barriers therefore retain large strict slack.
The projective principal-corridor perturbation bound with coefficient `73/6` is also
valid on the enlarged window.

The main support region used by the tangent-window lemma remains contained in an
oriented angular interval of length strictly below `pi`; the enlargement from
Section 104 is microscopic compared with the fixed endpoint margin.  Thus the
orientation lift used by the technical companion does not fail at the new cutoff.

## 3. The all-macroscopic-route excess sharpening is legitimate

For any fixed finite family `J` of positive complement gaps, select the corresponding
finite consecutive-attachment intervals.  The Section-82 exact outer-walk identity and
the ordinary two-edge floor on every unselected interval give

$$
\sum_{j\in J}\ell_j\le2\alpha.
$$

The selected routes are distinct outer-walk subchains.  The potentially linear
loaded-loaded contact correction has favorable sign because
`c^partial<=c`; the fixed cardinality of `J` contributes only `o(D)` after
normalization.

Enumerate the positive complement components.  A diagonal subsequence gives the
normalized route lengths for every fixed component.  Since every route length is
nonnegative, monotone exhaustion yields

$$
\sum_{j\ge1}\ell_j\le2\alpha.
$$

Canonical Section 101 gives

$$
C:=\sum_j\sin(g_j/2)\le2\alpha,
\qquad 2\alpha-C\le\sigma.
$$

Every route dominates its endpoint chord, so subtraction is termwise nonnegative and
therefore

$$
\boxed{
\sum_j\bigl(\ell_j-\sin(g_j/2)\bigr)
\le2\alpha-C\le\sigma.
}
$$

In particular the three principal routes have total normalized path excess at most
`sigma`.  The countable limiting order is therefore sound; Section 106 is not
silently interchanging a growing finite gap family with the scale limit.

## 4. The stronger Section-90 shore extraction is valid

From `R_D>=0.18D^2`, the phase-circle cut deletes only `O(D)` crossings, so for all
sufficiently large `D` at least `0.179D^2` remain.  With `K=1000`, the global defect
bound removes at most

$$
{5.317D\over1000/D}=0.005317D^2
$$

nongood crossings.  Thus at least `0.173683D^2` good crossings remain, and one of the
three unordered phase-label pairs supports at least `0.173683D^2/3`.

Bins of width `20K/D` retain at least `19/20` of those crossings for one shift, hence
more than

$$
0.0549996D^2
$$

internal-bin crossings.

Let `a_j,b_j` be the two shore sizes in a bin.  Simplicity of the train-crossing graph
gives `e_j<=a_jb_j`, and the total local-train bound gives

$$
\sum_j a_j\le6D,
\qquad
\sum_j b_j\le6D.
$$

If every bin were small on at least one shore at threshold `0.0045D`, then the bins
small on the first shore would carry at most `0.027D^2` edges and the remaining bins,
which must be small on the second shore, at most another `0.027D^2`.  This contradicts
the retained `0.0549996D^2` mass.

Therefore one common reduced-phase bin contains both shores of size at least
`0.0045D`.  Its width `20000/D` tends to zero, so the two fixed phase labels have
limiting projective directions exactly `pi/3` apart.

## 5. The endpoint supply uses the correct physical object

A local rhombus train is a chain through opposite rhombus edges.  Its fixed projective
train direction is the direction of those transverse edges.  The two ends of a full
local train segment are physical strict-rhombus boundary edges in that same direction.
Thus the phase direction used in Sections 68/90 is the direction of the endpoint edge
used later in the corridor projection identity; there is no hidden `pi/2` rotation.

Canonical Section 89 gives exactly two physical boundary ends per local train,
including hole boundaries.  A physical rhombus-boundary edge terminates only the train
using its edge direction.  Hence a shore of `0.0045D` distinct local trains supplies
`0.009D` distinct endpoint occurrences.

The Section-82/89 boundary classification is exhaustive for those occurrences:
terminal edges lie either on the outer-face walk or against bounded
nonquadrilateral-face boundary.  Section 106 inherits the Section-104 `5Q` budget for
the latter, so no hole/interface endpoint category is omitted.

## 6. The Section-104 leakage formula remains valid at the optimized cutoff

For one selected phase family, the inherited leakage terms are:

- nonquadrilateral bounded-face boundary: `5 sigma`;
- nonprincipal macroscopic outer routes: `19 sigma / 6`;
- exceptional micro routes: `9 sigma`;
- teeth in the two tiny spans adjacent to the principal gap: `20 sigma / 3`;
- tail-chord contribution in the two tangent windows: `13 sigma / 3`;
- bad-base teeth: `sigma/h`;
- good-base tangent-window capacity: `w(h)`.

The fixed coefficients sum to

$$
5+{19\over6}+9+{20\over3}+{13\over3}={169\over6},
$$

so

$$
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma
$$

is the correct occurrence-density bound.

The macro/micro split is interpreted in the audited Section-104 order

```text
fix epsilon > 0 -> D -> infinity -> epsilon -> 0,
```

so no growing finite gap family is classified before the scale limit.

For good unloaded-apex two-edge teeth, a base `b in [1,1+h]` makes either leg an angle
`beta(b)=arccos(b/2)` from the base.  Splitting by the two leg choices gives two
oriented base-direction windows, each of width at most

$$
w(h)=\pi/3-\arccos((1+h)/2).
$$

The Section-104 convex tangent-window lemma bounds each class by boundary length, and
unit separation converts that length bound to a base-count bound.  Counting both
classes separately is correct even if one tooth contributed both legs: two endpoint
occurrences should then be counted twice.

At `h=0.00455` and `sigma=1.2e-5` the published leakage is below `0.005605`, leaving
more than `0.003395D` endpoints on the three principal corridors and hence more than
`0.001131D` on one of them.  The choice `rho=0.00113` is safe.

## 7. The projection argument has no orientation or multiplicity defect

Take a principal route with chord projective direction `q` and at least `rho D`
selected endpoint edges from one phase family with limiting projective direction `u`.
Orient the route from one chord endpoint to the other.  For each unit route edge `z`,
its undirected direction is `u+o(1)`.  If its route orientation agrees with `q`, its
projection is at most `cos Delta+o(1)`; if it points the opposite way, the projection
is smaller and the loss is larger.  Therefore every selected occurrence contributes
at least

$$
1-\cos\Delta-o(1),
\qquad
\Delta=\operatorname{dist}_{RP^1}(u,q).
$$

to the exact identity

$$
\sum_e(1-q\cdot z_e)=\operatorname{len}(\text{route})-
\operatorname{len}(\text{chord}).
$$

Distinct selected trains give distinct physical endpoint occurrences, so these losses
may be summed without overcounting.  The principal-route excess bound then gives

$$
\rho(1-\cos\Delta)\le\sigma.
$$

At the Section-106 endpoint this yields `Delta<0.145866`.  The two phase families
cannot select the same principal corridor because their limiting directions are
`pi/3` apart while `2Delta<pi/3`.

If they select distinct corridors, the reverse triangle inequality in the projective
circle metric gives

$$
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-\pi/3
\right|
<2\Delta<0.291732.
$$

The complement-gap stability gives the incompatible lower bound `>0.3041104` for every
principal-corridor pair.  The final contradiction therefore has genuine positive
angular margin.

## 8. Disposition

Section 106 survives a full geometric hostile audit.  The valid proof-only consequence
is:

$$
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760410429297387484\ldots-o(1))D
}
$$

for some quadratic-area locally rhombus-saturated harmonic carrier in every sufficiently
large Type-II survivor.

This is still only a carrier theorem.  It does not force an exact unit equilateral
triangle, does not construct a source-preserving strict sub-`D` competitor, and does
not settle the separate container branch.  C-II and LEVEL I remain open.

**Theorem state:** unchanged; this audit does not promote Section 106.