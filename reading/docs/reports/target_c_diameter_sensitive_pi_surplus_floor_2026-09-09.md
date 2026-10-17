> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_sensitive_pi_surplus_floor_2026-09-09.md) · source SHA-256 `ef18d996174421db2c207390dd76b8dcfdcc60a00a44ce2a8943b396bdbf34ab`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-569D5F419E9A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — diameter-sensitive PI optimization raises the surplus floor

**Date:** 2026-09-09  
**Run type:** exact asymptotic optimization / post-PI branch exclusion  
**Target:** Target C C-II after ZF/DB/PI/JC  
**Depends on:** PI exact projective-spread area theorem, JC diameter-sensitive joint cavity capacity, DB `h/D>=2rho`  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

JC and GS obtained explicit lower bounds on

$$
\lambda:=\frac{e_{BB}+2s_C}{D}
$$

by replacing PI's force-hull area with a universal constant. PI actually gives a stronger area floor as a function of the normalized number of actual diameter edges

$$
y:=\frac hD.
$$

Keeping this dependence throughout the joint cavity inequality produces the stronger explicit bound

$$
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{PI}^*
=0.465351845396014\ldots .
}
\tag{DS.1}
$$

No new external theorem is required.

---

## 1. Asymptotic PI area as a function of diameter-edge density

PI proves the finite inequality

$$
area(F)
\ge
\frac{D^2}{2}
\sin\left(
\min\left\{(h-1)\delta_D,\frac\pi2-\delta_D\right\}
\right),
$$

where

$$
\delta_D=2\arcsin\frac1{2D},
\qquad
D\delta_D\to1.
$$

Pass to a subsequence with

$$
\frac hD\to y.
$$

DB gives

$$
y\ge2\rho=1.4781702664\ldots .
$$

Since `2rho<pi/2`, PI yields the density-sensitive asymptotic floor

$$
\boxed{
\liminf\frac{area(F)}{D^2}
\ge A(y),
}
\tag{DS.2}
$$

with

$$
\boxed{
A(y)=
\begin{cases}
\frac12\sin y,&2\rho\le y\le\frac\pi2,\\[1mm]
\frac12,&\frac\pi2\le y\le\pi.
\end{cases}
}
\tag{DS.3}
$$

The second branch follows because PI's projective angle approaches `pi/2` once `(h-1)delta_D` passes that threshold.

---

## 2. Diameter-sensitive joint cavity capacity

JC proves, along the same subsequence, the necessary inequality

$$
\boxed{
A(y)-\frac\pi4\lambda^2
\le
\frac{(t+m(y))^2}{4\pi},
}
\tag{DS.4}
$$

where

$$
t:=\lim\frac{e_{BB}}D,
\qquad
0\le t\le\lambda,
$$

and

$$
\boxed{m(y):=\min\{y,\pi-y\}.}
\tag{DS.5}
$$

Replacing `t` by its largest possible value `lambda` gives the necessary one-variable condition

$$
\boxed{
A(y)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y))^2}{4\pi}.
}
\tag{DS.6}
$$

Equivalently,

$$
\boxed{
(\pi^2+1)\lambda^2
+2m(y)\lambda
+m(y)^2
-4\pi A(y)
\ge0.
}
\tag{DS.7}
$$

For each fixed `y`, the left side is strictly increasing in positive `lambda`. Hence the smallest allowed `lambda` is the positive root of equality in DS.7.

---

## 3. The root is minimized at `y=pi/2`

It is enough to prove directly that, at the candidate root for `y=pi/2`, DS.7 fails for every other allowed `y`.

Let `lambda_*` be the positive solution of

$$
\boxed{
(\pi^2+1)\lambda^2
+\pi\lambda
+\frac{\pi^2}{4}
-2\pi=0.
}
\tag{DS.8}
$$

This is exactly DS.7 at

$$
y=\frac\pi2,
\qquad A(y)=\frac12,
\qquad m(y)=\frac\pi2.
$$

### Left half: `2rho<=y<=pi/2`

Here

$$
A(y)=\frac12\sin y,
\qquad m(y)=y.
$$

Define

$$
F_-(y)
:=(\pi^2+1)\lambda_*^2
+2y\lambda_*+y^2-2\pi\sin y.
$$

By DS.8,

$$
F_-(\pi/2)=0.
$$

Differentiate:

$$
F_-'(y)
=2\lambda_*+2y-2\pi\cos y.
\tag{DS.9}
$$

On the interval `y>=2rho`,

$$
y\ge2\rho=1.47817\ldots,
\qquad
\pi\cos y\le\pi\cos(2\rho)=0.2909\ldots .
$$

Hence

$$
\lambda_*+y-\pi\cos y>0,
$$

so

$$
F_-'(y)>0.
$$

Therefore

$$
F_-(y)<0
\qquad(2\rho\le y<\pi/2).
\tag{DS.10}
$$

Thus `lambda=lambda_*` violates the necessary condition DS.7 for every density strictly below `pi/2`.

### Right half: `pi/2<=y<=pi`

Put

$$
z:=\pi-y\in[0,\pi/2].
$$

Here

$$
A(y)=\frac12,
\qquad m(y)=z.
$$

The DS.7 left side becomes

$$
F_+(z)
=(\pi^2+1)\lambda_*^2
+2z\lambda_*+z^2-2\pi.
$$

This is strictly increasing in `z>=0`, while DS.8 gives

$$
F_+(\pi/2)=0.
$$

Therefore

$$
F_+(z)<0
\qquad(0\le z<\pi/2),
\tag{DS.11}
$$

which again violates DS.7 for every `y>pi/2`.

Hence the global minimum over all admissible diameter densities is attained uniquely at

$$
\boxed{y=\pi/2.}
\tag{DS.12}
$$

---

## 4. Explicit new constant

Solving DS.8 gives

$$
\boxed{
\lambda_{PI}^*
=
\frac{-\pi+
\sqrt{\pi^2-4(\pi^2+1)(\pi^2/4-2\pi)}}
{2(\pi^2+1)}.
}
\tag{DS.13}
$$

Numerically,

$$
\boxed{
\lambda_{PI}^*
=0.465351845396014\ldots .
}
\tag{DS.14}
$$

Therefore every unbounded post-ZF survivor sequence satisfies DS.1.

This supersedes the explicit Groemer split constant

$$
0.464792250394\ldots
$$

as the best current numerical lower bound. Groemer/JN remain useful for equality/stability information near maximal force-hull perimeter, but are no longer needed merely to beat the original JC scalar constant.

---

## 5. Consequence for diameter branching

ZK and DB give the slope constraint

$$
\frac{r_H}{D}
+\frac13\frac{e_{BB}+2s_C}{D}
\ge2\rho-o(1).
$$

Insert DS.1:

$$
\boxed{
\frac{r_H}{D}
\ge
2\rho-\frac{\lambda_{PI}^*}{3}-o(1)
=1.3230529846\ldots-o(1)
}
\tag{DS.15}
$$

for sequences approaching the minimum permitted pinned/contact currency.

The universal NB lower bound remains `0.609904...`; DS.15 describes the much more highly branched part of parameter space near the new surplus floor.

---

## 6. Extremal normal form

The scalar optimization identifies the only density at which the explicit floor can be approached:

$$
\boxed{h/D\to\pi/2.}
\tag{DS.16}
$$

Moreover the relaxation `t<=lambda` must be tight at equality, so an extremizing sequence would require

$$
\boxed{
\frac{e_{BB}}D\to\lambda_{PI}^*,
\qquad
\frac{s_C}{D}\to0.
}
\tag{DS.17}
$$

Thus the numerical worst case is no longer diffuse. It is a high-diameter-density, direct-loaded-contact-dominated shell with negligible pinned stress surplus.

JN's constant-width argument may further exclude exact attainment, but DS does not need that extra step for the explicit bound.

---

## 7. Regression audit

- The proof retains PI's actual `h/D` dependence rather than importing a new convex-geometric theorem.
- For `y>pi/2`, the projective spread saturates at perpendicularity; DS does not incorrectly use `sin y`, which would decrease.
- Replacing `t` by `lambda` is the only worst-case relaxation in the final scalar inequality. Equality therefore forces `s_C/D->0`.
- Regular shell regressions have large direct loaded contacts and diameter density near the high-density regime, so they are not falsely excluded without global inputs.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| density-sensitive area DS.3 | proved | asymptotic PI theorem |
| necessary inequality DS.7 | proved | JC joint cavity capacity |
| minimum occurs at `y=pi/2` | proved | monotonicity on both sides |
| explicit floor `0.4653518454...` | proved | quadratic root |
| extremal `s_C/D->0` | necessary for equality | tightness of `t<=lambda` |
| exact threshold attained by a source | not claimed | JN already indicates compactness obstruction at earlier scalar endpoint |
| Level I | still open | high direct-contact/high-branching shell remains |

---

## 9. Next target

The strongest explicit near-threshold normal form is now:

$$
h/D\approx\pi/2,
\qquad
 e_{BB}/D\approx0.46535,
\qquad
 s_C/D\approx0,
\qquad
 r_H/D\gtrsim1.32305.
$$

This points directly to the `s_C`-small attachment-cell geometry and the loaded-loaded contact shell, rather than to a diffuse pinned-stress obstruction.
