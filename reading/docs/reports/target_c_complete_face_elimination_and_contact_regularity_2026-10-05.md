> Generated reading edition · [exact source](../../../docs/reports/target_c_complete_face_elimination_and_contact_regularity_2026-10-05.md) · source SHA-256 `82a2fb5244b6760f2ba4860ffd2fa861e6a6a187030eaaeda45768a655c311bb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FE92EE7D1B20","canonical":true,"claim_ids":["C-CONTACT-FACE-REGULARITY"],"claim_statuses":{"C-CONTACT-FACE-REGULARITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — complete exceptional-face elimination and regularity of every contact constraint

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Run checkpoint:** f3959b83. **State:** 2026-09-14.audit.51.
**Classification:** canonical in `2026-10-05.audit.52` as `C-CONTACT-FACE-REGULARITY`
after independent promotion audit. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Universal source theorem and exact frontier change

Let $`A`$ be any canonical triangle-free C-II source in the Section-57
mixed-rigidity regime, with full $`C=C_*`$, $`H=H_*`$. Let $`V`$ be
its connected nonisolated positive-contact core, $`v=|V|`$, $`e=|C|`$,
$`f`$ the bounded nonquadrilateral contact-face count, and $`T`$ the
complete stopped-train count. Then

```math
\boxed{\operatorname{rank}C_{\rm face}=2f,
\qquad \operatorname{rank}R_C=e,
\qquad \sigma_C=0.}
\tag{E.1}
```

Every physical exceptional face admits a complete two-anchor elimination
order. There is no stalled bounded-face core of any size or degree.
No residual, phase, degree-tail, all-pentagon, disk-limit or terminal
hypothesis is imposed.

The exact unit-contact realization space near the source is a smooth
manifold of dimension $`q-k+2`$, including two translations and rotation.
After fixing a core translation, a complete train chart has dimension
$`q-k`$; modulo core Euclidean motions it has dimension $`q-k-1`$.
Every original source point, including each contact isolate, is retained.

This strengthens the preceding
[pentagon elimination candidate](target_c_all_pentagon_closure_core_elimination_2026-10-05.md).
Higher-degree faces cannot carry its former remaining pure-corank
alternative. The $`s_C`$ in the full-core surplus is the distinct
pinned-component slack; (E.1) supplies no upper bound on $`s_C`$.
The all-phase scalar survivor therefore remains compatible.

## 2. Actual positive-contact faces are strictly convex

Use canonical
[Section 67](../targets/target-c/67-rhombus-population-transport-audit.md):
loaded core vertices are exactly the force-hull vertices, every unloaded
core vertex is strictly inside that hull and has contact degree at least
three, and bounded augmented faces are convex simple polygons. All
actual core contact forces are positive.

A bounded-face sector at a loaded vertex is inside its strictly convex
hull tangent cone, so its angle is less than $`\pi`$. Suppose a sector
at an unloaded vertex had angle $`\pi`$. Every incident contact ray
is in the complementary closed half-plane. Projection of the positive
equilibrium equation on its normal forces **every** contact ray onto the
boundary line. Unit length and distinct source points permit at most
the two opposite neighbors on that line, contradicting degree at least
three. Thus these face angles are also less than $`\pi`$.

Every bounded physical contact face is therefore strictly convex. This
strengthens the ordinary convexity needed for Oler in Section 67 without
changing its proof or treating an auxiliary hull side as a contact.

In a strictly convex polygon, one projective side direction occurs at
most twice: once with each orientation. For a triangle-free physical
unit pentagon it occurs at most once, by the exact
[no-parallel-side argument](../../research/target_c_bounded_pentagon_no_parallel_sides_2026-09-18.md)
rechecked in the preceding report. All exceptional face degrees are at
least five; triangle faces are excluded and quadrilaterals are rhombi.

## 3. Internal train sparsity forbids every stalled core

The canonical audit.52
[AR.2](target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md)
gives independent angular columns for all trains whose endpoints are
bounded augmented faces. Its proof integrates contact edge velocities,
sets every auxiliary hull vector and every outside-ended train rate to
zero, fixes all loaded velocities and invokes canonical mixed rigidity.
It retains every pocket, including nonunit-chord four-sided pockets.

Restrict to any nonempty set $`U`$ of physical exceptional faces. The
two coordinate-sum row dependencies give

```math
e(U)\le2|U|-2.
\tag{E.2}
```

There are no internal loops. Hence some $`F\in U`$ has internal
train degree at most three. Its external terminal count is at least
$`\deg F-3`$.

- If $`\deg F=5`$, at least two external trains are present and their
  directions are nonparallel.
- If $`\deg F\ge6`$, at least three external trains are present. Since
  one projective direction has at most two physical side occurrences,
  two of these trains are nonparallel.

Activate $`F`$ using those two external trains and remove it from
$`U`$. The other endpoint is the actual outer face or a face activated
earlier. Continue. This constructs a complete order for all exceptional
faces, including arbitrarily high-degree faces. Terminal occurrences
determine the incidence degree, with repeated boundary vertices retained.

## 4. Full row rank and zero pure-contact corank

Select the two external train columns when each face enters the order.
A pivot train cannot be selected twice: at its earlier endpoint, its
later endpoint was still inactive and the train was not external.
The full face-row/pivot-column matrix is block upper triangular, with
diagonal blocks $`[Jw_1\ Jw_2]`$ of nonzero determinant. Thus
$`C_{\rm face}`$ has rank $`2f`$.

Train-angle integration on the actual contact graph gives
$`\ker R_C/\mathrm{Trans}\cong\ker C_{\rm face}`$. Euler and
$`T=e-2R`$, where $`R`$ is the strict-rhombus count, then give

```math
e-\operatorname{rank}R_C
=2f-\operatorname{rank}C_{\rm face}=0.
```

This checks the identity of the audited-working
[Section 156](../targets/target-c/156-157-face-closure-and-outer-train-bracing-audited.md)
at its exact core scope. Contact isolates enter neither side of this
matrix identity and have not been removed from the source.

Equivalently, if a full transpose-kernel vector were nonzero, its
nonzero support would have a face with two nonparallel train ends to
zero blocks. Their equations would force that face block to be zero.
Thus no pure closure mode can have any bounded support size. Earlier
finite signed reciprocal classifications remain valid at their formal
algebraic scopes; their nonzero canonical closure-mode antecedent is
excluded by (E.1), conditional on this new candidate's audit.

## 5. Complete finite contact chart

For each bounded physical exceptional face, impose the exact rotated
unit-edge closure

```math
\Psi_F(\theta)=\sum_{e\in\partial F}
\operatorname{Rot}(\theta_{\tau(e)})w_e=0.
```

Opposite sides of each original rhombus cancel identically. The pivot
Jacobian of all remaining equations is invertible by Section 4. The
implicit function theorem supplies a smooth exact train chart with
$`T-2f=q-k`$ free angles. Integrating the closed edge vectors gives
every nearby core realization up to translation. Alternatively, full
row rank of the actual contact constraints directly gives dimension
$`2v-e=q-k+2`$ in position coordinates.

All selected and unselected original contacts remain exactly unit.
Contact isolates are held at their original positions. Every initially
strict lower constraint and inactive upper constraint has positive
finite slack, so all persist in a sufficiently small neighborhood.
Cardinality is unchanged. Active diameter feasibility remains a
separate condition on that chart.

The radius can depend on the source, pivot determinants and all pair
slacks. It is not uniform along an asymptotic sequence. Full contact
integrability cannot be transferred into a common diameter-descent
direction: canonical mixed rigidity and positive KKT stationarity
already exclude such a non-Euclidean first-order direction.

Current main advanced during this run to `b9bf98d8` through provenance
salvage; all canonical state/frontier surfaces remained unchanged. Its
recovered universal **outer-supported** manifold was read and checked
against this argument. That report rotates only private outer train
blocks. The present chart reaches the entire contact tangent space;
the proof above does not import a salvage artifact as a premise.

## 6. Exact finite square energy on the complete chart

Let $`\Omega=L_C^\alpha-L_H^\beta`$ be a normalized relative-interior
canonical stress on the nonisolated core, with
$`\sum_H\beta_h=1`$, $`\sum_C\alpha_e=D^2`$, $`\Omega p=0`$ and
$`\Omega\ge0`$. For **any** labelled realization $`p'`$ preserving
all original contact lengths, put $`\delta=p'-p`$. The exact identity is

```math
\boxed{\sum_{h\in H}\beta_h|p'_i-p'_j|^2
=D^2-\sum_{c=1}^2\delta_c^T\Omega\delta_c.}
\tag{E.3}
```

This follows by expanding the stress quadratic form, using equilibrium
to cancel the cross term, and using the preserved contact lengths.
It is the canonical stress-energy identity applied to the complete
chart, not a new generic-PSD claim.

If the original contacts use at least three projective directions,
equality in (E.3) forces the target **core** to be congruent to the
original core. Indeed Section-57 affine-kernel rigidity makes equality
an affine map; preserving three distinct unit directions makes its
linear Gram matrix the identity. The statement concerns the core,
without extending that kernel to isolated coordinates.

For a chart path with core tangent $`u`$, differentiation gives
$`\sum_h\beta_h(|p_i(t)-p_j(t)|^2)''_{t=0}
=-2\sum_cu_c^T\Omega u_c`$. Weighted second-order contraction is
therefore explicit. It still is not contraction of every pair.

Two exact five-point regressions keep that boundary visible. For the
unit regular pentagon, $`D^2=(3+\sqrt5)/2`$, $`\beta_h=1/5`$:

1. A triangular trapezoid preserving all five old cycle contacts is
   unit-separated and has weighted old-diameter mean $`12/5<D^2`$,
   but its maximum squared distance is $`4>D^2`$.
2. A three-colour triangle collapse preserves all five old cycle bars
   and has every pair at distance at most one, with weighted mean
   $`3/5<D^2`$, but two labelled vertex pairs coincide. It is a
   three-point set and fails both lower separation and cardinality.

Thus a source replacement must check the full maximum and every lower
constraint, even when (E.3) is strict.

## 7. Hostile checks and exact verifier

[The verifier](../../../research/verify_target_c_complete_face_closure_elimination_2026_10_05.py)
checks 84 glued-pentagon and 4,734 positive-equilibrium hexagon-packet
source pairs, their full face/contact ranks, 31,549 abstract
$`(2,2)`$-sparse endpoint graphs and 94,647 mixed-valence elimination
orders. Its pins are not actual diameter loads and its abstract graphs
need not be embedded sources. It certifies the finite contracts, not
the analytic implicit-function theorem or a uniform radius.

A genuine unit-separated seven-point triangular wheel supplies actual
positive normalized KKT loads and pure contact corank one. All 21
source-pair constraints and the signed contact self-stress are checked.
Its bounded triangular faces fall outside the proof: the triangle-free
hypothesis cannot be dropped. Global optimality is not a premise of
this regression. Twenty target-pair checks certify both failures after
the exact finite square-energy comparison above.

Bridge and repeated outer-walk occurrences remain in the original
train ledger. Every added pocket remains in the AR.2 proof. No active
diameter, inactive upper pair or contact isolate is discarded from a
claimed source deformation. The new chart eliminates the contact
singularity/stalled-core escape; finite diameter descent and collective
repacking remain unproved.
