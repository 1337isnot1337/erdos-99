> Generated reading edition · [exact source](../../../docs/audits/target_c_short_unit_wall_zero_capacity_promotion_audit_2026-10-05.md) · source SHA-256 `b920d0e04e244e30d73e1b7bc9b00e81075367e97374f2954c05af08e74d22eb`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-59F0E269BB18","canonical":true,"claim_ids":["C-SHORT-WALL-ZERO-CAPACITY"],"claim_statuses":{"C-SHORT-WALL-ZERO-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — short unit-wall zero-capacity theorem

**Date:** 2026-10-05  
**Audit base:** audit.56 main  
**Target:** C-II / embedded-wall refill route  
**Verdict:** **PASS. Promote \`C-SHORT-WALL-ZERO-CAPACITY\`.**  
**LEVEL I STATUS:** still open. C-II remains open.

The audited theorem is exact:

```math
\boxed{
\text{every simple polygonal wall with at most six edges of length }\le1
\text{ has }W_C=\varnothing.
}
```

The proof is independent of all asymptotic Target C machinery.

For an interior candidate $`x`$, every wall vertex has radius $`r_i>1`$. The edge-length bound and cosine law imply each principal angular increment about $`x`$ satisfies

```math
|\theta_i|<\pi/3.
```

But a simple polygon containing $`x`$ has winding number $`\pm1`$, hence the signed angular increments sum to $`\pm2\pi`$. With $`n\le6`$,

```math
2\pi
\le
\sum_i|\theta_i|
<
n\pi/3
\le
2\pi,
```

which is impossible.

The threshold is sharp because the center of a regular unit heptagon lies at distance

```math
1/(2\sin(\pi/7))>1
```

from every wall vertex.

The audit also checked the Target C route consequence against canonical \`C-EMBEDDED-WALL-REFILL\`: that theorem certifies packet points inside the original wall-safe set $`W_C`$, so later deletion of diameter-cover vertices does not create retroactive packet capacity.

Therefore direct refill of the canonical terminal pentagon walls from \`C-PENTAGON-WALL-DISJOINT-BULK\`, while preserving their five boundary contacts, is impossible.

The promoted theorem does not claim that seven-edge walls have positive capacity; the canonical large-wall lock regression explicitly prevents that inference.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.57\`.
