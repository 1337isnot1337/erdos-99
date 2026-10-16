# Target C-II — paired leaf outer energy excludes `t<=1.8436`

**Date:** 2026-09-15  
**Status:** proof-only downstream contradiction  
**Scope:** full-core Type-II branch  
**Dependencies:** matched atomic floor `g=0.007707`; `t<=1.8436` two-leaf O--O localization; phase-resolved retained outer-mass theorem; two-leaf common-center terminal-energy theorem  
**Certificate:** `research/verify_target_c_paired_leaf_bathtub_exclusion_t18436.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current near-frontier stack already gives two facts which had not yet been combined.

First, every survivor with

\[
t:={q-k\over D}\le1.8436
\]

has retained dominant outer-occurrence masses

\[
z_C,z_U,z_V>0.616-o(1),
\qquad
z_C+z_U+z_V>2.2069-o(1).
\tag{PB.1}
\]

Second, the two leaf phases contain good outer-to-outer subfamilies of retained pair weight

\[
G_U,G_V>0.06895-o(1)
\tag{PB.2}
\]

whose complete cross-product is noncrossing. The endpoint theorem therefore gives the weighted energy inequality

\[
G_VE_U^{good}+G_UE_V^{good}
\ge(2-\sqrt3)G_UG_V-o(1).
\tag{PB.3}
\]

The missing observation is that these paired endpoint energies live inside the same phasewise outer-occurrence measures used by the bathtub theorem. Removing the paired endpoint submeasures before applying the bathtub inequality leaves enough residual occurrence mass that Jensen alone already exceeds the entire available outer-energy budget.

The consequence is

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}\ge1.8436
}
\]

at the current proof-only full-core Type-II scope. In particular the previous rounded floor `1.843579` is superseded by the structural exclusion of the whole interval through `1.8436`.

---

## 1. Trim both good leaf families to equal pair weight

Fix

\[
g:={1379\over20000}=0.06895.
\tag{PB.4}
\]

Fix an arbitrary `epsilon>0` and put `g_epsilon=g-epsilon`. By (PB.2), for all sufficiently large members of the sequence each good leaf family has retained pair weight above `g_epsilon`. Reduce retained weights inside each good family so that both trimmed families have normalized pair weight exactly `g_epsilon`. This is only a downward fractional trimming of the already-retained weights `w_\tau\in[0,1]`; it does not change train geometry, crossing relations, or endpoint energies. All inequalities below are first proved with `g_epsilon`, then `epsilon downarrow0` is taken after the source limit. For readability the displayed formulas write the limiting value `g`.

Write the trimmed pair energies as

\[
E_U',\qquad E_V'.
\]

Applying (PB.3) to the trimmed families gives

\[
gE_U'+gE_V'
\ge(2-\sqrt3)g^2-o(1),
\]

hence

\[
\boxed{
E_U'+E_V'
\ge(2-\sqrt3)g-o(1).
}
\tag{PB.5}

This keeps only a fixed subfamily of the parent theorem, so no new crossing or energy claim is introduced.

---

## 2. Paired endpoints are literal submeasures of the phase occurrence measures

For one leaf phase `i in {U,V}`, let `nu_i` be the retained outer-occurrence measure from the phasewise bathtub theorem. Its total mass is `z_i`, it satisfies

\[
0\le\nu_i\le d\theta,
\tag{PB.6}
\]

and its directional-energy integral is part of the global selected outer-energy budget.

For every trimmed good O--O train `tau`, put retained weight `w'_tau` at each of its two selected terminal occurrences. Summing these endpoint atoms in the limiting measure gives a paired endpoint submeasure `mu_i` with

\[
0\le\mu_i\le\nu_i,
\qquad
\mu_i(\mathbb R/\pi\mathbb Z)=2g,
\tag{PB.7}
\]

and energy exactly `E_i'` in the limiting normalization. The parent common-center theorem already records that this pair energy is not a new currency: it is a subset of the dominant outer directional-energy budget.

Therefore the residual measure

\[
\nu_i-\mu_i
\]

is nonnegative, still bounded above by `d\theta`, has mass

\[
z_i-2g,
\]

and is disjoint in measure weight from the paired energy already counted in `E_i'`.

Let

\[
f(s):=s-2\sin(s/2),
\qquad 0\le s\le\pi.
\tag{PB.8}
\]

The one-well bathtub theorem applies to every such residual submeasure, so if `A_i` denotes the total retained outer directional energy in phase `i`, then

\[
\boxed{
A_U\ge E_U'+f(z_U-2g)-o(1),
}
\tag{PB.9}
\]

\[
\boxed{
A_V\ge E_V'+f(z_V-2g)-o(1).
}
\tag{PB.10}

For the center phase no trimming is needed:

\[
\boxed{
A_C\ge f(z_C)-o(1).
}
\tag{PB.11}

No stability theorem is used here. The only input is measure domination `nu_i<=dtheta` plus removal of an actual submeasure.

---

## 3. Jensen converts the paired energy into a global outer-energy floor

The selected phase energies are disjoint pieces of the same outer-energy budget, hence

\[
\delta\ge A_C+A_U+A_V-o(1).
\tag{PB.12}
\]

Combining (PB.5) and (PB.9)--(PB.11),

\[
\delta
\ge
f(z_C)+f(z_U-2g)+f(z_V-2g)
+(2-\sqrt3)g-o(1).
\tag{PB.13}
\]

By (PB.1),

\[
z_C+(z_U-2g)+(z_V-2g)
>2.2069-4g-o(1).
\]

The exact arithmetic is

\[
2.2069-4(0.06895)=1.9311=3(0.6437).
\tag{PB.14}
\]

The function `f` is increasing and convex on `[0,pi]` because

\[
f'(s)=1-\cos(s/2)\ge0,
\qquad
f''(s)={1\over2}\sin(s/2)\ge0.
\]

Jensen therefore gives

\[
\boxed{
\delta
\ge
3f(0.6437)+(2-\sqrt3)(0.06895)-o(1).
}
\tag{PB.15}

The exact certificate proves the safe numerical form

\[
\boxed{
\delta>0.05163-o(1).
}
\tag{PB.16}

The actual certified lower value is above `0.0516390`.

---

## 4. The network envelope gives the incompatible upper bound

The current matched atomic theorem gives

\[
C_{707}:=2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3},
\]

and

\[
{T-q/2\over D}\ge C_{707}-o(1).
\]

Equivalently the current network variable satisfies

\[
U_{net}
={9t\over2}-2\pi-2\delta-\kappa/2
\ge C_{707}-o(1),
\tag{PB.17}
\]

with `kappa=k/D>=0`. Thus every survivor with `t<=1.8436` obeys

\[
2\delta
\le {9\over2}(1.8436)-2\pi-C_{707}+o(1).
\]

The exact verifier obtains

\[
\boxed{
\delta<0.05035+o(1),
}
\tag{PB.18}

more precisely an upper value below `0.0503411`.

Equations (PB.16) and (PB.18) differ by more than

\[
1.27\times10^{-3},
\]

so the contradiction has a macroscopic fixed margin. No sixth- or seventh-decimal endpoint cancellation is involved.

Therefore there is no full-core Type-II asymptotic survivor branch with limiting `t` at or below `1.8436`. Equivalently,

\[
\boxed{\liminf_{D\to\infty} t\ge1.8436.}
\]

---

## 5. Why this is stronger than the parent terminal-energy theorem

The common-center theorem by itself gave only

\[
E_U^{good}+E_V^{good}>0.01847-o(1),
\]

which is smaller than the ordinary total two-leaf bathtub energy in some phase-mass regimes. The new step is to remember **where** that energy lives.

Each unit of trimmed O--O pair weight occupies two actual terminal occurrences. Once those paired endpoint submeasures are removed, the remaining phase occurrence measure still has mass `z_i-2g` and must itself pay the one-well bathtub cost. This prevents the forced pair energy from being hidden inside the ordinary bathtub minimizer for free.

The argument is deliberately insensitive to how the paired energy splits between the two leaves. Equal trimming reduces (PB.3) to the scalar sum floor (PB.5), after which Jensen treats all three residual phase measures symmetrically.

---

## 6. Scope and next frontier

This theorem uses only already-proved full-core Type-II inputs and the current scope-safe matched atomic floor. It does not construct an exact equilateral triangle and does not close C-II globally.

What changes is the low-`t` frontier:

```text
previous proof-only scalar floor:  t >= 1.843579
new structural floor:              liminf t >= 1.8436
```

The next useful step is not another atomic-gap decimal. One should rerun the two-leaf localization and common-center trimming with `t` above `1.8436` and optimize the retained pair weight `g(t)` against the paired-bathtub inequality

\[
\delta
\ge
3f\left({z_{tot}-4g\over3}\right)
+(2-\sqrt3)g.
\]

That continuation may push the floor materially farther before the good-pair weight collapses.

**Disposition:** proved proof-only floor `liminf t>=1.8436` by paired-leaf bathtub exclusion. C-II and Level I remain open.
