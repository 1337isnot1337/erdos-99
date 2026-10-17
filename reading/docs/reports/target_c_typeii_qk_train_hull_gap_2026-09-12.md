> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_qk_train_hull_gap_2026-09-12.md) · source SHA-256 `21caac10e3c1e7ae1281572a465994322f44ed154f4a0a5b2f6dff094a62a987`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-31619C9F9537","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Type-II loaded-hull/train coupling

**Date:** 2026-09-12  
**Classification:** corrected proved candidate awaiting promotion; unreviewed and noncanonical  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note combines only canonical Sections 63, 80, and 85. It sharpens the
loaded-hull floor already extracted in the low-response report.

Put

```math
t_D:={q-k\over D},
\qquad
\Delta_2:={\pi\over2\sqrt3},
\qquad
Q=\sum_{F\ {\rm bounded}}(\deg F-4),
```

and let `f` be the number of bounded nonquadrilateral contact faces. In the
full-core Type-II branch, canonical Section 80 gives

```math
{\operatorname{per}(F)\over D}\to\pi,
\qquad
{R_4\over D^2}\to\Delta_2.
\tag{TQ.1}
```

## 1. Two finite inequalities

Section 63 gives the exact identities

```math
b=q+x_B,
\qquad
q-x_B=Q+2k.
\tag{TQ.2}
```

Since the outer contact walk dominates the force-hull perimeter,
`b\ge\operatorname{per}(F)`. Eliminating `x_B` from (TQ.2) gives

```math
Q=2(q-k)-b\le2(q-k)-\operatorname{per}(F).
\tag{TQ.3}
```

Canonical Section 85 gives

```math
q-k+2f\ge2\sqrt{R_4}.
\tag{TQ.4}
```

Every bounded nonquadrilateral face has degree at least five, so its contribution
to `Q` is at least one. Hence

```math
f\le Q.
\tag{TQ.5}
```

## 2. The corrected floor

Define

```math
t_*:={2\over5}\left(\pi+\sqrt{\Delta_2}\right)
=1.6375621841815\ldots .
\tag{TQ.6}
```

We prove

```math
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge t_*.
}
\tag{TQ.7}
```

Take an arbitrary subsequence along which `t_D` converges to a finite limit `t`.
There are two cases.

### Case 1: `t>=2 sqrt(Delta_2)`

Since

```math
2\sqrt{\Delta_2}>t_*,
```

we immediately have `t>=t_*`.

### Case 2: `t<2 sqrt(Delta_2)`

From (TQ.4) and the Type-II rhombus-density limit,

```math
{f\over D}
\ge\sqrt{\Delta_2}-{t\over2}+o(1).
\tag{TQ.8}
```

From (TQ.3) and the force-hull perimeter limit,

```math
{Q\over D}\le2t-\pi+o(1).
\tag{TQ.9}
```

Using `f<=Q` and passing to the limit gives

```math
\sqrt{\Delta_2}-{t\over2}
\le2t-\pi.
```

Rearranging correctly,

```math
\pi+\sqrt{\Delta_2}
\le{5\over2}t,
```

so

```math
\boxed{
t\ge {2\over5}\left(\pi+\sqrt{\Delta_2}\right)=t_*.
}
\tag{TQ.10}
```

Thus every subsequential limit of `t_D` is at least `t_*`, proving (TQ.7).
Equivalently,

```math
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge {2\over5}\left(\pi+\sqrt{\frac\pi{2\sqrt3}}\right)
=1.6375621842\ldots .
}
\tag{TQ.11}
```

This is stronger than the direct half-perimeter floor `\pi/2`; it uses the
first-order train-boundary cost of the rhombic Type-II core.

The previously advertised value

```math
2\sqrt{\Delta_2}=1.9046256137\ldots
```

is **rejected**. It came from the false algebraic rearrangement

```math
\sqrt{\Delta_2}-{t\over2}\le2t-\pi
\quad\not\Longrightarrow\quad
 t\ge {2\pi+2\sqrt{\Delta_2}\over3}.
```

The dated hostile audit
`target_c_typeii_qk_train_hull_gap_hostile_audit_2026-09-12.md` records this regression.

## 3. Scope and remaining gap

The proof is a scalar branch reduction only. It does not assert `q/D\to\pi`,
does not bound `k/D` separately, and does not control the aggregate outer-walk
detour `\sum_r(L_r-2d_r)`. Equality at the corrected floor leaves the same live
interface regime as Section 85: the train boundary can be paid by linear
near-geodesic corridors or exceptional faces. C-II and Level I remain open.
