<!-- migration-source: path=docs/reports/target_c_groemer_split_optimization_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e22fdd5323a14134cbfb04aee09d45919dfafc77; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — GS2: optimize the Groemer perimeter split

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-optimize-groemer-surplus`  
**Base:** `cf790155660ad46797e53c7f44371b078f7eab7b`  
**Run type:** exact one-parameter optimization of the GS proof  
**Target:** Target C post-ZF pinned/contact surplus  
**Depends on:** `target_c_groemer_stability_explicit_surplus_2026-09-09.md` only  
**Computation:** high-precision evaluation of one monotone scalar intersection; not used for the symbolic proof

## LEVEL I STATUS

**STILL OPEN.**

The current GS report proves

\[
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.464792250394\ldots
\]

using the deliberately nonoptimized perimeter split

\[
\varepsilon_*=0.0096.
\]

The two branches of that proof move monotonically in opposite directions as the split varies.  Therefore the best constant obtainable from the **same proof with no new geometric input** is obtained at their unique intersection.

The optimized split is

\[
\boxed{
\varepsilon_{opt}
=0.0096338617032600587\ldots
}
\]

and the corresponding universal floor is

\[
\boxed{
\lambda_{GS2}
=0.4647974456553926969\ldots .
}
\]

For an entirely explicit rational split, already

\[
\widehat\varepsilon
=0.0096338617
=\frac{96338617}{10^{10}}
\]

gives

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4647974456.
}
\]

This removes the numerical slack explicitly left in GS.  The improvement is small, as expected from the `epsilon^(2/3)` Groemer stability exponent, but it is rigorous within the existing two-case argument.

---

## 1. The two GS branch functions

Retain the constants

\[
A_{PI}=\frac12\sin(2\rho),
\qquad
A_{BL}=\frac{\pi-\sqrt3}{2},
\qquad
c_G=\frac{34}{25},
\]

where `rho=cos rho`.

For a split parameter

\[
\varepsilon>0,
\]

put

\[
\delta(\varepsilon)
=c_G\varepsilon^{2/3}
\]

and

\[
\boxed{
A_G(\varepsilon)
=A_{BL}-\pi\delta(\varepsilon)-\pi\delta(\varepsilon)^2.
}
\tag{GS2.1}

### Near-perimeter branch

If

\[
p:=\frac{\operatorname{per}(F)}D
\ge\pi-\varepsilon,
\]

Groemer plus Blaschke--Lebesgue gives area at least `A_G(epsilon)D^2`.  The GS cavity argument therefore forces `lambda` above the positive root `lambda_N(epsilon)` of

\[
\boxed{
A_G(\varepsilon)-\frac\pi4\lambda^2
=
\frac{(\lambda+\pi/2)^2}{4\pi}.
}
\tag{GS2.2}

### Far-perimeter branch

If

\[
p\le\pi-\varepsilon,
\]

PI supplies the area floor `A_PI`, while the actual-perimeter cavity bound uses `p<=pi-epsilon`.  Hence `lambda` must exceed the positive root `lambda_F(epsilon)` of

\[
\boxed{
A_{PI}-\frac\pi4\lambda^2
=
\frac{(\lambda+(\pi-\varepsilon)/2)^2}{4\pi}.
}
\tag{GS2.3}

For any chosen split, the GS proof therefore gives

\[
\boxed{
\lambda\ge
L(\varepsilon):=\min\{\lambda_N(\varepsilon),\lambda_F(\varepsilon)\}.
}
\tag{GS2.4}

---

## 2. Closed root formula

For arbitrary area floor `A` and perimeter parameter `p`, define `R(A,p)` as the positive root of

\[
A-\frac\pi4\lambda^2
=
\frac{(\lambda+p/2)^2}{4\pi}.
\]

Multiplication by `4pi` gives

\[
(\pi^2+1)\lambda^2
+p\lambda
+\frac{p^2}{4}
-4\pi A=0.
\]

Thus

\[
\boxed{
R(A,p)
=
\frac{
-p+
\sqrt{p^2-4(\pi^2+1)(p^2/4-4\pi A)}
}{2(\pi^2+1)}.
}
\tag{GS2.5}

Consequently

\[
\lambda_N(\varepsilon)
=R(A_G(\varepsilon),\pi),
\tag{GS2.6}
\]

\[
\lambda_F(\varepsilon)
=R(A_{PI},\pi-\varepsilon).
\tag{GS2.7}

---

## 3. Monotonicity makes the optimization one-dimensional and exact

The function `A_G(epsilon)` is strictly decreasing for `epsilon>0`, because both `delta` and `delta^2` increase strictly.

For fixed `p`, the positive root `R(A,p)` is strictly increasing in `A`: in the defining equation, increasing the left area floor shifts the unique positive intersection to larger `lambda`.  Therefore

\[
\boxed{
\lambda_N(\varepsilon)
\text{ is strictly decreasing.}
}
\tag{GS2.8}

For the far branch, fix `A=A_PI`.  At fixed `lambda>=0`, the right side

\[
\frac{(\lambda+p/2)^2}{4\pi}
\]

is strictly increasing in `p`.  Since the left-minus-right side is strictly decreasing in `lambda`, decreasing `p=pi-epsilon` shifts its unique zero to larger `lambda`.  Hence

\[
\boxed{
\lambda_F(\varepsilon)
\text{ is strictly increasing.}
}
\tag{GS2.9}

At `epsilon=0.0096`, the current GS report gives

\[
\lambda_N=0.4652804\ldots
>
0.4647922\ldots=\lambda_F.
\]

At `epsilon=0.01`, direct substitution gives

\[
\lambda_N=0.45957\ldots
<
0.46485\ldots=\lambda_F.
\]

Continuity and strict monotonicity imply that there is a **unique**

\[
\varepsilon_{opt}\in(0.0096,0.01)
\]

with

\[
\boxed{
\lambda_N(\varepsilon_{opt})
=\lambda_F(\varepsilon_{opt}).
}
\tag{GS2.10}

Because one branch decreases and the other increases, `L(epsilon)` increases up to this point and decreases afterward.  Therefore this intersection is the unique global maximizer of the two-case GS bound.

No numerical optimization theorem is needed; only monotonicity is used.

---

## 4. Optimized value

Solving the monotone scalar equation GS2.10 gives

\[
\boxed{
\varepsilon_{opt}
=0.0096338617032600587291991009\ldots
}
\tag{GS2.11}

At this split,

\[
\delta
=0.0615752022183200159\ldots,
\]

\[
A_G
=0.4994153541645548319\ldots,
\]

and both branch roots equal

\[
\boxed{
\lambda_{GS2}
=0.4647974456553926969496271\ldots .
}
\tag{GS2.12}

Thus the same GS proof, with its split optimized, yields

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
0.4647974456553926\ldots .
}
\tag{GS2.13}

---

## 5. Rational split certificate

To avoid making the theorem depend on the decimal representation of the optimizer, choose the rational

\[
\boxed{
\widehat\varepsilon
=\frac{96338617}{10^{10}}
=0.0096338617.
}
\tag{GS2.14}

Direct substitution in the exact formulas gives

\[
\lambda_N(\widehat\varepsilon)
=0.4647974457018929\ldots,
\]

\[
\lambda_F(\widehat\varepsilon)
=0.4647974456548925\ldots .
\]

Therefore both cases satisfy the conservative explicit bound

\[
\boxed{
\lambda>0.4647974456
}
\tag{GS2.15}

at the subsequential-limit level used by GS, and hence

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4647974456.
}
\tag{GS2.16}

The rational certificate alone is sufficient for the displayed improvement; GS2.11--GS2.13 identify the optimal split within this proof template.

---

## 6. Quantitative effect

The previous explicit GS constant was

\[
0.464792250394\ldots .
\]

The optimized value improves it by

\[
\boxed{
5.195261\times10^{-6}\text{ approximately}.
}
\tag{GS2.17}

This is intentionally characterized as a numerical tightening, not a new geometric phase exclusion.  The small gain confirms GS's explanation: the `2/3` stability exponent makes the near-perimeter area floor deteriorate rapidly as the split moves away from `pi`.

The structural next target therefore remains the simultaneous high-branching/high-loaded-contact state, not further scalar tuning.

---

## 7. Audit and caveats

- No new external theorem is imported; GS2 uses exactly the Groemer/Blaschke--Lebesgue input already audited in GS.
- The symbolic optimization is exact once the GS inequalities are accepted.
- Numerical computation is used only to evaluate the unique scalar intersection and the rational certificate.
- The result does not improve the nonconstructive JN gap, which may be larger.
- No Level I conclusion is claimed.

---

## 8. Classification

**Status:** proved quantitative refinement of the existing GS two-case argument.  
**Level I:** still open.  
**New literature:** none.  
**Computation:** scalar high-precision evaluation only.

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

GS used a nonoptimized split epsilon=0.0096. For a general epsilon define
    delta=(34/25) epsilon^(2/3),
    A_G=A_BL-pi delta-pi delta^2.
The near-perimeter root is
    lambda_N(epsilon)=R(A_G,pi),
and the far-perimeter root is
    lambda_F(epsilon)=R(A_PI,pi-epsilon),
where
    R(A,p)=(-p+sqrt[p^2-4(pi^2+1)(p^2/4-4pi A)])/[2(pi^2+1)].

lambda_N decreases strictly with epsilon; lambda_F increases strictly. Therefore the
best split is their unique intersection:
    epsilon_opt=0.0096338617032600587...,
    lambda_GS2=0.4647974456553926969....

The rational split 96338617/10^10 already certifies
    liminf (e_BB+2s_C)/D >= 0.4647974456.
This closes only the numerical slack in GS; the structural Level I endpoint remains.
```
