<!-- theorem-state: {"artifact_id":"ART-F0869713BA20","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fullcore_detour_shear_regression_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=14719348d4e3de5f84061c15f27d99300a5d241e; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-core detour and vanishing-shear regression

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / adversarial regression
**Target:** C-II / Level I
**Starting status:** canonical Sections 122–123, with the macroscopic-container branch still open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used
**Computation:** `python3 research/nearchain_vertex_regressions.py`

## LEVEL I STATUS

`STILL OPEN`

This report does not claim a global minimizer, a disproof sequence, or a Level I
closure. The new finite family is an exact regression against density-only,
uniform-angle-gap, and local-first-order-jamming closures.

## 1. Starting canonical endpoint

The selected route was the full-core C-II branch. The live implication chain was:

```text
new upper bound on Σᵣ (Lᵣ − 2dᵣ)
    -> combine with the canonical Section-122 detour floor
       and Section-123 payment of Σᵣ P_exc,ᵣ
    -> source-level contradiction, strict sub-D competitor, or exact unit triangle
    -> Level I
```

The canonical inputs are:

```text
liminf (1/D) Σᵣ (Lᵣ + P_exc,ᵣ − 2dᵣ) ≥ (π/2)(2 − √3)

Σᵣ P_exc,ᵣ ≤ 10(e_BB − k),       k = d_H + s_Z.
```

These are respectively `C-AGGREGATE-TWO-ARC-DETOUR` and
`C-AUGMENTED-CELL-DEFECT-BUDGET`. Both retain occurrence-counted outer walks and
contact-isolated source points. Neither supplies an upper bound on the residual
outer-walk detour

```text
T_out := Σᵣ (Lᵣ − 2dᵣ).
```

## 2. Strongest genuinely new result

**Classification:** regression / unreviewed candidate

### Statement — vanishing-shear finite triangle-free near-density family

There is a sequence of finite unit-separated sets `A_R ⊂ ℝ²`, with `R → ∞`, such
that:

1. `A_R` contains no unit equilateral triangle;
2. its unit-contact graph is bipartite and every contact edge belongs to one of two
   unit lattice directions;
3. if `D_R = diam(A_R)`, then `D_R = 2R + O(1)`;
4. with `Δ₂ = π/(2√3)`, `|A_R| = Δ₂ D_R² + O(D_R)`;
5. all lattice rhombi have angles `π/3 + R⁻²` and `2π/3 − R⁻²`, so their
   strictness from the equilateral endpoint is only `O(R⁻²)`.

Consequently, no theorem whose only quantitative inputs are unit separation,
triangle-freeness, near-disk diameter geometry, and first-order local lattice
contact structure can supply either a fixed positive loss in `n/D²` or a uniform
positive rhombus-angle gap. A
global-minimality or source-preserving second-order comparison is essential for
such a closure.

The last consequence is a regression about the proposed bridge, not a statement
about global minimizers: the family is not asserted to minimize diameter for its
cardinality.

### Scope

The family consists of arbitrary feasible finite packings. It is not a canonical
C-II source, does not carry a finite global KKT stress on its boundary, and does
not include contact-isolated points because it has no separate inactive cloud. Each
lattice point whose four lattice neighbors remain in `A_R` has the standard
positive local equilibrium from those four contact directions. The construction is
relevant to density,
near-rhombic, and local-jamming arguments, but it is not a global-optimality
certificate and cannot settle Level I in either direction.

### Proof

For `R > 10`, set

```text
ε_R = R⁻²,
θ_R = π/3 + ε_R,
u = (1, 0),
v = (cos θ_R, sin θ_R),
Λ_R = { i u + j v : i, j ∈ ℤ },
A_R = Λ_R ∩ B(0, R).
```

For large `R`, `0 < cos θ_R < 1/2`. Every nonzero lattice difference
`z = i u + j v` satisfies

```text
|z|² = i² + j² + 2ij cos θ_R.
```

If `ij ≥ 0`, either one coefficient is zero, giving `|z| ≥ 1`, or the squared
length is strictly larger than one. If `ij < 0`, write `a = |i|` and `b = |j|`:

```text
|z|² = (a − b)² + 2ab(1 − cos θ_R).
```

For `a = b = 1`, this is `2(1 − cos θ_R) > 1`; for `a ≠ b`, the first term
is at least one and the second is positive. Thus every pair of distinct points of
`A_R` is at distance at least one. Equality occurs only for differences `±u` and
`±v`.

The contact graph is therefore the induced graph of lattice edges in those four
directions. Coloring `iu + jv` by the parity of `i + j` makes every contact edge
bichromatic. The contact graph is bipartite and hence contains no triangle, in
particular no unit equilateral triangle.

For the counting estimate, let

```text
Q_R = { s u + t v : 0 ≤ s,t < 1 }.
```

The translates `λ + Q_R`, `λ ∈ Λ_R`, tile the plane,
`area(Q_R) = sin θ_R`, and every point of `Q_R` has norm at most two. Every point
of `B(0,R−2)` belongs to a tile based at a lattice point of `B(0,R)`. Conversely,
every tile based at a point of `A_R` lies in `B(0,R+2)`. Hence

```text
π(R−2)² / sin θ_R ≤ |A_R| ≤ π(R+2)² / sin θ_R.       (SR.1)
```

The same tiling gives points of `A_R` within distance two of each of
`(R−2)e` and `−(R−2)e`, for every unit vector `e`. Therefore

```text
2R − 8 ≤ D_R ≤ 2R.                                  (SR.2)
```

It also gives `h_conv(A_R)(e) ≥ R−4` and `h_conv(A_R)(e) ≤ R` for every unit
vector `e`. Thus the source hull contains `B(0,R−4)` and is contained in
`B(0,R)`; this is a bounded-Hausdorff-error near-disk family.

Since `sin θ_R = √3/2 + O(R⁻²)`, (SR.1) and (SR.2) give

```text
|A_R| = [π/(4 sin θ_R)] D_R² + O(D_R)
      = [π/(2√3)] D_R² + O(D_R).
```

The four-point lattice parallelograms with sides `u,v` are unit rhombi. Their
angles are `θ_R` and `π−θ_R`, so the angular gap from the equilateral endpoint is
exactly `R⁻²`.

### What the proof does and does not use

The proof is finite and elementary. It uses no limiting compactness, numerical
optimization, or unproved lattice-point estimate. It does not use global diameter
optimality, so it cannot be promoted to a Level I disproof. It also does not claim
that the finite boundary is a KKT equilibrium; only the infinite/interior lattice
contact pattern has the usual positive four-direction equilibrium.

## 3. Exact frontier effect

The result does not change canonical theorem state. It rejects the following
bridges without additional hypotheses:

```text
triangle-free + near-disk + asymptotically optimal density
    -> uniform angle gap or fixed density deficit

near-rhombic local contact pattern + first-order equilibrium
    -> quantitative source-level loss sufficient for Sections 122–123
```

It does not pay `e_BB − k` and does not create a strict same-cardinality sub-`D`
competitor for a global minimizer. The canonical full-core residual remains the
aggregate outer-walk detour coupled to the loaded diameter ledger.

The macroscopic-container branch remains completely uncovered by this regression.

## 4. Exact remaining lemma

One precise full-core target remains:

> **Source-level detour/deformation theorem.** For every sufficiently large
> triangle-free global minimizer in the Type-II full-core branch, either
> `Σᵣ(Lᵣ−2dᵣ)` satisfies an upper bound strong enough to contradict Sections
> 122–123 after the exact `10(e_BB−k)` payment, or the actual source admits an
> explicitly constructed same-cardinality unit-separated deformation with diameter
> strictly below `D(n)`, or the loaded/core geometry contains a unit equilateral
> triangle.

This statement is deliberately source-level. An upper bound on an abstract
scaffold, a selected carrier, or a local response model is insufficient.

The complete Level I endpoint also requires a theorem excluding the Type-I
macroscopic inactive chamber/exterior-cap branch.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Sections 122–123 canonical detour/payment statements | canonical | `C-AGGREGATE-TWO-ARC-DETOUR`, `C-AUGMENTED-CELL-DEFECT-BUDGET` | Exact hypotheses retained; occurrence and source conventions respected |
| Vanishing-shear finite family (SR.1–SR.2) | regression / unreviewed candidate | elementary lattice geometry | Complete finite proof above; no global-optimality claim |
| Triangle-free families must lose a fixed density fraction | rejected by regression | vanishing-shear family | Cell-area loss is `O(R⁻²)`, with only boundary-order counting error |
| Positive local equilibrium forces a uniform angle gap | rejected as stated | four-direction lattice equilibrium; existing degree-five regression | Boundary/global stress hypotheses are missing |
| Sections 122–123 alone close C-II | rejected as unsupported | canonical Sections 122–123 | They leave `T_out` and the macroscopic-container branch |
| Vanishing-shear family is a Level I disproof | rejected | missing global optimality | It is only a feasible family |

## 6. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Contact-isolated source points | pass | None are deleted from canonical C arguments; the new family simply has no separate isolate cloud |
| Near-equilateral triangle-free configurations | pass | `θ_R ↓ π/3` while every nonzero lattice distance remains at least one |
| Local positive equilibrium versus angle gap | pass | Interior lattice vertices balance four directions; finite global boundary equilibrium is not claimed |
| Local jammed is not global minimum-diameter optimality | pass | The family is explicitly not asserted globally optimal |
| Source/scaffold non-embeddability | pass | No scaffold is identified with a source; the family is an actual feasible source only |
| Occurrence-counted outer walks | pass | The family is used only as a density/local-angle regression, never as a canonical boundary count |
| Section-121 normalization correction | pass | No inference of `G_loc=o(D²) ⇒ G_loc/d=o(1)` is made |
| Existing exact near-chain regressions | pass | `nearchain_vertex_regressions.py` passes; its degree-five and concave-boundary examples independently block uniform local angle/degree shortcuts |

The family does not conflict with the canonical ZR/ZF scope because it is not being
used as a positive-contact-core theorem or as a full-source affine-kernel witness.

## 7. Literature imports

None. No external theorem is needed for the new regression.

## 8. Computation

The following existing regression/sanity scripts were run:

```text
python3 research/nearchain_vertex_regressions.py
python3 research/verify_target_c_anisotropic_two_arc_return_120.py
python3 research/verify_target_c_local_return_oler_121.py
```

It checked the two repository regression families by exact symbolic/radical pair
comparisons and reported:

```text
degree five: 11 points, 15 permanent unit pairs, 5 opening pairs, 35 other pairs with d²>=2; permanent graph triangle-free
degree three: 6 points, 7 permanent unit pairs, 0 opening pairs, 8 other pairs with d²>=2; permanent graph triangle-free
Exact pair-margin checks passed. Parameter-family proof is in the report.
```

The sheared-lattice proof above is analytic and does not rely on these scripts.
The near-chain script uses exact radical checks; the Section-120/121 scripts are
floating-point sanity checks of already-proved finite formulae. None proves
global optimality or Level I. The Section-120 check returned the canonical
uniform constant `4−2√3 = 0.5358983848622456` and the Section-121 certificate
explicitly reproduced the withdrawn normalization failure
`G_loc=o(D²) ⇒ G_loc/d=o(1)`.

## 9. Corrections / supersessions

No canonical theorem is superseded. The report sharpens the interpretation of the
existing near-equilateral and near-chain regressions: asymptotic density and
triangle-free near-rhombic geometry do not themselves provide a fixed gap.

## 10. Promotion recommendation

**unreviewed**. Preserve the exact regression, but do not promote it as a C-II
theorem until an independent audit checks whether a stronger version with the actual
finite global KKT/source hypotheses is needed. No state-version, route-map, or prompt
change is justified by this report.

## 11. Handoff

1. **Strongest new theorem:** the finite vanishing-shear family with
   `D_R = 2R + O(1)`, `|A_R| = Δ₂ D_R² + O(D_R)`, and angle gap `R⁻²`.
2. **Canonical chain:** `C-FULLCORE-NEAR-DISK` → `C-HARMONIC-CELL-TILING` →
   `C-AGGREGATE-TWO-ARC-DETOUR` / `C-AUGMENTED-CELL-DEFECT-BUDGET`; the new result
   is a regression against a density/angle-only bridge, not an added premise.
3. **Exact remaining lemma:** the source-level detour/deformation theorem in §4,
   plus exclusion of the macroscopic-container branch.
4. **Binding dead routes:** density-only shell exclusion, uniform angle-gap inference,
   raw support-depth-to-Oler conversion, deletion of contact-isolated points, and
   any global conclusion drawn from local jamming alone.
5. **Files to read next:** `docs/targets/target-c/CURRENT.md`, Sections 79–80,
   122–123, Target A §177, and Target B `README.md` for route-switch decisions.
