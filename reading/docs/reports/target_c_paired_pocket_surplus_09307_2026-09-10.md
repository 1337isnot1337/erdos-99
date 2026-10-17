> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_pocket_surplus_09307_2026-09-10.md) · source SHA-256 `a26dfb2012f485557e8bd8c5eebbb359d42f3aad9683558830d026b05d1aaea1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-65020AB0EE7D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — opposite-pocket pairing raises the post-ZF surplus floor above 0.930749

**Date:** 2026-09-10  
**Repository state:** branch `research/c99-c2-dpc-20260910-sol` after the DIDO and midpoint-polygon commits; contemporaneous `main` head `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Run type:** closing proof / global convex-geometric coupling / endpoint exclusion  
**Target:** Target C, C-II after ZF/FS/MP  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** no theorem imported  
**Computation:** decimal evaluation of an analytically unique scalar root only

## LEVEL I STATUS

`STILL OPEN`

The midpoint-polygon theorem

```math
d_H\left(F-o,\frac12P_H\right)=o(D)
```

has a stronger consequence than endpoint exclusion. Because `P_H/2` is centrally symmetric and all force-hull vertices lie in the FS radial annulus `D/2+o(D)`, every macroscopic force-hull side has an asymptotically equal opposite side. Thus macroscopic outer pockets occur in opposite chord-pairs.

Two new asymptotic bounds follow.

First, if

```math
\lambda=\lim\frac{e_{BB}+2s_C}{D}<1,
```

then the force-hull area satisfies

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
A(\lambda):=
\frac{\pi-r_\lambda+\sin r_\lambda}{4},
\qquad
r_\lambda=2\arcsin(\lambda/2).
}
\tag{PP.1}
```

Second, opposite outer pockets can be glued across equal limiting chords. The planar isoperimetric inequality then halves the previous universal reflection coefficient:

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac1{4\pi}
\left(\limsup\frac{d_P}{D}\right)^2.
}
\tag{PP.2}
```

Including exceptional faces and the GU attachment cells gives the necessary inequality

```math
A(\lambda)
\le
\left(\frac\pi4+\frac1{4\pi}\right)\lambda^2.
\tag{PP.3}
```

Its unique root in `(0,1)` is

```math
\boxed{
\lambda_{PP}=0.9307496328725488\ldots .
}
\tag{PP.4}
```

Moreover the equality endpoint is impossible: equality in PP.1 uses one macroscopic projective gap whose two opposite hull sides already consume all `d_P` mass, leaving asymptotically zero pocket detour, while PP.3 requires a positive quadratic cavity. Therefore there exist absolute `epsilon_PP>0` and `D_0` such that every sufficiently large post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{PP}+\epsilon_{PP}.
}
\tag{PP.5}
```

The gap is nonexplicit. Level I remains open above it.

## 1. Starting data

Use the C-II lexicographic source, FS.4, DB/PC, and the finite midpoint-polygon theorem MP:

```math
\boxed{
d_H\left(F-o,Q_D\right)\le L_D=o(D),
\qquad Q_D:=\frac12P_H.}
\tag{1.1}
```

Every vertex of `Q_D` has radius exactly `D/2`; every force-hull vertex has radius

```math
D/2+o(D)
\tag{1.2}
```

uniformly. The polygon `Q_D` is centrally symmetric.

For the projective diameter-direction gaps write

```math
\gamma_1,\ldots,\gamma_h,
\qquad
\sum_i\gamma_i=\pi.
\tag{1.3}
```

Its area identity is

```math
\boxed{
\frac{area(Q_D)}{D^2}
=\frac14\sum_i\sin\gamma_i.
}
\tag{1.4}
```

For the OP outer pockets write chain length `ell_P`, hull-side chord `s_P`, and

```math
x_P=\ell_P-2,
\qquad
\sum_Px_P=d_P.
\tag{1.5}
```

PC gives

```math
d_P+Q\le e_{BB}\le e_{BB}+2s_C.
\tag{1.6}
```

## 2. Macroscopic side pairing

### Lemma PP.1 — every macroscopic force-hull side has an opposite mate

Consider any unbounded C-II sequence and any sequence of force-hull sides with lengths

```math
s_D/D\to c>0.
```

After passage to a subsequence, there is a distinct force-hull side in the opposite boundary sector with length

```math
s_D'/D\to c.
```

#### Proof

Normalize by `D` and translate by `o`. By compactness take a Hausdorff limit of `Q_D/D`; call it `Q_infty`. Equation (1.1) gives the same limit for `(F-o)/D`. Since every `Q_D` is centrally symmetric, so is `Q_infty`.

The endpoints of the given force-hull sides have radii tending to `1/2`. Pass to limits `u,v`, with `|u-v|=c>0`. Supporting normals of the sides also have a convergent subsequence, so `[u,v]` is an exposed side of `Q_infty`. Central symmetry makes `[-u,-v]` an opposite exposed side of the same length.

The radial flat-side transfer lemma MP.3 applies to this opposite limiting side: Hausdorff closeness and the uniform radial annulus forbid force-hull vertices from filling the interior of the limiting chord. Hence an actual side of `F` crosses the opposite side sector and has length `cD+o(D)`. `square`

Every such side has length greater than one for large `D`, so it is a missing force-hull contact side and determines an OP outer pocket. Thus macroscopic OP chords are paired with asymptotically equal opposite chords.

## 3. Force-hull area from the available pocket-side budget

For a projective gap `gamma`, the corresponding side of `Q_D` has length

```math
D\sin(\gamma/2).
\tag{3.1}
```

A positive limiting gap therefore gives two opposite force-hull sides of the same asymptotic length. Their two OP chain lengths are at least their chord lengths. Consequently, if `r_j>0` are the positive limiting macroscopic projective gaps along a subsequence, then

```math
\boxed{
2\sum_j\sin(r_j/2)
\le
\tau:=\liminf\frac{d_P}{D}.
}
\tag{3.2}
```

The force-hull area deficit from the disk is carried only by these macroscopic gaps. Indeed, for gaps below `epsilon`,

```math
0\le\gamma-\sin\gamma\le\frac{\epsilon^2}{6}\gamma,
```

so their total deficit tends to zero as `epsilon downarrow0`. Using MP.1 and (1.4),

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
\frac14\left[
\pi-\sum_j(r_j-\sin r_j)
\right].
}
\tag{3.3}
```

We now optimize the right side under (3.2). Put

```math
c=2\sin(r/2),
\qquad
\varphi(c):=r-\sin r
=2\arcsin(c/2)-c\sqrt{1-c^2/4}.
\tag{3.4}
```

For `0<c<2`,

```math
\varphi'(c)
=\frac{c^2}{2\sqrt{1-c^2/4}},
\tag{3.5}
```

so `varphi` is strictly increasing and strictly convex, with `varphi(0)=0`. Hence it is superadditive on every interval on which the summed argument remains below `2`:

```math
\varphi(c_1)+\varphi(c_2)
\le\varphi(c_1+c_2).
\tag{3.6}
```

For `lambda<1`, (1.6) and (3.2) give

```math
\sum_j c_j\le\tau\le\lambda<1.
```

Repeated use of (3.6) therefore gives

```math
\sum_j(r_j-\sin r_j)
\le
\varphi(\lambda).
\tag{3.7}
```

With

```math
r_\lambda=2\arcsin(\lambda/2),
```

substitution into (3.3) proves PP.1.

### Equality structure

The inequality is strict unless all macroscopic gap-cost concentrates in one projective gap and the side budget is saturated. Thus if `area(F)/D^2 -> A(lambda)` with fixed `0<lambda<1`, then

```math
\frac{d_P}{D}\to\lambda,
\tag{3.8}
```

there is one macroscopic projective gap

```math
r\to r_\lambda,
\tag{3.9}
```

and all other macroscopic gap-cost vanishes. The single projective gap appears twice antipodally in `Q_D`, so it forces two opposite force-hull sides of lengths

```math
\boxed{
\left(\frac\lambda2+o(1)\right)D
}
\tag{3.10}
```

each.

## 4. Opposite-pocket isoperimetry

### Lemma PP.2 — equal-chord pocket pair

Let two convex pockets have the same chord length `s` and old-chain lengths `ell_1,ell_2`. Then

```math
\boxed{
area(P_1)+area(P_2)
\le
\frac{(\ell_1+\ell_2)^2}{4\pi}.
}
\tag{4.1}
```

#### Proof

Rigidly align the two chords and place the pockets on opposite sides of the common chord. The two old boundary chains then form a rectifiable Jordan curve: the common chord is internal and disappears. Its perimeter is `ell_1+ell_2`, and its enclosed area is exactly `area(P_1)+area(P_2)`. The planar isoperimetric inequality proves (4.1). `square`

If the two chord lengths differ by `o(D)`, scaling one pocket by a factor `1+o(1)` equalizes the chords and changes its chain length by `o(D)` and area by `o(D^2)`. Thus (4.1) remains valid asymptotically for the opposite pairs supplied by PP.1.

For a macroscopic pocket whose chord is `o(D)`, the sharp Dido theorem gives

```math
area(P)
\le
\left(\frac1{4\pi}+o(1)\right)\ell_P^2,
\tag{4.2}
```

because the Dido parameter tends to `theta=pi` when `s_P/ell_P->0`.

### Theorem PP.3 — paired outer-pocket capacity

Along every post-ZF sequence with

```math
\frac{d_P}{D}\to\tau,
```

one has

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le\frac{\tau^2}{4\pi}.
}
\tag{4.3}
```

#### Proof

Fix `epsilon>0` and discard pockets with `x_P<epsilon D`. Their total area is `O(epsilon D^2)+O(D)` by the reflection bound exactly as in DI.3.

Only `O_epsilon(1)` macroscopic-chain pockets remain. Pass to a subsequence so all normalized chain and chord lengths converge. Pair every positive limiting chord by PP.1. Apply (4.1) to each pair, with an `o(D^2)` error for the asymptotically equal chords. Apply (4.2) to every remaining zero-chord macroscopic pocket.

If the normalized chain masses of the resulting disjoint groups are `m_1,...,m_k`, then

```math
\limsup\frac{H_{out}}{D^2}
\le
\frac1{4\pi}\sum_jm_j^2+O(\epsilon).
```

The total macroscopic chain mass is at most `tau+o(1)`, because `ell_P=x_P+2` and there are only `O_epsilon(1)` retained pockets. Hence

```math
\sum_jm_j^2\le\left(\sum_jm_j\right)^2\le\tau^2.
```

Let `epsilon downarrow0`. This proves (4.3). `square`

## 5. Exceptional faces do not increase the paired capacity

Let

```math
\nu=\lim Q/D.
```

PC gives

```math
\tau+\nu\le\lambda.
```

PP.3 and the exceptional-face bound give

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{(\lambda-\nu)^2+\nu^2}{4\pi}
\le
\frac{\lambda^2}{4\pi},
\tag{5.1}
```

because `0<=nu<=lambda`. ZG therefore yields the clean global cavity ceiling

```math
\boxed{
\limsup\frac G{D^2}
\le\frac{\lambda^2}{4\pi}.
}
\tag{5.2}
```

This no longer uses a diameter-detour scalar optimization.

## 6. Whole-source comparison and the explicit threshold

GU bounds the attachment-cell area by

```math
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\lambda^2.
\tag{6.1}
```

Since

```math
area(F)=G+C_{att},
```

(5.2)-(6.1) give

```math
\limsup\frac{area(F)}{D^2}
\le
\left(\frac\pi4+\frac1{4\pi}\right)\lambda^2.
\tag{6.2}
```

For any hypothetical subsequence with `lambda<1`, PP.1 gives the opposite lower bound. Hence every such survivor limit must satisfy PP.3:

```math
\boxed{
A(\lambda)
\le
B\lambda^2,
\qquad
B:=\frac\pi4+\frac1{4\pi}.
}
\tag{6.3}
```

Put

```math
H(\lambda):=A(\lambda)-B\lambda^2.
```

For

```math
r_\lambda=2\arcsin(\lambda/2),
```

one has

```math
A'(\lambda)
=-\frac{\lambda^2}{8\sqrt{1-\lambda^2/4}}<0.
\tag{6.4}
```

Thus `H` is strictly decreasing on `(0,1)`.

Also `H(0)=pi/4>0`, while at `lambda=1`,

```math
A(1)=\frac\pi6+\frac{\sqrt3}{8}
<\frac\pi4+rac1{4\pi}=B.
```

The last strict inequality follows already from `pi>3` and `sqrt3<2`:

```math
B-A(1)
=rac\pi{12}+rac1{4\pi}-rac{\sqrt3}{8}>0.
```

Therefore there is a unique root

```math
\boxed{\lambda_{PP}\in(0,1)}
```

of

```math
\boxed{
\frac{\pi-2\arcsin(\lambda/2)
+\lambda\sqrt{1-\lambda^2/4}}{4}
=
\left(\frac\pi4+\frac1{4\pi}\right)\lambda^2.
}
\tag{6.5}
```

Numerically,

```math
\boxed{\lambda_{PP}=0.93074963287254879100\ldots .}
\tag{6.6}
```

Equation (6.3) is impossible below this root. Thus

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_{PP}.
\tag{6.7}
```

## 7. The `lambda_PP` endpoint is impossible

Assume an unbounded survivor sequence has

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_{PP}.
\tag{7.1}
```

Every inequality in the chain PP.1 -> (6.2) -> (6.5) must then be asymptotically sharp.

Because `A(lambda)` is strictly decreasing, the actual pocket-side budget must satisfy

```math
\frac{d_P}{D}\to\lambda_{PP}.
\tag{7.2}
```

Equality in the convex concentration step (3.7) forces one macroscopic projective gap `r_lambda`, and its two antipodal force-hull sides have lengths

```math
\left(\frac{\lambda_{PP}}2+o(1)\right)D
```

each. Their two OP chains therefore have combined length at least

```math
(\lambda_{PP}+o(1))D.
\tag{7.3}
```

But the total macroscopic chain length is at most `d_P+o(D)`, hence at most the same quantity. Thus both chains have asymptotically zero detour:

```math
(\ell_1-s_1)+(\ell_2-s_2)=o(D),
\tag{7.4}
```

and every other macroscopic pocket chain has total length `o(D)`.

DPC.1 or the sharp Dido theorem then gives

```math
H_{out}=o(D^2).
\tag{7.5}
```

Also (1.6) and (7.2) force `Q/D->0`, so

```math
A_{exc}=o(D^2).
\tag{7.6}
```

Hence ZG gives

```math
G=o(D^2).
\tag{7.7}
```

On the other hand, PP.1 and GU give

```math
\liminf\frac G{D^2}
\ge
A(\lambda_{PP})-rac\pi4\lambda_{PP}^2
=
\frac{\lambda_{PP}^2}{4\pi}>0,
\tag{7.8}
```

where the equality is the defining equation (6.5). Contradiction.

Therefore no `lambda_PP` endpoint sequence exists.

### Corollary PP.4 — uniform gap above the explicit root

There exist absolute constants `epsilon_PP>0` and `D_0<infinity` such that every post-ZF survivor with `D>=D_0` satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{PP}+\epsilon_{PP}.
}
\tag{7.9}
```

The sequential proof is identical to MPE.1: otherwise choose a sequence converging down to `lambda_PP`, contradicting Section 7.

## 8. Exact target implication

The report-level surplus frontier has moved in this run from

```math
0.5882283\ldots\to0.7739547\ldots\to0.8316870\ldots
```

and now to the uniform statement

```math
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.9307496328725488\ldots+\epsilon_{PP}
}
```

for all sufficiently large post-ZF survivors, for some absolute nonexplicit `epsilon_PP>0`.

This is not a repeated scalar iteration. PP.1 and PP.3 use the full-source FS midpoint geometry to couple diameter-direction gaps to actual outer-pocket chords and to pair opposite pockets.

The shortest remaining Level I implication is a high-surplus upper/global incompatibility. Any universal post-ZF upper bound

```math
\limsup\frac{e_{BB}+2s_C}{D}
\le0.9307496328\ldots
```

would now close C-II immediately.

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| macroscopic side pairing PP.1 | proved asymptotically | MP Hausdorff theorem + FS radial annulus + central symmetry |
| side-budget area floor PP.1 | proved asymptotically | projective gap area identity + paired side cost + convex concentration |
| equal-chord pair inequality PP.2 | proved finite | glue chains and apply isoperimetry |
| paired cavity PP.3 | proved asymptotically | large/small pocket split + opposite pairing + zero-chord Dido limit |
| exceptional faces cannot increase coefficient | proved | elementary quadratic inequality |
| explicit root `0.9307496328...` | proved as unique analytic threshold; decimal evaluated numerically | monotone scalar equation |
| endpoint exclusion | proved | equality forces two taut opposite pocket chains and zero quadratic cavity |
| uniform nonexplicit gap | proved | sequential compactness contradiction |
| Level I | still open | no contradictory high-surplus upper bound yet |

## 10. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its force hull and diameter-direction polygon are disk-like; PP does not infer a triangle from that local shell geometry |
| dense isolated fillings | yes | FS supplies the common center from the full source; isolates are never discarded |
| giant pocket with microscopic chord | yes | sharp Dido tends to the coefficient `1/(4pi)`, exactly the zero-chord term retained in PP.3 |
| giant pocket with macroscopic chord | yes | it is paired with an opposite macroscopic pocket by MP/FS and is bounded by the glued-pair isoperimetric inequality |
| many microscopic direction gaps | yes | their area deficit is bounded by `sum(gamma-sin gamma)=o(1)` after the epsilon truncation |
| exceptional face concentration | yes | `Q^2/(4pi)` is retained and combined with the reduced outer-pocket budget |

The shell regressions still lack the full-source global-minimum comparison behind GU/FS; PP's geometric inequalities alone do not claim to exclude them.

## 11. Failed routes and no-go results

1. The unpaired reflection coefficient `1/(2pi)` throws away the opposite-side structure forced by FS/MP and is off by a factor two at the group level.
2. A force-hull area bound based only on `h/D` ignores the much tighter side-length budget `d_P/D<=lambda`.
3. Exact endpoint equality is much more rigid than the scalar bound suggests: the side budget and pocket area cannot saturate simultaneously.

## 12. Canonical promotion recommendation

**Hold as report pending independent audit.** PP.2 is a clean finite lemma. PP.1/PP.3 and the threshold depend on the unpromoted FS/MP/PC/DB/GU/ZG report stack and should be promoted only after that chain is reviewed.

## 13. Next run

Use the exact PC identities to seek a universal upper bound on `lambda=e_BB+2s_C` from the planar loaded-contact embedding, now that any bound below `0.93075 D` closes C-II. In parallel, quantify the endpoint incompatibility in Section 7: a positive pocket detour needed for quadratic cavity consumes chain mass beyond the two opposite side chords, so a direct side-plus-detour inequality may raise the explicit threshold further, potentially past `1`.

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

MP/FS pairs every macroscopic force-hull side with an opposite side.
If lambda=(e_BB+2s_C)/D<1, then d_P/D<=lambda and every macroscopic projective gap r
costs two pocket chords of total normalized length 2sin(r/2). Since
    varphi(c)=2asin(c/2)-c sqrt(1-c^2/4)
is convex in c, all force-hull area deficit is maximized by one gap at total cost lambda:
    area(F)/D^2 >= A(lambda)
      =[pi-r_lambda+sin r_lambda]/4,
    r_lambda=2asin(lambda/2).

Opposite pockets with equal chord glue to a Jordan curve, so
    area(P1)+area(P2)<=(ell1+ell2)^2/(4pi).
Zero-chord giant pockets have the same limiting coefficient by sharp Dido.
Hence
    H_out/D^2 <= (d_P/D)^2/(4pi),
and after Q optimization
    G/D^2 <= lambda^2/(4pi).
GU gives attachment cells <=pi lambda^2/4, so every survivor needs
    A(lambda)<=(pi/4+1/(4pi))lambda^2.
The unique root is
    lambda_PP=0.9307496328725488... .

Equality is impossible: the one macroscopic projective gap creates two opposite hull
sides of length (lambda_PP/2)D each, consuming all d_P chain mass with zero detour,
so H_out=o(D^2) and Q=o(D), while the root equation requires
    G/D^2 -> lambda_PP^2/(4pi)>0.
Therefore some absolute epsilon_PP>0 exists with
    (e_BB+2s_C)/D >= lambda_PP+epsilon_PP
for all sufficiently large post-ZF survivors.
```
