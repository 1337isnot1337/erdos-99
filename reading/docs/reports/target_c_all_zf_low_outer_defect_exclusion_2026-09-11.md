> Generated reading edition · [exact source](../../../docs/reports/target_c_all_zf_low_outer_defect_exclusion_2026-09-11.md) · source SHA-256 `97ab9c7333d6f8709da06612ca5650983cbbc0bb911f0ffb01cdc3cf7b88b1cc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-07CDEAA9A5DF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — all-ZF exclusion of sublinear outer/face defect

**Date:** 2026-09-11  
**Run type:** exact branch exclusion / train-capacity synthesis  
**Target:** Target C C-II, including `s_Z>0`  
**Status:** report-level conditional theorem; no route-map promotion

## LEVEL I STATUS

`STILL OPEN`.

The low-defect argument in the preceding report was stated only for `s_Z=0`. The
exact post-ZF identities in fact remove that restriction. Conditional on the
audited but still unpromoted FSDB force-hull area theorem, every unbounded C-II
sequence satisfies the explicit positive bound

```math
\boxed{\liminf_{D\to\infty}\frac{x_B+Q}{D}\ge\varepsilon_0,}
\tag{A.1}
```

where `\varepsilon_0` is the positive root of

```math
\frac14\left(\frac\pi2+\frac52\varepsilon\right)^2
 +\frac{37}{4\pi}\varepsilon^2=A_{FS},
\qquad
A_{FS}=\frac{2\rho+\sin(2\rho)}4,
\quad \rho=\cos\rho.
\tag{A.2}
```

Numerically, `\varepsilon_0=0.0008238119818\ldots`. The numerical value is not
needed: (A.2) defines a strictly positive constant because
`A_{FS}>\pi^2/16`.

This excludes `x_B+Q=o(D)` in **all three** ledger branches, including `s_Z>0`.
It does not exclude linear outer/face defect, nor does it close the remaining
high-surplus branch.

## 1. Exact theorem

Let `D_j\to\infty` be a sequence of triangle-free C-II global minimizers in the
post-ZF normal form. Let `x=x_B`, let `Q` be the total bounded-face defect, and
let `f` be the number of bounded nonquadrilateral faces. Assume FSDB.1:

```math
\liminf_j\frac{\operatorname{area}F_j}{D_j^2}\ge A_{FS}.
\tag{A.3}
```

Then (A.1) holds.

### Proof

Put

```math
d_H=q-h,\qquad k=d_H+s_Z.
```

The exact post-ZF incidence identity is

```math
q=x+Q+2k.
\tag{A.4}
```

The stopped-train identity, valid with exceptional faces and arbitrary `s_Z`, is

```math
T=\frac{b+Q}{2}+2f=h-s_Z+2f.
\tag{A.5}
```

Using `h=q-d_H` and `k=d_H+s_Z`, (A.5) becomes

```math
T=q-k+2f
 =\frac q2+\frac x2+\frac Q2+2f.
\tag{A.6}
```

Since every exceptional face contributes at least one to `Q`, `f\le Q`, and since
the loaded vertices are unit-separated vertices of the diameter hull,

```math
q\le\operatorname{per}F\le\pi D.
\tag{A.7}
```

Consequently, with `r=(x+Q)/D`,

```math
\frac TD\le\frac\pi2+\frac{x+5Q}{2D}
\le\frac\pi2+\frac52r.
\tag{A.8}
```

The actual stopped-train crossing graph is simple and triangle-free. Mantel's
theorem therefore gives, for the number `R` of bounded quadrilateral faces,

```math
R\le\frac{T^2}{4}.
\tag{A.9}
```

Every strict unit rhombus has area at most one, so the total quadrilateral area is
at most `R`.

For outer pockets, OP gives `a\le x` missing force-hull sides and

```math
\sum_P k_P=x+2a\le3x.
\tag{A.10}
```

The closing chord has length at most `k_P`, so `\operatorname{per}P\le2k_P` and
the planar isoperimetric inequality gives

```math
\sum_P\operatorname{area}P\le\frac1\pi\sum_P k_P^2
\le\frac{9x^2}{\pi}.
\tag{A.11}
```

For exceptional bounded faces, write `r_i=\deg(F_i)-4`. Then
`\sum_i r_i=Q` and `f\le Q`. C51 makes the faces convex, hence

```math
\sum_i\operatorname{area}F_i
\le\frac1{4\pi}\sum_i(r_i+4)^2
\le\frac{Q^2+24Q}{4\pi}.
\tag{A.12}
```

The augmented contact subdivision partitions the force hull into these pockets,
exceptional faces, and quadrilateral faces. Combining (A.8)--(A.12), and taking
`D_j\to\infty` along any subsequence on which `r_j\to r<\infty`, gives

```math
\limsup_j\frac{\operatorname{area}F_j}{D_j^2}
\le U(r):=\frac14\left(\frac\pi2+\frac52r\right)^2
 +\frac{37}{4\pi}r^2.
\tag{A.13}
```

The term `24Q/(4\pi D^2)` vanishes, and the coefficient `37/(4\pi)` is
`9/\pi+1/(4\pi)`. The function `U` is strictly increasing for `r\ge0`. At
`r=0`,

```math
U(0)=\frac{\pi^2}{16}<A_{FS}.
\tag{A.14}
```

Let `\varepsilon_0` be the unique positive solution of `U(\varepsilon_0)=A_{FS}`.
If a subsequence had `r_j\to r<\varepsilon_0`, (A.13) would contradict (A.3).
Therefore every subsequential limit inferior is at least `\varepsilon_0`, proving
(A.1). `\square`

## 2. Why the `s_Z>0` branch is genuinely covered

The only place where the earlier proof used `s_Z=0` was the replacement
`T=h+2f`. The correct all-branch formula is (A.5), or equivalently (A.6).
The mixed-row surplus reduces `T` through `k=d_H+s_Z`; it cannot increase the
train capacity. At the same time, (A.4) accounts for the corresponding increase
in the number of loaded hull vertices. Thus `T\le\pi D/2+o(D)` in the
sublinear `x+Q` regime remains valid even when `s_Z` is linear.

Contact-isolated source points are retained: they affect neither the train
crossing graph nor the force-hull subdivision, while FSDB itself uses the full
source circumcenter and so does not discard them.

## 3. Dependency and regression audit

| Item | Treatment |
|---|---|
| `s_Z>0` | retained through (A.4)--(A.6), not set to zero |
| cyclic versus forest diameter graph | irrelevant to the train/Mantel bound; both are covered |
| repeated outer-walk edges | charged by OP's `x` and the chain sum (A.10) |
| exceptional faces, including one giant face | charged by the exact quadratic bound (A.12) |
| contact-isolated source points | retained in FSDB; no isolate is assumed in `F` |
| odd shells | not excluded: their `x+Q` is linear, outside (A.1)'s subbranch |
| near-equilateral rhombi | only `\operatorname{area}R\le1` is used |

The FSDB input remains an unpromoted report-level theorem. This report therefore
must not be treated as a promoted unconditional C-II theorem.

## 4. Exact surviving obstruction

The theorem leaves the mandatory regime

```math
x_B+Q\ge\varepsilon_0D-o(D),
\tag{A.15}
```

along with the independent post-ZF surplus constraints on
`e_{BB}+2s_C` and `x_B+Q+2s_Z`. No current theorem gives an upper bound on the
linear area capacity supplied by this defect, nor a global admissible reduction
that removes `s_Z>0`. Consequently (A.1) is not a Level-I settlement.
