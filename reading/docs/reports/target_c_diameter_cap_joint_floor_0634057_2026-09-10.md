> Generated reading edition · [exact source](../../../docs/reports/target_c_diameter_cap_joint_floor_0634057_2026-09-10.md) · source SHA-256 `11cd2239e953163ebccb3cc89c38b91843d8ed31d18efa006603f72c80810480`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7DA1B6578E1F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — diameter-capped pockets raise the post-ZF floor to 0.634058

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after DC diameter-capped moment  
**Run type:** exact asymptotic inequality synthesis / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC/DC  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The source-diameter cap on every outer-pocket chord sharply limits the cubic moment in
DD. Combining DC with MA, GU, CC, and the independent MA/JC threshold gives

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{DCJC}
=0.6340575990818539559\ldots .
}
\tag{DJ.1}
$$

This replaces the previous explicit `0.605623...` floor by a qualitatively different
capacity bound: a contact chain can exceed length `D` only by spending outer-walk
chain--chord detour.

---

## 1. Defect-aware DC cavity capacity

Take an arbitrary convergent audited post-ZF survivor subsequence and write

$$
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y:=\lim\frac hD,
\qquad
z:=\lim\frac{Q+2s_Z}{D}.
$$

DB gives

$$
y\ge2\rho,
\qquad
0\le z\le u(y):=y-2\cos(y/2).
\tag{1.1}
$$

MA/GU give

$$
\boxed{
\liminf\frac GD^2
\ge
\Phi(y)-\frac\pi4\lambda^2,
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
}
\tag{1.2}
$$

DC, PC, MA, and ZE give

$$
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{
M(2(y-z),u(y)-z)\,[u(y)-z]
},
\tag{1.3}
$$

where `M(L,nu)` is the exact excess-budget moment function from DC.

CC gives

$$
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}.
\tag{1.4}
$$

Together with `G<=H_out+A_exc+O(D)`, every survivor limit satisfies

$$
\boxed{
\Phi(y)-\frac\pi4\lambda^2
\le
B_y(z):=
\frac1{\sqrt6}
\sqrt{M(2(y-z),u-z)(u-z)}
+\frac{z^2}{4\pi}.
}
\tag{1.5}
$$

---

## 2. On the critical interval the cavity maximum is at z=0

Let

$$
I=[2\rho,8/5].
$$

DC proves

$$
0\le u(y)<\frac14
\qquad(y\in I).
\tag{2.1}
$$

Fix `y in I` and take `0<=z_1<z_2<=u`. Put

$$
L_i=2(y-z_i),
\qquad
\nu_i=u-z_i,
\qquad
M_i=M(L_i,\nu_i).
$$

The exact moment function is nondecreasing in both arguments, so

$$
M_2\le M_1.
\tag{2.2}
$$

Also `L_i>1`, hence `M_i>=1`. Therefore the drop in the outer-pocket term obeys

$$
\begin{aligned}
&\frac1{\sqrt6}\sqrt{M_1\nu_1}
-
\frac1{\sqrt6}\sqrt{M_2\nu_2}\\
&\qquad\ge
\frac1{\sqrt6}\sqrt{M_1}
(\sqrt{\nu_1}-\sqrt{\nu_2})\\
&\qquad=
\frac1{\sqrt6}\sqrt{M_1}
\frac{z_2-z_1}{\sqrt{\nu_1}+\sqrt{\nu_2}}\\
&\qquad>
\frac25(z_2-z_1),
\end{aligned}
\tag{2.3}
$$

because `1/sqrt6>2/5` and `2sqrt(u)<1`.

The exceptional-face term increases by at most

$$
\frac{z_2^2-z_1^2}{4\pi}
\le
\frac{2u}{4\pi}(z_2-z_1)
<\frac1{24}(z_2-z_1),
\tag{2.4}
$$

using `u<1/4` and `pi>3`.

Thus

$$
B_y(z_2)<B_y(z_1).
$$

Hence

$$
\boxed{
\max_{0\le z\le u(y)}B_y(z)=B_y(0)
}
\tag{2.5}
$$

throughout `I`. In particular every sequence near the new cavity threshold must have

$$
\frac{Q+2s_Z}{D}\to0.
\tag{2.6}
$$

---

## 3. Exact one-variable moment branch

Put

$$
p_0(y)=y+2\cos(y/2).
$$

DC proves on `I` that

$$
2<p_0(y)<3
\tag{3.1}
$$

and therefore

$$
\boxed{
M_y:=M(2y,u(y))
=(1+u(y))^3+1+[p_0(y)-2]^3.
}
\tag{3.2}
$$

Define

$$
\boxed{
H_D(y):=
\frac1{\sqrt6}\sqrt{M_yu(y)}
}
\tag{3.3}
$$

and

$$
\boxed{
T_D(y):=
\sqrt{\frac4\pi[\Phi(y)-H_D(y)]}
}
\tag{3.4}
$$

when the radicand is nonnegative. Equations (1.5) and (2.5) imply

$$
\boxed{\lambda\ge T_D(y).}
\tag{3.5}
$$

---

## 4. T_D is strictly decreasing on the critical interval

Both

$$
u'(y)=1+\sin(y/2)>1
$$

and

$$
p_0'(y)=1-\sin(y/2)>0
$$

on `I`. Hence `M_y` in (3.2) is strictly increasing.

For `y>2rho`,

$$
H_D'(y)
\ge
\frac1{\sqrt6}
\sqrt{M_y}\frac{u'(y)}{2\sqrt{u(y)}}.
\tag{4.1}
$$

By (2.1), `2sqrt(u)<1`. Also `M_y>2`, so `sqrt(M_y)>sqrt2>7/5`.
Therefore

$$
H_D'(y)>
\frac25\cdot\frac75
=\frac{14}{25}>rac12.
\tag{4.2}
$$

But

$$
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
$$

Thus

$$
\boxed{[T_D(y)^2]'<0}
\tag{4.3}
$$

wherever `T_D` is real. The diameter-cap threshold is strictly decreasing.

---

## 5. The independent MA/JC threshold is strictly increasing

MAJC gives the independent necessary condition

$$
\boxed{\lambda\ge R(y),}
\tag{5.1}
$$

where `R(y)` is the positive root of

$$
\boxed{
(\pi^2+1)R^2
+4\cos(y/2)R
+4\cos^2(y/2)
-\pi(y+\sin y)=0.
}
\tag{5.2}
$$

and `R` is strictly increasing for `y>=2rho`.

At `y=2rho`, `u=0`, so `H_D=0`. The MAJC root identity yields

$$
R(2\rho)<T_D(2\rho).
\tag{5.3}
$$

At `y=8/5`, the inequalities reverse. We record a rational audit to avoid making the
decimal crossover a proof input.

Put `x=4/5`. Alternating Taylor bounds give

$$
\frac{489869}{703125}
<\cos x<\frac{1307}{1875},
\tag{5.4}
$$

and

$$
\sin(8/5)>
\frac{24594328}{24609375}.
\tag{5.5}
$$

Using `3141/1000<pi<22/7`, substitution of `R=5/8` into the left side of (5.2) gives

$$
Q_R(8/5,5/8)
<-rac{316089095263}{1378125000000}<0.
$$

Since `Q_R` increases in `R`,

$$
\boxed{R(8/5)>5/8.}
\tag{5.6}
$$

For `T_D`, (5.4) gives

$$
u(8/5)>\frac{386}{1875}
>\left(\frac{453}{1000}\right)^2.
\tag{5.7}
$$

The lower cosine bound in (5.4) gives

$$
p_0(8/5)-2>
\frac{698488}{703125}.
$$

Direct rational arithmetic in (3.2) then gives

$$
M_{8/5}>
\left(\frac{483}{250}\right)^2.
\tag{5.8}
$$

Since

$$
\frac1{\sqrt6}>\frac{20}{49},
$$

(5.7)--(5.8) give

$$
H_D(8/5)>
\frac{20}{49}\cdot\frac{483}{250}\cdot\frac{453}{1000}
=
\frac{31257}{87500}.
\tag{5.9}
$$

Also `Phi(8/5)<13/20`. Hence

$$
\Phi(8/5)-H_D(8/5)
<\frac{12809}{43750}
<\frac{75}{256}.
$$

Using `pi>3`,

$$
T_D(8/5)^2
<\frac43\frac{75}{256}
=\frac{25}{64}.
$$

Therefore

$$
\boxed{T_D(8/5)<5/8<R(8/5).}
\tag{5.10}
$$

---

## 6. Unique crossover and global threshold

By (4.3), (5.3), (5.6), and (5.10), there is a unique

$$
\boxed{y_D\in(2\rho,8/5)}
\tag{6.1}
$$

for which

$$
\boxed{R(y_D)=T_D(y_D).}
\tag{6.2}
$$

Every survivor with `y in I` satisfies

$$
\lambda\ge\max\{R(y),T_D(y)\},
$$

whose minimum is the crossover value

$$
\boxed{\lambda_{DCJC}:=R(y_D)=T_D(y_D).}
\tag{6.3}
$$

For `y>=8/5`, monotonicity of `R` gives

$$
\lambda\ge R(y)>R(y_D),
$$

so (6.3) is the global post-ZF threshold. This proves DJ.1. `square`

---

## 7. Numerical evaluation and endpoint localization

Evaluation of the analytic crossover gives

$$
\boxed{
y_D
=1.5852324139288403018\ldots,}
\tag{7.1}
$$

$$
\boxed{
\lambda_{DCJC}
=0.6340575990818539559\ldots .
}
\tag{7.2}
$$

At this point

$$
u(y_D)=0.1812634582352110920\ldots,
$$

$$
p_0(y_D)=2.9892013696224695116\ldots,
$$

$$
M_{y_D}=3.6162680516422744450\ldots,
$$

and

$$
H_D(y_D)=0.3305291850316669596\ldots .
$$

Every endpoint sequence must satisfy

$$
\boxed{
\frac hD\to y_D,
\qquad
\frac{Q+2s_Z}{D}\to0.
}
\tag{7.3}
$$

The MA/JC equality also forces

$$
\boxed{
\frac{P_F}{D}\to p_0(y_D),
\qquad
\frac{e_{BB}}D\to\lambda_{DCJC},
\qquad
\frac{s_C}{D}\to0.
}
\tag{7.4}
$$

Thus the endpoint is again a pure-quadrangulation / zero-mixed-surplus regime, but now
with a substantially larger normalized outer-walk detour `u(y_D)`.

---

## 8. Regression audit

- **One giant outer pocket:** DC permits it only up to chain length `D` plus the entire
  detour budget; this is the exact source-diameter obstruction missing from DD.
- **Many unit-scale chains:** represented sharply by the integer-plus-remainder term in
  `M_y`.
- **Regular odd shell:** lies at much larger `y`; DC itself remains valid but DJ uses
  the critical small-detour branch only where it is proved.
- **Giant exceptional face:** the joint `z` optimization shows positive DB defect lowers
  total cavity capacity on the critical interval.
- **Dense isolated fillings:** still lack the global post-ZF source certificate.
- **Response trace and matching regressions:** unused.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| joint defect capacity B_y(z) | proved | DC + CC + exact post-ZF ledgers |
| maximum at z=0 | proved | finite-difference decrease of outer term dominates exceptional quadratic increase |
| exact moment branch M_y | proved | DC piecewise optimizer and `2<p_0<3` |
| T_D decreases | proved | detour growth dominates force-hull area derivative |
| unique crossover | proved | opposite endpoint signs and monotonicity |
| explicit floor `0.6340575990...` | proved asymptotically | analytic crossover |
| Level I | still open | the DC equality geometry remains to be audited |

---

## 10. Exact next obligation

The DC optimizer at the endpoint has normalized chain-length profile

$$
\boxed{
1+u(y_D),\quad 1,\quad p_0(y_D)-2,
}
\tag{10.1}
$$

up to permutation, with every other outer-pocket chain `o(D)`. Simultaneously MA/JC
forces `P_F/D->p_0(y_D)` and `z,s_C->0`.

Audit whether this three-macroscopic-pocket profile can coexist with MA's one-gap
force-hull equality geometry and with the exact chord/detour budget. In particular,
DC equality spends **all** detour on the unique chain longer than `D`; the other two
macroscopic chains must have chord lengths asymptotic to their chain lengths. This is a
finite geometric equality statement, not another scalar constant.
