<!-- theorem-state: {"artifact_id":"ART-2D9A4A9C8A89","canonical":true,"claim_ids":["C-WRAP-CAUCHY"],"claim_statuses":{"C-WRAP-CAUCHY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Cauchy wrapping-threshold hostile audit

**Date:** 2026-09-12
**Verdict:** PASS; promoted in theorem-state audit.38.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## Claim audited

For a wrapping Type-II harmonic-cell sequence with normalized cell diameter
`lambda<1`, put `theta=2 asin(lambda)` and `alpha=a/D`, where `a` is the loaded
attachment count. Canonical Section 94 gives

\[
\liminf \frac{\operatorname{per}(P_D)}D\ge\alpha+3\sin\theta,
\]

and canonical Section 96 gives

\[
\alpha\ge\frac32\sin\theta.
\]

The candidate combines these with the elementary convex-body inequality
`per(P_D)<=pi diam(P_D)`.

## Hostile proof check

The two canonical lower bounds imply

\[
\liminf \frac{\operatorname{per}(P_D)}D
\ge\frac92\sin\theta.
\]

Since `diam(P_D)/D -> lambda=sin(theta/2)`, Cauchy's projection formula gives

\[
\limsup \frac{\operatorname{per}(P_D)}D
\le\pi\sin(\theta/2).
\]

On the admissible wrapping interval `theta in [2pi/3,pi)`, `sin(theta/2)>0` and
`sin(theta)=2 sin(theta/2) cos(theta/2)`. Cancelling the positive factor yields

\[
9\cos(\theta/2)\le\pi.
\]

Therefore

\[
\lambda=\sin(\theta/2)
\ge\sqrt{1-(\pi/9)^2}
 =0.9370981976747776\ldots .
\]

The inequality is strict relative to the canonical Section-96 value
`0.936215741409583...`; direct evaluation gives a gap of about `8.82456e-4`.
No endpoint equality, KKT coefficient floor, contact-isolate deletion, or
unpromoted Section-97/98 statement is used.

## Frontier effect

The nominal Section-96 endpoint `lambda=0.936215741409583...` is incompatible with
the audited canonical inequalities and Cauchy. The proof-only Section-97 and Section-98
endpoint analyses remain valid only as conditional arguments over an empty asymptotic
regime. The live full-core branch must start at the stronger threshold above.

This does not close C-II. It leaves the same global obligation at the new endpoint:
couple the near-rhombic carrier, ordered train grid, and interface data to an exact
unit triangle or a source-preserving strict diameter decrease.

## Disposition

**Classification:** canonical after the audit.38 promotion transaction.
