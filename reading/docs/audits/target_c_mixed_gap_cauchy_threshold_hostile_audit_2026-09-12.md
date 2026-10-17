> Generated reading edition · [exact source](../../../docs/audits/target_c_mixed_gap_cauchy_threshold_hostile_audit_2026-09-12.md) · source SHA-256 `933389f81b904339c4d3c929db16e8185495aabd5b8c819a447de791bec9e7e8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B5029F12EA2F","canonical":true,"claim_ids":["C-WRAP-MIXED-CAUCHY"],"claim_statuses":{"C-WRAP-MIXED-CAUCHY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C mixed-gap Cauchy threshold hostile audit

**Date:** 2026-09-12
**Verdict:** PASS; promoted in theorem-state audit.39.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## Claim audited

For a wrapping limit, set `theta=2 asin(lambda)`, `alpha=a/D`,
`phi=2 pi-2 theta`, `L=(3/2) sin(theta)`, and `U=3 theta-2 pi`. Canonical
Sections 93, 94, and 96 give the cyclic-gap lower/upper bounds, three gaps at least
`phi`, and `alpha>=L`, `alpha<=U`. The candidate retains the residual angular mass
instead of discarding it.

## Proof check

For `theta<5/2`, `L>U/2`, so the residual mass
`R=2(U-alpha)` is nonnegative and no larger than one special-gap capacity
`theta-phi=U`. Since `sin(x/2)` is increasing and concave on the relevant gap range,
the smallest possible chord sum places all residual mass in one distinguished gap.
This gives the perimeter floor

```math
q(\alpha,\theta)=\alpha+2\sin\theta+
\sin(2\theta-\pi-\alpha).
```

Because `partial q/partial alpha = 1-cos(2 theta-pi-alpha)>=0`, use `alpha>=L`:

```math
Q(\theta)=\frac72\sin\theta+
\sin\left(2\theta-\pi-\frac32\sin\theta\right).
```

Cauchy gives `Q(theta)<=pi sin(theta/2)`. The candidate's derivative bound is valid:
on `[theta_5,5/2]`, with `theta_5=2 acos(pi/9)`,

```math
H'(\theta)\le2+2\cos\theta-
\frac\pi2\cos(\theta/2)<0,
```

using `cos(theta)<=cos(theta_5)`, `cos(theta/2)>=cos(5/4)`, and the displayed
rational Taylor bound for `cos(5/4)`. Also `H(theta_5)>0` and `H(5/2)<0`, so the
unique root is

```math
\theta_6=2.445200194924480059\ldots,
\qquad
\mu_6=\sin(\theta_6/2)=0.939989693353197775\ldots .
```

For `theta>=5/2`, `lambda>=sin(5/4)>mu_6`, so the restriction loses no cases.

## Frontier effect

The canonical wrapping threshold becomes `lambda>=0.9399896933531978...`,
strictly improving the prior Cauchy threshold `0.9370981976747776...`. The old
Section-96 equality analyses are vacuous. This still does not close C-II; the
remaining task is the global interface/grid contradiction at the new endpoint.

**Classification:** canonical after the audit. The scalar certificate is
`research/verify_target_c_mixed_gap_cauchy_threshold.py`.
