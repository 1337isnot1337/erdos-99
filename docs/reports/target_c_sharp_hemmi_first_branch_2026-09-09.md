<!-- theorem-state: {"artifact_id":"ART-737E85AAB988","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — HKS: sharp Hemmi first branch raises the post-ZF surplus floor to 0.48072

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** sharp external convex-geometry import + exact Target C optimization  
**Target:** Target C C-II after ZF/PI/JC  
**Depends on:** PDG fixed-perimeter PI/JC optimization; the sharp first Hemmi perimeter-diameter area branch  
**Computation:** scalar evaluation only; all geometry and monotonicity are analytic  
**New external literature:** Hemmi 1954, independently located on J-STAGE; Kripfganz 2003 used for the clean modern statement

## LEVEL I STATUS

**STILL OPEN.**

HKI imported only Hemmi's coarse inequality above the regular-hexagon perimeter

\[
p_2:=12\sin\frac{\pi}{12}.
\]

That left an artificial gap immediately below `p_2`. Hemmi's actual sharp solution gives an explicit lower-area formula throughout

\[
3D<L\le p_2D.
\]

After simplifying its parameterization, the sharp normalized area floor is the elementary quadratic

\[
\boxed{
A_H(p)
=3\left(\frac p{p_2}\right)^2
-\frac{3+\sqrt3}{2},
\qquad 3<p\le p_2,
}
\tag{HKS.1}

where `p=L/D`.

Combining `A_H(p)` with the existing PI area floor and JC actual-perimeter cavity bound gives a unique crossover

\[
\boxed{
p_c=3.0353123194039776374\ldots}
\tag{HKS.2}

at which

\[
A_H(p_c)=\frac12\sin\frac{p_c}{2}.
\]

The universal post-ZF pinned/contact surplus floor becomes

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{HKS}
=0.4807218393889119189\ldots .
}
\tag{HKS.3}

This is a substantial improvement over HKI `0.4707353395...`, PDG `0.4668176044...`, and current-main GS `0.4647922504...`.

---

## 1. External theorem: sharp first Hemmi branch

### Primary provenance

Denzaburo Hemmi, *The Minimum Area of Convex Curves for Given Diameter and Perimeter*, Proceedings of the Japan Academy 30 (1954), no. 9, 791–796, DOI `10.3792/pja/1195525912`.

The original paper is freely available through J-STAGE. On pp. 795–796 it divides the solved `3D<L<pi D` problem into cases and gives, for the first case

\[
3D<L<12D\sin\frac{\pi}{12},
\]

a sharp parametric lower-area inequality.

### Clean modern statement checked

Anita Kripfganz, *Hemmi–Polyeder*, Habilitationsschrift, Universität Leipzig, 2003, Chapter 5, Section 5.4.

Kripfganz states that the isoperimetric-isodiametric problem is quantitatively completely solved and that the following lower bounds are attained by Hemmi polyhedra. For

\[
3D<L\le 12D\sin\frac{\pi}{12},
\]

she gives

\[
\boxed{
F\ge
\left[
\frac32\sin\alpha
+\frac32\sin\left(\frac\pi3-\alpha\right)
-\frac{\sqrt3}{2}
\right]D^2,
}
\tag{HKS.4}

where

\[
\alpha\in\left[\frac\pi6,\frac\pi3\right)
\]

is determined by

\[
\boxed{
3\left[
\sin\frac\alpha2
+\sin\left(\frac\pi6-\frac\alpha2\right)
\right]
=\frac{L}{2D}.
}
\tag{HKS.5}

This is the only new external theorem used below.

---

## 2. Eliminate the Hemmi parameter exactly

Put

\[
p:=\frac LD,
\qquad
p_2:=12\sin\frac\pi{12}.
\]

Use

\[
\sin u+\sin v
=2\sin\frac{u+v}{2}\cos\frac{u-v}{2}.
\]

Equation HKS.5 becomes

\[
\frac p2
=6\sin\frac\pi{12}
\cos\left(\frac\alpha2-\frac\pi{12}\right).
\]

Hence, writing

\[
\theta:=\frac\alpha2-\frac\pi{12}\in[0,\pi/12),
\]

we have

\[
\boxed{
p=p_2\cos\theta.}
\tag{HKS.6}

For the area term,

\[
\sin\alpha+\sin\left(\frac\pi3-\alpha\right)
=\cos\left(\alpha-\frac\pi6\right)
=\cos(2\theta).
\]

Since

\[
\cos(2\theta)=2\cos^2\theta-1
=2\left(\frac p{p_2}\right)^2-1,
\]

HKS.4 becomes

\[
\begin{aligned}
\frac F{D^2}
&\ge
\frac32\left[2\left(\frac p{p_2}\right)^2-1\right]
-\frac{\sqrt3}{2}\\
&=
3\left(\frac p{p_2}\right)^2
-\frac{3+\sqrt3}{2}.
\end{aligned}
\]

This proves HKS.1.

At `p=3`, HKS.1 tends to the equilateral-triangle area `sqrt(3)/4`; at `p=p_2`, it gives `(3-sqrt(3))/2`, so the endpoint checks agree with the known extremal figures.

---

## 3. Compare the sharp Hemmi floor with PI

For fixed perimeter `p`, PDG proves that the PI/JC required surplus is minimized at

\[
y=\frac p2
\]

whenever `p>=4rho`. The entire interval used below satisfies this, because

\[
3>4\rho.
\]

The PI area floor at the fixed-perimeter optimizer is therefore

\[
\boxed{
A_{PI}^*(p)=\frac12\sin\frac p2,
\qquad 3\le p\le p_2<\pi.
}
\tag{3.1}

Define

\[
\Phi(p):=A_H(p)-A_{PI}^*(p).
\]

Then

\[
\Phi(3)<0,
\qquad
\Phi(p_2)>0.
\]

Moreover

\[
\Phi'(p)
=
\frac{6p}{p_2^2}
-\frac14\cos\frac p2.
\]

On `p>=3`, use `p_2<pi`, `pi^2<10`, and `cos(p/2)<=1` to obtain

\[
\Phi'(p)
>
\frac{18}{10}-\frac14
>0.
\]

Thus there is a **unique** crossover

\[
\boxed{p_c\in(3,p_2)}
\tag{HKS.7}

satisfying

\[
\boxed{
3\left(\frac{p_c}{p_2}\right)^2
-\frac{3+\sqrt3}{2}
=
\frac12\sin\frac{p_c}{2}.
}
\tag{HKS.8}

Numerically this is HKS.2.

Below `p_c`, PI is the stronger area floor. Above `p_c`, sharp Hemmi is stronger.

---

## 4. The required surplus decreases up to the crossover

For `p<=p_c`, simply use the PI/JC bound and ignore Hemmi.

PDG already proves that the optimized PI-only required surplus function `L_PI(p)` is decreasing in `p`. Therefore

\[
\boxed{
p\le p_c\quad\Longrightarrow\quad
\lambda\ge L_{PI}(p)\ge L_{PI}(p_c).}
\tag{HKS.9}

Here and below

\[
\lambda:=\lim\frac{e_{BB}+2s_C}{D}
\]

on a convergent post-ZF subsequence.

At `p_c`, the minimizing density is `y=p_c/2`, so the JC term has

\[
m=\min\{y,p-y\}=p_c/2.
\]

---

## 5. The Hemmi/JC required surplus increases after the crossover

For `p_c<=p<=p_2`, use the sharp area floor `A_H(p)`.

JC gives

\[
m=\min\{y,p-y\}\le\frac p2.
\]

Using the weaker `m=p/2` therefore gives the valid necessary inequality

\[
A_H(p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+p/2)^2}{4\pi}.
\tag{5.1}

Let `L_H(p)` be the positive root of equality.

Define

\[
F(p,\lambda)
:=
A_H(p)
-\frac\pi4\lambda^2
-\frac{(\lambda+p/2)^2}{4\pi}.
\]

We have

\[
F_\lambda<0.
\]

Also

\[
F_p
=
\frac{6p}{p_2^2}
-\frac{\lambda+p/2}{4\pi}.
\]

At the positive root, the nonnegative cavity term implies

\[
\frac\pi4\lambda^2\le A_H(p)<1,
\]

so `lambda<2`. Also `p/2<pi/2<2`. Therefore

\[
\frac{\lambda+p/2}{4\pi}<\frac4{12}=\frac13.
\]

Meanwhile

\[
\frac{6p}{p_2^2}
>\frac{18}{10}.
\]

Hence

\[
F_p>0.
\]

Implicit differentiation gives

\[
\boxed{L_H'(p)>0.}
\tag{HKS.10}

Therefore

\[
\boxed{
p_c\le p\le p_2
\quad\Longrightarrow\quad
\lambda\ge L_H(p)\ge L_H(p_c).}
\tag{HKS.11}

At `p_c`, the PI and Hemmi area floors agree, so

\[
L_H(p_c)=L_{PI}(p_c).
\]

---

## 6. Perimeters above `p_2` are safely separated

For `p>=p_2`, the coarse Hemmi inequality already imported in HKI gives the uniform area floor

\[
\frac F{D^2}\ge\frac{3-\sqrt3}{2}.
\]

The deliberately weakened JC estimate `m<=pi/2` then gives

\[
\lambda\ge0.5813130664\ldots,
\]

which is far above the crossover value derived below.

Thus the universal minimum cannot occur for `p>=p_2`.

---

## 7. Exact crossover constant

At `p=p_c`, put

\[
A_c:=rac12\sin\frac{p_c}{2}
=A_H(p_c),
\qquad
m_c:=\frac{p_c}{2}.
\]

The necessary PI/JC equality is

\[
A_c-\frac\pi4\lambda^2
=
\frac{(\lambda+m_c)^2}{4\pi}.
\tag{7.1}

Equivalently,

\[
\boxed{
(\pi^2+1)\lambda^2
+p_c\lambda
+\frac{p_c^2}{4}
-2\pi\sin\frac{p_c}{2}
=0.
}
\tag{HKS.12}

Let `lambda_HKS` be its positive root. Then

\[
\boxed{
\lambda_{HKS}
=0.4807218393889119189819710\ldots .
}
\tag{HKS.13}

Combining Sections 4–6 proves HKS.3.

---

## 8. Rational crossover certificate

For a completely conservative decimal certificate, choose

\[
\boxed{\widehat p=3.03531232.}
\tag{HKS.14}

This lies slightly above the unique crossover.

For all `p<=p_hat`, monotonicity of the PI-only requirement gives

\[
\lambda\ge L_{PI}(\widehat p)
=0.4807218393079660\ldots .
\]

For all `p>=p_hat` but `p<=p_2`, monotonicity of the Hemmi requirement gives

\[
\lambda\ge L_H(\widehat p)
=0.4807218403491543\ldots .
\]

For `p>=p_2`, Section 6 is much stronger.

Therefore the rational split certifies

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4807218.
}
\tag{HKS.15}

The higher-precision HKS.13 is the unique analytic crossover value.

---

## 9. Structural meaning of the new worst case

The coarse HKI threshold was artificial. HKS removes it and identifies a true competition between two independent lower-area mechanisms.

A sequence approaching the new scalar floor must have

\[
\boxed{
\frac{\operatorname{per}(F)}D\to p_c
=3.0353123194\ldots,
}
\tag{HKS.16}

and, by tightness of the fixed-perimeter PI optimization,

\[
\boxed{
\frac hD\to\frac{p_c}{2}
=1.5176561597\ldots .
}
\tag{HKS.17}

The force-hull area floor at the crossover is

\[
\boxed{
\frac{\operatorname{area}(F)}{D^2}
\gtrsim
A_c
=0.4992941967756003\ldots .
}
\tag{HKS.18}

Near equality must make **both** the PI diameter-direction area floor and the sharp Hemmi perimeter-diameter area floor simultaneously tight, while also nearly saturating JC's cavity estimate.

That is a much more rigid geometric normal form than the previous high-surplus statement.

---

## 10. Source audit

### Primary paper independently located

D. Hemmi, *The Minimum Area of Convex Curves for Given Diameter and Perimeter*, Proceedings of the Japan Academy 30 (1954), no. 9, 791–796, DOI `10.3792/pja/1195525912`, available from J-STAGE.

The original paper states that the `(L,D)` problem for `3D<L<pi D` is solved and lists the first case

\[
3D<L<12D\sin(\pi/12)
\]

with the corresponding parametric sharp inequality.

### Modern formula source

A. Kripfganz, *Hemmi–Polyeder*, Habilitationsschrift, Universität Leipzig, 2003, Section 5.4. The thesis states that the isoperimetric-isodiametric problem is quantitatively completely solved and reproduces HKS.4–HKS.5 as the first sharp case.

The Kripfganz PDF text and the relevant formula/range were inspected directly. A PDF screenshot attempt on the formula page failed because of a source cache miss; the parsed PDF lines and the independent original Hemmi paper agree on the case/range.

---

## 11. Regression audit

### Perimeter below 3D

No Hemmi first-branch statement is used. PI/JC alone is stronger near `p=3` and its optimized requirement is decreasing toward the crossover.

### Perimeter exactly at p2

Both the sharp first branch and the coarse n=2 Hemmi inequality are compatible with the regular-hexagon endpoint. The high-perimeter bound is much stronger than HKS.13.

### Force hull is polygonal

Hemmi's theorem is for arbitrary planar convex figures, so the convex polygonal force hull is included.

### Diameter is exactly D

The force hull contains endpoints of actual diameter pairs and lies inside the source convex hull, hence its diameter is exactly `D`.

### No false continuity argument

Unlike HKI, HKS uses the actual sharp first branch on the whole interval from `3D` to `p_2D`; there is no artificial threshold jump in the optimized range.

---

## 12. Classification

**Status:** proved Target C consequence conditional on a classical sharp Hemmi theorem; primary provenance independently located and modern formula checked.  
**Level I:** still open.  
**New external literature:** yes.  
**Computation:** scalar decimal evaluation only.

## 13. Next exact target

The global scalar worst case has moved into the interior of Hemmi's first branch. The next theorem should exploit **simultaneous near-equality** of:

1. PI at `y=p_c/2`;
2. the sharp Hemmi first-branch area inequality at `p=p_c`;
3. JC's joint pocket/exceptional cavity capacity; and
4. the relaxation `t=e_BB/D<=lambda`.

The sharp Hemmi extremizer in this branch is a six-sided Hemmi polyhedron with three sides of each of two alternating lengths. PI near-equality simultaneously requires the active diameter-direction span to generate nearly the same area. A direct incompatibility between those two equality geometries would raise the floor again and could potentially force a stable finite shell class.

## 14. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Sharp Hemmi first branch:
For 3<p=L/D<=p2=12 sin(pi/12), Kripfganz/Hemmi gives
  area/D^2 >= (3/2)[sin alpha + sin(pi/3-alpha)] - sqrt(3)/2,
  3[sin(alpha/2)+sin(pi/6-alpha/2)] = p/2.
Set theta=alpha/2-pi/12. Then p=p2 cos theta and the area formula simplifies to
  A_H(p)=3(p/p2)^2-(3+sqrt(3))/2.

PI at the fixed-perimeter optimizer gives
  A_PI*(p)=0.5 sin(p/2).
A_H-A_PI* is strictly increasing, so they cross once at
  p_c=3.0353123194039776374....
Below p_c the PI/JC required surplus decreases with p; above p_c the Hemmi/JC required
surplus increases with p. Hence the universal minimum is the crossover.

At p_c:
  (pi^2+1)lambda^2 + p_c lambda + p_c^2/4 - 2pi sin(p_c/2)=0,
so
  lambda_HKS=0.48072183938891191898....
The rational split p=3.03531232 certifies >=0.4807218.

Near equality now requires simultaneous PI + sharp-Hemmi + JC saturation. The Hemmi
extremizer is a six-sided alternating-side Hemmi polyhedron, giving a concrete equality
geometry for the next attack.
```
