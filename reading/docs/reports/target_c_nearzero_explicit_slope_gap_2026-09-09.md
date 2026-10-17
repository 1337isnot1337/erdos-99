> Generated reading edition · [exact source](../../../docs/reports/target_c_nearzero_explicit_slope_gap_2026-09-09.md) · source SHA-256 `a99fb8d915877e5b2e66bed15c4a84a84a3c16187eef64a381c2eef1be1ee827`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D8788A48874A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — QSG: an explicit gap above RCC slope one in the near-zero response phase

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-nearzero-physical-carrier`  
**Run type:** quantitative off-slope SCC/SAC stability + OD/Hemmi branch exclusion  
**Target:** Target C C-II, C66 phase `D epsilon -> 0`  
**Depends on:** RCC, NLC, ZK, SCC/SAC/SOD/SHX, PI, JC, OD, HKS/HKI  
**New external literature:** none beyond the already-audited Hemmi input  
**Computation:** fixed scalar evaluations with margins; no finite search is used as mathematical evidence

## LEVEL I STATUS

**STILL OPEN.**

RCC proves the asymptotic slope-one lower bound

$$
\liminf\frac{e_{BB}+2s_C}{D}\ge1
$$

when the response defect tends to zero. SHX proves that equality slope one cannot actually occur under the stronger near-zero condition `D epsilon -> 0`.

QSG makes that strictness explicit.

Put

$$
L:=e_{BB}+2s_C,
\qquad
\eta_0:=10^{-7}.
$$

### Theorem QSG — explicit near-zero slope gap

For every post-ZF sequence satisfying

$$
D\varepsilon\to0,
$$

one has

$$
\boxed{
\liminf_{D\to\infty}\frac{L}{D}
\ge1+10^{-7}.
}
\tag{QSG.1}
$$

In fact the proof excludes any subsequence on which

$$
\limsup L/D\le1+10^{-7}.
\tag{QSG.2}
$$

The constant is deliberately tiny. The point is qualitative-to-quantitative conversion: the slope-one endpoint is separated from all near-zero survivors by an explicit absolute amount.

---

## 1. Assume a near-slope-one countersequence

Suppose for contradiction that, after passage to a subsequence,

$$
D\varepsilon\to0,
\qquad
\frac LD\le1+\eta_0+o(1).
\tag{1.1}
$$

Since `1+eta_0<2`, NLC's integer branch-count inequality forces exactly one long harmonic response component `I_*` for all sufficiently large members of the sequence. It satisfies

$$
\boxed{\delta_*>D-3.}
\tag{QSG.3}
$$

Moreover NSE/UCM says asymptotically unit `z`-response mass goes to the actual diameter-partner set `P=N_H(z)`. Since the unique long component carries all but `o(1)` of the long `z`-response, there is an actual partner

$$
a\in P\cap A_*,
\qquad |z-a|=D.
\tag{1.2}
$$

Thus the SCC two-diameter-attachment augmentation is available off exact slope one as long as the long component is unique.

---

## 2. Quantitative ZK budget around the giant component

Put

$$
k:=d_H+s_Z.
$$

ZK gives the exact identity

$$
\sum_r\delta_r+R_I+s_B+3k=6+L.
\tag{2.1}
$$

Using QSG.3 and nonnegativity,

$$
D-3+3k<6+L,
$$

so

$$
\boxed{
\frac{k}{D}\le\frac{\eta_0}{3}+o(1).
}
\tag{QSG.4}
$$

Also

$$
\boxed{
\sum_{r\ne *}\delta_r
\le\eta_0D+o(D).
}
\tag{QSG.5}
$$

and

$$
\boxed{r_*\le\eta_0D+o(D),}
\tag{QSG.6}
$$

because `r_*<=R_I` and both `sum delta` and `R_I` occur with positive coefficient in (2.1).

A sharper combination is useful below:

$$
\boxed{
\delta_*+r_*
\le6+L.
}
\tag{QSG.7}
$$

---

## 3. Quantitative SCC: the giant component lies in a thin focal ellipse

As in SCC, adjoin the actual diameter attachments `z,a` to `C[I_*]`, retaining one actual contact edge from each attachment into the component. Call the resulting triangle-free penny graph `G'`.

Let `delta',r',b',Q'` be its graph diameter, Eppstein slack, outer boundary-walk length, and bounded-face defect.

SCC proves exactly

$$
b'+Q'=2\delta'+2r'
\tag{3.1}
$$

and

$$
r'=r_*+(\delta_*-\delta')+2.
$$

Therefore

$$
\delta'+r'=\delta_*+r_*+2.
$$

Using QSG.7,

$$
\boxed{
b'+Q'\le2L+16.}
\tag{QSG.8}
$$

Both `z,a` are outer-face vertices and split the outer boundary into two unit-edge walks of lengths `ell_1,ell_2`. Since `|z-a|=D`,

$$
\ell_i\ge D.
$$

From `ell_1+ell_2=b'` and QSG.8,

$$
\boxed{
0\le E_i:=\ell_i-D
\le2\eta_0D+o(D).
}
\tag{QSG.9}
$$

For every point `x` on either outer walk, the two subwalk lengths from `z` to `x` and from `x` to `a` sum to at most

$$
D+2\eta_0D+o(D).
$$

Hence every outer-face vertex lies in the common focal ellipse with foci `z,a` and major-axis length

$$
(1+2\eta_0)D+o(D).
$$

Every vertex of `G'` lies in the convex hull of its outer-face vertices, hence in that same ellipse.

The area of an ellipse with focal separation `D` and major-axis length `(1+2eta)D` is

$$
\frac\pi4(1+2\eta)
\sqrt{(1+2\eta)^2-1}\,D^2
=
\frac\pi2(1+2\eta)\sqrt{\eta(1+\eta)}\,D^2.
$$

Every attachment terminal in `A_*` lies within one unit of an internal vertex of `I_*`. Steiner enlargement by radius one changes normalized area only by `o(1)`. Therefore

$$
\boxed{
\limsup\frac{\operatorname{area}(\operatorname{conv}A_*)}{D^2}
\le
C_g(\eta_0),
}
\tag{QSG.10}
$$

where

$$
\boxed{
C_g(\eta)
:=
\frac\pi2(1+2\eta)\sqrt{\eta(1+\eta)}.
}
\tag{QSG.11}
$$

This improves the crude strip-rectangle stability constant by using the same focal-ellipse idea as OD.

---

## 4. All other attachment cells cost only `O(eta_0^2 D^2)`

For every harmonic component, C40 gives

$$
\operatorname{diam}(A_r)\le\delta_r+2.
$$

By isodiametry,

$$
\sum_{r\ne *}\operatorname{area}(\operatorname{conv}A_r)
\le
\frac\pi4\sum_{r\ne *}(\delta_r+2)^2.
\tag{4.1}
$$

Let

$$
T:=\sum_{r\ne *}\delta_r.
$$

QSG.5 gives `T<=eta_0D+o(D)`. Hence

$$
\sum_{r\ne *}\delta_r^2\le T^2
\le\eta_0^2D^2+o(D^2).
$$

The linear `4T` contribution is `o(D^2)`. The component-count term is also `o(D^2)`: ZU and `q=O(D)`, `L=O(D)` imply `c_I=O(D)`.

Therefore

$$
\boxed{
\limsup\frac1{D^2}
\sum_{r\ne *}\operatorname{area}(\operatorname{conv}A_r)
\le\frac\pi4\eta_0^2.
}
\tag{QSG.12}
$$

Combining QSG.10 and QSG.12, define

$$
\boxed{
C_A(\eta)
:=
\frac\pi2(1+2\eta)\sqrt{\eta(1+\eta)}
+\frac\pi4\eta^2.
}
\tag{QSG.13}
$$

Then

$$
\boxed{
\limsup
\frac{\sum_r\operatorname{area}(\operatorname{conv}A_r)}{D^2}
\le C_A(\eta_0).
}
\tag{QSG.14}
$$

At the chosen value

$$
\eta_0=10^{-7},
$$

one has conservatively

$$
\boxed{C_A(\eta_0)<0.000497.}
\tag{QSG.15}
$$

Thus the C49 attachment gap satisfies

$$
\boxed{
\liminf G/D^2
\ge
\liminf\operatorname{area}(F)/D^2-0.000497.
}
\tag{QSG.16}
$$

---

## 5. Scalar variables and actual-perimeter capacity

Pass to a further subsequence with

$$
y:=\lim h/D,
\qquad
p:=\lim P_F/D,
\qquad
P_F:=\operatorname{per}(F).
$$

QSG.4 gives

$$
d_H/D\le\eta_0/3+o(1).
$$

Since `q=h+d_H` and `q<=P_F`,

$$
p\ge y.
\tag{5.1}
$$

ZT gives

$$
P_F\le b=2h-Q-2s_Z\le2h,
$$

hence

$$
p\le2y.
\tag{5.2}
$$

Therefore

$$
\min\{y,p-y\}=p-y.
\tag{5.3}
$$

PI gives

$$
A_{PI}(y)
:=
\begin{cases}
\frac12\sin y,& y\le\pi/2,\\[3pt]
\frac12,& y\ge\pi/2,
\end{cases}
$$

and

$$
\operatorname{area}(F)/D^2\ge A_{PI}(y)-o(1).
\tag{5.4}
$$

The actual-perimeter JC capacity gives

$$
G/D^2
\le
\frac{(t+p-y)^2}{4\pi}+o(1),
\qquad
t:=\lim e_{BB}/D.
$$

Since `e_BB<=L`,

$$
t\le1+\eta_0.
$$

Thus every countersequence must satisfy

$$
\boxed{
A_{PI}(y)-C_A(\eta_0)
\le
\frac{(1+\eta_0+p-y)^2}{4\pi}.
}
\tag{QSG.17}
$$

The left side is positive throughout the relevant range. Hence

$$
\boxed{
p\ge p_\eta(y),}
\tag{QSG.18}
$$

where

$$
\boxed{
p_\eta(y)
:=y-(1+\eta_0)
+\sqrt{4\pi(A_{PI}(y)-C_A(\eta_0))}.}
\tag{QSG.19}
$$

---

## 6. Low diameter-density range: OD gives a uniform contradiction

DB gives universally

$$
y\ge2\rho,
\qquad
\rho=\cos\rho.
\tag{6.1}
$$

Consider first

$$
2\rho\le y\le1.5318.
\tag{6.2}
$$

If `p_eta(y)>2y`, QSG.18 contradicts `p<=2y` immediately. Otherwise define

$$
d_\eta(y):=2y-p_\eta(y)
=y+1+\eta_0
-\sqrt{4\pi(A_{PI}(y)-C_A(\eta_0))}.
\tag{6.3}
$$

Then ZT and QSG.18 give

$$
\limsup\frac{b-P_F}{D}\le d_\eta(y)
$$

and

$$
\limsup Q/D\le d_\eta(y).
\tag{6.4}
$$

OD gives

$$
H_{out}
\le
\frac\pi{4\sqrt2}(x_B+a)^{3/2}\sqrt{b-P_F}.
$$

As in SOD,

$$
x_B+a\le2q.
$$

By QSG.4,

$$
q/D=y+d_H/D
\le y+\eta_0/3+o(1).
$$

Therefore

$$
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac\pi{4\sqrt2}
[2(y+\eta_0/3)]^{3/2}
\sqrt{d_\eta(y)}.
}
\tag{QSG.5a}
$$

whenever `d_eta(y)>=0`.

The exceptional-face isoperimetric bound gives

$$
\boxed{
\limsup\frac{A_{exc}}{D^2}
\le
\frac{d_\eta(y)^2}{4\pi}.
}
\tag{QSG.5b}
$$

C49/ZG charging says

$$
G\le H_{out}+A_{exc}+O(D).
$$

Now `A_PI(y)` is increasing on (6.2), so the left side of QSG.16 is at least

$$
A_{PI}(2\rho)-C_A(\eta_0)
>0.49735.
\tag{6.5}
$$

The function `d_eta(y)` is increasing on (6.2). Indeed, here `cos y<0.1`, `sin y>0.99`, and the square-root denominator in its derivative exceeds `2.4`, so

$$
d_\eta'(y)>0.86.
$$

Thus the right sides QSG.5a-QSG.5b are maximized at `y=1.5318`. Direct conservative evaluation there gives

$$
d_\eta(1.5318)<0.02738
\tag{6.6}
$$

and

$$
\frac\pi{4\sqrt2}
[2(1.5318+\eta_0/3)]^{3/2}
\sqrt{0.02738}
+
\frac{0.02738^2}{4\pi}
<0.49275.
\tag{6.7}
$$

This contradicts (6.5) by more than `0.0046`.

Hence no countersequence can have

$$
\boxed{y\le1.5318.}
\tag{QSG.20}
$$

---

## 7. High diameter-density range: Hemmi beats JC

Now assume

$$
y\ge1.5318.
\tag{7.1}
$$

The forced perimeter QSG.18 is increasing in `y`. At the lower endpoint,

$$
\boxed{p_\eta(1.5318)>3.0362.}
\tag{7.2}
$$

Thus every remaining case lies in Hemmi's fixed-diameter perimeter range.

Put

$$
p_2:=12\sin(\pi/12)=3.10582854\ldots .
$$

### 7.1 First sharp Hemmi branch

For

$$
3<p\le p_2,
$$

HKS gives

$$
A_H(p)
=3(p/p_2)^2-\frac{3+\sqrt3}{2}.
\tag{7.3}
$$

The attachment-area allowance QSG.14 gives

$$
G/D^2\ge A_H(p)-C_A(\eta_0)-o(1).
$$

JC gives the upper capacity in QSG.17. Define

$$
\Phi_y(p)
:=A_H(p)-C_A(\eta_0)
-
\frac{(1+\eta_0+p-y)^2}{4\pi}.
$$

For `p>=3.0362`, `p<=p_2`, and `y>=1.5318`,

$$
A_H'(p)>1.86,
$$

while the derivative of the JC term is less than `0.42`. Hence

$$
\boxed{\Phi_y'(p)>1.44.}
\tag{7.4}
$$

It is enough to test the smallest allowed `p=p_eta(y)`. By definition of QSG.19,

$$
\frac{(1+\eta_0+p_\eta(y)-y)^2}{4\pi}
=A_{PI}(y)-C_A(\eta_0).
$$

Therefore

$$
\Phi_y(p_\eta(y))
=A_H(p_\eta(y))-A_{PI}(y).
\tag{7.5}
$$

The right side is increasing in `y` on the remaining interval. For `y<=pi/2`, `p_eta'(y)>1` while `A_PI'(y)<0.02` and `A_H'>1.86`; for `y>=pi/2`, `A_PI` is constant and `p_eta'=1`.

At `y=1.5318`, a conservative evaluation gives

$$
\boxed{
A_H(p_\eta(1.5318))-A_{PI}(1.5318)
>0.0014.
}
\tag{7.6}
$$

Thus every case with `p<=p_2` violates JC.

### 7.2 Perimeters at least `p_2`

For

$$
p\ge p_2,
$$

HKI's simple Hemmi `n=2` inequality gives

$$
A(F)/D^2
\ge
\frac p2\cos(\pi/12)-\frac{\sqrt3}{2}
\ge
\frac{3-\sqrt3}{2}
>0.6339.
$$

After subtracting the attachment allowance,

$$
G/D^2>0.6334.
$$

But for `p<=pi`, `y>=1.5318`, and `e_BB/D<=1+eta_0`, JC is at most

$$
\frac{(1+\eta_0+\pi-1.5318)^2}{4\pi}
<0.5421.
$$

Contradiction.

Thus no high-density case survives either.

---

## 8. Conclusion

Sections 6 and 7 cover every possible `y>=2rho`.

Therefore no subsequence satisfying (1.1) exists. This proves QSG.1.

The logical chain is

```text
D epsilon -> 0, L/D <= 1+1e-7
    -> NLC: one depth-D response carrier
    -> ZK: only eta_0 D graph-diameter/slack outside exact slope-one
    -> quantitative SCC focal ellipse
    -> total attachment-cell area < 0.000497 D^2
    -> PI + JC forces a large force-hull perimeter
    -> low y: OD cannot supply enough pocket/face area
    -> high y: sharp Hemmi area already exceeds JC capacity
    -> contradiction.
```

---

## 9. Regression audit

- The actual diameter pair `z,a` used in the augmented giant component is justified by NSE/UCM: actual diameter partners carry `1-o(1)` response; with NLC branch count one, the unique long component receives a positive contribution to at least one such pair.
- The quantitative ellipse bound uses only outer-walk length and endpoint diameter, not a false assumption that the giant graph is a simple path.
- `C_A(eta)` includes both the giant attachment polygon and all remaining harmonic attachment polygons.
- The low-density OD branch keeps the `d_H=O(eta D)` correction in `q/D`.
- The high-density branch subtracts the same attachment allowance from Hemmi before comparing to JC.
- No near-circle assumption is used.
- The small numerical constant is chosen far below the apparent limit of this argument; all displayed branch margins are at least `10^-3` except the harmless attachment allowance itself.

---

## 10. Next target

The present constants are deliberately crude. The same proof skeleton should support a larger explicit gap by optimizing `eta` instead of fixing `10^-7`.

A numerical exploration of the analytic inequalities indicates that the present coarse attachment-area estimate should remain closing until `eta` is on the order of `10^-7` to `10^-6`; improving the giant-cell ellipse budget or using the exact EFAQ/Hemmi perimeter relation may enlarge this considerably.

The higher-value structural target, however, is now the entire interval

$$
1+10^{-7}
\le
\liminf L/D
<2,
$$

where NLC still gives a unique depth-D response carrier but leaves a linear `O((L/D-1)D)` graph-diameter budget outside it. A useful next theorem is to force that extra budget into either

1. a second macroscopic electrical carrier, triggering NLC slope two; or
2. enough noncrossing singleton/outer-pocket structure to increase `L` again.

## 11. Compact handoff

```text
QSG quantitative near-zero slope gap.
Assume D epsilon->0 and L/D<=1+eta0+o(1), eta0=1e-7.
NLC has exactly one long component I_* with delta_*>D-3 and an actual diameter
attachment pair z,a.
ZK:
    sum delta + R_I+s_B+3k=6+L
implies
    k/D<=eta0/3+o(1),
    sum_{r!=*}delta_r<=eta0 D+o(D),
    delta_*+r_*<=6+L.
For SCC augmentation G',
    b'+Q'=2(delta_*+r_*+2)<=2L+16.
The two outer z-a arcs have excess <=2eta0 D+o(D), so all of G' lies in the focal
ellipse with major axis (1+2eta0)D+o(D). Hence giant attachment area/D^2 <=
    C_g=(pi/2)(1+2eta0)sqrt(eta0(1+eta0)).
Other attachment cells contribute <=(pi/4)eta0^2 D^2+o(D^2).
Thus total attachment-cell area <=C_A D^2 with C_A<0.000497.

Let y=h/D, p=per(F)/D. PI + actual-perimeter JC give
    A_PI(y)-C_A <= (1+eta0+p-y)^2/(4pi),
so
    p>=p_eta(y)=y-(1+eta0)+sqrt(4pi(A_PI(y)-C_A)).
For y<=1.5318, this also makes detour and Q small; OD+face isoperimetry give total
cavity capacity <0.49275, while PI-C_A>0.49735. Contradiction.
For y>=1.5318, p_eta>3.0362. On Hemmi's first branch, A_H grows in p with derivative
>1.86 while JC capacity grows <0.42, and already at p=p_eta the Hemmi-vs-PI margin
is >0.0014. For p>=p2 the margin is >0.09. Contradiction.
Therefore
    liminf L/D >=1.0000001
in every D epsilon->0 sequence.
```
