<!-- theorem-state: {"artifact_id":"ART-6DCDF4F1F826","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF force-hull area floor upgrade

**Date:** 2026-09-09  
**Repository base:** current post-ZF report stack / PR #110  
**Run type:** exact cross-route constant improvement  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

Canonical C67 proves a quadratic force-hull area floor from a lower bound on the
number of actual diameter edges. Its published constant uses only the pre-ZF estimate
`h>D/4`. ZS now proves the much stronger exact inequality

\[
h\ge\delta\ge\lceil D\rceil.
\]

Feeding that directly into the already-audited C67 projective-direction packing lemma
improves the asymptotic force-hull area constant from

\[
\frac12\sin(1/4)=0.1237019796\ldots
\]

to

\[
\boxed{
\frac12\sin(1)=0.4207354924\ldots .
}
\]

No new literature input or geometric lemma is needed.

## 1. C67 input

For two distinct actual diameter edges, C67 proves their projective directions are
separated by at least

\[
\boxed{
\delta_D:=2\arcsin\frac1{2D}.
}
\tag{1.1}
\]

The same report proves the finite projective-circle packing lemma:

> `h` pairwise `delta`-separated points on a circle of circumference `pi` contain two
> points at projective distance at least
> \[
> \min\{\pi/3,(h-1)\delta\}.
> \]

If two diameter chords have projective angle `phi`, whether they share an endpoint or
cross as disjoint diameter chords, the convex hull of their endpoints has area

\[
\boxed{\frac{D^2}{2}\sin\phi.}
\tag{1.2}
\]

All their endpoints lie in the force hull `F`.

## 2. Theorem ZA — strengthened post-ZF area floor

Define

\[
\boxed{
\Phi_{ZF}(D):=
\min\left\{
\frac\pi3,
(\lceil D\rceil-1)
2\arcsin\frac1{2D}
\right\}.
}
\tag{ZA.1}
\]

### Theorem ZA

Every sufficiently large post-ZF survivor satisfies the finite bound

\[
\boxed{
\operatorname{area}(F)
\ge
\frac{D^2}{2}\sin\Phi_{ZF}(D).
}
\tag{ZA.2}
\]

Consequently

\[
\boxed{
\liminf_{D\to\infty}
\frac{\operatorname{area}(F)}{D^2}
\ge
\frac12\sin1
=0.420735492403948\ldots .
}
\tag{ZA.3}
\]

### Proof

ZS gives `h>=ceil(D)`. Apply the C67 projective packing lemma to the `h` actual
diameter directions with separation `delta_D`. Two directions have angle at least

\[
\min\{\pi/3,(h-1)\delta_D\}
\ge\Phi_{ZF}(D).
\]

The relevant angles lie in `[0,pi/2]`, and the C67 truncation at `pi/3` keeps sine
monotone. Equation (1.2) therefore gives ZA.2.

Finally

\[
2D\arcsin\frac1{2D}\longrightarrow1,
\]

and `(ceil(D)-1)/D ->1`, so the second argument in ZA.1 tends to `1`, which is below
`pi/3`. Thus `Phi_ZF(D)->1`, proving ZA.3. `square`

## 3. Quantitative impact on the new gap theorem

The attachment-cell report proved, with

\[
L_2=6-3(d_H+s_Z)+e_{BB}+2s_C,
\]

that

\[
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\]

Replace the old C67 constant by ZA. Let

\[
\lambda_2:=\limsup\frac{e_{BB}+2s_C}{D}.
\]

Since `L_2/D<=lambda_2+o(1)`, the force-hull gap now obeys

\[
\boxed{
\liminf\frac G{D^2}
\ge
\frac12\sin1-rac\pi4\lambda_2^2.
}
\tag{ZA.4}
\]

Hence a positive quadratic gap is forced whenever

\[
\boxed{
\lambda_2
<
\sqrt{\frac{2\sin1}{\pi}}
=0.7319\ldots .
}
\tag{ZA.5}
\]

This substantially enlarges the rigorously controlled low-surplus phase. In
particular, if `e_BB+s_C=o(D)`, then

\[
\boxed{
G\ge\left(\frac12\sin1-o(1)\right)D^2.
}
\tag{ZA.6}

The outer-shell / giant-defect-face localization from ZG therefore holds with the
new `0.420735...` quadratic area currency rather than `0.123701...`.

## 4. Comparison with the previous constant

The old C67 route used only

\[
h>D/4,
\]

so `(h-1)delta_D` was bounded asymptotically by `1/4`. ZS replaces this by
`h>=D+O(1)`, multiplying the available projective spread by four before the sine is
taken.

Numerically,

\[
\frac{(1/2)\sin1}{(1/2)\sin(1/4)}
=3.401\ldots .
\]

The improvement is therefore not a bookkeeping epsilon; it changes the force-hull
carrier from a weak two-direction area floor to more than `42%` of `D^2`.

For comparison, the planar isodiametric upper bound remains

\[
\operatorname{area}(F)\le\frac\pi4D^2
=0.785398\ldots D^2.
\]

There is still substantial room, so ZA alone is not a contradiction.

## 5. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| finite ZA.2 | proved | ZS edge count inserted into C67's proved separation/packing lemma. |
| asymptotic constant `(1/2)sin1` | proved | elementary limit. |
| gap threshold `0.7319...` | proved | ZA plus ZK attachment-cell area estimate. |
| force-hull area contradiction | not proved | isodiametric upper constant remains larger. |
| Level I | still open | Macroscopic cavity and linear-surplus branches remain. |

## 6. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C67: h diameter directions, pairwise separated by
    delta_D=2 asin(1/(2D)),
force two directions separated by
    min(pi/3,(h-1)delta_D),
and therefore
    area(F)>=(D^2/2) sin(phi).

ZS gives h>=ceil(D), hence post-ZF
    Phi_ZF(D)=min(pi/3,(ceil(D)-1)2asin(1/(2D))) -> 1,
so
    liminf area(F)/D^2 >= (1/2)sin(1)=0.4207354924...

With ZK's L_2 bound,
    liminf G/D^2 >= (1/2)sin1-(pi/4)lambda_2^2,
    lambda_2=limsup(e_BB+2s_C)/D.
Thus G is quadratically positive whenever lambda_2<0.7319... .
```
