> Generated reading edition · [exact source](../../../docs/audits/target_c_section127_interface_augmented_defect_dichotomy_hostile_audit_2026-09-12.md) · source SHA-256 `ab3e923759d0ca6ac1d39f041c5e962507dd7ff5c858696e8d9ae2b7058b69cf`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-802BFCD3619E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C interface/augmented-defect dichotomy

**Date:** 2026-09-12  
**Reviewed:** proof-only Section 127 interface-floor candidate.  
**Disposition:** **PASS at proof-only scope.** C-II remains open.

## 1. Exact implication chain

```text
Section 123 augmented-cell identity + Section 85 rhombus boundary floor
 -> (q-k)+J_aug >= 2 sqrt(R_4)
 -> Type-II high loaded density or linear augmented/tile defect.
```

The defect term is retained. No conclusion of `q-k >= 2 sqrt(R_4)` is made without
the additional hypothesis `J_aug=o(D)`.

## 2. Augmented identity

Canonical Section 123 gives

```math
e_{BB}-k=\frac12\sum_r(a_r-T_r+Q_r^+)+d_{tile}.
```

With

```math
A_*:=\sum_r(a_r-T_r),\qquad Q_*:=\sum_rQ_r^+,qquad
J_{aug}:=A_*+Q_*+2d_{tile},
```

this is exactly

```math
\boxed{J_{aug}=2(e_{BB}-k)}.
```

The identity is finite and uses no global boundary-occurrence injection.

## 3. Interface substitution

Canonical Section 63 gives

```math
e_{BB}-k=Q+k+u_B+c_B\ge Q,
```

and every bounded nonquadrilateral face contributes at least one to the global
degree excess (Q). Hence (e_{BB}-k\ge f), so

```math
J_{aug}\ge2f.
```

Canonical Section 85 supplies

```math
q-k+2f\ge2\sqrt{R_4}.
```

Adding the two inequalities gives

```math
\boxed{(q-k)+J_{aug}\ge2\sqrt{R_4}}.
```

The inequality directions and the factor of two are correct.

**Verdict:** PASS.

## 4. Type-II passage and case split

In the canonical full-core Type-II branch,

```math
R_4/D^2\to\Delta=\frac\pi{2\sqrt3}.
```

Dividing the finite inequality by (D) gives

```math
\liminf\frac{(q-k)+J_{aug}}D\ge2\sqrt\Delta.
```

If (J_{aug}=o(D)), this yields the stated (q-k) floor. More generally, if
`(q-k)/D <= 2 sqrt(Delta)-eta+o(1)`, subtracting gives

```math
J_{aug}/D\ge eta-o(1).
```

This is an exhaustive two-way implication with the defect term intact.

**Verdict:** PASS, conditional on the canonical Type-II area asymptotic.

## 5. Scope and limitations

- The result is proof-only and does not alter the canonical theorem state.
- It does not bound `J_aug`, `q-k`, or the aggregate detour from above.
- It does not eliminate the high-density branch or the linear-defect branch.
- It does not address the macroscopic inactive-container branch.
- Contact-isolated source points remain outside the core ledgers and are not removed.

## Final classification

**Audited-working.** The interface/augmented-defect dichotomy is exact at its stated
scope and is safe to preserve as a research dependency. C-II remains open.
