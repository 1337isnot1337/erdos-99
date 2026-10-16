<!-- theorem-state: {"artifact_id":"ART-5AE341092088","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_clipped_disk_quantitative_stability_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=9817951950be7c5cb1fc4f22f12671ced6e66f0f; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — quantitative clipped-disk stability for the FS symmetral

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** FD, QPA, SA, ST on this branch  
**Run type:** elementary quantitative convex stability  
**Target:** Target C, C-II after ZF  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`.

ST excludes the SA/JC endpoint by a compactness argument: QPA perimeter saturation
forces a clipped-disk limit, while SA area saturation assigns that limit too little
area.  This report makes the first step quantitative with an elementary support
function estimate.

For `2<p<pi`, let `alpha(p)` be the QPA inverse defined by

\[
f(a)=2\left(\arcsin a+\sqrt{1-a^2}\right),
\qquad
\alpha=f^{-1}.
\tag{QS.1}
\]

For `a in [alpha(p),1]`, put

\[
\delta(a,p):=f(a)-p\ge0,
\tag{QS.2}
\]

\[
\tau(a):=
\frac12\left(\arcsin a+a\sqrt{1-a^2}\right),
\tag{QS.3}
\]

and

\[
B(a,p):=
\tau(a)
-p\sqrt{\frac{\delta(a,p)}2}
-\frac\pi2\delta(a,p).
\tag{QS.4}
\]

Define the explicit one-dimensional stability envelope

\[
\boxed{
\mathcal Z(p):=
\min_{a\in[\alpha(p),1]}
\max\left\{
\frac{ap}{4},
B(a,p)
\right\}.
}
\tag{QS.5}
\]

Then every unbounded post-ZF sequence with

\[
\frac{\operatorname{per}F}{D}\to p
\]

satisfies

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge\mathcal Z(p).
}
\tag{QS.6}
\]

Moreover

\[
\boxed{
\mathcal Z(p)>\Xi(p)
=\frac{p\alpha(p)}4
\qquad(2<p<\pi).
}
\tag{QS.7}

Thus the nonexplicit ST endpoint gap has a concrete finite-dimensional source: an
explicit area function strictly stronger than SA at every interior perimeter.

---

## 1. Support-deficit stability inside the QPA clipped disk

Normalize diameter to one.  Let `K` be a centrally symmetric convex body centered at
`0`, with

\[
\operatorname{diam}K=1,
\qquad
\operatorname{per}K=p.
\tag{1.1}
\]

Let its centered inradius be `r=a/2`.  QPA gives

\[
a\ge\alpha(p).
\tag{1.2}
\]

Choose a minimum-support direction `u`.  Then

\[
K\subseteq
T_a:=
\overline B(0,1/2)
\cap
\{x:|x\cdot u|\le a/2\}.
\tag{1.3}
\]

QPA computes

\[
\operatorname{per}T_a=f(a),
\qquad
\operatorname{area}T_a=\tau(a).
\tag{1.4}
\]

Put

\[
\delta=f(a)-p.
\tag{1.5}
\]

Because both bodies are centrally symmetric, write their support functions on the
projective angle circle `[0,pi]` as `h_T(theta)` and `h_K(theta)`.  Set

\[
d(\theta):=h_T(\theta)-h_K(\theta)\ge0.
\tag{1.6}
\]

Cauchy's perimeter formula gives

\[
\boxed{
\delta
=2\int_0^\pi d(\theta)\,d\theta.
}
\tag{1.7}
\]

Every body in (1.3) lies in the radius-`1/2` disk.  A support function of a body in
that disk is `1/2`-Lipschitz in angular distance: for unit directions `u_theta,u_phi`,

\[
|h(\theta)-h(\phi)|
\le\frac12|u_\theta-u_\phi|
\le\frac12|\theta-\phi|.
\tag{1.8}
\]

Hence their difference `d` is `1`-Lipschitz.

Let

\[
M:=\max_\theta d(\theta).
\tag{1.9}
\]

Since `0<=M<=1/2`, a unit-slope triangular lower profile fits on both sides of a
maximum on the projective circle.  Therefore

\[
\int_0^\pi d(\theta)\,d\theta
\ge M^2.
\tag{1.10}
\]

Combining (1.7) and (1.10),

\[
\boxed{
M\le\sqrt{\delta/2}.
}
\tag{1.11}
\]

For convex bodies, Hausdorff distance equals the sup norm of support-function
difference.  Thus `K subset T_a` and (1.11) imply

\[
T_a\subseteq K+MB_2.
\tag{1.12}
\]

Steiner's formula gives

\[
\operatorname{area}T_a
\le
\operatorname{area}K+M\operatorname{per}K+\pi M^2.
\tag{1.13}
\]

Using (1.4), (1.11), and `per(K)=p`,

\[
\boxed{
\operatorname{area}K
\ge
\tau(a)
-p\sqrt{\delta/2}
-\frac\pi2\delta
=B(a,p).
}
\tag{1.14}
\]

This is the quantitative form of the QPA equality rigidity used qualitatively in ST.

---

## 2. Combine with support triangulation

SA gives, for the same actual inradius ratio `a`,

\[
\boxed{
\operatorname{area}K\ge\frac{ap}{4}.
}
\tag{2.1}
\]

Therefore every admissible `a>=alpha(p)` satisfies

\[
\operatorname{area}K
\ge
\max\left\{
\frac{ap}{4},B(a,p)
\right\}.
\tag{2.2}
\]

Minimizing over the unknown actual inradius ratio gives

\[
\boxed{
\operatorname{area}K\ge\mathcal Z(p).
}
\tag{2.3}
\]

This is a finite diameter-one theorem.  No compactness or asymptotic argument has been
used yet.

---

## 3. Structure of the one-dimensional minimization

For fixed `p`, the first branch

\[
L(a,p):=\frac{ap}{4}
\]

is strictly increasing in `a`.

The stability branch `B(a,p)` is strictly decreasing on
`[alpha(p),1)`.  Put

\[
s=\sqrt{1-a^2},
\qquad
q=\sqrt{\delta/2}.
\]

The exact derivatives are

\[
\tau'(a)=s,
\qquad
f'(a)=2\frac{1-a}{s}.
\tag{3.1}
\]

Hence

\[
\frac{\partial B}{\partial a}
=
 s-
\frac{p f'(a)}{4q}
-
\frac\pi2f'(a)
\tag{3.2}
\]

for `a>alpha(p)`.  Dropping the middle negative term,

\[
\begin{aligned}
\frac{\partial B}{\partial a}
&<s-\pi\frac{1-a}{s}\\
&=
\frac{(1-a)(1+a-\pi)}s<0,
\end{aligned}
\tag{3.3}
\]

because `1+a<=2<pi`.

At the left endpoint `a=alpha(p)`, one has `delta=0`, so

\[
B(\alpha(p),p)=\tau(\alpha(p)).
\tag{3.4}
\]

Writing `a=alpha(p)` and using `p=f(a)`,

\[
\begin{aligned}
B(a,p)-L(a,p)
&=
\frac12\left(\arcsin a+a\sqrt{1-a^2}\right)\\
&\quad-
\frac a2\left(\arcsin a+\sqrt{1-a^2}\right)\\
&=
\boxed{
\frac{1-a}{2}\arcsin a>0
}
\end{aligned}
\tag{3.5}
\]

for `0<a<1`.

At `a=1`,

\[
L(1,p)=\frac p4,
\]

while

\[
B(1,p)
=
\frac\pi4
-p\sqrt{\frac{\pi-p}{2}}
-\frac\pi2(\pi-p).
\tag{3.6}
\]

Even after dropping the negative square-root term,

\[
B(1,p)-L(1,p)
<
\frac{\pi-p}{4}-\frac\pi2(\pi-p)
=
\frac{\pi-p}{4}(1-2\pi)<0.
\tag{3.7}
\]

Thus there is a unique crossing

\[
\boxed{
a_s(p)\in(\alpha(p),1)
\quad\text{such that}\quad
L(a_s(p),p)=B(a_s(p),p).
}
\tag{3.8}
\]

Because `L` rises and `B` falls,

\[
\boxed{
\mathcal Z(p)
=\frac{p\,a_s(p)}4.
}
\tag{3.9}
\]

In particular `a_s(p)>alpha(p)`, so

\[
\boxed{
\mathcal Z(p)>\frac{p\alpha(p)}4=\Xi(p)
}
\tag{3.10}
\]

for every `2<p<pi`.  This proves QS.7 without a compactness argument.

The crossing equation is explicit:

\[
\boxed{
\frac{ap}{4}
=
\tau(a)
-p\sqrt{\frac{f(a)-p}{2}}
-\frac\pi2(f(a)-p),
\quad
\alpha(p)<a<1.
}
\tag{3.11}
\]

Thus `mathcal Z` is directly computable by a one-dimensional monotone root solve.

---

## 4. Transfer to the actual force hull

Apply the diameter-one result to the normalized FD central symmetral

\[
K_D:=D^{-1}S_D,
\qquad
S_D=\frac12((F_D-o_D)-(F_D-o_D)).
\]

FD gives

\[
\operatorname{diam}K_D=1,
\qquad
\operatorname{per}K_D=\frac{\operatorname{per}F_D}{D},
\tag{4.1}
\]

and

\[
0\le
\frac{\operatorname{area}S_D-\operatorname{area}F_D}{D^2}
=O(D^{-1/4}).
\tag{4.2}
\]

Hence

\[
\frac{\operatorname{area}F_D}{D^2}
\ge
\mathcal Z\left(\frac{\operatorname{per}F_D}{D}\right)
-O(D^{-1/4}).
\tag{4.3}
\]

Continuity of the unique root in (3.11) gives continuity of `mathcal Z` on every
compact subinterval of `(2,pi)`.  Therefore if `per(F_D)/D->p in (2,pi)`, (4.3)
gives QS.6.

The post-ZF DB lower bound places every relevant perimeter in

\[
p\ge4\rho>2,
\]

so the lower endpoint `p=2` is never approached in the application.

---

## 5. Exact target implication

The post-ZF area floor can now be strengthened from

\[
\max\{\Phi(y),\Xi(p)\}
\]

to

\[
\boxed{
\max\{\Phi(y),\mathcal Z(p)\}.
}
\tag{5.1}

Together with DB and the actual-perimeter JC inequality, every subsequential limit must
satisfy

\[
2\rho\le y\le\pi,
\qquad
g(y)\le p\le\pi,
\tag{5.2}
\]

\[
\boxed{
\max\{\Phi(y),\mathcal Z(p)\}
-\frac\pi4\lambda^2
\le
\frac{(\lambda+\min\{y,p-y\})^2}{4\pi}.
}
\tag{5.3}

Because `mathcal Z(p)>Xi(p)` throughout the interior and the SJ scalar minimizer has
`p_*=2y_*<pi`, this finite system already gives a strictly larger global threshold
than `lambda_SA`.  The next report records that variational improvement separately.

---

## 6. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| support deficit is 1-Lipschitz after diameter-one normalization | proved | both support functions are 1/2-Lipschitz |
| `M<=sqrt(delta/2)` | proved | triangular lower profile + Cauchy perimeter formula |
| stability area lower bound `B(a,p)` | proved | Hausdorff support metric + Steiner |
| unique crossing `a_s(p)` | proved | `L` strictly increases, `B` strictly decreases, endpoint signs |
| `mathcal Z(p)>Xi(p)` for `2<p<pi` | proved | crossing occurs strictly above `alpha(p)` |
| force-hull transfer | proved asymptotically | FD central-symmetral area error |
| new explicit decimal lambda floor | not claimed here | requires compact optimization/certification |
| Level I | still open | high-surplus branch remains |

---

## 7. Next run

Optimize (5.2)--(5.3).  Even without a decimal certificate, compactness and the unique
SJ minimizer prove that its variational threshold is strictly greater than
`lambda_SA`.  The higher-value target is a certified rational or interval lower bound
for that threshold, using the one-dimensional monotone root characterization
(3.11) rather than a black-box numerical optimizer.
