> Generated reading edition · [exact source](../../../../docs/targets/target-c/wrapping-angular-measure-hostile-audit-2026-09-12.md) · source SHA-256 `07ec8374a1bcaa794fbdf793b59010b76ff2b573810a9e632afa133ec02b9507`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — Section 100 wrapping angular-measure hostile audit

**Date:** 2026-09-12  
**Verdict:** PASS as a proof-only theorem; theorem-state promotion remains separate.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit independently re-proves the new Section-100 support-measure inequality by a
different local argument than the antipodal-neighborhood proof in
`100-wrapping-angular-measure-threshold-audit.md`.

The audited conclusion is

```math
|S|\le3\theta-2\pi,
\qquad
\alpha\le {3\theta-2\pi\over2},
```

for every wrapping Type-II attachment limit of angular diameter `theta<pi`. Combined
with canonical Section 96,

```math
\alpha\ge {3\over2}\sin\theta,
```

this gives

```math
3\sin\theta\le3\theta-2\pi
```

and therefore

```math
\lambda\ge
0.9642670742838973\ldots .
```

The five fragile steps were checked separately below.

## 1. Paired-piece indexing is correct

Let the three Section-88 wrapping anchors be `x_1,x_2,x_3` in cyclic order, with
anchor gaps `g_i` from `x_i` to `x_{i+1}`. Put

```math
\delta_i:=\theta-g_i,
\qquad
\phi:=2\pi-2\theta.
```

In gap `g_1`, Section 88 permits support only for length `delta_3` immediately after
`x_1` and length `delta_2` immediately before `x_2`; cyclically the six allowed
pieces have lengths

```math
\delta_1,\delta_1,\delta_2,\delta_2,\delta_3,\delta_3.
```

The two pieces of length `delta_i` are indeed the pieces immediately **before** `x_i`
and immediately **after** `x_{i+1}`. They are outside the two endpoints of anchor gap
`g_i`; they are not the two pieces inside that gap. This is the indexing required by
the paired argument.

## 2. The circular minor-angle alternative keeps both branches

Parameterize the paired pieces by compact sets

```math
A_i,B_i\subset[0,\delta_i],
```

where `a` runs backward from `x_i` and `b` forward from `x_{i+1}`. The clockwise
separation between the corresponding two circle points across gap `g_i` is

```math
q=g_i+a+b=\theta-\delta_i+a+b.
```

Because `0<=q<2pi` and the **minor** angular separation is at most `theta`, one must
have

```math
q\le\theta
\quad\text{or}\quad
q\ge2\pi-\theta.
```

No unwrapping step may discard the second alternative. Substitution gives exactly

```math
a+b\le\delta_i
\quad\text{or}\quad
 a+b\ge\delta_i+\phi.
```

## 3. The reflection sign is one-sided and correct

Set

```math
C_i:=\delta_i-B_i.
```

Writing `c=delta_i-b`, the preceding alternative becomes

```math
a\le c
\quad\text{or}\quad
 a\ge c+\phi.
```

Hence

```math
(A_i-C_i)\cap(0,\phi)=\varnothing.
```

This is deliberately a one-sided difference exclusion. A symmetric exclusion is not
claimed or needed.

## 4. Translation packing removes the factor two

For every fixed `t` with `0<t<phi`, the difference exclusion implies

```math
A_i\cap(C_i+t)=\varnothing.
```

Moreover

```math
A_i\subset[0,\delta_i],
\qquad
C_i+t\subset[t,\delta_i+t].
```

Their disjoint union is therefore contained in an interval of length `delta_i+t`.
Lebesgue measure and translation invariance give

```math
|A_i|+|B_i|
=|A_i|+|C_i+t|
\le\delta_i+t.
```

Sending `t downarrow0` proves

```math
|A_i|+|B_i|\le\delta_i.
```

Summing over the three paired pieces yields

```math
|S|\le\sum_i\delta_i=3\theta-2\pi.
```

This proof works for arbitrary compact, disconnected, or fractal support subsets and
is independent of the antipodal-neighborhood proof in Section 100.

## 5. Finite attachment density really converges to half the angular measure

Let scaled attachment angle sets converge in Hausdorff distance to compact `S` and
write `a_D/D -> alpha` along a subsequence. For every `epsilon>0`, outer regularity and
compactness give a finite union of open angular intervals `U` with

```math
S\subset U,
\qquad
|U|\le|S|+\epsilon.
```

For all large `D`, every attachment angle lies in `U`. Canonical Section 88 equation
(88.8), applied to this fixed finite interval union, gives

```math
a_D
\le
\left({|U|\over2}+o(1)\right)D+O_U(1).
```

The number of interval components is fixed before `D->infinity`, so the additive term
vanishes after division by `D`. Thus

```math
\alpha\le{|U|\over2}
\le{|S|+\epsilon\over2}.
```

Letting `epsilon downarrow0` proves

```math
\alpha\le{|S|\over2}
\le{3\theta-2\pi\over2}.
```

This blocks the only serious compactness regression: `Theta(D)` unit-separated
attachments cannot hide in a zero-measure Hausdorff limit because the fixed open cover
is chosen before the scale limit.

## 6. Scalar step and actual-carrier transfer

Canonical Section 96 gives the independent floor

```math
\alpha\ge {3\over2}\sin\theta.
```

Therefore

```math
3\sin\theta\le3\theta-2\pi.
```

The scalar function

```math
F(\theta)=3\theta-2\pi-3\sin\theta
```

has derivative `3(1-cos theta)>0` on `[2pi/3,pi)`, so it has one root. The independent
regression certificate
`research/verify_target_c_paired_six_cluster_density.py` reproduces

```math
\theta_*=2.6053256746009029\ldots,
\qquad
\mu_*:=\sin(\theta_*/2)=0.9642670742838973\ldots .
```

The Section-88 cap-family argument depends only on excluding wrapping limits below a
fixed threshold. Hence, for every fixed `mu<mu_*`, all shorter macroscopic cell limits
are cap type; the same cap-capacity deficit and Section-83 perimeter/tail budget force
an actual macroscopic harmonic carrier of diameter at least `(mu_*-o(1))D`. Section
83's nonnegative summed local rhombic deficit then selects such a carrier with local
rhombic filling fraction `1-o(1)`.

## 7. Scope and disposition

The proof does not use Cauchy's perimeter inequality, the canonical Section-99
mixed-gap refinement, or conditional Sections 97--98. It depends on canonical Sections
88, 94, and 96 plus the Type-II near-circle attachment packing estimate already used
in Section 88.

The older thresholds remain mathematically valid but are no longer the live Type-II
frontier once Section 100 is promoted:

- Section 96: `0.9362157414...`;
- canonical Cauchy: `0.9370981977...`;
- canonical mixed-gap Cauchy / Section 99: `0.9399896934...`.

**Audit verdict:** PASS. The paired-piece proof independently confirms the support
ceiling and finite-density transfer used in Section 100. A promotion transaction may
therefore treat `100-wrapping-angular-measure-threshold-audit.md` as the canonical
proof and this file as an independent audit.
