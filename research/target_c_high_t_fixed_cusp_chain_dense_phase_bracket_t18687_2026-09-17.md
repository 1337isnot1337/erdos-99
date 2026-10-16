<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ce4f969e063a6b7440243ca5ad0b87d096970f59", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_fixed_cusp_chain_dense_phase_bracket_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4016041df3d71012ea2c9fd59ec1f717c4557168affe903001cb1f18b6c3a8e4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every fixed cusp chain has one near-full phase-pure circumcenter-bracketing ladder across all rows

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch through `t=(q-k)/D<=1.8687`  
**Dependencies:** fixed high-`t` cusp-chain sliding-window argument; canonical full strict-rhombus angular-defect budget; adjacent-strip terminal-topology bound; high-`t` crossing-neighbor floor; triangle-free complete-train crossing graph; exact train-step metric bound; full-source circumdisk bound  
**Certificate:** `research/verify_target_c_high_t_fixed_cusp_chain_dense_phase_bracket_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing fixed cusp-chain theorem gives, for every fixed strip depth `R`, a block of `R+1` consecutive selected O--O rows with finite total switching/terminal/KKT complexity and a common inverse-`D` column family of density only `0.0783`. Separately, each adjacent low-terminal pair has almost `0.6536D` common crossing trains.

The `0.0783` loss is not intrinsic to a fixed chain. The same sliding-window argument can charge the **full** angular defect of every row, not merely the defect against the previously synchronized `B_+` columns. Since the canonical full-source angular-defect sum is still only `O(D)`, the augmented window has the same `1,109,000 R` cost scale. Its total terminal symmetric-difference cost is finite, so the `R+1` rows share almost the entire `0.6536D` crossing family. Its full angular defect is also finite, so deleting only `sigma D` columns makes this near-full common family inverse-`D` near-equilateral on **every row of the chain**.

Because the same column order occurs on every row, the circumdisk-capacity argument then produces common linear flank blocks which bracket the source circumcenter coordinate on all `R+1` rows simultaneously.

For the concrete choice `sigma=mu=0.01`, every fixed chain length occurs with one common family of more than

\[
0.6436D-o(D)
\]

columns, every crossing has angular defect less than

\[
{1.109\times10^8 R\over D},
\]

and the same first and last

\[
(0.0547027-o(1))D
\]

columns lie respectively below `-0.01D` and above `+0.01D` on **every row**.

This replaces the sparse `0.0783D` fixed-chain scaffold by a near-full common ladder whose density stays above the exact circumcenter-bracketing threshold `1/sqrt(3)` even after phase purification.

---

## Theorem FCB — dense phase-pure bracketing ladder through any fixed cusp depth

Fix an integer

\[
R\ge1
\tag{FCB.1}
\]

before taking `D->infinity`. Put

\[
r_0:=0.6536,
\qquad
H:=1{,}109{,}000.
\tag{FCB.2}
\]

Fix constants

\[
0<\sigma<r_0,
\qquad
\mu\ge0
\tag{FCB.3}
\]

such that

\[
\boxed{
q:=r_0-\sigma-{1+2\mu\over\sqrt3}>0.
}
\tag{FCB.4}
\]

Then along every unbounded high-`t` survivor sequence there are `R+1` consecutive nonhub selected O--O rows

\[
\tau_0,\tau_1,\ldots,\tau_R
\tag{FCB.5}
\]

whose intervening strips satisfy the usual fixed-cusp bounds and which additionally admit one common transverse train family `P_R` with the following properties.

### 1. Finite total local defect complexity

For the `R` intervening interfaces,

\[
\boxed{
\sum_{i=0}^{R-1}(N_i+L_i+D B_i)
<HR,
}
\tag{FCB.6}
\]

and if

\[
F_j:=\sum_{b\in\Gamma_j}\delta_{jb}
\tag{FCB.7}
\]

is the **full** angular-defect sum of row `tau_j` over all complete trains crossing that row, then

\[
\boxed{
\sum_{j=0}^{R}F_j<HR.
}
\tag{FCB.8}
\]

Here `Gamma_j` is the complete-train crossing family of `tau_j`, and `delta_jb>0` is the canonical acute strict-rhombus angular defect.

Consequently

\[
\sum_iN_i<HR,
\qquad
\sum_iL_i<HR,
\qquad
\sum_iB_i<{HR\over D}.
\tag{FCB.9}
\]

For fixed `R`, every quantity except the final KKT factor is therefore bounded independently of `D`.

### 2. Almost the full `0.6536D` crossing family is common to all rows

There is a family

\[
C_R\subseteq\bigcap_{j=0}^{R}\Gamma_j
\tag{FCB.10}
\]

with

\[
\boxed{|C_R|>r_0D-HR-o(D)=0.6536D-o(D).}
\tag{FCB.11}
\]

The trains in `C_R` are pairwise noncrossing and occur in one common order on every row `tau_j`.

### 3. Delete only `sigma D` columns to get inverse-`D` phase purity on the entire chain

There is

\[
P_R\subseteq C_R
\]

with

\[
\boxed{|P_R|>(r_0-\sigma)D-o(D)}
\tag{FCB.12}
\]

such that for every row `0<=j<=R` and every column `b in P_R`,

\[
\boxed{
0<\delta_{jb}
\le {K_R\over D},
\qquad
K_R:={HR\over\sigma}.
}
\tag{FCB.13}
\]

Thus a **single** common column shore is inverse-`D` near-equilateral across all `R+1` rows.

### 4. The same columns bracket the circumcenter on every row

There are an initial block `P_R^-` and a terminal block `P_R^+` in the common column order such that

\[
\boxed{|P_R^-|,|P_R^+|>(q-o(1))D.}
\tag{FCB.14}
\]

Orient each row so that the common column order increases the exact train-monotone coordinate

\[
h_j(x)=\det(u_j,x-o).
\tag{FCB.15}
\]

If `z_jb` is the crossing-rhombus center of `tau_j` and `b`, then simultaneously for **every** `0<=j<=R`,

\[
\boxed{h_j(z_{jb})<-\mu D\qquad(b\in P_R^-),}
\tag{FCB.16}
\]

\[
\boxed{h_j(z_{jb})>\mu D\qquad(b\in P_R^+).}
\tag{FCB.17}
\]

Every flank crossing still satisfies the inverse-`D` defect bound (FCB.13).

---

## 1. Replace the sparse-row defect term by the full row defect

Let

\[
A_*=(\tau_1,\ldots,\tau_m),
\qquad
m>cD-o(D),
\qquad
c=0.0000226,
\tag{FCB.18}
\]

be the consecutive high-`t` row block. For an internal interface put

\[
C_i:=N_i+L_i+D B_i.
\tag{FCB.19}
\]

The fixed-chain proof used row angular sums against a previously selected common column family. Instead define the full row defect `F_j` by (FCB.7). Every term of `F_j` is the canonical defect of one strict rhombus crossed by `tau_j`.

The canonical global budgets give

\[
\sum_i C_i
\le(10T-2\pi+2)D+o(D),
\tag{FCB.20}
\]

and

\[
\sum_j F_j
\le C_{phase}D,
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{FCB.21}
\]

Define the augmented interface cost

\[
\boxed{
J_i^{full}:=C_i+F_i+F_{i+1}.
}
\tag{FCB.22}
\]

Each row appears in at most two adjacent-interface costs, so

\[
\sum_iJ_i^{full}
\le
(10T-2\pi+2+2C_{phase})D+o(D).
\tag{FCB.23}
\]

This is **the same global constant** used in the existing fixed-cusp-chain theorem. Its exact arithmetic certificate already proves

\[
{10T-2\pi+2+2C_{phase}\over c}
<1{,}108{,}000
< H.
\tag{FCB.24}
\]

Thus charging the full row defect costs no new leading constant.

---

## 2. The same sliding-window lemma gives a full-defect cusp chain

Consider all admissible length-`R` windows of consecutive nonhub interfaces. Their number is

\[
cD-o(D)
\]

for fixed `R`. Every interface belongs to at most `R` such windows. Hence

\[
\sum_W\sum_{i\in W}J_i^{full}
\le
R\sum_iJ_i^{full}.
\tag{FCB.25}
\]

Averaging and using the strict margin in (FCB.24) gives one admissible window with

\[
\boxed{
\sum_{i=0}^{R-1}J_i^{full}<HR
}
\tag{FCB.26}
\]

for all sufficiently large `D`.

Its `C_i` part gives (FCB.6). Moreover

\[
\sum_{i=0}^{R-1}(F_i+F_{i+1})
=F_0+2\sum_{j=1}^{R-1}F_j+F_R
\ge\sum_{j=0}^{R}F_j,
\]

so (FCB.26) also gives (FCB.8).

This is stronger than the previous fixed-chain phase statement: the bounded defect is now over **every complete train crossing every selected row**, not only over a pre-thinned `0.1567D` or `0.0783D` common column shore.

---

## 3. Finite terminal variation forces one near-full common train family

Each selected high-`t` row satisfies

\[
|\Gamma_j|>r_0D-o(D).
\tag{FCB.27}
\]

The adjacent-strip terminal-topology theorem gives

\[
|\Gamma_j\triangle\Gamma_{j+1}|\le L_j.
\tag{FCB.28}
\]

Start with `Gamma_0`. Passing from row `j` to row `j+1` can remove at most `L_j` trains from the running intersection. Therefore

\[
\left|\bigcap_{j=0}^{R}\Gamma_j\right|
\ge
|\Gamma_0|-\sum_{j=0}^{R-1}L_j.
\tag{FCB.29}
\]

Using (FCB.9) and (FCB.27),

\[
\boxed{
\left|\bigcap_{j=0}^{R}\Gamma_j\right|
>r_0D-HR-o(D).
}
\tag{FCB.30}
\]

Take this intersection as `C_R`.

Any two trains in `C_R` both cross `tau_0`. The complete-train crossing graph is triangle-free, so they cannot cross each other. Since all rows are noncrossing and every row crosses every column exactly once, the standard pseudoline order lemma gives one common column order on all `R+1` rows, after orienting the rows consistently.

For fixed `R`, the finite loss `HR` is absorbed by `o(D)`, giving the asymptotic density `r_0=0.6536` in (FCB.11).

---

## 4. Full-defect boundedness purifies the near-full common family

For `b in C_R`, define its total chain defect

\[
\Delta_b:=\sum_{j=0}^{R}\delta_{jb}.
\tag{FCB.31}
\]

Because `C_R subset Gamma_j` for every row,

\[
\sum_{b\in C_R}\Delta_b
\le
\sum_{j=0}^{R}F_j
<HR.
\tag{FCB.32}
\]

Call `b` bad when

\[
\Delta_b>{HR\over\sigma D}={K_R\over D}.
\tag{FCB.33}
\]

There can be fewer than `sigma D` bad columns, since otherwise their total contribution would exceed `HR`.

Delete them and call the remainder `P_R`. From (FCB.11),

\[
|P_R|>(r_0-\sigma)D-HR-o(D)
=(r_0-\sigma)D-o(D),
\]

which is (FCB.12).

For every retained `b`, each individual nonnegative row defect is bounded by the total:

\[
0<\delta_{jb}\le\Delta_b\le{K_R\over D}.
\]

This proves (FCB.13).

The important point is that the deletion is by **columns**, after the entire chain is fixed. The same retained column set is phase-pure on every row; no intersection of separately purified row families is needed.

---

## 5. Circumdisk capacity gives flanks common to all `R+1` rows

Deleting columns preserves pairwise noncrossing and the common column order. The exact train-step metric inequality gives, along every oriented row,

\[
h_j(z_{j,s+1})-h_j(z_{j,s})>{\sqrt3\over2}
\tag{FCB.34}
\]

for consecutive retained columns in their common order.

The full source hull lies in

\[
B(o,R_D),
\qquad
R_D<{D\over2}+o(D).
\tag{FCB.35}
\]

Hence, on any one row, at most

\[
\left({1+2\mu\over\sqrt3}+o(1)\right)D
\tag{FCB.36}
\]

retained crossings can lie at coordinate at least `-mu D`; the symmetric statement holds at coordinate at most `+mu D`.

Since

\[
|P_R|>(r_0-\sigma)D-o(D),
\]

every row has more than

\[
\left(r_0-\sigma-{1+2\mu\over\sqrt3}-o(1)\right)D
=(q-o(1))D
\]

retained crossings below `-mu D`, and the same number above `+mu D`.

On every row, the below-set is an initial segment of the **same** column order. Therefore the first `(q-o(1))D` labels work simultaneously on all `R+1` rows. Likewise the final `(q-o(1))D` labels work above `+mu D` on all rows. These are `P_R^-` and `P_R^+`, proving (FCB.14)--(FCB.17).

---

## 6. Concrete `sigma=mu=0.01` specialization

Take

\[
\sigma=\mu={1\over100}.
\tag{FCB.37}
\]

Then

\[
\boxed{|P_R|>0.6436D-o(D).}
\tag{FCB.38}
\]

The common flank density is

\[
\boxed{
q=0.6436-{1.02\over\sqrt3}
=0.0547027254265\ldots .
}
\tag{FCB.39}
\]

The angular-defect coefficient is

\[
\boxed{
K_R={1{,}109{,}000R\over0.01}
=110{,}900{,}000R.
}
\tag{FCB.40}
\]

Thus for each fixed `R`, all `R+1` rows carry the same `>0.6436D` columns, every one of their `(R+1)|P_R|` crossings satisfies

\[
0<\delta<{1.109\times10^8R\over D},
\]

and the same `>0.05470D` first/last columns bracket the `+-0.01D` circumcenter corridor on every row.

At the same time the entire chain has fewer than `1,109,000R` switching support changes, fewer than the same number of assigned terminal face-side occurrences, and total switching KKT mass below `1,109,000R/D`.

---

## 7. Fixed-depth limit and growing-depth diagonal

For fixed `R`, (FCB.13) tends to exact `pi/3` crossing geometry uniformly on the whole retained `R+1` by `Theta(D)` grid, while (FCB.6)--(FCB.9) keep all non-rhombic/switching defect complexity finite. Thus every fixed depth has a genuine compact limiting model consisting of an exact triangular train ladder plus only finitely many switching/terminal defects.

The standard diagonal argument can also choose a subsequence with depths

\[
R_D\to\infty
\]

arbitrarily slowly. Choosing it slowly enough that `HR_D=o(D)` preserves

\[
|P_{R_D}|>(0.6436-o(1))D,
\]

and the same positive flank density. The per-crossing defect bound then becomes

\[
O(R_D/D)=o(1).
\]

This diagonal statement is weaker than inverse-`D` control with a fixed constant, but it produces a growing-depth near-triangular corridor with a near-full common transverse shore and sublinear total switching/terminal complexity.

---

## 8. Frontier effect

The previous fixed-cusp-chain theorem left a cardinality mismatch:

```text
finite-depth KKT cusp chain
+ only 0.0783D common phase-controlled columns.
```

The new full-defect sliding window removes that mismatch:

```text
arbitrarily long fixed cusp chain
+ <1,109,000R total switching/terminal complexity
+ <1,109,000R/D total switching KKT mass
+ >0.6436D columns common to every row
+ inverse-D near-equilateral on every crossing
+ >0.05470D common columns on each side of the source circumcenter.
```

The next closing target is therefore finite and more rigid: classify the fixed-`R` limit of switching diameter intervals inside an exact triangular `R+1` by continuum-width ladder, then show that the classification cannot persist as `R` increases. The old possibility that the finite cusp lived inside a sparse or unrelated transverse scaffold is eliminated.

No such final classification is proved here. C-II remains open.

**Disposition:** strengthened every fixed high-`t` cusp chain to carry one near-full common transverse ladder which is simultaneously inverse-`D` near-equilateral and circumcenter-bracketing on all rows. The full angular-defect charge fits inside the existing fixed-chain budget, so no new leading constant is paid.