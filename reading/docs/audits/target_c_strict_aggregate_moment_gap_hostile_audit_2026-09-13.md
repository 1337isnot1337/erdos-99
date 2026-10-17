> Generated reading edition · [exact source](../../../docs/audits/target_c_strict_aggregate_moment_gap_hostile_audit_2026-09-13.md) · source SHA-256 `2f2aceb03bc531315dbc930add55d7e14a3e5f842cc912f724e22c30ad8217f0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4BE792C45D05","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C strict aggregate moment gap

**Date:** 2026-09-13
**Reviewed:** `research/target_c_strict_aggregate_moment_gap_2026-09-13.md`.
**Base state:** `2026-09-12.audit.46`.
**Disposition:** **PASS at proof-only Type-II scope; C-II remains open.**

## 1. Finite algebra

Write `X=q-k-sum_r d_r`.  The exact outer-walk decomposition and the audited
completion-side payment give

```math
0\le S_{\rm out}\le2X+4c_I-4-Q_{\rm loc}.
```

Hence `Q_loc<=2X+4c_I-4`.  Since

```math
E_{\rm agg}=S_{\rm out}+4F_{\rm loc}+Q_{\rm loc}
```

and each bounded nonquadrilateral face contributes at least one unit to degree
excess, `F_loc<=Q_loc`.  The largest possible right side is

```math
E_{\rm agg}
\le(2X+4c_I-4)+4(2X+4c_I-4)
=10X+20c_I-20.
```

The coefficient `10` is therefore an intentional loss from retaining both the
outer surplus and the defect term; no cancellation with the global degree defect
is hidden.

## 2. Asymptotic passage

The canonical Section-75 component estimate gives `c_I=O(D^(2/3))`, so the
finite `-20` and the `20c_I` term vanish after division by `D`.  Combining
with the canonical Section-122 lower bound

```math
\liminf E_{\rm agg}/D\ge \frac\pi2(2-\sqrt3)
```

proves

```math
\liminf\frac{q-k-\sum_r d_r}{D}
\ge\frac\pi{20}(2-\sqrt3)=0.0420893607\ldots .
```

No liminf/limsup reversal occurs: the finite inequality holds for every member
of the Type-II sequence, and the lower bound is a liminf lower bound.

## 3. Endpoint specialization and arithmetic

The Section-118 common-cap input is the separately audited lower bound

```math
\liminf\sum_r d_r/D\ge2.798596312209462\ldots .
```

Adding the two liminf bounds is valid for the same scoped sequence.  The
stdlib-only certificate uses `pi>=3.14159` and `sqrt3<=1.73205`, which
gives `c_det/10>0.04208`, and uses `S_118>2.79859`; their sum is `>2.8406`.
The exact script checks these one-sided rational inequalities.

## 4. Explicit limits of the claim

This audit does not promote a theorem-state entry.  It does not turn the local
quantities `Q_loc,F_loc` into the global `Q,f`, does not prove
simultaneous exchange compatibility, and does not give a source-preserving finite
motion or global minimum-diameter conclusion.  The endpoint number is scoped to
the Section-118 common-cap profile.  C-II and Level I remain open.

**Classification:** audited-working proof-only candidate; no state mutation.
