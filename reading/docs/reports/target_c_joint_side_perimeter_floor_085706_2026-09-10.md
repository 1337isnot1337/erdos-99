> Generated reading edition · [exact source](../../../docs/reports/target_c_joint_side_perimeter_floor_085706_2026-09-10.md) · source SHA-256 `86210b0e04c4bcfa7deaac90a296efa4ecea16084d12b3a1a125bc41bf1a4524`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 3 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-209A4321A2B8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_joint_side_perimeter_floor_085706_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=6e3f48bbc5d7674158899a80a9a40cafc434accd; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — joint side/perimeter budget raises the all-phase renormalized floor to 0.857065

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after SC/SCE  
**Run type:** exact joint-budget optimization  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

The previous SC theorem raised the explicit all-phase renormalized lower endpoint to
`0.83644...` and excluded equality.  SC still optimized the pocket/face currency and
the macroscopic force-side cost through separate upper bounds.  This report keeps the
same diameter-component choice in both budgets and obtains a stronger exact tradeoff.

The result is the closed-form threshold

```math
\boxed{
\liminf\mu_D\ge\mu_0,
\qquad
\mu_0:=
\frac{2\pi\bigl(3\sqrt{2\pi^2+1}-1\bigr)}{9\pi^2+4}
=0.857065063182212\ldots .
}
\tag{JS.1}
```

The decimal is diagnostic.  The proof gives the exact rational bracket

```math
\boxed{0.857<\mu_0<0.86.}
\tag{JS.2}
```

The theorem uses no numerical optimizer.

---

## 1. Variables and the joint side/pocket budget

Pass to a convergent post-ZF subsequence and write

```math
\mu=\lim\mu_D,
\qquad
x=\lim\frac{d_P+Q}{D},
\qquad
y=\lim\frac hD,
```

```math
d=\lim\frac{d_H}{D},
\qquad
s=\lim\frac{s_Z}{D}.
```

The exact PC/RPE identities imply

```math
x\le\mu+d+s
\tag{1.1}
```

and

```math
x\le y-d-2s.
\tag{1.2}
```

Twice (1.1) plus (1.2) gives

```math
\boxed{3x\le2\mu+y+d.}
\tag{1.3}
```

Now let `C` be the total normalized chord cost of all positive limiting macroscopic
projective gaps.  As in SC, a projective gap `r` creates two opposite actual force-hull
sides with total normalized length

```math
2\sin(r/2).
```

Every force-hull side has length at least one.  If the `q` force-hull vertices are
listed cyclically with side lengths `ell_i`, then exactly

```math
P_F-q=\sum_{i=1}^q(\ell_i-1).
\tag{1.4}
```

A fixed macroscopic side contributes its normalized length to the right side up to
`o(1)`.  Therefore

```math
C\le\liminf\frac{P_F-q}{D}.
\tag{1.5}
```

Cauchy's perimeter-diameter inequality gives `P_F<=pi D`, while `q=h+d_H`.  Hence

```math
\boxed{C\le\pi-y-d.}
\tag{1.6}
```

Add (1.3) and (1.6):

### Theorem JS.1 — joint pocket/side budget

```math
\boxed{
3x+C\le2\mu+\pi.
}
\tag{JS.3}
```

Also every macroscopic force-side chord is paid by its OP contact chain, so

```math
\boxed{0\le C\le d_P/D\le x.}
\tag{1.7}
```

Consequently, with

```math
B:=2\mu+\pi,
```

```math
\boxed{
0\le C\le B/4,
\qquad
x\le(B-C)/3.
}
\tag{1.8}
```

This is the key improvement: `x` and `C` cannot independently take their separate
maxima.

---

## 2. Force-area lower and cavity upper bounds

SC proves the force-side area lower bound

```math
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
A(C):=\frac{\pi-\varphi(C)}4,
}
\tag{2.1}
```

where, for `0<=C<2`,

```math
\varphi(C)
=2\arcsin(C/2)-C\sqrt{1-C^2/4}.
\tag{2.2}
```

The RP paired-pocket and exceptional-face estimates give

```math
\limsup\frac G{D^2}
\le\frac{x^2}{4\pi}.
\tag{2.3}
```

GR/ZK gives

```math
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\mu^2.
\tag{2.4}
```

Since `area(F)=C_att+G`, equations (1.8), (2.1)-(2.4) imply that every survivor limit
with `mu<0.86` must have some `C in [0,B/4]` satisfying

```math
\boxed{
A(C)
\le
\frac\pi4\mu^2+
\frac{(B-C)^2}{36\pi}.
}
\tag{JS.4}
```

We now show that throughout the relevant range the easiest value is exactly `C=0`.

---

## 3. `C=0` is the global minimizing side cost

Define the left-minus-right gap

```math
H_\mu(C)
:=
A(C)-\frac\pi4\mu^2-\frac{(B-C)^2}{36\pi}.
\tag{3.1}
```

Subtract its value at zero:

```math
\boxed{
D_\mu(C):=H_\mu(C)-H_\mu(0)
=-\frac{\varphi(C)}4
+
\frac{C(2B-C)}{36\pi}.
}
\tag{3.2}
```

Since `varphi` is convex, `-varphi/4` is concave; the quadratic term is strictly
concave.  Thus

```math
\boxed{D_\mu\text{ is concave on }[0,B/4].}
\tag{3.3}
```

Also `D_mu(0)=0`.  It remains only to show the other endpoint is positive.

Put

```math
C_*=B/4.
```

For `mu<mu_0<0.86` and `pi<22/7`,

```math
C_*<\frac{2(0.86)+22/7}{4}<\frac54.
\tag{3.4}
```

The derivative of `varphi` is

```math
\varphi'(u)=\frac{u^2}{2\sqrt{1-u^2/4}}.
\tag{3.5}
```

For `0<=u<=5/4`,

```math
\boxed{
\frac1{\sqrt{1-u^2/4}}
\le1+\frac{3u^2}{16}.
}
\tag{3.6}
```

Indeed, after squaring positive quantities, (3.6) is equivalent to

```math
9t^2+60t-128\le0,
\qquad t=u^2,
```

and the left side is increasing while at `t=25/16` it equals

```math
-3143/256<0.
```

Integrating (3.5)-(3.6) from zero gives

```math
\varphi(C)
\le\frac{C^3}{6}+\frac{3C^5}{160}.
\tag{3.7}
```

For `C<=5/4`,

```math
\frac{\varphi(C)}{C^2}
\le\frac5{24}+\frac{75}{2048}
=
\frac{1505}{6144}.
\tag{3.8}
```

Moreover

```math
\frac{1505}{6144}
<\frac{49}{198}
<\frac7{9\pi},
\tag{3.9}
```

where the exact first margin is

```math
\frac{49}{198}-\frac{1505}{6144}
=
\frac{511}{202752}>0,
```

and the second inequality uses `pi<22/7`.

At `C_*=B/4`, equation (3.2) becomes

```math
D_\mu(C_*)
=-\frac{\varphi(C_*)}{4}
+
\frac{7C_*^2}{36\pi}.
```

By (3.9), this is strictly positive:

```math
\boxed{D_\mu(C_*)>0.}
\tag{3.10}
```

A concave function lies above the chord joining its endpoint values.  Since
`D_mu(0)=0` and `D_mu(C_*)>0`,

```math
\boxed{D_\mu(C)\ge0\quad(0\le C\le C_*).}
\tag{3.11}
```

Therefore

```math
\boxed{H_\mu(C)\ge H_\mu(0).}
\tag{3.12}
```

The worst possible side-cost state is `C=0`.

---

## 4. Closed-form threshold

At `C=0`, `A(0)=pi/4` and `B=2mu+pi`.  Necessary condition JS.4 becomes

```math
\frac\pi4
\le
\frac\pi4\mu^2+
\frac{(2\mu+\pi)^2}{36\pi}.
\tag{4.1}
```

Equivalently

```math
\boxed{
(9\pi^2+4)\mu^2+4\pi\mu-8\pi^2\ge0.
}
\tag{4.2}
```

The left side is strictly increasing for `mu>=0` and has one positive zero.  Solving
the quadratic gives

```math
\boxed{
\mu_0
=
\frac{2\pi\bigl(3\sqrt{2\pi^2+1}-1\bigr)}{9\pi^2+4}.
}
\tag{4.3}
```

Hence every survivor limit satisfies

```math
\boxed{\mu\ge\mu_0.}
```

This proves JS.1.

### Exact bracket

Let

```math
N(m):=(8-9m^2)\pi^2-4m\pi-4m^2.
```

Then (4.1) is violated exactly when `N(m)>0`, and the threshold has `N(mu_0)=0`.
Using

```math
6283/2000<\pi<3927/1250,
```

one obtains the rigorous signs

```math
N(857/1000)>0
```

with lower rational bound

```math
\frac{41341990351}{4000000000000}>0,
```

and

```math
N(43/50)<0
```

with upper rational bound

```math
-\frac{1969912139}{3906250000}<0.
```

Thus

```math
0.857<\mu_0<0.86.
```

High-precision evaluation gives the decimal in JS.1.

---

## 5. Equality structure

Suppose a sequence approaches `mu_0`.  Since `H_mu(C)>H_mu(0)` for every fixed
`C>0`, necessary equality forces

```math
\boxed{C\to0.}
\tag{5.1}
```

Thus every projective diameter-direction gap is `o(1)`; the normalized force hull is
asymptotically disk-like at the area level:

```math
\boxed{area(F)/D^2\to\pi/4.}
\tag{5.2}
```

Equality in JS.3 and `x<=(B-C)/3` gives

```math
\boxed{x\to x_0:=\frac{2\mu_0+\pi}{3}.}
\tag{5.3}
```

The perimeter-side inequality also becomes sharp:

```math
\boxed{y+d\to\pi,}
\tag{5.4}
```

so

```math
q/D\to\pi,
\qquad
P_F/D\to\pi.
\tag{5.5}
```

Moreover equality in the two PC affine bounds implies, after discarding only the
explicit nonnegative remainders,

```math
\frac aD,\frac{c_B}{D},\frac{s_C}{D}\to0,
```

and

```math
d+s\to x_0-\mu_0=\frac{\pi-\mu_0}{3}.
\tag{5.6}
```

The split between `d_H` and `s_Z` is not fixed by this theorem.

This endpoint is a near-maximal-perimeter, near-disk force hull with almost every hull
side a unit contact, but a linear mixed/diameter defect remains.  No contradiction is
claimed here.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| joint budget JS.3 | proved | two exact PC inequalities + perimeter side-cost charge |
| `C<=x` | proved asymptotically | every macroscopic force side is paid by OP chain degree |
| side-area floor `A(C)` | proved in SC | midpoint polygon + projective gap defect |
| cavity upper `x^2/(4pi)` | proved | paired outer-pocket + exceptional-face bounds |
| `C=0` is worst | proved analytically | concavity + endpoint estimate (3.6)-(3.10) |
| closed-form `mu_0` | proved | quadratic at `C=0` |
| decimal `0.857065...` | diagnostic | not a proof input |
| equality endpoint impossible | open | requires mixed-defect/near-disk structure |
| Level I | open | no universal upper contradiction yet |

---

## 7. Next target

The JS endpoint forces simultaneously

```math
C=o(1),
\quad
q/D\to\pi,
\quad
P_F/D\to\pi,
\quad
a=o(D),
```

so all but `o(D)` of the `pi D+o(D)` force-hull sides are exact unit contacts and the
force hull has maximal normalized area/perimeter.  At the same time

```math
(d_H+s_Z)/D
\to(\pi-\mu_0)/3>0.76.
```

The next theorem should show that a near-circular unit-contact boundary cannot support
that much Woodall diameter-component / mixed-rigidity defect under the restored KKT
response.  This is now a much narrower structural problem than the original C-II
gate.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let C be total normalized chord cost from macroscopic projective gaps and
x=(d_P+Q)/D.  Exact PC gives
  x<=mu+d+s,
  x<=y-d-2s,
so
  3x<=2mu+y+d.
Since projective macroscopic sides contribute to P_F-q and
  q/D=y+d, P_F/D<=pi,
we have
  C<=pi-y-d.
Therefore
  3x+C<=2mu+pi,
  C<=x,
so x<=(2mu+pi-C)/3 and C<=(2mu+pi)/4.

Side-gap geometry gives area(F)/D^2>=A(C)=(pi-varphi(C))/4.
Paired-pocket capacity gives G/D^2<=x^2/(4pi), and C_att<=pi mu^2/4.
Thus
  A(C)<=pi mu^2/4+(2mu+pi-C)^2/(36pi).
For mu<.86, C<=5/4.  The difference from C=0 is concave in C and positive at
C=(2mu+pi)/4 because
  varphi(C)/C^2 <=1505/6144 <49/198<7/(9pi).
Hence C=0 is the worst case.
At C=0 the threshold is
  (9pi^2+4)mu^2+4pi mu-8pi^2=0,
so
  mu>=mu_0=2pi(3sqrt(2pi^2+1)-1)/(9pi^2+4)
    =0.85706506318...
with exact bracket .857<mu_0<.86.

Endpoint forces C->0, q/D,P_F/D->pi, area(F)/D^2->pi/4,
a,c_B,s_C=o(D), but (d_H+s_Z)/D remains linear.
Next: exclude this near-circular, almost-unit-boundary high-defect geometry.
```
