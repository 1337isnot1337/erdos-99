> Generated reading edition · [exact source](../../../docs/reports/target_c_rs_symmetric_area_floor_audit_2026-09-10.md) · source SHA-256 `a5b34c81927c513965737cb946352ae1a9fdc99b5611607e0cae4dfeb1664289`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-3FE0E8A48F6B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — audit of the FSRS symmetric-area floor

**Date:** 2026-09-10  
**Repository state:** branch `research/2026-09-10-rs-symmetric-area-floor`, after `72fee161`  
**Run type:** adversarial proof audit  
**Target:** Target C, C-II  
**Audited report:** `target_c_rs_symmetric_area_floor_059214_2026-09-10.md`  
**LEVEL I STATUS:** STILL OPEN

## Audit verdict

The FSRS proof survives this audit.  The strongest audited report-level conclusion is

```math
\liminf\frac{e_{BB}+2s_C}{D}\ge
\lambda_{RS}=0.5921405436062881\ldots,
```

and the exact endpoint is unattainable.  Hence an absolute nonexplicit
`epsilon_RS>0` exists above this explicit base value.

This remains report-level and should not be promoted into the route map without an
independent review of the literature normalization and the projective-gap stability
argument.

## 1. Literature normalization

Rogalski--Saint Raymond Theorem 1 applies to a centrally symmetric compact convex
planar set with area `I`, perimeter `L`, and diameter `D`.  In the paper's half-graph
notation `I=2S` and `L=2l`; the displayed theorem is equivalent to

```math
I\ge \frac\pi{(\pi-2)^2}(L/2-D)^2.
```

The Euclidean disk gives equality and fixes the best constant.  The paper's Problem 2
explicitly asks whether equality implies the disk.  Therefore the main report is
correct not to use equality uniqueness.

## 2. Central-symmetral transfer

For `F_0=F-o` and

```math
S=(F_0+(-F_0))/2=(F-F)/2,
```

Minkowski additivity of widths gives `w_S=w_F` in every direction.  Hence
`diam S=D`, and Cauchy's width formula gives `per S=per F=P` exactly.

FS.4 gives `d_H(F_0,-F_0)<=2L_D`.  Support functions then give
`d_H(F_0,S)<=L_D`.

For the endpoint argument one needs **two-sided** area closeness.  It follows directly
from the Hausdorff estimate:

```math
S\subset F_0+L_DB_2,
\qquad
F_0\subset S+L_DB_2.
```

Since both bodies have perimeter `P`, Steiner's formula yields

```math
\boxed{
|\operatorname{area}S-\operatorname{area}F|
\le P L_D+\pi L_D^2=o(D^2).
}
\tag{A.1}
```

The main report explicitly states the first inclusion/one-sided bound because that is
all the area floor needs; equation (A.1) supplies the symmetric form used later in
Section 6.  Thus the endpoint use is valid, though this two-sided version should be
inserted if the theorem is promoted.

## 3. Two-variable minimization audit

The necessary relaxed inequality is

```math
(\pi^2+1)\lambda^2+2m\lambda+m^2
-4\pi\max\{\Phi(y),\Psi(p)\}\ge0,
```

with

```math
\Phi(y)=(y+\sin y)/4,
\quad
\Psi(p)=\frac\pi{(\pi-2)^2}(p/2-1)^2,
\quad
m=\min\{y,p-y\}.
```

The domain is `2rho<=y<=pi`, `max(2,y)<=p<=pi`.

The crossover

```math
p_c(y)=2+2(\pi-2)\sqrt{\Phi(y)/\pi}
```

is feasible.  For `y>=2`, `Phi(y)-Psi(y)` is concave, positive at `2`, and zero at
`pi`; for `y<2`, `p_c>2>y`.

The fixed-`y` root decreases while `Phi` is active and `m` grows.  Once `Psi` is
active before `p=2y`, differentiating the defining polynomial gives

```math
H_p=2(\lambda+p-y)-4\pi C_{RS}(p/2-1)<0,
```

because `p_c>3`, the root has `lambda<1`, and `C_RS>2`.  Since the polynomial is
increasing in `lambda`, its root increases after the crossover.  Beyond `p=2y`, `m`
is fixed and increasing `Psi` again raises the root.  The fixed-`y` minimizer in the
main report is therefore correct.

Also `p_c'(y)<1`, so `p_c(y)-2y` is strictly decreasing.  The rational bounds already
used in FSJC give `p_c(2rho)>4rho`, while `p_c(pi/2)<pi`; hence there is one
`y_0 in (2rho,pi/2)` with `p_c(y_0)=2y_0`.

On the left of `y_0`, the FSJC root decreases in `y`; on the right,
`n(y)=p_c(y)-y` decreases while `Phi(y)` increases, so the root increases.  Thus the
global minimizer `(y_0,2y_0)` is unique.

The standard-library diagnostic reproduces

```text
rho=0.7390851332151607
y0=1.5100171437629437
p0=3.0200342875258874
Phi(y0)=0.6270426644374163
lambda_RS=0.5921405436062881
lambda_FSJC=0.5882283437736393
explicit_gain=0.0039121998326488
perimeter_mismatch=0.0534858058775636
```

The grid diagnostic is not used as proof.

## 4. Endpoint-relaxation audit

If `L/D->lambda_RS`, uniqueness of the relaxed minimizer forces

```math
h/D\to y_0,
\qquad
P/D\to2y_0.
```

Retaining the exact ZK correction gives a lower gap term

```math
A_0-\frac\pi4(\lambda_{RS}-3\kappa)^2,
\qquad
\kappa=\lim(k/D),
```

while JC gives an upper term `(t+y_0)^2/(4pi)` with `t<=lambda_RS`.
The threshold equation is equality only at `kappa=0,t=lambda_RS`; hence

```math
k/D\to0,
\quad
s_C/D\to0,
\quad
e_{BB}/D\to\lambda_{RS},
\quad
q/D\to y_0.
```

Combining the cell upper bound and JC gap upper bound then forces
`area(F)/D^2->A_0`.  Equation (A.1) gives the same limit for `S`.

No hidden sign reversal occurs in this step: positive `kappa` makes the cell upper
bound smaller and therefore the gap lower bound larger, while `t<lambda_RS` makes the
cavity upper bound smaller.  Both move in the contradictory direction.

## 5. Projective-gap stability audit

Let `gamma_i>=delta_D` be the `h` projective direction gaps and put
`x_i=gamma_i-delta_D`, `E_D=sum x_i`, `M_D=max x_i`.  For

```math
g_D(x)=\sin(\delta_D+x)-\sin\delta_D,
```

strict concavity on `[0,E_D]` and `g_D(0)=0` imply

```math
\sum_i g_D(x_i)
\ge \frac{E_D}{M_D}g_D(M_D)
\ge g_D(E_D).
```

If the area approaches the one-large-gap minimum but `M_D` stays below `E_D` by a
fixed amount, a convergent subsequence gives

```math
\frac{E}{M}\sin M>\sin E,
\qquad 0\le M<E<\pi,
```

because `sin x/x` is strictly decreasing.  This is a fixed positive area defect.
Therefore `M_D/E_D->1`; all nonmaximal excess gap mass tends to zero.

This justifies the perimeter limit

```math
\operatorname{per}(Q_H)/D
\to y_0+2\cos(y_0/2).
```

There is no assumption that every finite gap except one is exactly minimal.
Asymptotic area saturation is enough.

## 6. Containment/equal-area endpoint audit

`Q_H=P_H/2` is contained in `S=(F-F)/2` exactly.  At the endpoint, both normalized
areas tend to the same positive `A_0`.  Since centrally symmetric diameter-one bodies
centered at the origin lie in the radius-`1/2` disk, Blaschke selection applies.
Any Hausdorff limits satisfy `Q_infty subset S_infty` and have equal positive area;
convexity forces equality of the bodies.  Cauchy's formula makes perimeter continuous
under Hausdorff convergence.

Thus the endpoint would require

```math
2y_0=y_0+2\cos(y_0/2).
```

The function `y-2cos(y/2)` is strictly increasing and vanishes at `2rho` because
`rho=cos rho`.  Since `y_0>2rho`, the equality is impossible.

This endpoint contradiction is independent of the open equality-uniqueness problem
for the Rogalski--Saint Raymond inequality.

## 7. Regression audit

- Odd regular shells do not violate the convex inequality or FSDB gap lemma; they fail
the low post-ZF currency endpoint needed to force simultaneous saturation.
- Dense contact-isolated fillings are retained.  No estimate on `n-v` is used.
- No response trace estimate, arbitrary-boundary-data operator norm, hull saturation,
or almost-full-weight diameter matching is assumed.
- The proof uses global-source information exactly at FS.4 and at the post-ZF ZK/JC
package.  These inputs are absent from the shell regressions.

## 8. Remaining gap

The theorem is still a one-sided lower restriction on
`(e_BB+2s_C)/D`.  Level I needs a crossing upper restriction, a finite strict
competitor in the high-surplus branch, or a quantitative structural theorem that
eliminates every remaining value above the new threshold.

The nearest quantitative target is to turn the endpoint perimeter discrepancy

```math
y_0-2\cos(y_0/2)=0.05348580587756\ldots
```

into an explicit area penalty for `Q_H subset S`; this would replace the compactness
`epsilon_RS` by an explicit increment and can then be fed through the exact PC/ZK
ledgers.

## 9. Promotion recommendation

**Hold as report pending independent audit.**  The proof is internally consistent in
this pass, but the result imports a literature theorem and materially changes the
best post-ZF constant.  Promotion should be a separate reviewed commit.
