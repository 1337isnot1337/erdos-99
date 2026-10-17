> Generated reading edition · [exact source](../../../docs/reports/target_c_mixed_gap_cauchy_threshold_candidate_2026-09-12.md) · source SHA-256 `7babc497c015b94f12e8c54e6327e20f075cb1040270e1b83fe35c478e46d9fd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-6103A072CD46","canonical":true,"claim_ids":["C-WRAP-MIXED-CAUCHY"],"claim_statuses":{"C-WRAP-MIXED-CAUCHY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — mixed forbidden-gap/Cauchy wrapping threshold

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** canonical after independent hostile audit and theorem-state promotion.

Canonical Sections 93, 94, and 96 contain a stronger wrapping obstruction than the
currently canonical Section-96 scalar threshold. Section 94 used three distinguished
forbidden angular gaps but discarded the residual angular mass left after the ordinary
attachment gaps were charged at their minimum spacing. Section 96 independently gives
a stronger lower bound on attachment density. Keeping that residual mass and placing it
optimally by concavity, then applying Cauchy's perimeter-diameter inequality, raises the
necessary wrapping diameter to

```math
\boxed{
\mu_6=0.9399896933531978\ldots .
}
```

This strictly subsumes the proof-only coarse Cauchy bound
`\sqrt{1-(\pi/9)^2}=0.9370981976747776...` and makes the nominal Section-96 endpoint
`\mu_4=0.936215741409583...` impossible a fortiori.

No Section-97 or Section-98 endpoint theorem is used. Their conditional deductions can
remain internally valid, but their `\lambda\to\mu_4` hypothesis is not a live Type-II
survivor regime.

---

# 99. Residual forbidden-gap mass plus Cauchy forces diameter at least 0.939989 D

## 99.1 Canonical wrapping data

Let `P_D=conv(A_D)` be a wrapping Type-II harmonic-cell sequence with source diameter
`D -> infinity` and

```math
{\operatorname{diam}(P_D)\over D}\to\lambda<1.
\tag{99.1}
```

Put

```math
\theta:=2\arcsin\lambda\in[2\pi/3,\pi),
\qquad
\phi:=2\pi-2\theta,
\tag{99.2}
```

and, after passing to a subsequence,

```math
{a_D\over D}\to\alpha,
\qquad a_D:=|A_D|.
\tag{99.3}
```

Write

```math
L(\theta):={3\over2}\sin\theta,
\qquad
U(\theta):=3\theta-2\pi.
\tag{99.4}
```

Canonical Section 96 gives the attachment-density floor

```math
\boxed{\alpha\ge L(\theta),}
\tag{99.5}
```

while canonical Section 88 gives the six-cluster ceiling

```math
\boxed{\alpha\le U(\theta).}
\tag{99.6}
```

Canonical Sections 93--94 give finite gap information. If
`g_{1,D},\ldots,g_{a_D,D}` are the cyclic polar gaps between consecutive attachments,
then

1. every gap obeys
   ```math
   g_{i,D}\ge\ell_D,
   \qquad D\ell_D\to2;
   \tag{99.7}
   
   ```
2. every gap obeys
   ```math
   g_{i,D}\le\theta+o(1)
   \tag{99.8}
   
   ```
   uniformly; and
3. three distinct distinguished gaps obey
   ```math
   g_{i_j,D}\ge\phi-o(1),
   \qquad j=1,2,3.
   \tag{99.9}
   
   ```

The three special lower bounds are the central forbidden arcs in the Section-88
six-cluster geometry.

## 99.2 In the only relevant scalar range one special gap can absorb all residual mass

If

```math
\theta\ge {5\over2},
```

then already

```math
\lambda=\sin(\theta/2)\ge\sin(5/4)=0.94898\ldots>\mu_6,
```

so only `theta<5/2` needs analysis.

On

```math
2\pi/3\le\theta<{5\over2}<{5\pi\over6},
```

we have `sin(theta)>1/2`, hence

```math
L(\theta)>{3\over4}.
\tag{99.10}
```

Also, using `pi>3`,

```math
{U(\theta)\over2}
<{3(5/2)-6\over2}
={3\over4}.
\tag{99.11}
```

Therefore every relevant wrapping sequence satisfies

```math
\boxed{
\alpha\ge L(\theta)>{U(\theta)\over2}.
}
\tag{99.12}
```

Charge three distinguished gaps at their asymptotic lower value `phi` and all other
`a_D-3` gaps at the uniform minimum `ell_D`. Their baseline total angular mass tends to

```math
3\phi+2\alpha.
\tag{99.13}
```

Since all cyclic gaps sum to `2pi`, the remaining angular mass tends to

```math
R(\alpha,\theta)
:=2\pi-3\phi-2\alpha
=2\bigl(U(\theta)-\alpha\bigr).
\tag{99.14}
```

By (99.12),

```math
0\le R(\alpha,\theta)\le U(\theta).
\tag{99.15}
```

But one distinguished gap has capacity

```math
\theta-\phi=3\theta-2\pi=U(\theta)
\tag{99.16}
```

between its lower value `phi` and the common upper bound `theta`. Thus one special gap
can absorb the entire first-order residual angular mass.

## 99.3 Concavity gives the sharpened perimeter floor

Let

```math
f(x):=\sin(x/2),
\qquad 0\le x<\pi.
```

The function `f` is increasing and concave, with decreasing derivative. If `x>=y`,
shifting a small amount of angular mass from `y` to `x` cannot increase
`f(x)+f(y)`. Repeating this exchange shows that, subject to the lower/upper gap bounds,
the minimum chord sum places residual mass into the currently largest gaps first.

Because (99.15)--(99.16) let one distinguished gap absorb all first-order residual,
the asymptotic minimizing pattern is

```text
ordinary gaps:  ell_D at first order,
special gap 1:  phi,
special gap 2:  phi,
special gap 3:  phi + R(alpha,theta).
```

The `o(1)` finite slack in (99.8)--(99.9) changes the chord sum by only `o(1)`.
Using

```math
(a_D-3)\sin(\ell_D/2)\to\alpha
```

from Section 93 and `sin(phi/2)=sin(theta)`, we obtain

```math
\boxed{
\liminf {\operatorname{per}(P_D)\over D}
\ge
q(\alpha,\theta)
:=
\alpha+2\sin\theta
+\sin(2\theta-\pi-\alpha).
}
\tag{99.17}
```

Indeed

```math
{\phi+R(\alpha,\theta)\over2}
=2\theta-\pi-\alpha.
\tag{99.18}
```

For feasible `alpha` in the range (99.12), this angle lies between `phi/2` and
`theta/2`. Therefore

```math
{\partial q\over\partial\alpha}
=1-\cos(2\theta-\pi-\alpha)\ge0.
\tag{99.19}
```

The easiest perimeter case is consequently the minimum allowed attachment density,
`alpha=L(theta)`. Hence every relevant wrapping limit satisfies

```math
\boxed{
\liminf {\operatorname{per}(P_D)\over D}
\ge
Q(\theta)
:={7\over2}\sin\theta
+\sin\left(2\theta-\pi-{3\over2}\sin\theta\right).
}
\tag{99.20}
```

This is strictly stronger than the coarse Section-94/96 combination
`(9/2) sin(theta)` in the scalar range containing the new threshold: it retains the
positive residual angular mass forced by `alpha<U(theta)`.

## 99.4 Cauchy perimeter-diameter gives the new scalar obstruction

For every planar convex body `K`, Cauchy's projection formula gives

```math
\operatorname{per}(K)
\le\pi\operatorname{diam}(K).
\tag{99.21}
```

Applying this to `P_D` and using (99.1),

```math
\limsup {\operatorname{per}(P_D)\over D}
\le\pi\lambda
=\pi\sin(\theta/2).
\tag{99.22}
```

Thus every wrapping limit with `theta<5/2` must satisfy

```math
\boxed{
H(\theta)
:={7\over2}\sin\theta
+\sin\left(2\theta-\pi-{3\over2}\sin\theta\right)
-\pi\sin(\theta/2)
\le0.
}
\tag{99.23}
```

Before solving this inequality, note that dropping the residual term recovers the
coarse Cauchy bound

```math
{9\over2}\sin\theta\le\pi\sin(\theta/2)
\quad\Longrightarrow\quad
9\cos(\theta/2)\le\pi.
\tag{99.24}
```

Hence every wrapping limit already obeys

```math
\theta\ge\theta_5:=2\arccos(\pi/9).
\tag{99.25}
```

This is the valid core of the proof-only coarse-Cauchy Section-98 proposal.

## 99.5 `H` has one root in the live interval

Put

```math
A(\theta):=2\theta-\pi-{3\over2}\sin\theta.
```

Then

```math
H'(\theta)
={7\over2}\cos\theta
+\left(2-{3\over2}\cos\theta\right)\cos A(\theta)
-{\pi\over2}\cos(\theta/2).
\tag{99.26}
```

On `[theta_5,5/2]`, use `cos A<=1` to get

```math
H'(\theta)
\le
2+2\cos\theta-{\pi\over2}\cos(\theta/2).
\tag{99.27}
```

Since `theta>=theta_5` and

```math
\cos\theta_5=2(\pi/9)^2-1,
```

we have

```math
2+2\cos\theta\le {4\pi^2\over81}.
\tag{99.28}
```

Also `theta/2<=5/4`, so `cos(theta/2)>=cos(5/4)`. The alternating Taylor bound gives

```math
\cos(5/4)
\ge
1-{(5/4)^2\over2}+{(5/4)^4\over24}-{(5/4)^6\over720}
={185899\over589824}.
\tag{99.29}
```

Using `pi<22/7`,

```math
{185899\over589824}
>{176\over567}
>{8\pi\over81}.
\tag{99.30}
```

Equations (99.27)--(99.30) imply

```math
\boxed{H'(\theta)<0\quad(\theta_5\le\theta\le5/2).}
\tag{99.31}
```

At `theta=theta_5`, the coarse Cauchy inequality (99.24) is equality. Writing
`F_4(theta)=U(theta)-L(theta)`, the canonical Section-96 scalar function, we have

```math
A(\theta_5)
=(\pi-\theta_5)+F_4(\theta_5).
\tag{99.32}
```

Canonical Section 96 has a unique zero `theta_4`, and the coarse Cauchy threshold is
strictly larger: `theta_5>theta_4`. Thus `F_4(theta_5)>0`. Both angles in (99.32) lie
in `(0,pi/2)`, so

```math
H(\theta_5)
=\sin A(\theta_5)-\sin(\pi-\theta_5)>0.
\tag{99.33}
```

Direct scalar evaluation gives

```math
H(5/2)<0.
\tag{99.34}
```

Therefore `H` has exactly one zero `theta_6` in `(theta_5,5/2)`. Define

```math
\boxed{
H(\theta_6)=0,
\qquad
\mu_6:=\sin(\theta_6/2).
}
\tag{99.35}
```

The accompanying scalar regression certificate gives

```math
\boxed{
\theta_6
=2.445200194924480059\ldots,
\qquad
\mu_6
=0.939989693353197775\ldots .
}
\tag{99.36}
```

In particular,

```math
\mu_6-\sqrt{1-(\pi/9)^2}
=0.00289149567842017\ldots>0.
\tag{99.37}
```

Since `H` is strictly decreasing on the entire live interval beginning at `theta_5`,
(99.23) forces

```math
\boxed{
\lambda\ge\mu_6
=0.9399896933531978\ldots .
}
\tag{99.38}
```

## 99.6 Propagate to an actual macroscopic carrier

Fix any `mu<mu_6`. By (99.38), a macroscopic harmonic-cell limit of normalized
diameter at most `mu` cannot be wrapping, so it is cap type. The canonical Section-88
cap-family capacity theorem therefore applies exactly as in Sections 94 and 96:

```math
\limsup {1\over D^2}
\sum_{\operatorname{diam}(P_r)\le\mu D}
\operatorname{area}(P_r)
\le\mathcal C(\mu)<{\pi\over4}.
\tag{99.39}
```

The total harmonic-cell perimeter bound leaves only uniformly many cells longer than
`mu D`, and canonical Section 83 gives summed local rhombic deficit `o(D^2)`. A
diagonal choice `mu upward mu_6` therefore yields an actual macroscopic locally
rhombus-saturated carrier `P_*` with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(\mu_6-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_6D^2,
\qquad
{A_{4,*}\over\operatorname{area}(P_*)}\to1
}
\tag{99.40}
```

for one absolute `c_6>0`.

## 99.7 Audit consequence and next frontier

The live full-core Type-II carrier threshold is therefore at least `0.939989... D` if
this proof survives independent review. In particular:

- the Section-96 `mu_4` equality regime is empty;
- Sections 97--98 are useful conditional/equality analyses but are not live survivor
  branches at `mu_4`;
- the proof-only coarse Cauchy threshold `0.937098...` is valid but nonoptimal;
- endpoint research should move to `mu_6`, where equality would require simultaneous
  saturation of the Section-96 attachment-density floor, the mixed three-gap concavity
  floor, and Cauchy's perimeter-diameter inequality.

That equality stack is substantially more rigid than the old `mu_4` stack. A natural
next attack is to combine Cauchy near-equality (near constant width) with the three
macroscopic forbidden gaps and the canonical ordered train grid. No such closing
implication is claimed here.

## 99.8 Dependency and regression audit

- **Canonical Section 93:** uniform lower and upper finite cyclic-gap bounds and the
  annular chord-to-perimeter transfer.
- **Canonical Section 94:** three distinct finite forbidden gaps of asymptotic lower
  size `phi=2pi-2theta`.
- **Canonical Section 96:** attachment-density floor
  `alpha >= (3/2) sin(theta)`.
- **Canonical Section 88:** six-cluster ceiling `alpha<=3theta-2pi` and cap-family
  propagation.
- **Canonical Section 83:** local-rhombic-deficit summability for the actual-carrier
  conclusion.
- **Cauchy perimeter-diameter inequality:** `per(P)<=pi diam(P)` for planar convex
  attachment polygons.
- **No Section 97/98 endpoint statement is used.**
- **No KKT coefficient floor, Fox--Pach constant, rejected cap theorem, or removal of
  contact-isolated source points is used.**

**Promotion:** completed in theorem-state audit.39. The `mu_6` threshold is now the
live canonical wrapping bound; the `mu_4` endpoint branches are vacuous conditional
structure.
