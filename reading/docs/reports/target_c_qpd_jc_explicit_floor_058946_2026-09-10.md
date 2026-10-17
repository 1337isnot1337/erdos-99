> Generated reading edition · [exact source](../../../docs/reports/target_c_qpd_jc_explicit_floor_058946_2026-09-10.md) · source SHA-256 `b01fa11e9f13e922984342978253690ab399f400e81409694b8c3793bfb63f31`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DA78A49B9CB9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — QPD/JC raises the explicit post-ZF floor to 0.589461

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FSDB, JC/FD actual-perimeter cavity bound, QPD on this branch  
**Run type:** exact compact optimization / pinned-contact floor improvement  
**Target:** Target C, C-II after ZF  
**External input:** none  
**Computation:** high-precision decimal evaluation only; the proof uses the exact implicit constants

## LEVEL I STATUS

`STILL OPEN`.

QPD turns FD's qualitative maximal-perimeter disk rigidity into an explicit area
function of the actual force-hull perimeter.  Combining that function with FSDB and
retaining the actual perimeter in JC gives a compact two-parameter optimization that
can be solved exactly.

The result is

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{QPD}
=0.5894611562694627\ldots .
}
\tag{QJ.1}
$$

This replaces the previous explicit FSJC floor

$$
\lambda_{FSJC}=0.5882283437736394\ldots
$$

by an exact implicit constant larger by approximately

$$
0.0012328124958233.
$$

The new minimizing normalized diameter-edge density and force-hull perimeter are

$$
\boxed{
y_c=1.5534703643186141\ldots,
\qquad
p_c=2y_c=3.1069407286372283\ldots .
}
\tag{QJ.2}
$$

No decimal is a proof dependency.

---

## 1. Feasible-region inequality

Pass to a convergent post-ZF subsequence and write

$$
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y=\lim\frac hD,
\qquad
p=\lim\frac{\operatorname{per}F}{D}.
\tag{1.1}
$$

DB and Cauchy's perimeter bound give

$$
\boxed{
2\rho\le y\le\pi,
\qquad
g(y):=y+2\cos(y/2)\le p\le\pi.
}
\tag{1.2}
$$

FSDB and QPD give the joint area floor

$$
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
A(y,p):=\max\{\Phi(y),\Omega(p)\},
}
\tag{1.3}
$$

where

$$
\Phi(y)=\frac{y+\sin y}{4}
\tag{1.4}
$$

and `Omega` is the QPD perimeter/area function.

Let

$$
m(y,p):=\min\{y,p-y\}.
\tag{1.5}
$$

The actual-perimeter JC inequality retained in FD gives

$$
A(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi}.
\tag{1.6}
$$

Equivalently,

$$
\boxed{
H(\lambda;A,m)
:=(\pi^2+1)\lambda^2+2m\lambda+m^2-4\pi A
\ge0.
}
\tag{1.7}
$$

For fixed `(A,m)` in the feasible region, `H` is strictly increasing in `lambda>=0`.
Let

$$
\boxed{
R(A,m):=
\frac{
\sqrt{4\pi(\pi^2+1)A-\pi^2m^2}-m
}{\pi^2+1}
}
\tag{1.8}
$$

be the positive threshold root.  Then every survivor satisfies

$$
\lambda\ge R(A(y,p),m(y,p)).
\tag{1.9}
$$

The relevant monotonicities are

$$
\boxed{
\frac{\partial R}{\partial A}>0,
\qquad
\frac{\partial R}{\partial m}<0.
}
\tag{1.10}
$$

Indeed, implicit differentiation of `H=0` gives

$$
\frac{\partial R}{\partial A}
=
\frac{2\pi}{(\pi^2+1)R+m}>0,
\tag{1.11}
$$

$$
\frac{\partial R}{\partial m}
=-
\frac{R+m}{(\pi^2+1)R+m}<0.
\tag{1.12}
$$

---

## 2. The unique FSDB/QPD crossover at fixed `y`

QPD proves

$$
\Omega(g(y))
=\frac14\left[y\sin^2(y/2)+\sin y\right],
\tag{2.1}
$$

hence

$$
\boxed{
\Phi(y)-\Omega(g(y))
=\frac y4\cos^2(y/2)>0
\qquad(0<y<\pi).
}
\tag{2.2}
$$

Also

$$
\Omega(\pi)=\frac\pi4,
\qquad
\Phi(y)<\frac\pi4
\qquad(y<\pi).
\tag{2.3}
$$

Since `Omega` is strictly increasing, for every `y in [2rho,pi)` there is a unique

$$
\boxed{
c(y)\in(g(y),\pi)
\quad\text{such that}\quad
\Omega(c(y))=\Phi(y).
}
\tag{2.4}
$$

Set `c(pi)=pi` by continuity.

QPD also proves on the entire post-ZF perimeter range

$$
\boxed{
\Omega'(p)>\frac12.
}
\tag{2.5}
$$

Since

$$
\Phi'(y)=\frac{1+\cos y}{4}\le\frac12,
\tag{2.6}
$$

implicit differentiation of (2.4) gives

$$
\boxed{
0\le c'(y)
=\frac{\Phi'(y)}{\Omega'(c(y))}<1
\qquad(2\rho\le y<\pi).
}
\tag{2.7}
$$

Thus the crossover perimeter grows strictly more slowly than `y`.

---

## 3. Optimize `p` for fixed `y`

Fix `y`.  The feasible perimeter interval is

$$
g(y)\le p\le\pi.
$$

Before the crossover, `p<=c(y)`, one has

$$
A(y,p)=\Phi(y).
\tag{3.1}
$$

As `p` increases, `m=min(y,p-y)` increases until `p=2y` and then remains equal to
`y`.  By (1.10), the threshold `R` therefore decreases until `p=2y` and is constant
thereafter as long as QPD has not become active.

After the crossover, `p>=c(y)`, one has

$$
A(y,p)=\Omega(p).
\tag{3.2}
$$

If `p>=2y`, then `m=y` is constant while `Omega` increases, so `R` increases.

It remains to exclude a second decrease in the region

$$
c(y)<p<2y.
\tag{3.3}
$$

There `m=p-y`, and differentiating through (1.11)--(1.12) gives

$$
\frac{d}{dp}R(\Omega(p),p-y)
=
\frac{
2\pi\Omega'(p)-(R+m)
}{(\pi^2+1)R+m}.
\tag{3.4}
$$

The numerator is positive uniformly.  First, `A<=pi/4`, so evaluating (1.7) at
`lambda=1` gives

$$
H(1;A,m)
\ge1+2m+m^2>0.
$$

Hence every positive threshold root satisfies

$$
R<1.
\tag{3.5}
$$

In the region `p<2y`, one always has

$$
0\le m\le\frac\pi2.
\tag{3.6}
$$

Indeed, if `y<=pi/2` then `m=p-y<y<=pi/2`; if `y>=pi/2`, then
`p<=pi` gives `m=p-y<=pi-y<=pi/2`.

Using QPD.6.6,

$$
\Omega'(p)>\frac{7}{12},
$$

so

$$
2\pi\Omega'(p)
>\frac{7\pi}{6}
>1+\frac\pi2
>R+m.
\tag{3.7}
$$

Thus (3.4) is strictly positive.

Therefore the fixed-`y` optimum has the following exact form:

- if `c(y)>=2y`, its value is `R(Phi(y),y)` and any `p in [2y,c(y)]` realizes the
  same scalar threshold;
- if `c(y)<2y`, the unique optimum is `p=c(y)` and its value is
  `R(Phi(y),c(y)-y)`.

---

## 4. There is one transition `y_c`

At the DB lower endpoint `y=2rho`, the defining equation `rho=cos rho` gives

$$
g(2\rho)=2\rho+2\cos\rho=4\rho=2(2\rho).
\tag{4.1}
$$

By (2.2), `Omega(g(2rho))<Phi(2rho)`, hence

$$
c(2\rho)>4\rho=2(2\rho).
\tag{4.2}
$$

At `y=pi/2`,

$$
2y=\pi,
$$

while

$$
\Omega(\pi)=\frac\pi4
>
\frac{\pi/2+1}{4}
=\Phi(\pi/2),
$$

so

$$
c(\pi/2)<\pi=2(\pi/2).
\tag{4.3}
$$

Finally (2.7) implies

$$
\frac d{dy}(c(y)-2y)<-1.
\tag{4.4}
$$

Therefore there is a unique

$$
\boxed{
y_c\in(2\rho,\pi/2)
\quad\text{such that}\quad
c(y_c)=2y_c.
}
\tag{4.5}
$$

Equivalently,

$$
\boxed{
\Omega(2y_c)=\Phi(y_c).
}
\tag{4.6}
$$

This is the exact definition of the new optimizing diameter density.

---

## 5. The optimized threshold decreases to `y_c` and increases after it

### Left branch: `2rho <= y <= y_c`

Here `c(y)>=2y`, so the optimized threshold is

$$
M_-(y)=R(\Phi(y),y).
\tag{5.1}
$$

This is exactly the left-hand per-`y` threshold in FSJC.  FSJC proves that for
`lambda=lambda_FSJC`,

$$
\partial_y H(\lambda_{FSJC};\Phi(y),y)>0
\qquad(2\rho\le y\le\pi/2).
\tag{5.2}
$$

It also proves `M_-(y)>=lambda_FSJC`.  Since `partial_y H` is increasing in `lambda`,

$$
\partial_y H(M_-(y);\Phi(y),y)>0.
$$

As `partial_lambda H>0`, implicit differentiation gives

$$
\boxed{M_-'(y)<0.}
\tag{5.3}
$$

Thus the optimized threshold strictly decreases up to `y_c`.

### Right branch: `y_c <= y <= pi`

Here `c(y)<=2y`, so the optimized threshold is

$$
M_+(y)=R(\Phi(y),c(y)-y).
\tag{5.4}
$$

The area variable `Phi(y)` is increasing, while by (2.7)

$$
\frac d{dy}(c(y)-y)=c'(y)-1<0.
\tag{5.5}
$$

By the monotonicities (1.10), both changes increase `R`.  Hence

$$
\boxed{M_+(y)\text{ is strictly increasing on }[y_c,\pi].}
\tag{5.6}
$$

Therefore the global minimum of the complete `(y,p)` feasible region occurs exactly
at

$$
\boxed{y=y_c,\qquad p=2y_c.}
\tag{5.7}
$$

---

## 6. Exact new constant

Define

$$
\boxed{
\lambda_{QPD}:=R(\Phi(y_c),y_c),
}
\tag{6.1}
$$

where `y_c` is the unique solution of QJ.4.6 in `(2rho,pi/2)`.
Equivalently, `lambda_QPD` is the positive root of

$$
\boxed{
(\pi^2+1)\lambda^2
+2y_c\lambda
+y_c^2
-\pi(y_c+\sin y_c)=0.
}
\tag{6.2}
$$

Sections 1--5 prove that every post-ZF subsequential limit satisfies

$$
\lambda\ge\lambda_{QPD},
$$

which proves QJ.1.

The improvement over FSJC is strict without any numerical evaluation.  Since

$$
y_c<\pi/2
$$

and the FSJC left-branch threshold `R(Phi(y),y)` is strictly decreasing up to
`pi/2`,

$$
\boxed{
\lambda_{QPD}
>
R(\Phi(\pi/2),\pi/2)
=\lambda_{FSJC}.
}
\tag{6.3}
$$

High-precision evaluation gives only for orientation

$$
y_c=1.55347036431861416947\ldots,
$$

$$
2y_c=3.10694072863722833895\ldots,
$$

$$
\lambda_{QPD}=0.58946115626946273690\ldots .
$$

The exact characterization (4.6), (6.1) is the theorem.

---

## 7. Equality localization at the new scalar endpoint

If an unbounded survivor sequence were to satisfy

$$
\frac{e_{BB}+2s_C}{D}\to\lambda_{QPD},
$$

then the strict optimization above forces simultaneously

$$
\boxed{
\frac hD\to y_c,
\qquad
\frac{\operatorname{per}F}{D}\to2y_c,
}
\tag{7.1}
$$

and

$$
\boxed{
\Phi(y_c)=\Omega(2y_c).
}
\tag{7.2}
$$

The replacement `t=e_BB/D<=lambda` in JC must also saturate, so

$$
\boxed{
\frac{s_C}{D}\to0.
}
\tag{7.3}
$$

Moreover `p=2y` is exactly the balance point of the two actual-perimeter JC branches:

$$
\min\{y,p-y\}=y=p-y.
\tag{7.4}
$$

Thus the new endpoint has a substantially sharper normal form than FSJC's old
`y=pi/2` endpoint: its diameter density, actual force-hull perimeter, active pair of
area currencies, and JC branch balance are all fixed.

This localization is the next structural target.  A proof that simultaneous equality
in FSDB and QPD is impossible, or that JC branch balance forces a positive defect in
one of them, would again raise the floor without another blind scalar iteration.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| compact feasible system (1.2)--(1.6) | proved from existing reports + QPD | DB, FSDB, FD/JC, QPD |
| unique crossover `c(y)` | proved | endpoint ordering + strict monotonicity of `Omega` |
| `c'(y)<1` | proved | `Phi'<=1/2<Omega'` |
| fixed-`y` perimeter optimizer | proved | monotonicity of `R` plus derivative (3.4) |
| unique transition `y_c` | proved | signs at `2rho`, `pi/2` and `c'-2<0` |
| global minimum at `(y_c,2y_c)` | proved | left branch decreases, right branch increases |
| `lambda_QPD>lambda_FSJC` | proved exactly | `y_c<pi/2` and strict FSJC left monotonicity |
| decimal `0.5894611562...` | numerical orientation | not a proof dependency |
| Level I | still open | no universal structural upper contradiction yet |

---

## 9. Regression and no-go checks

- **Regular odd shell:** it has `p->pi` and force-hull area `->pi/4`, well above the
  minimizing `(y_c,p_c)` state.  QJ does not exclude it by itself.
- **Perfect matching:** already excluded upstream by NB and independently by MFS; QJ
  does not rely on that exclusion to optimize the surviving post-ZF inequalities.
- **Low DB endpoint:** at `y=2rho`, QPD is below FSDB on the DB perimeter boundary and
  the threshold is strictly above its value at `y_c`.
- **Old FSJC endpoint:** `y=pi/2,p=pi` is now far inside the QPD-active area regime and
  cannot minimize the new system.
- **Nonsharp QPD equality:** QPD may itself have further positive slack.  QJ only uses
  its proved lower bound, so such slack can strengthen but cannot invalidate QJ.1.

---

## 10. Next run

Attack the equality localization (7.1)--(7.4), not another unconstrained decimal
bootstrap.  At the QJ endpoint both FSDB and QPD area lower bounds must saturate while
JC's two actual-perimeter branches balance.  Trace the equality conditions in QPD's
strip/inball/diameter construction and FSDB's diameter-gap concentration.  Any
incompatibility gives a second endpoint exclusion; a quantitative incompatibility
would turn it directly into a larger explicit floor.
