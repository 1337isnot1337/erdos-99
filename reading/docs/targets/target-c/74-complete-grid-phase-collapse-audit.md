> Generated reading edition · [exact source](../../../../docs/targets/target-c/74-complete-grid-phase-collapse-audit.md) · source SHA-256 `a20e11a5dea529feb2423ba44b62cc861dc5a781861bdfd183aa47a839ba294f`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C — complete-grid phase-collapse audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module strengthens the proof-only Section 73 grid extraction. A linear-by-linear
phase-pure complete train grid cannot merely be `epsilon`-coherent for fixed epsilon.
The global Section-68 angular-defect budget forces a half-sized complete subgrid whose
**every** rhombus has angular defect `O(1/D)`.

No external theorem is used beyond Section 73's already audited pseudosegment
extraction.

---

# 74. Complete phase-pure grids collapse to inverse-diameter phase width

Work in one physical grain after the canonical Section-68/69 phase cuts. Put

```math
L={\pi\over3}.
```

Every train `v` in the grain has a real phase potential `x_v` in one common real bin
and a label `ell_v in Z/3`, with

```math
\phi_v\equiv x_v+L\ell_v\pmod\pi.
\tag{74.1}
```

For every retained rhombus crossing, Section 68 orients the crossing `u->v` so that

```math
\phi_v-\phi_u\equiv L+\delta_{uv}\pmod\pi,
\qquad
x_v-x_u=\delta_{uv}>0.
\tag{74.2}
```

Here `delta_{uv}` is the acute-angle excess above `pi/3`.

Let `A,B` be the phase-pure complete train families supplied by Section 73. Write

```math
a=|A|,\qquad b=|B|.
```

Every `A` train crosses every `B` train exactly once, while each family is internally
noncrossing.

## 74.1 The crossing orientation is uniform on the complete product

Substitute (74.1) into the first congruence in (74.2) and use the second:

```math
L(\ell_v-\ell_u)+\delta_{uv}
\equiv L+\delta_{uv}\pmod{3L}.
```

Therefore every oriented retained crossing satisfies

```math
\boxed{\ell_v-\ell_u\equiv1\pmod3.}
\tag{74.3}
```

The families `A,B` have two fixed distinct labels. Hence exactly one of the two label
orders occurs on every `A x B` crossing. After interchanging the names if necessary,
we may assume

```math
\ell_B-\ell_A\equiv1\pmod3.
```

Then **every** complete-grid crossing is oriented from `A` to `B` and

```math
\boxed{\delta_{ab}=x_b-x_a>0
\qquad(a\in A,\ b\in B).}
\tag{74.4}
```

In particular

```math
\max_{a\in A}x_a<\min_{b\in B}x_b.
\tag{74.5}
```

This uniform sign is the key extra information supplied by phase purity.

## 74.2 The whole complete grid spends only boundary-order defect

Define

```math
S_{AB}:=\sum_{a\in A}\sum_{b\in B}\delta_{ab}.
\tag{74.6}
```

Every pair `a,b` corresponds to a distinct retained rhombus, so `S_AB` is a sub-sum
of the global strict-rhombus angular defect

```math
\Delta_{train}:=\sum_R\delta_R.
```

Canonical (68.14) gives

```math
{3\Delta_{train}\over\pi}
<(2+\sqrt3)c_0\operatorname{per}(K)
\le(2+\sqrt3)c_0\pi D,
\qquad c_0={\sqrt3\over4}.
```

Hence

```math
\boxed{
S_{AB}\le\Delta_{train}<C_{phase}D,
\qquad
C_{phase}:={\pi^2\sqrt3(2+\sqrt3)\over12}.
}
\tag{74.7}
```

Put

```math
\lambda:={S_{AB}\over ab}.
\tag{74.8}
```

If `a,b>=gamma D` for some fixed `gamma>0`, then

```math
\boxed{
\lambda<{C_{phase}\over\gamma^2D}.
}
\tag{74.9}
```

Thus the mean defect on the complete product is already `O(1/D)`. The next step
upgrades this to a uniform bound on a still-linear complete subgrid.

## 74.3 Half-sized subfamilies have uniformly inverse-D defect

Let

```math
x_A^+:=\max_{a\in A}x_a,
\qquad
x_B^-:=\min_{b\in B}x_b.
```

By (74.5), `x_B^- - x_A^+>0`. Since every pair contributes at least this gap,

```math
\boxed{x_B^- - x_A^+\le\lambda.}
\tag{74.10}
```

Also, for every `a in A` and every `b in B`,

```math
x_b-x_a\ge x_A^+-x_a,
```

so summing gives

```math
{1\over a}\sum_{a\in A}(x_A^+-x_a)\le\lambda.
\tag{74.11}
```

Similarly

```math
{1\over b}\sum_{b\in B}(x_b-x_B^-)\le\lambda.
\tag{74.12}
```

By Markov's inequality there are subfamilies

```math
A_0\subseteq A,
\qquad
B_0\subseteq B,
```

with

```math
|A_0|\ge {a\over2},
\qquad
|B_0|\ge {b\over2},
\tag{74.13}
```

such that

```math
x_A^+-x_a\le2\lambda
\quad(a\in A_0),
\qquad
x_b-x_B^-\le2\lambda
\quad(b\in B_0).
\tag{74.14}
```

For every `a in A_0`, `b in B_0`, combine (74.10) and (74.14):

```math
\begin{aligned}
\delta_{ab}
&=x_b-x_a\\
&=(x_b-x_B^-)+(x_B^--x_A^+)+(x_A^+-x_a)\\
&\le5\lambda.
\end{aligned}
```

Therefore

```math
\boxed{
\delta_{ab}\le {5C_{phase}\over\gamma^2D}
\qquad
(a\in A_0,\ b\in B_0),
}
\tag{74.15}
```

whenever `a,b>=gamma D`.

At the same time, all `A_0` phase potentials lie in an interval of width at most
`2lambda`, and all `B_0` phase potentials lie in an interval of width at most
`2lambda`. Thus each phase family itself collapses from a fixed `epsilon` window to an
`O(1/D)` window.

## 74.4 Quantitative geometric consequence

Every pair in `A_0 x B_0` still crosses, so the subgrid remains complete. Its two
shores satisfy

```math
|A_0|,|B_0|\ge{\gamma\over2}D.
\tag{74.16}
```

Every one of its rhombi has acute angle

```math
\boxed{
{\pi\over3}
<\theta_{ab}
\le {\pi\over3}+{5C_{phase}\over\gamma^2D}.
}
\tag{74.17}
```

Therefore the quadratic-core branch contains an actual linear-by-linear complete grid
that is not merely phase coherent: it is **uniformly inverse-diameter close to the
triangular-lattice angle**.

This is stronger than applying the global average defect estimate to arbitrary
rhombi. The complete-product orientation converts the global `O(D)` defect budget into
uniform control on `Omega(D^2)` specifically organized crossings.

## 74.5 What this does not yet prove

Equation (74.17) does not by itself give a diameter contradiction. The finite train
arcs may still terminate on several boundary components, and Section 74 does not assert
that the `A_0 x B_0` crossings occur in one common order along all trains.

The next theorem should exploit the new scale separation:

```text
linear x linear complete grid
+ every grid rhombus has defect O(1/D)
+ total physical grain boundary O(D)
```

rather than returning to a fixed-width phase argument. Two plausible closing routes
are:

1. prove that crossing-order failures force distinct boundary/interface events and use
   the `O(D)` boundary budget to extract a large common-order subgrid; or
2. derive a diameter lower bound directly from the inverse-D phase-collapsed grid,
   avoiding any disk/common-order reduction.

## 74.6 Dependency audit

- **Section 68:** supplies the exact oriented phase law and global
  `Delta_train=O(D)` bound.
- **Section 69:** places all trains of one physical grain in one lifted phase bin.
- **Section 73:** supplies the phase-pure complete families `A,B` with linear size in
  the quadratic-core branch.
- **Uniform orientation:** follows algebraically from the fixed phase labels via
  (74.3); no topological order assumption is used.
- **No hidden averaging leap:** the half-sized uniform subgrid follows from the exact
  product identity (74.4), the global defect sub-sum, and Markov's inequality.
- **No disk hypothesis:** holes remain allowed throughout.

## 74.7 Compact handoff

```text
Section 73:
    A,B phase-pure complete train grid,
    |A|,|B| >= gamma D.

Section 68 phase law:
    every oriented crossing raises the phase label by 1 mod 3,
    and raises the real potential by exactly delta_e.

Fixed labels on A,B:
    all A x B crossings have the same orientation,
    delta_ab = x_b-x_a > 0.

Global angular defect:
    S_AB=sum_{A x B} delta_ab <= C_phase D.

Let lambda=S_AB/(|A||B|)=O(1/D).
Then half-sized A0,B0 satisfy
    delta_ab <= 5 lambda = O(1/D)
for every a in A0, b in B0.

So the quadratic-core branch contains a complete Omega(D) x Omega(D) grid
whose every rhombus angle is pi/3 + O(1/D).
```
