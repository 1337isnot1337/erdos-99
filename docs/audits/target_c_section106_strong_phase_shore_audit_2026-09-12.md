<!-- theorem-state: {"artifact_id":"ART-C8CCC53E6BF5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 106 stronger phase-shore audit

**Date:** 2026-09-12  
**Verdict:** arithmetic and finite-count checks pass; proof-only candidate remains
unpromoted.  C-II remains open.

This audit checks the stronger Section 106 phase-shore candidate against the canonical
Sections 90, 101--103 and the proof-only Sections 104--105.  The independent scalar
regression is `research/verify_target_c_strong_phase_shore_gap.py`.

## 1. What is established

The certificate reproduces the stated root of

\[
3\theta-2\pi-\sin(\theta/2)-2\sin\theta=1.2\times10^{-5}
\]

and obtains

\[
\theta=2.7029105818462229\ldots,
\qquad
\mu=\sin(\theta/2)=0.9760410429297388\ldots .
\]

It independently checks the phase-shore arithmetic:

\[
0.179-5.317/1000=0.173683,
\]

\[
\frac{19}{20}\frac{0.173683}{3}=0.0549996166\ldots>0.054,
\]

so the bin argument with two total train shores bounded by `6D` supports shore
density `0.0045` and endpoint density `0.009`.

At `h=0.00455`, the inherited leakage expression gives

\[
L=0.005604304520\ldots,
\qquad
\rho=\frac{0.009-L}{3}=0.001131898493\ldots>0.00113.
\]

Exact cosine inversion then gives

\[
\Delta<0.14586513,
\qquad
m-2\Delta>0.0123802,
\]

where `m` is the Section-102 principal-corridor separation lower bound.  The numerical
inequalities in the candidate therefore have strict margins.

## 2. Scope limits

The checks above do not prove the inherited complement-gap stability, route-excess
ledger, leakage estimate, or the canonical carrier concentration theorem.  Section 106
rederives the principal-route excess inequality but still uses the proof-only Section
104 technical estimates.  It also remains a subsequential macroscopic argument; it
does not produce an exact unit equilateral triangle or a source-preserving strict
subdiameter competitor.

The canonical ordered-grid Section 91 remains the next bridge.  Its explicit grid
coefficient is too small to force the grid diameter above `D`, so Section 106 cannot be
promoted as a C-II closure from the present inputs.

**Disposition:** audited-working arithmetic candidate; theorem state unchanged at
`2026-09-12.audit.43`.
