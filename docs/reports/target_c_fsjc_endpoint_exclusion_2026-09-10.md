<!-- theorem-state: {"artifact_id":"ART-697F9FF8140B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fsjc_endpoint_exclusion_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=cc52e84547c7fa76694f3d7699a9f688dda76f24; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — FSJC endpoint exclusion by circular force-hull feedback

**Date:** 2026-09-10  
**Repository state:** `main` at `1ea7a3c5970d614c9f860841eea5ad3718ca171f` at start  
**Run type:** closing-proof continuation / equality-case audit  
**Target:** Target C, C-II after ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md` resolved against the promoted C-I restoration  
**External web search:** not used in the proof  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The current FSJC report proves the post-ZF lower endpoint

\[
\lambda_*:=0.5882283437736394\ldots,
\qquad
\lambda_* >0,
\]

defined exactly by

\[
\boxed{
(\pi^2+1)\lambda_*^2+\pi\lambda_*
-\frac{\pi^2}{4}-\pi=0,
}
\tag{E.1}
\]

for the normalized pinned/contact currency

\[
\lambda_D:=\frac{e_{BB}+2s_C}{D}.
\]

It also proves that any sequence with `lambda_D -> lambda_*` must have

\[
\frac hD\to\frac\pi2.
\]

This report proves that such an endpoint sequence cannot exist. The key point is that
saturation of the joint cavity inequality forces the force-hull perimeter to approach
its absolute diameter maximum `pi D`. FS.4 simultaneously makes that same force hull
asymptotically centrally symmetric about the full-source circumcenter. Every
Hausdorff limit is therefore the radius-`1/2` disk. Its true normalized area is
`pi/4`, larger than the FSDB lower bound used to create the FSJC endpoint by the exact
amount

\[
\boxed{
\frac\pi4-\frac{\pi/2+1}{4}
=\frac{\pi-2}{8}>0.
}
\tag{E.2}
\]

Feeding this recovered disk area back into the same GU/JC inequalities gives an exact
contradiction.

Consequently the FSJC bound is not asymptotically sharp:

### Main conclusion

There exist constants `epsilon_0>0` and `D_0<infinity` such that every sufficiently
large post-ZF C-II survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge\lambda_*+\epsilon_0
\qquad(D\ge D_0).
}
\tag{E.3}
\]

The proof is compactness-based and does not give a numerical value of `epsilon_0`.
This is not another finite decimal iteration: it excludes the entire FSJC near-equality
normal form and proves a genuine open neighborhood above the former endpoint is empty.

---

## 1. Inputs and notation

Work on one unbounded sequence of lexicographically normalized triangle-free global
sources satisfying the audited post-ZF stack. All quantities below belong to the same
source representative.

Let

\[
L:=e_{BB}+2s_C,
\qquad
\lambda:=\frac LD,
\qquad
t:=\frac{e_{BB}}D,
\qquad
y:=\frac hD.
\tag{1.1}
\]

For the exact contact/face ledgers write

\[
d_H:=q-h,
\qquad
s_Z:=e+h-(2v-2),
\qquad
Q:=\sum_{f\text{ bounded}}(\deg f-4),
\tag{1.2}
\]

\[
z:=Q+2s_Z,
\qquad
r_H:=2h-q=x_B+z,
\qquad
x_B:=b-q.
\tag{1.3}
\]

Let `F` be the full force hull of the relative-interior normalized KKT stress, and let

\[
E:=E_{out}=\sum_P(L_P-3)
\tag{1.4}
\]

be the total OP outer-pocket perimeter excess. Let

\[
G:=\operatorname{area}(F)-\sum_r\operatorname{area}(P_r)
\tag{1.5}
\]

be the GU attachment-cell area gap.

The proof uses the following already established report-level inputs.

1. **FS.4.** If `o` is the full-source circumcenter and
   \[
   L_D=\sqrt{D\eta+\eta^2},\qquad \eta=3^{1/4}\sqrt D,
   \]
   then for the relative-interior full-support stress
   \[
   d_H(F-o,-(F-o))\le2L_D=o(D).
   \tag{1.6}
   \]
   The use of the relative-interior stress is essential: its positive diameter support
   is the full actual `H=H_*`, so this `F` is the same force hull used by DB, JC, and
   FSDB.
2. **FSDB.** Along a subsequence with `h/D->y`,
   \[
   \liminf\frac{\operatorname{area}F}{D^2}
   \ge\Phi(y):=\frac{y+\sin y}{4}.
   \tag{1.7}
   \]
3. **GU/ZK component-area bound.** Put
   \[
   k=d_H+s_Z,
   \qquad
   L_2=6-3k+e_{BB}+2s_C.
   \tag{1.8}
   \]
   Then
   \[
   \sum_r\operatorname{area}(P_r)
   \le\frac\pi4L_2^2+\pi L_2+\pi^2D.
   \tag{1.9}
   \]
4. **JC exact perimeter/cavity ledger.** One has
   \[
   E=x_B+P_F-q-a,
   \qquad P_F:=\operatorname{per}F,
   \tag{1.10}
   \]
   and the exact inequalities
   \[
   \boxed{
   E+Q
   \le e_{BB}+h-3d_H-Q-4s_Z,
   }
   \tag{1.11}
   \]
   \[
   \boxed{
   E+Q
   \le e_{BB}+P_F-h-3d_H-2s_Z.
   }
   \tag{1.12}
   \]
   Moreover
   \[
   G\le H_{out}+A_{exc}+2q,
   \tag{1.13}
   \]
   and
   \[
   H_{out}+A_{exc}
   \le\frac{(E+Q)^2}{4\pi}+o(D^2).
   \tag{1.14}
   \]
5. **Convex perimeter ceiling.** Since `diam(F)=D`,
   \[
   P_F\le\pi D.
   \tag{1.15}
   \]
6. **FSJC.** Every unbounded post-ZF sequence has
   \[
   \liminf\lambda\ge\lambda_*.
   \tag{1.16}
   \]
   If `lambda->lambda_*`, then
   \[
   y\to\pi/2.
   \tag{1.17}
   \]

For audit, (1.11) and (1.12) rederive directly from JC.5. With
`r_H=2h-q`, `d_H=q-h`, and `z=Q+2s_Z`, JC.5 gives

\[
E+Q\le x_B+P_F-2q+e_{BB}+Q.
\]

Using `P_F<=q+x_B` gives (1.11), while substituting the exact identities without
that perimeter replacement gives (1.12). Thus the nonnegative defect terms used below
are not artifacts of a later asymptotic relaxation.

---

## 2. Any endpoint sequence makes the direct-contact part saturate

Assume for contradiction that an unbounded post-ZF sequence satisfies

\[
\lambda\to\lambda_*.
\tag{2.1}
\]

By FSJC,

\[
y\to\pi/2.
\tag{2.2}
\]

Pass to an arbitrary further subsequence on which

\[
t=\frac{e_{BB}}D\to t_0.
\tag{2.3}
\]

Since `L=e_BB+2s_C` and `s_C>=0`,

\[
0\le t_0\le\lambda_*.
\tag{2.4}
\]

FSDB plus (1.9), with only `L_2<=L+6`, gives the same lower gap estimate used in
FSJC:

\[
\liminf\frac GD^2
\ge
\Phi(\pi/2)-\frac\pi4\lambda_*^2.
\tag{2.5}
\]

The diameter-sensitive JC upper bound gives

\[
\limsup\frac GD^2
\le
\frac{(t_0+\pi/2)^2}{4\pi}.
\tag{2.6}
\]

By the defining equation (E.1),

\[
\boxed{
\Phi(\pi/2)-\frac\pi4\lambda_*^2
=
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
}
\tag{2.7}
\]

The right side of (2.6) is strictly increasing in `t_0>=0`. Equations
(2.4)--(2.7) are therefore compatible only when

\[
\boxed{t_0=\lambda_*.}
\tag{2.8}
\]

The chosen convergent subsequence was arbitrary, so in fact

\[
\boxed{
\frac{e_{BB}}D\to\lambda_*,
\qquad
\frac{s_C}{D}\to0.
}
\tag{2.9}
\]

Thus endpoint saturation cannot be hidden in the pinned-stress currency.

---

## 3. Every dropped JC defect is sublinear

Put

\[
C_*:=\frac{(\lambda_*+\pi/2)^2}{4\pi}.
\tag{3.1}
\]

Equations (2.5)--(2.7) give

\[
\liminf\frac GD^2\ge C_*.
\tag{3.2}
\]

From (1.13)--(1.14),

\[
\frac GD^2
\le
\frac1{4\pi}\left(\frac{E+Q}{D}\right)^2+o(1),
\tag{3.3}
\]

because `q=O(D)`. On the other hand JC gives the finite bound

\[
E+Q\le e_{BB}+\min\{h,\pi D-h\}.
\tag{3.4}
\]

By (2.2) and (2.9),

\[
\limsup\frac{E+Q}{D}
\le\lambda_*+\frac\pi2.
\tag{3.5}
\]

If the left side of (3.5) were smaller along any subsequence by a fixed amount,
(3.3) would contradict (3.2). Hence

\[
\boxed{
\frac{E+Q}{D}	o\lambda_*+\frac\pi2,
\qquad
\frac GD^2\to C_*.
}
\tag{3.6}
\]

Now apply the stronger exact inequality (1.11). Its first two terms satisfy

\[
\frac{e_{BB}+h}{D}\to\lambda_*+\frac\pi2.
\]

The left side has the same limit by (3.6), while

\[
3d_H+Q+4s_Z\ge0.
\]

Therefore

\[
\boxed{
\frac{d_H}{D}\to0,
\qquad
\frac QD\to0,
\qquad
\frac{s_Z}{D}\to0.
}
\tag{3.7}
\]

This is the first structural strengthening beyond the FSJC report.

The exact identities (1.3) now give

\[
\boxed{
\frac qD\to\frac\pi2,
\qquad
\frac{r_H}{D}\to\frac\pi2,
\qquad
\frac{x_B}{D}\to\frac\pi2,
\qquad
\frac bD\to\pi.
}
\tag{3.8}
\]

Indeed `q=h+d_H`, `r_H=h-d_H`, `z=Q+2s_Z=o(D)`, `x_B=r_H-z`, and
`b=q+x_B`.

---

## 4. The force-hull perimeter itself must saturate

Use the second exact pre-relaxation inequality (1.12):

\[
E+Q
\le e_{BB}+P_F-h-3d_H-2s_Z.
\]

Divide by `D` and apply (2.2), (2.9), (3.6), and (3.7). The left side tends to

\[
\lambda_*+\frac\pi2,
\]

while all terms on the right except `P_F/D` tend to

\[
\lambda_* - \frac\pi2.
\]

Thus

\[
\liminf\frac{P_F}{D}\ge\pi.
\tag{4.1}
\]

The universal convex perimeter ceiling (1.15) gives the reverse inequality, so

\[
\boxed{
\frac{P_F}{D}\to\pi.
}
\tag{4.2}
\]

For completeness, the exact OP identity (1.10) then also yields

\[
\boxed{
\frac aD\to\frac\pi2-\lambda_*.
}
\tag{4.3}
\]

Indeed `Q=o(D)` makes `E/D->lambda_*+pi/2`, while (3.8) and (4.2) give

\[
\frac ED
=
\frac{x_B+P_F-q-a}{D}
\to\pi-\frac aD.
\]

Hence the PC inequality `a+e_BB>=q` is itself asymptotically tight. Also
`Q=o(D)` implies the exceptional-face count and excess `f+g_F=o(D)`.

The endpoint normal form is therefore much stronger than `h/D->pi/2`: all of

\[
s_C,\ d_H,\ Q,\ s_Z,\ f+g_F,\ b-P_F,\ a+e_{BB}-q
\]

are `o(D)`, while

\[
h,q,r_H,x_B\sim\frac\pi2D,
\qquad
b,P_F\sim\pi D.
\tag{4.4}
\]

---

## 5. FS.4 plus perimeter saturation forces a circular force hull

Translate and scale the force hull by the full-source circumcenter:

\[
K_D:=\frac{F-o}{D}.
\tag{5.1}
\]

FS.1 contains every selected force hull in the disk of radius

\[
\frac12+o(1)
\]

centered at the origin after this translation and scaling, so the `K_D` lie in one
fixed compact disk. They are nonempty compact convex bodies. Pass to a
Hausdorff-convergent subsequence

\[
K_D\to K_\infty.
\tag{5.2}
\]

The following standard planar convex-body facts can also be read directly from support
functions and Cauchy's perimeter formula:

- diameter is continuous under Hausdorff convergence;
- support functions, hence widths, converge uniformly;
- perimeter
  \[
  P(K)=\int_0^\pi w_K(\theta)\,d\theta
  \]
  is continuous under Hausdorff convergence;
- area is continuous for convex bodies under Hausdorff convergence.

Since `diam(F)=D`,

\[
\operatorname{diam}K_\infty=1.
\tag{5.3}
\]

FS.4 and (1.6) give

\[
d_H(K_D,-K_D)\to0,
\]

so

\[
\boxed{K_\infty=-K_\infty.}
\tag{5.4}
\]

Equation (4.2) gives

\[
\operatorname{per}K_\infty=\pi.
\tag{5.5}
\]

For every direction `theta`, the width satisfies

\[
w_{K_\infty}(\theta)\le\operatorname{diam}K_\infty=1.
\tag{5.6}
\]

Together with Cauchy's formula and (5.5),

\[
\int_0^\pi w_{K_\infty}(\theta)\,d\theta=\pi.
\]

The width function is continuous and bounded above by one, so equality of the
integral forces

\[
\boxed{w_{K_\infty}(\theta)=1\quad\text{for every }\theta.}
\tag{5.7}
\]

Thus `K_infty` has constant width one. By (5.4) it is centrally symmetric about the
origin. If `h_K` denotes the support function, central symmetry gives

\[
h_K(-u)=h_K(u),
\]

whereas constant width gives

\[
h_K(u)+h_K(-u)=1.
\]

Therefore

\[
h_K(u)=\frac12
\qquad\text{for every unit }u.
\]

A compact convex body is determined by its support function, so

\[
\boxed{
K_\infty=B(0,1/2).
}
\tag{5.8}
\]

Every Hausdorff-convergent subsequence has the same conclusion. In particular area
continuity implies

\[
\boxed{
\frac{\operatorname{area}F}{D^2}\to\frac\pi4.
}
\tag{5.9}
\]

No equality characterization is imported here: (5.6)--(5.8) prove it directly from
Cauchy's width formula and FS central symmetry.

---

## 6. Circular area fed back into GU contradicts the endpoint

The endpoint defects in (3.7) and (2.9) sharpen the component-area parameter (1.8):

\[
\frac{L_2}{D}
=
\frac{6-3(d_H+s_Z)+e_{BB}+2s_C}{D}
\to\lambda_*.
\tag{6.1}
\]

Divide (1.9) by `D^2`. Together with the true force-hull area (5.9), this gives

\[
\boxed{
\liminf\frac GD^2
\ge
\frac\pi4-\frac\pi4\lambda_*^2.
}
\tag{6.2}
\]

But (3.3) and (3.6) give the opposite upper bound

\[
\boxed{
\limsup\frac GD^2
\le
\frac{(\lambda_*+\pi/2)^2}{4\pi}.
}
\tag{6.3}
\]

By (2.7), the right side of (6.3) is

\[
\Phi(\pi/2)-\frac\pi4\lambda_*^2.
\]

Subtracting this from the lower bound in (6.2) leaves the exact positive gap

\[
\frac\pi4-\Phi(\pi/2)
=
\frac\pi4-\frac{\pi/2+1}{4}
=
\boxed{\frac{\pi-2}{8}>0.}
\tag{6.4}
\]

Equations (6.2)--(6.4) are impossible. Hence no unbounded endpoint sequence (2.1)
exists.

This is the decisive new step. It uses the geometry forced by equality in the old
inequalities and then re-enters those inequalities with a strictly stronger area
value. The argument is not a numerical strengthening of FSJC.

---

## 7. Uniform open gap above the FSJC endpoint

Suppose no constants `epsilon_0>0,D_0<infinity` satisfying (E.3) existed. Then for
every integer `j>=1` one could choose a post-ZF survivor with

\[
D_j\ge j,
\qquad
\lambda_{D_j}<\lambda_*+\frac1j.
\tag{7.1}
\]

FSJC gives

\[
\liminf_j\lambda_{D_j}\ge\lambda_*.
\]

Equation (7.1) gives the reverse limsup, so

\[
\lambda_{D_j}\to\lambda_*.
\]

This is exactly the endpoint sequence excluded in Sections 2--6. Contradiction.
Therefore some `epsilon_0>0,D_0<infinity` exist, proving (E.3).

The constants are uniform over all post-ZF survivors because the contradiction starts
from an arbitrary sequence of such survivors rather than from a chosen geometric
subclass.

---

## 8. Relation to the now-closed perfect-matching branch

The main branch now contains MFS, which independently excludes every sufficiently large
post-ZF source whose full diameter graph is a perfect matching. The present theorem is
different:

- it does not assume a matching;
- at the forbidden FSJC endpoint one has `d_H=o(D)`, not `d_H=q/2`;
- the endpoint diameter graph is highly branching:
  \[
  r_H=2h-q\sim\frac\pi2D;
  \]
- the contradiction comes from joint perimeter/cavity equality plus FS central
  symmetry, not from the pure-rhombic Mantel area ceiling.

Thus the two September 10 exclusions remove disjoint limiting regimes.

---

## 9. Regression and scope audit

### Regular odd shell

A regular odd shell has force hull approaching the radius-`D/2` disk, so the circular
limit in Section 5 is not itself contradictory. What it does not satisfy is the FSJC
near-endpoint currency: its loaded-loaded contact currency is of order `pi D`, far
above `lambda_* D`. The theorem therefore does not falsely exclude the shell by its
force geometry alone.

### Dense isolated fillings

No step removes or bounds contact-isolated source points. FS.4 gets its common center
from the full source, while all ZF/JC quantities are taken only on the nonisolated core
exactly as defined. Dense isolated fillings therefore remain valid regressions against
any attempted core-population identification.

### Small response trace / conductance

No lower bound on an individual response conductance or diameter KKT weight is used.
The proof never turns coordinate-field radialization into an operator estimate.

### Representative changes

No RA, hull-saturated, or contact-richer representative is substituted. Every force,
contact, diameter, pocket, and FS quantity belongs to the same contact-minimal then
diameter-pair-minimal source. The relative-interior KKT stress is selected inside that
fixed source only to make its positive support equal the full actual support.

### Exact use of global optimality

The odd-shell examples can imitate the limiting disk and much of the force geometry.
The proof uses global-source information where those regressions lack it:

1. FS.1/FS.4 derive the common near-minimal circumcenter from the strict translated-
   lattice comparison for a global minimizer;
2. ZF/JC use the lexicographic global-minimizer normal form and C63 finite integration;
3. the contradiction feeds the resulting geometry into the same global post-ZF
   attachment/cavity ledger.

Thus the decisive step is not a statement true of arbitrary near-circular packings.

---

## 10. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| endpoint forces `e_BB/D->lambda_*`, `s_C=o(D)` | proved under FSDB/JC | equality in the monotone `t<=lambda` relaxation |
| `d_H,Q,s_Z=o(D)` | proved under exact JC | saturation of pre-drop inequality (1.11) |
| `q,r_H,x_B->(pi/2)D`, `b->pi D` | proved | exact ZT/ZE identities |
| `P_F/D->pi` | proved | pre-drop inequality (1.12) plus Cauchy ceiling |
| force hull converges after scaling to radius-`1/2` disk | proved under FS.4 | Hausdorff compactness + Cauchy width formula + central symmetry |
| endpoint contradiction with exact gap `(pi-2)/8` | proved | true disk area in GU versus saturated JC capacity |
| uniform `epsilon_0>0` above FSJC endpoint | proved | sequential compactness/contradiction |
| explicit numerical `epsilon_0` | not proved | would require quantitative stability of the equality chain |
| Level I | still open | high-surplus sources outside the excluded neighborhood remain |

Because several post-ZF inputs remain report-level rather than promoted canonical
modules, this theorem should remain a report until those dependencies and this equality
audit receive independent review.

---

## 11. Exact remaining obligation

The old near-FSJC endpoint is gone. A surviving post-ZF source now has all of the
following:

1. the perfect-matching diameter branch is excluded by MFS;
2. its force hull obeys the FSDB functional area floor;
3. its pinned/contact currency is separated by a uniform positive gap from
   `lambda_*D`;
4. FS.4 gives `o(D)` half-turn asymmetry and the full-source common center;
5. the full whole-source capacity contradiction
   \[
   n-1\le\frac\pi{2\sqrt3}D^2
   \]
   is still not proved.

A next closing theorem must control the genuinely higher-surplus regime. The natural
quantity to retain is the unrelaxed three-variable system `(lambda,t,y)` together with
the pre-drop defects in (1.11)--(1.12), rather than iterating a single scalar lower
bound. A quantitative stability version of Section 5 could make the open gap explicit,
but an explicit constant is not itself a Level I endpoint unless it crosses a proved
upper bound.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

New theorem: the FSJC endpoint lambda_* is not attainable even asymptotically.
Assume lambda=(e_BB+2s_C)/D -> lambda_*.
FSJC gives h/D->pi/2. Equality in its t<=lambda relaxation forces
    e_BB/D->lambda_*, s_C=o(D).
Saturation of the exact pre-drop JC inequalities then forces
    d_H,Q,s_Z=o(D),
    q/D,r_H/D,x_B/D->pi/2,
    b/D->pi,
    per(F)/D->pi.
FS.4 gives d_Haus((F-o)/D,-(F-o)/D)->0.
Any Hausdorff limit has diameter 1, perimeter pi, and central symmetry.
Cauchy's width formula forces constant width 1; central symmetry then forces the
radius-1/2 disk. Hence area(F)/D^2->pi/4.

GU now gives
    liminf G/D^2 >= pi/4-(pi/4)lambda_*^2,
while saturated JC gives
    limsup G/D^2 <= (lambda_*+pi/2)^2/(4pi)
                 = Phi(pi/2)-(pi/4)lambda_*^2.
The exact gap is
    pi/4-Phi(pi/2)=(pi-2)/8>0,
a contradiction.
Therefore there exist epsilon_0>0,D_0 such that every sufficiently large post-ZF
survivor has
    (e_BB+2s_C)/D >= lambda_*+epsilon_0.
No explicit epsilon_0 is claimed.
```
