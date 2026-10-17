> Generated reading edition · [exact source](../../../docs/reports/target_c_shape_detour_nearglobal_carrier_0988676_2026-09-29.md) · source SHA-256 `9364112f0723c96cc1b0500fe19ce751c657a399405782f8b353fe19dee398df`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6FBE4C3BD01C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — the new shape-detour gap forces a 0.988676 near-global carrier

**Date:** 2026-09-29  
**Base main:** 9a13d56caae2a8cdc156e0c1e4230bb3f2df23d2  
**Status:** proof-only current-main theorem; theorem-state authority unchanged  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Statement

Work in the canonical full-core Type-II branch. Put

```math
S_D:=\sum_r d_r,
\qquad
d_r:=\operatorname{diam}P_r
```

for the actual harmonic attachment cells.

The current-main near-disk chord-dissection theorem gives

```math
\liminf {q-k-S_D\over D}\ge {\pi\over2}-1,
\tag{1.1}
```

while $`q-k\le q\le \operatorname{per}(F)=\pi D+o(D)`$. Hence

```math
\boxed{
\limsup {S_D\over D}\le M_0:=1+{\pi\over2}.
}
\tag{1.2}
```

Let

```math
H(\lambda)
:=2\lambda+4\lambda\sqrt{1-\lambda^2},
\qquad
{\sqrt3\over2}\le\lambda\le1.
\tag{1.3}
```

There is a unique number

```math
\boxed{
\lambda_0\in({\sqrt3\over2},1)
}
```

satisfying

```math
\boxed{
H(\lambda_0)=1+{\pi\over2}.
}
\tag{1.4}
```

Numerically,

```math
\boxed{
\lambda_0=0.988676929088057\ldots .
}
\tag{1.5}
```

Then every full-core Type-II survivor sequence contains, after the usual
subsequence/diagonal selection, an actual locally rhombus-saturated
macroscopic harmonic cell $`P_{*,D}`$ satisfying

```math
\boxed{
{\operatorname{diam}(P_{*,D})\over D}
\ge \lambda_0-o(1).
}
\tag{1.6}
```

More precisely, for every fixed $`\mu<\lambda_0`$, the cells with
$`d_r>\mu D`$ carry total area at least

```math
\boxed{
\bigl(\Gamma(\mu)-o(1)\bigr)D^2,
\qquad
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0,
}
\tag{1.7}
```

where $`\mathcal C(\mu)`$ is the canonical Section-88 cap-family capacity.
At the limiting threshold,

```math
\mathcal C(\lambda_0)=0.6403783202\ldots,
\qquad
\boxed{
\Gamma(\lambda_0)=0.1450198431\ldots .
}
\tag{1.8}
```

The decimal values are orientation only. The theorem is the symbolic
root statement (1.4) together with (1.6)--(1.7).

This raises the live full-core carrier coefficient from the previous
approximately $`0.97624`$ frontier to $`0.9886769\ldots`$.

## 2. Uncapped complement-gap diameter moment

The proof-only all-regime wrapping/two-half-disk theorem and its hostile audit
use only canonical Type-II near-disk/cell-tiling inputs.

Suppose first that a positive-area center-wrapping harmonic-cell sequence has
normalized limit

```math
K=\operatorname{conv}(S)\subset B_{1/2},
\qquad
0\in\operatorname{int}K,
```

with

```math
\lambda:=\operatorname{diam}K<1.
```

Write the complement gaps of the circle support $`S`$ as $`g_j\in(0,\pi)`$.
The hostile-audited complement-gap filling argument gives

```math
\liminf {1\over D}\sum_{r\ne w}d_r
\ge
C(K):=\sum_j\sin(g_j/2).
\tag{2.1}
```

Canonical Section 101 applies to the same wrapping support. Put

```math
\theta:=2\arcsin\lambda.
```

Its complement-chord theorem gives

```math
C(K)
\ge
\sin(\theta/2)+2\sin\theta
=
\lambda+4\lambda\sqrt{1-\lambda^2}.
\tag{2.2}
```

The wrapping carrier contributes $`\lambda D+o(D)`$. Therefore

```math
\boxed{
\liminf {S_D\over D}
\ge
H(\lambda)
=
2\lambda+4\lambda\sqrt{1-\lambda^2}.
}
\tag{2.3}
```

No common cell-diameter cap is used in (2.1)--(2.3).

## 3. Monotonicity and the new threshold

Every center-wrapping support with diameter below one has

```math
\lambda\ge{\sqrt3\over2}.
```

Put

```math
y:=\sqrt{1-\lambda^2}\in(0,1/2].
```

Differentiating (1.3),

```math
H'(\lambda)
=
2+4y-{4\lambda^2\over y}
=
2+8y-{4\over y}.
\tag{3.1}
```

The function on the right is increasing in $`y`$. At $`y=1/2`$ it equals
$`-2`$. Hence

```math
\boxed{
H'(\lambda)<0
\quad
({\sqrt3\over2}\le\lambda<1).
}
\tag{3.2}
```

Also

```math
H({\sqrt3\over2})=2\sqrt3>1+{\pi\over2},
\qquad
H(1)=2<1+{\pi\over2}.
```

Thus (1.4) has a unique root.

Now combine (2.3) with the current-main upper moment bound (1.2). Any fixed
center-wrapping limit with $`\lambda<1`$ must satisfy

```math
H(\lambda)\le M_0.
```

By strict monotonicity,

```math
\boxed{
\lambda\ge\lambda_0.
}
\tag{3.3}
```

A center-wrapping diameter-one limit already satisfies (3.3).

## 4. The no-wrapping alternative cannot evade the threshold

The hostile-audited all-regime Type-II dichotomy says that after a subsequence
either

1. there is a positive-area center-wrapping cell limit; or
2. the leading cell area splits into two complementary half-disk cap groups,
   each with an actual defining harmonic-cell sequence of normalized diameter
   tending to one.

The second alternative already contains actual cells with

```math
d_r/D\to1>\lambda_0.
```

Thus every Type-II subsequence has a further subsequence containing an actual
harmonic cell of normalized diameter at least $`\lambda_0-o(1)`$.

This qualitative observation alone does not yet guarantee that the selected
long cell carries quadratic area. Section 5 supplies that strengthening.

## 5. Positive area at the new threshold

Fix any

```math
\mu<\lambda_0.
```

Consider the harmonic cells with

```math
d_r\le\mu D.
```

Any positive-area macroscopic limit of such a cell cannot be center-wrapping:
if it were, Section 3 would require normalized diameter at least
$`\lambda_0>\mu`$. Therefore all positive-area macroscopic limits in this
short-cell family are cap type.

Canonical Section 88's laminar cap-family capacity theorem applies exactly to
this family and gives

```math
\limsup {1\over D^2}
\sum_{d_r\le\mu D}\operatorname{area}(P_r)
\le
\mathcal C(\mu)
<
{\pi\over4}.
\tag{5.1}
```

Canonical full-core cell-area saturation gives

```math
\sum_r\operatorname{area}(P_r)
=
\left({\pi\over4}-o(1)\right)D^2.
```

Subtracting (5.1),

```math
\boxed{
\sum_{d_r>\mu D}\operatorname{area}(P_r)
\ge
\bigl(\Gamma(\mu)-o(1)\bigr)D^2,
}
\tag{5.2}
```

where

```math
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
```

This proves (1.7).

For reference, when
$`\theta_\mu=2\arcsin\mu`$,

```math
\mathcal C(\mu)
=
{1\over8}
\left[
2\pi-k_\mu\sin\theta_\mu-\sin r_\mu
\right],
```

```math
k_\mu=\left\lfloor{2\pi\over\theta_\mu}\right\rfloor,
\qquad
r_\mu=2\pi-k_\mu\theta_\mu.
\tag{5.3}
```

At $`\mu=\lambda_0`$, $`k_\mu=2`$, and evaluating the exact formula gives
the orientation values in (1.8).

## 6. Select one actual locally rhombus-saturated carrier

Canonical Section 83 gives

```math
\sum_r\operatorname{per}(P_r)=O(D).
\tag{6.1}
```

Every convex cell satisfies

```math
\operatorname{per}(P_r)\ge2d_r.
```

Hence, for fixed $`\mu>0`$, the number of cells with $`d_r>\mu D`$ is
bounded independently of $`D`$.

Together with (5.2), this implies that for every fixed
$`\mu<\lambda_0`$, at least one long cell has

```math
\operatorname{area}(P_r)\ge c_\mu D^2
\tag{6.2}
```

for a constant $`c_\mu>0`$.

The canonical local filling deficits are nonnegative and obey

```math
\sum_r\left(
\operatorname{area}(P_r)-A_{4,r}
\right)
=o(D^2).
\tag{6.3}
```

Since only $`O_\mu(1)`$ long cells are present and they carry
$`\Omega_\mu(D^2)`$ total area, one can select an actual long cell with
quadratic area and local strict-rhombus filling ratio tending to one.

Choose a sequence $`\mu_j\uparrow\lambda_0`$, then perform the standard
finite diagonal selection. This produces one actual cell sequence
$`P_{*,D}`$ with

```math
{\operatorname{diam}(P_{*,D})\over D}
\ge\lambda_0-o(1),
```

quadratic area, and

```math
{A_{4,*}\over\operatorname{area}(P_{*,D})}\to1.
```

This proves (1.6).

## 7. Frontier effect

The full-core carrier handoff is now

```math
\boxed{
d_*/D\ge0.988676929088\ldots-o(1)
}
```

rather than the previous roughly $`0.97624`$ coefficient.

The improvement is not another optimization of the old Section-101 scalar
window. It comes from composing three different geometric facts:

```math
\text{global cell-shape detour}
\Longrightarrow
S_D/D\le1+\pi/2,
```

```math
\text{wrapping complement-gap filling}
\Longrightarrow
S_D/D\ge H(\lambda),
```

```math
\text{cap-family capacity}
\Longrightarrow
\text{quadratic area on cells above every }\mu<\lambda_0.
```

The remaining full-core problem is correspondingly narrower:

```math
\boxed{
0.988676929088\ldots
\le d_*/D\le1.
}
\tag{7.1}
```

A closing argument must now attack a genuinely near-global, locally
rhombus-saturated carrier, or the two-half-disk diameter-one alternative.

## 8. Scope audit

- The current-main input (1.1) is the proof-only near-disk
  chord-dissection shape-detour theorem already pushed on main.
- The wrapping/two-half-disk dichotomy is proof-only but has an independent
  hostile audit passing its stated Type-II scope.
- The uncapped complement-gap filling theorem used in (2.1) is the
  hostile-audited mechanism behind the Section-130 / near-global-carrier
  research chain. It does not use a common diameter cap after the wrapping
  carrier is selected.
- Canonical Section 101 supplies only the support-gap inequality (2.2).
- Canonical Sections 83 and 88 supply cell-area saturation, total cell
  perimeter $`O(D)`$, local filling-deficit summability, and cap-family
  capacity.
- Contact-isolated source points are retained.
- No KKT coefficient floor, source/scaffold substitution, Reuleaux-cap
  inference, or full-source affine-kernel extension is used.
- No computation is load-bearing.
- The theorem-state manifest is unchanged.

**Disposition:** proof-only current-main carrier theorem. C-II and Level I
remain open.
