> Generated reading edition · [exact source](../../../docs/reports/target_c_pinned_stress_face_slack_identity_2026-09-09.md) · source SHA-256 `e5c77bef00b916db78df13e515231ed18e04a9279446887fcf0911068def3259`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FC4F14A8D5FF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — pinned-contact stress surplus is exact planar face slack

**Date:** 2026-09-09  
**Repository base:** current post-ZF report stack / PR #110  
**Run type:** exact cross-ledger identity  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

The C42 quadrangulation-defect theorem states

```math
b+Q\le4q-2c_I-2e_{BB}-4,
```

where `Q=sum_F(deg F-4)` over bounded contact faces. The post-ZF ledger introduces the
pinned-contact stress surplus

```math
s_C=(e-e_{BB})-2(v-q)-c_I\ge0.
```

These are not separate currencies. Euler shows that the entire slack in C42's face
inequality is exactly twice `s_C`.

## Theorem ZL — exact face/stress identity

Every fully force-visible C-II source in the post-C63 normalization satisfies

```math
\boxed{
 b+Q
 =4q-2c_I-2e_{BB}-2s_C-4.
}
\tag{ZL.1}
```

Equivalently,

```math
\boxed{
2s_C
=4q-2c_I-2e_{BB}-4-(b+Q).
}
\tag{ZL.2}
```

### Proof

Euler and face-incidence counting for the connected contact core give

```math
\boxed{
e=2v-2-\frac{b+Q}{2}.}
\tag{ZL.3}
```

The definition of the pinned-contact surplus gives

```math
\boxed{
e=2(v-q)+c_I+e_{BB}+s_C.}
\tag{ZL.4}
```

Equate ZL.3 and ZL.4 and rearrange. `square`

No ZF rank inequality is needed for ZL itself; ZF enters only when this identity is
combined with the later `s_Z,d_H` ledgers.

## Corollary ZL.1 — exact quadrangulation equality criterion

C42's bound is equality if and only if

```math
\boxed{s_C=0.}
```

Thus the zero-surplus branch excluded by ZQ is exactly the branch in which the pinned
contact network saturates C42's planar face-defect inequality after the loaded-loaded
contact term is fixed.

## Corollary ZL.2 — direct expression for the closing defect

The desired Level I face inequality is

```math
b+Q>2h.
```

Insert ZL.1 and `h=q-d_H`:

```math
\begin{aligned}
(b+Q)-2h
&=2q-2c_I-2e_{BB}-2s_C+2d_H-4.
\end{aligned}
```

Using the post-ZF pinned ledger

```math
c_I+e_{BB}+s_C=q-2+d_H+s_Z
```

gives the exact identity

```math
\boxed{
(b+Q)-2h=-2s_Z.
}
\tag{ZL.5}
```

This recovers the known fact that a post-ZF survivor lies on the wrong side of the
closing inequality by exactly `2s_Z`, but it now resolves the contact-side part of
that defect into the geometric C42 face slack `2s_C`.

## Corollary ZL.3 — terminal partition without separate Euler algebra

Write

```math
x_B=b-q,
\qquad
g_F=Q-f.
```

Then `b+Q=q+x_B+f+g_F`. Substitute ZL.1 and the ZU relation for
`c_I+e_BB+s_C`; after cancellation one recovers

```math
\boxed{
q=x_B+f+g_F+2d_H+2s_Z.
}
```

Thus ZT's terminal partition can be viewed as the equality between two exact planar
slack decompositions: C42/pinned-contact slack on one side and diameter/mixed-stress
slack on the other.

## Interpretation

`s_C` has three equivalent exact meanings in the post-ZF framework:

1. extra left-nullity of the pinned contact rigidity matrix beyond one mandatory KKT
   relation per unloaded component;
2. excess component attachment beyond what is explained by Eppstein edge slack, via
   `U=s_C+R_I` from ZK;
3. half the slack in C42's planar boundary/face-defect inequality, via ZL.2.

This removes one bookkeeping ambiguity from the linear-surplus branch. A future bound
on `s_C` can be attacked either through stress-space geometry or directly through the
contact-face decomposition; the two are exactly the same finite currency.

## Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| ZL.1/ZL.2 | proved | Euler plus definition of `s_C`. |
| C42 equality iff `s_C=0` | proved | Immediate. |
| closing defect equals `-2s_Z` | proved | ZL + ZU. |
| positive `s_C` by itself closes Level I | false | It lowers `b+Q`, but ZU forces compensating terminal/mixed currencies. |
| Level I | still open | Need new global/geometric sign information. |

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact identity:
    b+Q = 4q-2c_I-2e_BB-2s_C-4.
Therefore
    2s_C = [C42 upper bound]-(b+Q).
So s_C is exactly half the C42 planar face-defect slack.

Together with ZU and h=q-d_H:
    (b+Q)-2h = -2s_Z.
```
