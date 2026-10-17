> Generated reading edition · [exact source](../../research/target_c_high_t_growing_fully_loaded_force_corridor_t18687_2026-09-17.md) · source SHA-256 `b198deeffe590361615d9e67704467ae4cdb60f84e40f0e260ed8976001fd1d5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cbf0b9c6e9bbc75718ba8750267351a4e196370b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_growing_fully_loaded_force_corridor_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a406ce7ddbc570ae8613d39ff4ea6fd636b5104fe239c02c4a5d8037ced92171"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a growing exact-phase corridor can be force-loaded at every interface

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** canonical one-sided high-`t` survivor through `t=(q-k)/D<=1.8687`  
**Dependencies:** growing exact-phase force-block dichotomy; threshold-free exact-force-pair narrow-capacity argument; bilateral birth-loading inequality; wide-dipole central-diamond theorem; coupled host-margin sharpening; common inverse-`D` column family and additive phase decomposition  
**Certificate:** `research/verify_target_c_high_t_growing_fully_loaded_force_corridor_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing growing-block theorem gives a consecutive exact-phase run whose length tends to infinity, but only proves that a growing number of its interfaces carry a **fixed-angle** exact force diamond. It does not force a force diamond at every interface of one growing run.

There is a useful complementary diagonal. Let the pair-angle threshold decrease sufficiently slowly. The exact-antipodal force-pair packing theorem then makes the narrow-pair interfaces sublinear, while the central-diamond midpoint error is still much smaller than the decreasing angular scale. Removing the resulting sublinear exceptional set leaves a growing consecutive run on which **every** internal interface carries a bilateral force-generating diameter pair.

The same run can be taken from the `slow-good` exact population of the growing-block theorem. Consequently every internal interface also has `J_i<C\sqrt D`. Exact phase then propagates one `O(D^{-1/2})` row-column defect bound across the whole run against the same global column family `B_0`.

Put

$$
c={113\over5{,}000{,}000},
\qquad
C=1{,}109{,}000,
\qquad
c_H=0.453819885927\ldots .
\tag{FC.1}
$$

Here `c_H` is the sharpened coupled-host transverse constant.

---

## Theorem FC — growing fully loaded force corridor

Assume the positive-density non-antipodal TB1 alternative does not occur. After passing to a subsequence, there exist

- a sequence `rho_D>0` with
  $$
  \boxed{\rho_D\to0,
  \qquad \rho_DD^{1/4}\to\infty,}
  \tag{FC.2}
  $$
- and a consecutive one-sided interface block
  $$
  I_D^{\rm force}=[p_D,q_D]
  \tag{FC.3}
  $$
  whose length
  $$
  \boxed{R_D:=q_D-p_D+1\to\infty,}
  \tag{FC.4}
  $$

such that every internal interface `i in I_D^{force}` simultaneously has the following properties.

### 1. Every interface is slow-good and exactly antipodal

$$
\boxed{J_i<C\sqrt D,}
\tag{FC.5}
$$

and all rows in the corridor have one exact oriented phase,

$$
\boxed{
u_{p_D}=u_{p_D+1}=\cdots=u_{q_D+1}=:v_D.}
\tag{FC.6}
$$

In particular,

$$
N_i,L_i<C\sqrt D,
\qquad
B_i<{C\over\sqrt D},
\qquad
S_i+S_{i+1}<C\sqrt D,
\qquad
0<|G_i|<C\sqrt D.
\tag{FC.7}
$$

### 2. Every interface has a `rho_D`-wide exact force pair

There are two switching actual diameter bars with unit directions `d_i^-,d_i^+` such that

$$
\boxed{
G_i
=D\bigl(\lambda_i^-d_i^-+\lambda_i^+d_i^+\bigr),
\qquad
\lambda_i^\pm>0,
}
\tag{FC.8}
$$

and

$$
\boxed{
d_{\mathbb{RP}^1}([d_i^-],[d_i^+])\ge\rho_D.}
\tag{FC.9}
$$

The two birth endpoints lie on opposite ordered host subarcs. Switching supports at distinct corridor interfaces are disjoint, so all selected force bars at different interfaces are distinct.

### 3. Every pair forms a super-`D^(3/4)` central diamond

Let

$$
L_D=O(D^{3/4})
$$

be the common source midpoint error. The diagonal can be chosen so slowly that, in addition to (FC.2),

$$
2L_D\le {1\over2}D\sin{\rho_D\over2}
\tag{FC.10}
$$

for all sufficiently large retained sources. Hence every selected pair has four distinct endpoints, the two diameter bars cross, and its four-endpoint hull contains

$$
\boxed{
B\!\left(o,{D\over2}\sin{\rho_D\over2}-L_D\right).
}
\tag{FC.11}
$$

If `r_D^{cent}` denotes the radius in (FC.11), then

$$
\boxed{
r_D^{cent}=o(D),
\qquad
{r_D^{cent}\over D^{3/4}}\to\infty.}
\tag{FC.12}
$$

The two diagonals intersect within

$$
\left(1+{2\over\sin\rho_D}\right)L_D=o(D)
\tag{FC.13}
$$

of the common source circumcenter. Thus the pair angle tends to zero, but much more slowly than the source midpoint-error scale: every interface still carries a genuinely large central diamond.

### 4. Every selected force ray keeps a fixed transverse margin

The coupled host theorem is pointwise and does not deteriorate with `rho_D`. Therefore

$$
\boxed{
|d_i^\pm\cdot Jv_D|
\ge c_H-o(1)
=0.453819885927\ldots-o(1).}
\tag{FC.14}
$$

The elementary antipodal dipole coordinate has opposite-sign squared-length slopes satisfying

$$
\boxed{
|\ell_{h_i^\pm}(s d^{(i)})|
\ge(0.907639771854\ldots-o(1))D|s|.}
\tag{FC.15}
$$

The exact force coefficients obey

$$
\boxed{
(c_H-o(1)){|G_i|\over D}
\le\lambda_i^\pm
\le {C\over\sqrt D\,\sin\rho_D}.}
\tag{FC.16}
$$

Because `rho_DD^{1/4}->infinity`, the upper bound in (FC.16) tends to zero; in fact it is `o(D^{-1/4})`. This is only a bound on the two-ray compression coefficients, not a positive lower bound on the original KKT multipliers.

### 5. One common linear column family is uniformly `O(D^(-1/2))`-equilateral through the whole corridor

Use the global family `B_0` from the common-grid theorem:

$$
\boxed{|B_0|>0.0783D-o(D).}
\tag{FC.17}
$$

Choose any internal corridor interface `i`. From (FC.5),

$$
S_i<C\sqrt D.
$$

The additive rectangle decomposition and the global `B_0` column bound give

$$
0<\theta(\tau_i,b)-{\pi\over3}
<
{C\over0.1567\sqrt D}
+{3.004\times10^6\over D}
+o(D^{-1/2})
\tag{FC.18}
$$

for every `b in B_0`. Every row in (FC.6) has exactly the same oriented phase, so the same estimate holds on **every row of the growing corridor**:

$$
\boxed{
0<\theta(\tau_j,b)-{\pi\over3}
< {7.078\times10^6+o(1)\over\sqrt D}
}
\tag{FC.19}
$$

uniformly for

$$
p_D\le j\le q_D+1,
\qquad b\in B_0.
$$

The rows are internally noncrossing, the columns are internally noncrossing, every cross-pair meets once, and the inherited determinant sign is common. Thus this is one ordered growing near-equilateral train rectangle, not separate local grids.

### 6. All exact reactions are co-axial and strictly ordered

Write

$$
F_j=A_jv_D,
\qquad A_j>0.
$$

The one-sided separation functional gives

$$
\boxed{
A_{p_D}>A_{p_D+1}>\cdots>A_{q_D+1}
}
\tag{FC.20}
$$

up to reversing the common orientation convention. All `G_i` point in the same ordinary direction and telescope:

$$
\boxed{
\sum_{i=p_D}^{q_D}|G_i|
=|A_{p_D}-A_{q_D+1}|<D.}
\tag{FC.21}
$$

So the fully loaded corridor carries a growing ordered stack of exact positive force dipoles whose total axial reaction remains below one diameter scale.

---

## 1. Start from the asymptotically full slow-good exact population

On the no-TB1 branch, the growing exact-phase theorem proves that the one-sided shore `I_D` has

$$
|I_D|>{c\over2}D-o(D)
\tag{FC.22}
$$

and that all but `o(D)` of its interfaces are **slow-good exact-antipodal**:

$$
E_D^{slow}
=\{i:\ J_i<C\sqrt D\text{ and }i\text{ is exact-antipodal}\},
$$

$$
\boxed{|I_D\setminus E_D^{slow}|=o(D).}
\tag{FC.23}
$$

At every member of `E_D^{slow}`, choose the exact positive force pair from the antipodal force-pair theorem.

---

## 2. Diagonalize the narrow-pair capacity above the midpoint-error scale

For every fixed `rho>0`, the threshold-free narrow exact-force-pair packing argument gives

$$
N_D^{narrow}(\rho)
\le2\rho D+o(D).
\tag{FC.24}
$$

The proof uses only the common one-sided open semicircle, opposite transverse signs of the exact pair, the shrinking common row-axis window, disjoint switching supports, and C67 diameter-direction separation. It does not use a fixed local cost threshold.

For integers `k>=2`, put

$$
\rho_k={1\over k}.
$$

Choose an increasing sequence of source thresholds `D_k` so large that whenever a retained source has `D>=D_k`, all of the following hold:

$$
N_D^{narrow}(\rho_k)\le {3D\over k},
\tag{FC.25}
$$

$$
D^{1/4}\ge k^2,
\tag{FC.26}
$$

and

$$
2L_D\le {1\over2}D\sin{1\over2k}.
\tag{FC.27}
$$

This is possible because (FC.24) holds for each fixed `k`, `L_D/D=O(D^{-1/4})->0`, and `D^{1/4}->infinity`.

For `D_k<=D<D_{k+1}`, set

$$
\rho_D={1\over k}.
\tag{FC.28}
$$

Then `k=k(D)->infinity`, so

$$
\rho_D\to0,
\qquad
\rho_DD^{1/4}\ge k\to\infty,
$$

and (FC.25) gives

$$
\boxed{N_D^{narrow}(\rho_D)=o(D).}
\tag{FC.29}
$$

This proves the angular part of the diagonal without assuming any quantitative rate for the original shrinking row-phase window.

---

## 3. Bilateral failures are also sublinear on this diagonal

For a `rho_D`-wide exact pair, the bilateral birth-loading inequality is exact:

$$
N_D^{same}
\left(D\sin{\rho_D\over2}-2L_D\right)
\le\pi D.
\tag{FC.30}
$$

By (FC.27),

$$
D\sin{\rho_D\over2}-2L_D
\ge {1\over2}D\sin{\rho_D\over2}.
$$

Therefore

$$
N_D^{same}
\le {2\pi\over\sin(\rho_D/2)}
=O(k(D)).
\tag{FC.31}
$$

Since `D>=D_k` and (FC.26) imply `D>=k^8`,

$$
\boxed{N_D^{same}=o(D).}
\tag{FC.32}
$$

The same inequality also gives positive cross-pair endpoint separation, so the selected pair cannot share an endpoint and its two diameter bars cross.

---

## 4. Remove a sublinear exceptional set and take the longest run

Let `Z_D` be the union of

1. the non-slow-good or nonexact interfaces `I_D\setminus E_D^{slow}`;
2. the `rho_D`-narrow exact-force interfaces;
3. the `rho_D`-wide interfaces whose two birth endpoints lie on the same host side.

By (FC.23), (FC.29), and (FC.32),

$$
\boxed{|Z_D|=o(D).}
\tag{FC.33}
$$

Hence the complement has

$$
\boxed{|I_D\setminus Z_D|>{c\over2}D-o(D).}
\tag{FC.34}
$$

The complement is a union of at most `|Z_D|+1=o(D)` maximal consecutive runs. Therefore the longest run has length at least

$$
{|I_D\setminus Z_D|\over |Z_D|+1}\longrightarrow\infty.
\tag{FC.35}
$$

Choose that run as `I_D^{force}`. By construction every internal interface satisfies (FC.5), (FC.8)--(FC.10), and bilateral birth. Exact antipodality throughout the run gives (FC.6) and the reaction ordering (FC.20)--(FC.21).

---

## 5. Metric and grid consequences

From (FC.10),

$$
r_D^{cent}
={D\over2}\sin{\rho_D\over2}-L_D
\ge {D\over4}\sin{\rho_D\over2}.
\tag{FC.36}
$$

For small `rho_D`, `sin(rho_D/2)` is comparable to `rho_D`. Thus (FC.2) gives

$$
{r_D^{cent}\over D^{3/4}}
\gg \rho_DD^{1/4}\to\infty,
$$

while `rho_D->0` gives `r_D^{cent}/D->0`. This proves (FC.12). The central-intersection estimate divided by `D` is

$$
O\!\left({D^{-1/4}\over\rho_D}\right)=o(1),
$$

which proves (FC.13).

The sharpened host theorem gives (FC.14)--(FC.16) pointwise. The upper force-coefficient bound uses `|G_i|<C sqrt(D)` from slow-goodness and `sin(p_i+q_i)>=sin(rho_D)` in the exact two-ray sine law.

For the common grid, the global `B_0` family is crossed by every row in the one-sided rectangle. The additive phase formula gives

$$
g+r_i\le {S_i\over|B_+|},
\qquad
|B_+|>0.1567D-o(D),
$$

and every `b in B_0` has

$$
q_b<{3.004\times10^6\over D}+o(D^{-1}).
$$

Use `S_i<C sqrt(D)` to get (FC.18). Exact phase makes the left side identical on every corridor row, giving (FC.19). Numerically,

$$
{C\over0.1567}=7{,}077{,}217.6\ldots,
$$

so `7.078e6` is a safe readable coefficient in (FC.19).

---

## 6. Frontier effect

The no-TB1 branch now contains one genuinely consecutive growing object with no sparse internal force gaps:

```text
R_D -> infinity consecutive exact-phase interfaces;
every interface slow-good;
every interface has a bilateral exact positive force pair;
pair gap rho_D -> 0 but rho_D D^(1/4) -> infinity;
every force diamond contains a central ball of radius omega(D^(3/4));
every diagonal crossing point is o(D) from the common center;
every force ray has fixed transverse component >=0.453819...;
all rows cross the same >0.0783D columns with O(D^(-1/2)) angle defect;
all exact reactions are co-axial, strictly ordered, and telescope to <D.
```

This is stronger in a different direction from the almost-linear tagged-resultant ladder: that theorem has much greater depth and denser common columns, while the present corridor forces an actual positive two-diameter reaction certificate at **every** internal interface.

C-II remains open because the positive force scale can still vanish from interface to interface. The remaining local obstruction is now precise: show that a growing exact-phase near-equilateral strip corridor cannot support a bilateral central diameter force dipole at every separator with fixed transverse slope but vanishing KKT scale. A second-order critical-cone or ordered-normal argument can now be applied without first paying for missing force interfaces.

**Disposition:** upgraded the no-TB1 growing exact-phase branch from “growing many fixed-angle force diamonds” to one growing consecutive corridor in which every interface carries a bilateral central exact force pair, with super-`D^(3/4)` central diamonds and one common `O(D^(-1/2))` train grid. No closure is claimed.
