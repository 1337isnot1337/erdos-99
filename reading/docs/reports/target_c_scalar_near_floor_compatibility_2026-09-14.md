> Generated reading edition · [exact source](../../../docs/reports/target_c_scalar_near_floor_compatibility_2026-09-14.md) · source SHA-256 `9d4ee986c7dc492e1247637714edca0080f7fda32cc63054cf9ff79f956ffc4b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5C764E41C786","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — scalar compatibility arbitrarily close above the C-II train floor

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.50
**Run type:** exact scalar regression / adversarial closure audit
**Target:** Target C-II / Level I
**Starting status:** canonical Sections 122–123, loaded-chord/train floor, and
canonical exact-floor endpoint exclusion
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature search:** not used for the result
**Computation:** used — research/verify_target_c_scalar_near_floor.py

## LEVEL I STATUS

STILL OPEN

This report is an exact regression against scalar-only closure. It does not construct
a planar packing, a KKT stress, a global minimizer, or a disproof sequence.

## 1. Starting canonical endpoint

The current full-core route has the canonical scalar package

```math
 \mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D,
 \qquad
 \liminf\mu_D\ge
 \mu_{\rm TC}:=\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5,
```

and

```math
 \sum_r P_{{\rm exc},r}\le10(e_{BB}-k),
 \qquad
 \liminf_D\frac1D\sum_r(L_r+P_{{\rm exc},r}-2d_r)
 \ge \frac\pi2(2-\sqrt3),
```

where $`k=d_H+s_Z`$. The canonical endpoint exclusion shows that an actual
full-core sequence cannot satisfy $`\mu_D\to\mu_{\rm TC}`$, but its proof uses
the geometric train/pseudosegment structure. The question tested here is whether
the displayed scalar ledgers themselves contain a hidden positive margin above
$`\mu_{\rm TC}`$.

The implication chain is

    scalar near-floor compatibility
        -> no scalar-only margin above mu_TC
        -> any remaining endpoint gap must use actual train geometry or global minimality
        -> Sections 122--123 still require a source-level closure

## 2. Strongest genuinely new result

**Classification:** exact regression; unreviewed and noncanonical.

### Theorem — parametric scalar near-floor compatibility

For every $`\eta>0`$, there are sufficiently large integers $`D`$ and rational
assignments to the scalar variables in the current full-core package such that:

1. the pinned and loaded-hull identities hold with $`c_B=0`$ and
   $`e_{BB}=q-m_B`$;
2. the near-disk scalar perimeter inequalities hold;
3. the two train-floor inequalities
   ```math
   \frac{q-k}{D}\ge\frac{p}{2D}+\frac{Q}{2D},
   \qquad
   \frac{q-k}{D}+2\frac fD\ge2\sqrt{\frac{R_4}{D^2}}
   
   ```
   hold with strict room;
4. the exact two-cell augmented Euler/dissection identities hold, including the
   Section-123 payment and nonnegative local defect variables;
5. the Section-122 expression is positive and satisfies its canonical lower demand;
6. the normalized surplus obeys
   ```math
   \mu_{\rm TC}<\mu_D<\mu_{\rm TC}+\eta.
   
   ```

The assignment is scalar only. It is not claimed to be realizable by one convex
force hull and one planar contact source.

### Scope

All variables are the scalar quantities occurring in the canonical Sections 63, 85,
122, and 123 ledgers. The two cell labels are abstract ledger cells; their
attachment sets are not supplied as point coordinates. Contact-isolated source
points remain in the scalar identities through $`c_I`$ and $`s_Z`$, but no
affine-kernel statement is made about them. Occurrence-counted walks are represented
only by scalar lengths; no simple-boundary or Euler-path assertion is added.

The conclusion is finite for each chosen $`\eta`$, while the parametric statement is
asymptotic in the choice of sufficiently large $`D`$. It is a regression against an
algebraic inference, not a theorem about the original optimization problem.

### Proof

Put

```math
 \Delta_2=\frac\pi{2\sqrt3},
 \qquad
 f_0=\frac{4\sqrt{\Delta_2}-\pi}{5}.
```

The definition of $`\mu_{\rm TC}`$ gives

```math
 \mu_{\rm TC}=\frac\pi2+\frac{f_0}2,
 \qquad
 \mu_{\rm TC}+2f_0=2\sqrt{\Delta_2}.
 \tag{2.1}
```

Choose small positive rational $`\alpha,\beta`$, with
$`\alpha+\beta<\eta/3`$. By rational density choose $`u`$ strictly above
$`\mu_{\rm TC}+\alpha`$, sufficiently close to it that

```math
 u>\frac\pi2+\frac{f_0}2,
 \qquad
 u+2f_0>2\sqrt{\Delta_2},
 \tag{2.2}
```

and $`u+\beta<\mu_{\rm TC}+\eta`$. For a large common denominator $`D`$, round
$`uD,\beta D,f_0D/2`$ to integers while preserving these strict inequalities.
Set

```math
 q=uD+O(1),\quad m_B=\beta D+O(1),\quad
 k=2,\quad c_I=2,
```

```math
 e_{BB}=q-m_B,\qquad
 s_C=m_B+k-c_I-2=m_B-2,\qquad
 x_B=q-2k,\qquad Q_B=0.
 \tag{2.3}
```

These assignments satisfy exactly

```math
 c_I+e_{BB}+s_C=q-2+k,\quad
 q-x_B=Q_B+2k,\quad
 c_I+s_C+c_B=m_B+k-2,\quad
 e_{BB}=q-m_B.
 \tag{2.4}
```

Since $`u`$ is close to $`\mu_{\rm TC}`$, while
$`\pi/2<u<\pi`$, the near-disk scalar relations $`q<\pi D`$ and
$`x_B>\pi D-q`$ hold for large $`D`$. The normalized surplus is

```math
 \mu_D=\frac{e_{BB}+2s_C-3k}{D}
       =\frac{q+m_B-10}{D}
       =u+\beta+o(1),
 \tag{2.5}
```

which proves the required interval around the floor.

Use two equal abstract cells with

```math
 a_1=a_2=\frac{3D}{4},\qquad
 f_1=f_2=Q_1=Q_2=\frac{f_0D}{2}+O(1),\qquad
 T_1=T_2=0.
 \tag{2.6}
```

Define

```math
 d_{\rm tile}=q-2-2(a_1-2),\qquad
 X_r=e_{BB}-k-d_{\rm tile},
```

```math
 Q_r^+=X_r-a_r,\quad
 s_r=a_r-3-\frac{X_r}{2},\quad
 Q_{M,r}=Q_r^+-Q_r,\quad
 Q_{C,r}=Q_r,\quad Q_{I,r}=0.
 \tag{2.7}
```

For fixed sufficiently small $`\beta>0`$, all these quantities are nonnegative for
large $`D`$: asymptotically $`s_r=\beta D/2+O(1)>0`$, while
$`Q_r^+=3D/4+O(\beta D)>Q_r`$. The definitions give

```math
 X_r=2(a_r-3-s_r),\quad
 Q_r^+=Q_{M,r}+Q_{C,r}+Q_{I,r},\quad
 e_{BB}-k=\frac12\sum_rX_r+d_{\rm tile}.
 \tag{2.8}
```

Finally set

```math
 L_r=4a_r-6-2s_r-Q_r,\qquad
 P_{{\rm exc},r}=4f_r+Q_r=5Q_r,\qquad d_r=D.
 \tag{2.9}
```

Then $`L_r+Q_r=4a_r-6-2s_r`$, and the repaired augmented payment holds with
the exact missing-side credit:

```math
 2\sum_r(L_r+P_{{\rm exc},r}-2a_r)
 =10(e_{BB}-k-d_{\rm tile})-4\sum_rM_r,
 \quad M_r=a_r-T_r+Q_{M,r}.
 \tag{2.10}
```

For small $`\beta`$, equation (2.9) gives

```math
 L_r+P_{{\rm exc},r}-2d_r
   =(1-\beta+2f_0+o(1))D>0.
 \tag{2.11}
```

Thus the aggregate Section-122 expression is positive and exceeds its canonical
$`\frac\pi2(2-\sqrt3)D`$ demand for large $`D`$. The train-floor inequalities
follow from (2.2) and the rounding choice. The local zero-host and Section-89
scalar inequalities have strict room because (2.11) has a positive linear margin
and the same quadratic margins as the existing scalar compatibility certificate.
This proves the theorem. $`\square`$

## 3. Certified finite instance

The accompanying exact certificate takes $`D=10^{12}`$,
$`q/D=1.6375625`$, $`m_B/D=0.0000005`$, and
$`f/D=0.133532`$ per cell. It obtains

```math
 \mu_D=1.637562999990.
```

The rational bounds in the script certify

```math
 \mu_{\rm TC}<1.637562184369,
 \qquad
 \mu_D-1.637562184369>0.
```

The abstract two-cell ledger has

```math
 \sum_r(L_r+P_{{\rm exc},r}-2d_r)=2534126999992>0,
```

and satisfies the exact pinned, train, augmented-payment, Section-122, and
Section-123 scalar checks.

## 4. Exact frontier effect

This regression rejects the implication

    Sections 63, 85, 122, 123 + loaded-chord relation
        -> an explicit scalar gap mu_D >= mu_TC + epsilon_0.

More strongly, the parametric construction shows that no positive scalar gap can be
obtained from those inequalities alone. The canonical exact-floor exclusion is not
undermined: it uses actual train pseudosegments, phase orientation, an unequal-shore
complete crossing extraction, and a source-hull diameter inequality, none of which is
encoded in this scalar witness.

The macroscopic inactive chamber/exterior-cap branch is unaffected.

## 5. Exact remaining lemma

A closing theorem must use a genuinely geometric or variational fact absent from the
scalar package. In the full-core branch, it must either:

1. upper-bound the actual occurrence-counted $`\sum_r(L_r-2d_r)`$ after the
   Section-123 payment;
2. turn the loaded-hull/nonunit-side or aggregate-detour currency into an explicit
   same-cardinality unit-separated source of diameter strictly below $`D(n)`$; or
3. force an exact unit equilateral triangle.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Parametric scalar assignments near $`\mu_{\rm TC}`$ | regression theorem | Sections 63/85/122/123 definitions | Rational-density perturbation of the exact scalar floor |
| Finite $`D=10^{12}`$ instance | exact regression | research/verify_target_c_scalar_near_floor.py | Fraction checks with certified rational bounds |
| Scalar package has an explicit positive gap | rejected | Current scalar package | Parametric assignments approach the floor from above |
| Scalar witness is a planar source | rejected interpretation | None | No coordinates or incidence realization are asserted |
| Scalar witness is a global minimizer | rejected interpretation | Global optimality absent | No $`D(n)`$ certificate is supplied |
| C-II is closed | false | Source-level bridge missing | The regression does not address that bridge |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
| --- | --- | --- |
| Contact-isolated source points | pass | $`c_I`$ and $`s_Z`$ remain explicit; no isolate enters the affine core |
| Loaded-chord relation | pass | $`c_B=0`$, $`e_{BB}=q-m_B`$ are imposed exactly |
| Train-floor endpoint exclusion | pass | The canonical exclusion uses geometry absent from the scalar witness |
| Occurrence-counted walks | pass | Walks remain scalar occurrences; no simple-boundary reduction is used |
| Section-123 dissection slack | pass | $`d_{\rm tile}\ge0`$ and the augmented identity are checked exactly |
| Scalar-to-source promotion | rejected | No planar embedding, KKT stress, or global optimality is claimed |

## 8. Literature imports

No external theorem is imported. The proof uses rational density and canonical
repository ledgers only. The script uses certified rational bounds for $`\pi`$,
$`\sqrt3`$, and the derived train-floor expression; no floating-point assertion is
used as a premise.

## 9. Computation

Run:

    python3 -m py_compile research/verify_target_c_scalar_near_floor.py
    python3 research/verify_target_c_scalar_near_floor.py

The script uses Fraction arithmetic throughout. It checks the pinned and loaded-hull
identities, the certified floor comparison, near-disk scalar room, the exact
two-cell augmented identity, Section-123 payment, positive Section-122 detour, the
two train-floor inequalities, and the local scalar margins. It does not check a
planar embedding, source cardinality, positive KKT stress, global minimum diameter,
or any original Level-I quantifier.

## 10. Corrections / supersessions

This report does not supersede target_c_latest_scalar_compatibility. It strengthens
that regression by moving its witness from $`\mu_D\approx2.1`$ to a certified value
only about $`8.2\times10^{-7}`$ above the train floor, and by proving a
rational-density parametric version. It does not challenge the canonical geometric
endpoint exclusion.

## 11. Promotion recommendation

**regression/rejection only.** Do not update the canonical theorem manifest or route
map. Preserve this artifact to prevent a future scalar-only upgrade from silently
reusing a false margin.

## 12. Handoff

1. **Strongest new result:** the current scalar ledgers admit exact rational
   assignments arbitrarily close above $`\mu_{\rm TC}`$ with positive Section-122
   detour.
2. **Canonical dependency chain:** C-FULLCORE-LOADED-CHORD +
   C-FULLCORE-TRAIN-SURPLUS-FLOOR + C-AGGREGATE-TWO-ARC-DETOUR +
   C-AUGMENTED-CELL-DEFECT-BUDGET, used only as scalar statements.
3. **Exact remaining lemma:** an actual train-geometry or source-preserving global
   minimality theorem controlling aggregate detour/nonunit-side currency.
4. **Binding dead route:** scalar elimination without planar realization or global
   optimality is rejected.
5. **Files to read next:** docs/targets/target-c/CURRENT.md, the canonical Sections
   122–123, and the canonical endpoint report.
