> Generated reading edition · [exact source](../../../docs/reports/target_c_cap_joint_cavity_floor_0593235_2026-09-10.md) · source SHA-256 `2ad3188b72cbafe1a81f962d170ce4e17fa02a63a68353eed2ae0b21fec378ee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-FEB9D2B50C45","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — CAP/JC raises the post-ZF pinned/contact floor to 0.593235

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after commit `85033bfd6a98e6b6fa07e937bc19edfda0409994`  
**Run type:** exact asymptotic inequality synthesis / closing-proof continuation  
**Target:** Target C, C-II after ZF/FS/FSDB/FSJC/FDJ/CAP  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The cyclic force-hull area/perimeter theorem CAP restores the actual force-hull
perimeter variable which FSJC had to discard. Combining CAP, FSDB, GU, and the
actual-perimeter JC cavity inequality gives the explicit improved lower bound

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{CAPJC}
=0.5932351999620735312\ldots .
}
\tag{CJ.1}
```

The constant is defined without numerical optimization. Let `y_0` be the unique root
in `(2rho,pi/2)` of

```math
\boxed{7y_0-\sin y_0=3\pi,}
\tag{CJ.2}
```

where `rho=cos rho` is the Dottie number from DB. Then `lambda_CAPJC` is the unique
positive root of

```math
\boxed{
(\pi^2+1)\lambda^2
+2y_0\lambda
+y_0^2
-\pi(y_0+\sin y_0)
=0.
}
\tag{CJ.3}
```

Numerically,

```math
y_0=1.4887737130981834799\ldots,
\qquad
\lambda_{CAPJC}=0.5932351999620735312\ldots .
```

This improves the FSJC value

```math
0.5882283437736394387\ldots
```

by about `0.00500685618843409`.

---

## 1. Limit variables and the new feasible-region inequality

Take an arbitrary unbounded post-ZF survivor sequence. If the ratio in CJ.1 has
infinite liminf there is nothing to prove. Otherwise pass to a subsequence on which

```math
\lambda:=\lim\frac{e_{BB}+2s_C}{D}<\infty.
\tag{1.1}
```

Pass again so that

```math
y:=\lim\frac hD,
\qquad
p:=\lim\frac{\operatorname{per}F}{D}
\tag{1.2}
```

exist. DB/ZS and Cauchy's perimeter bound give

```math
2\rho\le y\le p\le\pi.
\tag{1.3}
```

Here `h<=q<=per(F)`: Hopf--Pannwitz gives `h<=q`, every loaded diameter endpoint is a
force-hull vertex, and every force-hull side has length at least one.

Put

```math
\Phi(y)=\frac{y+\sin y}{4}.
\tag{1.4}
```

FSDB and CAP together give

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A_0(y,p):=
\max\left\{
\Phi(y),
p-\frac{3\pi}{4}
\right\}.
\tag{1.5}
```

GU gives

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{1.6}
```

Thus for the attachment-cell gap `G`,

```math
\liminf\frac GD^2
\ge
A_0(y,p)-\frac\pi4\lambda^2.
\tag{1.7}
```

Let

```math
t:=\lim\frac{e_{BB}}D
```

along a further subsequence. Since `0<=t<=lambda`, the actual-perimeter JC estimate
implies

```math
\limsup\frac GD^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi},
\tag{1.8}
```

where

```math
\boxed{m(y,p):=\min\{y,p-y\}.}
\tag{1.9}
```

Combining (1.7)--(1.8) gives the necessary condition

```math
\boxed{
Q(y,p,\lambda):=
(\pi^2+1)\lambda^2
+2m(y,p)\lambda
+m(y,p)^2
-4\pi A_0(y,p)
\ge0.
}
\tag{1.10}
```

For each admissible `(y,p)`, `Q` is strictly increasing in `lambda>=0`.
Moreover `Q(y,p,0)<0` and `Q(y,p,pi)>0`: indeed
`m<=pi/2`, `A_0>=Phi(y)>1/4`, and `A_0<=pi/4`. Thus there is a unique positive
threshold root

```math
r(y,p)\in(0,\pi)
\tag{1.11}
```

and every survivor limit satisfies

```math
\lambda\ge r(y,p).
\tag{1.12}
```

The problem is now an exact two-variable minimization of `r` on (1.3).

---

## 2. The perimeter crossover

Define

```math
\boxed{
p_c(y):=\Phi(y)+\frac{3\pi}{4}
=\frac{y+\sin y+3\pi}{4}.
}
\tag{2.1}
```

This is exactly where the two area floors in (1.5) agree. For every `0<y<pi`,

```math
y<p_c(y)<\pi.
\tag{2.2}
```

Indeed

```math
p_c(y)-y=\frac{\sin y-3y+3\pi}{4}>0
```

because the numerator has derivative `cos y-3<0` and vanishes at `pi`; similarly

```math
\pi-p_c(y)=\frac{\pi-y-\sin y}{4}>0
```

because the numerator has derivative `-1-cos y<=0` and vanishes at `pi`.

The location of `p_c` relative to the cavity midpoint `2y` changes exactly once.
Let

```math
g(y)=7y-\sin y-3\pi.
\tag{2.3}
```

Then `g'(y)=7-cos y>0`, so `g` is strictly increasing. Also

```math
g(\pi/2)=\pi/2-1>0.
\tag{2.4}
```

At the DB lower endpoint `2rho`, use the already-audited bounds

```math
\frac{739}{1000}<\rho<\frac{37}{50}
```

and the elementary `pi>3141/1000`. Since

```math
\sin\rho=\sqrt{1-\rho^2}>
\sqrt{1-(37/50)^2}>\frac{33}{50},
```

we obtain

```math
\begin{aligned}
g(2\rho)
&=14\rho-2\rho\sin\rho-3\pi\\
&<
\frac{259}{25}
-
\frac{48774}{50000}
-
\frac{9423}{1000}\\
&=-\frac{481}{12500}<0.
\end{aligned}
\tag{2.5}
```

Hence there is a unique

```math
\boxed{y_0\in(2\rho,\pi/2)}
\tag{2.6}
```

with `g(y_0)=0`. Equation `g(y_0)=0` is equivalent to

```math
\boxed{p_c(y_0)=2y_0.}
\tag{2.7}
```

For `y<y_0`, `p_c(y)>2y`; for `y>y_0`, `p_c(y)<2y`.

---

## 3. Exact minimization in the perimeter variable

Fix `y` and let `r(y,p)` denote the threshold root (1.11).

### Case I: `2rho<=y<=y_0`

Here `p_c>=2y`.

For

```math
y\le p\le2y,
```

we have `A_0=Phi(y)` and `m=p-y`. At fixed `lambda`,

```math
\partial_p Q=2(\lambda+m)>0.
```

Since `Q` is increasing in `lambda`, the threshold root strictly decreases as `p`
increases.

For

```math
2y\le p\le p_c,
```

we have `A_0=Phi(y)` and `m=y`, so `Q` and its threshold root are independent of `p`.

For

```math
p_c\le p\le\pi,
```

we have `A_0=p-3pi/4` and `m=y`, so

```math
\partial_pQ=-4\pi<0.
```

The threshold root strictly increases.

Therefore the minimum over `p` is attained throughout `[2y,p_c]` and equals the
positive root `L(y)` of

```math
\boxed{
Q_L(y,\lambda):=
(\pi^2+1)\lambda^2
+2y\lambda+y^2
-\pi(y+\sin y)=0.
}
\tag{3.1}
```

### Case II: `y_0<=y<=pi`

Here `p_c<=2y`.

For `y<=p<=p_c`, again `A_0=Phi(y)`, `m=p-y`, and `partial_p Q>0`, so the threshold
root decreases toward `p_c`.

For

```math
p_c\le p\le\min\{2y,\pi\},
```

we have `A_0=p-3pi/4`, `m=p-y`. At the threshold root, (1.11) gives
`lambda<pi` and always `m<=pi/2`. Hence

```math
\partial_pQ
=2(\lambda+m)-4\pi
<3\pi-4\pi
=-\pi<0.
\tag{3.2}
```

Thus the threshold root increases immediately to the right of `p_c`.
If `2y<pi`, then for `p>=2y` we have `m=y` and still
`partial_pQ=-4pi<0`, so the root continues to increase.

Therefore for every `y>=y_0`, the unique minimizing perimeter is

```math
\boxed{p=p_c(y).}
\tag{3.3}
```

At this perimeter

```math
m_c(y):=p_c(y)-y
=\frac{\sin y-3y+3\pi}{4},
\tag{3.4}
```

and the threshold root `C(y)` is determined by

```math
\boxed{
Q_C(y,\lambda):=
(\pi^2+1)\lambda^2
+2m_c(y)\lambda+m_c(y)^2
-\pi(y+\sin y)=0.
}
\tag{3.5}
```

At `y=y_0`, equation (2.7) gives `m_c(y_0)=y_0`, so

```math
L(y_0)=C(y_0).
\tag{3.6}
```

---

## 4. Exact minimization in the diameter-density variable

### Left of `y_0`

FSJC's exact derivative audit proves that on `[2rho,pi/2]`

```math
\partial_y Q_L(y,\lambda_*)>0,
\tag{4.1}
```

where `lambda_*` is the old FSJC endpoint. For `y<pi/2`, the positive root `L(y)`
is strictly larger than `lambda_*`; `partial_y Q_L` is increasing in `lambda`.
Therefore

```math
\partial_y Q_L(y,L(y))>0
\qquad(2\rho\le y\le y_0).
\tag{4.2}
```

Since `partial_lambda Q_L>0`, implicit differentiation gives

```math
\boxed{L'(y)<0.}
\tag{4.3}
```

Thus the best threshold on the left occurs at `y=y_0`.

### Right of `y_0`

Differentiate (3.4):

```math
m_c'(y)=\frac{\cos y-3}{4}<0.
\tag{4.4}
```

At the positive root `C(y)`,

```math
\begin{aligned}
\partial_yQ_C
&=2m_c'(y)(C(y)+m_c(y))
-\pi(1+\cos y)\\
&<0.
\end{aligned}
\tag{4.5}
```

The first term is strictly negative and the second is nonpositive. Again
`partial_lambda Q_C>0`, so

```math
\boxed{C'(y)>0.}
\tag{4.6}
```

Thus the best threshold on the right also occurs at `y=y_0`.

Equations (3.6), (4.3), and (4.6) prove the exact global minimization

```math
\boxed{
\inf_{2\rho\le y\le p\le\pi}r(y,p)
=r(y_0,2y_0).
}
\tag{4.7}
```

At `(y_0,p=2y_0)`, `m=y_0` and the two area floors agree. Therefore the threshold is
exactly the positive root CJ.3. This proves CJ.1. `square`

---

## 5. Endpoint localization

All minimizations above are strict away from their stated equality sets. Therefore any
survivor sequence satisfying

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_{CAPJC}
\tag{5.1}
```

must satisfy

```math
\boxed{
\frac hD\to y_0,
\qquad
\frac{\operatorname{per}F}{D}\to2y_0.
}
\tag{5.2}
```

The relaxation `t=e_BB/D<=lambda` must also saturate. Otherwise the JC upper bound is
strictly smaller at the same `(y_0,p)` while the FSDB/CAP/GU lower bound is unchanged.
Hence

```math
\boxed{
\frac{e_{BB}}D\to\lambda_{CAPJC},
\qquad
\frac{s_C}{D}\to0.
}
\tag{5.3}
```

The endpoint is therefore even more rigid than the old FSJC endpoint: it has a fixed
nonmaximal force-hull perimeter

```math
2y_0=2.9775474261963669599\ldots<\pi,
```

and asymptotically all pinned/contact currency is direct loaded-loaded contact
currency.

---

## 6. Exact target implication

The best explicit report-level lower bound on the post-ZF pinned/contact currency is
now

```math
\boxed{0.5932351999620735312\ldots}
```

rather than the old FSJC `0.5882283437736394...`.

This is not another scalar iteration of the old detour constant. It uses a new geometric
constraint: FS.4 forces the force hull to be asymptotically cyclic and centrally
symmetric, so increasing actual perimeter has a compulsory area cost.

C-II is not closed because the theorem stack still contains no universal upper bound
on `(e_BB+2s_C)/D` below `lambda_CAPJC`.

---

## 7. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its normalized currency is asymptotic to `pi`, far above CJ.1; CAP is sharp only at its disk limit |
| dense isolated shell filling | yes | FS supplies the common radial geometry from the whole source; no isolate-count bound is used |
| half-weight matching obstruction | yes | no matching or beta-mass extraction appears |
| shell response trace defect | yes | no response-operator norm or trace upper bound is used |
| near-equilateral rhombic bulk | yes | the new charge lives on the global force-hull circle gaps, not individual contact faces |
| heptagon plus isolated center | yes | isolates stay outside the ZF core; FS sees them only through the source hull |

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| CAP area/perimeter inequality | proved in adjacent report | exact cyclic derivative identity plus FS radial transport |
| feasible-region inequality (1.10) | proved | direct combination of FSDB, CAP, GU, and actual-perimeter JC |
| unique crossover `y_0` | proved | monotonic `7y-sin y-3pi` with certified endpoint signs |
| exact `(y,p)` minimization | proved | piecewise monotonicity of the quadratic threshold |
| explicit floor `lambda_CAPJC` | proved asymptotically | global minimum of the necessary threshold |
| endpoint localization (5.2)--(5.3) | proved | strict compact minimization and saturation of `t<=lambda` |
| endpoint itself impossible | not proved in this report | CAP is strict for any fixed non-disk cyclic gap pattern, suggesting a further stability gain |
| Level I | still open | high pinned/contact surplus remains compatible with current upper bounds |

---

## 9. Reproducibility / constant audit

No computation is a proof dependency. The constants are defined by CJ.2--CJ.3.
A high-precision evaluation gives

```math
y_0=1.488773713098183479940432558528608\ldots,
```

```math
\lambda_{CAPJC}
=0.593235199962073531222166311244151\ldots .
```

The improvement over FSJC is

```math
0.005006856188434092507214676375427\ldots .
```

---

## 10. Canonical promotion recommendation

**Hold as report pending joint dependency audit.** If FS/FSDB/JC/CAP are promoted, CJ
should replace the explicit `0.588228...` floor in the post-ZF frontier and record the
new equality normal form `(y,p,t)=(y_0,2y_0,lambda_CAPJC)`.

---

## 11. Next run

The endpoint (5.2) has `p=2y_0<pi`, while equality in the elementary cyclic CAP
inequality can occur only in the disk limit `p=pi`. Therefore the CAP step used in
CJ cannot actually be asymptotically sharp at the displayed endpoint. The next exact
task is to quantify this strict cyclic-gap excess at fixed perimeter, or at minimum
prove compact nonattainment and obtain a uniform positive gap above
`lambda_CAPJC`.

A stronger route is to solve the exact circle-gap extremal problem:

```text
centrally symmetric convex hull of points on radius 1/2 circle
+ fixed normalized perimeter p
-> sharp minimum normalized area A_cyc(p).
```

Substituting `A_cyc(p)` for the linear CAP floor in (1.10) would continue increasing
the explicit post-ZF threshold without introducing any unsupported local packing or
conductance hypothesis.
