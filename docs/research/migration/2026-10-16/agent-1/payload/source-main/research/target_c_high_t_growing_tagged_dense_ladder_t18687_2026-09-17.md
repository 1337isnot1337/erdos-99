# Target C-II — one low-defect interval contains an almost-linear tagged nested rail and one dense common ladder

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** corrected one-sided high-`t` obstruction shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** full tagged nested rail; global full-defect budget; adjacent complete-train topology; exact diameter-normal order  
**Certificate:** `research/verify_target_c_high_t_growing_tagged_dense_ladder_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The global tagged rail and the dense common-train geometry can be fused without assuming any upper bound on the total number of selected O--O rows.

Let

\[
c=0.0000226,
\qquad
\gamma={c_0\over2}=2.825\times10^{-6}={c\over8}.
\tag{GL.1}
\]

The full tagged-rail theorem supplies more than

\[
\gamma D-o(D)
\]
rail interfaces on one fixed side of the common routing hub, all born on one fixed physical host and strictly nested in selected-cut support.

The dense cusp-chain audit supplies a global nonnegative local cost

\[
J_i^{\rm full}=N_i+L_i+DB_i+F_i+F_{i+1}
\]

with

\[
\sum_iJ_i^{\rm full}\le K_{\rm glob}D+o(D),
\qquad
{K_{\rm glob}\over c}<1{,}108{,}000.
\tag{GL.2}

Since `gamma=c/8`,

\[
{K_{\rm glob}\over\gamma}<8{,}864{,}000.
\tag{GL.3}

Partition the ordered tagged rail into consecutive groups of `k_D` rail positions and take the path interval from the first to the last rail position in each group. These intervals are disjoint and all lie on the same hub side. Averaging (GL.2) over the groups proves:

> For every integer sequence `k_D->infinity` with `k_D=o(D)`, some contiguous hub-free path interval contains at least `k_D` positions of the same fixed-host tagged nested rail and satisfies
> \[
> \boxed{
> \sum_{i\text{ in interval}}J_i^{\rm full}<9{,}000{,}000\,k_D.
> }
> \tag{GL.4}
> \]

This interval has one common complete-train family of size

\[
\boxed{(0.6536-o(1))D,}
\tag{GL.5}

and, after deleting only `sigma_DD=o(D)` common columns with

\[
\sigma_D\to0,
\qquad
{k_D\over\sigma_DD}\to0,
\tag{GL.6}

all retained crossings in the entire interval have uniform angular defect

\[
\boxed{
0<\delta_{jb}
\le {9{,}000{,}000\,k_D\over\sigma_DD}=o(1).
}
\tag{GL.7}

At metric margin `mu=.01`, the same common column order contains two circumcenter flanks, simultaneous on every row in the interval, each of density

\[
\boxed{
0.6536-{1.02\over\sqrt3}-o(1)
=0.0647027254\ldots-o(1).
}
\tag{GL.8}

Taking

\[
k_D=\left\lfloor{D\over\log D}\right\rfloor,
\qquad
\sigma_D={1\over\sqrt{\log D}},
\tag{GL.9}

produces one contiguous interval containing

\[
\boxed{
{D\over\log D}(1-o(1))
}
\tag{GL.10}

positions of the exact-normal tagged nested rail, while the whole interval shares `(0.6536-o(1))D` transverse columns and has uniform angular defect `O((log D)^(-1/2))`.

After fixing one mechanism tag (`EA` or `TB1`) and one physical destination (opposite host or `T_m`), at least

\[
\boxed{
{D\over4\log D}(1-o(1))
}
\tag{GL.11}

rail positions remain inside this same common ladder.

---

## 1. Partition by rail positions, not by raw row length

Let the fixed-host tagged rail positions on one hub side be

\[
i_1<i_2<\cdots<i_s,
\qquad
s>\gamma D-o(D).
\tag{GL.12}

Fix `k=k_D`. Partition the first `floor(s/k)k` rail positions into consecutive groups

\[
(i_1,\ldots,i_k),
(i_{k+1},\ldots,i_{2k}),\ldots .
\]

For each group use the contiguous path interval from its first rail interface through its last. Different group intervals are disjoint because the rail indices are strictly ordered. They never cross the common hub because every rail position is already on one fixed hub side.

The number of full groups is

\[
G_D=\left\lfloor{s\over k}\right\rfloor
={\gamma D\over k}-o(D/k).
\tag{GL.13}

Since all local costs are nonnegative and the group intervals are disjoint,

\[
\sum_{g=1}^{G_D}J(g)
\le K_{\rm glob}D+o(D),
\tag{GL.14}

where `J(g)` is the sum of `J_i^full` over group interval `g`. Therefore some group obeys

\[
J(g)
\le {K_{\rm glob}D+o(D)\over G_D}
<\left({K_{\rm glob}\over\gamma}+o(1)\right)k.
\tag{GL.15}

By (GL.3), for all sufficiently large `D`, this is less than `9,000,000 k`. This proves (GL.4).

This argument does **not** use the lower row-block density `cD` as an upper bound on the total row count. The earlier window-density shortcut is therefore unnecessary.

---

## 2. The selected interval shares almost the full crossing population

Let the rows in the chosen interval be

\[
\tau_p,\tau_{p+1},\ldots,\tau_q.
\]

Every row has more than

\[
r_0D-o(D),
\qquad r_0=0.6536,
\]

complete crossing trains. Adjacent terminal topology gives

\[
|\Gamma_j\triangle\Gamma_{j+1}|\le L_j.
\]

The `L_j` part of (GL.4) gives

\[
\sum_{j=p}^{q-1}L_j<9{,}000{,}000\,k_D.
\tag{GL.16}

Starting from `Gamma_p`, at most `L_j` trains can be lost from the running intersection at interface `j`. Hence

\[
\left|\bigcap_{j=p}^{q}\Gamma_j\right|
>r_0D-9{,}000{,}000\,k_D-o(D).
\tag{GL.17}

Since `k_D=o(D)`, this is (GL.5). The common columns are pairwise noncrossing and have one common order on every row.

---

## 3. A vanishing common-column deletion makes the entire interval phase-pure

The `F` part of (GL.4) gives

\[
\sum_{j=p}^{q}F_j<9{,}000{,}000\,k_D.
\tag{GL.18}

For each common column `b`, let

\[
\Delta_b:=\sum_{j=p}^{q}\delta_{jb}.
\]

Then

\[
\sum_b\Delta_b<9{,}000{,}000\,k_D.
\]

Delete columns satisfying

\[
\Delta_b>{9{,}000{,}000\,k_D\over\sigma_DD}.
\]

There are fewer than `sigma_DD=o(D)` such columns. The surviving common family still has density `(0.6536-o(1))D`, and every retained crossing is bounded by its column total, proving (GL.7).

For the choice (GL.9),

\[
{k_D\over\sigma_DD}
={1+o(1)\over\sqrt{\log D}},
\]

so the whole common ladder is uniformly asymptotically equilateral.

---

## 4. Common circumcenter flanks survive on every row

Fix `mu=.01`. The exact train-step metric and the source circumdisk capacity apply to the same retained ordered column family on every row. After the `o(D)` deletion, each row has more than

\[
\left(0.6536-{1.02\over\sqrt3}-o(1)\right)D
\]

columns below the `-.01D` row-normal level and the same number above `+.01D`.

Because the column order is common throughout the interval, the same initial and final column blocks work simultaneously on every row. This proves (GL.8).

---

## 5. The global rail structure survives intact inside the interval

By construction the chosen interval contains a full group of `k_D` consecutive positions in the globally ordered tagged rail. Therefore these `k_D` bars retain:

- one fixed birth host;
- distinct ordered birth endpoints;
- strictly nested selected-cut support intervals;
- strictly ordered exact diameter/hull-normal directions;
- exact antipodal transport of that normal parameter to the partner endpoint;
- partner endpoint on the opposite host or `T_m`;
- an `EA` or `TB1` mechanism tag at every position.

Pigeonholing the two mechanism tags and two destinations leaves at least `k_D/4` positions with one common tag and one common physical destination. Equation (GL.11) follows from (GL.9).

---

## 6. Frontier effect

The corrected fusion is stronger than a raw sliding-window argument because it uses the rail itself to partition the path. It requires no upper bound on the total number of selected rows.

The current survivor contains one contiguous hub-free interval with

```text
D/log D positions of one fixed-host exact-normal nested rail;
(0.6536-o(1))D transverse trains common to every row of the interval;
uniform O((log D)^(-1/2)) rhombus defect after an o(D) column deletion;
(0.0647027-o(1))D common columns on each side of a +-0.01D circumcenter corridor;
and D/(4 log D) rail positions after fixing one mechanism and one destination.
```

C-II remains open. The remaining problem is no longer to synchronize the global rail with a common train ladder: a growing piece of the rail already lies inside one phase-pure, metrically bracketed ladder.

**Disposition:** repaired the rail/grid fusion using a partition by consecutive rail positions, yielding an almost-linear number of tagged nested bars in one low-defect common ladder without any unjustified row-count denominator.