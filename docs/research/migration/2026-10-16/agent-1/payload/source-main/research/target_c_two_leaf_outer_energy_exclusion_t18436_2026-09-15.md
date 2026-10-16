# Target C-II — two-leaf O--O energy excludes the entire branch `t<=1.8436`

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II exclusion  
**Scope:** full-core/no-macroscopic-container Type-II branch  
**Dependencies:** hostile-audited `g=.0077` residual stability; `t<=1.8436` two-leaf train-mass theorem; phasewise outer-energy bathtub; low-energy cross-phase O--O endpoint theorem; dominant-orbit triangle-free correlation  
**Certificate:** `research/verify_target_c_two_leaf_outer_energy_exclusion_t18436.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current near-frontier stack has two facts that had not been combined tightly enough:

1. residual stability makes the complement population essentially disappear near
   `t=1.8436`, so almost all retained boundary mass must remain in the dominant exact
   three-phase orbit;
2. both leaf phases have train mass below `0.513D`, while their retained boundary mass
   is much larger.

Keeping the residual incidence term instead of using the older coarse bootstrap raises
the phasewise retained-occurrence floor from `0.616D` to more than `0.7179D`.  Hence
**each** leaf phase carries more than `0.2049D` retained O--O pair weight.  The
common-center/triangle-free argument then forces enough pair-weighted leaf terminal
energy that, after adding only the disjoint center-phase one-well energy, the required
outer directional energy exceeds the complete available detour budget.

Therefore no survivor can satisfy

\[
\boxed{t={q-k\over D}\le1.8436.}
\]

Equivalently, at the present proof-only full-core scope,

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.8436.
}
\tag{TE.1}

The contradiction has macroscopic margin, more than `0.0107D` in the final energy
ledger.  It is not a sixth-decimal corner test.

---

## 1. Residual survivor identities near `1.8436`

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
C_{77}=2\sqrt{\Delta_2}+0.0077,
\]

and use the hostile-audited residual variables

\[
t={q-k\over D},
\qquad
x={\kappa\over2},
\qquad
\delta={d_{out}\over D},
\]

\[
h=U_{net}-C_{77},
\qquad c=1.05.
\]

The exact envelope is

\[
\boxed{
2\delta+x+h
=R_t:={9t\over2}-2\pi-C_{77}.
}
\tag{TE.2}

The already-proved `t<=1.8436` localization gives

\[
\boxed{0\le h<0.00013-o(1).}
\tag{TE.3}

Shared routewise retention gives retained dominant outer-occurrence mass `z` and
retained complement O--O pair mass `p` satisfying

\[
\boxed{
z+p
\ge
S:=\pi-{t\over2}-x-ch-o(1).
}
\tag{TE.4}

Let `e_c` be the selected complement terminal-edge directional energy.  The
hostile-audited complement-rhombus incidence theorem and the disjoint dominant/
complement energy split give

\[
\boxed{
p(1-\delta)-{e_c\over2}
\le{c^2h^2\over2}+o(1),}
\tag{TE.5}

\[
\boxed{F(z)+e_c\le\delta+o(1),
\qquad F(z)=z-6\sin(z/6).}
\tag{TE.6}

Consequently, for fixed `z`,

\[
\boxed{
p
\le
{c^2h^2+\delta-F(z)
 \over2(1-\delta)}+o(1),}
\tag{TE.7}

whenever `F(z)<=delta`; otherwise that `z` is itself impossible.

---

## 2. Total retained dominant mass is above `2.2196D`

Assume for contradiction

\[
z\le Z:=2.2196.
\tag{TE.8}

On the live box, the right side of

\[
z+{c^2h^2+\delta-F(z)\over2(1-\delta)}
\]

is strictly increasing in `z`.  Indeed

\[
{\partial\over\partial z}
=1-{F'(z)\over2(1-\delta)}
>0.96.
\tag{TE.9}

Thus the best capped retention occurs at the largest energetically feasible `z`.
There are two pieces.

### `delta>=F(Z)`

Set `z=Z`.  For fixed `t,h`, the capped retention excess increases with `x` until the
energy boundary `delta=F(Z)`.  The exact derivative has the form

\[
1-{B\over2},
\qquad
B={1+c^2h^2-F(Z)\over2(1-\delta)^2},
\]

and the verifier proves `B<1` on the whole box.  Hence the worst point is on

\[
\delta=F(Z).
\]

There

\[
x=R_t-h-2F(Z).
\]

The capped-retention excess increases with both `t` and `h`, so its global maximum is
at `t=1.8436` and at the largest `h` compatible with `x>=0`, namely

\[
h_*=R_{1.8436}-2F(Z).
\tag{TE.10}

The exact certificate gives

\[
0.0001283911<h_*<0.0001283912<0.00013.
\]

At this point `x=0` and the maximum capped-retention excess is

\[
Z+{c^2h_*^2\over2(1-F(Z))}
-\left(\pi-{1.8436\over2}-ch_*\right).
\tag{TE.11}

Outward rational/Taylor evaluation proves

\[
\boxed{\text{(TE.11)}<-5.7\times10^{-5}.}
\tag{TE.12}

So (TE.4) cannot be met.

### `delta<F(Z)`

The largest allowed dominant mass is now `F^{-1}(delta)<Z`.  This is exactly the
residual survivor-capacity branch whose audited derivatives satisfy

\[
Q_x<0,
\qquad Q_h<0.
\]

Its maximum therefore occurs when it meets the boundary `delta=F(Z)`, already excluded
above.  Thus no point with (TE.8) survives.

We have proved the stronger retained-mass floor

\[
\boxed{z>2.2196-o(1).}
\tag{TE.13}

This is the first use here of the near-frontier residual incidence term at its natural
scale; the older all-`t<=1.844` bootstrap only needed the much coarser `z>2.2069`.

---

## 3. Every exact phase retains more than `0.7179D`

Write the retained dominant mass by exact phase as

\[
z=z_C+z_U+z_V.
\]

For one phase, the one-well bathtub energy is

\[
f(s)=s-2\sin(s/2).
\tag{TE.14}

The selected phase edge sets are disjoint, so

\[
\boxed{
\delta
\ge f(z_C)+f(z_U)+f(z_V)-o(1).
}
\tag{TE.15}

From (TE.2), `x,h>=0`, and `t<=1.8436`,

\[
\delta
\le\delta_{max}
:={1\over2}
\left({9(1.8436)\over2}-2\pi-C_{77}\right).
\tag{TE.16}

The exact certificate gives

\[
\delta_{max}<0.05034454.
\]

Suppose one phase retained at most

\[
a:=0.7179.
\]

For fixed total mass, strict convexity of `f` makes the other two phases cheapest when
equal.  While the exceptional phase is below one third of the total, the resulting
energy decreases as that exceptional mass increases.  Therefore (TE.13) gives the
uniform lower bound

\[
f(z_C)+f(z_U)+f(z_V)
\ge
f(0.7179)
+2f\left({2.2196-0.7179\over2}\right)-o(1).
\tag{TE.17}

The exact verifier proves

\[
\boxed{
\text{right side of (TE.17)}
>\delta_{max}+9.1\times10^{-7}.
}
\tag{TE.18}

This contradicts (TE.15).  Hence

\[
\boxed{
z_C,z_U,z_V>0.7179-o(1).}
\tag{TE.19}

---

## 4. Both leaf phases carry more than `0.2049D` O--O pair weight

The independently proved near-frontier phase-capacity theorem gives, throughout
`t<=1.8436`,

\[
\boxed{U<0.513-o(1),
\qquad V<0.513-o(1).}
\tag{TE.20}

For one phase `i`, if its retained terminal weights on train `tau` are
`a_tau,b_tau`, put `w_tau=min(a_tau,b_tau)` and let

\[
P_i={1\over D}\sum_{\tau\in i}w_\tau.
\]

The elementary inequality

\[
a_\tau+b_\tau\le1+w_\tau
\]

gives

\[
z_i\le M_i+P_i+o(1),
\tag{TE.21}

where `M_i` is the train mass of that phase.  Combining (TE.19)--(TE.20),

\[
\boxed{
P_U,P_V>0.7179-0.513-o(1)
=0.2049-o(1).
}
\tag{TE.22}

This is almost twice the previously recorded `0.103D` two-leaf pair-weight floor.

---

## 5. Most pair weight in both leaves has center degree above `C/2`

Let `C` now denote the center-phase train mass.  For a leaf O--O train `tau`, let
`d_tau D` be its number of center-phase crossing neighbors.

The hostile-audited center/leaf missing-pair correlation implies that the **total**
retained O--O weight, across the two leaf phases together, on trains satisfying

\[
d_\tau\le{C D\over2}
\]

is at most

\[
{2h_{phase}\over C-U},
\qquad
h_{phase}:=C(W-C)-E_{dom}.
\tag{TE.23}

The existing exact common-center certificate proves uniformly on the `t<=1.8436`
box that

\[
\boxed{
{2h_{phase}\over C-U}<0.03405.
}
\tag{TE.24}

Its proof is a one-variable quadratic sign check: with the certified constants

\[
W<1.912456,
\quad
E_{dom}>0.90689967,
\quad
U,V<0.513,
\]

the polynomial

\[
0.03405(C-0.513)-2[C(1.912456-C)-0.90689967]
\]

has positive leading coefficient and negative discriminant, hence is positive for all
real `C`.

Even if the entire bad weight lay in one leaf, (TE.22)--(TE.24) leave in **each** leaf
a high-center-degree O--O subfamily of retained weight

\[
\boxed{
G_U,G_V>0.2049-0.03405-o(1)
=0.17085-o(1).
}
\tag{TE.25}

---

## 6. High-degree O--O trains from the two leaves must be noncrossing

Take one train from the `U` good family and one from the `V` good family.  Each crosses
more than half of all center trains.  Their center-neighbor sets therefore intersect.
Let `gamma` be a shared center neighbor.

If the two leaf trains crossed each other, the three trains would form a triangle in
the strict-rhombus train-crossing graph:

```text
U leaf -- center
   |        |
   +-- V ---+
```

The crossing graph is triangle-free.  Hence every good `U` train is noncrossing with
every good `V` train.

The two leaf phases are distinct exact atoms of the same projective `pi/3` orbit, so
their phases differ by exactly `pi/3`.

---

## 7. Noncrossing cross-leaf O--O pairs require macroscopic terminal energy

For an O--O train `tau`, let `e_tau` be the sum of the exact directional-energy costs
of its two outer terminals.  The low-energy cross-phase endpoint theorem proves:

\[
\boxed{
\text{if two O--O trains in phases separated by }\pi/3
\text{ are noncrossing, then}
\quad e_\tau+e_\sigma\ge2-\sqrt3-o(1).
}
\tag{TE.26}

Let `E_U^g,E_V^g` be the pair-weighted terminal energies of the two good families.  The
inequality (TE.26) holds for every pair in the complete product of their supports.
Taking weighted averages therefore gives

\[
{E_U^g\over G_U}+{E_V^g\over G_V}
\ge2-\sqrt3-o(1).
\]

Since both energies are nonnegative,

\[
\boxed{
E_U+E_V
\ge E_U^g+E_V^g
\ge(2-\sqrt3)\min(G_U,G_V)-o(1).
}
\tag{TE.27}

Using (TE.25),

\[
\boxed{
E_U+E_V
>(2-\sqrt3)(0.17085)-o(1).
}
\tag{TE.28}

The exact rational enclosure `sqrt(3)<1.7321` yields the safe lower bound

\[
E_U+E_V>0.045770715-o(1).
\tag{TE.29}

---

## 8. Add only the disjoint center-phase bathtub energy

The pair-weighted leaf energies in (TE.29) are paid by selected terminal edges in the
`U` and `V` phase windows.  The center-phase selected occurrences are physically
disjoint from those leaf edge classes.  Therefore their directional energies add.

By (TE.19), the center phase alone pays

\[
E_C\ge f(z_C)>f(0.7179)-o(1).
\tag{TE.30}

The exact certificate gives

\[
f(0.7179)>0.0153173048.
\]

Consequently

\[
\begin{aligned}
\delta
&\ge E_C+E_U+E_V-o(1)\\
&>0.0153173048+0.045770715-o(1)\\
&>0.0610880198-o(1).
\end{aligned}
\tag{TE.31}

But (TE.16) gives

\[
\delta<0.05034454+o(1).
\]

The final strict gap exceeds

\[
\boxed{0.01074.}
\tag{TE.32}

This contradiction proves (TE.1).

---

## 9. Frontier effect

This composition is qualitatively stronger than the preceding scalar endpoint work.
It removes the full-core Type-II interval through `1.8436` by combining three distinct
physical facts:

```text
near-frontier residual collapse
    -> z_C,z_U,z_V > .7179
    -> P_U,P_V > .2049

phase-star center incidence
    -> >.17085 good O-O pair weight in each leaf
    -> every good U/V pair shares a center neighbor
    -> U/V trains cannot cross

O-O boundary geometry
    -> noncrossing pi/3 leaf pairs cost >=2-sqrt(3)
    -> leaf terminal energy >.04577

+ disjoint center one-well energy >.01531
    -> total outer energy >.06108
    > available detour <.05035
    -> contradiction.
```

The current proof-only low-`t` frontier therefore moves from `1.843579` to

\[
\boxed{1.8436.}
\]

The next task is to extend the same two-leaf mechanism beyond `1.8436` by replacing
the hard `U,V<0.513` cutoff with a continuous leaf-mass/pair-weight tradeoff, rather
than returning to atomic-gap decimal tuning.

**Disposition:** proved proof-only full-core Type-II exclusion through `t=1.8436`.
C-II and Level I remain open.
