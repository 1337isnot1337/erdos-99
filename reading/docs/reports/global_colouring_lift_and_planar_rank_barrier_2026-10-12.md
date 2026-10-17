> Generated reading edition · [exact source](../../../docs/reports/global_colouring_lift_and_planar_rank_barrier_2026-10-12.md) · source SHA-256 `ab1fc0f0d2cdd3b1f72b801a7b873d56f5db6bed68bfd231f29d88b5945538bc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4DE55BC9FA0D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — global colour lift and the planar rank barrier

**Date:** 2026-10-12
**Repository commit:** ab6dd3336f9f8d440f2bada76edb32153391cddc
**State version:** 2026-10-10.audit.234
**Run type:** closing-proof research / exact regression
**Target:** Level I, independent whole-source route
**Starting status:** Level I open; no unpromoted premise
**Active prompt:** `docs/prompts/erdos_problem_99_GPT6_ASTRA_FULL_SOLUTION_PROMPT.md`
**External literature:** Eppstein's original paper rechecked
**Computation:** `research/verify_global_colouring_lift_rank_2026_10_12.py`

## LEVEL I STATUS

**STILL OPEN.** New mathematical claims are **unreviewed candidates**. The
dimension-free closure is a **regression / rejected attempt**. No promotion.

## 1. Global endpoint and diverse approaches

The endpoint is a planar unit-separated set of all n source labels, of diameter
strictly less than D(n). An intervening path need not stay feasible: global
optimality prohibits the endpoint itself.

| Mechanism | Exact proposed bridge | Obstruction |
| --- | --- | --- |
| Distance-matrix interpolation | Improve all actual diameters and preserve every contact | Embedding rank increases; proved below |
| Proper-colour lift | Every triangle-free source has strict descent in dimension four | Planar realization fails in general |
| Finite colour translations and contraction | Satisfy every endpoint pair polynomial at one common parameter | Inactive lower constraints and same-colour clearance must also be paid |
| Unlabelled packing replacement | Retain at least n sites of diameter strictly below D | Density alone gives neither exact count nor attainment |
| Triangle-clearance plateau exclusion | Exclude all positive-clearance optimizers at D(n) | A rate tending to zero does not exclude every positive plateau |

Only the first three are developed here. No conditional chart, scaffold or
carrier is identified with the source. All contact-isolated labels are retained.

```text
proper-colour lift -> full-source strict metric improvement
-> planar realization -> contradiction to D(n).
```

The planar realization arrow fails. Omitting it would falsely resolve the unit
square regression, which is a four-point global minimizer.

## 2. Universal squared-distance descent and its exact rank jump

For any finite unit-separated source with diameter D>1 and 0<lambda<1 define

```math
d_{ij}'{}^2=1+\lambda(d_{ij}^2-1)\quad(i\ne j).
```

Every unit contact remains unit, every noncontact stays strictly above one, and
D'^2=1+lambda(D^2-1)<D^2. These distances are Euclidean: take orthogonal sums of
sqrt(lambda) times the source and sqrt(1-lambda) times a regular unit simplex.

For a planar source P, put J=I-11^T/n and G=JPP^TJ. The new centred Gram matrix is

```math
G'=\lambda G+\frac{1-\lambda}{2}J.
```

For every nonzero x perpendicular to 1,

```math
x^TG'x=\lambda|P^Tx|^2+\frac{1-\lambda}{2}|x|^2>0.
```

Thus rank(G')=n-1 exactly. For n>=4 there is no planar realization. This
obstructs this relaxation, not every possible planar competitor. For n=3 the
construction really is planar, excluding triangle-free three-point sources of
diameter greater than one as global minimizers.

The rank-free Euclidean-distance optimization has optimum one for every n,
realized by a regular unit simplex. Any successful planar comparison must
therefore exploit a planar restriction beyond the distance inequalities alone.

## 3. Four-dimensional strict descent for every triangle-free source

Take any proper q-colouring c of the full contact graph. Let z_c be the vertices
of a regular unit (q-1)-simplex and set

```math
p_i(t)=\frac{(p_i,tz_{c(i)})}{\sqrt{1+t^2}}.
```

For different colours the new squared distance is (d_ij^2+t^2)/(1+t^2); for
equal colours it is d_ij^2/(1+t^2). Define

```math
\delta_c=\min_{i\ne j,\ c(i)=c(j)}(d_{ij}^2-1),
```

with infinity for an empty minimum. Finiteness and proper colouring give
delta_c>0. For 0<t^2<delta_c all lower constraints hold and the complete contact
graph is preserved. Every old actual diameter pair strictly shortens, and

```math
\operatorname{diam}P(t)^2\le\frac{D^2+t^2}{1+t^2}<D^2.
```

All inactive upper constraints are checked by the same formula. This is a
simultaneous full-source improvement, not a stress-weighted average.

The canonical baseline `docs/problem/literature_baseline.md` §2.4 records
Eppstein's Theorem 1: triangle-free penny graphs are 2-degenerate. Reverse
greedy colouring gives q<=3, including isolates. The source contact graph is a
penny graph using radius-1/2 disks, so the lift uses at most four dimensions.
The source was rechecked in [Eppstein's original journal paper](https://www.maths.tcd.ie/EMIS/journals/JGAA/accepted/2018/463.pdf),
Section 2, Theorem 1. Only degeneracy is imported, with its stated normalization.
No geometric flexibility or near-quadrangulation claim is inferred from it.

## 4. Exact criterion for isometric planar flattening

Write P_0=JP and Z_0=JZ. For t>0 the lifted affine dimension is
rank[P_0 Z_0]. If P is noncollinear, that rank is at most two exactly when
every column of Z_0 is in the column space of P_0. Equivalently an affine map
of the source plane sends each p_i to its assigned colour vertex.

For two nonempty colours, this is exactly the condition that the two colour
classes lie on two parallel lines. Then the lift actually has a planar
realization and supplies a strict competitor. The condition concerns every
source point, including isolates.

For three nonempty colours Z_0 has rank two. If its columns are in the column
space of P_0, the corresponding linear part is invertible, since P_0 also has
rank two. Each of its three colour values then has only one preimage. Hence
n<=3. With all three colours used, no source with n>=4 can be flattened this
way. This does not prohibit a different planar rearrangement.

The bipartite unit square has lift rank three. A rectangle whose only contacts
are its two horizontal unit edges can be coloured by its vertical columns;
its lift has rank two and contracts the other direction. Both conclusions are
checked exactly, distinguishing metric descent from planar descent.

## 5. Full-source planar endpoint checker without a local-path premise

For arbitrary planar v_i and t>0 propose y_i=(p_i+t v_i)/sqrt(1+t^2). For each
pair put u=p_i-p_j, w=v_i-v_j, d^2=|u|^2, b=u.w and c=|w|^2. The exact lower
constraint and strict upper constraint are respectively

```math
(d^2-1)+2bt+(c-1)t^2\ge0,
```

```math
(D^2-d^2)-2bt+(D^2-c)t^2>0.
```

One common endpoint t must satisfy both for every pair. No first-order sign or
feasible-path premise is imposed. Assigning one target per colour leaves
same-colour differences unchanged before normalization, requiring t^2<=delta_c;
proper colouring alone does not resolve the other simultaneous quadratics.

The script accepts JSON with rational `source`, `target` and `t`. It checks all
exact endpoint distances. A deliberately nonlocal two-label swap crosses a
collision at t=2/3 but gives a valid strict competitor at t=1; this verifies
endpoint-only semantics. It is not Level I evidence. A square contraction is
rejected even though its diameter decreases, since its lower bounds fail.

## 6. Verification, classification and remaining obligation

```sh
python3 research/verify_global_colouring_lift_rank_2026_10_12.py
```

Rational arithmetic and exact SymPy ranks check four complete-source lift
fixtures, four uniform Gram interpolations, the two different lift ranks, a
genuine planar flattening, endpoint-only semantics, and rejection of an
infeasible square contraction. No global source optimality is certified.

| Claim | Classification | Limit |
| --- | --- | --- |
| Universal metric descent and rank n-1 | Unreviewed candidate | Usually requires more than two dimensions |
| Every triangle-free source descends contact-preservingly in R^4 | Unreviewed candidate | Planar realization absent |
| Affine-colour flattening criterion | Unreviewed candidate | Does not extract affine colours |
| Dimension-free closure by lifting | Regression / rejected attempt | Unit square has rank-three lift |
| Full-pair planar endpoint criterion | Unreviewed candidate | Certifies supplied endpoints only |

No canonical frontier changes. The unresolved global theorem must construct an
actual planar endpoint for every sufficiently large triangle-free *global*
minimizer, retaining all n labels and all pair bounds. Isometric projection of
this lift cannot supply it in general. Density improvement and lifted endpoints
do not replace that obligation.

## Autonomous audit (2026-10-15)

The [PR958 AI audit](../audits/pr958_autonomous_proof_audit_2026-10-15.md)
records the complete proof and certificate review, scope, source provenance and
JSON proof replay. All checkers require assertions and refuse optimized Python.
The reports remain noncanonical and unreviewed. The source AI audit is provenance,
not a destination exact-head review; no canonical claim is promoted.
