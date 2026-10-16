<!-- theorem-state: {"artifact_id":"ART-B7EBA97202B3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_joint_direction_perimeter_area_floor_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a7dd79f73a3be57943780d1652bb1f1145c29282; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — joint diameter-direction/perimeter/area floor

**Date:** 2026-09-10  
**Repository state:** branch `research/fs-perimeter-cavity-20260910`, after `40dfea6f8896a07183834d971416b8435c6b8d5f`  
**Run type:** closing-proof continuation / exact convex geometry / asymptotic optimization  
**Target:** Target C, C-II after ZF/FS/FSDB/JC/GU  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** no external theorem used  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The previous PS/BSG/CSRI reports treated force-hull area and diameter-direction
population partly as separate constraints.  This report couples them directly.

Let

\[
S=\frac12((F-o)-(F-o)),
\qquad
\Omega=\frac2D S\subseteq B(0,1),
\]

and let

\[
p=\frac{P_F}{D}=\frac12\operatorname{per}\Omega,
\qquad
y=\lim\frac hD.
\]

The exact diameter-direction polygon

\[
Q_D:=\operatorname{conv}\{\pm u_e:e\in E(H)\}
\subseteq\Omega
\]

has `h` projective unit-circle directions with gaps at least

\[
\delta_D=2\arcsin\frac1{2D}.
\]

A new finite cap inequality proves that area added outside `Q_D` cannot create force-
hull perimeter for free.  The resulting asymptotic theorem is

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\mathcal J(y,p)
:=\frac{y+\sin(y/2)(p-y)}4.}
\tag{JD.1}
\]

It simultaneously contains the FSDB area floor and the new diameter-direction
perimeter floor

\[
\boxed{p\ge y+2\cos(y/2).}
\tag{JD.2}
\]

at the sharp lower-perimeter edge.

Feeding JD.1 into the actual-perimeter JC/GU cavity budget yields a fully explicit
post-ZF currency bound.  Let `rho` be the Dottie number `rho=cos rho` and define
`lambda_JD` as the unique positive root of

\[
\boxed{
(\pi^2+1)\lambda^2
+4\rho\lambda+4\rho^2
-2\pi\rho(1+\sin\rho)=0.}
\tag{JD.3}
\]

Equivalently, put `y_*=2rho` and use

\[
(\pi^2+1)\lambda^2+2y_*\lambda+y_*^2
-\pi(y_*+\sin y_*)=0.
\]

Then

\[
\boxed{
\lambda_{JD}=0.5937285472681860970\ldots,}
\tag{JD.4}
\]

and every unbounded post-ZF survivor sequence satisfies

\[
\boxed{
\liminf\frac{e_{BB}+2s_C}{D}
\ge\lambda_{JD}.}
\tag{JD.5}
\]

This strictly improves the previous explicit report-level floors
`0.593361...`, `0.593483...`, and `0.593504...`.  Unlike those improvements, JD uses
no reverse-isoperimetric literature.

The unique scalar equality geometry is also forced:

\[
\boxed{
\frac hD\to2\rho,
\qquad
\frac{P_F}{D}\to4\rho.}
\tag{JD.6}
\]

Level I remains open because this report does not yet exclude that exact low-density,
minimum-perimeter diameter-direction geometry or give a universal high-currency upper
bound.

---

## 1. Exact target implication

The route is

```text
all actual diameter directions + C67 separation
    -> inscribed direction polygon Q_D subset Omega
cap area/perimeter inequality relative to Q_D
    -> finite joint area/perimeter/direction inequality
FS.4
    -> transfer from exact central symmetral to actual force hull
JC + GU
    -> necessary inequality in (y,p,lambda)
exact endpoint comparison
    -> lambda >= lambda_JD
    -> equality can occur only at y=2rho, p=4rho.
```

The desired Level I endpoint is still exclusion of every post-ZF source, equivalently
`b+Q>2h`, or a strict sub-`D` competitor.

---

## 2. Geometry of the mandatory direction polygon

Order the `h` projective diameter directions cyclically and write their gaps

\[
g_1,\ldots,g_h,
\qquad
\sum_{i=1}^h g_i=\pi.
\tag{2.1}
\]

C67 gives

\[
\boxed{g_i\ge\delta_D:=2\arcsin\frac1{2D}.}
\tag{2.2}
\]

Put

\[
G_D:=\pi-(h-1)\delta_D,
\qquad
c_D:=\cos\frac{G_D}{2}
=\sin\frac{(h-1)\delta_D}{2}.
\tag{2.3}
\]

Since the other `h-1` gaps are at least `delta_D`, every actual gap satisfies

\[
g_i\le G_D.
\tag{2.4}
\]

The symmetric inscribed polygon

\[
Q_D=\operatorname{conv}\{\pm u_e\}
\]

has exact area and perimeter

\[
\boxed{
\operatorname{area}Q_D
=\sum_{i=1}^h\sin g_i,}
\tag{2.5}
\]

\[
\boxed{
\frac12\operatorname{per}Q_D
=2\sum_{i=1}^h\sin\frac{g_i}{2}.}
\tag{2.6}
\]

The DB inclusion gives

\[
Q_D\subseteq\Omega.
\tag{2.7}
\]

---

## 3. Local cap inequality

### Lemma JD.1 — cap area pays for excess perimeter

Let `a,b` be consecutive vertices of an inscribed convex polygon `Q subset B(0,1)`,
with central gap `g in (0,pi)` and chord length `d=2sin(g/2)`.  Let `K` be convex with

\[
Q\subseteq K\subseteq B(0,1).
\]

Let `Gamma` be the portion of `partial K` joining `a` to `b` outside the chord, of
length `ell`, and let `C` be the cap between `Gamma` and `[a,b]`.  Then

\[
\boxed{
\operatorname{area}C
\ge\frac12\cos\frac g2\,(\ell-d).}
\tag{3.1}
\]

### Proof

Rotate coordinates so that the endpoints are

\[
a=(\cos(g/2),-\sin(g/2)),
\qquad
b=(\cos(g/2),\sin(g/2)).
\]

Orient `Gamma` counterclockwise from `a` to `b`.  At almost every point of a convex
boundary the unit tangent `T` and outward normal `n` exist, and

\[
x\times T=h_K(n),
\]

where `h_K` is the support function.

Along this boundary portion the outward normal angle lies between the endpoint radial
directions.  In every such direction the support of the two-point chord hull is at
least `cos(g/2)`.  Since `Q subset K`,

\[
h_K(n)\ge\cos(g/2)
\]

for almost every point of `Gamma`.  Therefore

\[
\int_\Gamma x\times dx
\ge\cos(g/2)\,\ell.
\tag{3.2}
\]

Close the cap by traversing the chord from `b` back to `a`.  Its signed Green integral
is exactly

\[
-\cos(g/2)d.
\]

Hence Green's formula gives

\[
2\operatorname{area}C
\ge\cos(g/2)(\ell-d),
\]

which is (3.1).  Nonsmooth boundary points form a length-null set, so no smoothness
assumption is needed. `square`

### Corollary JD.1 — global cap sum

Apply Lemma JD.1 to all `2h` antipodally paired sides of `Q_D`.  Because every
`g_i<=G_D`,

\[
\cos(g_i/2)\ge c_D.
\]

The caps have disjoint interiors and cover `Omega\setminus Q_D` up to boundaries.
Thus

\[
\boxed{
\operatorname{area}\Omega-\operatorname{area}Q_D
\ge
\frac{c_D}{2}
\left(\operatorname{per}\Omega-\operatorname{per}Q_D\right).}
\tag{3.3}
\]

Put

\[
p_D:=\frac12\operatorname{per}\Omega=\frac{P_F}{D},
\qquad
p_{Q,D}:=\frac12\operatorname{per}Q_D.
\]

Then

\[
\boxed{
\operatorname{area}\Omega
\ge
c_Dp_D+
\sum_{i=1}^h
\left(
\sin g_i-2c_D\sin\frac{g_i}{2}
\right).}
\tag{3.4}
\]

---

## 4. Exact finite gap minimization

Define on `[delta_D,G_D]`

\[
f_D(g)=\sin g-2c_D\sin(g/2).
\tag{4.1}
\]

Then

\[
f_D''(g)
=
-\sin g+\frac{c_D}{2}\sin(g/2)
=
\sin(g/2)
\left(-2\cos(g/2)+\frac{c_D}{2}\right).
\]

Because `g<=G_D`, `cos(g/2)>=c_D`, so

\[
\boxed{f_D''(g)\le-\frac32c_D\sin(g/2)\le0.}
\tag{4.2}
\]

Thus `f_D` is concave.  Under

\[
g_i\ge\delta_D,
\qquad
\sum g_i=\pi,
\]

a concave sum is minimized at an extreme point of the feasible simplex: `h-1` gaps
are `delta_D` and the remaining gap is `G_D`.  Since

\[
f_D(G_D)=0,
\]

(3.4) yields the exact finite theorem:

### Theorem JD — finite direction/perimeter/area coupling

\[
\boxed{
\operatorname{area}\Omega
\ge
c_Dp_D
+(h-1)
\left(
\sin\delta_D
-2c_D\sin\frac{\delta_D}{2}
\right).}
\tag{4.3}
\]

No global optimality is used in JD itself beyond the availability of the actual
`Q_D subset Omega`; it is a deterministic convex-geometric consequence of that
inclusion and C67 separation.

---

## 5. Companion perimeter floor

From `Q_D subset Omega` and monotonicity of convex perimeter,

\[
p_D\ge p_{Q,D}
=2\sum_i\sin(g_i/2).
\]

The function `sin(g/2)` is concave on `[0,pi]`, so the same extreme-point argument
gives

\[
\boxed{
p_D\ge
2\left[
(h-1)\sin\frac{\delta_D}{2}
+\cos\frac{(h-1)\delta_D}{2}
\right].}
\tag{5.1}
\]

This is the finite version of JD.2.

---

## 6. Asymptotic transfer to the actual force hull

Take an unbounded post-ZF survivor sequence and a subsequence on which

\[
\frac hD\to y,
\qquad
\frac{P_F}{D}\to p.
\tag{6.1}
\]

DB gives

\[
2\rho\le y\le\pi,
\tag{6.2}
\]

while convex perimeter gives `p<=pi`.  Also

\[
D\delta_D\to1,
\qquad
(h-1)\delta_D\to y,
\qquad
c_D\to\sin(y/2).
\tag{6.3}
\]

Equation (5.1) gives

\[
\boxed{
p\ge p_0(y):=y+2\cos(y/2).}
\tag{6.4}
\]

Divide (4.3) by one, use

\[
(h-1)\sin\delta_D\to y,
\]

\[
2(h-1)c_D\sin(\delta_D/2)
\to y\sin(y/2),
\]

and obtain

\[
\liminf\operatorname{area}\Omega
\ge
p\sin(y/2)+y(1-\sin(y/2)).
\tag{6.5}
\]

Since

\[
\operatorname{area}\Omega
=4\frac{\operatorname{area}S}{D^2}
\]

and FS.4/FD give

\[
\operatorname{area}S-\operatorname{area}F=o(D^2),
\]

we get JD.1:

\[
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\frac{y+\sin(y/2)(p-y)}4.}
\tag{6.6}
\]

At the minimum permitted perimeter `p=p_0(y)`, the right side becomes

\[
\frac{y+\sin y}{4}=\Phi(y),
\]

so FSDB is recovered exactly at the lower-perimeter edge.  For every
`p>p_0(y)`, JD.1 is strictly stronger than the bare FSDB area floor.

---

## 7. The new JC/GU necessary inequality

Let

\[
\lambda=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t=\lim\frac{e_{BB}}D,
\qquad 0\le t\le\lambda.
\]

JC with actual force-hull perimeter gives

\[
\limsup\frac G{D^2}
\le
\frac{(t+m)^2}{4\pi},
\qquad
m=\min\{y,p-y\}.
\tag{7.1}
\]

GU gives

\[
\limsup\frac1{D^2}\sum_r\operatorname{area}(P_r)
\le\frac\pi4\lambda^2.
\tag{7.2}
\]

Using `G=area(F)-sum area(P_r)`, JD.1, and `t<=lambda`, every survivor limit must
satisfy

\[
\boxed{
\mathcal J(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m)^2}{4\pi},}
\tag{7.3}
\]

where

\[
\mathcal J(y,p)=\frac{y+s(p-y)}4,
\qquad s=\sin(y/2),
\]

and

\[
2\rho\le y\le\pi,
\qquad
p_0(y)\le p\le\pi.
\tag{7.4}
\]

Equivalently define

\[
\boxed{
H(\lambda;y,p)
=(\pi^2+1)\lambda^2
+2m\lambda+m^2
-\pi\bigl[y+s(p-y)\bigr].}
\tag{7.5}
\]

Every survivor limit has `H>=0`.  For fixed `(y,p)`, `H` is strictly increasing in
`lambda>=0`.

---

## 8. Exact global optimization

Put

\[
y_*=2\rho.
\]

Because `rho=cos rho`,

\[
p_0(y_*)
=2\rho+2\cos\rho
=4\rho
=2y_*.
\tag{8.1}
\]

Let `lambda_JD` be the positive root of

\[
H(\lambda;y_*,2y_*)=0.
\]

This is exactly JD.3.

First note

\[
0<\lambda_{JD}<1.
\tag{8.2}
\]

At `lambda=0`, the defining polynomial is negative because
`y_*<pi/2` implies `y_*^2<pi y_*<pi(y_*+sin y_*)`.  At `lambda=1`,
`y_*+sin y_*<pi/2+1<pi`, so the `pi^2` term alone dominates the negative area term,
leaving additional positive terms.  Thus the positive root lies in `(0,1)`.

We now prove

\[
\boxed{
H(\lambda_{JD};y,p)\le0
}
\tag{8.3}
\]

throughout the feasible domain, with equality only at `(y,p)=(y_*,2y_*)`.
Since a survivor requires `H>=0`, this proves JD.5.

Write

\[
x=p-y,
\qquad
x_0(y)=2\cos(y/2).
\]

The domain is

\[
x_0(y)\le x\le\pi-y.
\tag{8.4}
\]

### 8.1 The minimum-perimeter endpoint

At `x=x_0`, JD.1 equals FSDB exactly, and

\[
H_0(y)
=(\pi^2+1)\lambda_{JD}^2
+4\lambda_{JD}\cos(y/2)
+4\cos^2(y/2)
-\pi(y+\sin y).
\tag{8.5}
\]

At `y=y_*`, `x_0=y_*`, so `H_0(y_*)=0`.  Differentiating,

\[
H_0'(y)
=-2\lambda_{JD}\sin(y/2)
-2\sin y
-\pi(1+\cos y)<0
\tag{8.6}
\]

for `y in[y_*,pi)`.  Hence

\[
H_0(y)<0
\qquad(y>y_*).
\tag{8.7}
\]

### 8.2 The point `p=2y`

For `y<=pi/2`, the cavity width reaches its maximum `m=y` at `x=y`.  There

\[
H_2(y)
=(\pi^2+1)\lambda_{JD}^2
+2y\lambda_{JD}+y^2
-\pi y(1+\sin(y/2)).
\tag{8.8}
\]

Again `H_2(y_*)=0`.  Its derivative is

\[
H_2'(y)
=2\lambda_{JD}+2y
-\pi\left(1+\sin(y/2)+\frac y2\cos(y/2)\right).
\tag{8.9}
\]

This is strictly negative on `[y_*,pi/2]`.  Indeed `lambda_JD<1` and `2y<=pi` give

\[
2\lambda_{JD}+2y<2+\pi.
\]

Also `sin(y/2)>=sin rho`.  The standard exact Dottie enclosure

\[
\rho<\frac{37}{50}
\]

gives

\[
\sin\rho=\sqrt{1-\rho^2}>
\frac{\sqrt{1131}}{50}>rac23.
\]

Since `pi>3`,

\[
\pi(1+\sin(y/2))>\pi+2.
\]

The omitted positive term `(y/2)cos(y/2)` only strengthens the inequality.  Thus

\[
H_2(y)<0
\qquad(y>y_*).
\tag{8.10}
\]

### 8.3 All `p` for `y<=pi/2`

When `x<=y`, `m=x` and, for fixed `y,lambda_JD`,

\[
H=(\pi^2+1)\lambda_{JD}^2
+2x\lambda_{JD}+x^2
-\pi(y+sx)
\]

is a convex quadratic in `x`.  Hence its maximum on `[x_0,y]` occurs at one of the
endpoints, already controlled by `H_0,H_2`.

When `x>=y`, `m=y` is fixed and `H` is affine with derivative

\[
\frac{\partial H}{\partial x}=-\pi s<0.
\]

So its maximum on that region occurs at `x=y`.  Therefore (8.3) holds for all
`y in[y_*,pi/2]`, with equality only at `y=y_*`, `x=y_*`.

### 8.4 All `p` for `y>=pi/2`

Here `x<=pi-y<=y`, so `m=x` throughout.  The same convexity says the maximum over
`x in[x_0,pi-y]` is at `x=x_0` or `x=pi-y`.

The first endpoint is `H_0<0`.  At the second endpoint, `p=pi`, put

\[
H_\pi(y)=H(\lambda_{JD};y,\pi).
\]

Differentiating with `x=pi-y`,

\[
H_\pi'(y)
=-2\lambda_{JD}-2x
-\pi\left(1-\sin(y/2)+\frac x2\cos(y/2)\right)<0.
\tag{8.11}
\]

The bracket is nonnegative.  At `y=pi/2`, `H_pi=H_2<0`, so

\[
H_\pi(y)<0
\qquad(y\ge\pi/2).
\tag{8.12}
\]

This completes the proof of (8.3) and therefore JD.5.

### Uniqueness of scalar equality

Every inequality above is strict away from

\[
(y,p)=(2\rho,4\rho).
\]

Therefore any survivor sequence satisfying

\[
\frac{e_{BB}+2s_C}{D}\to\lambda_{JD}
\]

must satisfy JD.6 after passage to every convergent subsequence.  Compactness then
forces JD.6 for the full sequence.

---

## 9. Exact improvement over the preceding floors

The previous strongest explicit report-level bound on this branch was

\[
\lambda_{CS}=0.5935048918881262\ldots .
\]

JD gives

\[
\lambda_{JD}=0.5937285472681861\ldots .
\]

The strict improvement does not depend on the printed decimals.  CSRI optimizes among
all centrally symmetric disk bodies of the given perimeter, but its endpoint has only
finitely many unit-circle contacts.  JD instead retains the linear population of
actual C67-separated diameter directions.  The JD feasible set is therefore strictly
smaller in the low-perimeter regime.  Numerically the increase is

\[
0.0002236553800599\ldots,
\]

but the theorem is defined by the exact root JD.3.

The earlier Bogosel reports remain useful audits of why the direction population
matters, but are no longer needed for the strongest bound.

---

## 10. Equality geometry and exact remaining lemma

At the JD endpoint,

\[
y=2\rho,
\qquad p=4\rho,
\qquad p=p_0(y)=2y.
\]

Thus both the C67 perimeter floor and the finite joint-area inequality must
asymptotically saturate.  The gap minimization in Section 4 shows what that means at
leading order: all but one projective diameter-direction gaps concentrate at the
minimum scale `delta_D`, while one residual projective gap has size

\[
\pi-2\rho+o(1).
\]

Equivalently, the mandatory direction polygon tends to the convex hull of two
antipodal unit-circle arcs of projective length `2rho`.  There is no asymptotic
perimeter available for a macroscopic cap outside this direction hull.

This is the next exact target:

> **JD endpoint exclusion.**  Exclude every unbounded post-ZF survivor sequence for
> which
> \[
> h/D\to2\rho,
> \qquad
> P_F/D\to4\rho,
> \qquad
> (e_{BB}+2s_C)/D\to\lambda_{JD},
> \]
> by combining the one-gap diameter-direction concentration with the diameter-graph
> caterpillar/shared-endpoint structure, reciprocal equilibrium, or a finite strict
> sub-`D` rearrangement.

Excluding this endpoint would again produce a uniform positive gap above
`lambda_JD`.  A stronger result would give a direct universal upper bound below the
new lower floor and close C-II.

---

## 11. Regression audit

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | its diameter directions become equidistributed, so `p->pi`, far from the one-large-gap JD endpoint |
| dense isolated shell filling | yes | JD acts on the actual force symmetral; full-source FS.4 retains isolates, and no small-isolate assumption is made |
| perfect matching | yes | no matching hypothesis is used; matching is independently excluded |
| near-star response | yes | no conductance floor or arbitrary response-operator estimate is used |
| fixed symmetric six-gon | yes | JD keeps `h=Theta(D)` actual circle contacts rather than replacing them by an unconstrained finite extremizer |
| FSDB concentrated-gap model | yes | JD recovers FSDB exactly when the force-hull perimeter is itself minimal for those directions |

The decisive global-source input is FS.4, which transfers the exact central-symmetral
geometry back to the actual force hull up to `o(D^2)` area.  A generic dense isolated
filling has no certificate that it is a global source satisfying the whole selected
post-ZF theorem stack.

---

## 12. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| local cap inequality JD.1 | proved exactly | Green's formula + support monotonicity on one direction gap |
| global cap sum | proved exactly | caps partition `Omega\Q_D` and each side gap is at most `G_D` |
| finite JD inequality (4.3) | proved exactly | concavity of `f_D` and extreme-point gap concentration |
| finite perimeter floor (5.1) | proved exactly | convex perimeter monotonicity + concavity of `sin(g/2)` |
| asymptotic joint floor JD.1 | proved under FS.4/DB/C67 | exact scaling and `o(D^2)` area transfer |
| JC/GU survivor inequality | proved | existing exact cavity and cell-area bounds, only relaxation `t<=lambda` |
| global optimizer `y=2rho,p=4rho` | proved | endpoint monotonicity plus convexity in `p-y` |
| explicit `lambda_JD` floor | proved asymptotically | exact root JD.3 |
| JD endpoint impossible | not proved | remains the immediate equality-geometry target |
| Level I | still open | no contradiction for all high-currency survivors |

---

## 13. Failed routes and no-go results

1. **Separate force-hull area and perimeter optimization.**  This loses the fact that
   the same `Theta(D)` diameter directions create both quantities.  JD strictly
   improves all three preceding separate-area floors.
2. **Generic reverse-isoperimetric stability.**  It is unnecessary for the strongest
   current scalar bound.  The elementary cap calculation directly incorporates the
   required diameter points.
3. **Declaring the concentrated one-gap endpoint impossible.**  Unlike the finite
   Bogosel polygons, its limit has continuum unit-circle contact arcs and can absorb
   `Theta(D)` separated directions.  The previous circle-crowding contradiction does
   not apply.  A new source-specific argument is required.

---

## 14. Computation and reproducibility

No computation is a proof dependency.  The exact constant is JD.3 with
`rho=cos rho`.  Decimal orientation:

```text
rho       = 0.7390851332151606416553120876738734...
y_*       = 1.4781702664303212833106241753477468...
p_*       = 2.9563405328606425666212483506954936...
lambda_JD = 0.5937285472681860970190308266960039...
```

The proof of the location of the optimizer is symbolic and uses only the standard
rational Dottie enclosure `rho<37/50`, `pi>3`, and elementary trigonometric signs.

---

## 15. Concurrent repository state

The branch was created from `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4`.
During the run, `main` advanced to
`f977f2d0d25f5022c2a587e59cab38375d85caee` only to correct perfect-matching
provenance.  That change does not alter FS, FSDB, DB, C67, JC, or GU, so the theorem
state used here remains compatible without silently rebasing the proof.

---

## 16. Promotion recommendation

**Hold as report pending independent audit.**  JD is now the preferred quantitative
post-FS C-II result because it is stronger and has fewer external dependencies than
PS/BSG/CSRI.  Before promotion, independently check:

1. the cap normal-range/support argument in Lemma JD.1;
2. the factor-of-two normalization in the antipodal cap sum;
3. the concavity/extreme-point finite gap minimum;
4. the global `H(lambda_JD;y,p)<=0` case split.

If those pass, promote JD and JD.5 into the post-FS Target C frontier.  The earlier
reverse-isoperimetric reports should remain dated provenance rather than parallel
canonical endpoints.

---

## 17. Next run

Attack the exact JD equality geometry.  The highest-value source-specific question is
whether a post-ZF diameter graph with `h~2rho D` can place all but one of its projective
direction gaps at the C67 minimum scale while simultaneously satisfying FS.3's
shared-endpoint clustering, the caterpillar/odd-cycle diameter-graph classification,
and the selected KKT equilibrium.  A fixed positive loss in either direction-gap
concentration or force-hull cap perimeter would raise the explicit floor again.

Do not iterate an unrelated scalar constant: the next mechanism must exclude the
one-gap endpoint or turn its structure into a strict competitor.

---

## 18. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New finite theorem JD:
Let Omega=2S/D and Q_D=conv{+-u_e} subset Omega.  If the h projective direction gaps
satisfy g_i>=delta_D, put
    G_D=pi-(h-1)delta_D,
    c_D=cos(G_D/2).
Then
    area(Omega)
      >= c_D*(per(Omega)/2)
         +(h-1)[sin(delta_D)-2c_D sin(delta_D/2)].
Proof: each cap outside one Q_D chord pays at least
    (cos(g_i/2)/2)*(excess boundary length),
then minimize the remaining concave gap sum at h-1 minimal gaps and one residual gap.
Also
    per(Omega)/2
      >=2[(h-1)sin(delta_D/2)+cos((h-1)delta_D/2)].

Asymptotically, with y=h/D and p=P_F/D,
    area(F)/D^2 >= [y+sin(y/2)(p-y)]/4,
    p>=y+2cos(y/2).
Insert this into actual-perimeter JC + GU.  The exact global optimizer is
    y=2rho,
    p=4rho=2y,
where rho=cos rho.  Thus
    (e_BB+2s_C)/D >= lambda_JD-o(1),
    lambda_JD=0.5937285472681860970...,
with lambda_JD defined by
    (pi^2+1)lambda^2+4rho lambda+4rho^2
      -2pi rho(1+sin rho)=0.

Equality is not yet excluded.  It forces one-gap concentration of the actual diameter
directions: all but one projective gap are asymptotically at the C67 minimum scale,
with one residual gap pi-2rho+o(1), and P_F/D->4rho.

Exact next lemma:
Exclude that one-gap post-ZF geometry using diameter-graph incidence/shared-endpoint
structure, reciprocal equilibrium, or a strict sub-D rearrangement.
```