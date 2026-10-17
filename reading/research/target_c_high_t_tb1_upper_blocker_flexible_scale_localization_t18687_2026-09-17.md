> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_upper_blocker_flexible_scale_localization_t18687_2026-09-17.md) · source SHA-256 `4341c2b60c7cd036feaac777dd6cd5d6c6a51ad403d08880299bfaf5a2a6534f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5ceab0f3dc6781b204d3b4a5b369a463dc51cf58", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_upper_blocker_flexible_scale_localization_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "db9ee7ca5592b9ac14c5d93ec913041513df8887aeb3cf917e745dd9ad6c9e00"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — upper Horn blockers localize at every diverging sublinear scale

**Date:** 2026-09-17  
**Status:** proof-only strengthening of upper-blocker dense-grid localization; no canonical promotion claimed  
**Scope:** seven-spaced one-sign strong-TB1 Horn UPPER branches through `t=(q-k)/D<=1.8687`  
**Dependencies:** seven-spaced Horn propagation; exact O--O path interval support; global complete-train count; global angular-defect and terminal-variation budgets; SIGNED/THIN split  
**Certificate:** `research/verify_target_c_high_t_tb1_upper_blocker_flexible_scale_localization_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing upper-blocker localization theorem fixed

$$
L_D=\left\lfloor{D\over\log D}\right\rfloor
$$

before splitting blocker intervals into long and short supports. Nothing in its proof uses the logarithm. The exact requirement is only

$$
\boxed{
L_D\longrightarrow\infty,
\qquad
L_D=o(D).
}
\tag{FL.1}
$$

Running the same argument at an arbitrary scale satisfying (FL.1) gives a stronger parameterized theorem.

Let

$$
\gamma_7={113\over640{,}000{,}000},
\qquad
T_*={6121\over2000}=3.0605,
$$

and

$$
\boxed{
c_{*,7}:={\gamma_7\over48T_*}
={113\over94{,}018{,}560{,}000}
=1.20189035016\ldots\times10^{-9}.}
\tag{FL.2}
$$

Every non-LOWER Horn branch contains an injectively owned upper family of density at least

$$
\delta_{0,7}:={\gamma_7\over8}.
\tag{FL.3}
$$

Then for **every** choice of `L_D` satisfying (FL.1), one of the following holds for all sufficiently large `D`:

> **COMMON-CUT:** one selected O--O row supports more than
> 

$$

> \boxed{(c_{*,7}-o(1))L_D}
> 
$$


> distinct upper blockers of one common type, SIGNED or THIN. Its full angular-defect cost satisfies
> 

$$

> \boxed{F_j=O(D/L_D)=o(D).}
> 
$$


>
> **LOCAL-WINDOW:** one path window of at most
> 

$$

> \boxed{2L_D+O(1)}
> 
$$


> consecutive regions contains both endpoints of more than
> 

$$

> \boxed{(c_{*,7}-o(1))L_D}
> 
$$


> distinct upper blockers of one common type. Its full row-defect plus terminal-variation cost satisfies
> 

$$

> \boxed{C_W=O(L_D)=o(D).}
> 
$$



In either case the same purification argument leaves a common family of

$$
(0.6536-o(1))D
$$

transverse trains with uniform `o(1)` angular error on the selected row/window, together with the standard `0.01D` circumcenter flanks of density

$$
(0.0647027254265\ldots-o(1))D
$$

on each side.

The old `D/log D` statement is the specialization `L_D=D/log D`.

More useful choices are now available. For example,

$$
L_D={D\over\log\log D}
$$

gives

$$
\boxed{
(c_{*,7}-o(1)){D\over\log\log D}
}
$$

same-type blockers in one common cut or one `O(D/log log D)` low-defect window. More generally, taking

$$
L_D={D\over\omega(D)},
\qquad
\omega(D)\to\infty,
\qquad
\omega(D)=o(D),
$$

gives

$$
(c_{*,7}-o(1)){D\over\omega(D)}
$$

localized blockers while keeping every normalized train-defect cost vanishing.

Choosing `omega(D)` to diverge arbitrarily slowly shows that the upper Horn obstruction localizes at **near-linear scale**:

$$
\boxed{D^{1-o(1)}\text{ same-type upper blockers}}
$$

inside either one common row or an `o(D)` path window, without sacrificing the `Theta(D)` near-equilateral train scaffold.

---

## 1. Owned upper input

By the seven-spaced poison-forest theorem, every UPPER outcome contains a family `E_D` of distinct upper singleton blockers with injective retained-coordinate ownership and

$$
|E_D|>(\delta_{0,7}-o(1))D,
\qquad
\delta_{0,7}={\gamma_7\over8}.
\tag{FL.4}
$$

For an upper blocker with endpoint regions `R_a,R_b`, `a<b`, exact path support is

$$
I(e)=\{a+1,\ldots,b\},
\qquad
\ell(e)=b-a.
\tag{FL.5}
$$

The selected O--O path has

$$
m\le T_*D+o(D).
\tag{FL.6}
$$

Fix any integer sequence `L=L_D` satisfying (FL.1) and split

$$
E_D^{long}=\{e:\ell(e)\ge L\},
\qquad
E_D^{short}=\{e:\ell(e)<L\}.
\tag{FL.7}
$$

One class has size more than

$$
\left({\delta_{0,7}\over2}-o(1)\right)D.
\tag{FL.8}
$$

Put

$$
\vartheta_7:={\delta_{0,7}\over3T_*}.
\tag{FL.9}
$$

After the final SIGNED/THIN split, the universal localized coefficient will be

$$
{\vartheta_7\over2}
={\delta_{0,7}\over6T_*}
={\gamma_7\over48T_*}
=c_{*,7}.
\tag{FL.10}
$$

---

## 2. Long supports: the defect cost is `O(D/L)`

Assume the long class satisfies (FL.8). For each selected cut `j`, let

$$
h_j=|\{e\in E_D^{long}:j\in I(e)\}|.
$$

Then

$$
\sum_jh_j
=\sum_{e\in E_D^{long}}\ell(e)
>
\left({\delta_{0,7}\over2}-o(1)\right)DL.
\tag{FL.11}
$$

Call `j` rich when

$$
h_j\ge\vartheta_7L.
\tag{FL.12}
$$

By (FL.6), poor cuts carry at most

$$
(T_*D+o(D))\vartheta_7L
\le
\left({\delta_{0,7}\over3}+o(1)\right)DL.
\tag{FL.13}
$$

Hence rich cuts carry total blocker incidence more than

$$
\boxed{
\left({\delta_{0,7}\over6}-o(1)\right)DL.
}
\tag{FL.14}
$$

Let `F_j` be the full angular-defect sum on row `j`. The global budget is

$$
\sum_jF_j=O(D).
\tag{FL.15}
$$

Weighted averaging with (FL.14) gives one rich row with

$$
{F_j\over h_j}=O(L^{-1}).
\tag{FL.16}
$$

Injective ownership gives

$$
h_j\le |E_D|=O(D),
$$

so

$$
\boxed{F_j=O(D/L).}
\tag{FL.17}
$$

Because `L->infinity`, this is `o(D)`.

The row supports at least `vartheta_7 L` upper blockers. Splitting SIGNED versus THIN leaves more than

$$
\boxed{(c_{*,7}-o(1))L}
\tag{FL.18}
$$

blockers of one type. This is COMMON-CUT.

---

## 3. Short supports: the window cost is `O(L)`

Assume instead the short class satisfies (FL.8). Partition the path-region indices into consecutive blocks of `L` indices. Assign a blocker with endpoint indices `a<b` to the block containing `a`. Since

$$
b-a<L,
$$

both endpoints lie in the union of that block and the following one, a window of at most

$$
2L+O(1)
$$

regions.

There are at most

$$
{T_*D\over L}+o(D/L)
\tag{FL.19}
$$

candidate windows.

Call a window rich if it contains at least

$$
\vartheta_7L
\tag{FL.20}
$$

assigned blockers. Poor windows contain altogether at most

$$
\left({\delta_{0,7}\over3}+o(1)\right)D
$$

blockers. Thus rich windows contain more than

$$
\boxed{
\left({\delta_{0,7}\over6}-o(1)\right)D
}
\tag{FL.21}
$$

blockers.

For a window `W`, let `C_W` be the sum of all row angular-defect costs plus all internal adjacent terminal-variation costs. As in the existing localization proof, each row/interface belongs to at most two two-block windows, so

$$
\sum_WC_W=O(D).
\tag{FL.22}
$$

Weighted averaging over the rich windows gives one rich `W` with

$$
{C_W\over e_W}=O(1),
\tag{FL.23}
$$

where `e_W` is its blocker count.

Injective ownership is the key scale control. Every assigned blocker has its distinct owner inside the two-block window, so

$$
e_W\le2L+O(1).
\tag{FL.24}
$$

Therefore

$$
\boxed{C_W=O(L).}
\tag{FL.25}
$$

Because `L=o(D)`, this is `o(D)`.

The rich window contains at least `vartheta_7L` blockers. Splitting SIGNED versus THIN again leaves (FL.18) blockers of one type. This is LOCAL-WINDOW.

---

## 4. Dense common trains survive at every scale

COMMON-CUT has full row defect `F_j=o(D)`. Starting from the high-`t` crossing-neighbor floor

$$
|\Gamma_j|>(0.6536-o(1))D,
$$

delete columns above a threshold `epsilon_D->0` chosen so slowly that

$$
{F_j\over\epsilon_D}=o(D).
$$

The retained row has `(0.6536-o(1))D` columns, all at angle `pi/3+o(1)`.

LOCAL-WINDOW has total row plus terminal cost `C_W=o(D)`. Intersecting the rowwise train families through the window loses only `o(D)` columns by terminal variation. Then use the angular part of `C_W` and the same slow-threshold argument to retain one common family of

$$
(0.6536-o(1))D
$$

columns with uniform `o(1)` defect across the whole window.

The exact train-step metric plus the circumdisk capacity estimate then gives the usual common `0.01D` initial/terminal flank blocks, each of density

$$
0.6536-{1.02\over\sqrt3}
=0.0647027254265\ldots .
\tag{FL.26}
$$

Thus changing the localization scale costs no train density.

---

## 5. Useful scales

The theorem can now be tuned to the downstream argument rather than fixing a logarithm in advance.

### `L=D/log log D`

For sufficiently large `D`,

$$
L_D=\left\lfloor{D\over\log\log D}\right\rfloor
$$

satisfies (FL.1). The localized same-type population is

$$
>(c_{*,7}-o(1)){D\over\log\log D}.
$$

COMMON-CUT has `F_j=O(log log D)`, while LOCAL-WINDOW has width and total cost `O(D/log log D)`.

### General slowly diverging denominator

Let

$$
L_D=\left\lfloor{D\over\omega(D)}\right\rfloor,
$$

where

$$
\omega(D)\to\infty,
\qquad
\omega(D)=o(D).
$$

Then

$$
\boxed{
N_{localized}>
(c_{*,7}-o(1)){D\over\omega(D)}.
}
\tag{FL.27}
$$

COMMON-CUT has

$$
F_j=O(\omega(D)),
$$

and LOCAL-WINDOW has width/cost

$$
O(D/\omega(D)).
$$

Taking, for example, `omega(D)=log log D`, or any still slower explicit divergent function, gives a localized population of order `D^(1-o(1))` while every normalized defect and every normalized LOCAL-WINDOW width tends to zero.

---

## 6. Frontier effect

The upper Horn branch no longer has an intrinsic `D/log D` localization scale. Its correct current statement is scale-free:

```text
for every L -> infinity with L=o(D),
either
    Theta(L) same-type upper blockers share one o(D)-defect row,
or
    Theta(L) same-type upper blockers lie in one O(L)-width/o(D)-defect window,
and in both cases a fixed (0.6536-o(1))D near-60 train scaffold survives.
```

Choosing `L=D/omega(D)` with `omega(D)` arbitrarily slowly divergent makes the localized obstruction near-linear.

This does not change the `D^(1/4-o(1))` exponent of the later SIGNED matching/braid extraction, because the generic inactive-near-diameter degree is `O(D^(3/4))`. It does remove an unnecessary logarithmic choice from the structural theorem and gives much larger raw SIGNED/THIN populations for any downstream argument that can use blocker multiplicity before matching extraction.

**Disposition:** generalized upper-blocker dense-grid localization from the single scale `D/log D` to every diverging sublinear scale, with explicit defect laws `O(D/L)` and `O(L)` and near-linear localization available by choosing `L=D/omega(D)` with `omega(D)` slowly divergent. C-II and Level I remain open.
