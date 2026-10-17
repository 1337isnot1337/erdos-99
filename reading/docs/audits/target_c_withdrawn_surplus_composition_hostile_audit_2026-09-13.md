> Generated reading edition · [exact source](../../../docs/audits/target_c_withdrawn_surplus_composition_hostile_audit_2026-09-13.md) · source SHA-256 `d617e6260d7e6e388f0b4828de6939e539a778abbea2de6510e4c793fd0c78f3`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-85090E90E2B3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — withdrawn surplus/diameter scalar composition

**Date:** 2026-09-13  
**Base state:** `2026-09-12.audit.46`  
**Reviewed:** `research/target_c_surplus_diameter_scalar_composition_2026-09-12.md`.

**Disposition:** REJECT the former `2.0585` floor and the claimed elimination of
`t=1.9`. The reviewed report's corrected algebra is sound and its original scalar
composition must not be used as a theorem premise. Canonical state is unchanged.

## 1. Normalization check

The finite attachment identity is

```math
c_I+s_C=m+k-2.
```

After division by `D`, this is

```math
\frac mD=c+s-\kappa+\frac2D,
```

not `c+s-kappa+2`. Hence

```math
e=t+2\kappa-c-s-\frac2D,
\qquad
\frac{e_{BB}+2s_C-3k}{D}
=t-\kappa+s-c-\frac2D.
```

Using `e>=0` gives only

```math
2t+\kappa\ge z_0-o(1),
```

while the separate moment input gives

```math
5t-2\kappa\ge A_0-o(1).
```

There is no normalized `+4` term. The old `2.0585` interval came from treating the
finite integer `2` as a quantity of order `D`.

## 2. Witness check

The corrected scalar values

```math
t=1.9,\quad \kappa=0,\quad e=0.9,\quad c=0,\quad s=1
```

satisfy the corrected asymptotic identities and the displayed surplus and moment
lower bounds. The accompanying verifier passes these exact rational checks. This is
only a scalar feasibility witness; it is not a geometric contact complex or a global
minimizer, but it is sufficient to refute the former scalar elimination claim.

**Verdict:** the old composition is rejected. The corrected report is useful only as a
bookkeeping regression and must not be promoted or used to exclude the high-surplus
Type-II region.

## Final disposition

The finite-versus-asymptotic normalization error is now recorded in a hostile audit as
well as in the source report and research index. No state mutation is justified; C-II
remains open.
