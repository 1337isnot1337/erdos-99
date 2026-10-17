> Generated reading edition · [exact source](../../../docs/reports/target_c_symmetric_area_perimeter_joint_cavity_2026-09-10.md) · source SHA-256 `99b6a9f5b35fe433cd6e71ffcff0f5dd3f023b92d7998b37c51d6edc23dcd194`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EEEDA03CB2EA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — symmetric area/perimeter coupling strengthens the post-ZF cavity obstruction

**Date:** 2026-09-10  
**Repository base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Run type:** literature import / exact asymptotic synthesis / endpoint exclusion  
**Target:** Target C, C-II after ZF  
**Depends on:** FS.4, FSDB, FSJC, FD.1–FD.2, GU, JC  
**External input:** Rogalski–Saint Raymond (1985), Theorem 1  
**Computation:** decimal localization only; no numerical value is a proof dependency

## LEVEL I STATUS

`STILL OPEN`.

This report adds a second functional lower bound for the actual force-hull area.  The
central symmetral from FS/FD has the same diameter and perimeter as the force hull, and
Rogalski–Saint Raymond prove the sharp inequality

```math
\boxed{
\operatorname{area}S
\ge c_R\left(\frac{\operatorname{per}S}{2}-D\right)^2,
\qquad
c_R:=\frac{\pi}{(\pi-2)^2},
}
\tag{RS.1}
```

for every centrally symmetric compact convex planar set of diameter `D`, with equality
only for the disk.  Their paper is:

> M. Rogalski and J. Saint Raymond, *Inequalities about Symmetric Compact Convex Sets
> in the Plane*, Amer. Math. Monthly 92 (1985), 466–480, Theorem 1,
> https://www.jstor.org/stable/2322501 .

An author-hosted scan is available at
`https://webusers.imj-prg.fr/~jean.saint-raymond/preprints/IneqR2.pdf`.

Transporting RS.1 through FS.4 and combining it with FSDB and the unrelaxed JC cavity
bound gives a new explicit post-ZF floor

```math
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge \lambda_R
=0.5921405436062881570\ldots .
}
\tag{RSJ.1}
```

The optimizer is unique.  It is defined exactly by a number
`y_R in (3/2,pi/2)` satisfying

```math
\boxed{
\frac{y_R+\sin y_R}{4}
=
\frac{\pi}{(\pi-2)^2}(y_R-1)^2,
}
\tag{RSJ.2}
```

and

```math
\boxed{p_R=2y_R.}
\tag{RSJ.3}
```

Numerically,

```math
y_R=1.5100171437629435859\ldots,
\qquad
p_R=3.0200342875258871717\ldots .
\tag{RSJ.4}
```

The value `lambda_R` is the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2
+2y_R\lambda
+y_R^2
-\pi(y_R+\sin y_R)=0.
}
\tag{RSJ.5}
```

More importantly, this endpoint cannot occur.  Equality would force the normalized
central symmetral to attain RS.1 at perimeter `p_R<pi`, but the equality case of RS.1
is the diameter-one disk, whose perimeter is `pi`.  Therefore there is a nonexplicit
absolute gap:

```math
\boxed{
\exists\epsilon_R>0\ \exists D_0\ \forall D\ge D_0,
\qquad
\frac{e_{BB}+2s_C}{D}
\ge\lambda_R+\epsilon_R
}
\tag{RSJ.6}
```

for every post-ZF survivor.

This strictly improves the FSJC/FD frontier `lambda_FSJC+epsilon_FS`, whose explicit
base point is `0.5882283437...`.  It still does not supply an upper bound on the same
currency, so Level I remains open.

---

## 1. Central-symmetral transfer of the Rogalski–Saint Raymond inequality

Translate the force hull by the full-source circumcenter `o` and put

```math
F_0=F-o,
\qquad
S=\frac12(F_0-F_0).
\tag{1.1}
```

FD.1 proves exactly

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=\operatorname{per}F.
\tag{1.2}
```

FD.2 proves, with the FS quantity `L_D=O(D^{3/4})`,

```math
0\le \operatorname{area}S-\operatorname{area}F
\le L_D\operatorname{per}F+\pi L_D^2
=o(D^2).
\tag{1.3}
```

Apply RS.1 to `S`.  Since `per(S)=per(F)`, the finite consequence is

```math
\boxed{
\operatorname{area}F
\ge
c_R\left(\frac{\operatorname{per}F}{2}-D\right)^2
-L_D\operatorname{per}F-\pi L_D^2.
}
\tag{1.4}
```

Thus along a subsequence with

```math
p:=\lim\frac{\operatorname{per}F}{D},
\tag{1.5}
```

we have

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Psi(p):=c_R\left(\frac p2-1\right)^2.
}
\tag{1.6}
```

The ordinary perimeter bounds give

```math
2\le p\le\pi.
\tag{1.7}
```

FSDB independently gives, for

```math
y:=\lim\frac hD,
\qquad 2\rho\le y\le p,
\tag{1.8}
```

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
}
\tag{1.9}
```

Hence the force hull simultaneously satisfies

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_*(y,p):=\max\{\Phi(y),\Psi(p)\}.
}
\tag{1.10}
```

This is the new geometric input.

---

## 2. Joint cavity feasibility region

Pass to a convergent survivor subsequence and write

```math
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D,
\tag{2.1}
```

so `0<=t<=lambda`.  GU gives

```math
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{2.2}
```

The actual-perimeter form of JC gives for the uncovered force-hull gap `G`

```math
\limsup\frac G{D^2}
\le
\frac{(t+m(y,p))^2}{4\pi},
\qquad
m(y,p):=\min\{y,p-y\}.
\tag{2.3}
```

Combining (1.10), (2.2), (2.3), and `t<=lambda`, every survivor limit must satisfy

```math
\boxed{
A_*(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi}.
}
\tag{2.4}
```

Equivalently,

```math
\boxed{
Q(\lambda;A_*,m)
:=(\pi^2+1)\lambda^2
+2m\lambda+m^2-4\pi A_*
\ge0.
}
\tag{2.5}
```

For `A>0`, let `R(A,m)` be the nonnegative threshold root of `Q=0`.  On the relevant
range,

```math
\frac{\partial R}{\partial A}
=\frac{2\pi}{(\pi^2+1)R+m}>0,
\tag{2.6}
```

and

```math
\frac{\partial R}{\partial m}
=-\frac{R+m}{(\pi^2+1)R+m}<0.
\tag{2.7}
```

Thus larger required area raises the pinned/contact threshold, while larger available
cavity perimeter lowers it.

The geometric domain is

```math
\boxed{
2\rho\le y\le p\le\pi,
\qquad p\ge2.
}
\tag{2.8}
```

---

## 3. The unique crossover `y_R`

Put

```math
g(y):=\Phi(y)-\Psi(2y)
=\frac{y+\sin y}{4}-c_R(y-1)^2.
\tag{3.1}
```

On the DB interval starting at `2rho`, `g` is strictly decreasing.  Indeed

```math
g'(y)=\frac{1+\cos y}{4}-2c_R(y-1).
\tag{3.2}
```

Here `rho>7/10`, hence `y-1>2/5`, while `c_R>2`; therefore the negative term in
(3.2) is already greater than `8/5`, whereas the positive term is at most `1/2`.

Also `2rho<3/2`.  At `y=3/2`, the elementary alternating Taylor estimate gives
`sin(3/2)>99/100`, while `3.14<pi` and monotonicity of
`x/(x-2)^2` for `x>2` give `c_R<121/50`.  Hence

```math
\Phi(3/2)>\frac{249}{400}>\frac{121}{200}>\Psi(3),
\tag{3.3}
```

so `g(3/2)>0`.  At the other endpoint,

```math
\begin{aligned}
g(\pi/2)
&=\frac{\pi/2+1}{4}
-c_R\left(\frac\pi2-1\right)^2\\
&=\frac{\pi+2}{8}-\frac\pi4\\
&=\frac{2-\pi}{8}<0.
\end{aligned}
\tag{3.4}
```

Therefore there is a unique

```math
\boxed{y_R\in(3/2,\pi/2)}
\tag{3.5}
```

satisfying RSJ.2.

---

## 4. Exact minimization of the two-variable feasibility problem

We now minimize

```math
R(A_*(y,p),m(y,p))
\tag{4.1}
```

over (2.8).

### 4.1 The range `2rho <= y <= y_R`

For any `p`,

```math
m(y,p)\le y,
\qquad
A_*(y,p)\ge\Phi(y).
```

Therefore

```math
R(A_*(y,p),m(y,p))
\ge R(\Phi(y),y).
\tag{4.2}
```

Because `g(y)>=0`, taking `p=2y` makes `m=y` and
`Psi(2y)<=Phi(y)`, so (4.2) is the exact minimum over `p` for fixed `y`.

Let

```math
r_-(y):=R(\Phi(y),y).
\tag{4.3}
```

The earlier FSJC theorem gives `r_-(y)>=lambda_FSJC>1/2`.  At a root of the
corresponding quadratic,

```math
\partial_y Q
=2r_-(y)+2y-\pi(1+\cos y)>0
\tag{4.4}
```

throughout `[2rho,pi/2]`; this is exactly the monotonicity estimate already audited in
FSJC, and it becomes only stronger when `lambda` is above the FSJC minimum.  Since
`partial_lambda Q>0`, implicit differentiation gives

```math
\boxed{r_-'(y)<0.}
\tag{4.5}
```

Thus the best point in this range is the right endpoint `y=y_R`.

### 4.2 The range `y >= y_R`

For each such `y`, define the unique perimeter at which the two area floors agree:

```math
\boxed{
p_e(y):=2+2\sqrt{\frac{\Phi(y)}{c_R}}.
}
\tag{4.6}
```

It is feasible.  First, `p_e(y)<=2y` follows from `g(y)<=0`.  Also
`p_e(y)<=pi` because `Psi(pi)=pi/4>=Phi(y)`.  Finally `p_e(y)>=y`:
for `y<=2` this is immediate from `p_e>=2`; for `2<=y<=pi`, the function

```math
H(y):=\Phi(y)-\Psi(y)
```

has `H(2)>0`, `H(pi)=0`, and

```math
H''(y)=-\frac{\sin y}{4}-\frac{c_R}{2}<0.
```

Concavity therefore gives `H(y)>=0`, which is equivalent to `p_e(y)>=y`.

If `p<=p_e(y)`, then `A_*>=Phi(y)` and

```math
m(y,p)\le p-y\le p_e(y)-y.
```

Hence the threshold is minimized at `p=p_e(y)` on this side.

If `p>=p_e(y)` while `p<=2y`, then `A_*=Psi(p)` and `m=p-y`.  Along this branch the
threshold root `lambda(p)` satisfies

```math
(\pi^2+1)\lambda^2
+2(p-y)\lambda+(p-y)^2
-\pi c_R(p-2)^2=0.
\tag{4.7}
```

Implicit differentiation shows that `lambda'(p)>0` exactly when

```math
\pi c_R(p-2)>\lambda+p-y.
\tag{4.8}
```

Here `p>=p_e(y)>=p_e(y_R)=2y_R>3` and `c_R>2`.  Also the threshold root is less
than one: since `Psi(p)<=Psi(pi)=pi/4`, substituting `lambda=1` into (4.7) gives a
strictly positive left side.  Therefore

```math
\pi c_R(p-2)>2\pi>1+\pi>\lambda+p-y,
```

which proves (4.8).  If `p>=2y`, then `m=y` is fixed while `Psi(p)` increases, so the
threshold again increases.  Thus for every `y>=y_R`, the unique best perimeter is

```math
\boxed{p=p_e(y).}
\tag{4.9}
```

At this perimeter put

```math
m_e(y)=p_e(y)-y
=2+2\sqrt{\frac{\Phi(y)}{c_R}}-y.
\tag{4.10}
```

Now `Phi` is increasing and

```math
m_e'(y)
=\frac{\Phi'(y)}{\sqrt{c_R\Phi(y)}}-1<0.
\tag{4.11}
```

Indeed `Phi'(y)<=1/2`, while on this range `c_R>2` and `Phi(y)>1/2`.  By
(2.6)–(2.7),

```math
\boxed{
r_+(y):=R(\Phi(y),m_e(y))
\text{ is strictly increasing for }y\ge y_R.
}
\tag{4.12}
```

Combining (4.5) and (4.12), the global minimum is unique and occurs at

```math
\boxed{(y,p)=(y_R,2y_R).}
\tag{4.13}
```

At this point `m=y_R` and `Phi(y_R)=Psi(2y_R)`, so the threshold equation is exactly
RSJ.5.  This proves RSJ.1.

---

## 5. The new endpoint is impossible

Assume for contradiction that an unbounded survivor sequence satisfies

```math
\lambda_D:=\frac{e_{BB}+2s_C}{D}\to\lambda_R.
\tag{5.1}
```

Put

```math
y_D:=\frac hD,
\qquad
p_D:=\frac{\operatorname{per}F}{D},
\qquad
m_D:=\min\{y_D,p_D-y_D\}.
\tag{5.2}
```

Compactness of the normalized parameter domain and the strict minimization in Section
4 force

```math
y_D\to y_R,
\qquad
p_D\to p_R=2y_R,
\qquad
m_D\to y_R.
\tag{5.3}
```

Write

```math
A_D=\frac{\operatorname{area}F}{D^2}.
```

From (1.10),

```math
\liminf A_D\ge A_R:=\Phi(y_R)=\Psi(p_R).
\tag{5.4}
```

On the other hand, the unrelaxed JC/GU upper chain gives

```math
A_D
\le
\frac\pi4\lambda_D^2
+
\frac{(\lambda_D+m_D)^2}{4\pi}
+o(1).
\tag{5.5}
```

By the defining equality RSJ.5, the right side tends exactly to `A_R`.  Therefore

```math
\boxed{A_D\to A_R.}
\tag{5.6}
```

FD.2 gives

```math
\frac{\operatorname{area}S-\operatorname{area}F}{D^2}\to0,
```

so

```math
\frac{\operatorname{area}S}{D^2}\to A_R.
\tag{5.7}
```

Normalize `S` by `D`.  These bodies are centrally symmetric, have diameter exactly
one, lie in the radius-`1/2` disk, and have perimeter tending to `p_R`.  By Blaschke
selection, pass to a Hausdorff limit `S_infty`.  Area and perimeter are continuous for
planar convex bodies, hence

```math
\operatorname{diam}S_\infty=1,
\qquad
\operatorname{per}S_\infty=p_R,
\qquad
\operatorname{area}S_\infty=A_R.
\tag{5.8}
```

But `A_R=Psi(p_R)`, so `S_infty` attains equality in RS.1.  Rogalski–Saint Raymond's
equality characterization forces `S_infty` to be the diameter-one disk.  Its perimeter
is `pi`, while

```math
p_R=2y_R<\pi
\tag{5.9}
```

because `y_R<pi/2`.  Contradiction.

Thus no endpoint sequence exists.

Exactly as in FDJ, a diagonal-sequence argument now proves RSJ.6: if no uniform
`epsilon_R` existed, one could choose survivors with `D_j>=j` and
`lambda_j<lambda_R+1/j`; RSJ.1 would force `lambda_j->lambda_R`, contradicting the
endpoint exclusion.

---

## 6. Numerical localization

The theorem is defined by RSJ.2 and RSJ.5.  High-precision evaluation gives

```math
\boxed{
\begin{aligned}
y_R&=1.5100171437629435858529801140\ldots,\\
p_R&=3.0200342875258871717059602281\ldots,\\
A_R&=0.6270426644374162987256839961\ldots,\\
\lambda_R&=0.5921405436062881570395130229\ldots .
\end{aligned}
}
\tag{6.1}
```

No sign in the proof depends on these decimals.

---

## 7. Regression and scope audit

- **Regular odd shells:** retained.  Their force hull approaches the disk; their
  pinned/contact currency is far above the new floor.
- **Perfect matching:** already excluded quantitatively by NB; the later FSDB/Mantel
  proof is an independent geometric exclusion.  RSJ does not use either matching
  argument.
- **Contact-isolated source points:** retained.  The central symmetral transfer uses
  FS.4, whose center/radius input comes from the full source hull.
- **Response radialization:** unused.  No coordinate-field estimate is promoted to an
  operator estimate.
- **Rogalski–Saint Raymond equality:** used only for centrally symmetric `S`, exactly
  within the theorem's hypotheses.
- **Numerical optimizer:** not a proof dependency.  Section 4 proves the unique global
  minimizer analytically.

---

## 8. Exact remaining obstruction

The report-level lower frontier is now

```math
\frac{e_{BB}+2s_C}{D}
\ge0.5921405436\ldots+\epsilon_R
```

for some absolute nonexplicit `epsilon_R>0` in the sufficiently-large post-ZF class.
There is still no universal upper bound on this currency below that value.

The most useful next targets are therefore structural rather than another scalar
iteration:

1. exploit the `s_Z=0` rigidity-circuit phase, where the full mixed graph has a unique
   dependence and every proper mixed edge set is independent;
2. derive a geometric upper tradeoff between direct loaded-loaded contacts `e_BB` and
   pinned-contact surplus `s_C` using the near-common-circle force-hull geometry;
3. retain the full three-variable state `(y,p,lambda)` when combining pocket/detour or
   circuit-separator inequalities.  Collapsing immediately to `lambda` discards the
   new perimeter information.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let S=(F-o-(F-o))/2.  FD gives
    diam S=D,
    per S=per F,
    area S-area F=o(D^2).
Rogalski-Saint Raymond (1985), Theorem 1, gives for centrally symmetric S
    area S >= [pi/(pi-2)^2] (per S/2-D)^2,
with equality only for the disk.
Hence, with y=h/D and p=per(F)/D,
    area(F)/D^2 >= max{
        Phi(y)=(y+sin y)/4,
        Psi(p)=[pi/(pi-2)^2](p/2-1)^2
    }-o(1).
JC+GU require
    max{Phi(y),Psi(p)}-pi lambda^2/4
      <= (lambda+min(y,p-y))^2/(4pi),
    lambda=(e_BB+2s_C)/D.

The exact two-variable minimum occurs uniquely at
    p=2y,
    Phi(y)=Psi(2y),
with y=y_R in (3/2,pi/2).
Numerically
    y_R=1.51001714376294...,
    p_R=3.02003428752589...,
    lambda_R=0.592140543606288....

The endpoint is impossible: approaching lambda_R forces the normalized central
symmetral to attain the Rogalski-Saint Raymond equality at perimeter p_R<pi, while
equality requires the diameter-one disk, whose perimeter is pi.
Therefore for some epsilon_R>0 and all sufficiently large post-ZF survivors,
    (e_BB+2s_C)/D >= lambda_R+epsilon_R.

Next: use the retained (y,p,lambda) state inside the s_Z=0 rigidity-circuit phase;
do not collapse back to a scalar surplus iteration.
```
