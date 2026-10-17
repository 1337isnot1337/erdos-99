# Target C-II — `g=0.0050` propagation through complement outer-train bracing energy

**Date:** 2026-09-15  
**Status:** proof-only low-`t` Type-II strengthening; theorem-state authority unchanged  
**Scope:** same full-core/no-container Type-II scope as `target_c_complement_outer_train_bracing_energy_2026-09-15.md`  
**LEVEL I STATUS:** `STILL OPEN`

The complement outer-train bracing theorem on current `main` is symbolic in the lower bound

\[
C_0\le C={T-q/2\over D}.
\]

Its first numerical instantiation still used the older conservative value

\[
C_0=2\sqrt{\Delta_2}+0.00042,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and obtained

\[
{q-k\over D}\ge1.82806-o(1).
\]

The now-merged hostile-audited iterative-pruning theorem proves the stronger matched all-train/rhombic input

\[
\boxed{
C_0=2\sqrt{\Delta_2}+0.0050.
}
\tag{GCE.1}
\]

Substituting (GCE.1) into the same complement-energy theorem and rechecking its feasible-triangle monotonicity raises the safe floor to

\[
\boxed{
\liminf {q-k\over D}\ge1.82891.
}
\tag{GCE.2}
\]

The scalar crossing is

\[
1.82891235390268043\ldots,
\]

but only `1.82891` is claimed.

C-II remains open.

---

## 1. Inputs

Write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

and

\[
U={9t\over2}-2\pi-2\delta-{\kappa\over2}.
\tag{GCE.3}
\]

The merged `g=0.0050` theorem gives

\[
C_0:=2\sqrt{\Delta_2}+0.0050
\le C.
\tag{GCE.4}
\]

Section 171 gives `C<=U`, hence

\[
2\delta+{\kappa\over2}
\le R_{50}(t):={9t\over2}-2\pi-C_0.
\tag{GCE.5}
\]

All orbit atomization, outer-occurrence, two-sided bracing, near-antipodal capacity, and phase-sector arguments are unchanged from the current-main complement-energy theorem. In particular its scalar obstruction remains

\[
\delta\ge F(z_*)+J(p_*),
\tag{GCE.6}
\]

with

\[
F(z)=z-6\sin(z/6),
\qquad
J(p)=2p-6\sin(p/3),
\tag{GCE.7}
\]

\[
z_*=
\pi-t-\kappa-2U+{8\Delta_2\over U},
\tag{GCE.8}
\]

and

\[
p_*=
\left[
\pi-Q(\delta)-U-{t+\kappa\over2}+{4\Delta_2\over U}
\right]_+,
\tag{GCE.9}
\]

where `Q=Phi^{-1}` for

\[
\Phi(q)=q-6\arcsin(\tanh(q/6)).
\tag{GCE.10}
\]

The dominant and complement edge-energy payments remain disjoint because the complement family is taken outside shrinking windows around the dominant atomic orbit.

---

## 2. The worst feasible point is unchanged

The current-main theorem proves symbolically that, at fixed `t,delta`, increasing `kappa` increases both `z_*` and `p_*`. Since `F` and `J` are increasing, the contradiction margin is minimized at

\[
\boxed{\kappa=0.}
\tag{GCE.11}
\]

At fixed `t,kappa`,

\[
{\partial z_*\over\partial\delta}
=4+{16\Delta_2\over U^2},
\tag{GCE.12}
\]

and

\[
-{\partial N_*\over\partial\delta}
=2\left(1+{4\Delta_2\over U^2}\right),
\tag{GCE.13}
\]

where `N_*` is the complement-train count upper bound from the parent theorem.

The stronger lower bound `U>=C0` improves both numerical derivative bounds:

\[
4+{16\Delta_2\over C_0^2}
=7.9790809080\ldots<8,
\tag{GCE.14}
\]

\[
2\left(1+{4\Delta_2\over C_0^2}\right)
=3.9895404540\ldots<4.
\tag{GCE.15}
\]

On the relevant range the parent proof uses

\[
F'(z)<0.025,
\qquad
\Phi'(Q)<0.04,
\qquad
J'(p)>0.041
\quad(p>0.61).
\tag{GCE.16}
\]

The new endpoint certificate checks

\[
Q<1.61,
\qquad
z<1.30,
\qquad
p>0.616,
\tag{GCE.17}
\]

so these bounds apply with slack. In particular

\[
{\partial p_*\over\partial\delta}<-21
\]

and the contradiction-margin derivative satisfies the same coarse strict inequality

\[
{\partial\mathcal M\over\partial\delta}
<0.025(8)-21(0.041)-1
=-1.661<0.
\tag{GCE.18}
\]

Thus the weakest feasible point is again

\[
\boxed{
\kappa=0,
\qquad
\delta={R_{50}(t)\over2},
\qquad
U=C_0.
}
\tag{GCE.19}

---

## 3. One-variable endpoint

At (GCE.19), define

\[
\delta_0(t)={1\over2}\left({9t\over2}-2\pi-C_0\right),
\tag{GCE.20}
\]

\[
z_0(t)=
\pi-t-2C_0+{8\Delta_2\over C_0},
\tag{GCE.21}
\]

\[
N_0(t)=
C_0+{t\over2}-{4\Delta_2\over C_0},
\tag{GCE.22}
\]

\[
p_0(t)=
\pi-Q(\delta_0(t))-N_0(t),
\tag{GCE.23}
\]

and

\[
\boxed{
\mathcal M_{50}(t)
=F(z_0(t))+J(p_0(t))-\delta_0(t).
}
\tag{GCE.24}
\]

A survivor requires

\[
\mathcal M_{50}(t)\le0.
\tag{GCE.25}
\]

The verifier

`research/verify_target_c_complement_outer_train_bracing_energy_g0050.py`

checks at the safe endpoint

\[
\delta_0(1.82891)=0.0186420395462\ldots,
\]

\[
z_0(1.82891)=1.2927088367325\ldots,
\]

\[
Q(\delta_0)=1.6002717323577\ldots,
\]

\[
p_0(1.82891)=0.6168790128034\ldots,
\]

and

\[
\boxed{
\mathcal M_{50}(1.82891)
=1.1858132079\times10^{-5}>0.
}
\tag{GCE.26}
\]

The same certificate brackets the scalar zero by

\[
\boxed{
1.82891235390268043
<t_*<
1.82891235390268044.
}
\tag{GCE.27}
\]

Therefore every proof-only full-core Type-II survivor satisfies (GCE.2).

---

## 4. Relation to the previous floors

The implication chain now carried on `main` plus this branch is

\[
C_0=2\sqrt{\Delta_2}+0.0050
\]

\[
\Longrightarrow
\text{joint dominant-orbit floor }t\ge1.82515-o(1)
\]

\[
\Longrightarrow
\text{dominant/complement outer-energy floor }t\ge1.82891-o(1).
\]

The numerical increment over `1.82806` is not a new geometric theorem. It is the correct propagation of the already-proved stronger atomic input through a theorem that had still been instantiated with the stale `0.00042` constant.

The geometric frontier after this propagation is therefore not further tuning of `C0`. The next useful information must distinguish exact atomic-orbit terminal routing, exploit the ordered parallel-cut subfamilies, or improve the noncrossing near-antipodal capacity lemma.

No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is produced here.

**Disposition:** proof-only strengthening. C-II and Level I remain open.
