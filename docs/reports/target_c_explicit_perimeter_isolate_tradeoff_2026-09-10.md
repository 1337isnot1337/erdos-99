<!-- theorem-state: {"artifact_id":"ART-424246FDFEB6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — explicit force-perimeter and external-isolate tradeoff

**Date:** 2026-09-10  
**Repository state:** PR #178; base `main` now contains `f0e565d92d331c74f672f32b2e2e6c81b587f61e`  
**Run type:** exact synthesis / population transfer  
**Target:** Target C, C-II after ZF  
**Depends on:** FS/FD central symmetral, Rogalski–Saint Raymond transfer from RSJ, GU, actual-perimeter JC, ER, canonical global density asymptotics  
**Computation:** decimals only; all theorem statements use closed forms

## LEVEL I STATUS

`STILL OPEN`

The RSJ report uses the symmetric area--perimeter inequality primarily to raise the
unconditional pinned/contact lower floor to `0.5921405436...`.  Keeping the perimeter
variable gives a different consequence that is more useful for the isolate-heavy
branch.

Put

\[
\lambda_D:=\frac{e_{BB}+2s_C}{D},
\qquad
p_D:=\frac{\operatorname{per}F}{D}.
\]

For every asymptotic pinned/contact level

\[
0\le\lambda<
\lambda_{\rm disk}
:=
\frac{\pi(\sqrt{3\pi^2+4}-1)}{2(\pi^2+1)},
\]

define

\[
a:=\frac{\pi-2}{2},
\qquad
A:=\pi^2-a^2,
\tag{PI.1}
\]

\[
\boxed{
 r_+(\lambda)
 :=
 \frac{
 a(1+\lambda)
 +\pi\sqrt{(1+\lambda)^2+A\lambda^2}
 }{A},
}
\tag{PI.2}
\]

and

\[
\boxed{
p_+(\lambda):=2+(\pi-2)r_+(\lambda).}
\tag{PI.3}
\]

Then any survivor sequence with `lambda_D -> lambda` satisfies

\[
\boxed{
\limsup p_D\le p_+(\lambda)<\pi.
}
\tag{PI.4}
\]

More generally, if `limsup lambda_D<=lambda_0<lambda_disk`, then

\[
\boxed{
\limsup p_D\le p_+(\lambda_0)<\pi.
}
\tag{PI.5}
\]

This turns the qualitative MP perimeter loss into an explicit one.

It also forces an explicit source-population split.  If `Z_ext` is the number of
contact-isolated source points outside the force hull, then

\[
\boxed{
\liminf\frac{Z_{ext}}{D^2}
\ge
\frac{1}{2\pi\sqrt3}
\bigl(\pi^2-p_+(\lambda_0)^2\bigr),
}
\tag{PI.6}
\]

and, since `n/D^2 -> pi/(2sqrt3)`,

\[
\boxed{
\liminf\frac{Z_{ext}}n
\ge
1-\left(\frac{p_+(\lambda_0)}\pi\right)^2.
}
\tag{PI.7}
\]

Thus every post-ZF sequence below the disk threshold either has high
pinned/contact currency or carries a quantitatively positive fraction of completely
contact-isolated source points outside the KKT force hull.

---

## 1. Exact implication chain

The route is

```text
Rogalski-Saint Raymond on the FS/FD central symmetral
    -> area(F)/D^2 >= Psi(p)-o(1)
GU + actual-perimeter JC
    -> Psi(p) <= pi lambda^2/4 + (lambda+p/2)^2/(4pi)
solve the resulting quadratic in normalized perimeter
    -> p <= p_+(lambda) < pi for lambda<lambda_disk
ER + isoperimetry
    -> explicit quadratic external-isolate population
canonical n/D^2 asymptotic
    -> explicit positive external-isolate fraction.
```

No matching approximation, response-trace estimate, small-isolate hypothesis, or
hull-saturation normalization is used.

---

## 2. Perimeter feasibility inequality

RSJ imports the exact Rogalski--Saint Raymond theorem through the FD central
symmetral.  With

\[
c_R=\frac\pi{(\pi-2)^2},
\qquad
\Psi(p)=c_R\left(\frac p2-1\right)^2,
\]

it gives along every convergent subsequence

\[
\liminf\frac{\operatorname{area}F}{D^2}\ge\Psi(p).
\tag{2.1}
\]

GU gives

\[
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{2.2}
\]

The unrelaxed JC estimate gives

\[
\limsup\frac G{D^2}
\le
\frac{(t+m)^2}{4\pi},
\tag{2.3}
\]

where

\[
0\le t\le\lambda,
\qquad
m=\min\{y,p-y\}\le\frac p2.
\]

Since

\[
\operatorname{area}F
=\sum_r\operatorname{area}(P_r)+G,
\]

(2.1)--(2.3) imply the necessary condition

\[
\boxed{
\Psi(p)
\le
\frac\pi4\lambda^2
+\frac{(\lambda+p/2)^2}{4\pi}.
}
\tag{2.4}
\]

This deliberately relaxes the diameter-density variable `y`.  The point is not to
improve RSJ's scalar lower threshold; it is to get a closed-form upper envelope for
`p` at a prescribed `lambda`.

---

## 3. Exact solution for the perimeter envelope

Write

\[
p=2+(\pi-2)r,
\qquad 0\le r\le1.
\tag{3.1}
\]

Then

\[
\Psi(p)=\frac\pi4r^2,
\qquad
\frac p2=1+ar.
\tag{3.2}
\]

Multiply (2.4) by `4pi`:

\[
\pi^2r^2
\le
\pi^2\lambda^2+(1+\lambda+ar)^2.
\]

Equivalently,

\[
\boxed{
A r^2
-2a(1+\lambda)r
-\bigl(\pi^2\lambda^2+(1+\lambda)^2\bigr)
\le0,
}
\tag{3.3}
\]

where `A=pi^2-a^2>0`.

The negative root is irrelevant.  The positive root is

\[
\frac{
 a(1+\lambda)
 +\sqrt{a^2(1+\lambda)^2
 +A(\pi^2\lambda^2+(1+\lambda)^2)}
}{A}.
\]

Because `a^2+A=pi^2`, the radicand simplifies to

\[
\pi^2\bigl((1+\lambda)^2+A\lambda^2\bigr),
\]

which is exactly PI.2.  Thus `r<=r_+(lambda)` and PI.4 follows.

At `r=1`, equation (3.3) becomes

\[
(\pi^2+1)\lambda^2
+\pi\lambda
-\frac{3\pi^2}{4}\ge0.
\tag{3.4}
\]

Its positive root is precisely `lambda_disk`.  Hence

\[
r_+(\lambda)<1,
\qquad
p_+(\lambda)<\pi
\quad\text{for }\lambda<\lambda_{\rm disk}.
\tag{3.5}
\]

The right side of (2.4) is increasing in `lambda`, so `p_+(lambda)` is increasing.
This proves the `limsup lambda_D<=lambda_0` form PI.5.

---

## 4. Explicit external-isolate population

ER gives, for every post-ZF source,

\[
Z_{ext}
>
\frac2{\sqrt3}
\left(
\frac\pi4D^2-\operatorname{area}F
\right)
-\frac12\operatorname{per}F.
\tag{4.1}
\]

Isoperimetry gives

\[
\operatorname{area}F
\le\frac{\operatorname{per}(F)^2}{4\pi}.
\tag{4.2}
\]

Under `limsup lambda_D<=lambda_0<lambda_disk`, PI.5 and (4.2) therefore give

\[
\limsup\frac{\operatorname{area}F}{D^2}
\le\frac{p_+(\lambda_0)^2}{4\pi}.
\tag{4.3}
\]

Divide (4.1) by `D^2`; its perimeter term vanishes.  This yields

\[
\liminf\frac{Z_{ext}}{D^2}
\ge
\frac2{\sqrt3}
\left(
\frac\pi4-
\frac{p_+(\lambda_0)^2}{4\pi}
\right),
\]

which is PI.6.

For global minimizers the canonical upper/lower diameter bounds imply

\[
\frac n{D^2}\longrightarrow\frac\pi{2\sqrt3}.
\tag{4.4}
\]

Dividing PI.6 by (4.4) gives exactly PI.7. `square`

---

## 5. Scale of the forced population

The theorem is exact; the following decimals are only orientation.

| `lambda_0` | `p_+(lambda_0)` | forced `liminf Z_ext/n` |
| ---: | ---: | ---: |
| `0.5921405436063` | `3.020034287526` | `0.0758892933` |
| `0.6000000000000` | `3.029400052854` | `0.0701486800` |
| `0.6200000000000` | `3.053300240543` | `0.0554188415` |
| `0.6500000000000` | `3.089319027373` | `0.0330015606` |
| `0.6800000000000` | `3.125521890293` | `0.0102047975` |
| `0.6900000000000` | `3.137627230911` | `0.0025228733` |

At `lambda_disk` the envelope reaches `pi` and the forced fraction vanishes, exactly
as it must.

The first row should not be read as an attainable endpoint: RSJ independently proves
that its scalar equality point is not attained and obtains a nonexplicit positive gap
above `0.5921405436...`.

---

## 6. Relation to AS and CP

AS proves the sharper structural statement

\[
Z_{ext}
=\frac2{\sqrt3}
\operatorname{area}(K\setminus F)+O(D)
\]

in the low-surplus branch, and external minimum separation

\[
s_{ext}=1+O(D^{-1}).
\]

CP proves for the full source hull

\[
\pi D-P_K<\frac{\pi\sqrt3}{2}.
\]

PI makes the previously nonexplicit MP perimeter loss quantitative.  Combining the
three reports gives, for every fixed `lambda_0<lambda_disk`, an explicit positive
annular/source-population fraction, asymptotic triangular-density saturation of that
annulus, and only an absolute `O(1)` outer source-perimeter defect.

---

## 7. Exact effect on the C-II endpoint

The post-ZF survivor set now has the following quantitative dichotomy:

1. `liminf lambda_D>=lambda_disk`; or
2. along any subsequence with `limsup lambda_D<=lambda_0<lambda_disk`, at least
   \[
   1-\left(p_+(\lambda_0)/\pi\right)^2
   \]
   of all source points are external contact-isolates asymptotically.

The second branch is not merely "many isolates": AS forces those points to saturate
the actual annular area to triangular density up to boundary-order error.

This does not yet give `b+Q>2h`.  A closure must now show that the force-visible mixed
rigidity circuit / boundary-surplus structure cannot coexist with a global source in
which a positive prescribed fraction of all points live in that saturated, strictly
noncontact annulus.

---

## 8. Regression audit

- **Odd shell:** its pinned/contact currency is far above the disk threshold, so PI
  imposes no false isolate conclusion.
- **Dense isolated shell filling:** it can imitate the population split, but lacks the
  ER global-optimality lower bound.  Thus it remains a warning that density alone is
  not the closing theorem.
- **RS equality:** PI uses only the inequality, not its equality characterization.
- **Perfect matching:** unused.
- **Response trace / arbitrary boundary data:** unused.
- **Hull saturation:** not imposed.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| PI.4--PI.5 explicit perimeter envelope | proved | exact RS/GU/JC relaxation and quadratic solution |
| PI.6 external-isolate density | proved | ER plus isoperimetry |
| PI.7 external-isolate fraction | proved | canonical `n/D^2` limit |
| positive fraction alone gives a competitor | not proved | dense-shell regression blocks that inference |
| Level I | still open | high-surplus branch and finite annular compatibility remain |

---

## 10. Next obligation

Use the PI fraction inside a **finite compatibility theorem**, not another density
estimate.  A sufficient result is:

> for some `lambda_0<lambda_disk`, every lexicographically normalized post-ZF source
> with `lambda_D<=lambda_0+o(1)` and the PI/AS saturated external population admits a
> cardinality-preserving replacement of the force-visible core inside diameter `<D`,
> while maintaining unit separation from the retained external points.

The cross-boundary separation is the entire difficulty.  Any proof that simply packs
the core into an eroded copy of `F` loses `Theta(D)` boundary capacity and must show
where that loss is recovered.
