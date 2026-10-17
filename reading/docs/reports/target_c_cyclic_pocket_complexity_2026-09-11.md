> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_pocket_complexity_2026-09-11.md) · source SHA-256 `20ef31a6ac211d493abea8a674aa381da1bd7d9ef0a560e096e18d4eaf1cc837`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-7EA43AA25AF7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic pocket complexity after the exceptional-face floor

**Date:** 2026-09-11  
**Repository state:** remote main `643a06bc28354ec06167a7b8529129640bb689ad`  
**Run type:** closing-proof attempt / exact cyclic boundary synthesis  
**Target:** Target C, C-II, cyclic `s_Z=d_H=0` branch  
**External web search:** used only to check public status; no theorem imported  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The new result below couples the outer-pocket degree excess to the same loaded-loaded
contact currency that pays the cyclic exceptional-face defect.  It does not eliminate
the cyclic branch.  Its endpoint consequence is nevertheless exact: at the formal
`0.9955405...` atomic lower endpoint, all but `o(D)` outer pockets are triangular in
the graph-boundary sense.  The remaining obstruction is a family of nearly straight
boundary chains whose extra equilibrium contacts may have vanishing, but positive,
selected-stress coefficients.

## 1. Starting endpoint

The promoted and report-level cyclic inputs are:

* the cyclic identities `q=x_B+Q`, `b+Q=2q` and `b/D -> pi`;
* the outer-pocket identities
  `a+e_BB >= q` and
  `x_B=a+sum_P(k_P-3)`, where `a` is the number of missing force-hull sides and
  `k_P>=3` is the graph-boundary degree of the corresponding pocket;
* the report-level universal cyclic defect floor
  `Q/D >= (4/5)sqrt(pi/(2sqrt(3)))`;
* the atomic endpoint inequality for
  `nu=(e_BB+2s_C)/D`.

The hoped-for closing implication was

```text
linear missing-side pockets + full positive equilibrium
    -> a uniform boundary/area cost
    -> contradiction with cyclic force-hull saturation.
```

The uniform cost implication is false with the presently available hypotheses.

## 2. New exact theorem

### Theorem CP — pocket degree excess is paid by loaded-loaded surplus

Let a post-ZF fully force-visible source satisfy the outer-pocket identities above,
and write `d_H` for the loaded diameter-graph defect and `s_Z` for the mixed-rank
surplus.  Then

```math
\boxed{
 0\le \sum_P(k_P-3)
 \le e_{BB}-Q-2d_H-2s_Z.
}
\tag{CP.1}
```

In particular,

```math
\boxed{e_{BB}\ge Q+2d_H+2s_Z.}
\tag{CP.2}
```

In the cyclic circuit branch `s_Z=d_H=0`, let
```math
\nu_D=\frac{e_{BB}+2s_C}{D}.
```
If an unbounded sequence has `limsup nu_D <= 1`, then
```math
\boxed{
\liminf\frac aD
\ge
\frac12\left(\pi+\frac45\sqrt{\frac\pi{2\sqrt3}}\right)-1
=0.9517214495\ldots .
}
\tag{CP.3}
```

If, more specifically, `nu_D -> lambda_A`, where
```math
\lambda_A=
\frac{\pi}{\sqrt{\pi^2+(5/4-\sqrt{\pi/(2\sqrt3)})^2}},
```
then
```math
\boxed{
\frac QD\to\lambda_A,
\qquad
\frac{e_{BB}}D\to\lambda_A,
\qquad
\frac1D\sum_P(k_P-3)\to0.
}
\tag{CP.4}
```
Thus all but `o(D)` of the `a=Theta(D)` pockets have `k_P=3` at that endpoint.

### Proof

The exact outer-pocket decomposition gives
```math
x_B=a+\sum_P(k_P-3).
\tag{CP.5}
```
The missing-side/contact coupling gives `a>=q-e_{BB}`.  The exact post-ZF
terminal partition is
```math
q=x_B+Q+2d_H+2s_Z.
\tag{CP.6}
```
Therefore
```math
\begin{aligned}
\sum_P(k_P-3)
&=x_B-a\\
&\le x_B-(q-e_{BB})\\
&=e_{BB}-Q-2d_H-2s_Z.
\end{aligned}
```
The left side is nonnegative, proving (CP.1) and (CP.2).

Now assume the cyclic branch.  Its identities give
```math
q=x_B+Q,
\qquad b+Q=2q,
\qquad b/D\to\pi.
\tag{CP.7}
```
Writing `xi=Q/D`, (CP.7) gives
```math
\frac qD\to\frac{\pi+\xi}{2}.
\tag{CP.8}
```
Since `a>=q-e_{BB}`, `e_{BB}<=e_{BB}+2s_C=nu_D D`, and the cyclic exceptional-face
floor gives `liminf xi >= (4/5)sqrt(pi/(2sqrt(3)))`, (CP.3) follows.

For (CP.4), use the atomic endpoint inequalities.  In the notation of the cyclic
atomic report, `w=xi-phi` satisfies
```math
w\ge\pi\sqrt{1-\nu^2},
\qquad
\nu\ge\frac45\left(w+\sqrt{r_{\min}(w)}\right),
\tag{CP.9}
```
where
```math
r_{\min}(w)=\frac{\pi^2-w^2}{2\pi\sqrt3}.
```
For `0<=w<=1`, the right side of the second inequality is increasing in `w`.
Consequently every limit with `nu<1` satisfies
```math
\xi\ge \frac45\left(
\pi\sqrt{1-\nu^2}+\nu\sqrt{\frac\pi{2\sqrt3}}
\right).
\tag{CP.10}
```
At `nu=lambda_A` the right side equals `lambda_A` by the defining equation for
`lambda_A`.  On the other hand, always
```math
\xi=\lim Q/D\le\lim e_{BB}/D\le\lim\nu_D=\lambda_A.
\tag{CP.11}
```
Hence `xi->lambda_A`.  The two inequalities
`Q<=e_{BB}<=e_{BB}+2s_C` then force `e_{BB}/D->lambda_A` as well.  Apply (CP.1)
with `d_H=s_Z=0` to get
```math
0\le D^{-1}\sum_P(k_P-3)
\le e_{BB}/D-Q/D\to0.
```
Since the summands are nonnegative integers, only `o(D)` pockets can have
`k_P>3`.  This proves (CP.4).  $`\square`$

## 3. Exact endpoint obstruction exposed by CP

At `nu_D -> lambda_A`, CP and the cyclic identities imply
```math
\frac aD\to\frac{\pi-\lambda_A}{2}>1,
\qquad
\frac{x_B}D\to\frac{\pi-\lambda_A}{2}.
\tag{CP.12}
```
Thus the formal endpoint consists asymptotically of a linear number of triangular
outer pockets and no linear graph-boundary degree surplus.  The outer-walk saturation
`b-P_F=o(D)` further says that the aggregate path-versus-hull-chord detour of these
pockets is `o(D)`.

This does not itself contradict full force visibility.  At an internal vertex of a
boundary chain of **degree three**, exact collinearity of the two chain edges is
incompatible with a strictly positive equilibrium coefficient on the third contact
edge: if the two unit contact vectors are `u` and `-u`, then force balance with
positive coefficients `alpha,beta,gamma` would read
```math
(alpha-beta)u+gamma w=0,
```
forcing `gamma=0` whenever the third unit vector `w` is not parallel to `u`.
Near-straight degree-three chains already give the binding escape.  Take the two
chain rays at directions `0` and `pi-epsilon`, and the third ray at `3pi/2`.  For
small positive `epsilon`, the three cyclic angular gaps are
`pi-epsilon`, `pi/2+epsilon`, and `pi/2`; all exceed `pi/3`, so the local star is
triangle-free.  The unique positive equilibrium coefficients are proportional to
the sines of the opposite gaps, and the coefficient of the third ray is
`sin(epsilon)`, tending to zero.  Thus the boundary chain can approach exact
collinearity while every finite member still has a positive selected stress.  The
C-II normalization supplies no uniform positive lower bound on that coefficient.
This is the local form of the thin oblique-rhombic boundary-strip regression.

Therefore CP narrows the endpoint but does not produce the missing uniform cost.

## 4. Scope and dependencies

The theorem concerns the actual fully force-visible global-minimizer representative;
it does not replace it by a scaffold or a smaller optimum.  It retains loaded and
unloaded vertices exactly as in the C-II notation.  It uses only the following
report-level inputs:

* `target_c_outer_pocket_count_coupling_2026-09-09.md` (PC.2 and PC.4);
* the exact post-ZF terminal partition `q=x_B+Q+2d_H+2s_Z`;
* `target_c_attachment_perimeter_and_cyclic_exceptional_floor_2026-09-11.md`
  (the universal cyclic Q floor);
* `target_c_cyclic_atomic_endpoint_incidence_2026-09-10.md` (CP.9).

No claim here uses the unpromoted C56 kernel-collapse package, a pure-disk transport
through exceptional faces, or an individual stress lower bound.

## 5. Failed closure and exact remaining lemma

The tempting implication
```math
\text{CP.4 + }b-P_F=o(D)
\Longrightarrow\text{a fixed positive area/stress cost per pocket}
```
is not proved and is false if interpreted as a local geometric statement.  Near-
straight oblique-rhombic boundary strips realize the required limiting local geometry
with positive stresses whose third-edge coefficients tend to zero.

The decisive missing theorem would have to be global:

> **Uniform endpoint transport.**  In a cyclic C-II global minimizer, a linear family
> of near-straight triangular outer pockets must either carry a uniform aggregate
> positive KKT stress/reaction cost, or yield a strict smaller-diameter packing.

That statement is still absent.  CP therefore does not close the cyclic branch, and
the forest `s_Z=0` and positive `s_Z` branches remain untouched.

## 6. Audit classification

| Claim | Classification | Reason |
|---|---|---|
| CP.1--CP.2 | proved | exact combination of PC.2, PC.4, and the post-ZF partition |
| CP.3 | proved, report-level | uses the unpromoted cyclic Q floor and cyclic perimeter identities |
| CP.4 | proved, report-level | equality squeezing in the atomic endpoint inequalities |
| exact straight degree-three equilibrium obstruction | proved | direct force-balance calculation |
| near-straight chains have a uniform positive cost | rejected | vanishing third-edge stress / oblique-rhombic regression |
| cyclic C-II branch closed | not proved | CP leaves the weak-stress boundary family |
| Level I | still open | all C-II branches and global quantifiers remain |

## 7. Promotion recommendation

**Hold as report.**  The theorem is a useful exact synthesis, but it depends on
unpromoted September 10--11 inputs and does not close the route.

## 8. Compact handoff

```text
New exact synthesis (cyclic C-II):
    0 <= sum_P(k_P-3) <= e_BB-Q-2d_H-2s_Z.

In the cyclic circuit branch, if nu=(e_BB+2s_C)/D <= 1 along a sequence, then
    liminf a/D >= (pi + (4/5)sqrt(pi/(2sqrt3)))/2 - 1
                 = 0.9517214495...

At the formal atomic endpoint nu -> lambda_A=0.99554058458...,
    Q/D -> lambda_A,
    e_BB/D -> lambda_A,
    sum_P(k_P-3)=o(D),
so all but o(D) of the linear number of outer pockets are triangular.

The exact remaining obstruction is a linear family of nearly straight triangular
boundary chains. Exact straight degree-three equilibrium is impossible, but the
third positive stress may tend to zero; no uniform lower bound is available.
Forest s_Z=0 and s_Z>0 remain open.
```
