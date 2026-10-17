> Generated reading edition · [exact source](../../../docs/reports/target_c_rs_symmetric_area_floor_059214_2026-09-10.md) · source SHA-256 `8fbdd2b231a8a58eb5d7f0606821b42678fd5140ffabb8c7f21bfc508a15d923`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BFE1CD7B65E4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — symmetric force-hull area raises the post-ZF floor

**Date:** 2026-09-10  
**Repository state:** `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4` at start  
**Run type:** closing proof / literature import / exact asymptotic synthesis  
**Target:** Target C, C-II after ZF / FS / FSDB / FSJC  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used; Rogalski--Saint Raymond Theorem 1 audited below  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`.

This report imports a sharp area--perimeter--diameter inequality for centrally
symmetric planar convex bodies and applies it to the exact central symmetral of the
post-ZF force hull.  Combined with FS.4, FSDB, ZK, and the unrelaxed JC cavity bound,
it raises the explicit pinned/contact threshold from

```math
0.5882283437736394\ldots
```

to

```math
\boxed{
\lambda_{RS}=0.5921405436062881\ldots .
}
\tag{RS.1}
```

More strongly, the new endpoint cannot be attained by an unbounded post-ZF survivor
sequence.  Therefore there are absolute constants `epsilon_RS>0` and `D_0<infinity`
such that every post-ZF survivor with `D>=D_0` satisfies

```math
\boxed{
\frac{e_{BB}+2s_C}{D}\ge \lambda_{RS}+\epsilon_{RS}.
}
\tag{RS.2}
```

The value of `epsilon_RS` is not made explicit here.

The endpoint exclusion does **not** assume that equality in the imported symmetric
convex-body inequality characterizes the disk.  Rogalski--Saint Raymond explicitly
leave that uniqueness question open.  Instead, simultaneous saturation of FSDB forces
the half difference-body diameter-direction polygon to have a different limiting
perimeter from the force-hull central symmetral.

---

## 1. Starting endpoint and closing implication

Use the post-ZF notation

```math
L=e_{BB}+2s_C,
\qquad
k=d_H+s_Z,
\qquad
h=|E(H)|,
\qquad
P=\operatorname{per}F.
```

The September 10 FSJC theorem proved

```math
\liminf \frac LD\ge
\lambda_*=0.5882283437736394\ldots,
```

and current main excludes exact saturation `L/D -> lambda_*` by FS.4 disk rigidity.
No universal upper bound on `L/D` is known, so this is not yet a Level I
contradiction.

The new implication chain is

```text
FS.4 approximate central symmetry of F
  -> exact central symmetral S=(F-F)/2 has the same D and P as F
  -> Rogalski--Saint Raymond gives area(S) from P and D
  -> area(F) inherits that lower bound up to o(D^2)
  + FSDB diameter-density area lower bound
  + exact ZK attachment-cell budget
  + unrelaxed actual-perimeter JC cavity upper bound
  -> L/D >= lambda_RS > lambda_*
  -> equality forces simultaneous RS and FSDB saturation
  -> FSDB gap stability gives an incompatible perimeter for (1/2)P_H
  -> no endpoint sequence; hence L/D >= lambda_RS+epsilon_RS.
```

This still does not give a universal upper bound below the new lower threshold and
therefore does not settle Level I.

---

## 2. Literature import: Rogalski--Saint Raymond

Marc Rogalski and Jean Saint Raymond, *Inequalities About Symmetric Compact Convex
Sets in the Plane*, **American Mathematical Monthly** 92(7) (1985), 466--480,
Theorem 1.  Public author-hosted copy:

`https://webusers.imj-prg.fr/~jean.saint-raymond/preprints/IneqR2.pdf`

### Imported theorem

Let `S` be a centrally symmetric compact convex set in the Euclidean plane, with
area `A`, perimeter `P`, and diameter `D`.  Then

```math
\boxed{
A\ge
\frac{\pi}{(\pi-2)^2}
\left(\frac P2-D\right)^2.
}
\tag{RS.3}
```

The Euclidean disk attains equality.  The paper proves that the constant
`pi/(pi-2)^2` is best possible.

### Exact hypotheses and applicability

The theorem requires only planar compact convexity and central symmetry.  It does not
require smoothness, strict convexity, a lattice, a packing, or a finite vertex set.
The central symmetral used below satisfies these hypotheses exactly.

### Equality caveat

The same paper asks as its Problem 2 whether equality in (RS.3) forces the Euclidean
ball.  Consequently this report does **not** use such a uniqueness statement.

---

## 3. FS.4 transfers the symmetric inequality back to the actual force hull

Let `o` be the full-source circumcenter from FS.4, and write

```math
F_0:=F-o,
\qquad
S:=\frac12(F_0+(-F_0))=\frac12(F-F).
\tag{3.1}
```

The body `S` is centrally symmetric about the origin.

### Lemma RSF.1 — exact diameter and perimeter preservation

```math
\boxed{
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P.
}
\tag{3.2}
```

#### Proof

For every unit vector `u`, Minkowski addition and reflection give

```math
w_S(u)
=\frac12\bigl(w_{F_0}(u)+w_{-F_0}(u)\bigr)
=w_F(u).
```

The diameter of a planar convex body is the maximum of its directional widths, so
`diam S=diam F=D`.  Cauchy's perimeter formula is the integral of the width over a
projective half-circle, so equality of every width also gives `per S=per F=P`.
`\square`

### Lemma RSF.2 — quantitative Hausdorff transfer

With

```math
L_D=\sqrt{D\,3^{1/4}\sqrt D+3^{1/2}D}
=O(D^{3/4})
```

as in FS.4,

```math
\boxed{d_{\rm Haus}(F_0,S)\le L_D.}
\tag{3.3}
```

Consequently

```math
\boxed{
\operatorname{area}F
\ge
\operatorname{area}S-P L_D-\pi L_D^2.
}
\tag{3.4}
```

#### Proof

FS.4 gives

```math
d_{\rm Haus}(F_0,-F_0)\le2L_D.
```

For support functions,

```math
h_S(u)=\frac{h_{F_0}(u)+h_{F_0}(-u)}2.
```

Hence

```math
|h_S(u)-h_{F_0}(u)|
\le\frac12|h_{F_0}(-u)-h_{F_0}(u)|
\le L_D,
```

which is (3.3).  Thus `S subset F_0+L_D B_2`.  Steiner's formula gives

```math
\operatorname{area}(F_0+L_DB_2)
=\operatorname{area}F+P L_D+\pi L_D^2,
```

and (3.4) follows. `\square`

### Theorem RSF — perimeter-sensitive force-hull area floor

Put

```math
C_{RS}:=\frac\pi{(\pi-2)^2},
\qquad
\Psi(p):=C_{RS}\left(\frac p2-1\right)^2.
\tag{3.5}
```

Every post-ZF source satisfies the finite estimate

```math
\boxed{
\operatorname{area}F
\ge
C_{RS}\left(\frac P2-D\right)^2
-P L_D-\pi L_D^2.
}
\tag{3.6}
```

Thus along every subsequence on which `P/D -> p`,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}\ge\Psi(p).
}
\tag{3.7}
```

#### Proof

Apply (RS.3) to `S`, use (3.2), and then (3.4).  Since `P<=pi D` and
`L_D/D=O(D^{-1/4})`, the error in (3.6) is `o(D^2)`. `\square`

This is the first place in the current C-II stack where FS.4's approximate central
symmetry is combined with a sharp perimeter-sensitive area theorem.  It is stronger
near maximal perimeter than FSDB alone.

---

## 4. Combine RSF with FSDB, ZK, and JC

Pass to an arbitrary convergent post-ZF survivor subsequence and write

```math
\lambda:=\lim\frac LD,
\qquad
t:=\lim\frac{e_{BB}}D,
\qquad
y:=\lim\frac hD,
\qquad
p:=\lim\frac PD,
\qquad
\kappa:=\lim\frac kD.
\tag{4.1}
```

After further extraction these limits always exist.  The known bounds give

```math
2\rho\le y\le\pi,
\qquad
\max\{2,y\}\le p\le\pi,
\qquad
0\le t\le\lambda,
\tag{4.2}
```

where `rho` is the positive root of `rho=cos rho`.  Here `p>=2` is the elementary
perimeter-diameter inequality and `p>=y` follows from
`h<=q<=per(F)`.

FSDB gives

```math
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y):=\frac{y+\sin y}{4}.
\tag{4.3}
```

Together with RSF,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A(y,p):=\max\{\Phi(y),\Psi(p)\}.
}
\tag{4.4}
```

The exact ZK cell budget uses

```math
L_2=6-3k+L\ge0
```

and gives

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le
\frac\pi4(\lambda-3\kappa)^2.
\tag{4.5}
```

In particular `0<=3kappa<=lambda`.  Therefore the attachment gap satisfies

```math
\liminf\frac GD^2
\ge
A(y,p)-\frac\pi4(\lambda-3\kappa)^2.
\tag{4.6}
```

The unrelaxed actual-perimeter JC bound gives

```math
\limsup\frac GD^2
\le
\frac{(t+m(y,p))^2}{4\pi},
\qquad
m(y,p):=\min\{y,p-y\}.
\tag{4.7}
```

Dropping the favorable `kappa` correction and using `t<=lambda`, every survivor limit
must satisfy

```math
\boxed{
(\pi^2+1)\lambda^2
+2m(y,p)\lambda
+m(y,p)^2
-4\pi A(y,p)
\ge0.
}
\tag{4.8}
```

For fixed `A>0` and `m>=0`, let `R(A,m)` denote the positive root of the corresponding
quadratic equality.  Implicit differentiation gives

```math
\frac{\partial R}{\partial A}
=\frac{2\pi}{(\pi^2+1)R+m}>0,
\qquad
\frac{\partial R}{\partial m}
=-\frac{R+m}{(\pi^2+1)R+m}<0.
\tag{4.9}
```

Thus more area raises the required currency while more cavity perimeter lowers it.

---

## 5. Exact minimization of the new feasible region

For fixed `y`, let `p_c(y)` be the unique perimeter at which the two area floors cross:

```math
\Psi(p_c(y))=\Phi(y).
\tag{5.1}
```

Since `Psi` is increasing on `[2,pi]`,

```math
\boxed{
p_c(y)
=2+2(\pi-2)\sqrt{\frac{\Phi(y)}\pi}.
}
\tag{5.2}
```

### Lemma 5.1 — the crossover is always feasible

For `2rho<=y<=pi`,

```math
\boxed{p_c(y)\ge\max\{2,y\}.}
\tag{5.3}
```

#### Proof

The assertion is immediate when `y<2`.  For `2<=y<=pi`, put

```math
d(y):=\Phi(y)-\Psi(y).
```

Then

```math
d''(y)=-\frac{\sin y}{4}-\frac{C_{RS}}2<0.
```

Also `d(2)=Phi(2)>0` and `d(pi)=0`, because `Psi(pi)=pi/4=Phi(pi)`.
Concavity puts `d` above its endpoint chord, hence `d(y)>=0`.  Therefore
`Psi(y)<=Phi(y)` and `p_c(y)>=y`. `\square`

### Lemma 5.2 — fixed-y minimization

For each fixed `y`, the smallest root allowed by (4.8) is

```math
\boxed{
\begin{cases}
R(\Phi(y),y),&p_c(y)\ge2y,\\[3pt]
R(\Phi(y),p_c(y)-y),&p_c(y)\le2y.
\end{cases}}
\tag{5.4}
```

#### Proof

For `p<=p_c`, the area floor is the fixed value `Phi(y)`.  While `p<=2y`,
`m=p-y` increases with `p`, so (4.9) shows that the threshold decreases.  If
`2y<=p<=p_c`, then `m=y` and the threshold is constant.

It remains to show that after `p_c` the threshold cannot decrease.  First note that
`p_c(y)>3` on the whole DB interval.  FSJC already records

```math
\frac{739}{1000}<\rho<\frac{37}{50}.
\tag{5.5}
```

Using `sin rho=sqrt(1-rho^2)` gives

```math
\sin\rho>\frac{84}{125},
\qquad
\Phi(2\rho)>0.617804.
\tag{5.6}
```

The standard bound `pi>157/50` gives

```math
C_{RS}<\frac{121}{50},
\qquad
\Psi(3)=\frac{C_{RS}}4<0.605.
\tag{5.7}
```

Since `Phi` is increasing, (5.6)--(5.7) imply `p_c(y)>3`.

On the branch `p_c<=p<=2y`, put

```math
H(p,\lambda)
=(\pi^2+1)\lambda^2
+2(p-y)\lambda+(p-y)^2-4\pi\Psi(p).
```

At its positive root, `lambda<1`, because `Psi(p)<=pi/4` and hence
`(pi^2+1)lambda^2<=pi^2`.  Also `p-y<=pi`.  Therefore

```math
\partial_pH
=2(\lambda+p-y)-4\pi C_{RS}\left(\frac p2-1\right)
<2(1+\pi)-2\pi C_{RS}.
```

The elementary bounds `3<pi<22/7` imply `C_RS>2`, so the last quantity is less
than `2(1-pi)<0`.  Since `H` is increasing in `lambda`, its threshold root increases
with `p`.

For `p>=2y`, the cavity term is fixed at `m=y`; once `Psi` is active it strictly
increases with `p`, so the threshold again increases.  These observations prove
(5.4). `\square`

### Lemma 5.3 — there is one crossover between the two fixed-y regimes

There is a unique

```math
\boxed{y_0\in(2\rho,\pi/2)}
\tag{5.8}
```

such that

```math
\boxed{p_c(y_0)=2y_0.}
\tag{5.9}
```

Equivalently,

```math
\boxed{
\frac\pi{(\pi-2)^2}(y_0-1)^2
=\frac{y_0+\sin y_0}{4}.
}
\tag{5.10}
```

#### Proof

Differentiate (5.2):

```math
p_c'(y)
=\frac{\pi-2}{\sqrt\pi}
\frac{\Phi'(y)}{\sqrt{\Phi(y)}}.
```

On the relevant interval, `(pi-2)/sqrt(pi)<1`, `Phi'(y)<=1/2`, and
`Phi(y)>1/4`; hence

```math
\boxed{p_c'(y)<1.}
\tag{5.11}
```

Thus `p_c(y)-2y` is strictly decreasing.

At `y=2rho`, use (5.5)--(5.7):

```math
\Psi(4\rho)
=C_{RS}(2\rho-1)^2
<\frac{121}{50}\left(\frac{12}{25}\right)^2
<0.558
<\Phi(2\rho).
```

Hence `p_c(2rho)>4rho`.  At `y=pi/2`,

```math
\Phi(\pi/2)=\frac{\pi/2+1}{4}<\frac\pi4=\Psi(\pi),
```

so `p_c(pi/2)<pi`.  The intermediate value theorem and strict monotonicity prove
(5.8)--(5.9). `\square`

### Theorem FSRS.1 — explicit improved post-ZF floor

Let `y_0` be defined by (5.8)--(5.10), and let `lambda_RS` be the positive root of

```math
\boxed{
(\pi^2+1)\lambda_{RS}^2
+2y_0\lambda_{RS}
+y_0^2
-\pi(y_0+\sin y_0)=0.
}
\tag{5.12}
```

Then every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}\ge\lambda_{RS}.
}
\tag{5.13}
```

The exact minimizer of the relaxed asymptotic feasible region is

```math
\boxed{(y,p)=(y_0,2y_0).}
\tag{5.14}
```

#### Proof

If `y<=y_0`, Lemmas 5.2--5.3 give the fixed-y threshold
`R(Phi(y),y)`.  This is the left FSJC threshold.  Its defining polynomial is

```math
J(y,\lambda)
=(\pi^2+1)\lambda^2+2y\lambda+y^2-\pi(y+\sin y).
```

FSJC proves these roots are all above `lambda_*>1/2`.  For `lambda>=1/2`,

```math
\partial_yJ
=2\lambda+2y-\pi(1+\cos y)>0
```

throughout `[2rho,pi/2]`: the right side is increasing in `y`, and at `2rho`
its lower bound obtained from (5.5) and `pi<22/7` is already positive.  Therefore
implicit differentiation shows that `R(Phi(y),y)` is strictly decreasing in `y`.

If `y>=y_0`, Lemmas 5.2--5.3 give the fixed-y threshold

```math
R(\Phi(y),n(y)),
\qquad
n(y):=p_c(y)-y.
```

Equation (5.11) gives `n'(y)<0`, while `Phi'(y)>=0`.  For the defining equation

```math
(\pi^2+1)\lambda^2+2n\lambda+n^2-4\pi\Phi(y)=0,
```

the derivative with respect to `y` at fixed `lambda` is

```math
2n'(\lambda+n)-4\pi\Phi'(y)<0.
```

Hence the positive root is strictly increasing in `y`.

The decreasing and increasing branches meet only at `y_0`; there
`p_c(y_0)=2y_0` and (5.12) is exactly the threshold equation.  This proves
(5.13)--(5.14). `\square`

For reference only,

```math
\begin{aligned}
y_0&=1.5100171437629435858\ldots,\\
p_0:=2y_0&=3.0200342875258871717\ldots,\\
\Phi(y_0)&=0.6270426644374162987\ldots,\\
\lambda_{RS}&=0.5921405436062881570\ldots .
\end{aligned}
\tag{5.15}
```

The constants are defined by (5.10) and (5.12); the decimals are not proof inputs.
Since `y_0<pi/2` and the left FSJC threshold is strictly decreasing,

```math
\lambda_{RS}>\lambda_*.
```

---

## 6. Saturating the new threshold forces an exact normal form

Assume for contradiction that an unbounded post-ZF sequence has

```math
\frac LD\to\lambda_{RS}.
\tag{6.1}
```

The strict uniqueness of the minimizer in Section 5 and compactness of the
`(y,p)` domain force

```math
\boxed{
\frac hD\to y_0,
\qquad
\frac PD\to2y_0.
}
\tag{6.2}
```

Pass to a subsequence with `k/D -> kappa` and `e_BB/D -> t`.  At the endpoint,
(4.6)--(4.7) become

```math
\Phi(y_0)-\frac\pi4(\lambda_{RS}-3\kappa)^2
\le
\frac{(t+y_0)^2}{4\pi}.
\tag{6.3}
```

By (5.12), equality holds in (6.3) when `kappa=0` and `t=lambda_RS`.  Since
`0<=3kappa<=lambda_RS` and `t<=lambda_RS`, any `kappa>0` makes the left side strictly
larger while any `t<lambda_RS` makes the right side strictly smaller.  Hence

```math
\boxed{
\frac{d_H+s_Z}{D}\to0,
\qquad
\frac{e_{BB}}D\to\lambda_{RS},
\qquad
\frac{s_C}{D}\to0.
}
\tag{6.4}
```

Since `q=h+d_H`, also

```math
\boxed{\frac qD\to y_0.}
\tag{6.5}
```

Let `A_F=area(F)`.  The cell bound and JC upper bound now imply

```math
\limsup\frac{A_F}{D^2}
\le
\frac\pi4\lambda_{RS}^2
+
\frac{(\lambda_{RS}+y_0)^2}{4\pi}
=\Phi(y_0),
```

where the equality is (5.12).  The combined area lower bound gives the reverse
inequality.  Therefore

```math
\boxed{
\frac{\operatorname{area}F}{D^2}\to
A_0:=\Phi(y_0)=\Psi(2y_0).
}
\tag{6.6}
```

By Lemma RSF.2, the exact central symmetral `S=(F-F)/2` satisfies

```math
\boxed{
\frac{\operatorname{area}S}{D^2}\to A_0,
\qquad
\frac{\operatorname{per}S}{D}\to2y_0,
\qquad
\operatorname{diam}S=D.
}
\tag{6.7}
```

Thus the endpoint simultaneously saturates the RSF and FSDB area floors.

---

## 7. FSDB saturation gives an incompatible perimeter

For every actual diameter edge `e`, let `u_e` be its projective unit direction and
put, as in DB/FSDB,

```math
P_H:=D\,\operatorname{conv}\{\pm u_e:e\in E(H)\},
\qquad
Q_H:=\frac12P_H.
\tag{7.1}
```

Because `P_H subset F-F`, there is an exact finite containment

```math
\boxed{Q_H\subseteq S.}
\tag{7.2}
```

Order the `h` projective diameter directions around the circle of circumference
`pi`, and let their gaps be

```math
\gamma_1,\ldots,\gamma_h,
\qquad
\gamma_i\ge\delta_D:=2\arcsin\frac1{2D},
\qquad
\sum_i\gamma_i=\pi.
\tag{7.3}
```

The normalized area and perimeter of `Q_H` are exactly

```math
\boxed{
\frac{\operatorname{area}Q_H}{D^2}
=\frac14\sum_i\sin\gamma_i,
\qquad
\frac{\operatorname{per}Q_H}{D}
=2\sum_i\sin\frac{\gamma_i}{2}.
}
\tag{7.4}
```

FSDB's gap minimization gives

```math
\frac14\sum_i\sin\gamma_i
\ge
\frac14\left[(h-1)\sin\delta_D
+\sin((h-1)\delta_D)\right].
\tag{7.5}
```

Under `h/D -> y_0`, the right side tends to `Phi(y_0)=A_0`.  By (7.2) and
(6.7), the left side is at most `A_0+o(1)`.  Hence

```math
\boxed{
\frac{\operatorname{area}Q_H}{D^2}\to A_0,
}
\tag{7.6}
```

so the projective gap inequality itself is asymptotically saturated.

### Lemma 7.1 — stability of the FSDB projective-gap minimum

If (7.3) holds, `h/D -> y in (0,pi)`, and the area in (7.4) approaches the lower
bound in (7.5), then

```math
\boxed{
\frac{\operatorname{per}Q_H}{D}
\to y+2\cos\frac y2.
}
\tag{7.7}
```

#### Proof

Write `delta=delta_D` and

```math
x_i:=\gamma_i-\delta\ge0,
\qquad
E_D:=\sum_i x_i=\pi-h\delta.
```

Then `delta->0` and `E_D->E:=pi-y in (0,pi)`.  Define

```math
g_D(x):=\sin(\delta+x)-\sin\delta.
```

On `[0,E_D]`, `g_D` is strictly concave, `g_D(0)=0`, and therefore
`g_D(x)/x` is strictly decreasing.  If `M_D=max_i x_i`, concavity gives

```math
\sum_i g_D(x_i)
\ge
\frac{E_D}{M_D}g_D(M_D)
\ge g_D(E_D).
\tag{7.8}
```

The last term is exactly the one-large-gap minimum behind (7.5).  If area saturation
holds but `M_D` does not tend to `E_D`, pass to a subsequence with
`M_D->M<E`.  Taking limits in (7.8) gives

```math
\frac{E}{M}\sin M>\sin E
```

(with the left side interpreted as `E` when `M=0`), because `sin x/x` is strictly
decreasing on `(0,pi)`.  This produces a fixed positive area gap, contradiction.
Thus

```math
M_D\to E_D,
\qquad
\sum_{i\ne i_*}x_i=E_D-M_D\to0
```

for an index `i_*` attaining the maximum.

Consequently

```math
\gamma_{i_*}\to\pi-y,
\qquad
\max_{i\ne i_*}\gamma_i\to0,
\qquad
\sum_{i\ne i_*}\gamma_i\to y.
```

For the small gaps, `2sin(z/2)=z+O(z^3)` uniformly, and the sum of the cubic errors
is `o(1)` because their maximum tends to zero while their total remains bounded.
Using (7.4),

```math
\frac{\operatorname{per}Q_H}{D}
\to
2\sin\frac{\pi-y}{2}+y
=y+2\cos\frac y2.
```

This proves (7.7). `\square`

Apply Lemma 7.1 at `y=y_0`:

```math
\boxed{
\frac{\operatorname{per}Q_H}{D}
\to y_0+2\cos\frac{y_0}{2}.
}
\tag{7.9}
```

### Theorem FSRS.2 — the explicit endpoint is unattainable

There is no unbounded post-ZF survivor sequence satisfying (6.1).

#### Proof

Normalize `S` and `Q_H` by `D`.  Both are centrally symmetric convex bodies contained
in the radius-`1/2` disk, and `Q_H/D subset S/D`.  By Blaschke selection pass to a
subsequence on which both converge in Hausdorff distance to convex bodies
`Q_infty subset S_infty`.

Equations (6.7) and (7.6) give

```math
\operatorname{area}Q_\infty
=\operatorname{area}S_\infty
=A_0>0.
```

A proper containment between two full-dimensional compact convex bodies has positive
area difference, so

```math
Q_\infty=S_\infty.
\tag{7.10}
```

Perimeter is continuous under Hausdorff convergence of planar convex bodies.  Hence
(6.7), (7.9), and (7.10) force

```math
2y_0=y_0+2\cos\frac{y_0}{2},
```

or

```math
y_0=2\cos\frac{y_0}{2}.
\tag{7.11}
```

But `y=2rho` satisfies (7.11) exactly because `rho=cos rho`.  The function

```math
y-2\cos(y/2)
```

has derivative `1+sin(y/2)>0`, so (7.11) has a unique root.  Section 5 proved
`y_0>2rho`.  Contradiction. `\square`

This endpoint contradiction uses the actual complete diameter-direction set through
`P_H`; it does not depend on an unproved equality classification for (RS.3).

---

## 8. Uniform strict improvement

If no absolute improvement above `lambda_RS` existed, for every integer `j` one could
choose a post-ZF survivor with `D_j->infinity` and

```math
\frac{L_j}{D_j}<\lambda_{RS}+\frac1j.
```

Theorem FSRS.1 forces `L_j/D_j -> lambda_RS`, contradicting Theorem FSRS.2.  Therefore
there exist absolute `epsilon_RS>0` and `D_0<infinity` such that (RS.2) holds.

This is a nonexplicit strict improvement above an explicit base constant.  A
quantitative stability version of Section 7 would make `epsilon_RS` explicit.

---

## 9. Exact target implication

Before this report, current main had

```text
L/D >= 0.5882283437736394...
and the exact endpoint is excluded, hence L/D >= 0.588228... + epsilon.
```

This report gives

```text
L/D >= lambda_RS = 0.5921405436062881...
and the exact new endpoint is excluded, hence
L/D >= lambda_RS + epsilon_RS
for some absolute epsilon_RS>0.
```

The new endpoint normal form, before its contradiction, is

```math
\begin{aligned}
h/D&\to y_0,\\
P/D&\to2y_0,\\
(d_H+s_Z)/D&\to0,\\
s_C/D&\to0,\\
e_{BB}/D&\to\lambda_{RS},\\
q/D&\to y_0,\\
\operatorname{area}(F)/D^2&\to\Phi(y_0)=\Psi(2y_0).
\end{aligned}
```

This is still a lower-bound theorem.  There is no proved universal upper bound on
`L/D` that crosses it, so Level I remains open.

---

## 10. Exact remaining lemma

A useful next theorem must produce a contradictory **upper** restriction or turn the
strict endpoint gap quantitative enough to interact with another structural bound.
The cleanest post-ZF formulation is:

```math
\boxed{
\text{Prove a universal }\Lambda_{\rm top}<\lambda_{RS}+\epsilon_{RS}
\text{ with }
\frac{e_{BB}+2s_C}{D}\le\Lambda_{\rm top}+o(1),
}
\tag{10.1}
```

or construct a strict sub-`D` competitor whenever the left side lies above the new
lower region.

A nearer structural target is a quantitative version of Lemma 7.1 plus convex
containment stability: convert the fixed perimeter mismatch

```math
2y_0-\left(y_0+2\cos\frac{y_0}{2}\right)>0
```

into an explicit positive area/cavity penalty.  That would give an explicit increment
above `lambda_RS` rather than a compactness-only `epsilon_RS` and may be iterated with
the exact PC/ZK ledgers.

---

## 11. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | Its central symmetral and perimeter can nearly saturate the symmetric convex-body inequality, but it does not satisfy the post-ZF low `L/D` currency endpoint; the contradiction uses ZK/JC and the complete diameter-direction set simultaneously. |
| dense isolated shell fillings | yes | FS.4 is a full-source theorem and the argument never assumes `n-v=O(D)` or force-hull population saturation. |
| FS response trace defect | yes | No arbitrary boundary-data operator estimate or trace-smallness statement is used. |
| near-radial coordinate response only | yes | Central symmetry enters only through FS.4's proved Hausdorff estimate; it is not upgraded to an operator norm assertion. |
| RS equality uniqueness | not assumed | The 1985 paper explicitly leaves uniqueness as an open problem; Section 7 avoids it by using FSDB saturation. |
| perfect diameter matching | already excluded | MFS closes that branch independently; this theorem covers the remaining post-ZF population. |

The decisive global-optimality input absent from the shell regressions is the full
post-ZF source package: the lexicographically selected global minimizer, FS.4's
full-source circumradius transport, ZF/ZS diameter lower structure, the exact ZK
attachment-cell budget, and JC's source cavity upper bound.

---

## 12. Failed routes and no-go results

1. **Exact whole-source Oler reversal.**  The identity
   
   ```math
   \delta_K+\mathscr O_A
   =c_0P-\frac\pi4\left(\frac{2\sqrt3}{\pi}(n-1)-D^2\right)
   ```

   shows that the requested reverse inequality is exactly the finite lower bound
   `D^2 >= (2sqrt(3)/pi)(n-1)`.  FS.1--FS.4 alone do not supply this discrete
   packing-number jump.

2. **Pure ZF face bookkeeping.**  The exact defect ledger makes
   `b+Q>2h` equivalent to `s_Z<0`; Euler accounting cannot prove it because
   `s_Z>=0` by definition.

3. **Generic symmetric equality classification.**  It is invalid to claim that equality
   in (RS.3) forces a disk; Rogalski--Saint Raymond list that as an open problem.
   The endpoint proof therefore uses FSDB direction-gap stability instead.

4. **Scalar-constant iteration without structure.**  Merely replacing `0.588228` by a
   decimal and rerunning the old JC relaxation would not justify a strict improvement.
   Sections 5--7 identify the exact new minimizer and exclude its equality geometry.

---

## 13. Literature imported

### Rogalski--Saint Raymond (1985)

- Link: `https://webusers.imj-prg.fr/~jean.saint-raymond/preprints/IneqR2.pdf`
- Citation: Marc Rogalski and Jean Saint Raymond, *Inequalities About Symmetric Compact Convex Sets in the Plane*, American Mathematical Monthly 92(7) (1985), 466--480.
- Theorem: Theorem 1.
- Exact hypotheses: centrally symmetric compact convex set in the Euclidean plane.
- Exact conclusion: (RS.3), with best constant `pi/(pi-2)^2`; the Euclidean disk attains equality.
- Normalization here: divide area by `D^2` and perimeter by `D`, giving `Psi(p)`.
- Applicable here: yes, exactly, to `S=(F-F)/2`.
- Equality limitation: the paper's Problem 2 asks whether equality forces the disk; uniqueness is not imported.
- Route effect: adds a perimeter-sensitive quadratic force-hull area floor that crosses FSDB before the old FSJC midpoint.

No other external theorem is used in the new proof.

---

## 14. Computation and reproducibility

No computation is a proof dependency.  The defining equations are (5.10) and (5.12).
Standard bisection/Newton evaluation gives the decimals in (5.15).  A small
standard-library reproduction script should be added under `research/` separately;
it should be classified as numerical verification of the displayed decimals and
monotonicity diagnostics only, not as a proof of the global theorem.

---

## 15. Canonical promotion recommendation

**Hold as report pending independent audit.**

If the audit confirms the literature normalization, the central-symmetral transfer,
the two-variable minimization, and the FSDB saturation lemma, promote the following
facts into the Target C route map/addendum:

1. RSF perimeter-sensitive force-hull area floor (3.6)--(3.7);
2. explicit post-ZF currency floor `lambda_RS` (5.13);
3. endpoint normal form (6.2)--(6.7);
4. FSDB projective-gap stability Lemma 7.1;
5. endpoint exclusion and nonexplicit uniform gap (RS.2).

Do not promote a disk equality classification for the imported theorem.

---

## 16. Next run

Quantify Section 7.  The endpoint has a fixed normalized perimeter mismatch

```math
\Delta_P
:=y_0-2\cos(y_0/2)>0
```

between the central symmetral demanded by JC and the FSDB direction body demanded by
area saturation.  Derive an explicit lower bound on the area increment of a
central-symmetric diameter-one body `S` containing `Q_H` when
`per(S)-per(Q_H)>=Delta_P/2`, while retaining the projective-gap area defect.  Feed
that increment back into (4.8).  This is the shortest route to an explicit improvement
beyond `lambda_RS` and may expose a contradiction with the exact PC/ZK topology.

---

## 17. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New literature input (Rogalski--Saint Raymond 1985, Thm. 1):
for centrally symmetric planar convex S,
  area(S) >= [pi/(pi-2)^2] (per(S)/2-diam(S))^2.
Disk attains equality, but uniqueness is explicitly open and is NOT used.

For the force hull F, set S=(F-F)/2. Widths are identical, so
  diam(S)=D, per(S)=per(F).
FS.4 gives d_H(F-o,S)<=L_D=o(D), hence
  area(F)/D^2 >= Psi(p)-o(1),
  Psi(p)=pi/(pi-2)^2 (p/2-1)^2,
  p=per(F)/D.
Combine with FSDB Phi(y)=(y+sin y)/4, y=h/D.
ZK+JC imply
  (pi^2+1)lambda^2+2m lambda+m^2
    -4pi max(Phi(y),Psi(p)) >=0,
  lambda=(e_BB+2s_C)/D,
  m=min(y,p-y),
  2rho<=y<=pi, max(2,y)<=p<=pi.

For fixed y the threshold is minimized at m=y if p_c(y)>=2y,
and at p=p_c(y) if p_c(y)<=2y, where
  p_c(y)=2+2(pi-2)sqrt(Phi(y)/pi).
There is a unique y0 in (2rho,pi/2) with p_c(y0)=2y0, equivalently
  [pi/(pi-2)^2](y0-1)^2=(y0+sin y0)/4.
The threshold decreases before y0 and increases after it. Thus
  lambda >= lambda_RS,
where
  (pi^2+1)lambda_RS^2+2y0 lambda_RS+y0^2
    -pi(y0+sin y0)=0,
  y0=1.5100171437629435...,
  lambda_RS=0.5921405436062881....

Endpoint lambda->lambda_RS forces
  h/D->y0,
  per(F)/D->2y0,
  (d_H+s_Z)/D->0,
  s_C/D->0,
  e_BB/D->lambda_RS,
  area(F)/D^2->Phi(y0).
Let Q_H=(D/2)conv{+-u_e} subset S. Endpoint saturation also forces
area(Q_H)/D^2->Phi(y0). If gamma_i are projective direction gaps,
FSDB stability shows all excess gap concentrates in one gap, hence
  per(Q_H)/D -> y0+2cos(y0/2).
But area(Q_H) and area(S) have the same positive limit with Q_H subset S,
so Hausdorff limits coincide and their perimeters must agree. JC requires
per(S)/D->2y0. Therefore y0=2cos(y0/2), whose unique solution is y0=2rho,
contradicting y0>2rho.

Hence the explicit endpoint is unattainable. There exists epsilon_RS>0 such that
all sufficiently large post-ZF survivors satisfy
  (e_BB+2s_C)/D >= 0.5921405436062881... + epsilon_RS.
Level I remains open because no crossing upper bound is proved.

Report:
  docs/reports/target_c_rs_symmetric_area_floor_059214_2026-09-10.md
```
