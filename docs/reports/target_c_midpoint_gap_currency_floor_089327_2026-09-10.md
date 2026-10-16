<!-- migration-source: path=docs/reports/target_c_midpoint_gap_currency_floor_089327_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=903a7fc2613c8f3d312ef312addf54e61bb7bae9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — midpoint gap currency raises the post-ZF floor to 0.893278

**Date:** 2026-09-10  
**Repository state:** `f977f2d0d25f5022c2a587e59cab38375d85caee` at start  
**Run type:** closing proof / exact geometric synthesis / endpoint exclusion  
**Target:** Target C, C-II after C-I restoration and ZF  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** none used in the proof  
**Computation:** decimal evaluation only; no floating-point sign is a proof dependency

## LEVEL I STATUS

`STILL OPEN`.

This report proves a new report-level post-ZF lower bound

\[
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge \lambda_{MG}
=0.8932783754208358\ldots,
}
\tag{MG.1}
\]

and excludes exact saturation. Hence there exist absolute constants
`epsilon_MG>0` and `D_0<infinity` such that every sufficiently large post-ZF C-II
survivor satisfies

\[
\boxed{
\frac{e_{BB}+2s_C}{D}\ge\lambda_{MG}+\epsilon_{MG}.
}
\tag{MG.2}
\]

The constant is the unique root in `(0,1)` of

\[
\boxed{
\pi-
\left(
2\arcsin\frac\lambda2
-\lambda\sqrt{1-\frac{\lambda^2}{4}}
\right)
=
\left(\pi+\frac2\pi\right)\lambda^2.
}
\tag{MG.3}
\]

The proof does not use the fixed-chord Dido optimization. It uses only the FS.4
midpoint/radial estimates, full actual diameter support of the lexicographic source,
the OP pocket decomposition, a reflected-pocket isoperimetric bound, the standard
exceptional-face bound, and the GU attachment-cell bound.

The decisive new bridge is that every macroscopic projective gap in the full diameter
direction set forces **two actual long missing force-hull sides**. Their chord lengths
consume outer-pocket degree currency. The same projective gaps are exactly what create
the deficit of the midpoint polygon from disk area. This couples the FSDB area deficit
to `d_P`, rather than treating diameter directions and pocket capacity independently.

Level I remains open because no proved universal upper bound crosses MG.2.

---

## 1. Exact implication to the closing currency

Write

\[
L=e_{BB}+2s_C,
\qquad
\lambda=\lim\frac LD
\]

along a convergent unbounded post-ZF subsequence. If `lambda>=1`, MG.1 is automatic,
so the only branch needing exclusion has `lambda<1`.

The proof establishes two source-specific estimates.

First, diameter-direction gaps and pocket degree imply

\[
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
\frac{\pi-\mathcal Q(\lambda)}4,
}
\tag{1.1}
\]

where

\[
\boxed{
\mathcal Q(x)
:=2\arcsin\frac x2-x\sqrt{1-\frac{x^2}{4}}
\qquad(0\le x<2).
}
\tag{1.2}
\]

Second, outer-pocket and attachment-cell capacity imply

\[
\boxed{
\limsup\frac{area(F)}{D^2}
\le
\left(\frac\pi4+\frac1{2\pi}\right)\lambda^2.
}
\tag{1.3}
\]

Their compatibility is exactly MG.3 at threshold. The left side of MG.3 is strictly
decreasing in `lambda`, while the right side is strictly increasing, so every
survivor limit must satisfy `lambda>=lambda_MG`.

---

## 2. Finite midpoint-polygon theorem

Let `o` and

\[
L_D=O(D^{3/4})=o(D)
\]

be the full-source circumcenter and midpoint error from FS.4. Let `H` be the full
actual diameter graph of the lexicographically selected C-II source. For every
`e=bk in E(H)`, choose an orientation

\[
p_b-p_k=D u_e,
\qquad |u_e|=1,
\]

and define

\[
P_H=D\,conv\{\pm u_e:e\in E(H)\},
\qquad
Q_H=\frac12P_H.
\tag{2.1}
\]

### Theorem MG.1 — two-sided midpoint polygon

\[
\boxed{
d_{Haus}(F-o,Q_H)\le L_D.
}
\tag{2.2}
\]

Every vertex of `F-o` also satisfies the uniform radial estimate

\[
\boxed{
\left||p_b-o|-\frac D2\right|=O(\sqrt D)=o(D).
}
\tag{2.3}
\]

#### Proof

For a diameter edge `e=bk`, put `m_e=(p_b+p_k)/2`. Then

\[
p_b-o=\frac D2u_e+(m_e-o),
\qquad
p_k-o=-\frac D2u_e+(m_e-o).
\]

FS.4 gives `|m_e-o|<L_D`. Therefore every generator of `Q_H` lies within `L_D`
of a force-hull point, so

\[
Q_H\subseteq(F-o)+L_DB_2.
\]

For the reverse inclusion, the C-I lexicographic normalization gives `H=H_*`; C65
then identifies the selected relative-interior diameter support with the full actual
diameter graph. Thus every force-hull vertex is an endpoint of an actual positive
diameter edge. The same midpoint identity places that vertex within `L_D` of the
corresponding generator of `Q_H`. Taking convex hulls yields

\[
F-o\subseteq Q_H+L_DB_2.
\]

This proves (2.2). The radial estimate is the endpoint annulus in FS.4. `square`

Consequently Steiner's formula gives

\[
\boxed{
area(F)=area(Q_H)+o(D^2)
=\frac14 area(P_H)+o(D^2).
}
\tag{2.4}
\]

---

## 3. A macroscopic direction gap spends pocket degree

Order the `h=|E(H)|` projective diameter directions cyclically and let

\[
\gamma_1,\ldots,\gamma_h>0,
\qquad
\sum_i\gamma_i=\pi.
\tag{3.1}
\]

The vertices of `Q_H` lie on the radius-`D/2` circle. A projective gap `gamma_i`
therefore appears twice, at antipodal positions, as two sides of `Q_H`, each of
length

\[
D\sin(\gamma_i/2).
\tag{3.2}
\]

### Lemma MG.2 — uniform long-side transfer

Fix `epsilon>0`. For every gap `gamma_i>=epsilon`, the force hull has two distinct
missing sides whose lengths are

\[
D\sin(\gamma_i/2)+o_\epsilon(D).
\tag{3.3}
\]

The error is uniform over all such gaps.

#### Proof

There are at most `pi/epsilon` such projective gaps. Consider one corresponding side
of `Q_H`. Rotate so its endpoint directions are `+-gamma_i/2` and its outward normal
is horizontal. The supporting line of `Q_H` is

\[
x=(D/2)\cos(\gamma_i/2).
\]

By (2.2), the support of `F-o` in that normal differs by at most `L_D=o(D)`.
Every force-hull vertex has radius `D/2+o(D)` by (2.3). Hence no force-hull vertex can
lie a fixed angular distance inside the open sector between the two endpoint
directions: such a vertex would project farther than the allowed support by a fixed
multiple of `D`.

Hausdorff closeness supplies force-hull vertices in `o(1)` angular neighborhoods of
both endpoint directions. Since `F-o` contains the origin in its interior for large
`D` (the largest gap here is bounded away from `pi`, and `Q_H` has a centered inball
of radius `c_epsilon D` on the relevant sector), cyclic hull order is polar order.
Thus the last vertex in one endpoint cluster and the first vertex in the other are
consecutive force-hull vertices. Their radii are `D/2+o(D)` and their angular
separation is `gamma_i-o(1)`, giving (3.3).

The antipodal copy gives a second, distinct side. Since the number of gaps under
consideration is bounded in terms of `epsilon`, the errors are uniform after taking
the maximum over them. For large `D` these sides have length greater than one, so
none is a unit-contact side. `square`

Each missing force-hull side creates a distinct OP outer pocket. Let its old contact
chain have `ell_P` unit edges. The triangle inequality gives `ell_P>=s_P`, where
`s_P` is its hull-side chord, and OP uses pocket degree excess

\[
x_P=\ell_P-2,
\qquad
\sum_Px_P=d_P.
\tag{3.4}
\]

Therefore Lemma MG.2 gives, for every fixed `epsilon`,

\[
\boxed{
\frac{d_P}{D}
\ge
2\sum_{\gamma_i\ge\epsilon}\sin(\gamma_i/2)-o_\epsilon(1).
}
\tag{3.5}
\]

The `-2` contribution from each selected pocket is `O_epsilon(1)/D` and disappears.

Since PC gives

\[
e_{BB}=d_P+Q+2(d_H+s_Z)+c_B,
\tag{3.6}
\]

all terms on the right are nonnegative, and hence along the chosen subsequence

\[
\boxed{
\limsup
2\sum_{\gamma_i\ge\epsilon}\sin(\gamma_i/2)
\le\lambda.
}
\tag{3.7}
\]

---

## 4. Convert pocket currency into a force-hull area floor

For `0<=x<2`, define `mathcal Q` by (1.2). If

\[
x=2\sin(\gamma/2),
\]

then exactly

\[
\boxed{
\mathcal Q(x)=\gamma-\sin\gamma.
}
\tag{4.1}
\]

Also

\[
\mathcal Q'(x)=\frac{x^2}{\sqrt{4-x^2}}>0,
\qquad
\mathcal Q''(x)=
\frac{x(8-x^2)}{(4-x^2)^{3/2}}>0.
\tag{4.2}
\]

Thus `mathcal Q` is strictly increasing and strictly convex on `(0,2)`, with
`mathcal Q(0)=0`. In particular it is superadditive whenever the sum stays below 2:

\[
\mathcal Q(x)+\mathcal Q(y)\le\mathcal Q(x+y),
\qquad x,y\ge0,\ x+y<2.
\tag{4.3}
\]

Indeed

\[
\mathcal Q(x+y)-\mathcal Q(x)-\mathcal Q(y)
=\int_0^y[\mathcal Q'(x+t)-\mathcal Q'(t)]dt\ge0.
\]

The midpoint polygon has the exact area formula

\[
\frac{area(P_H)}{D^2}=\sum_i\sin\gamma_i.
\tag{4.4}
\]

Hence by (2.4),

\[
\frac{4area(F)}{D^2}
=
\pi-\sum_i(\gamma_i-\sin\gamma_i)+o(1).
\tag{4.5}
\]

Fix `epsilon>0`. For the small gaps,

\[
0\le\gamma-\sin\gamma\le\frac{\gamma^3}{6}
\le\frac{\epsilon^2}{6}\gamma,
\]

so

\[
\sum_{\gamma_i<\epsilon}(\gamma_i-\sin\gamma_i)
\le\frac{\pi\epsilon^2}{6}.
\tag{4.6}
\]

For the large gaps put `x_i=2sin(gamma_i/2)`. Because we are excluding a branch with
`lambda<1`, (3.7) makes `sum x_i<2` for large `D`. By superadditivity,

\[
\sum_{\gamma_i\ge\epsilon}(\gamma_i-\sin\gamma_i)
=
\sum\mathcal Q(x_i)
\le
\mathcal Q\left(\sum x_i\right)
\le
\mathcal Q(\lambda+o(1)).
\tag{4.7}
\]

Take first `D->infinity` and then `epsilon->0` in (4.5)-(4.7). This proves

\[
\boxed{
\liminf\frac{area(F)}{D^2}
\ge
\frac{\pi-\mathcal Q(\lambda)}4.
}
\tag{4.8}
\]

This is the new response-to-pocket-capacity theorem. Near-disk midpoint polygons have
small area deficit because generating such a deficit would require macroscopic
projective gaps, and each such gap spends actual OP pocket degree through two long
missing sides.

---

## 5. Independent upper capacity from reflected pockets

Let an OP outer pocket have missing hull chord `AB` and old contact chain of `ell`
unit edges. OP proves the pocket is a simple convex polygon.

Reflect the pocket across line `AB`. The two copies form a rectifiable Jordan domain
of area `2 area(P)` and boundary length `2ell`; the common chord is internal. The
planar isoperimetric inequality gives

\[
2area(P)\le\frac{(2\ell)^2}{4\pi},
\]

so

\[
\boxed{area(P)\le\frac{\ell^2}{2\pi}.}
\tag{5.1}
\]

Using `ell=x_P+2`,

\[
\begin{aligned}
H_{out}
&\le\frac1{2\pi}\sum_P(x_P+2)^2\\
&=\frac1{2\pi}
\left(\sum_Px_P^2+4d_P+4a\right)\\
&\le\frac1{2\pi}
\left(d_P^2+4d_P+4a\right).
\end{aligned}
\tag{5.2}
\]

The OP/PC identities give `a<=q<=per(F)<=pi D`, while `d_P<=e_BB<=L=O(D)` on a
subsequence with finite `lambda`. Thus, if

\[
\tau=\lim d_P/D,
\qquad
\nu=\lim Q/D,
\]

then

\[
\limsup\frac{H_{out}}{D^2}\le\frac{\tau^2}{2\pi}.
\tag{5.3}
\]

The standard exceptional-face estimate gives

\[
\limsup\frac{A_{exc}}{D^2}\le\frac{\nu^2}{4\pi}.
\tag{5.4}
\]

From (3.6), `tau+nu<=lambda`. Therefore

\[
\frac{\tau^2}{2\pi}+\frac{\nu^2}{4\pi}
\le\frac{\lambda^2}{2\pi}.
\tag{5.5}
\]

Indeed, `tau<=lambda-nu` and

\[
2(\lambda-\nu)^2+\nu^2\le2\lambda^2
\qquad(0\le\nu\le\lambda).
\]

Thus the complete outer/exceptional cavity obeys

\[
\boxed{
\limsup\frac G{D^2}\le\frac{\lambda^2}{2\pi}.
}
\tag{5.6}
\]

GU/ZK bounds total attachment-cell area by

\[
\limsup\frac{C_{att}}{D^2}\le\frac\pi4\lambda^2.
\tag{5.7}
\]

Since `area(F)=C_att+G`, (5.6)-(5.7) prove

\[
\boxed{
\limsup\frac{area(F)}{D^2}
\le
\left(\frac\pi4+\frac1{2\pi}\right)\lambda^2.
}
\tag{5.8}
\]

---

## 6. Exact scalar optimization

Define

\[
R(\lambda)
:=
\frac{\pi-\mathcal Q(\lambda)}4
-
\left(\frac\pi4+\frac1{2\pi}\right)\lambda^2
\qquad(0\le\lambda\le1).
\tag{6.1}
\]

By (4.2),

\[
R'(\lambda)
=-\frac14\mathcal Q'(\lambda)
-2\left(\frac\pi4+\frac1{2\pi}\right)\lambda<0
\]

for `lambda>0`. Also `R(0)=pi/4>0`, while

\[
R(1)
=\frac14\left(\frac{2\pi}{3}+\frac{\sqrt3}{2}\right)
-\left(\frac\pi4+\frac1{2\pi}\right)<0.
\]

For the sign at one, after multiplying by four it is enough that

\[
\frac{2\pi}{3}+\frac{\sqrt3}{2}
<\pi+\frac2\pi,
\]

and the difference of right minus left is
`pi/3+2/pi-sqrt(3)/2>0`, already from `pi>3` and `sqrt(3)/2<1`.

Hence there is a unique `lambda_MG in (0,1)` with `R(lambda_MG)=0`; this is exactly
MG.3. Equations (4.8) and (5.8) make every survivor limit with `lambda<1` satisfy
`R(lambda)<=0`, so

\[
\boxed{\lambda\ge\lambda_{MG}.}
\tag{6.2}
\]

A high-precision evaluation gives

\[
\boxed{\lambda_{MG}=0.8932783754208358088\ldots .}
\tag{6.3}
\]

The decimal is not used in the proof.

---

## 7. The explicit endpoint cannot occur

Assume for contradiction that a post-ZF survivor sequence has

\[
L/D\to\lambda_{MG}.
\tag{7.1}
\]

Then (4.8), (5.8), and `R(lambda_MG)=0` force

\[
\frac{area(F)}{D^2}
\to
\frac{\pi-\mathcal Q(\lambda_{MG})}{4}
=
\left(\frac\pi4+\frac1{2\pi}\right)\lambda_{MG}^2.
\tag{7.2}
\]

The area-deficit proof in Section 4 can be sharp only if the total normalized chord
currency carried by macroscopic projective gaps tends to `lambda_MG`. Otherwise,
strict monotonicity of `mathcal Q` leaves a fixed positive improvement in (4.8).
By (3.5) and `d_P<=e_BB<=L`, this forces

\[
\boxed{
\frac{d_P}{D}\to\lambda_{MG}.
}
\tag{7.3}
\]

Then PC (3.6) gives

\[
\boxed{
Q/D,\ (d_H+s_Z)/D,\ c_B/D,\ s_C/D\to0.
}
\tag{7.4}
\]

Strict superadditivity of `mathcal Q` also forces the area-deficit currency to
concentrate into one macroscopic projective gap: if two gap-chord currencies stayed
bounded below, (4.3) would have a fixed strict gap. Thus for one projective gap
`gamma_*`,

\[
2\sin(\gamma_*/2)\to\lambda_{MG},
\tag{7.5}
\]

while all other macroscopic gap-chord currency vanishes.

That single projective gap appears twice antipodally. Lemma MG.2 therefore gives two
distinct missing force-hull sides with chord lengths

\[
\left(\frac{\lambda_{MG}}2+o(1)\right)D
\]

each. Let their pocket chains have lengths `ell_1,ell_2`. Since
`ell_j>=s_j`,

\[
\frac{(\ell_1-2)+(\ell_2-2)}D
\ge\lambda_{MG}-o(1).
\]

Together with (7.3), the two selected pockets consume asymptotically all of `d_P`.
Their total chain-chord detour is therefore `o(D)`, and all remaining pockets have
total degree excess `o(D)`.

For the two selected pockets, the elementary discrete Dirichlet estimate

\[
area(P)^2
\le\frac{\ell^3}{6}(\ell-s)
\tag{7.6}
\]

follows exactly as in the standard piecewise-linear Green-function proof: vertical
edge energy is at most `2(ell-s)` and the discrete Green energy is at most `ell^3/12`.
Since `ell=O(D)` and the two detours sum to `o(D)`, their total area is `o(D^2)`.
For every remaining pocket, (5.1) and

\[
\sum x_P=o(D),
\qquad a=O(D),
\]

give total area `o(D^2)` by the expansion in (5.2). Therefore

\[
\boxed{H_{out}=o(D^2).}
\tag{7.7}
\]

Equation (7.4) and the exceptional-face estimate give `A_exc=o(D^2)`, hence

\[
\boxed{G=o(D^2).}
\tag{7.8}
\]

But then GU gives

\[
\limsup\frac{area(F)}{D^2}
\le\frac\pi4\lambda_{MG}^2,
\]

which contradicts (7.2) because `lambda_MG^2/(2pi)>0`. Thus no endpoint sequence
exists.

### Corollary MG.3 — uniform strict gap

There exist absolute `epsilon_MG>0` and `D_0<infinity` such that every post-ZF C-II
survivor with `D>=D_0` satisfies MG.2.

#### Proof

If not, choose survivors with `D_j>=j` and

\[
L_j/D_j<\lambda_{MG}+1/j.
\]

MG.1 forces the ratios to converge to `lambda_MG`, contradicting Section 7. `square`

---

## 8. Regression and dependency audit

### Odd regular shell

The shell has only microscopic projective gaps. Then
`sum(gamma-sin gamma)=o(1)`, so Section 4 merely says its midpoint polygon is near a
disk. No false matching or response-trace conclusion is drawn. The shell still lacks
the full post-ZF global-source GU/PC package required for the contradiction.

### Dense isolated filling

No small-isolate assumption is made. Isolates enter FS.4 through the full-source
circumradius estimate and are otherwise untouched. The cavity/attachment comparison is
for the selected source with all isolates retained.

### Finite subdivision of a limiting flat

Hausdorff central symmetry alone would not force a finite long force-hull side.
Lemma MG.2 uses the stronger midpoint-polygon identification plus the FS radial annulus;
a vertex a fixed angular distance inside a macroscopic midpoint-polygon gap would
violate the support estimate by `Theta(D)`. Thus an actual long hull side survives.

### Full actual diameter support

The reverse inclusion in MG.1 is not generic strict complementarity. It uses the
lexicographic C-II fact `H=H_*` and C65, which identifies every actual diameter edge
with the selected relative-interior support. The C-I restoration explicitly permits
this normalization for the representative whose exclusion suffices for an arbitrary
counterexample.

### Where global optimality enters

The midpoint identities alone are geometric. The source-specific ingredient absent
from shell regressions is FS.4: its common near-diameter circumdisk comes from the
**entire globally minimizing source** via Oler plus the strict translated-lattice
comparison. The post-ZF PC/GU package then converts that force geometry into the
selected source's exact pocket and attachment currencies.

---

## 9. Failed mechanisms recorded

1. The exact whole-source allowance reversal remains exactly
   `D^2 >= (2sqrt(3)/pi)(n-1)` and is not supplied by FS alone.
2. Pure post-ZF face bookkeeping still asks for `s_Z<0` and cannot close itself.
3. Near-central symmetry without midpoint-generator identification does not preserve
   finite hull subdivision; MG.2 needs the radial annulus.
4. The reflection pocket bound by itself gives only a cavity upper bound. The new
   improvement comes from coupling the **same** macroscopic diameter gaps to `d_P`.
5. No response trace, conductance floor, almost-full-weight matching, or arbitrary
   boundary-data operator bound is used.

---

## 10. Remaining Level I implication

MG.2 is still a lower restriction on

\[
L/D=(e_{BB}+2s_C)/D.
\]

A Level I closure now follows from any uniform post-ZF upper bound below the strict
MG threshold, or from a direct strict sub-`D` competitor in the high-currency branch.
The nearest quantitative continuation is stronger than the scalar MG.1 relaxation:
retain the actual macroscopic chord currency `T` instead of replacing it by `lambda`.
The large-pocket detour available for quadratic area is at most the remaining chain
currency `lambda-T`. Combining this with the fixed-chord Dido envelope yields a
strictly stronger two-variable necessary inequality and numerically moves the relaxed
threshold above `0.90`. That refinement is not claimed proved in this report.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

The finite midpoint-polygon theorem and Lemma MG.2 are strong promotion candidates.
MG.1/MG.2 depend on the existing unpromoted FS/PC/GU chain and should be promoted only
after independent review of the long-side transfer and endpoint concentration step.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let L=e_BB+2s_C and lambda=L/D along a post-ZF survivor subsequence.
FS.4 + H=H_* give the finite midpoint-polygon theorem
    d_Haus(F-o, (D/2)conv{+-u_e}) <= L_D=o(D),
with every force-hull vertex at radius D/2+o(D).

For each fixed epsilon, every projective diameter gap gamma>=epsilon transfers to two
actual missing F sides of length
    D sin(gamma/2)+o(D).
Their two OP chains imply
    d_P/D >= 2 sum_{gamma>=epsilon} sin(gamma/2)-o(1).
Since d_P<=L, macroscopic gap chord currency is at most lambda.

Define
    Q(x)=2asin(x/2)-x sqrt(1-x^2/4).
Then Q(2sin(gamma/2))=gamma-sin gamma, Q is increasing/strictly convex, and
superadditivity plus the microscopic-gap error gives
    area(F)/D^2 >= [pi-Q(lambda)]/4-o(1).

Reflecting each convex OP pocket across its missing hull chord gives
    area(P)<=ell(P)^2/(2pi).
Summing with ell=x+2, plus exceptional faces and PC tau+nu<=lambda, gives
    G/D^2 <= lambda^2/(2pi)+o(1).
GU attachment cells give
    C_att/D^2 <= pi lambda^2/4+o(1).
Thus
    [pi-Q(lambda)]/4 <= (pi/4+1/(2pi))lambda^2.
The unique root is
    lambda_MG=0.8932783754208358....

Endpoint equality is impossible: it forces one macroscopic projective gap whose two
opposite long pocket chords consume all d_P currency, hence H_out=o(D^2) and Q=o(D),
so G=o(D^2). But scalar equality would require the positive extra cavity allowance
lambda_MG^2/(2pi). Contradiction.
Therefore some absolute epsilon_MG>0 exists above the explicit 0.893278... floor.

Level I remains open: no crossing high-surplus upper bound is yet proved.
```
