> Generated reading edition · [exact source](../../../docs/audits/target_c_section112_joint_train_audit_2026-09-12.md) · source SHA-256 `859597606abfd34830f3930bf9bf144fec5a55516f09726044df15a7119329ed`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-D875F4B9D223","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — superseded optimized joint-train audit

**Date:** 2026-09-12  
**Verdict:** scalar and finite-count checks pass; proof-only candidate remains
unpromoted. C-II remains open.

The independent regression is
`research/verify_target_c_optimized_joint_train_legacy.py`.

The historical optimized joint-train candidate combines the exact Section-82/89 train budget with the joint-shore
capacity correction. At `sigma=4.5e-4`, it verifies

```math
T_D/D<1.827,
\qquad
|A_D|,|B_D|\ge0.085D,
\qquad
\mu_{16}=0.9760511764172871\ldots .
```

The finite phase-bin margin is `0.0013366422...D^2`, the endpoint density on one
principal corridor is above `0.0415`, and the exact-cosine contradiction margin is
`0.0039862558...` radians.

The joint-shore step is valid because the two distinct phase labels select disjoint
subsets of the same local train set, so the two small-bin capacities add to at most
`aT_DD`, not `2aT_DD`. The report still relies on proof-only Section 107 area/stability
and the audited Section-104 leakage theorem. It produces a stronger full-core carrier
bound, but does not force an exact equilateral triangle, construct a strict global
competitor, or address the macroscopic inactive-container branch.

**Disposition:** audited-working historical quantitative advance; superseded as a numbered proof-only frontier by aggregate Section 112. The theorem state remains unchanged at
`2026-09-12.audit.44`.
