> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_lower_blocker_local_ladders_t18687_2026-09-17.md) · source SHA-256 `d1ec8173b6da3ef3fcf21570f2356154af53325ea2d4d1b8993d802ccd3b28f3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 26 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "efcace70234df8b72ff11223c10f872f3c33b974", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_lower_blocker_local_ladders_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f168d9a44ffb896400a9feae1b8b1a7416d2fab56a371ed53a64464d30fc699a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — permanent LOWER Horn blockers synchronize to disjoint local ladders and one global column

**Date:** 2026-09-17  
**Status:** proof-only continuation of the Horn poison-forest extraction; no canonical promotion claimed  
**Scope:** the permanent LOWER side of the 15-spaced one-sign strong-TB1 Horn subsystem through `t=(q-k)/D<=1.8687`  
**Dependencies:** Horn poison-forest theorem; fourteen-row short-blocker bandwidth; global angular-defect and terminal-variation budgets; high-`t` crossing-neighbor floor; complete-train count; exact train-step metric  
**Certificate:** `research/verify_target_c_high_t_tb1_lower_blocker_local_ladders_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The Horn poison-forest theorem leaves one branch with a linear population of permanent near-unit blockers:

```math
N_D^{lower}>
\left({\gamma\over4}-o(1)\right)D,
\qquad
\gamma={791\over9{,}600{,}000{,}000}.
\tag{LL.1}
```

Every blocker is owned by one retained strong-TB1 path layer, the retained owners are pairwise at least fifteen indices apart, and the short-pair bandwidth theorem gives blocker support length at most fourteen.

Those two integer scales fit exactly. After fixing whether the other endpoint lies path-left or path-right of the owner, the blocker support intervals become pairwise disjoint. This lets the global train-defect budget be spent independently on a linear number of blocker windows.

The result is:

> **LOWER local-ladder theorem.** The permanent LOWER branch contains more than
> 

```math
> \left({\gamma\over16}-o(1)\right)D
> 
```
> blockers whose exact support intervals are pairwise disjoint and whose entire support windows each carry one local common train family of
> 

```math
> (0.6436-o(1))D
> 
```
> columns with uniform inverse-`D` angular defect on every row of the window and common `0.01D` circumcenter flanks.
>
> Moreover one single complete stopped train belongs to the local common-column family of more than
> 

```math
> \boxed{
> \left(1.08295128110\ldots\times10^{-9}-o(1)\right)D
> }
> 
```
> of these pairwise-disjoint blocker windows.

Thus the remaining lower Horn obstruction is not merely path-local. A linear subfamily can be threaded by one common transverse train while every local blocker window is independently near-equilateral to inverse-`D` accuracy.

---

## 1. Fix one support orientation

Write the selected path as

```math
R_0\xleftrightarrow{\tau_1}R_1\xleftrightarrow{}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{LL.2}
```

A permanent lower blocker owned by retained layer `R_i` has its other endpoint in some `R_j`, `j!=i`, and

```math
\boxed{|i-j|\le14}
\tag{LL.3}
```

by the short-pair path-bandwidth theorem. Its exact selected-cut support is the integer interval between `i` and `j`.

Split the lower blockers according to whether

```math
j>i
\quad\text{or}\quad
j<i.
```

Retain the larger class. Its size is more than

```math
\boxed{
\left({\gamma\over8}-o(1)\right)D.}
\tag{LL.4}
```

The retained owner coordinates all belong to the same fifteen-spaced Horn set `P_D`. Hence if `i<i'` are two owners,

```math
i'-i\ge15.
\tag{LL.5}
```

Suppose the chosen orientation is `j>i`. Then the support of the first blocker ends no later than cut `i+14`, while the support of the next blocker begins no earlier than cut `i'+1>=i+16`. Therefore the two exact support intervals are disjoint. The `j<i` orientation is symmetric.

Thus

```math
\boxed{
\text{all blocker support intervals in the retained oriented family are pairwise disjoint.}
}
\tag{LL.6}
```

This is stronger than mere bounded overlap and uses both constants `14` and `15` sharply.

---

## 2. A full train-defect cost for one blocker window

For a retained blocker `e`, let

```math
I(e)=\{a+1,\ldots,b\},
\qquad
1\le |I(e)|\le14,
\tag{LL.7}
```

be its exact support interval.

Define its local train-defect cost

```math
C(e)
:=
\sum_{j\in I(e)}F_j
+
\sum_{j:\,j,j+1\in I(e)}L_j,
\tag{LL.8}
```

where

- `F_j` is the full angular-defect sum over all complete trains crossing row `tau_j`;
- `L_j` is the adjacent terminal-variation cost controlling `|Gamma_j triangle Gamma_{j+1}|`.

The canonical global budgets give

```math
\sum_jF_j=O(D),
\qquad
\sum_jL_j=O(D).
\tag{LL.9}
```

By (LL.6), distinct retained blocker intervals use disjoint row sets and disjoint internal adjacent-row transitions. Hence

```math
\boxed{
\sum_e C(e)=O(D).
}
\tag{LL.10}
```

There are more than `(gamma/8-o(1))D` intervals. Therefore a fixed constant `H_0`, independent of `D`, can be chosen so that all but at most half have

```math
C(e)\le H_0.
\tag{LL.11}
```

Retain such good blockers. Their number is

```math
\boxed{
N_D^{good}>
\left({\gamma\over16}-o(1)\right)D.}
\tag{LL.12}
```

Numerically,

```math
{\gamma\over16}
=5.14973958333\ldots\times10^{-9}.
\tag{LL.13}
```

Their support intervals remain pairwise disjoint.

---

## 3. Every good blocker window has a dense inverse-D common train ladder

Fix a good blocker `e` with support rows `I(e)`.

Every selected high-`t` row satisfies the crossing-neighbor floor

```math
|\Gamma_j|>(0.6536-o(1))D.
\tag{LL.14}
```

Adjacent rows obey

```math
|\Gamma_j\triangle\Gamma_{j+1}|\le L_j.
\tag{LL.15}
```

Since the total internal `L`-cost of this support interval is at most `H_0`, intersecting the crossing families across at most fourteen rows loses only `O(1)` columns. Therefore

```math
\boxed{
\left|\bigcap_{j\in I(e)}\Gamma_j\right|
>(0.6536-o(1))D.}
\tag{LL.16}
```

For a column `b` in this common family, let

```math
\Delta_e(b)=\sum_{j\in I(e)}\delta_{jb}
\tag{LL.17}
```

be its summed acute angular defect across the local window. Equation (LL.11) gives

```math
\sum_b\Delta_e(b)\le H_0.
\tag{LL.18}
```

Delete the at most `0.01D` columns with

```math
\Delta_e(b)>{100H_0\over D}.
\tag{LL.19}
```

Indeed Markov gives at most

```math
{H_0\over100H_0/D}=0.01D
```

such columns. The surviving family `P(e)` satisfies

```math
\boxed{|P(e)|>(0.6436-o(1))D}
\tag{LL.20}
```

and, simultaneously for every support row and every retained column,

```math
\boxed{
0<\delta_{jb}\le{100H_0\over D}.}
\tag{LL.21}
```

Thus each blocker support interval sits inside a fixed-depth common train ladder with uniform inverse-`D` near-equilateral geometry.

The common column order and exact train-step metric give the standard `mu=0.01` circumcenter flanks. Their density is

```math
\boxed{
0.6436-{1.02\over\sqrt3}
=0.0547027254265\ldots .}
\tag{LL.22}
```

The same initial and terminal flank blocks work on every row of this local window.

Finally, the blocker endpoints are separated by every row in `I(e)`, so its straight segment meets every row of its own local ladder.

---

## 4. One transverse train threads linearly many disjoint blocker windows

Let `T_D` be the total number of complete stopped trains in the source. The audited train ledger gives

```math
\boxed{T_D<(T_*+o(1))D,
\qquad T_*=3.0605={6121\over2000}.}
\tag{LL.23}
```

Count incidences

```math
(e,b),
\qquad
b\in P(e),
```

between the good blocker windows from (LL.12) and their pure common column families.

By (LL.12) and (LL.20), the number of incidences is more than

```math
\left({\gamma\over16}\,0.6436-o(1)\right)D^2.
\tag{LL.24}
```

There are at most `(T_*+o(1))D` possible complete trains `b`. Hence one train `b_*` occurs in at least

```math
\left(
{\gamma\over16}{0.6436\over T_*}-o(1)
\right)D
\tag{LL.25}
```

local ladders.

Using

```math
0.6436={1609\over2500},
```

the exact coefficient is

```math
\boxed{
{\gamma\over16}{0.6436\over T_*}
={1{,}272{,}719\over1{,}175{,}232{,}000{,}000{,}000}
=1.08295128110\ldots\times10^{-9}.}
\tag{LL.26}
```

Therefore one fixed complete stopped train crosses every support row of a linear number of pairwise-disjoint permanent-lower blocker windows, and at all those crossings its angle with the local selected row is

```math
{\pi\over3}+O(D^{-1})
\tag{LL.27}
```

with one source-independent coefficient determined by `H_0`.

Because the blocker intervals are pairwise disjoint and identically oriented in path order, these occurrences are globally ordered along the selected O--O path.

---

## 5. Horn frontier after both metric synchronizations

The 15-spaced Horn obstruction now has a train-geometric representative in every branch.

```text
PERMANENT LOWER:
    linear many <=14-row near-unit blockers;
    linear subfamily has pairwise-disjoint support windows;
    each window has >0.6436D common inverse-D near-60 columns;
    one fixed transverse train threads a linear number of those windows.

UPPER:
    by the separate upper-localization theorem,
    either D/log D same-type blockers share one low-defect row,
    or D/log D same-type blockers lie in one o(D)-width low-defect window
    with >0.6536D common near-60 columns.
```

This removes the last train-synchronization gap from the LOWER Horn branch. It does not yet contradict the existence of the near-unit blockers. The remaining lower task is local: exploit a strict near-unit blocker crossing at most fourteen co-phased rows while the same transverse train passes through a linear ordered family of such local ladders.

**Disposition:** synchronized a linear permanent-lower Horn family to pairwise-disjoint inverse-`D` local ladders and one globally repeated transverse train. C-II and Level I remain open.
