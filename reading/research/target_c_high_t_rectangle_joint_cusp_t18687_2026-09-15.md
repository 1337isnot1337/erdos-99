> Generated reading edition · [exact source](../../research/target_c_high_t_rectangle_joint_cusp_t18687_2026-09-15.md) · source SHA-256 `9a88f748bde245709a990de8d808783124ffb4f4645f0c93ca887436668758e6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e934e1807b08f42ac4d2a176fb547eac34b6ae32", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_rectangle_joint_cusp_t18687_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5f56ae53dde1ac59d0c2c32f9ad2a69fba9b5c686cfbfd7759bd60d198ea1091"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — one finite KKT cusp sits inside the high-`t` macroscopic rectangle

**Date:** 2026-09-15  
**Status:** proof-only high-`t` finite-cusp strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` complete rectangle; high-`t` rectangle orientation extraction; finite-defect/KKT global budgets; canonical angular-defect budget; path Helly hub and strip-reaction nondegeneracy  
**Certificate:** `research/verify_target_c_high_t_rectangle_joint_cusp_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The high-`t` rectangle contains a consecutive row block

$$
A_*=(\tau_1,\ldots,\tau_m),
\qquad m>0.0000226D-o(D),
$$

and, after deleting only `O(1)` orientation-ambiguous transverse trains and choosing the larger oriented side, a common column family

$$
B_+,
\qquad |B_+|>0.1567D-o(D),
$$

such that every row crosses every column.

This note spends four global currencies on one **adjacent row pair inside this same complete rectangle**:

1. actual diameter interval starts/stops;
2. complete-stopped-train terminal occurrences;
3. switching diameter KKT mass;
4. the angular defect of the two rows against the common columns.

For some nonhub adjacent pair

$$
\tau_i,\tau_{i+1}
$$

one has

$$
\boxed{
N_i+L_i+D B_i+S_i+S_{i+1}<1{,}109{,}000,
}
\tag{JC.1}
$$

where

- `N_i` is the number of actual diameter intervals starting or stopping at the interface;
- `L_i` is the number of stopped-train terminal face-side occurrences in the intervening region;
- `B_i` is the switching KKT diameter multiplier mass;
- `S_j` is the total angular defect of row `tau_j` against all columns in `B_+`.

Consequently the same adjacent pair has

$$
N_i,L_i\le1{,}108{,}999,
\qquad
B_i<{1{,}109{,}000\over D},
\tag{JC.2}
$$

$$
\|F_{i+1}-F_i\|<1{,}109{,}000,
\tag{JC.3}
$$

and projective row-phase gap

$$
\boxed{
d_{\mathbb{RP}^1}(u_i,u_{i+1})
<{7.08\times10^6\over D}+o(D^{-1}).}
\tag{JC.4}
$$

Moreover, after discarding at most half of `B_+`, there remains a common transverse family

$$
B_0,
\qquad
\boxed{|B_0|>0.0783D-o(D),}
\tag{JC.5}
$$

such that every `b in B_0` crosses **both** selected rows with angular excess

$$
\boxed{
0<\theta(\tau_i,b)-{\pi\over3},
\theta(\tau_{i+1},b)-{\pi\over3}
<{1.416\times10^7\over D}+o(D^{-1}).
}
\tag{JC.6}

The columns in `B_0` are pairwise noncrossing and occur in the same order along both rows. Thus the unresolved high-`t` obstruction is now a bounded-complexity KKT/terminal cusp embedded in a macroscopic ordered near-triangular ladder.

---

## 1. Global finite-defect/KKT budget restricted to the rectangle block

For an internal row interface put

\[
C_i:=N_i+L_i+D B_i.
$$

The already-audited global budgets give

$$
\sum_iN_i\le2\pi D,
$$

$$
\sum_iL_i\le(10T-4\pi)D+o(D),
$$

and

$$
\sum_iD B_i\le2D.
$$

Therefore, even after restricting to the rectangle block,

$$
\boxed{
\sum_{i\in A_*}C_i
\le(10T-2\pi+2)D+o(D).
}
\tag{JC.7}

At `T=1.8687`, the coefficient is

\[
10T-2\pi+2=14.40381469\ldots .
$$

---

## 2. Two-row angular-defect budget

Use the consistent oriented representatives from the rectangle phase theorem. For a row `tau_j` and column `b in B_+`, write

$$
\delta_{jb}
:=\theta(\tau_j,b)-{\pi\over3}>0
$$

on the common oriented branch, and set

$$
S_j:=\sum_{b\in B_+}\delta_{jb}.
\tag{JC.8}
$$

All these crossings are distinct strict rhombi. Hence the canonical global angular-defect budget gives

$$
\sum_jS_j<C_{phase}D,
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{JC.9}
$$

Summing adjacent two-row costs,

$$
\boxed{
\sum_j(S_j+S_{j+1})<2C_{phase}D.
}
\tag{JC.10}
$$

---

## 3. Joint averaging on the consecutive rectangle rows

For each internal rectangle interface define

$$
J_i:=C_i+S_i+S_{i+1}.
\tag{JC.11}
$$

Delete the unique hub region if it lies inside the block, and delete the `O(1)` end indices. This changes the available row-boundary count by only `O(1)`, while

$$
|A_*|>0.0000226D-o(D).
$$

By (JC.7) and (JC.10),

$$
\sum_iJ_i
<\left(10T-2\pi+2+2C_{phase}\right)D+o(D).
$$

The exact certificate proves

$$
{10T-2\pi+2+2C_{phase}\over0.0000226}
<1{,}108{,}000.
\tag{JC.12}
$$

Thus for every sufficiently large source some eligible nonhub interface satisfies the deliberately rounded bound

$$
J_i<1{,}109{,}000.
$$

This proves (JC.1)--(JC.2).

The exact Section-157 cut resultants are

$$
F_j=\sum_h\beta_h\varepsilon_{hj}r_h,
\qquad |r_h|=D.
$$

Therefore

$$
\|F_{i+1}-F_i\|
\le D B_i,
$$

which gives (JC.3). The reverse triangle inequality also gives

$$
|A_{i+1}-A_i|<1{,}109{,}000.
$$

---

## 4. The selected rows are inverse-`D` phase-close

Let their real oriented contact phases be `alpha_i,alpha_{i+1}`. For every common column `b`,

$$
\delta_{ib}-\delta_{i+1,b}
=\alpha_{i+1}-\alpha_i.
$$

Hence

$$
|\alpha_{i+1}-\alpha_i|
\le\delta_{ib}+\delta_{i+1,b}.
$$

Sum over `B_+`:

$$
|B_+|\,|\alpha_{i+1}-\alpha_i|
\le S_i+S_{i+1}
<1{,}109{,}000.
$$

Using

$$
|B_+|>0.1567D-o(D),
$$

the exact certificate yields

$$
|\alpha_{i+1}-\alpha_i|
<{7.08\times10^6\over D}+o(D^{-1}),
$$

which is (JC.4).

---

## 5. A macroscopic uniformly near-triangular transverse scaffold

For `b in B_+` put

$$
x_b:=\delta_{ib}+\delta_{i+1,b}\ge0.
$$

Then

$$
\sum_{b\in B_+}x_b=S_i+S_{i+1}<1{,}109{,}000.
$$

By Markov, at least half of `B_+` satisfies

$$
x_b\le{2(1{,}109{,}000)\over|B_+|}.
$$

Call this retained family `B_0`. Then

$$
|B_0|>|B_+|/2>0.0783D-o(D),
$$

and the exact certificate gives

$$
x_b<{1.416\times10^7\over D}+o(D^{-1}).
$$

Since each summand in `x_b` is nonnegative, both individual row-column angular defects satisfy (JC.6).

All columns of `B_0` already belonged to the internally noncrossing oriented rectangle family. The signed monotone-grid order lemma therefore gives the same column order along both selected rows.

---

## 6. The same pair retains the finite-strip topology

The selected interface is nonhub. Hence every switching actual diameter interval is one-sided toward the common diameter-routing hub.

The region contains at most

$$
\left\lfloor{1{,}108{,}999\over5}\right\rfloor
=221{,}799
$$

bounded nonquadrilateral faces, because each contributes at least five terminal face-side incidences.

The terminal-topology argument gives

$$
|\Gamma(\tau_i)\triangle\Gamma(\tau_{i+1})|
\le L_i\le1{,}108{,}999.
$$

The exact layer reaction is nonzero by adjacent-strip reaction nondegeneracy and is generated by one or two actual switching diameter bars by planar conic Caratheodory.

Thus one source-level adjacent row pair simultaneously has

```text
>0.0783 D ordered common transverse trains
+ both row-column angle excesses O(1/D)
+ row-row phase gap O(1/D)
+ <=1,108,999 switching diameter rows
+ switching KKT mass <1,109,000/D
+ cut-resultant jump <1,109,000
+ <=1,108,999 train-terminal occurrences
+ <=221,799 bounded exceptional faces
+ one-sided hub switching
+ exact nonzero reaction generated by <=2 diameter bars.
```

This is the high-`t` analogue of the earlier low-`t` finite cusp, but now it sits inside a macroscopic ordered near-triangular crossing scaffold.

The remaining obligation is to use the scaffold, rather than only the bounded defect counts, to eliminate the one/two-bar reaction or construct a source-preserving diameter-decreasing local multishear.

No C-II or Level-I closure is claimed.

**Disposition:** proved proof-only finite KKT cusp embedded in the high-`t` complete rectangle through `t<=1.8687`. C-II and Level I remain open.
