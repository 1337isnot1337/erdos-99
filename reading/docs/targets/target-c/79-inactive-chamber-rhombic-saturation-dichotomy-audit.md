> Generated reading edition · [exact source](../../../../docs/targets/target-c/79-inactive-chamber-rhombic-saturation-dichotomy-audit.md) · source SHA-256 `a7dc0a2a7a52359fa3f78396dab35e9580ef371bc1d2ccc5ac1aaefbd7651847`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — inactive-chamber / rhombic-saturation dichotomy audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Canonical Section 77 gives much more than a theorem for the explicitly
subquadratic-core branch. Its finite identities hold for every post-ZF C-II survivor:

$$
a_0N_F=A_F+O(D),
\qquad
a_0Z_{ch}=A_{ch}+O(D),
\qquad
P_{ch}=O(D),
\tag{79.1}
$$

where

- `a_0=sqrt(3)/2`;
- `A_F=area(F)` is the actual force-hull area;
- `N_F` is the full source population in `F`;
- `m` is the population of the nonisolated positive-contact core;
- `Z_ch=N_F-m` is the contact-isolated population assigned to inactive chambers;
- `A_4` is the total area of bounded quadrilateral contact faces;
- `A_ch=A_F-A_4` is the total inactive-chamber area; and
- `P_ch<=13*pi*D` is the summed chamber perimeter.

This section extracts the global dichotomy implicit in those identities.

> Along every unbounded survivor subsequence, either one actual inactive chamber has
> quadratic area and quadratic contact-isolated population, or the strict-rhombus
> faces fill the force hull in area to `o(D^2)` and the positive KKT core contains
> asymptotically every source point lying in the force hull.

Thus the live problem no longer has a third regime consisting of a positive-density
core plus a diffuse positive-density inactive cloud spread among only submacroscopic
chambers.

The theorem is full-source: no isolated point is discarded. Canonical Section 78 is
not needed for the dichotomy, but it becomes the natural local refinement of the
rhombic-saturation side.

---

# 79. Macroscopic inactive chamber or force-hull rhombic saturation

Retain the notation of canonical Sections 67, 68, and 77. In particular

$$
Z_{ch}=N_F-m,
\qquad
A_{ch}=A_F-A_4.
\tag{79.2}
$$

Canonical Section 77 proves the finite boundary-order relation

$$
\boxed{
a_0Z_{ch}=A_{ch}+O(D).
}
\tag{79.3}
$$

The implied constant is absolute over the post-ZF class. It also proves

$$
\boxed{
P_{ch}:=\sum_j P_j\le13\pi D,
}
\tag{79.4}
$$

where `C_j` are the actual convex inactive chambers, `P_j=per(C_j)`, and
`A_j=area(C_j)`.

## 79.1 Any quadratic inactive population concentrates in one chamber

Let

$$
A_{max}:=\max_jA_j.
$$

For every chamber, the planar isoperimetric inequality gives

$$
\sqrt{A_j}\le{P_j\over2\sqrt\pi}.
$$

Hence

$$
\sum_j\sqrt{A_j}
\le{P_{ch}\over2\sqrt\pi}
\le{13\sqrt\pi\over2}D.
\tag{79.5}
$$

Since

$$
A_{ch}=\sum_jA_j
\le\sqrt{A_{max}}\sum_j\sqrt{A_j},
$$

we obtain the finite concentration estimate

$$
\boxed{
A_{max}
\ge {4A_{ch}^2\over169\pi D^2}.
}
\tag{79.6}
$$

Now suppose along a subsequence that for some fixed `zeta>0`,

$$
Z_{ch}\ge\zeta D^2.
\tag{79.7}
$$

Equation (79.3) gives

$$
A_{ch}\ge a_0\zeta D^2-O(D).
$$

Substitution in (79.6) yields

$$
\boxed{
\liminf {A_{max}\over D^2}
\ge {4a_0^2\zeta^2\over169\pi}>0.
}
\tag{79.8}
$$

Choose a chamber `C_*` attaining `A_max`. Canonical Section 77 also gives total
isolate-only Oler slack `sum_j sigma_j=O(D)`, so `sigma_*=O(D)`. Therefore

$$
z_*={A_{max}\over a_0}+{P_*\over2}+1-\sigma_*
={A_{max}\over a_0}+O(D),
\tag{79.9}
$$

and hence

$$
\boxed{z_*=\Omega(D^2).}
\tag{79.10}
$$

Thus **any** quadratic inactive population in the force hull, not only the special
branch `m=o(D^2)`, forces one actual macroscopic inactive chamber.

## 79.2 Absence of a macroscopic chamber forces `Z_ch=o(D^2)`

Conversely suppose an unbounded subsequence has no macroscopic inactive chamber:

$$
A_{max}=o(D^2).
\tag{79.11}
$$

Then (79.5) gives

$$
A_{ch}
\le\sqrt{A_{max}}\,{13\sqrt\pi\over2}D
=o(D^2).
\tag{79.12}
$$

Equation (79.3) immediately yields

$$
\boxed{Z_{ch}=o(D^2).}
\tag{79.13}
$$

Since `Z_ch=N_F-m`,

$$
\boxed{m=N_F-o(D^2).}
\tag{79.14}
$$

Canonical Section 77's force-hull population saturation is

$$
a_0N_F=A_F+O(D).
\tag{79.15}
$$

Therefore

$$
\boxed{a_0m=A_F-o(D^2).}
\tag{79.16}
$$

This already shows that, in the no-macroscopic-chamber branch, the positive KKT core
itself saturates the force-hull area at the leading packing density.

## 79.3 Strict rhombi then fill the force hull in area

Canonical Section 67 gives the exact face count

$$
\boxed{m=R_4+f+q-k+1,}
\tag{79.17}
$$

where `R_4` is the number of bounded quadrilateral contact faces, `f` the number of
bounded nonquadrilateral faces, and `k=d_H+s_Z`.

Every correction in (79.17) is boundary order:

$$
q=O(D),
\qquad
f=O(D),
\qquad
k=O(D).
\tag{79.18}
$$

Hence

$$
\boxed{R_4=m+O(D).}
\tag{79.19}
$$

Every quadrilateral face is a strict unit rhombus. Write

$$
A_4=a_0R_4+E_4,
\tag{79.20}
$$

where canonical Section 68 gives

$$
E_4=O(D).
\tag{79.21}
$$

Combining (79.16), (79.19), and (79.21),

$$
\boxed{
A_4=A_F-o(D^2).
}
\tag{79.22}
$$

Equivalently,

$$
\boxed{A_{ch}=A_F-A_4=o(D^2),}
\tag{79.23}
$$

now obtained directly from the positive-core/rhombus ledgers as well.

Thus the no-macroscopic-chamber branch is a genuine **rhombic-saturation branch**:
strict quadrilateral contact faces occupy all but `o(D^2)` of the force-hull area.

Canonical `C-FS-STABILITY` supplies

$$
\liminf {A_F\over D^2}
\ge
A_{SC}:={2\rho+\sin(2\rho)\over4}>0,
\qquad \rho=\cos\rho.
\tag{79.24}
$$

Therefore (79.16) and (79.22) also give the explicit leading floors

$$
\boxed{
\liminf {m\over D^2}
\ge {A_{SC}\over a_0},
\qquad
\liminf {R_4\over D^2}
\ge {A_{SC}\over a_0}.
}
\tag{79.25}
$$

Numerically `A_SC/a_0=0.714148...`, but the exact expression is the theorem.

## 79.4 Phase cuts preserve the area saturation

Fix `epsilon in (0,pi/6)`. Canonical Section 69 deletes only

$$
|F_\epsilon|=O_\epsilon(D)
\tag{79.26}
$$

strict rhombi to obtain `epsilon`-coherent physical grains. Every deleted unit rhombus
has area at most one, so the retained grain union has area

$$
A_{ret}=A_4-O_\epsilon(D).
\tag{79.27}
$$

In the no-macroscopic-chamber branch, (79.22) gives

$$
\boxed{
A_{ret}=A_F-o(D^2).
}
\tag{79.28}
$$

Thus the coherent physical grains produced by Section 69 fill the force hull in area
to leading order. The total physical grain perimeter remains

$$
\sum_jP_j=O_\epsilon(D).
\tag{79.29}
$$

This is stronger than the earlier statement that one quadratic coherent grain exists.
For each fixed `epsilon`, all but `o(D^2)` of the force-hull area is carried by a
finite-perimeter polycrystalline family of `epsilon`-coherent strict-rhombus grains.

There is also a quantitative small-grain tail. Let `R_j` be the retained rhombus
counts and suppose `R_j<eta D^2` for grains in a set `S_eta`. Section 69 gives

$$
2\sqrt{\pi a_0}\sum_j\sqrt{R_j}=O_\epsilon(D).
$$

Therefore

$$
\sum_{j\in S_\eta}R_j
\le\sqrt\eta D\sum_j\sqrt{R_j}
=O_\epsilon(\sqrt\eta\,D^2).
\tag{79.30}
$$

So, after first fixing `epsilon` and then choosing `eta` small, finitely many
macroscopic coherent grains carry all but an arbitrarily small fraction of the
rhombic mass.

## 79.5 Exact global dichotomy

Every unbounded post-ZF C-II survivor sequence has, after passage to a subsequence,
one of the following two forms.

### Branch A — macroscopic inactive chamber

There is one actual convex inactive chamber `C_*` with

$$
\boxed{
area(C_*)=\Omega(D^2),
\qquad
z_*=\Omega(D^2),
\qquad
per(C_*)=O(D),
\qquad
\sigma_*=O(D).
}
\tag{79.31}
$$

Every point counted by `z_*` is an actual contact-isolated source point. This branch
includes canonical Section 77's entire `m=o(D^2)` regime, but it can also occur when
the positive core itself is quadratic.

### Branch B — rhombic force-hull saturation

$$
\boxed{
Z_{ch}=o(D^2),
\quad
m=N_F-o(D^2),
\quad
A_4=A_F-o(D^2),
}
\tag{79.32}
$$

and, for every fixed `epsilon in (0,pi/6)`, the Section-69 coherent physical grains
cover `F` up to `o(D^2)` area while having total perimeter `O_epsilon(D)`.

This eliminates the formerly possible intermediate picture

```text
quadratic positive core
+ quadratic inactive population
+ all inactive chambers submacroscopic.
```

Such a diffuse quadratic inactive population is impossible because the chamber
perimeter budget forces concentration.

## 79.6 Interaction with canonical Section 78

Section 78 is not a dependency of Sections 79.1--79.5. It gives a useful refinement
inside Branch B: after deleting only `O(D)` loaded-touching rhombi from one quadratic
coherent grain, one quadratic coherent subgrain lies inside one harmonic attachment
cell `P_*`, and the Section-76 complete-grid diameter inequality localizes to
`diam(P_*)`.

The combined quadratic-side normal form is therefore:

```text
no macroscopic inactive chamber
 -> rhombi fill F in area to o(D^2)
 -> fixed-epsilon coherent grains fill F to o(D^2)
 -> finitely many macroscopic grains carry asymptotically all rhombic mass
 -> one quadratic coherent subgrain lies in one harmonic cell P_*
 -> complete-grid diameter budget localizes to diam(P_*).
```

This still does not settle C-II. The remaining rhombic-saturation obstruction is a
second-order coverage/aggregation or source-preserving deformation theorem for these
macroscopic coherent grains. The chamber branch separately needs a boundary/minimality
coupling theorem; density alone is insufficient because a near-triangular packing can
avoid exact unit contacts by arbitrarily small perturbations.

## 79.7 Dependency audit

- **Canonical Section 77 / `C-INACTIVE-CHAMBER`:** (79.1)--(79.4), including exact
  chamber partition, population saturation, total chamber perimeter, and Oler slack.
- **Canonical Section 67 / `C-RHOMBUS-POP`:** exact face count (79.17).
- **Canonical Section 68 / `C-PUNCTURED-PHASE`:** `E_4=O(D)` and the boundary-order
  angular-defect/phase-cut machinery.
- **Canonical Section 69 / `C-COHERENT-GRAINS`:** fixed-width coherent physical grain
  decomposition, `O_epsilon(D)` deletion and total perimeter, and square-root grain
  budget.
- **Canonical `C-FS-STABILITY`:** positive force-hull area floor used only for the
  explicit density lower bound (79.25).
- **Canonical Section 78 / `C-HARMONIC-GRID-LOCAL`:** not used to prove the dichotomy;
  used only in the handoff.
- **Contact isolates:** explicitly retained and counted in Branch A.

**Status:** canonical as `C-INACTIVE-DICHOTOMY`; see `docs/state/theorem-state.yaml` for lifecycle authority. C-II remains open.
