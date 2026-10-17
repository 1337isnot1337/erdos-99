> Generated reading edition · [exact source](../../../docs/reports/target_c_fsjc_endpoint_central_symmetry_exclusion_2026-09-10.md) · source SHA-256 `1a00499b814d042e577afee8249dca178745db05ee9f121ff98c89c1902b468d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-900E2197781E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fsjc_endpoint_central_symmetry_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=68757e622a30fcb27ae90866d7a6dad14ce06d19; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — central symmetry excludes the FSJC endpoint

**Date:** 2026-09-10  
**Repository base:** `1ea7a3c5970d614c9f860841eea5ad3718ca171f`  
**Run type:** exact asymptotic equality-case exclusion  
**Target:** Target C, C-II after ZF / FSDB / FSJC  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

The FSJC report proves

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_*,
\qquad
\lambda_*=0.5882283437736394\ldots,
```

where `lambda_*` is the positive root of

```math
(\pi^2+1)\lambda^2+\pi\lambda-\frac{\pi^2}{4}-\pi=0.
\tag{E.1}
```

It also proves that any sequence attaining this endpoint must have

```math
\frac hD\to\frac\pi2.
```

This report closes that equality case completely. There is **no** unbounded post-ZF survivor sequence with

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_*.
```

Consequently there exists an absolute `epsilon>0` such that every sufficiently large post-ZF survivor satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\ge\lambda_*+\epsilon.
}
\tag{E.2}
```

The value of `epsilon` is not made explicit here.

The mechanism is structural. Exact endpoint saturation forces simultaneously

```math
\frac{d_H+s_Z}{D}\to0,
\qquad
\frac{s_C}{D}\to0,
\qquad
\frac{e_{BB}}D\to\lambda_*,
\qquad
\frac{\operatorname{per}F}{D}\to\pi.
```

FS.4 makes the normalized force hull asymptotically centrally symmetric. A centrally symmetric diameter-one convex limit with perimeter `pi` must be the radius-`1/2` disk. Hence

```math
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
```

But this disk-area limit raises the GU attachment-gap lower bound above the JC cavity upper bound by the exact positive constant

```math
\boxed{\frac{\pi-2}{8}.}
```

That contradiction excludes the FSJC endpoint.

---

## 1. Inputs

Let an unbounded post-ZF survivor sequence be given. Use the standard notation

- `F` for the force hull;
- `h` for the number of actual diameter pairs;
- `e_BB` for loaded-loaded unit contacts;
- `s_C` for pinned-contact stress surplus;
- `d_H=q-h` for the number of tree components of the planar diameter pseudoforest;
- `s_Z` for extra mixed-framework row dependence.

Put

```math
L=e_{BB}+2s_C,
\qquad
k=d_H+s_Z.
\tag{1.1}
```

The exact ZK component ledger gives

```math
L_2:=6-3k+L\ge0
\tag{1.2}
```

and the attachment-cell area bound

```math
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4L_2^2+\pi L_2+\pi^2D.
\tag{1.3}
```

Thus if

```math
\frac LD\to\lambda,
\qquad
\frac kD\to\kappa,
\qquad
\frac hD\to y,
```

then FSDB's force-hull area bound

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}
\tag{1.4}
```

and (1.3) imply

```math
\boxed{
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4(\lambda-3\kappa)^2.
}
\tag{1.5}
```

Here `G` is the GU attachment-cell gap. Nonnegativity of `L_2` gives

```math
0\le3\kappa\le\lambda.
\tag{1.6}
```

Next put

```math
t:=\lim\frac{e_{BB}}D
```

after passing to a further subsequence. Since `L=e_BB+2s_C`,

```math
0\le t\le\lambda.
\tag{1.7}
```

Let

```math
p:=\lim\frac{\operatorname{per}F}{D}
```

after another extraction. Unit separation of consecutive force-hull vertices and `h<=q` give `p>=y`, while Cauchy's perimeter-diameter inequality gives

```math
p\le\pi.
\tag{1.8}
```

The actual-perimeter JC proof gives

```math
E_{out}+Q
\le
 e_{BB}+\min\{h,\operatorname{per}F-h\},
\tag{1.9}
```

and hence

```math
\boxed{
\limsup\frac GD^2
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi}.
}
\tag{1.10}
```

This is the unrelaxed form needed below.

FS.4 supplies a common source circumcenter `o` and

```math
\boxed{
 d_{\rm Haus}(F-o,-(F-o))\le2L_D,
\qquad
\frac{L_D}{D}=O(D^{-1/4}).
}
\tag{1.11}
```

Thus every Hausdorff limit of the normalized force hulls `(F-o)/D` is centrally symmetric about the origin.

---

## 2. Endpoint saturation kills all hidden ZK and pinned-stress slack

Assume for contradiction that

```math
\boxed{
\frac LD\to\lambda_*.
}
\tag{2.1}
```

FSJC endpoint localization gives

```math
\boxed{
\frac hD\to\frac\pi2.
}
\tag{2.2}
```

Pass to a subsequence on which `k/D`, `e_BB/D`, and `per(F)/D` converge to `kappa,t,p`.

At `y=pi/2`, (1.5) gives

```math
\liminf\frac GD^2
\ge
\frac{\pi/2+1}{4}
-
\frac\pi4(\lambda_*-3\kappa)^2.
\tag{2.3}
```

Equation (1.10) gives

```math
\limsup\frac GD^2
\le
\frac{(t+\min\{\pi/2,p-\pi/2\})^2}{4\pi}.
\tag{2.4}
```

Using `t<=lambda_*` and `p<=pi`,

```math
\limsup\frac GD^2
\le
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
\tag{2.5}
```

By the defining equation (E.1),

```math
\boxed{
\frac{\pi/2+1}{4}
-
\frac\pi4\lambda_*^2
=
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
}
\tag{2.6}
```

Now compare (2.3) with (2.5).

Because `0<=3kappa<=lambda_*`, if `kappa>0` then

```math
(\lambda_*-3\kappa)^2<\lambda_*^2,
```

so the lower bound in (2.3) is strictly larger than the common value in (2.6), contradicting (2.5). Therefore

```math
\boxed{\kappa=0.}
\tag{2.7}
```

With `kappa=0`, equality throughout the remaining endpoint chain is forced. If `t<lambda_*`, then the right side of (2.4) is strictly below the common value in (2.6), contradiction. Hence

```math
\boxed{t=\lambda_*.}
\tag{2.8}
```

Since

```math
\lambda_*-t
=\lim\frac{2s_C}{D},
```

we obtain

```math
\boxed{\frac{s_C}{D}\to0.}
\tag{2.9}
```

Likewise, to attain the upper endpoint in (2.4) one must have

```math
\min\{\pi/2,p-\pi/2\}=\pi/2.
```

Thus `p>=pi`, and (1.8) yields

```math
\boxed{
\frac{\operatorname{per}F}{D}\to\pi.
}
\tag{2.10}
```

Finally (2.7) is exactly

```math
\boxed{
\frac{d_H+s_Z}{D}\to0.
}
\tag{2.11}
```

Since both terms are nonnegative, each is individually `o(D)`.

### Additional exact ledger consequence

Because

```math
q=h+d_H,
```

(2.2) and (2.11) give

```math
\frac qD\to\frac\pi2.
\tag{2.12}
```

ZU gives

```math
c_I+e_{BB}+s_C=q-2+d_H+s_Z.
```

Using (2.8)-(2.12),

```math
\boxed{
\frac{c_I}{D}
\to
\frac\pi2-\lambda_*
=0.9825679830\ldots .
}
\tag{2.13}
```

Thus a hypothetical FSJC-endpoint sequence would have almost one unloaded contact component per unit diameter. This fact is not needed for the contradiction below, but it records the exact endpoint normal form.

---

## 3. Near-maximal perimeter plus FS.4 forces a disk limit

Translate by the FS.4 common center `o` and scale by `D`:

```math
\widetilde F:=\frac{F-o}{D}.
```

Every `F` contains endpoints of an actual diameter edge, so

```math
\operatorname{diam}\widetilde F=1.
\tag{3.1}
```

The full-source circumradius estimate places every force hull in a uniformly bounded disk after this normalization. By Blaschke selection, pass to a subsequence converging in Hausdorff distance to a compact convex body `F_infty`.

Equation (1.11) gives

```math
d_{\rm Haus}(\widetilde F,-\widetilde F)\to0,
```

so

```math
\boxed{F_\infty=-F_\infty.}
\tag{3.2}
```

Thus the limit is centrally symmetric about the origin.

Perimeter and diameter are continuous under Hausdorff convergence of planar convex bodies. By (2.10) and (3.1),

```math
\boxed{
\operatorname{diam}F_\infty=1,
\qquad
\operatorname{per}F_\infty=\pi.
}
\tag{3.3}
```

Let `w(theta)` be the width of `F_infty`. Since its diameter is one,

```math
0\le w(\theta)\le1
\qquad(0\le\theta<\pi).
\tag{3.4}
```

Cauchy's width formula and (3.3) give

```math
\int_0^\pi w(\theta)\,d\theta=\pi.
\tag{3.5}
```

The width function is continuous. Since it is everywhere at most one and its integral equals the integral of the constant function one, necessarily

```math
\boxed{w(\theta)\equiv1.}
\tag{3.6}
```

So `F_infty` has constant width one.

For a centrally symmetric convex body centered at the origin, its support function satisfies

```math
h(u)=h(-u),
```

while the width is

```math
w(u)=h(u)+h(-u)=2h(u).
```

Equation (3.6) therefore gives

```math
h(u)\equiv\frac12.
```

A convex body with constant support function `1/2` is the Euclidean disk of radius `1/2`. Hence

```math
\boxed{
F_\infty=\overline B(0,1/2).
}
\tag{3.7}
```

Area is also continuous under Hausdorff convergence of convex bodies, so

```math
\boxed{
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
}
\tag{3.8}
```

This is the key gain over the bare FSDB endpoint value `(pi/2+1)/4`.

---

## 4. Disk area contradicts the same endpoint cavity budget

Return to the GU attachment gap. Since `k=o(D)`, the exact ZK cell budget has

```math
\frac{L_2}{D}\to\lambda_*.
```

Equation (1.3) and the disk-area limit (3.8) give

```math
\boxed{
\liminf\frac GD^2
\ge
\frac\pi4(1-\lambda_*^2).
}
\tag{4.1}
```

On the other hand, (2.4), (2.8), and (2.10) give the JC upper bound

```math
\boxed{
\limsup\frac GD^2
\le
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
}
\tag{4.2}
```

Subtract the right side of (4.2) from the right side of (4.1). Multiplying by `4pi`, the numerator is

```math
\begin{aligned}
&\pi^2(1-\lambda_*^2)-(\lambda_*+\pi/2)^2\\
&=\frac{3\pi^2}{4}-(\pi^2+1)\lambda_*^2-\pi\lambda_*.
\end{aligned}
\tag{4.3}
```

Use the defining equation (E.1):

```math
(\pi^2+1)\lambda_*^2+\pi\lambda_*
=\frac{\pi^2}{4}+\pi.
```

Thus (4.3) equals

```math
\frac{\pi^2}{2}-\pi
=\pi\left(\frac\pi2-1\right)>0.
```

After division by `4pi`, the exact gap is

```math
\boxed{
\frac\pi4(1-\lambda_*^2)
-
\frac{(\lambda_*+\pi/2)^2}{4\pi}
=
\frac{\pi-2}{8}>0.
}
\tag{4.4}
```

This contradicts (4.1)-(4.2).

Therefore no endpoint sequence (2.1) exists.

---

## 5. Uniform strict improvement above FSJC

Suppose no absolute improvement existed. Then for every integer `j` there would be a sufficiently large post-ZF survivor with

```math
\frac{e_{BB}+2s_C}{D}<\lambda_*+\frac1j.
```

Taking `D->infinity` along such a diagonal sequence and using FSJC's lower bound produces a subsequence with

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_*.
```

Section 4 proves that impossible. Hence there exist absolute constants

```math
\epsilon>0,
\qquad D_0<\infty
```

such that every post-ZF survivor with `D>=D_0` satisfies (E.2).

This is a qualitative strict improvement, not an explicit decimal floor.

---

## 6. Exact target implication

Before this report the sharp report-level endpoint was

```text
lambda=(e_BB+2s_C)/D >= lambda_*=0.588228...
with equality forcing h/D -> pi/2.
```

It is now

```text
lambda >= lambda_* + epsilon
for some absolute epsilon>0.
```

The equality mechanism also identifies the rejected endpoint geometry:

```text
h/D -> pi/2,
d_H+s_Z=o(D),
s_C=o(D),
e_BB/D -> lambda_*,
q/D -> pi/2,
c_I/D -> pi/2-lambda_*,
per(F)/D -> pi,
normalized F -> radius-1/2 disk.
```

The contradiction comes from the disk area, not from an unsupported assumption of force-hull saturation.

---

## 7. Regression audit

### Regular odd shell

The regular odd shell has centrally symmetric limits only after the odd cycle becomes dense, and its normalized hull tends to the disk with perimeter `pi`. It is not excluded merely by Section 3. The contradiction uses the **simultaneous FSJC endpoint currency** `lambda=lambda_*`, which the shell does not satisfy.

### Dense isolated shell fillings

The proof does not assume that all source points lie in the force hull or that the force-visible core has full population. FSDB/FS.4 already transported the needed full-source geometry to the force hull. Dense isolates therefore do not invalidate the argument.

### Perfect matching

Already excluded by MFS. The present argument concerns the much different `h/D->pi/2`, `d_H=o(D)` endpoint, where the diameter graph has asymptotically one unicyclic component rather than many tree components.

### Non-disk constant-width bodies

Cauchy equality alone would allow Reuleaux-type constant-width limits. FS.4 central symmetry is essential: a centrally symmetric body of constant width is a disk.

---

## 8. Failed routes and cautions

1. `per(F)/D->pi` alone does **not** imply a disk limit. Constant-width non-disk bodies are counterexamples.
2. FS.4 alone does **not** imply a disk limit. Centrally symmetric diameter-one polygons are counterexamples.
3. The contradiction needs both conclusions simultaneously, and the common-center Hausdorff estimate must be applied to the same force hull used by FSJC.
4. No explicit value of `epsilon` is claimed. Obtaining one requires a quantitative stability version of Section 3.
5. Level I remains open: large pinned/contact surplus above the excluded endpoint remains feasible under the current inequalities.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.** The proof uses only current report-level FSDB/FSJC/ZK/JC and the audited FS.4 common-center theorem. If those dependencies are promoted, this report should replace the weak endpoint-localization statement by the strict qualitative gap (E.2).

No change to Level I status is warranted.

---

## 10. Next theorem

There are two high-value continuations.

1. Quantify the compactness argument. Combine FS.4's explicit `O(D^{-1/4})` central-symmetry error with a quantitative perimeter-to-constant-width stability theorem to obtain an explicit `epsilon` above `lambda_*`.
2. Use the endpoint normal-form derivation before the final contradiction as a template for a wider interval: show that every `lambda` near `lambda_*` forces `d_H+s_Z`, `s_C`, and `pi D-per(F)` to be small in terms of `lambda-lambda_*`, then feed those small defects into the mixed rigidity/contact topology. This may eliminate a whole interval rather than only the exact endpoint.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let lambda=(e_BB+2s_C)/D. FSJC gives lambda>=lambda_* and says
lambda->lambda_* forces h/D->pi/2.

Retain the exact ZK correction k=d_H+s_Z:
  G/D^2 >= Phi(pi/2) - (pi/4)(lambda_*-3k/D)^2 - o(1).
Retain actual e_BB and actual force-hull perimeter in JC:
  G/D^2 <= [e_BB/D + min(pi/2, per(F)/D-pi/2)]^2/(4pi)+o(1).
At lambda=lambda_*, the relaxed lower and upper bounds are exactly equal.
Therefore equality forces
  k/D->0,
  e_BB/D->lambda_*,
  s_C/D->0,
  per(F)/D->pi.
Also q/D->pi/2 and ZU gives
  c_I/D->pi/2-lambda_*=0.9825679830...

FS.4 gives normalized central symmetry of F. Since per(F)/D->pi and diam(F)=D,
any normalized convex limit has diameter 1, perimeter pi, and central symmetry.
Cauchy width equality gives constant width 1; central symmetry then forces the
radius-1/2 disk. Hence area(F)/D^2->pi/4.

With disk area, GU gives
  liminf G/D^2 >= (pi/4)(1-lambda_*^2),
while JC gives
  limsup G/D^2 <= (lambda_*+pi/2)^2/(4pi).
Their exact difference is
  (pi-2)/8 > 0,
a contradiction.

Therefore no sequence can attain lambda_*. By compactness/diagonalization there is
an absolute epsilon>0 such that every sufficiently large post-ZF survivor has
  (e_BB+2s_C)/D >= lambda_*+epsilon.

Next: make epsilon explicit or derive quantitative near-endpoint normal form.
```
