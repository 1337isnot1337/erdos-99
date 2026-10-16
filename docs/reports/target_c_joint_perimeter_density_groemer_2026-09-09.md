<!-- migration-source: path=docs/reports/target_c_joint_perimeter_density_groemer_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=5760191f795c2ed543e50c37fd3fa02a0b7ea859; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — PDG: jointly optimize force-hull perimeter and diameter density

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** two-parameter feasible-region optimization / convex stability synthesis  
**Target:** Target C C-II after ZF/DB/PI/JC/GS  
**Depends on:** DJC, PI, JC actual-perimeter cavity bound, GU/ZG gap charging, Groemer stability as already audited in GS, Blaschke--Lebesgue as already audited in GS  
**New external literature:** none  
**Computation:** decimal evaluation of an explicit one-dimensional crossover; the structural minimization is analytic

## LEVEL I STATUS

**STILL OPEN.**

DJC keeps the actual diameter-edge density

\[
y=\frac hD
\]

in the PI area lower bound and the JC cavity upper bound, raising the post-ZF pinned/contact floor to `0.465351845396...`.

There is another variable that should not be discarded:

\[
p=\frac{\operatorname{per}(F)}D.
\]

JC's proof before the Cauchy relaxation uses `min{h,per(F)-h}`, while Groemer makes the force-hull area rise sharply when `p` approaches `pi`. Keeping `p` and `y` simultaneously yields a stronger universal floor.

The resulting optimized constant is

\[
\boxed{
\lambda_{PDG}
=0.4668176044029515745\ldots,
}
\tag{PDG.1}

where the exact constant is defined below by a unique scalar crossover equation. In particular the rational split certificate in Section 7 proves unconditionally that

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge0.4668175.
}
\tag{PDG.2}

This improves current-main GS by about `0.00202535` and DJC by about `0.00146576`.

---

## 1. Subsequence variables and constraints

Pass to an unbounded post-ZF subsequence on which

\[
y:=\lim\frac hD,
\qquad
p:=\lim\frac{\operatorname{per}(F)}D,
\qquad
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D
\tag{1.1}
\]

exist.

DB and the diameter-thrackle bound give

\[
2\rho\le y,
\qquad
\rho=\cos\rho.
\tag{1.2}

The loaded terminals are the convex-hull vertices and consecutive source points are at distance at least one, so

\[
q\le\operatorname{per}(F).
\]

Since `h<=q`,

\[
\boxed{2\rho\le y\le p\le\pi.}
\tag{PDG.3}

Finally

\[
\boxed{0\le t\le\lambda.}
\tag{PDG.4}

---

## 2. The joint necessary inequality

PI gives the density-sensitive area floor

\[
A_{PI}(y)
:=
\begin{cases}
\frac12\sin y,&y\le\pi/2,\\[3pt]
\frac12,&y\ge\pi/2.
\end{cases}
\tag{2.1}

so

\[
\liminf\frac{\operatorname{area}(F)}{D^2}
\ge A_{PI}(y).
\tag{2.2}

If `p` is sufficiently close to `pi`, apply the already-audited Groemer theorem with the actual perimeter deficit

\[
\varepsilon:=\pi-p.
\]

Put

\[
c_G:=\frac{34}{25},
\qquad
\delta(p):=c_G(\pi-p)^{2/3},
\tag{2.3}
\]

and

\[
\boxed{
A_G(p)
:=
A_{BL}-\pi\delta(p)-\pi\delta(p)^2,
\qquad
A_{BL}:=\frac{\pi-\sqrt3}{2}.
}
\tag{2.4}

Then Groemer plus Steiner and Blaschke--Lebesgue gives

\[
\frac{\operatorname{area}(F)}{D^2}
\ge A_G(p)-o(1).
\tag{2.5}

GU subtracts at most

\[
\frac\pi4\lambda^2D^2+o(D^2)
\]

for the attachment cells.

On the other side, JC before replacing the actual perimeter by `pi D` gives

\[
\limsup\frac GD^2
\le
\frac{(t+\min\{y,p-y\})^2}{4\pi}.
\tag{2.6}

Using `t<=lambda`, every survivor satisfies

\[
\boxed{
A-\frac\pi4\lambda^2
\le
\frac{(\lambda+m)^2}{4\pi},
}
\tag{PDG.5}

where one may take

\[
A=A_{PI}(y)
\]

always, and in the near-perimeter range also

\[
A=\max\{A_{PI}(y),A_G(p)\},
\]

while

\[
\boxed{m=\min\{y,p-y\}.}
\tag{2.7}

For fixed `A,m`, let `R(A,m)` denote the positive root of equality in PDG.5. Explicitly,

\[
\boxed{
R(A,m)
=
\frac{
-2m+
\sqrt{4m^2-4(\pi^2+1)(m^2-4\pi A)}
}{2(\pi^2+1)}.
}
\tag{PDG.6}

It is strictly increasing in `A` and strictly decreasing in `m`.

---

## 3. For fixed perimeter, the PI-only worst density is explicit

First ignore Groemer and use only `A_PI(y)`.

### Case `p<=4rho`

Then

\[
p/2\le2\rho\le y.
\]

Hence throughout the allowed density interval

\[
m=p-y.
\]

As `y` increases, `A_PI(y)` is nondecreasing while `m` decreases. Both changes increase the required root. Therefore the smallest PI-only root occurs at

\[
\boxed{y=2\rho.}
\tag{PDG.7}

### Case `p>=4rho`

Now `p/2>=2rho` is allowed.

For `2rho<=y<=p/2`, one has `m=y`. DJC proves the PI/JC root is strictly decreasing in `y` on this interval.

For `y>=p/2`, one has `m=p-y`. Then `A_PI(y)` is nondecreasing and `m` strictly decreases, so the required root strictly increases.

Therefore the unique fixed-`p` PI-only minimizer is

\[
\boxed{y=p/2.}
\tag{PDG.8}

Define the optimized PI-only perimeter function

\[
L_{PI}(p):=
\begin{cases}
R(A_{PI}(2\rho),p-2\rho),&2\rho\le p\le4\rho,\\[4pt]
R(\frac12\sin(p/2),p/2),&4\rho\le p\le\pi.
\end{cases}
\tag{3.1}

The first branch decreases because its area is fixed while `m=p-2rho` increases. The second decreases by DJC after substituting `y=p/2`.

Thus

\[
\boxed{L_{PI}(p)\text{ is decreasing on }[2\rho,\pi].}
\tag{PDG.9}

---

## 4. Groemer takes over near `pi`

For the near-perimeter branch, use `A_G(p)` independently of `y`. Since

\[
m=\min\{y,p-y\}\le p/2,
\]

PDG.5 implies the weaker but density-free necessary bound

\[
\lambda\ge L_G(p):=R(A_G(p),p/2).
\tag{4.1}

We only need this for

\[
p>\pi-0.0096,
\]

the same explicit neighborhood already used in GS.

On that interval,

\[
A_G'(p)
=
\frac{2\pi c_G}{3}(\pi-p)^{-1/3}
\left(1+2c_G(\pi-p)^{2/3}\right).
\tag{4.2}

Since `pi-p<0.01`, `c_G>1`, and `0.01^{-1/3}>4`,

\[
A_G'(p)>\frac{8\pi}{3}>8.
\tag{4.3}

At the root `L_G(p)`, the nonnegative right side of PDG.5 gives

\[
\frac\pi4L_G(p)^2\le A_G(p)\le A_{BL}<1,
\]

so `L_G(p)<2`; also `p/2<2`. Therefore

\[
\frac{L_G(p)+p/2}{4\pi}<1.
\]

For

\[
F(p,\lambda)
:=
A_G(p)-\frac\pi4\lambda^2
-\frac{(\lambda+p/2)^2}{4\pi},
\]

we have

\[
F_p
=A_G'(p)-\frac{\lambda+p/2}{4\pi}>0,
\qquad
F_\lambda<0.
\]

Implicit differentiation therefore gives

\[
\boxed{L_G'(p)>0.}
\tag{PDG.10}

So PI's optimized requirement decreases with perimeter, while Groemer's requirement increases sharply once the perimeter is close to maximal.

---

## 5. Unique crossover and global optimizer

On the interval

\[
\pi-0.0096<p<\pi-0.0095,
\]

we have `p>4rho`, so the PI optimizer is `y=p/2`.

Consider

\[
H(p):=A_G(p)-\frac12\sin(p/2).
\tag{5.1}

The derivative satisfies

\[
H'(p)
=A_G'(p)-\frac14\cos(p/2)>0
\]

throughout this interval by (4.3). Direct interval evaluation at the two rational perimeter deficits gives

\[
H(\pi-0.0096)<0,
\qquad
H(\pi-0.0095)>0.
\]

Hence there is a unique

\[
\boxed{p_0\in(\pi-0.0096,\pi-0.0095)}
\tag{PDG.11}

such that

\[
\boxed{
A_G(p_0)=\frac12\sin(p_0/2).
}
\tag{PDG.12}

Numerically,

\[
\boxed{
\pi-p_0
=0.0095953786945277566646\ldots,
}
\tag{PDG.13}

\[
\boxed{
p_0
=3.1319972748952654818\ldots .}
\tag{PDG.14}

For `p<=p_0`, PI alone gives

\[
\lambda\ge L_{PI}(p)\ge L_{PI}(p_0).
\]

For `p>=p_0`, Groemer gives

\[
\lambda\ge L_G(p)\ge L_G(p_0).
\]

At the crossover the two area floors agree and `y=p_0/2`, so

\[
L_{PI}(p_0)=L_G(p_0).
\]

Therefore the global minimum over all allowed `(p,y)` is exactly

\[
\boxed{
\lambda_{PDG}
=L_{PI}(p_0)
=L_G(p_0).
}
\tag{PDG.15}

Numerically,

\[
\boxed{
\lambda_{PDG}
=0.4668176044029515745016456013\ldots .
}
\tag{PDG.16}

The associated worst density is

\[
\boxed{
y_0=p_0/2=1.5659986374476327409\ldots,}
\tag{PDG.17}

slightly below `pi/2`.

---

## 6. Symbolic characterization of the constant

The optimized constant is defined without decimal approximation by the unique solution `p_0` of PDG.12 in the interval PDG.11, followed by the positive root `lambda` of

\[
\boxed{
\frac12\sin(p_0/2)-\frac\pi4\lambda^2
=
\frac{(\lambda+p_0/2)^2}{4\pi}.
}
\tag{PDG.18}

Equivalently,

\[
(\pi^2+1)\lambda^2
+p_0\lambda
+\frac{p_0^2}{4}
-2\pi\sin(p_0/2)
=0.
\tag{PDG.19}

This implicit definition is the exact theorem constant. The decimals only identify it numerically.

---

## 7. Rational split certificate

A fully conservative certificate avoids relying on the displayed optimizer digits. Choose

\[
\boxed{
\widehat\varepsilon
=0.00959538
=\frac{479769}{50,000,000},
\qquad
\widehat p=\pi-\widehat\varepsilon.
}
\tag{PDG.20}

For all `p<=p_hat`, monotonicity of `L_PI` gives

\[
\lambda\ge L_{PI}(\widehat p)
=0.4668176046012\ldots .
\]

For all `p>=p_hat`, monotonicity of `L_G` gives

\[
\lambda\ge L_G(\widehat p)
=0.4668175860107\ldots .
\]

Therefore the rational split alone certifies

\[
\boxed{
\lambda\ge0.4668175.
}
\tag{PDG.21}

This is sufficient for a decimal theorem statement even before independently reproducing the higher-precision crossover.

---

## 8. Improvement over the previous frontier

The relevant explicit floors are now

\[
\lambda_{JC}=0.4633168954\ldots,
\]

\[
\lambda_{GS}=0.4647922504\ldots,
\]

\[
\lambda_{DJC}=0.4653518454\ldots,
\]

and

\[
\boxed{\lambda_{PDG}=0.4668176044\ldots .}
\]

The improvement over current-main GS is approximately

\[
\boxed{0.0020253540.}
\tag{PDG.22}

The gain comes from retaining both variables that the earlier one-dimensional relaxations discarded:

1. actual diameter density controls the PI area floor;
2. actual force-hull perimeter controls the complementary JC cavity budget and, near `pi`, activates Groemer stability.

---

## 9. Near-equality normal form

A survivor approaching the PDG floor must force simultaneous near-equality in the monotone reductions. In particular it must have

\[
\boxed{
\frac{\operatorname{per}(F)}D\to p_0,
\qquad
\frac hD\to\frac{p_0}{2}.
}
\tag{PDG.23}

Moreover the two independent area lower bounds meet:

\[
\frac{\operatorname{area}(F)}{D^2}
\to
A_0
:=
\frac12\sin(p_0/2)
=A_G(p_0)
=0.4999942455552\ldots .
\tag{PDG.24}

Thus the hardest surviving scalar geometry is extremely specific:

- force-hull perimeter deficit about `0.00959538 D` from the Rosenthal--Szasz maximum;
- diameter-edge density about `1.56599864 D`;
- force-hull area about `0.49999425 D^2`;
- the PI two-diameter area floor and Groemer/constant-width stability floor meet to first order;
- the JC joint cavity capacity must also be nearly saturated.

This is a much narrower target than the generic high-surplus branch.

---

## 10. Audit and caveats

- Groemer is used only for `pi-p<=0.0096`, exactly within the explicit near-perimeter regime already used in GS.
- The PI-only fixed-perimeter optimization treats separately `p<=4rho` and `p>=4rho`; no assumption `y=p/2` is made outside its valid range.
- `m<=p/2` is used only in the Groemer branch as a weakening, so it cannot invalidate the lower bound.
- The relaxation `t<=lambda` remains. A pinned-stress-dominated survivor is more constrained than PDG records.
- No Level I contradiction follows from the scalar floor alone.
- The exact optimizer is implicit. The rational split PDG.20 independently certifies the conservative bound PDG.21.

---

## 11. Classification

**Status:** proved report-level quantitative refinement of the existing PI/JC/GS feasible region.  
**Level I:** still open.  
**New external literature:** none; Groemer and Blaschke--Lebesgue were already imported and audited by GS.  
**Computation:** scalar evaluation only.

## 12. Next exact target

Attack the PDG near-equality geometry rather than further scalar relaxation.

A useful sufficient theorem is:

> **PDG incompatibility.** There is an absolute `c>0` such that no sufficiently large post-ZF survivor can simultaneously have perimeter density within `o(1)` of `p_0`, diameter density within `o(1)` of `p_0/2`, force-hull area within `o(1)` of both the PI and Groemer lower floors, and joint cavity area within `o(D^2)` of the JC isoperimetric upper capacity.

Any fixed incompatibility raises the pinned/contact floor again. A sufficiently strong incompatibility may force a stable near-constant-width shell or a strict sub-`D` competitor.

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

PDG retains both
    y=h/D,
    p=per(F)/D.
Constraints: 2rho<=y<=p<=pi.

For fixed p, PI-only optimization gives the hardest y:
    y=2rho            if p<=4rho,
    y=p/2             if p>=4rho.
The resulting PI-only required surplus L_PI(p) decreases with p.

Near p=pi, Groemer gives
    A_G(p)=A_BL-pi*delta-pi*delta^2,
    delta=(34/25)(pi-p)^(2/3).
Using min(y,p-y)<=p/2 gives a Groemer required surplus L_G(p), which increases
strictly for pi-p<0.0096.

There is a unique crossover p_0 in (pi-0.0096,pi-0.0095) where
    A_G(p_0)=0.5 sin(p_0/2).
Numerically
    pi-p_0 = 0.0095953786945277567...,
    p_0    = 3.13199727489526548...,
    y_0    = p_0/2,
    lambda = 0.4668176044029515745....

Hence
    liminf (e_BB+2s_C)/D >= lambda_PDG.
The rational split epsilon=479769/50,000,000 independently certifies >=0.4668175.

Near equality now forces a very specific joint perimeter/density/area/cavity regime.
```
