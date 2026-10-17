> Generated reading edition · [exact source](../../research/target_c_high_t_unconditional_max_aperture_corridor_t18687_2026-09-17.md) · source SHA-256 `1f31ed3f4ed329b4c5aa4a0d167b62604613e9f4ff8ac3bef1298a1401d7e3cb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8d7e7a0d37b5082d06c0871f5e0916ed1ccd21f0", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_unconditional_max_aperture_corridor_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "47710be05dab284d5ec80929df4341d63c7f8197b8c61b30c85524c5ff2799f1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — an unconditional near-maximal-aperture vanishing-mass corridor

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the no-positive-density-TB1 near-full paired exact-force shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** near-full paired-shore construction with `o(D)` physical holes; ordered bilateral narrow-pair capacity; global one-sided reaction budget; coercive cancellation-kernel theorem; dense-force-grid synchronization  
**Certificate:** `research/verify_target_c_high_t_unconditional_max_aperture_corridor_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current fixed-aperture corridor theorem separates a terminal-dominant branch from a positive-density non-TT return branch. The ordered two-lane capacity theorem makes that separation unnecessary for corridor existence.

The near-full paired population has density

$$
\nu={113\over10{,}000{,}000}=1.13\times10^{-5}.
$$

For any fixed projective aperture `rho<gamma_H`, the ordered bilateral theorem says that the number of force pairs with gap below `rho` is at most

$$
{\rho\over2}D+o(D).
$$

Therefore, for every fixed `0<epsilon<1`, choosing

$$
\rho_\epsilon=(1-\epsilon)c,
\qquad
c:=2\nu={113\over5{,}000{,}000}=2.26\times10^{-5},
$$

leaves more than

$$
\epsilon\nu D-o(D)
$$

paired centers whose force-pair gap is at least `rho_epsilon`. The narrow pairs form an initial segment in the ordered force population, so the surviving wide pairs form a suffix. Because the paired construction has only `o(D)` physical holes, that wide suffix contains arbitrarily many long consecutive physical interface blocks.

Averaging the global one-sided KKT budget over those blocks then gives a growing consecutive block with vanishing total switching mass. All previous exact-phase, coercivity, and dense-grid conclusions apply to that same block.

Consequently the no-TB1 branch always contains a fixed-aperture vanishing-mass dense-force corridor. No terminal/nonterminal destination hypothesis is needed.

Moreover, diagonalizing `epsilon->0` gives a corridor sequence whose uniform force-pair aperture satisfies

$$
\boxed{
\eta_i\ge c-o(1)
=2.26\times10^{-5}-o(1)
}
$$

at every separator. This is twice the previous full-parent non-TT aperture `nu`.

The corresponding common central-diamond radius is

$$
\boxed{
\left({1\over2}\sin{c\over2}-o(1)\right)D
=(5.64999999988\ldots\times10^{-6}-o(1))D.
}
$$

---

## 1. Ordered narrow-pair capacity at an arbitrary fixed threshold

Use the near-full paired exact-force population on one fixed side of the common hub,

$$
i_1<i_2<\cdots<i_N<k,
\qquad
N>(\nu-o(1))D,
\tag{MC.1}
$$

with

$$
\nu={c\over2},
\qquad
c={113\over5{,}000{,}000}.
\tag{MC.2}
$$

At every paired center let

$$
\eta_s
=d_{\mathbb{RP}^1}([d_s^A],[d_s^B])
\tag{MC.3}
$$

be the projective gap of the exact positive force pair.

The ordered bilateral theorem supplies

$$
\delta_D=2\arcsin{1\over2D}
\tag{MC.4}
$$

and, for every fixed `0<rho<gamma_H`,

$$
\boxed{
N_D^{\rm narrow}(\rho)
\le {\rho\over2\delta_D}+1.
}
\tag{MC.5}
$$

Since

$$
\delta_D\ge{1\over D},
\tag{MC.6}
$$

this gives the finite upper bound

$$
\boxed{
N_D^{\rm narrow}(\rho)
\le {\rho D\over2}+1.
}
\tag{MC.7}
$$

The same theorem proves more than cardinality: all `rho`-narrow pairs form an initial segment of the ordered exact-force population. Hence, after restricting to the paired centers in (MC.1), the pairs with

$$
\eta_s\ge\rho
\tag{MC.8}
$$

form a suffix in paired-center order.

---

## 2. Any fixed fraction of the maximal threshold leaves linear wide density

Fix

$$
0<\epsilon<1
\tag{MC.9}
$$

and put

$$
\boxed{
\rho_\epsilon
=(1-\epsilon)c
=2(1-\epsilon)\nu.
}
\tag{MC.10}
$$

The constant `c=2.26e-5` is many orders of magnitude below `gamma_H=0.471...`, so the ordered capacity theorem applies.

By (MC.1) and (MC.7), the number `W_D(epsilon)` of paired centers with gap at least `rho_epsilon` satisfies

$$
\begin{aligned}
W_D(\epsilon)
&\ge N-N_D^{\rm narrow}(\rho_\epsilon)\\
&>(\nu-o(1))D-(1-\epsilon)\nu D-1.
\end{aligned}
\tag{MC.11}
$$

Therefore

$$
\boxed{
W_D(\epsilon)
>(\epsilon\nu-o(1))D.
}
\tag{MC.12}
$$

This estimate is independent of the TT/mixed/OO destination word. In particular:

- `epsilon=1/2` gives aperture `rho=nu=1.13e-5` on a suffix of density at least `nu/2=5.65e-6`;
- smaller fixed `epsilon` gives aperture arbitrarily close to `c=2.26e-5`, while retaining a positive linear suffix.

The factor `2` in the limiting aperture comes exactly from the two-lane narrow-pair capacity `rho D/2`.

---

## 3. The wide suffix has only `o(D)` physical holes

Use the construction-level interpretation audited for the near-full paired diagonal. It begins with a consecutive physical one-sided shore `I_D` and obtains the paired population by explicit deletion, with

$$
\boxed{
H_D:=|I_D\setminus P_D|=o(D).
}
\tag{MC.13}
$$

The wide paired centers form a suffix of `P_D`. Take the physical interface interval from the first wide paired center through the last paired center. This interval contains all `W_D(epsilon)` wide centers and at most `H_D` holes. There are no narrow paired centers inside it.

Let `T_D=o(D)` denote the neighborhood-complexity scale on the same diagonal. Choose an integer block length `m_D` so slowly that

$$
\boxed{
m_D\to\infty,
\qquad
{m_D(H_D+1)\over D}\to0,
\qquad
{m_DT_D\over D}\to0.
}
\tag{MC.14}
$$

The holes split the wide suffix into at most `H_D+1` consecutive physical runs. Packing disjoint `m_D`-blocks gives `K_D` blocks with

$$
K_Dm_D
\ge
W_D(\epsilon)-(H_D+1)(m_D-1).
\tag{MC.15}
$$

Using (MC.12) and (MC.14),

$$
\boxed{
K_D
\ge(\epsilon\nu-o(1)){D\over m_D}
\to\infty.
}
\tag{MC.16}
$$

Every interface in every one of these blocks is a paired exact-force center with

$$
\boxed{
\eta_i\ge\rho_\epsilon.
}
\tag{MC.17}
$$

---

## 4. Global KKT mass selects a vanishing-mass wide block

Let

$$
B_i=\sum_{h\in X_i}\beta_h
\tag{MC.18}
$$

be the switching KKT mass at interface `i`. On one side of the common hub the switching sets are edge-disjoint, so

$$
\sum_iB_i\le1.
\tag{MC.19}
$$

Choose among the `K_D` blocks one block `J_D` minimizing total switching mass. Then

$$
\boxed{
\mathcal B_D:=\sum_{i\in J_D}B_i
\le {1\over K_D}
=O_\epsilon\!\left({m_D\over D}\right)
\to0.
}
\tag{MC.20}
$$

The reaction bound gives

$$
\boxed{
{1\over D}\sum_{i\in J_D}|G_i|
\le\mathcal B_D\to0.
}
\tag{MC.21}
$$

Write the exact positive two-ray compression as

$$
G_i=D(\lambda_i^-d_i^-+\lambda_i^+d_i^+).
\tag{MC.22}
$$

Because every pair has gap at least the fixed `rho_epsilon`, the sine-law estimate gives

$$
\boxed{
\sum_{i\in J_D}(\lambda_i^-+\lambda_i^+)
\le
{2\mathcal B_D\over\sin\rho_\epsilon}
\to0.
}
\tag{MC.23}
$$

Thus fixed aperture, vanishing original KKT mass, and vanishing compressed-force mass coexist without any destination classification.

---

## 5. Coercivity and the near-full common grid survive unchanged

Every interface of `J_D` is exact-antipodal, so its `m_D+1` rows have one exact common phase. The full first-order cancellation kernel is

$$
\mathcal K_D
=
\left\{a\in\mathbb R^{m_D+1}:\sum_ja_j=0\right\},
\qquad
\dim\mathcal K_D=m_D\to\infty.
\tag{MC.24}
$$

The direct-sum theorem gives

$$
\boxed{
\left\|D^{-1}L_D(a)\right\|_2
\ge(\sqrt2\,c_H-o(1))\|a\|_2,
}
\tag{MC.25}
$$

with

$$
\sqrt2\,c_H=0.64179823755\ldots .
\tag{MC.26}
$$

The adjacent crossing-family drift is below `T_D` at every separator. By (MC.14), the common intersection across the whole block loses only `o(D)` columns. The one-row angular-defect purification then yields a common train family `P_D` with

$$
\boxed{|P_D|>(0.6536-o(1))D}
\tag{MC.27}
$$

and

$$
\boxed{
{\pi\over3}<\theta(\tau_j,b)
={\pi\over3}+o(1)
}
\tag{MC.28}
$$

uniformly over every row and column of the growing rectangle.

The common initial/final column flanks remain

$$
\boxed{
|P_D^-|,|P_D^+|
>(0.0647027254265\ldots-o(1))D,
}
\tag{MC.29}

with crossing centers below `-0.01D` and above `+0.01D` in row-normal circumcenter coordinates on every row.

Finally the fixed aperture gives a common central disk in every force quadrilateral:

\[
\boxed{
B\!\left(o,
\left({1\over2}\sin{\rho_\epsilon\over2}-o(1)\right)D
\right)
\subset Q_i
\qquad(i\in J_D).
}
\tag{MC.30}
$$

---

## 6. Diagonalize `epsilon->0`: aperture tends to `c`

The fixed-`epsilon` theorem is enough for every subsequent compactness argument. It also permits a stronger diagonal statement.

Take any sequence

$$
\epsilon_n\downarrow0.
\tag{MC.31}
$$

For each `n`, apply Sections 2--5 with `epsilon=epsilon_n` and then choose the source diameter so far out that

1. the wide suffix has at least `(epsilon_n nu/2)D` centers;
2. the physical-hole and complexity errors admit a block length `m_n>=n`;
3. the selected block satisfies `mathcal B_n<=1/n`; and
4. all asymptotic grid/coercivity errors are at most `1/n`.

This diagonal extraction gives

$$
|J_n|=m_n\to\infty
\tag{MC.32}
$$

and a uniform aperture

$$
\boxed{
\inf_{i\in J_n}\eta_i
\ge\rho_{\epsilon_n}
=(1-\epsilon_n)c
=c-o(1).
}
\tag{MC.33}
$$

The switching and compressed masses still tend to zero because `sin rho_{epsilon_n}->sin c>0`. The common central-diamond radius coefficient tends to

$$
\boxed{
{1\over2}\sin{c\over2}
=5.649999999879\ldots\times10^{-6},
}
\tag{MC.34}
$$

and the cross-chord endpoint-separation coefficient tends to

$$
\boxed{
\sin{c\over2}
=1.129999999976\ldots\times10^{-5}.
}
\tag{MC.35}
$$

The limiting compressed-force factor is finite:

$$
\boxed{
{2\over\sin c}
=88495.5752288\ldots .
}
\tag{MC.36}
$$

Thus the aperture does not have to shrink when the corridor depth diverges.

---

## 7. Frontier effect

On the no-positive-density-TB1 branch, the current strongest consecutive-corridor normal form is now unconditional with respect to TT/mixed/OO destinations:

```text
an unbounded consecutive exact-phase row stack;
every separator carries a bilateral exact positive diameter force pair;
uniform projective pair aperture >= (2.26e-5-o(1));
every force diamond contains one common radius-(5.65e-6-o(1))D disk;
total switching KKT mass over the whole stack -> 0;
total compressed two-ray mass over the whole stack -> 0;
normalized resultant variation over the whole stack -> 0;
the full cancellation kernel has singular-value floor 0.641798...-o(1);
all rows cross the same (0.6536-o(1))D near-equilateral columns;
common +/-0.01D circumcenter flanks each have density 0.0647027-o(1).
```

The far-terminal alternative remains useful as additional geometry: if a TT pair falls below the smaller parent threshold `nu`, the separate near-diametrical-terminal theorem forces `diam(T_m)/D>=cos(nu/2)-o(1)`. But terminal concentration is no longer an escape from the fixed-aperture massless corridor itself.

C-II remains open. The no-TB1 seam is now the geometric placement of actual diameter chords inside this common near-equilateral grid, not the existence, density, destination type, aperture, KKT scale, or first-order coercivity of the force corridor. The separate positive-density strong-TB1 branch remains unresolved.

**Disposition:** used the two-lane narrow-pair capacity at thresholds approaching `c=2.26e-5` to force an unconditional growing fixed-aperture vanishing-mass corridor on the no-TB1 branch, independent of the terminal destination word.