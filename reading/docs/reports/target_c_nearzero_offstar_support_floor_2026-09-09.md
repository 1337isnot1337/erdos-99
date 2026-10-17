> Generated reading edition · [exact source](../../../docs/reports/target_c_nearzero_offstar_support_floor_2026-09-09.md) · source SHA-256 `ca0445b68a011f41351efa953dbd34017329395b67461eef0fee614a28ed61cd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E22C31AE0AE7","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — OSF: a near-zero beta star still leaves a linear off-star diameter support

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-e43-scalar-stability`  
**Run type:** exact support-count geometry / C66 near-star refinement  
**Target:** Target C C-II, C66 near-zero phase  
**Depends on:** C18 shared-endpoint diameter-angle bound, C65 full diameter visibility, C67 diameter-direction separation, DB diameter-edge density  
**New external literature:** none  
**Computation:** decimal evaluation only

## LEVEL I STATUS

**STILL OPEN.**

C66 says that when `D epsilon ->0`, almost all normalized diameter reaction weight `beta` lies on one star centered at a loaded diameter vertex `z`. This does **not** mean the actual full diameter graph becomes a star.

C18 confines every diameter partner of `z` to an angular interval of width `Theta_D`, where

```math
\Theta_D
=
\frac{
D(5\pi/6-\sqrt3)+4\pi/3+\pi/(2D)
}{D+1},
\tag{OSF.1}
```

and

```math
\Theta_D\to
\theta_\infty:=\frac{5\pi}{6}-\sqrt3
=0.885943070422617\ldots .
\tag{OSF.2}
```

Distinct diameter partners are unit-separated and lie on the circle of radius `D` centered at `z`. Hence their angular separation is at least

```math
\delta_D:=2\arcsin\frac1{2D}.
\tag{OSF.3}
```

Therefore the actual diameter degree of `z` satisfies the finite bound

```math
\boxed{
\deg_H(z)
\le
1+\left\lfloor\frac{\Theta_D}{\delta_D}\right\rfloor.
}
\tag{OSF.4}
```

Since `D delta_D ->1`, asymptotically

```math
\boxed{
\limsup\frac{\deg_H(z)}D
\le\theta_\infty.
}
\tag{OSF.5}
```

DB independently gives

```math
\boxed{
\liminf\frac hD
\ge2\rho
=1.478170266430321\ldots,
}
\tag{OSF.6}
```

where `rho=cos rho`.

Thus **for every loaded vertex** `z`, not only the C66 center,

```math
\boxed{
|E(H)\setminus E_H(z)|
\ge
\left(
2\rho-\frac{5\pi}{6}+\sqrt3-o(1)
\right)D,
}
\tag{OSF.7}
```

with

```math
\boxed{
2\rho-\frac{5\pi}{6}+\sqrt3
=0.592227196007704\ldots .
}
\tag{OSF.8}
```

At the C66 center, all these off-star edges remain actual active diameter constraints with positive relative-interior `beta`, but their **total** beta weight satisfies

```math
\sum_{h\not\ni z}\beta_h
\le\frac{723\pi}{49}D\varepsilon
=o(1).
\tag{OSF.9}
```

Consequently the near-zero phase has at least `0.592227D-o(D)` genuine off-star diameter constraints whose average normalized reaction weight is `o(1/D)`.

This is a hard support-versus-weight separation: the full mixed framework remains linearly two-dimensional even while its mechanical diameter measure collapses to one star.

---

## 1. Star partners occupy one short angular interval

Fix any loaded diameter vertex `z`. Every diameter partner `a` satisfies

```math
|a-z|=D.
```

C18 proves that all such partner rays from `z` lie in one angular interval of width at most `Theta_D` in OSF.1.

For distinct partners `a,b`, source unit separation gives

```math
|a-b|\ge1.
```

Since both lie on the radius-`D` circle around `z`,

```math
|a-b|
=2D\sin\frac{\angle azb}{2}.
```

Therefore

```math
\angle azb
\ge2\arcsin\frac1{2D}
=\delta_D.
\tag{1.1}
```

If `m=deg_H(z)` partner directions lie in an interval of length `Theta_D` and are pairwise separated by at least `delta_D`, then the ordered first and last directions span at least `(m-1)delta_D`. Hence

```math
(m-1)\delta_D\le\Theta_D,
```

which proves OSF.4.

---

## 2. Compare with the global diameter-edge floor

Let

```math
h=|E(H)|.
```

The number of diameter edges not incident to `z` is exactly

```math
h-\deg_H(z).
\tag{2.1}
```

DB gives OSF.6. C18 and `D delta_D->1` give OSF.5. Thus

```math
\begin{aligned}
\liminf\frac{h-\deg_H(z)}D
&\ge
2\rho-\theta_\infty\\
&=
2\rho-\frac{5\pi}{6}+\sqrt3.
\end{aligned}
```

The right side is positive:

```math
2\rho-\theta_\infty
=0.592227196007704\ldots .
```

This proves OSF.7--OSF.8.

No beta weights enter this count.

---

## 3. Insert the C66 weight concentration

For the C66 center `z`, E43R makes the C66 estimate explicit:

```math
\delta_z
:=\sum_{h\not\ni z}\beta_h
\le\frac{723\pi}{49}D\varepsilon.
\tag{3.1}
```

If

```math
D\varepsilon\to0,
```

then

```math
\delta_z=o(1).
```

But OSF gives at least

```math
(c_{OSF}-o(1))D,
\qquad
c_{OSF}:=2\rho-\frac{5\pi}{6}+\sqrt3>0,
```

actual off-star diameter edges.

Because the KKT stress is chosen in the relative interior of the maximal-support polytope, each of these edges has strictly positive beta weight. Their average satisfies

```math
\boxed{
\frac1{|E(H)\setminus E_H(z)|}
\sum_{h\not\ni z}\beta_h
=o(1/D).
}
\tag{OSF.10}
```

No individual upper bound is claimed; the statement is an aggregate support/weight mismatch.

---

## 4. Interaction with NLC and the bridge-hinge rank route

NLC says the same near-zero phase has at most three depth-`D` harmonic response carriers attached to `z`, carrying `D^2-o(D^2)` contact stress.

OSF says the full diameter support simultaneously contains at least `0.592227D-o(D)` off-star diameter edges, even though their total beta mass is `o(1)`.

Thus the remaining branch has the precise shape

```text
weighted mechanics:
    beta mass -> one z-star
    contact stress -> <=3 depth-D harmonic carriers from z

unweighted mixed rigidity:
    >=0.592227D-o(D) actual off-star diameter constraints remain
    all with positive but collectively o(1) beta mass
```

This is exactly the regime where the bridge-hinge interval-rank theorem of PR #126 is relevant: mixed rigidity sees support, not weight. If a long physical bridge trunk lies in one of the NLC carriers, ZHP forces almost one proper-interval diameter blocker per bridge hinge. OSF supplies a linear global reservoir of such tiny-weight off-star constraints.

The missing theorem is geometric: show that the off-star diameter thrackle cannot route `Theta(D)` proper-interval blockers through only the at-most-three depth-`D`, almost-radial NLC carriers without either a forbidden near-equilateral triple or a positive transverse response/stress cost.

---

## 5. Regression audit

- OSF counts actual full diameter edges, not KKT mass.
- A linear number of tiny positive beta weights is allowed; OSF does not by itself contradict C66.
- The star-degree bound uses C18's stronger global angle interval, not merely the elementary `pi/3` shared-endpoint bound.
- The pairwise separation `delta_D` follows directly from unit separation of distinct star partners on the radius-`D` circle.
- The floor applies to every diameter vertex; only OSF.9--OSF.10 use the C66 center.

## 6. Compact handoff

```text
OSF support floor.
For any diameter vertex z, C18 places all diameter partners in an angular interval
Theta_D -> theta_inf=5pi/6-sqrt(3)=0.8859430704....
Distinct partners lie on radius-D circle and are unit-separated, so their angular
spacing is at least delta_D=2 asin(1/(2D)). Hence
    deg_H(z) <= 1+floor(Theta_D/delta_D),
    limsup deg_H(z)/D <= theta_inf.
DB gives h/D>=2rho=1.4781702664.... Therefore
    h-deg_H(z) >=
    (2rho-5pi/6+sqrt(3)-o(1))D
    =(0.5922271960...-o(1))D.
At the C66 center, total beta on these off-star edges is o(1) when D epsilon->0.
So >=0.592227D actual off-star constraints survive with average beta=o(1/D).
Combine with NLC: <=3 depth-D response/stress carriers + linear tiny-weight off-star
mixed constraints. Next target is routing these off-star constraints through the carrier geometry.
```
