# Target C-II — near-floor survivors force linear dominant double-outer trains

**Date:** 2026-09-15  
**Status:** proof-only structural consequence  
**Scope:** full-core Type-II branch with the corrected `g=0.0053` matched atomic floor  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The corrected phase-star / energy-restored incidence stack gives more than the scalar
floor `t=(q-k)/D>=1.84289`.  In the narrow post-floor window

\[
\boxed{t\le1.843,}
\]

the dominant exact three-phase train orbit is forced to put two selected outer
terminal occurrences on a linear family of complete trains.

Precisely, after freezing shrinking windows around the dominant exact `pi/3` orbit,
let `H_D` be the number of dominant-window complete trains whose two terminal face
incidences are both selected outer occurrences in the joint-retention construction.
Then every survivor sequence in the stated window satisfies

\[
\boxed{
\liminf {H_D\over D}>0.3025.
}
\tag{DO.1}

This is a source-level boundary-order statement, not another carrier decimal.  It says
that more than `0.3025D` complete trains in one exact three-direction orbit run from
the outer contact walk back to the outer contact walk.

---

## 1. Audited inputs

Use

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\delta={d_{out}\over D},
\]

\[
U={9t\over2}-2\pi-2\delta-\kappa/2,
\tag{DO.2}

and

\[
C_{53}=2\sqrt{\Delta_2}+0.0053,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{DO.3}

The corrected matched phase-star theorem gives

\[
U\ge C_{53}.
\tag{DO.4}

Put

\[
m_2(U)={U+\sqrt{8\Delta_2-U^2}\over2},
\qquad
r(U)=U-m_2(U).
\tag{DO.5}

The joint-retention / rhombus-incidence / disjoint-energy stack gives retained dominant
outer-occurrence mass `z` and retained complement outer-to-outer pair mass `p` with

\[
z+p\ge S(t,\delta,\kappa)-o(1),
\tag{DO.6}

where

\[
S(t,\delta,\kappa)
=\pi-U-{t+\kappa\over2}+m_2(U),
\tag{DO.7}

and

\[
p\le
{\delta-F(z)+r(U)^2\over2(1-\delta)}+o(1),
\qquad
F(z)=z-6\sin(z/6).
\tag{DO.8}

The dominant selected edges are actual disjoint outer-edge occurrences, so their
energy is a subset of the total outer detour:

\[
\boxed{\delta\ge F(z)-o(1).}
\tag{DO.9}

---

## 2. Uniform endpoint envelopes for `t<=1.843`

Let

\[
T_0=1.843,
\qquad
U_{max}={9T_0\over2}-2\pi.
\tag{DO.10}

Since `delta,kappa>=0`, every source with `t<=T0` has

\[
U\le U_{max}.
\tag{DO.11}

Combining this with `U>=C53`,

\[
\delta\le
\delta_{max}:={U_{max}-C_{53}\over2}
<0.05020.
\tag{DO.12}

On `U>=C53>2sqrt(Delta2)`, `m_2'(U)<0`, hence

\[
r'(U)=1-m_2'(U)>0.
\tag{DO.13}

Also, after substituting (DO.2),

\[
S=3\pi-5t+2\delta+m_2(U).
\tag{DO.14}

Thus throughout the relevant interval

\[
{\partial S\over\partial t}
=-5+{9\over2}m_2'(U)<0,
\]

\[
{\partial S\over\partial\delta}
=2-2m_2'(U)>0,
\]

\[
{\partial S\over\partial\kappa}
=-{1\over2}m_2'(U)>0.
\tag{DO.15}

These monotonicities make an explicit lower bootstrap for `z` possible.

---

## 3. One bootstrap step

Suppose a survivor is already known to satisfy

\[
z\ge z_j-o(1).
\tag{DO.16}

By (DO.9) and monotonicity of `F`,

\[
\delta\ge d_j-o(1),
\qquad d_j:=F(z_j).
\tag{DO.17}

Therefore

\[
U\le U_j+o(1),
\qquad
U_j:=U_{max}-2d_j,
\tag{DO.18}

and by (DO.13),

\[
r(U)\le r(U_j)+o(1).
\tag{DO.19}

The monotonicities (DO.15) show that, under `t<=T0`, `delta>=d_j`, and `kappa>=0`,
`S` is minimized at

\[
t=T_0,
\qquad
\delta=d_j,
\qquad
\kappa=0.
\]

Hence

\[
S\ge
S_j-o(1),
\qquad
S_j:=
\pi-U_j-{T_0\over2}+m_2(U_j).
\tag{DO.20}

For the complement pair bound (DO.8), use simultaneously

\[
\delta\le\delta_{max},
\qquad
F(z)\ge F(z_j)=d_j,
\qquad
r(U)\le r(U_j).
\]

This gives the conservative uniform upper bound

\[
p\le P_j+o(1),
\qquad
P_j:={
\delta_{max}-d_j+r(U_j)^2
\over2(1-\delta_{max})}.
\tag{DO.21}

Combining (DO.6), (DO.20), and (DO.21),

\[
\boxed{
z\ge S_j-P_j-o(1).}
\tag{DO.22}

This is the bootstrap map.

---

## 4. Four certified rounds

Start with the trivial `z>=0`.  The exact rational verifier

`research/verify_target_c_dominant_double_outer_trains_2026-09-15.py`

uses Machin bounds for `pi`, integer-square-root enclosures, and alternating-series
bounds for `sin`.  It certifies the following rounded-down implications:

\[
\boxed{
0
\Longrightarrow z>2.0786-o(1),
}
\tag{DO.23}

\[
\boxed{
2.0786
\Longrightarrow z>2.1918-o(1),
}
\tag{DO.24}

\[
\boxed{
2.1918
\Longrightarrow z>2.2101-o(1),
}
\tag{DO.25}

\[
\boxed{
2.2101
\Longrightarrow z>2.2132-o(1).
}
\tag{DO.26}

The smallest numerical margin in these four certified implications is more than
`3.85e-5`.

Therefore every survivor with `t<=1.843` satisfies

\[
\boxed{z>2.2132-o(1).}
\tag{DO.27}

The energy inequality (DO.9) then gives

\[
\delta
\ge F(2.2132)-o(1)
>0.04984862-o(1).
\tag{DO.28}

Substitute back into (DO.2), using `t<=1.843` and `kappa>=0`:

\[
\boxed{
U<1.910618+o(1).
}
\tag{DO.29}

---

## 5. Convert retained occurrences to double-outer trains

Freeze the dominant orbit windows before passing to the finite sources.  Let `M_D` be
the number of complete stopped trains in those windows and let `H_D` be the number of
those trains with two selected outer terminal occurrences.

Every complete stopped train is a path and has exactly two terminal face incidences.
Therefore a dominant-window train outside `H_D` contributes at most one selected outer
terminal occurrence, while a train in `H_D` contributes at most two.  Fractional
joint-retention weights are at most one per occurrence.  Hence the finite retained
weight obeys

\[
z_DD\le M_D+H_D.
\tag{DO.30}

After first taking `D->infinity` and then shrinking the phase windows, the dominant
window train mass is at most the total atomic train mass `A`, and the exposed-hull
inequality gives

\[
M:=\limsup {M_D\over D}
\le A
\le C
\le U.
\tag{DO.31}

Combining (DO.27), (DO.29), (DO.30), and (DO.31),

\[
\liminf {H_D\over D}
\ge2.2132-1.910618
>0.3025.
\]

This proves (DO.1).

---

## 6. What this changes

The current low-`t` obstruction is no longer merely "one dominant atomic orbit carries
most train mass."  In every surviving source with

\[
1.84289\lesssim t\le1.843,
\]

more than `0.3025D` complete trains from that same exact three-phase orbit have both
terminal incidences on the outer contact walk.

This creates a concrete next geometric object:

```text
>0.3025 D dominant-orbit outer-to-outer trains
    + one of only three projective phase directions
    + near-saturated dominant rhombus crossing graph
    + cyclic order of their two outer endpoints on the round loaded hull.
```

A closing theorem can now target the cyclic endpoint order or crossing incidence of
this linear O--O family.  This is stronger than continuing to optimize the scalar
complement mass, which is already nearly zero at the current floor.

**Disposition:** proved proof-only structural narrowing; C-II and Level I remain open.
