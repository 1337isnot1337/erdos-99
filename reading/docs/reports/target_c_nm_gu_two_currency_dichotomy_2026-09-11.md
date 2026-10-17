> Generated reading edition · [exact source](../../../docs/reports/target_c_nm_gu_two_currency_dichotomy_2026-09-11.md) · source SHA-256 `6beeedd7b2e794fb3ed071d43d3e6a6bb9d0ebdef314d377447304656382d0d0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-F2D3436BABEA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — two-currency C-II dichotomy

**Date:** 2026-09-11

**Target:** Target C, C-II

**Status:** unpromoted report-level theorem; route-map status unchanged

**Dependencies:** NM near-matching stability, DB-upgraded force-hull area floor,
ZK attachment-cell cancellation, and the full-source defect localization theorem.

## Result

Every unbounded post-ZF C-II sequence satisfies the diameter/topology defect floor

```math
\boxed{
\liminf\frac{x_B+Q+2s_Z}{D}
\ge c_*:=\frac{2\rho}{3}=0.4927234221\ldots .}
\tag{1}
```

At the same time, writing

```math
\Lambda_D=\frac{e_{BB}+2s_C}{D},
\qquad
G=\operatorname{area}(F)-\sum_r\operatorname{area}(\operatorname{conv}A_r),
```

one has the dichotomy

```math
\boxed{
\limsup\Lambda_D\ge
\lambda_*:=\sqrt{\frac{\sqrt3}{\pi}}=0.7425152492\ldots
}
\tag{2}
```

or, for some $`g>0`$,

```math
\boxed{G\ge gD^2}
\tag{3}
```

along a subsequence. In the second case, after passing to a further subsequence,
either

```math
\operatorname{area}(F\text{ in the outer contact face})ge \frac g2D^2-o(D^2),
\tag{4}
```

or there is a bounded nonquadrilateral face with perimeter at least

```math
\frac{2g}{5}D-o(D).
\tag{5}
```

Thus every survivor simultaneously pays a linear diameter/topology defect and
either a linear pinned/contact surplus or a macroscopic visible cavity/giant face.

This is not a Level-I settlement: no current theorem rules out either alternative.

## Proof

The exact post-ZF incidence identities are

```math
q=x_B+Q+2(d_H+s_Z),
\qquad
r_H:=2h-q=x_B+Q+2s_Z.
\tag{6}
```

The doubled-gap/stopped-train theorem gives

```math
3r_H\ge h-2,
```

and the DB diameter-edge density gives $`h/D\ge2\rho-o(1)`$. Hence (1).

For the attachment-cell term, ZK gives

```math
L_2=6-3(d_H+s_Z)+e_{BB}+2s_C,
\qquad
\sum_r\delta_r\le L_2.
\tag{7}
```

The attachment hulls have disjoint interiors and
$`\operatorname{diam}(A_r)\le\delta_r+2`$. The planar isodiametric inequality
therefore gives

```math
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{8}
```

Since $`d_H+s_Z\ge0`$,

```math
\limsup\frac{L_2}{D}le\limsup\Lambda_D.
\tag{9}
```

The DB-upgraded force-hull theorem gives

```math
\liminf\frac{\operatorname{area}F}{D^2}\ge\frac{\sqrt3}{4}.
\tag{10}
```

Subtracting (8) from (10) yields

```math
\liminf\frac G{D^2}
\ge
\frac{\sqrt3}{4}-\frac\pi4\left(\limsup\Lambda_D\right)^2.
\tag{11}
```

If $`\limsup\Lambda_D<\lambda_*`$, the right side is a positive number $`g`$,
proving (3). Otherwise (2) holds.

Finally, the full-source defect localization gives

```math
G\le H_{out}+A_{exc}+2q,
\tag{12}
```

where $`H_{out}`$ is the outer-face area inside $`F`$, and $`A_{exc}) is the
total exceptional-face area. DB also gives \(Q\le\pi D+O(1)`$, so the total
exceptional-face perimeter is at most $`5\pi D+O(1)`$. If (4) fails, then (12)
forces $`A_{exc}\ge gD^2/2-o(D^2)`$. Isoperimetry and the total perimeter bound
then imply that the largest exceptional face has perimeter at least
$`(2g/5)D-o(D)`$, proving (5). $`\square`$

## Branch interpretation

In the exact $`s_Z=0`$ forest branch, the existing lower bound

```math
\frac{e_{BB}+2s_C}{D}
\ge0.597+3\frac{d_H}{D}+o(1)
```

means that any forest with $`d_H/D\ge0.048506\ldots`$ already lies in alternative
(2). Forests with smaller component density must lie in the cavity/giant-face
alternative unless their surplus independently exceeds $`\lambda_*D`$.



**Source formatting excerpt (unbalanced inline math in the original):**

```text
The cyclic branch is already in alternative (2) by its stronger lower surplus
floor $`0.9955405\ldots D`$, while positive \(s_Z) remains covered only by the
all-branch lower ledgers and has no support-to-motion theorem.
```



## Exact obstruction

The missing implication is a coupling of the two currencies:



**Source formatting excerpt (unbalanced inline math in the original):**

```text
* linear \(x_B+Q+2s_Z\) must force either a surplus above $`\lambda_*D`$ or a
  strict global area loss; and
* a macroscopic outer pocket or giant exceptional face must be incompatible with
  the full source population, including contact-isolated points.
```



Neither implication follows from planarity, density, or a generic response-rank
argument. The report therefore records a branch dichotomy, not a settlement.
