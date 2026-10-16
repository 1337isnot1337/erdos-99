# Target C-II — shore-balanced atomic gap plus quadratic orbit concentration in the joint energy theorem

**Date:** 2026-09-15  
**Repository base:** `main` through the joint orbit-capacity / phase-energy refinement, plus the shore-balanced atomic-gap theorem on this branch  
**Status:** proof-only low-`t` Type-II strengthening; theorem-state authority unchanged  
**Scope:** full-core/no-container Type-II branch  
**LEVEL I STATUS:** `STILL OPEN`

The current joint orbit-capacity / phase-energy theorem converts a dominant atomic
train orbit into the exact continuum route cost

\[
\Phi(z)=z-6\arcsin(\tanh(z/6))
\]

and, with the old `eta_grid=0.00042` atomic floor and generic dominant-orbit estimate,
proves the safe bound

\[
\liminf {q-k\over D}\ge1.82434.
\]

Two independent improvements can be inserted without changing that local joint-energy
argument:

1. the shore-balance theorem on this branch raises the atomic/all-train floor to
   `2 sqrt(Delta_2)+0.00059`;
2. the full orbit-mass vector gives a stronger quadratic lower bound for the largest
   orbit than `4 Delta_2/C`.

Together with the already-merged joint cost `Phi`, they raise the safe proof-only floor
to

\[
\boxed{\liminf {q-k\over D}\ge1.82439.}
\]

The scalar zero of the resulting one-variable inequality is approximately

\[
1.8243916294\ldots,
\]

but only the round value `1.82439` is claimed.

---

## 1. Updated scalar floor and feasible region

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2=\sqrt{\Delta_2},
\qquad
C_0:=2s_2+0.00059.
\tag{SJ.1}
\]

For a convergent full-core Type-II subsequence write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\qquad
C={T-q/2\over D}.
\]

The shore-balanced atomic theorem and the existing exposed-hull propagation give

\[
\boxed{C\ge C_0.}
\tag{SJ.2}
\]

The audited Section-171 upper envelope is unchanged:

\[
\boxed{
C\le U:={9t\over2}-2\pi-2\delta-{\kappa\over2}.
}
\tag{SJ.3}
\]

Hence

\[
2\delta+{\kappa\over2}
\le R(t),
\qquad
R(t):={9t\over2}-2\pi-C_0.
\tag{SJ.4}
\]

---

## 2. Quadratic concentration of the dominant exact orbit

Let `A=x sigma` be the total absolute atomic train mass.  The audited exposed-hull
inequality gives

\[
A\le C.
\tag{SJ.5}
\]

Group atomic mass by the exact projective orbit

\[
\phi\mapsto\phi+{\pi\over3}\pmod\pi.
\]

Let `M_r` be the absolute train mass in orbit `r`, `E_r` its strict-rhombus crossing
mass, and

\[
M:=\max_r M_r.
\]

The audited orbit decomposition gives

\[
E_r\le {M_r^2\over4},
\qquad
\sum_rE_r=\Delta_2,
\qquad
\sum_rM_r=A.
\tag{SJ.6}
\]

Choose an orbit attaining `M`.  The remaining orbit masses have total `A-M`, so

\[
\sum_{r\ne r_*}M_r^2\le(A-M)^2.
\]

Therefore

\[
\boxed{
4\Delta_2\le M^2+(A-M)^2.
}
\tag{SJ.7}
\]

The already-valid generic estimate

\[
M\ge {4\Delta_2\over A}
\tag{SJ.8}
\]

selects the large quadratic branch in the present low-`t` range.  Indeed
`A^2<8 Delta_2`, so (SJ.8) gives `M>A/2`.  Solving (SJ.7) then yields

\[
\boxed{
M\ge m(A):={A+\sqrt{8\Delta_2-A^2}\over2}.
}
\tag{SJ.9}
\]

For `A>=2s_2`, the function `m` is nonincreasing, because

\[
m'(A)
={1\over2}\left(1-{A\over\sqrt{8\Delta_2-A^2}}\right)\le0.
\]

Since `A<=C`,

\[
\boxed{
M\ge m(C)
={C+\sqrt{8\Delta_2-C^2}\over2}.
}
\tag{SJ.10}

At `C=C_0`, this improves the generic dominant-orbit lower bound by about
`0.00058973` units of train mass per `D`.

---

## 3. Improved outer terminal-occurrence lower bound

Before any route-energy relaxation, the dominant-orbit argument gives the exact
asymptotic lower bound

\[
K\ge
\pi+\delta-t-\kappa-2C+2M
\tag{SJ.11}
\]

for the normalized number of outer terminal occurrences carried by shrinking phase
windows around the dominant orbit.

Insert (SJ.10):

\[
\boxed{
K\ge
\pi+\delta-t-\kappa-C+
\sqrt{8\Delta_2-C^2}.
}
\tag{SJ.12}
\]

Define

\[
g(C):=-C+\sqrt{8\Delta_2-C^2}.
\]

Then

\[
g'(C)=-1-{C\over\sqrt{8\Delta_2-C^2}}<0.
\]

Since `C<=U`, replacing `C` by `U` weakens the lower bound safely:

\[
\boxed{
K\ge K_*:=
\pi+\delta-t-\kappa-U+
\sqrt{8\Delta_2-U^2}.
}
\tag{SJ.13}
\]

Throughout the interval excluded below, `U<1.927<sqrt(8 Delta_2)`, so every square
root is real.

---

## 4. Reuse the exact merged joint route relaxation

The merged joint theorem proves route by route that if `n_i` dominant-orbit outer
occurrences lie on a loaded-hull route of side length `s_i`, phase mismatch cost
`g_i`, and detour `d_i`, then simultaneously

\[
d_i\ge n_i g_i,
\qquad
d_i\ge n_i-s_i.
\]

Its exact convex dual and the round-hull perimeter-measure limit yield

\[
\boxed{
\delta\ge\Phi(K),
\qquad
\Phi(z):=z-6\arcsin(\tanh(z/6)),
}
\tag{SJ.14}
\]

for the relevant range `0<K<3 log 3`.  Since `Phi` is increasing and (SJ.13) is a
lower bound for `K`, every survivor necessarily satisfies

\[
\boxed{
\delta\ge\Phi(K_*(t,\delta,\kappa)).
}
\tag{SJ.15}

No part of the local convex-dual calculation is changed here.

Put

\[
H(t,\delta,\kappa)
:=\Phi(K_*(t,\delta,\kappa))-\delta.
\tag{SJ.16}
\]

A survivor requires `H<=0`.

---

## 5. The feasible triangle still reduces to its detour endpoint

Write

\[
S(U):=\sqrt{8\Delta_2-U^2}.
\]

Because `U>=C_0>2s_2`, one has `U>S(U)`.

Differentiate (SJ.13).  At fixed `t,delta`,

\[
\boxed{
{\partial K_*\over\partial\kappa}
={1\over2}\left({U\over S(U)}-1\right)>0.
}
\tag{SJ.17}
\]

Since `Phi` is increasing, `H` is minimized at

\[
\kappa=0.
\tag{SJ.18}
\]

At fixed `t,kappa`,

\[
\boxed{
{\partial K_*\over\partial\delta}
=3+{2U\over S(U)}.
}
\tag{SJ.19}
\]

For `t<=1.82439`, the largest possible `U` is below `1.927`; consequently

\[
{\partial K_*\over\partial\delta}<5.05.
\tag{SJ.20}
\]

Also

\[
K_*<\pi+\delta-t<1.33
\]

throughout the interval under consideration.  The exact derivative from the merged
joint theorem is

\[
\Phi'(z)=1-\operatorname{sech}(z/6),
\]

so for `K_*<1.33`,

\[
\Phi'(K_*)<0.025.
\]

Thus

\[
{\partial H\over\partial\delta}
=\Phi'(K_*){\partial K_*\over\partial\delta}-1
<5.05(0.025)-1<0.
\tag{SJ.21}
\]

After setting `kappa=0`, the contradiction margin therefore decreases with `delta`.
The weakest feasible point is the largest allowed detour,

\[
\boxed{
\kappa=0,
\qquad
\delta={R(t)\over2},
\qquad
U=C_0.
}
\tag{SJ.22}

---

## 6. One-variable endpoint

At (SJ.22), put

\[
S_0:=\sqrt{8\Delta_2-C_0^2}
\]

and

\[
\boxed{
K_0(t)
:=
\pi+{R(t)\over2}-t-C_0+S_0.
}
\tag{SJ.23}
\]

The scalar contradiction margin is

\[
\boxed{
H_0(t):=\Phi(K_0(t))-{R(t)\over2}.
}
\tag{SJ.24}
\]

Since

\[
K_0'(t)={5\over4},
\]

we have

\[
H_0'(t)
={5\over4}\Phi'(K_0(t))-{9\over4}<0.
\tag{SJ.25}
\]

The high-precision certificate gives

\[
\boxed{
H_0(1.82439)
=3.6173637\times10^{-6}\ldots>0.
}
\tag{SJ.26}
\]

and the scalar zero is bracketed by

\[
\boxed{
1.82439162<t_*<1.82439163.
}
\tag{SJ.27}
\]

Therefore every convergent full-core Type-II survivor with

\[
t\le1.82439
\]

violates the necessary joint orbit-energy inequality.

### Theorem SJ.1 — shore-balanced joint orbit-energy floor

In the stated proof-only full-core Type-II scope,

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.82439.
}
\tag{SJ.28}
\]

---

## 7. Quantitative comparison

The successive scalar roots are

```text
old 0.00042 + sequential F + generic orbit:          1.824281235...
old 0.00042 + joint Phi + generic orbit:             1.824348869...
old 0.00042 + joint Phi + quadratic orbit:           1.824357930...
new 0.00059 + joint Phi + generic orbit:             1.824378912...
new 0.00059 + joint Phi + quadratic orbit:           1.824391629...
new safe theorem constant:                           1.82439
```

The numerical movement is still small, but the two new inputs are upstream and
reusable.  The shore-balance theorem strengthens every argument that depends on the
atomic/all-train gap, while the quadratic orbit estimate strengthens any argument that
needs concentration into one exact `pi/3` orbit.

C-II remains open.  The joint local route relaxation is already exact for its two
inputs, so further progress on this path must add new geometry: bounded-face endpoint
restrictions, correlations between the two outer terminals of one train, or a direct
interaction with the pentagon / signed-penetration / two-sided-diameter-bracing stack.

---

## 8. Audit boundaries

- The only new geometric-combinatorial theorem is the shore-balanced atomic gap
  `eta_grid=0.00059`; its proof retains the old individual shore floor for the
  common-neighbor/transitivity step.
- The quadratic orbit inequality (SJ.7) is elementary nonnegative mass algebra.
- Selection of its large root uses the pre-existing generic dominant-orbit lower bound,
  not an unproved assumption that one orbit has majority mass.
- `A -> C -> U` substitutions are through explicitly nonincreasing/decreasing
  functions and always weaken the claimed lower bound.
- The joint route dual, its `Phi` formula, occurrence multiplicities, and perimeter
  measure limit are imported unchanged from the merged theorem.
- Contact-isolated source points remain outside the positive-contact train ledger and
  are never removed from the full source.
- No theorem-state promotion is requested.
