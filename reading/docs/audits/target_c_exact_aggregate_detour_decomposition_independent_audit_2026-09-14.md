> Generated reading edition · [exact source](../../../docs/audits/target_c_exact_aggregate_detour_decomposition_independent_audit_2026-09-14.md) · source SHA-256 `f4d167d0eed11074f17afc79598ee4de047b8b7cc528b61f71af43ed6e8d074b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C977E57F6E1B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — exact aggregate detour decomposition

**Date:** 2026-09-14  
**Audited artifact:** `docs/reports/target_c_exact_aggregate_detour_decomposition_2026-09-14.md`  
**State version:** `2026-09-14.audit.51`  
**Verdict:** `PASS` at audited-working proof-only scope  
**LEVEL I STATUS:** `STILL OPEN`

## 1. Audit question

The report claims that the canonical Section-122 residual

```math
 S_{\rm out}=\sum_r(L_r-2d_r)
```

has the exact finite decomposition (AD.3), and that adding the actual exceptional
face perimeters gives (AD.4). The audit checks the local Euler identity, the
augmented-cell substitution, all signs, and the scope of the multiplicities.

## 2. Independent algebra check

For one induced harmonic graph, canonical Section 82 states

```math
 L_r+Q_r=4a_r-6-2s_r-2c_r.
```

With `eta_r=a_r-3-s_r`, direct rearrangement gives

```math
 L_r=2a_r+2eta_r-2c_r-Q_r.
```

Thus

```math
 L_r-2d_r
 =2(a_r-d_r)+2eta_r-2c_r-Q_r.
```

Canonical Section 123 states

```math
 eta_r=(a_r-T_r+Q_r^+)/2
```

and

```math
 e_{BB}-k=\sum_r eta_r+d_{tile}.
```

Therefore `sum eta_r=e_BB-k-d_tile`, and summing proves (AD.3) exactly.

The actual bounded nonquadrilateral perimeter is, by definition,

```math
 P_{{\rm exc},r}=4f_r+Q_r.
```

Adding this to the component identity cancels `-Q_r` and gives (AD.4), with no
inequality or asymptotic replacement.

Finally, Section 123 gives

```math
 d_{tile}=q-2-a+2c_I,
 \qquad
 c_I+e_{BB}+s_C=q-2+k.
```

Eliminating `c_I` gives

```math
 a=3q-6+2k-2e_{BB}-2s_C-d_{tile}.
```

Substitution into (AD.3) gives

```math
 S_{\rm out}=6q-12+2k-2e_{BB}-4s_C-2\sum_rd_r
 -4d_{tile}-2C_{loc}-Q_{loc}.
```

Since `mu_D D=e_BB+2s_C-3k`, the first three currency terms equal
`-2mu_DD-4k`, proving (AD.5). Every displayed algebraic identity passes.

## 3. Scope and multiplicity audit

1. `L_r` is not replaced by a simple polygon perimeter. Bridges and repeated outer
   occurrences remain included because the only use of `L_r` is canonical Section
   82's occurrence-counted face-incidence identity.

2. The sum `C_loc=sum c_r` is deliberately local. If a loaded-loaded contact is
   present in more than one induced cell, it is counted with that multiplicity. The
   identity remains true, and its coefficient is negative in (AD.3), so no hidden
   upper bound on multiplicity is used.

3. The `d_tile` relation is the exact Section-123 convex-cell triangulation deficit;
   it is not inferred from a simple global boundary. Its nonnegativity is canonical.

4. Contact-isolated source points are not vertices of these positive-contact ledgers,
   but the report never deletes them from the source or uses a deformation of them.
   The affine-kernel theorem is not invoked.

5. The no-component endpoint is consistent: when `c_I=0`, `a=0`,
   `d_tile=q-2`, and the pinned ledger gives `e_BB-k=q-2`; the identity reduces to
   `S_out=0`, as it must because the component sum is empty.

6. The formula is finite. It does not divide by `D`, pass to a subsequence, or
   replace a source by a scaffold.

## 4. Regression audit

| Regression | Result | Reason |
|---|---|---|
| Contact-isolated points | pass | retained globally; absent only from explicitly core-local quantities |
| Repeated vertices/bridges | pass | occurrence-counted `L_r` is never simplified |
| Shared cell boundaries | pass | only cell-local incidence is used |
| Loaded-loaded chord multiplicity | pass | `C_loc` records it with exact multiplicity |
| Scalar near-floor witness | pass | satisfies ledgers with positive detour; shows no contradiction follows automatically |
| Vanishing-shear oblique lattice | pass | no affine conclusion is inferred |
| Macroscopic chamber/cap | uncovered by design | the theorem is full-core-only |

## 5. Audit conclusion

The report is correct as an audited-working exact reduction under the canonical
Sections 82 and 123 hypotheses. It advances the bookkeeping frontier by replacing
the formerly free aggregate detour with identities (AD.3)–(AD.5). It does **not**:

- upper-bound the right-hand side with a strict margin;
- construct a same-cardinality feasible competitor;
- force a unit equilateral triangle;
- cover the macroscopic-container branch; or
- discharge the Level-I quantifiers.

The proper lifecycle is therefore `audited-working`, not canonical closure.
