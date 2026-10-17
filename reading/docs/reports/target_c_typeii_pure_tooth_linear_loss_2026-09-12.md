> Generated reading edition · [exact source](../../../docs/reports/target_c_typeii_pure_tooth_linear_loss_2026-09-12.md) · source SHA-256 `2a5d11d07244d4e7ff90e0f97501c0f71b84f7115daed3f5af6ed569cfa7661f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-154DFFB63448","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — Type-II linear loss from the pure-tooth endpoint

**Date:** 2026-09-12
**Classification:** conditional/proof-only quantitative candidate; noncanonical
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note turns the audited-working §142 phase gap into a quantitative
separation from the exact Section-126 triangular-tooth endpoint. It uses the
Type-II loaded-hull-side theorem and the audited §§128 and 130 ledgers. None of
these research-tail modules is canonical theorem-state authority.

## 1. The loss variable

Let $`T_\triangle=\sum_rT_r`$ be the augmented-cell triangular-face count.
Let $`m`$ be the number of nonunit loaded-hull sides, $`Q`$ the global
nonquadrilateral degree excess, $`k=d_H+s_Z`$, $`u_B`$ the outer-walk surplus,
and

```math
r_{\rm deep}:=m-T_\triangle\ge0.
```

Audited-working Type-II loaded-hull-side structure gives $`c_B=0`$ and

```math
e_{BB}=q-m=Q+2k+u_B.
\tag{LT.1}
```

Consequently,

```math
\boxed{
q-T_\triangle
=(q-m)+(m-T_\triangle)
=Q+2k+u_B+r_{\rm deep}.
}
\tag{LT.2}
```

In particular, the exact endpoint $`T_\triangle=q`$ forces all four terms on the
right to vanish.

## 2. Phase-gap payment

Audited-working §142 proves the all-defect Type-II gap

```math
\liminf_{D\to\infty}{T_{\rm train}-q\over D}
\ge
\gamma,\qquad
\gamma:=2\sqrt{\Delta_2}-{\pi\over2}
=0.333829286933018\ldots ,
\tag{LT.3}
```

where $`\Delta_2=\pi/(2\sqrt3)`$. Its exact train ledger is

```math
T_{\rm train}-q=2f-k,
\tag{LT.4}
```

with $`f`$ the number of bounded nonquadrilateral faces. Since every such face
contributes at least one unit to $`Q`$,

```math
f\le Q.
\tag{LT.5}
```

Therefore every Type-II sequence in the audited-working scope satisfies

```math
2Q-k\ge\gamma D-o(D).
\tag{LT.6}
```

Using $`e_{BB}=Q+2k+u_B`$ in the same inequality gives the stronger
loaded-side payment

```math
\boxed{
e_{BB}\ge{\gamma\over2}D+{5\over2}k+u_B-o(D).
}
\tag{LT.6a}
```

Because $`c_B=0`$, every contact counted by $`e_{BB}`$ is an actual unit side of
the loaded convex hull in this Type-II scope. Thus the phase gap forces a
linear exact unit-side population; it cannot be paid entirely by deep nonunit
routes.

## 3. Quantitative endpoint separation

From (LT.6),

```math
Q\ge{\gamma\over2}D+{k\over2}-o(D).
```

Insert this into (LT.2), discarding the other nonnegative terms:

```math
\boxed{
q-T_\triangle
\ge
{\gamma\over2}D+{5\over2}k-o(D).
}
\tag{LT.7}
```

Numerically,

```math
\boxed{
\liminf_{D\to\infty}{q-T_\triangle\over D}
\ge0.166914643466509\ldots .
}
\tag{LT.8}
```

Thus no Type-II sequence covered by the audited-working hypotheses can be
asymptotically pure in the sense $`T_\triangle=q-o(D)`$. The exact endpoint
exclusion is the zero-defect special case; (LT.7) supplies the missing linear
stability currency.

## 4. What this does not yet close

The lower bound in (LT.7) is a defect lower bound, not a contradiction. It does
not show that the forced $`q-T_\triangle`$ defect produces a unit equilateral
triangle or a same-cardinality strict diameter descent. The remaining route must
couple this defect to the canonical Section-122 aggregate detour and Section-123
payment, or prove a finite source-preserving exchange in the resulting
exceptional-face/corridor branch. The macroscopic inactive-container branch is
untouched.
