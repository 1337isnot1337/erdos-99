> Generated reading edition · [exact source](../../../docs/audits/target_c_section109_asymptotic_shore_audit_2026-09-12.md) · source SHA-256 `fcf163fcb78afe587ba45d3a5cab690a82c19bfe4024ff964fcbf36486a1b8f0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AE8C314F7654","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 109 asymptotic phase-shore audit

**Date:** 2026-09-12  
**Verdict:** scalar and asymptotic counting checks pass; proof-only candidate remains
unpromoted. C-II remains open.

The independent regression
`research/verify_target_c_asymptotic_phase_shores.py` verifies the Section-109
constants and the strict finite margins. With carrier rhombus density `r` and train
budget `C_T`, the bin argument gives every shore density

$$
a<\frac{r}{6C_T}.
$$

Using `r=0.472`, `C_T=6`, and `a=0.0131` gives endpoint density `0.0262`. The
certificate obtains

$$
\theta_{13}=2.7029186637961029\ldots,
\qquad
\mu_{13}=0.9760419221833405\ldots,
$$

and verifies the leakage/projection contradiction margin
`0.0107208601...` radians at `sigma=5e-5`.

The result still depends on proof-only Sections 104 and 107 for geometric leakage and
area rigidity. It yields a stronger carrier lower bound in the full-core Type-II
branch, but does not force an exact unit equilateral triangle, construct a strict
source-preserving subdiameter competitor, or resolve the macroscopic inactive-container
branch.

**Disposition:** audited-working quantitative advance; theorem state unchanged at
`2026-09-12.audit.43`.
