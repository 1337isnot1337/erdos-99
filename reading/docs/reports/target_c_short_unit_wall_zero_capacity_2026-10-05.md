> Generated reading edition · [exact source](../../../docs/reports/target_c_short_unit_wall_zero_capacity_2026-10-05.md) · source SHA-256 `3b33e018f6f6172366eba84f4985670021aa9b395f9f20bcc296ebf823b23075`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-41056CA4E2D4","canonical":true,"claim_ids":["C-SHORT-WALL-ZERO-CAPACITY"],"claim_statuses":{"C-SHORT-WALL-ZERO-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: short unit walls have zero wall-safe refill capacity

**Date:** 2026-10-05  
**State:** \`2026-10-05.audit.57\`  
**Status:** canonical as \`C-SHORT-WALL-ZERO-CAPACITY\`.  
**LEVEL I STATUS:** still open. C-II remains open.

Audit.54 defines, for a simple polygonal wall $`C`$ of actual unit contacts,

```math
W_C=
\{x\in\operatorname{int}C:\ |x-b|>1
\text{ for every wall vertex }b\}.
```

The embedded-wall refill theorem requires certified packet sites inside $`W_C`$.

## Theorem

Let
```math
C=(v_1,\dots,v_n)
```
be a simple polygonal wall with
```math
|v_{i+1}-v_i|\le1
```
for every cyclic edge.

If
```math
n\le6,
```
then

```math
\boxed{W_C=\varnothing.}
```

The threshold is sharp: a regular unit heptagon has $`W_C\neq\varnothing`$.

## Proof

Assume $`x\in W_C`$. Put

```math
r_i=|v_i-x|>1.
```

Because $`x`$ lies inside the simple polygon, the polygonal loop has winding number $`+1`$ or $`-1`$ around $`x`$.

Let
```math
\theta_i\in(-\pi,\pi)
```
be the principal oriented angle from $`v_i-x`$ to $`v_{i+1}-x`$. Then

```math
\sum_i\theta_i=\pm2\pi.
\tag{1}
```

Write
```math
a_i=|v_{i+1}-v_i|\le1.
```

By the cosine law,

```math
a_i^2
=
r_i^2+r_{i+1}^2
-
2r_ir_{i+1}\cos|\theta_i|.
```

Hence

```math
\cos|\theta_i|
\ge
\frac{r_i^2+r_{i+1}^2-1}{2r_ir_{i+1}}.
```

Moreover

```math
r_i^2+r_{i+1}^2-r_ir_{i+1}-1
=
(r_i-r_{i+1})^2+r_ir_{i+1}-1
>0,
```

because $`r_i,r_{i+1}>1`$. Therefore

```math
\cos|\theta_i|>\frac12,
```

so

```math
|\theta_i|<\frac\pi3
```

for every edge.

Consequently,

```math
2\pi
=
\left|\sum_i\theta_i\right|
\le
\sum_i|\theta_i|
<
\frac{n\pi}{3}
\le
2\pi,
```

a contradiction.

Thus $`W_C=\varnothing`$.

## Sharpness

A regular unit heptagon has circumradius

```math
R=\frac1{2\sin(\pi/7)}>1.
```

Its center lies in the polygon and is farther than one from every wall vertex. Hence the center belongs to $`W_C`$.

Therefore seven boundary edges are necessary and the edge-count threshold is sharp.

## Target C consequence

Every terminal physical pentagon in canonical \`C-PENTAGON-WALL-DISJOINT-BULK\` is a simple five-edge unit-contact wall. Hence its wall-safe region is identically empty:

```math
\boxed{W_C=\varnothing.}
```

This remains true under any exact contact motion that preserves the five boundary contacts and keeps the wall simple, because the moved wall is still a simple unit pentagon.

Deleting wall vertices later as part of a diameter cover does not rescue the audit.54 refill contract: \`C-EMBEDDED-WALL-REFILL\` certifies packet sites against the original wall-safe region before those cover vertices are deleted.

Therefore the route

```math
\text{pentagon wall}
\;+\;
\text{exact contact motion preserving its five-cycle}
\;\Longrightarrow\;
\text{positive }W_C\text{ refill capacity}
```

is impossible.

Any continuation through \`C-EMBEDDED-WALL-REFILL\` must instead do at least one of the following:

1. break at least one pentagon boundary contact before certifying refill capacity;
2. enlarge the protected object to a composite simple unit-contact wall with at least seven boundary edges;
3. derive a different shield/replacement theorem whose protected packet region is not $`W_C`$.

Seven edges are only necessary, not sufficient: the canonical large-wall lock regression remains binding.

This theorem is finite and analytic. No computation, verifier, or asymptotic hypothesis is used.
