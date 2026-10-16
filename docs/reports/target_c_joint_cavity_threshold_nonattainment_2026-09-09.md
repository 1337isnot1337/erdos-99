<!-- migration-source: path=docs/reports/target_c_joint_cavity_threshold_nonattainment_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=f3bd57717304bbb6de916be5fa4c91ecafa281bb; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — the joint-cavity threshold is not attainable

**Date:** 2026-09-09  
**Run type:** compactness / equality-case stability theorem  
**Target:** Target C C-II after ZF/DB/PI/JC  
**Depends on:** JC joint cavity budget, GU attachment-cell upper bound, Rosenthal--Szász equality case, Blaschke--Lebesgue theorem  
**External sources:** Balestro--Martini, *The Rosenthal--Szasz inequality for normed planes*, arXiv:1804.00215 (classical Euclidean theorem recalled in the introduction); Harrell, *A direct proof of a theorem of Blaschke and Lebesgue*, arXiv:math/0009137  
**Computation:** arithmetic only for displayed decimals

## LEVEL I STATUS

`STILL OPEN`

JC proves the explicit post-ZF floor

\[
\lambda:=\frac{e_{BB}+2s_C}{D}
\not\to\lambda_1^- ,
\qquad
\lambda_1=0.4633168953789\ldots,
\]

in the sense that every unbounded survivor sequence has `liminf lambda>=lambda_1`.

The scalar calculation used only the universal bounds

\[
\min\{h,\pi D-h\}\le\pi D/2
\]

and the PI area floor. Equality in the scalar bound would force the force-hull perimeter to approach the Rosenthal--Szász maximum `pi D`. The equality case then makes the normalized force-hull limit a body of constant width one, and Blaschke--Lebesgue raises its area from PI's `0.497856...` to at least `0.704770...`. That is incompatible with the same cavity capacity which defined `lambda_1`.

Therefore the JC threshold is not merely unattained at equality: compactness gives a **uniform positive gap**.

### Theorem JN — strict nonattainment

There exists an absolute constant

\[
\boxed{\eta_0>0}
\tag{JN.1}
\]

such that every sufficiently large audited post-ZF survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_1+\eta_0.
}
\tag{JN.2}
\]

The proof is qualitative and does not make `eta_0` explicit.

---

## 1. What equality in JC would require

Suppose for contradiction that there is an unbounded survivor sequence with

\[
\lambda_j:=\frac{e_{BB,j}+2s_{C,j}}{D_j}
\longrightarrow\lambda_1.
\tag{JN.3}
\]

Pass to a subsequence on which

\[
t_j:=\frac{e_{BB,j}}{D_j}\to t,
\qquad
 y_j:=\frac{h_j}{D_j}\to y.
\tag{JN.4}
\]

The bounds `0<=t_j<=lambda_j` and `h_j<=pi D_j+O(1)` make this possible.

JC gives the diameter-sensitive necessary inequality

\[
A_{PI}-\frac\pi4\lambda^2
\le
\frac{(t+\min\{y,\pi-y\})^2}{4\pi},
\tag{JN.5}
\]

where

\[
A_{PI}=\frac12\sin(2\rho).
\]

By definition, `lambda_1` is the positive solution of

\[
A_{PI}-\frac\pi4\lambda_1^2
=
\frac{(\lambda_1+\pi/2)^2}{4\pi}.
\tag{JN.6}
\]

But

\[
t\le\lambda_1,
\qquad
\min\{y,\pi-y\}\le\pi/2.
\]

Thus JN.5--JN.6 can hold only if both inequalities are equalities:

\[
\boxed{t=\lambda_1,}
\tag{JN.7}
\]

and

\[
\boxed{y=\pi/2.}
\tag{JN.8}
\]

Moreover the lower and upper normalized gap bounds themselves converge to the common value

\[
U_1
:=
A_{PI}-\frac\pi4\lambda_1^2
=
\frac{(\lambda_1+\pi/2)^2}{4\pi}
=0.3292610673\ldots .
\tag{JN.9}
\]

So every relaxation used in the joint cavity upper bound must be asymptotically tight.

---

## 2. Tightness forces `per(F)/D -> pi`

Recall

\[
E_{out}:=\sum_P(L_P-3).
\]

The proof of JC.12 actually gives the sharper finite inequality

\[
\boxed{
E_{out}+Q
\le
\pi D-h+e_{BB}
-
\bigl[(\pi D-P_F)+3d_H+(z-Q)\bigr],
}
\tag{JN.10}
\]

where

\[
P_F=\operatorname{per}(F),
\qquad
z=Q+2s_Z.
\]

Every term in the square bracket is nonnegative.

JC's area estimate is

\[
H_{out}+A_{exc}
\le
\frac{(E_{out}+Q)^2}{4\pi}+o(D^2),
\tag{JN.11}
\]

while the gap charging gives

\[
G\le H_{out}+A_{exc}+O(D).
\tag{JN.12}
\]

Since JN.9 says the normalized upper bound is attained asymptotically, JN.10 cannot lose a positive linear amount. Using JN.7--JN.8,

\[
\frac{\pi D_j-h_j+e_{BB,j}}{D_j}
\to
\frac\pi2+\lambda_1.
\]

Therefore JN.10--JN.12 force

\[
\boxed{
\frac{\pi D_j-P_{F,j}}{D_j}\longrightarrow0.
}
\tag{JN.13}
\]

In particular

\[
\boxed{
\frac{P_{F,j}}{D_j}\longrightarrow\pi.
}
\tag{JN.14}
\]

The same saturation also gives `d_H/D->0` and `(z-Q)/D=2s_Z/D->0`, but those facts are not needed below.

---

## 3. Normalize and take a force-hull limit

Scale each force hull by `D_j` and translate it so that one point lies at the origin:

\[
\widetilde F_j:=D_j^{-1}(F_j-p_j).
\]

Then

\[
\operatorname{diam}(\widetilde F_j)=1.
\]

All sets lie in a fixed unit disk after translation. By Blaschke selection, pass to a Hausdorff-convergent subsequence

\[
\widetilde F_j\longrightarrow F_\infty.
\tag{JN.15}
\]

For planar convex bodies, diameter, perimeter, and area are continuous under Hausdorff convergence. Hence JN.14 gives

\[
\operatorname{diam}(F_\infty)=1,
\qquad
\operatorname{per}(F_\infty)=\pi.
\tag{JN.16}
\]

The classical Rosenthal--Szász theorem states

\[
\operatorname{per}(K)\le\pi\operatorname{diam}(K)
\]

for every planar convex body, with equality exactly for bodies of constant width equal to the diameter. Thus JN.16 implies

\[
\boxed{F_\infty\text{ has constant width }1.}
\tag{JN.17}
\]

---

## 4. Blaschke--Lebesgue gives a much larger limiting area

The Blaschke--Lebesgue theorem says that among planar convex bodies of constant width one, the Reuleaux triangle has minimum area. Therefore

\[
\boxed{
\operatorname{area}(F_\infty)
\ge
A_{BL}:=\frac{\pi-\sqrt3}{2}
=0.7047709230\ldots .
}
\tag{JN.18}
\]

By area continuity,

\[
\liminf_j
\frac{\operatorname{area}(F_j)}{D_j^2}
\ge A_{BL}.
\tag{JN.19}
\]

GU's attachment-cell upper bound depends only on

\[
L=e_{BB}+2s_C.
\]

Along JN.3,

\[
\limsup_j
\frac1{D_j^2}
\sum_r\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4\lambda_1^2.
\tag{JN.20}
\]

Consequently

\[
\boxed{
\liminf_j\frac{G_j}{D_j^2}
\ge
A_{BL}-\frac\pi4\lambda_1^2
=0.53617535399\ldots .
}
\tag{JN.21}
\]

But JN.9--JN.12 give

\[
\limsup_j\frac{G_j}{D_j^2}
\le U_1
=0.32926106730\ldots .
\tag{JN.22}
\]

This is impossible.

Therefore no unbounded post-ZF survivor sequence can satisfy `lambda_j->lambda_1`. `square`

---

## 5. Compactness upgrades nonattainment to a uniform gap

JC already proves the universal asymptotic lower bound

\[
\liminf\lambda_j\ge\lambda_1
\]

for every unbounded survivor sequence.

If JN.2 were false for every `eta_0>0`, then for each integer `m` one could choose a sufficiently large survivor with

\[
\lambda<\lambda_1+1/m.
\]

Using the JC lower bound to choose the diameters increasingly large, a diagonal sequence would satisfy

\[
\lambda_j\to\lambda_1,
\]

contradicting Sections 1--4.

Hence some universal `eta_0>0` exists. This proves Theorem JN.

No numerical value is claimed because the argument uses only compactness and equality cases, not a quantitative stability theorem for Rosenthal--Szász or Blaschke--Lebesgue.

---

## 6. What the extremal analysis also reveals

Any hypothetical sequence attempting to approach the old JC threshold would have to satisfy simultaneously

\[
\frac hD\to\frac\pi2,
\qquad
\frac{e_{BB}}D\to\lambda_1,
\qquad
\frac{s_C}{D}\to0,
\tag{JN.23}
\]

and

\[
\frac{P_F}{D}\to\pi,
\qquad
\frac{d_H}{D}\to0,
\qquad
\frac{s_Z}{D}\to0.
\tag{JN.24}
\]

Thus the numerical worst case was already a near-constant-width loaded shell, not an arbitrary cavity. The constant-width equality theory removes it.

This is useful independently of the nonconstructive gap: future quantitative work can target stability of this near-shell normal form.

---

## 7. Regression audit

### Reuleaux triangle

It attains the Blaschke--Lebesgue area minimum among constant-width bodies, so JN uses the sharp possible limiting area. It is not a large triangle-free source and is only an equality body for the convex-geometric limit.

### Regular odd shells

Their hulls approach a circle, hence have normalized perimeter near `pi` and area near `pi/4`, which is above the Blaschke--Lebesgue floor. They do not contradict JN; they remain local/non-global high-surplus regressions.

### Near-maximal perimeter without pointwise constant width

JN does not assume finite members have constant width. Constant width appears only in the Hausdorff limit from equality in Rosenthal--Szász.

### No hidden quantitative stability claim

The proof does not assert an explicit estimate between perimeter deficit and Hausdorff distance to constant-width bodies. The existence of `eta_0` follows by contradiction/compactness only.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| threshold approach forces `h/D->pi/2` | proved | equality in JC scalar relaxation |
| threshold approach forces `P_F/D->pi` | proved | exact remainder JN.10 |
| Hausdorff limit is constant width | classical input | Rosenthal--Szász equality |
| limit area at least `(pi-sqrt3)/2` | classical input | Blaschke--Lebesgue |
| sequence `lambda->lambda_1` impossible | proved | gap lower `0.536...` vs upper `0.329...` |
| some universal `eta_0>0` exists | proved nonconstructively | diagonal compactness |
| explicit improved constant | not proved | would require quantitative stability or another finite inequality |
| Level I | still open | high-surplus near-shell branch remains |

---

## 9. Next target

Two routes are now especially concrete:

1. import or prove a quantitative stability form of Rosenthal--Szász/Blaschke--Lebesgue to turn `eta_0` into an explicit numerical improvement;
2. attack the high-surplus shell directly using the coexistence constraints NB, JC/JN, ZK, and the loaded degree-three boundary geometry.
