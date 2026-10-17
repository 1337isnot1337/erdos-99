<!-- theorem-state: {"artifact_id":"ART-A988F1770584","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ANS: angle-sensitive nested stability raises the explicit HKS gap

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-density-sensitive-cavity`  
**Run type:** exact finite-angle convex stability optimization  
**Target:** explicit quantitative replacement for HKN using FAQ+NCS  
**Depends on:** FAQ, NCS.1, HKS, PI, JC/GU  
**External literature:** none beyond the already imported Hemmi theorem underlying HKS  
**Computation:** decimal evaluation of one explicit scalar crossover only

## LEVEL I STATUS

**STILL OPEN.**

NCS made the HKN gap explicit by combining the nested-convex area stability lemma with Tamvakis's global quadrilateral perimeter bound. FAQ is stronger because the PI endpoint quadrilateral has a known diagonal angle.

Keeping that angle as a live variable yields the stronger explicit floor

\[
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{ANS}
=0.4807218398270484821385\ldots .
}
\tag{ANS.1}

The increase over HKS is

\[
\boxed{
\lambda_{ANS}-\lambda_{HKS}
=4.3813656316\times10^{-10}\ldots>0.
}
\tag{ANS.2}

The gain is still numerically small, but it is fully explicit and uses the actual PI angle rather than a global four-gon relaxation.

---

## 1. Simplify the FAQ perimeter formula

FAQ proves that a diameter-one quadrilateral with both diagonals of length one and diagonal angle

\[
\phi\in[\pi/3,2\pi/3]
\]

has perimeter at most

\[
2+
\sqrt{2-\sqrt3\sin\phi-\cos\phi}
+
\sqrt{2-\sqrt3\sin\phi+\cos\phi}.
\]

On this interval,

\[
2-\sqrt3\sin\phi-\cos\phi
=4\sin^2\left(\frac\phi2-\frac\pi6\right),
\]

and

\[
2-\sqrt3\sin\phi+\cos\phi
=4\sin^2\left(\frac\pi3-\frac\phi2\right).
\]

Hence

\[
\begin{aligned}
P_4(\phi)
&=2+2\sin\left(\frac\phi2-\frac\pi6\right)
+2\sin\left(\frac\pi3-\frac\phi2\right)\\
&=\boxed{
2+4\sin\frac\pi{12}
\cos\left(\frac\phi2-\frac\pi4\right)}.
\end{aligned}
\tag{ANS.3}

For

\[
\phi\in[\pi/3,\pi/2],
\]

this is strictly increasing and

\[
P_4'(\phi)
=2\sin\frac\pi{12}
\sin\left(\frac\pi4-\frac\phi2\right).
\tag{ANS.4}

Moreover, if

\[
A_0(\phi):=\frac12\sin\phi,
\]

then

\[
A_0'(\phi)=\frac12\cos\phi.
\]

Writing

\[
u:=\frac\pi4-\frac\phi2\in[0,\pi/12],
\]

we obtain the exact derivative ratio

\[
\boxed{
\frac{P_4'(\phi)}{A_0'(\phi)}
=
\frac{2\sin(\pi/12)}{\cos u}
\le2\tan\frac\pi{12}<1.
}
\tag{ANS.5}

This inequality is the useful quantitative feature of FAQ.

---

## 2. Carry the actual PI angle through NCS

Normalize the force hull to diameter one. PI chooses two actual diameter chords with projective angle `phi`. Their four-endpoint hull `Q_phi` satisfies

\[
A(Q_\phi)=A_0(\phi)=\frac12\sin\phi.
\]

FAQ gives

\[
P(Q_\phi)\le P_4(\phi).
\]

NCS.1 therefore gives, for force-hull perimeter density `p`,

\[
\boxed{
A(F)/D^2
\ge
B(p,\phi):=
A_0(\phi)
\left[
1+rac{(p-P_4(\phi))_+^2}{16\pi^2}
\right].
}
\tag{ANS.6}

C67/PI supplies asymptotically

\[
\phi\ge y-o(1)
\]

when

\[
y=h/D<\pi/2.
\]

The relevant HKS region has

\[
y\ge2\rho>\pi/3.
\]

---

## 3. The NCS-enhanced area is increasing in the diameter angle

Fix `p<=p_2`, where

\[
p_2=12\sin(\pi/12)<\pi.
\]

For `phi in[2rho,pi/2]`, put

\[
g=(p-P_4(\phi))_+,
\qquad
C=16\pi^2.
\]

If `g=0`, then

\[
\partial_\phi B=A_0'(\phi)>0.
\]

If `g>0`, differentiate:

\[
\frac{\partial B}{\partial\phi}
=
A_0'(\phi)\left(1+\frac{g^2}{C}\right)
-
A_0(\phi)\frac{2gP_4'(\phi)}{C}.
\tag{3.1}

Divide by the positive `A_0'`. By ANS.5,

\[
\frac{P_4'}{A_0'}<1.
\]

Also

\[
2A_0\le1,
\qquad
0<g<p_2-2<2.
\]

Therefore

\[
\frac1{A_0'}\frac{\partial B}{\partial\phi}
>
1-
\frac{2}{16\pi^2}
>0.
\]

Thus

\[
\boxed{
B(p,\phi)\text{ is strictly increasing in }\phi
\text{ on }[2\rho,\pi/2].
}
\tag{ANS.7}

Consequently, for fixed diameter density `y<pi/2`, the weakest valid area bound occurs at the smallest PI angle:

\[
\boxed{
A(F)/D^2
\ge
B(p,y)-o(1).
}
\tag{ANS.8}

This eliminates the extra unknown angle exactly.

---

## 4. The fixed-perimeter worst diameter density remains `y=p/2`

Combine ANS.8 with JC. Let

\[
\lambda=(e_{BB}+2s_C)/D,
\qquad
m=\min\{y,p-y\}.
\]

The necessary inequality is

\[
B(p,y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m)^2}{4\pi}.
\tag{4.1}

For

\[
y\le p/2,
\]

we have `m=y`. The derivative of `B(p,y)` is bounded above by

\[
A_0'(y)\left(1+\frac{g^2}{16\pi^2}\right),
\]

because the perimeter-bonus derivative term is negative. Since

\[
y\ge2\rho>4/3,
\]

we have

\[
\cos y<\cos(4/3)<1/4,
\]

so

\[
\partial_y B<\frac18\left(1+\frac1{16\pi^2}\right)<0.13.
\]

On the other hand

\[
\frac{\lambda+y}{2\pi}
\ge\frac{y}{2\pi}
>\frac{2}{3\pi}>0.21.
\]

Hence the left-minus-right side of (4.1) strictly decreases with `y`, so its required positive root `lambda` strictly decreases on the first half.

For

\[
y\ge p/2,
\]

`m=p-y` decreases while `B(p,y)` increases by ANS.7, so the required root strictly increases.

Therefore

\[
\boxed{
 y=p/2
}
\tag{ANS.9}

is again the unique fixed-perimeter worst density in the relevant `p>=4rho` range.

---

## 5. One-dimensional angle-sensitive PI area floor

Insert

\[
y=\phi=p/2.
\]

Define

\[
\boxed{
A_{ANS}(p)
:=
\frac12\sin\frac p2
\left[
1+rac{(p-P_4(p/2))_+^2}{16\pi^2}
\right].
}
\tag{ANS.10}

Let `L_ANS(p)` be the positive root of

\[
A_{ANS}(p)-\frac\pi4\lambda^2
=
\frac{(\lambda+p/2)^2}{4\pi}.
\tag{ANS.11}

On the narrow first-Hemmi crossover range, `L_ANS(p)` is strictly decreasing. A crude bound suffices: the derivative of the area term is below `0.07`, while the derivative contribution from the cavity term is at least

\[
\frac{p}{8\pi}>\frac1{3\pi}>0.10.
\]

The exact margin is much larger.

The sharp Hemmi/JC root `L_H(p)` from HKS remains strictly increasing.

---

## 6. New explicit crossover

The unique new crossover is therefore the solution of

\[
\boxed{
A_H(p_A)=A_{ANS}(p_A),
}
\tag{ANS.12}

where

\[
A_H(p)=3(p/p_2)^2-\frac{3+\sqrt3}{2}.
\]

Numerically,

\[
\boxed{
p_A
=3.0353123196759289569462\ldots .}
\tag{ANS.13}

At this perimeter, the common area floor and the JC cavity equality give

\[
\boxed{
\lambda_{ANS}
=0.4807218398270484821385\ldots .}
\tag{ANS.14}

This proves ANS.1.

---

## 7. Conservative decimal certificate

Choose

\[
\widehat p=3.03531231968.
\]

Direct substitution into the exact formulas gives

\[
L_{ANS}(\widehat p)
=0.4807218398264956028\ldots,
\]

\[
L_H(\widehat p)
=0.4807218398336072766\ldots .
\]

The two branch monotonicities therefore certify

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge0.4807218398264.
}
\tag{ANS.15}

This is a fully explicit theorem above HKS, not merely a nonattainment statement.

---

## 8. Equality geometry is still forbidden by C15/C43

FAQ equality at a prescribed angle forces a three-vertex equilateral triangle of side one among the PI quadrilateral vertices. In the original scale these would be three pairwise diametral source points.

C15 excludes that exact configuration for sufficiently large global minimizers, while C43 excludes a uniform neighborhood of it.

Therefore the ANS scalar floor is itself not expected to be sharp. A further positive gap should follow by combining FAQ's equality classification with a quantitative version of C43 or with another nested-convex stability step.

ANS deliberately does not use that extra exclusion in its numerical constant.

---

## 9. Audit

- FAQ applies because the post-ZF diameter-density range has PI angle above `2rho>pi/3`, while the chosen projective angle is at most `pi/2`.
- ANS.7 treats the unknown actual PI angle rather than silently replacing it by its lower bound.
- The fixed-perimeter `y=p/2` minimization is rechecked after adding the angle-sensitive bonus.
- The Hemmi branch is unchanged and remains the increasing side of the crossover.
- No new compactness theorem or external source is imported.
- The numerical improvement is small but its sign is certified by the rational decimal split in Section 7.

## 10. Classification

**Status:** proved explicit quantitative refinement of HKS/NCS.  
**Level I:** still open.  
**Strongest explicit scalar floor in this branch:** `0.4807218398264` conservatively, with optimizer value ANS.14.  
**Computation:** scalar evaluation only.

## 11. Compact handoff

```text
ANS:
FAQ simplifies to
  P4(phi)=2+4 sin(pi/12) cos(phi/2-pi/4),
  phi in [pi/3,pi/2].
NCS applied to the PI four-endpoint hull gives
  area(F)/D^2 >= B(p,phi)
    =0.5 sin(phi)[1+(p-P4(phi))_+^2/(16pi^2)].

The derivative ratio
  P4'(phi)/(0.5 cos phi)
  =2 sin(pi/12)/cos(pi/4-phi/2)
  <=2 tan(pi/12)<1,
so B increases strictly with phi. The weakest PI angle is therefore the C67 lower
endpoint phi=y. Re-optimizing JC at fixed p still gives y=p/2.

Hence use
  A_ANS(p)=0.5 sin(p/2)[1+(p-P4(p/2))_+^2/(16pi^2)].
Its JC root decreases near the crossover, while the sharp Hemmi root increases.
The unique crossover is
  p_A=3.0353123196759289569...,
  lambda_ANS=0.4807218398270484821....
The split p=3.03531231968 certifies lambda>=0.4807218398264.

FAQ equality is a diametral equilateral triple, so C15/C43 imply this new threshold is
still not sharp. Next: quantify that forbidden-equality gap.
```
