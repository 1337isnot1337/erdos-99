> Generated reading edition · [exact source](../../../docs/reports/target_c_cq_joint_cavity_floor_0593385_2026-09-10.md) · source SHA-256 `68516d151159adbf352054fa0ddba3b7a62a495ff15f8e0716ec63789636d16e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-399220ECC431","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — quadratic cyclic stability raises the post-ZF floor to 0.593386

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after quadratic cyclic stability  
**Run type:** exact asymptotic inequality synthesis / closing-proof continuation  
**Target:** Target C, C-II after ZF/FS/FSDB/JC/CQ  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

Put

$$
\kappa=\frac{288}{5\pi^5},
\qquad
\Psi(p)=p-\frac{3\pi}{4}+\kappa(\pi-p)^2.
\tag{CQJ.1}
$$

The quadratic cyclic force-hull theorem gives

$$
\frac{\operatorname{area}F}{D^2}
\ge\Psi\!\left(\frac{\operatorname{per}F}{D}\right)-o(1).
$$

Combining this with FSDB, GU, and the actual-perimeter JC inequality yields

$$
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{CQJC}
=0.5933858947681038264\ldots .
}
\tag{CQJ.2}
$$

Let `y_1` be the unique root in `(2rho,pi/2)` of

$$
\boxed{
7y_1-\sin y_1-3\pi
+4\kappa(\pi-2y_1)^2=0.
}
\tag{CQJ.3}
$$

Then

$$
y_1=1.4856143270733655372\ldots
\tag{CQJ.4}
$$

and `lambda_CQJC` is the positive root of

$$
\boxed{
(\pi^2+1)\lambda^2
+2y_1\lambda
+y_1^2
-\pi(y_1+\sin y_1)=0.
}
\tag{CQJ.5}
$$

This strictly improves the linear-CAP value `0.5932351999620735...`.

---

## 1. Feasible-region inequality

Pass to a convergent survivor subsequence and write

$$
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y=\lim\frac hD,
\qquad
p=\lim\frac{\operatorname{per}F}{D}.
\tag{1.1}
$$

As in the CAP/JC report,

$$
2\rho\le y\le p\le\pi.
\tag{1.2}
$$

FSDB and CQ give

$$
A_1(y,p):=
\max\left\{
\Phi(y),\Psi(p)
\right\},
\qquad
\Phi(y)=\frac{y+\sin y}{4},
\tag{1.3}
$$

as a lower bound for the normalized force-hull area. GU and JC therefore imply

$$
\boxed{
Q_1(y,p,\lambda):=
(\pi^2+1)\lambda^2
+2m(y,p)\lambda
+m(y,p)^2
-4\pi A_1(y,p)
\ge0,
}
\tag{1.4}
$$

where

$$
m(y,p)=\min\{y,p-y\}.
\tag{1.5}
$$

For fixed `(y,p)`, `Q_1` is strictly increasing in `lambda>=0`. Its unique positive
threshold root lies below `pi`: both area floors in (1.3) are at most `pi/4`, while
substitution `lambda=pi` leaves a positive term at least `pi^4`.

---

## 2. The new perimeter crossover

The function `Psi` is strictly increasing on the whole admissible perimeter interval.
Indeed `kappa<1/5` (for example from `pi>3141/1000`), and for `p>=2rho>1`,

$$
\Psi'(p)=1-2\kappa(\pi-p)>0.
\tag{2.1}
$$

For each `y`, let `p_c(y)` be the unique solution of

$$
\boxed{\Psi(p_c(y))=\Phi(y).}
\tag{2.2}
$$

It lies in `[y,pi]`. At `p=pi`, `Psi(pi)=pi/4>=Phi(y)`. At `p=y`, put
`x=pi-y`; then

$$
4(\Psi(y)-\Phi(y))
=-3x-\sin x+4\kappa x^2<0
\tag{2.3}
$$

for `y<pi`, since `kappa<1/5` and `x<pi-1<15/7` give `4kappa x<3`.

The equation `p_c(y)=2y` is exactly CQJ.3. Define

$$
g_1(y)=7y-\sin y-3\pi+4\kappa(\pi-2y)^2.
$$

On `[2rho,pi/2]`,

$$
g_1'(y)=7-\cos y-16\kappa(\pi-2y)>0.
\tag{2.4}
$$

A coarse bound suffices: `7-cos y>=6`, `kappa<1/5`, and
`pi-2y<=pi-4rho<1`.

At `y=pi/2`,

$$
g_1(\pi/2)=\pi/2-1>0.
\tag{2.5}
$$

At `y=2rho`, the constant audit from the CAP/JC report gives

$$
14\rho-\sin(2\rho)-3\pi< -\frac{481}{12500}.
$$

Also, using `rho>739/1000`, `pi<22/7`, and `kappa<1/5`,

$$
4\kappa(\pi-4\rho)^2
<\frac45\left(\frac{327}{1750}\right)^2.
$$

Consequently

$$
g_1(2\rho)
<
-\frac{481}{12500}
+
\frac45\left(\frac{327}{1750}\right)^2
=
-\frac{161509}{15312500}<0.
\tag{2.6}
$$

Thus CQJ.3 has a unique root `y_1 in (2rho,pi/2)`. Moreover

$$
p_c(y)>2y\quad(y<y_1),
\qquad
p_c(y)<2y\quad(y>y_1).
\tag{2.7}
$$

---

## 3. Minimize in perimeter

Let `r_1(y,p)` be the positive threshold root of (1.4).

### If `2rho<=y<=y_1`

Then `p_c>=2y`.

- On `y<=p<=2y`, `A_1=Phi(y)` and `m=p-y`, so
  `partial_p Q_1=2(lambda+m)>0`; the root decreases with `p`.
- On `2y<=p<=p_c`, `A_1=Phi(y)` and `m=y`; the root is constant.
- On `p>=p_c`, `A_1=Psi(p)`, `m=y`, and
  `partial_pQ_1=-4pi Psi'(p)<0`; the root increases.

Hence the minimum over `p` is again the root `L(y)` of

$$
(\pi^2+1)\lambda^2+2y\lambda+y^2-\pi(y+\sin y)=0.
\tag{3.1}
$$

### If `y_1<=y<=pi`

Then `p_c<=2y`. On `p<=p_c` the threshold decreases for the same reason as above.
For `p>=p_c`, first note that `p_c(y)` is increasing because both `Phi` and `Psi` are
increasing. Hence

$$
p\ge p_c(y)\ge p_c(y_1)=2y_1>4\rho.
\tag{3.2}
$$

Using `rho>739/1000`, `pi<22/7`, and `kappa<1/5`,

$$
\Psi'(p)
=1-2\kappa(\pi-p)
>
1-\frac25\frac{327}{1750}
>
\frac34.
\tag{3.3}
$$

If `p<=2y`, then `m=p-y` and at the threshold root `lambda<pi`, `m<=pi/2`. Therefore

$$
\partial_pQ_1
=2(\lambda+m)-4\pi\Psi'(p)
<3\pi-3\pi=0.
\tag{3.4}
$$

If `p>=2y`, then `m=y` and

$$
\partial_pQ_1=-4\pi\Psi'(p)<0.
\tag{3.5}
$$

Thus for every `y>=y_1`, the unique minimizing perimeter is

$$
\boxed{p=p_c(y).}
\tag{3.6}
$$

---

## 4. Minimize in diameter density

On the left, the minimizing root is the same `L(y)` as in the CAP/JC analysis. The
FSJC derivative audit implies

$$
\boxed{L'(y)<0\qquad(2\rho\le y\le y_1).}
\tag{4.1}
$$

On the right, set

$$
m_c(y)=p_c(y)-y.
$$

Implicit differentiation of (2.2) gives

$$
p_c'(y)=\frac{\Phi'(y)}{\Psi'(p_c(y))}.
\tag{4.2}
$$

For `y>=y_1`, (3.3) gives `Psi'(p_c)>3/4`, while

$$
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
$$

Hence

$$
p_c'(y)<\frac23<1,
\qquad
m_c'(y)<0.
\tag{4.3}
$$

At `p=p_c(y)`, the two area floors agree, so the threshold equation is

$$
(\pi^2+1)\lambda^2
+2m_c(y)\lambda+m_c(y)^2
-\pi(y+\sin y)=0.
\tag{4.4}
$$

Its partial derivative in `y` at fixed `lambda` is

$$
2m_c'(y)(\lambda+m_c(y))
-\pi(1+\cos y)<0.
\tag{4.5}
$$

Since the derivative in `lambda` is positive, the threshold root is strictly
**increasing** for `y>=y_1`.

Therefore the global minimum occurs at the unique crossover

$$
\boxed{y=y_1,\qquad p=2y_1.}
\tag{4.6}
$$

At this point `m=y_1` and `Psi(2y_1)=Phi(y_1)`, so the threshold is the positive root
CQJ.5. This proves CQJ.2. `square`

---

## 5. Endpoint localization

Any sequence approaching the CQJC lower endpoint must asymptotically realize the
unique global minimizer in (4.6). Thus

$$
\boxed{
\frac hD\to y_1,
\qquad
\frac{\operatorname{per}F}{D}\to2y_1.
}
\tag{5.1}
$$

The relaxation `e_BB/D<=lambda` must also saturate, so

$$
\boxed{
\frac{e_{BB}}D\to\lambda_{CQJC},
\qquad
\frac{s_C}{D}\to0.
}
\tag{5.2}
$$

Numerically,

$$
2y_1=2.9712286541467310744\ldots<\pi.
\tag{5.3}
$$

This fixed perimeter deficit is the next source of cyclic area charge.

---

## 6. Exact target implication

The report-level explicit lower floor progresses as

$$
0.5882283437736394\ldots
<0.5932351999620735\ldots
<\boxed{0.5933858947681038\ldots}.
$$

The last step is backed by a proved quadratic cyclic stability inequality rather than a
numerical iteration.

C-II remains open because no universal upper bound on the same currency has crossed
this value.

---

## 7. Regression and dependency audit

The proof uses only:

- ZF/ZS for the post-ZF source and `h<=q`;
- FS.1/FS.4 through CQ;
- FSDB's functional area floor;
- GU's attachment-cell area upper bound;
- JC's actual-perimeter cavity upper bound;
- elementary calculus and the already audited FSJC left-branch derivative sign.

Regular odd shells and dense isolated fillings remain valid regressions: their currency
lies well above the new floor. No matching-weight, conductance, operator-response, or
small-isolate theorem is used.

---

## 8. Promotion recommendation and next step

**Hold as report pending joint dependency audit.** CQJC supersedes CAPJC as the strongest
explicit cyclic-capacity floor.

The endpoint still has normalized perimeter bounded away from `pi`. The quadratic CQ
bound was obtained from deliberately coarse sine and moment inequalities, so equality
at `(y_1,2y_1)` is not expected to be realizable. The next useful theorem is either:

1. solve the sharp fixed-perimeter cyclic area minimization; or
2. retain another certified positive remainder from the CQ proof and obtain a further
   explicit threshold increase.

Neither requires a new response hypothesis; both continue to use the full-source FS
geometry which the shell regressions lack as a global-source theorem.
