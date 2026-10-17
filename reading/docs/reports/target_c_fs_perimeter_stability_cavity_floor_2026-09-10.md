> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_perimeter_stability_cavity_floor_2026-09-10.md) · source SHA-256 `0b87b770e88dbf103669e1a050c2b5a18bf49bddaf4419c95fef6e44a2a89574`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7548F05BBBB0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_perimeter_stability_cavity_floor_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ff15a8339ce66fe679de1d05750fa0c9427a3d62; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — quantitative FS perimeter stability raises the cavity floor

**Date:** 2026-09-10  
**Repository state:** `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4` at start  
**Run type:** closing-proof continuation / exact asymptotic optimization / audit  
**Target:** Target C, C-II after ZF/FS/FSDB/FSJC/FDJ  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** decimal evaluation only; no computation is a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The just-landed FDJ theorem excludes the exact FSJC endpoint and therefore gives a
nonexplicit gap above

```math
\lambda_{FSJC}=0.5882283437736394\ldots .
```

This report makes a positive part of that gap explicit.  The new geometric input is a
quantitative reverse area estimate for a centrally symmetric diameter-bounded convex
body.  Applied to the FS central symmetral, it gives the actual force hull the
perimeter-sensitive area lower bound

```math
\boxed{
\liminf \frac{\operatorname{area}F}{D^2}
\ge
\Psi(p):=\frac{p^2}{2\pi}-\frac\pi4,
\qquad
p=\lim\frac{\operatorname{per}F}{D}.
}
\tag{PS.1}
```

Combining this with FSDB's diameter-density lower bound

```math
\Phi(y)=\frac{y+\sin y}{4},
\qquad y=\lim h/D,
```

and JC's **actual-perimeter** cavity capacity yields a two-parameter feasible-region
inequality.  Its exact global minimum can be solved analytically.

Let `rho` be the Dottie number `rho=cos rho`.  Let `y_0` be the unique root in
`(2rho,pi/2)` of

```math
\boxed{
8y_0^2=\pi^2+\pi(y_0+\sin y_0).
}
\tag{PS.2}
```

Let `lambda_PS` be the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2+2y_0\lambda+\pi^2-7y_0^2=0.
}
\tag{PS.3}
```

Numerically,

```math
y_0=1.4861348981098190\ldots,
\qquad
\lambda_{PS}=0.5933612807422635\ldots .
```

Then every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge \lambda_{PS}.
}
\tag{PS.4}
```

Moreover `lambda_PS>lambda_FSJC` exactly.  Thus FDJ's nonexplicit strict gap contains
the explicit increment

```math
\lambda_{PS}-\lambda_{FSJC}
=0.0051329369686240\ldots .
```

This is still a lower bound, not a Level I contradiction.  No universal upper bound
below `lambda_PS` is proved here.

---

## 1. Starting endpoint and closing implication

The current post-FSJ C-II state supplies, along every convergent survivor subsequence,

```math
2\rho\le y:=\lim h/D\le\pi,
\tag{1.1}
```

```math
0\le t:=\lim e_{BB}/D\le
\lambda:=\lim(e_{BB}+2s_C)/D,
\tag{1.2}
```

and FSDB gives

```math
\liminf \frac{\operatorname{area}F}{D^2}
\ge \Phi(y):=\frac{y+\sin y}{4}.
\tag{1.3}
```

The actual force-hull perimeter will be written

```math
p:=\lim \frac{P_F}{D},
\qquad P_F:=\operatorname{per}F.
\tag{1.4}
```

The post-ZF endpoint-count and convex-perimeter bounds give

```math
\boxed{2\rho\le y\le p\le\pi.}
\tag{1.5}
```

Indeed `h<=q`, while the `q` loaded force-hull vertices are cyclically
unit-separated, so `q<=P_F`; Cauchy's perimeter-diameter inequality gives
`P_F<=pi D`.

The implication attacked here is

```text
FS.4 approximate central symmetry
    -> quantitative force-hull area floor Psi(p)
FSDB
    -> independent area floor Phi(y)
actual-perimeter JC
    -> cavity capacity with min{y,p-y}
exact two-parameter minimization
    -> explicit lambda >= lambda_PS > lambda_FSJC.
```

The result does not by itself supply the missing upper bound on `lambda`.

---

## 2. Quantitative centrally symmetric perimeter-area inequality

### Lemma PS.1 — symmetric diameter/perimeter forces area

Let `S` be a compact centrally symmetric planar convex body with diameter `D` and
perimeter `P`.  Then

```math
\boxed{
\operatorname{area}S
\ge
\frac{P^2}{2\pi}-\frac{\pi D^2}{4}.
}
\tag{2.1}
```

The inequality is useful near `P=pi D`; at the disk it is exact.

### Proof

Translate the center of symmetry to the origin.  Since `S=-S` and `diam(S)=D`, every
`x in S` satisfies

```math
2|x|=|x-(-x)|\le D,
```

so

```math
S\subseteq B(0,D/2).
\tag{2.2}
```

Let `h(theta)` be the support function of `S`.  Central symmetry makes `h`
`pi`-periodic.  At almost every direction `theta` the support point is unique and has
the standard support-coordinate form

```math
x(\theta)=h(\theta)u(\theta)+h'(\theta)u(\theta)^\perp.
```

By (2.2),

```math
h(\theta)^2+h'(\theta)^2\le \frac{D^2}{4}
\qquad\text{for a.e. }\theta.
\tag{2.3}
```

The planar support-function area formula, first for smooth strictly convex
approximants and then by Hausdorff approximation, is

```math
\operatorname{area}S
=
\int_0^\pi
\bigl(h^2-(h')^2\bigr)\,d\theta.
\tag{2.4}
```

Using (2.3),

```math
\operatorname{area}S
\ge
2\int_0^\pi h^2\,d\theta
-\frac{\pi D^2}{4}.
\tag{2.5}
```

Cauchy's width formula and central symmetry give

```math
P=\int_0^\pi w(\theta)\,d\theta
=2\int_0^\pi h(\theta)\,d\theta.
\tag{2.6}
```

Cauchy--Schwarz therefore yields

```math
\int_0^\pi h^2\,d\theta
\ge
\frac1\pi
\left(\int_0^\pi h\,d\theta\right)^2
=
\frac{P^2}{4\pi}.
\tag{2.7}
```

Substitution in (2.5) proves (2.1). `square`

### Audit note on nonsmooth bodies

No differentiability hypothesis is being added to the force hull.  Support functions
of compact convex bodies are Lipschitz; (2.3) holds a.e.  Alternatively, apply the
argument to `S+epsilon B_2`, rescale its diameter if desired, and pass to the limit.
Area, perimeter, and diameter are continuous for planar convex bodies under Hausdorff
convergence.  Thus polygons and degenerate limiting support directions are covered.

---

## 3. Transfer from the central symmetral to the actual force hull

Translate by the full-source circumcenter `o` from FS.4 and set

```math
F_0=F-o,
\qquad
S=\frac12(F_0-F_0).
\tag{3.1}
```

FD already proves exactly

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=P_F,
\tag{3.2}
```

and, with

```math
L_D=\sqrt{D\eta+\eta^2},
\qquad
\eta=3^{1/4}\sqrt D,
```

FS.4 gives

```math
0\le \operatorname{area}S-\operatorname{area}F
\le L_DP_F+\pi L_D^2.
\tag{3.3}
```

Apply Lemma PS.1 to `S` and use (3.3):

### Theorem PS.2 — finite force-hull perimeter-area floor

Every post-ZF source to which FS.4 applies satisfies

```math
\boxed{
\operatorname{area}F
\ge
\frac{P_F^2}{2\pi}-\frac{\pi D^2}{4}
-L_DP_F-\pi L_D^2.
}
\tag{3.4}
```

Since `P_F<=pi D` and `L_D/D=O(D^{-1/4})`, any subsequence with `P_F/D->p` obeys

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
\Psi(p):=\frac{p^2}{2\pi}-\frac\pi4.
}
\tag{3.5}
```

Together with FSDB,

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge A(y,p):=\max\{\Phi(y),\Psi(p)\}.
}
\tag{3.6}
```

This quantitatively strengthens FD: if `p->pi`, then `Psi(p)->pi/4` directly.

---

## 4. Actual-perimeter form of the JC cavity bound

JC retains more information than its printed `pi D-h` relaxation.  Recall

```math
E_{out}=x_B+P_F-q-a,
\qquad
a+e_{BB}\ge q.
\tag{4.1}
```

With `z=Q+2s_Z`, `r_H=2h-q=x_B+z`, and `d_H=q-h`, direct substitution gives

```math
E_{out}+Q
\le P_F-h+e_{BB}-3d_H-2s_Z
\le P_F-h+e_{BB}.
\tag{4.2}
```

JC's outer-walk bound separately gives

```math
E_{out}+Q\le h+e_{BB}.
\tag{4.3}
```

Hence the exact perimeter coupling is

```math
\boxed{
E_{out}+Q
\le e_{BB}+\min\{h,P_F-h\}.
}
\tag{4.4}
```

The same isoperimetric cavity argument used in JC therefore gives, along a convergent
subsequence,

```math
\boxed{
\limsup\frac{G}{D^2}
\le
\frac{(t+m(y,p))^2}{4\pi},
\qquad
m(y,p):=\min\{y,p-y\}.
}
\tag{4.5}
```

The quantity `p-y` is nonnegative by (1.5).

GU gives

```math
\limsup\frac1{D^2}\sum_r\operatorname{area}(P_r)
\le\frac\pi4\lambda^2,
\tag{4.6}
```

so (3.6) implies

```math
\liminf\frac G{D^2}
\ge A(y,p)-\frac\pi4\lambda^2.
\tag{4.7}
```

Since `t<=lambda`, every survivor limit must satisfy the necessary inequality

```math
\boxed{
A(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi},
\qquad
2\rho\le y\le p\le\pi.
}
\tag{4.8}
```

Equivalently,

```math
\boxed{
H(\lambda;y,p):=
(\pi^2+1)\lambda^2
+2m\lambda+m^2
-4\pi A(y,p)
\ge0.
}
\tag{4.9}
```

For fixed `(y,p)`, `H` is strictly increasing in `lambda>=0`; its unique positive
root will be denoted `R(y,p)`.  The root is less than one because `A<=pi/4` and
`H(1)>=1`.

---

## 5. Exact minimization over the force-hull perimeter

For fixed `y`, define the unique crossing perimeter

```math
\boxed{
p_c(y)
:=\sqrt{\frac\pi2\bigl(\pi+y+\sin y\bigr)}.}
\tag{5.1}
```

It is characterized by

```math
\Psi(p_c(y))=\Phi(y).
\tag{5.2}
```

For `0<=y<=pi`,

```math
\Psi(y)-\Phi(y)
\le
\frac{y-\pi-\sin y}{4}
\le0,
```

where `y^2/(2pi)<=y/2` was used.  Also `Phi(y)<=pi/4`.  Hence

```math
y\le p_c(y)\le\pi.
\tag{5.3}
```

For fixed `y`, the root `R` increases with the area input `A` and decreases with the
cavity width `m`:

```math
\frac{\partial R}{\partial A}>0,
\qquad
\frac{\partial R}{\partial m}<0.
\tag{5.4}
```

As `p` increases from `y`, `m=p-y` until `p=2y`, after which `m=y`, while
`Psi(p)` is strictly increasing.

Before `p_c`, the area input is the constant `Phi(y)`, so increasing `p` can only
improve cavity capacity.  After `p_c`, `A=Psi(p)`.  If `p<2y`, differentiation of
(4.9) at its root gives

```math
\frac{\partial H}{\partial p}
=2(R-p-y)<0,
\tag{5.5}
```

because `R<1` while `p+y>=2y>=4rho>1`.  Therefore `dR/dp>0` after the crossing.  If
`p>=2y`, `m` is fixed and the increasing `Psi` again makes `R` increase.

Consequently the minimum over `p in [y,pi]` is exactly

```math
\boxed{
\min_p R(y,p)=
\begin{cases}
R(y,2y),&p_c(y)\ge2y,\\
R(y,p_c(y)),&p_c(y)\le2y.
\end{cases}}
\tag{5.6}
```

When `p_c>2y`, every `p in[2y,p_c]` gives the same root; the choice `2y` is only a
canonical representative of that plateau.

---

## 6. The unique transition density `y_0`

On `[2rho,pi/2]` define

```math
g(y):=\Psi(2y)-\Phi(y).
\tag{6.1}
```

Then

```math
g'(y)=\frac{4y}{\pi}-\frac{1+\cos y}{4}>0
\tag{6.2}
```

throughout this interval.  Indeed `y>1` and `pi<4`, so the first term exceeds one,
while the second is at most one half.

At `y=pi/2`,

```math
g(\pi/2)=\frac{\pi-2}{8}>0.
\tag{6.3}
```

At the left endpoint `g(2rho)<0`.  For an exact elementary sign check, use the same
rational enclosure already used in the FSJC audit,

```math
\frac{739}{1000}<\rho<\frac{37}{50},
\qquad
\frac{157}{50}<\pi<\frac{22}{7}.
\tag{6.4}
```

Since `g` is increasing and `2rho<37/25`, it is enough to bound `g(37/25)`.  Put
`z=pi/2-37/25`.  Then

```math
0<z<\frac{16}{175},
\qquad
\sin(37/25)=\cos z
>1-\frac{z^2}{2}
>\frac{30497}{30625}.
```

Using the lower bound `pi>157/50` in the two places that maximize `g` gives

```math
\boxed{
g(37/25)<-
\frac{338333}{38465000}<0.}
\tag{6.5}
```

Therefore there is a unique

```math
y_0\in(2\rho,\pi/2)
```
with `g(y_0)=0`.  The equation `g(y_0)=0` is exactly (PS.2), and

```math
p_c(y_0)=2y_0.
\tag{6.6}
```

Thus (5.6) uses the first branch for `2rho<=y<=y_0` and the second branch for
`y_0<=y<=pi`.

---

## 7. Exact minimization over the diameter density

### Left branch: `2rho<=y<=y_0`

Here the optimizing perimeter can be taken as `p=2y`, and the threshold root solves

```math
\boxed{
(\pi^2+1)\lambda^2+2y\lambda+y^2
-\pi(y+\sin y)=0.
}
\tag{7.1}
```

The prior FSJC theorem already gives every such threshold
`lambda>=lambda_FSJC>1/2`.  At the root,

```math
\partial_yH
=2\lambda+2y-\pi(1+\cos y).
\tag{7.2}
```

The rational Dottie enclosure in (6.4) gives

```math
\cos y\le\cos(2\rho)=2\rho^2-1<\frac{119}{1250},
```

while `y>=2rho>739/500`.  Hence

```math
2\lambda+2y
>1+\frac{739}{250},
```

and

```math
\pi(1+\cos y)
<\frac{22}{7}\frac{1369}{1250}.
```

The first quantity is strictly larger than the second.  Therefore
`partial_yH>0`.  Since `partial_lambda H>0`, implicit differentiation gives

```math
\boxed{\frac{d\lambda}{dy}<0}
\qquad(2\rho\le y\le y_0).
\tag{7.3}
```

### Right branch: `y_0<=y<=pi`

Here the optimizing perimeter is `p=p_c(y)`, the two area floors are equal, and

```math
m(y)=p_c(y)-y.
\tag{7.4}
```

Differentiating (5.1),

```math
p_c'(y)=\frac{\pi(1+\cos y)}{4p_c(y)}<1
\tag{7.5}
```

on this interval.  One direct bound is `p_c>=y>=2rho`,
`cos y<=cos(2rho)<119/1250`, together with (6.4).  Thus

```math
m'(y)=p_c'(y)-1<0.
\tag{7.6}
```

Along the equality `A=Phi(y)`, the derivative of (4.9) with respect to `y` at fixed
`lambda` is

```math
\frac{dH}{dy}
=2m'(y)(\lambda+m(y))-\pi(1+\cos y)<0.
\tag{7.7}
```

Therefore implicit differentiation gives

```math
\boxed{\frac{d\lambda}{dy}>0}
\qquad(y_0\le y\le\pi).
\tag{7.8}
```

The optimized threshold decreases up to `y_0` and increases after `y_0`.  Hence its
unique global minimum occurs at

```math
(y,p)=(y_0,2y_0).
\tag{7.9}
```

At that point `m=y_0` and `A=Phi(y_0)=Psi(2y_0)`, so (7.1) applies.  Using (PS.2),

```math
\pi(y_0+\sin y_0)=8y_0^2-\pi^2,
```

and (7.1) becomes exactly (PS.3).  Its unique positive root is `lambda_PS`.

This proves the optimization theorem:

### Theorem PS.3 — explicit post-FSJ cavity floor

Every post-ZF survivor limit satisfying the audited FS/FSDB/GU/JC hypotheses obeys

```math
\boxed{\lambda\ge\lambda_{PS}.}
\tag{7.10}
```

Since an arbitrary sequence realizing the liminf of
`(e_BB+2s_C)/D` has a further subsequence on which `(y,p,t)` converge, (7.10) proves
(PS.4).

Finally, `y_0<pi/2` and the left-branch threshold in (7.1) is strictly decreasing in
`y`; at `y=pi/2` its root is exactly `lambda_FSJC`.  Hence

```math
\boxed{\lambda_{PS}>\lambda_{FSJC}}
\tag{7.11}
```

without using decimal approximations.

---

## 8. Exact target implication

The strongest explicit report-level post-ZF pinned/contact lower bound changes from

```math
\lambda\ge0.5882283437736394\ldots
```

to

```math
\boxed{\lambda\ge0.5933612807422635\ldots .}
```

The minimizing geometry is also localized exactly:

```math
\boxed{
\frac hD\to y_0,
\qquad
\frac{P_F}{D}\to2y_0
}
\tag{8.1}
```

for any sequence approaching the new scalar endpoint.  At that endpoint the two
independent force-hull area floors are simultaneously tight:

```math
\Phi(y_0)=\Psi(2y_0).
\tag{8.2}
```

This replaces FDJ's nonexplicit statement by a concrete quantitative subgap and a new
candidate equality geometry.  It does not close the high-`lambda` branch.

---

## 9. Exact remaining lemma

A useful next theorem should attack the new equality geometry rather than merely rerun
the scalar optimizer.

> **PS endpoint incompatibility.** Exclude every unbounded post-ZF survivor sequence
> with
> ```math
> \frac{e_{BB}+2s_C}{D}\to\lambda_{PS},
> \quad
> \frac hD\to y_0,
> \quad
> \frac{P_F}{D}\to2y_0,
> ```
> by combining the equality conditions in Lemma PS.1, FS.4, FSDB, GU, and JC, or
> construct a strict sub-`D` competitor.

If this endpoint is excluded, compactness again yields a positive gap above
`lambda_PS`.  A stronger result would convert the large pinned/contact currency itself
into a contradictory upper bound or the exact face inequality.

---

## 10. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| symmetric area inequality PS.1 | proved | support coordinates + diameter ball + Cauchy--Schwarz |
| force-hull floor `Psi(p)` | proved under FS.4 | central symmetral has same diameter/perimeter and `o(D^2)` area loss |
| actual-perimeter JC form | proved | retain `P_F` in JC.5 instead of replacing it by `pi D` |
| two-parameter necessary inequality (4.8) | proved | PS/FSDB lower gap + GU + JC, with only `t<=lambda` relaxed |
| fixed-`y` optimizer | proved | monotonicity before/after `Psi=Phi` crossing |
| unique global minimizer `(y_0,2y_0)` | proved | exact one-dimensional derivative signs |
| explicit floor `lambda_PS` | proved asymptotically | compact subsequence argument |
| `lambda_PS>lambda_FSJC` | proved exactly | left threshold decreases strictly toward the FSJC endpoint |
| Level I closure | not proved | no universal upper bound on `lambda` |

---

## 11. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | `p->pi`; PS forces disk-scale area, which the shell force hull has; its pinned/contact currency is above the new floor |
| dense isolated shell filling | yes | FS.4 is full-source; the force hull is unchanged and the theorem does not assume a small isolated population |
| Reuleaux constant-width body | yes | PS is applied to the central symmetral, not to an arbitrary constant-width source hull |
| perfect matching | yes | already excluded by MFS; PS does not use that branch closure |
| near-star response with tiny strict minors | yes | no numerical conductance floor or arbitrary operator bound is used |
| low diameter-density DB endpoint | yes | it lies on the decreasing left branch and requires a larger threshold than the unique transition point |

---

## 12. Failed routes and no-go results

1. **Perimeter saturation alone.**  For a nonsymmetric convex body, `P_F/D` near `pi`
   does not force a disk; constant-width noncircular limits remain.  FS.4 is essential
   because it makes the central symmetral area-equivalent to `F`.
2. **Another scalar FSJC iteration.**  Simply inserting a larger constant area floor
   into JC misses the dependence on `P_F`.  The improvement here comes from retaining
   the actual perimeter and optimizing it jointly with `h/D`.
3. **Claiming the new endpoint impossible.**  PS.1 used Cauchy--Schwarz, and equality
   conditions at `(y_0,2y_0)` have not yet been pushed through all of FSDB/GU/JC.  The
   endpoint is therefore retained, not silently excluded.

---

## 13. Literature imported

None.  The support-function identities used in Lemma PS.1 are standard planar convex
geometry and are proved at the level needed here; no external theorem is imported as
a black-box closing step.

---

## 14. Computation and reproducibility

No computation is a proof dependency.  Decimal evaluation of the exact roots gives

```text
rho       = 0.7390851332151606416553120877...
y_0       = 1.4861348981098190445497808940...
2 y_0     = 2.9722697962196380890995617881...
lambda_PS = 0.5933612807422635245852806883...
lambda_FS = 0.5882283437736394387149516349...
difference= 0.0051329369686240858703290534...
```

The theorem is defined by the exact equations (PS.2)--(PS.3), not these decimals.
The rational sign certificate (6.5) is included in the proof, so no floating-point
root finder is required to establish existence, uniqueness, or strict improvement.

---

## 15. Canonical promotion recommendation

**Hold as report pending independent audit.**  If the support-function proof and the
actual-perimeter JC retention survive review, promote PS.2--PS.3 into the post-FS
Target C frontier and replace the printed explicit floor `lambda_FSJC` by
`lambda_PS`.  FDJ remains independently useful because it gives a qualitative strict
gap even without optimizing the quantitative support-function estimate.

The just-landed FDJ report also contains a typographical `rac\pi4` in its displayed
(4.3); that typo does not affect its mathematics and should be repaired separately.

---

## 16. Next run

Audit the PS endpoint equality conditions.  In particular, determine whether equality
in the support-function estimate forces enough concentration of the force-hull support
function to contradict the FSDB diameter-direction polygon, or whether the two lower
bounds can genuinely be simultaneously sharp.  This is the shortest path to a further
strict gap that uses new geometry rather than another free numerical parameter.

---

## 17. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem PS:
For a centrally symmetric planar convex body S of diameter D and perimeter P,
    area(S) >= P^2/(2pi)-pi D^2/4.
With S=(F-F)/2 and FS.4,
    area(F)/D^2 >= Psi(p)-o(1),
    Psi(p)=p^2/(2pi)-pi/4,
    p=per(F)/D.
FSDB independently gives Phi(y)=(y+sin y)/4, y=h/D.
Actual-perimeter JC gives cavity width min{y,p-y}.
Therefore every limit must satisfy
    max{Phi(y),Psi(p)}-pi lambda^2/4
      <=(lambda+min{y,p-y})^2/(4pi),
    2rho<=y<=p<=pi.
The exact optimizer is the unique transition
    p=2y,
    Phi(y)=Psi(2y),
i.e. y=y_0 solves
    8y_0^2=pi^2+pi(y_0+sin y_0).
The resulting positive quadratic root is
    lambda_PS=0.5933612807422635...,
strictly above lambda_FSJC=0.5882283437736394....

Exact endpoint now:
Exclude the PS equality geometry or prove a structural upper bound on
(e_BB+2s_C)/D.

Binding regressions:
odd shells and dense isolate fillings remain valid; no conductance floor or small-isolate
assumption was used.
```
