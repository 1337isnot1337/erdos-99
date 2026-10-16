<!-- theorem-state: {"artifact_id":"ART-0664E92246F1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 112 aggregate projection audit

**Date:** 2026-09-12  
**Verdict:** scalar and aggregate-count checks pass; proof-only candidate remains
unpromoted. C-II remains open.

The independent regression is
`research/verify_target_c_aggregate_projection_gap_112.py`.

The key improvement is to retain the full principal-corridor endpoint mass from both
disjoint phase families before selecting a corridor. At `sigma=10^-3`, the leakage
bound with `h=0.0413` leaves

\[
P=0.0836069307802826\ldots
\]

principal endpoint density per family. The two-family metric argument forces aggregate
projection cost at least

\[
P\,2\left(1-\cos\frac{m}{2}\right)
=0.0017800942587230\ldots,
\]

while the available route slack is only `0.001`. The resulting carrier coefficient is

\[
\mu_{16}=0.9760638978066385\ldots .
\]

This remains conditional on proof-only Sections 107 and 111 and the audited Section-104
leakage theorem. It excludes only the full-core branch under the stated cap; it does
not force an exact unit equilateral triangle, construct a strict global competitor, or
resolve the macroscopic inactive-container branch.

**Disposition:** audited-working quantitative advance; theorem state unchanged at
`2026-09-12.audit.44`.
