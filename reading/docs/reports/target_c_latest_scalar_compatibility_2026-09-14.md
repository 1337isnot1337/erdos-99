> Generated reading edition · [exact source](../../../docs/reports/target_c_latest_scalar_compatibility_2026-09-14.md) · source SHA-256 `c941a0967a7f9bb0ed6bce5f1ce747dac84bd3da99653d6b65b659ac5057e443`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-8A83749A39EA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_latest_scalar_compatibility_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b3ccc234ddc6dc996feb8c53d39b6918b2a91cb3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — current C-II scalar-package compatibility regression

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** exact scalar regression / adversarial closure audit
**Target:** Target C-II / Level I
**Classification:** unreviewed candidate; not canonical
**Certificate:** `research/verify_target_c_latest_scalar_compatibility.py`

## LEVEL I STATUS

`STILL OPEN`

This report records an exact no-go for scalar-only elimination from the current
promoted package. It does not construct a planar packing, a KKT stress, a source
configuration, a global minimizer, or a disproof sequence.

## 1. Candidate implication audited

The attempted closure chain was

```text
loaded-chord elimination + train-coupled mu floor
    -> Section-122 detour lower bound plus Section-123 payment
    -> contradiction in the full-core branch
```

The current canonical inputs are, in their exact scopes,

```math
\liminf\mu_D\ge
\mu_{TC}:=\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5,
\qquad
\sum_r P_{{\rm exc},r}\le10(e_{BB}-k),
```

and

```math
\liminf_D\frac1D\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\ge\frac\pi2(2-\sqrt3).
```

The loaded-chord companion supplies (c_B=0) and
(e_{BB}=q-m_B) in the full-core near-disk branch. The regression below satisfies
all these scalar relations with strict room, while retaining positive aggregate
detour.

## 2. Exact scalar witness

Take (D=10^6), (q=8D/5), (d_H=0), (s_Z=2), (k=2), (c_I=2), and
```math
m_B=D/2,
\qquad e_{BB}=q-m_B=11D/10,
\qquad s_C=D/2-2.
```
Then the pinned and loaded-hull identities hold exactly:

```math
c_I+e_{BB}+s_C=q-2+k,
\quad q-x_B=Q_B+2k,
\quad c_B=0,
\quad c_I+s_C+c_B=m_B+k-2.
```

The renormalized surplus is
```math
\mu_D=\frac{e_{BB}+2s_C-3k}{D}=2.09999,
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
which is strictly above the current train-coupled floor. Indeed (\pi<22/7) and
\(\sqrt3>5/3) imply
```

```math
\mu_{TC}<\frac{58}{35}<2.09999.
```



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The near-disk perimeter annotation is also scalar-compatible: (q/D=8/5<\pi),
and the hull-walk excess (x_B=q-4) exceeds
\((\pi-8/5)D<(54/35)D). This is only a scalar perimeter decomposition; no
polygon or outer contact walk is asserted.
```



For two abstract actual cells set
```math
a_r=3D/4,\quad s_r=D/4-1,\quad c_r^\partial=0,
\quad f_r=Q_r=D/8,
```
with (T_r=0), (Q_r^+=D/4-4), and (P_{{\rm exc},r}=5D/8). The exact
local Euler identity gives
```math
L_r=19D/8-4,
\qquad
L_r+P_{{\rm exc},r}-2D=D-4.
```
Thus the aggregate Section-122 expression is (2D-8), which is strictly larger
than the canonical lower demand because
```math
\frac\pi2(2-\sqrt3)D<\frac{11}{21}D<2D-8.
```

The same cells satisfy the augmented Section-123 identity. Their dissection slack is
```math
d_{\rm tile}=q-2-2(a_r-2)=D/10+2,
```
and, writing (X_r=a_r-T_r+Q_r^+=D-4),
```math
e_{BB}-k=\frac12\sum_rX_r+d_{\rm tile}=11D/10-2.
```
The exact augmented payment inequality is met with equality:
```math
\sum_r(L_r+P_{{\rm exc},r}-2a_r)
=10(e_{BB}-k-d_{\rm tile})-4\sum_rM_r,
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
where (M_r=7D/8-4). Also
\(sum_rP_{{\rm exc},r}=5D/4\le10(e_{BB}-k)).
```



The Section-85 train-end inequality is compatible: with total (f=D/4),
```math
q-k+2f>\frac{49}{25}D,
```


**Source formatting excerpt (unbalanced inline math in the original):**

```text
while (R_4/D^2\) may have its canonical near-disk value
\(\pi/(2\sqrt3)), for which (2\sqrt{R_4}<(49/25)D) under the elementary
rational bounds used by the certificate. The Section-89 same-cell train budget and
the local zero-host area inequalities have similarly strict rational margins.
```



Every assertion is checked by `Fraction` arithmetic in the certificate. The
occurrence-counted boundary and repeated-vertex conventions are not silently
replaced by simple cycles; they are represented only through the scalar variables.

## 3. What this proves and what it does not

The certificate proves that the current scalar package has a compatible point with

- the promoted (c_B=0) loaded-chord relation;
- the promoted train-coupled surplus floor;
- the exact pinned and augmented-cell ledgers;
- the Section-122 lower demand;
- the Section-123 exceptional-perimeter payment;
- the near-disk perimeter scale; and
- the train-end/local area inequalities.

It therefore rejects the proposed implication

```text
current scalar ledgers -> full-core contradiction.
```

The witness is not a geometric counterexample. It does not realize the exact
incidence of actual cells, the convex force hull, the contact graph, a positive KKT
stress, source cardinality, or global diameter optimality. A source-level bridge is
still required: an upper bound for the actual aggregate detour, an exact triangle,
or an explicit same-cardinality strict diameter decrease.

## 4. Regression audit

| Item | Classification | Result |
| --- | --- | --- |
| Loaded-chord relation | canonical input | Used only as (c_B=0,e_{BB}=q-m_B) |
| Train-coupled surplus floor | canonical input | Satisfied with (mu_D=2.09999) |
| Section 122 detour demand | canonical input | Satisfied with positive (2D-8) margin |
| Section 123 payment | canonical input | Satisfied, including exact augmented identity |
| Contact-isolated source points | regression check | None are deleted; (c_I,s_Z) remain explicit |
| Scalar witness as planar source | rejected interpretation | No embedding or global optimality is claimed |
| Scalar witness as Level-I disproof | rejected interpretation | It is not a construction of global minimizers |

The vanishing-shear lattice regression remains the relevant geometric warning:
near-disk, near-density, triangle-free local structure does not imply a fixed
second-order loss. It likewise does not supply global optimality.

## 5. Exact remaining C-II implication

The full-core branch still requires a theorem of one of these forms:



**Source formatting excerpt (unbalanced inline math in the original):**

```text
1. an upper bound on the actual occurrence-counted
   \(\sum_r(L_r-2d_r)\) strong enough to contradict Section 122 after the exact
   Section-123 payment;
2. a source-preserving finite deformation with the same cardinality, all pairwise
   distances at least one, and diameter strictly below (D(n)); or
3. an exact unit equilateral triangle forced by the source geometry.
```



The Type-I macroscopic internal-chamber/exterior-cap branch remains separately open;
the scalar witness does not address it.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| (c_B=0, e_{BB}=q-m_B) | canonical input | `C-FULLCORE-LOADED-CHORD` | Used only in its near-disk full-core scope |
| (liminfmu_Dgemu_{TC}) | canonical input | `C-FULLCORE-TRAIN-SURPLUS-FLOOR` | Witness has (mu_D>mu_{TC}) with rational room |
| Local Euler and augmented-cell identities | exact regression | Sections 82/123 definitions | Checked for two abstract cells by integer arithmetic |
| Section-122 detour lower demand | canonical input | `C-AGGREGATE-TWO-ARC-DETOUR` | Witness has aggregate value (2D-8) |
| Section-123 exceptional payment | canonical input | `C-AUGMENTED-CELL-DEFECT-BUDGET` | Payment and augmented identity both pass |
| Abstract witness as a planar source | rejected interpretation | None | No coordinates or incidence realization is supplied |
| Abstract witness as a global minimizer | rejected interpretation | Global optimality absent | No (D(n)) certificate is asserted |
| Scalar package closes C-II | rejected implication | Current scalar package | Exact compatible assignment leaves positive detour |

## 7. Regression checks

The witness was checked against the binding C-II failure modes:

- all source-level quantities retained in the scalar annotation, including (c_I)
  and (s_Z); no isolated source is put into the ZR/ZF core;
- outer-walk quantities are treated as occurrence counts, with no Euler-path or
  simple-boundary assumption;
- (c_B=0) is imposed rather than inferred from an arbitrary polygon;
- the train-end inequality is imposed at the near-disk (R_4/D^2) scale;
- the exact (D)-dependent integer margins are retained before taking any limit;
- no scalar witness is interpreted as a source/scaffold embedding; and
- the vanishing-shear, square-grid, strict-saturated-chamber, and co-embedded-cover
  regressions remain outside the witness and continue to block geometry-free
  upgrades.

The key negative result is not a counterexample to the original problem. It is a
counterexample to the narrower inference that the displayed scalar ledgers alone
force a contradiction.

## 8. Literature imports

No external theorem is imported. The proof uses only the canonical repository
theorem IDs named above and elementary inequalities
(3<pi<22/7) and (sqrt3>5/3) to certify strict rational margins. No literature
result is used to identify the abstract variables with a geometric source.

Two external scope checks were made during the continuation audit. The public
listing for Erdős Problem 99 still labels the original question open and describes
Thue's triangular-lattice construction only as an asymptotic benchmark; it does not
provide the required every-cardinality/every-minimizer theorem. The primary paper
by Pach, Radoičić, and Vondrák, *On the diameter of separated point sets with many
nearly equal distances*, Theorem 1.1, proves a lower bound of order
$`n^{2/(d-1)}`$ when $`\Omega(n^2)`$ pairs have distances in one interval of
length one. That hypothesis is not supplied by the C-II contact/cell ledgers: they
give unit contacts and local rhombic faces, not a quadratic population of nearly
equal long distances. Consequently the result does not bound the occurrence-counted
outer detour, force a unit equilateral triangle, or furnish a strict finite
same-cardinality diameter decrease. It is recorded as a near miss only, not as a
dependency of this regression.

## 9. Computation

Run:

```text
python3 research/verify_target_c_latest_scalar_compatibility.py
```

Expected output consists of six `PASS` lines ending with
`abstract scalar witness is not a planar/global packing`. The computation proves
only the rational compatibility assertions above; it does not prove any global
packing or optimality statement.

The certificate uses Python `Fraction` arithmetic throughout. It checks the exact
pinned, loaded-hull, train-floor, local-Euler, augmented-payment, Section-122,
Section-123, near-disk, and Section-89 inequalities at (D=10^6). It does not
check a planar embedding, a KKT stress, a source cardinality (n), or the value of
(D(n)). The separate fixed-container and affine-window regression commands listed
in the run ledger were also rerun during the hostile audit; their scopes remain
restricted to the reports that define them.

## 10. Corrections / supersessions

This report does not supersede a canonical theorem. It refreshes the older scalar
compatibility artifact, whose state snapshot predates the promoted loaded-chord and
train-coupled results, and explicitly adds those current constraints to the
regression. The older artifact remains provenance; this report is the current
unreviewed scalar no-go certificate.

## 11. Promotion recommendation

**unreviewed**. The arithmetic and scope audit are complete, but the witness is
deliberately not a geometric theorem and therefore cannot be promoted as a C-II
dependency. No state-version increment or canonical route-map change is justified.

## 12. Handoff

1. **Strongest new result:** the current promoted scalar package remains compatible
   with a positive Section-122 detour; the exact witness is the one given in §2.
2. **Canonical dependency chain:** `C-FULLCORE-NEAR-DISK` (	o)
   `C-FULLCORE-LOADED-CHORD` (	o)
   `C-FULLCORE-TRAIN-SURPLUS-FLOOR`, together with
   `C-AGGREGATE-TWO-ARC-DETOUR` and
   `C-AUGMENTED-CELL-DEFECT-BUDGET`.
3. **Exact remaining lemma:** bound the actual
   (sum_r(L_r-2d_r)), construct a finite source-preserving strict decrease, or
   force an exact unit equilateral triangle; separately eliminate the Type-I
   macroscopic container/cap branch.
4. **Binding dead routes:** scalar elimination, density-only angle gaps, contact
   creation without force transfer, full-source affine-kernel extension, and
   arbitrary affine-window equilateralization.
5. **Files to read next:** [Target C current frontier](../targets/target-c/CURRENT.md),
   [the Section 122–123 promotion audit](../targets/target-c/122-123-promotion-audit-2026-09-12.md),
   [the train-floor audit](../audits/target_c_fullcore_train_coupled_surplus_floor_independent_audit_2026-09-14.md),
   and [the C-II proof-obligation ledger](target_c_sol_run_ledger_2026-09-14.md).
