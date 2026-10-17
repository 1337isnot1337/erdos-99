> Generated reading edition · [exact source](../../research/target_c_small_leaf_rectangle_7404_profile_2026-09-15.md) · source SHA-256 `366f3bec0eb881845f4373af9eee72a0aaef7729ac2b7d689296fd182132d749`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "972be6d5637135e3c2fcb97eacab0f98c8b255f2", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_small_leaf_rectangle_7404_profile_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ea7473c2014a19d1c36ead28ceac5bd4388e4dc176d50937f67fdd42c8166ec4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — `0.7404D` fan sharpens the complete small-leaf rectangle

**Date:** 2026-09-15  
**Status:** proof-only phase-resolved structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited `>0.7404D` weighted small-leaf center fan; retained pair-weight floor `P_V>0.0848-o(1)`; corrected dual-tree-backbone rectangle extraction  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The corrected dual-tree rectangle theorem used the older `0.73D` weighted fan and an
arbitrary good-leaf threshold `0.57D`.  The newly audited fan bound is

$$
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}
>0.7404-o(1),
\tag{R7404.1}
$$

where `d_tau D` is the number of center-phase complete trains crossing the retained
smallest-leaf outer-to-outer train `tau`.  Together with

$$
{1\over D}\sum_\tau w_\tau>0.0848-o(1),
\qquad
0<w_\tau\le1,
\tag{R7404.2}
$$

and the center-phase size ceiling

$$
N_C<1.063D+o(D),
\tag{R7404.3}
$$

this yields a two-parameter family of stronger complete rectangles.

For any fixed threshold

$$
0<\lambda<0.7404
$$

and any fixed block density `rho>0` below the certified backbone density defined
below, there are smallest-leaf outer-to-outer trains `L_{lambda,rho}` and center-phase
complete trains `C_{lambda,rho}` such that every leaf train crosses every center train
and

$$
|L_{\lambda,\rho}|\ge \rho D-o(D),
\tag{R7404.4}
$$

$$
|C_{\lambda,\rho}|>
\bigl(\lambda-\alpha(\lambda)\rho\bigr)D-o(D),
\tag{R7404.5}
$$

where

$$
g(\lambda)
={ (0.7404-\lambda)(0.0848)\over1.063-\lambda},
\tag{R7404.6}
$$

$$
s(\lambda)
={\lambda g(\lambda)\over1.063},
\tag{R7404.7}
$$

and

$$
\boxed{
\alpha(\lambda)
={1.063\over s(\lambda)}
={1.063^2(1.063-\lambda)
 \over\lambda(0.7404-\lambda)(0.0848)}.
}
\tag{R7404.8}

Two simple exact choices give the main quantitative consequences:

\[
\boxed{
K_{\,0.00831D-o(D),\;0.00831D-o(D)}
}
\tag{R7404.9}
$$

as an actual complete leaf/center train rectangle, and

$$
\boxed{
|L_*|>0.00409D-o(D),
\qquad
|C_*|>0.3004D-o(D).
}
\tag{R7404.10}

The second rectangle carries more than

\[
0.0012288D^2-o(D^2)
\tag{R7404.11}
$$

complete leaf/center crossings.

---

## 1. Symbolic good-leaf threshold

Fix `lambda` in `(0,0.7404)`. Call a retained smallest-leaf O--O train **good** when

$$
d_\tau>\lambda.
$$

Let

$$
G_D={1\over D}\sum_{\tau\ good}w_\tau.
$$

Every leaf train is crossed by at most all center trains, so

$$
d_\tau<1.063+o(1).
$$

If `G_D` were smaller, the weighted average in (R7404.1) would obey

$$
0.7404P_V
<\lambda(P_V-G_D)+1.063G_D+o(1),
$$

where `P_V=(1/D)\sum w_tau`. Therefore

$$
G_D>
{(0.7404-\lambda)P_V\over1.063-\lambda}-o(1).
$$

Using (R7404.2),

$$
\boxed{
G_D>g(\lambda)-o(1).
}
\tag{R7404.12}

Since every retained pair weight is at most one, the number `m_D` of distinct good
leaf trains satisfies

\[
\boxed{
m_D>g(\lambda)D-o(D).
}
\tag{R7404.13}

This is a valid conversion from weighted mass to train count. It is not the invalid
fan-density normalization retracted on September 12: the count lower bound comes from
`sum_good w_tau<=#good`, after the weighted thresholding argument.

---

## 2. Dual-tree backbone with symbolic density

The good leaf trains are outer-to-outer and pairwise noncrossing, so their complement
dual is a tree `T_L`.  Every center train crosses a simple path in this tree.

The good-leaf/center incidence satisfies

\[
I>\lambda m_DD-o(D^2).
$$

There are fewer than `1.063D+o(D)` center trains. Hence some center train has a crossing
path `P_0` of length

$$
|P_0|>
{\lambda m_D\over1.063}-o(D)
>s(\lambda)D-o(D).
\tag{R7404.14}

Order the backbone edges of `P_0` as

\[
\lambda_1,\ldots,\lambda_s.
$$

As in the corrected parent theorem, the intersection of any other center path with
`P_0` is a consecutive interval.

---

## 3. Symbolic consecutive-block extraction

Every backbone leaf is good, so total center/backbone incidence is

$$
I_0>\lambda sD-o(D^2).
\tag{R7404.15}

Let

\[
r=\lfloor\rho D\rfloor,
\qquad
0<\rho<s(\lambda).
$$

Summing the number of consecutive `r`-blocks contained in each center interval gives

$$
\sum_B\#\{\gamma:B\subset N(\gamma)\cap P_0\}
\ge I_0-(r-1)N_C.
\tag{R7404.16}

There are at most `s` such blocks. Therefore some block `B_*` has common center
neighborhood

\[
\begin{aligned}
|N(B_*)|
&>{I_0-(r-1)N_C\over s}\\
&>\left(\lambda-{1.063\rho\over s/D}\right)D-o(D)\\
&>\left(\lambda-{1.063\rho\over s(\lambda)}\right)D-o(D)\\
&=\bigl(\lambda-\alpha(\lambda)\rho\bigr)D-o(D).
\end{aligned}
\tag{R7404.17}

Take `L_{lambda,rho}=B_*` and `C_{lambda,rho}=N(B_*)`. This proves the profile
(R7404.4)--(R7404.5).

The inequality direction in the third line is safe because `s/D>s(lambda)-o(1)` and
the penalty `1.063 rho/(s/D)` decreases as the actual backbone gets longer.

---

## 4. Balanced square above `0.00831D`

Choose

\[
\lambda={561\over1000}=0.561.
$$

The exact certificate gives

$$
g(\lambda)
={47541\over1568750}
=0.0303050199\ldots,
$$

and

$$
s(\lambda)
={26670501\over1667581250}
=0.0159935241\ldots .
$$

Take

$$
\rho={831\over100000}=0.00831.
$$

Then the exact right side of (R7404.17) is

$$
{1234784329\over142242672000}
=0.0086808291\ldots,
$$

which exceeds `0.00831` by more than `0.0003708`. Therefore

$$
\boxed{
|L_*|>0.00831D-o(D),
\qquad
|C_*|>0.00831D-o(D).
}
\tag{R7404.18}

This improves the previously merged balanced `0.00779D` square by about seven percent
on each shore.

---

## 5. High-product rectangle above `0.00409D x 0.3004D`

Choose instead

\[
\lambda={3\over5}=0.6.
$$

Then

$$
g(\lambda)
={37206\over1446875}
=0.0257147300\ldots,
$$

$$
s(\lambda)
={892944\over61521125}
=0.0145144289\ldots .
$$

Take

$$
\rho={409\over100000}=0.00409.
$$

Equation (R7404.17) gives the exact common-center lower bound

$$
{214634280377\over714355200000}
=0.3004587638\ldots
>0.3004.
$$

Hence

$$
\boxed{
|L_*|>0.00409D-o(D),
\qquad
|C_*|>0.3004D-o(D).
}
\tag{R7404.19}

The exact guaranteed crossing-product density exceeds

\[
0.0012288.
$$

This improves both shores of the earlier simple high-product rectangle
`0.00395D x 0.285D`.

---

## 6. Certificate and frontier

Run

`python3 research/verify_target_c_small_leaf_rectangle_7404_profile.py`.

The certificate uses only exact rational arithmetic and checks the two concrete choices
above, including the strict good-leaf, backbone, block-existence, and common-center
margins.

The continuous two-parameter optimization places the best balanced threshold near
`lambda=0.5613` and balanced shore density near `0.0083155`; the theorem intentionally
uses the simpler safe value `0.00831`.  The best crossing-product threshold lies near
`lambda=0.6007`; the simple choice `lambda=0.6` is essentially optimal for this
particular scalar extraction.

The remaining obstruction is geometric rather than scalar. The new rectangles should
be fed into common-order/diameter-bracing or simultaneous-shear arguments; further
threshold tuning has little value compared with exploiting the ordered outer-to-outer
leaf block.

**Disposition:** exact proof-only structural strengthening; C-II and Level I remain open.
