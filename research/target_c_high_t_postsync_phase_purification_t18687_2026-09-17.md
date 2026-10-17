<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d47c686f772ae9720a52a1cd52cc159faa59e191", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_postsync_phase_purification_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ffa976c89885233b7f9d5db61d882cc85cdc63e3d733092564d28ea98401fe19"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — phase purification after diameter synchronization keeps almost the whole high-`t` rectangle

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` complete rectangle and oriented-column reduction; global strict-rhombus angular-defect budget; full-rectangle metric saturation lock  
**Certificate:** `research/verify_target_c_high_t_postsync_phase_purification_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The earlier inverse-`D` phase-collapse theorem purifies the full train rectangle first and then synchronizes it with region-saturation diameters. That order pays fixed factors before the hub/median extraction. The new full-rectangle saturation lock shows that the order can be reversed: first choose the hub-aligned row block and the diameter family, then spend the global angular-defect budget only on the already synchronized product.

This removes any fixed `1/2` phase-purification loss. For every fixed `epsilon>0`, one can keep a `(1-epsilon)` fraction of the synchronized rows and a `(1-epsilon)` fraction of the full consistently oriented transverse shore while still forcing every crossing angle to be

\[
{\pi\over3}+O_\epsilon(D^{-1}).
\]

The synchronized diameter family is not thinned at all. In the concrete `epsilon=0.1` specialization this gives

\[
|E_*|>5.65\times10^{-6}D-o(D),
\]

\[
|A_{90}|>5.085\times10^{-6}D-o(D),
\]

\[
|B_{90}|>0.14103D-o(D),
\]

where every diameter in `E_*` spans every row in `A_{90}`, every `A_{90} x B_{90}` pair is one strict rhombus in common order, and every grid angle satisfies

\[
0<\theta_{ab}-{\pi\over3}
<{1.262\times10^8\over D}+o(D^{-1}).
\]

Compared with the prior synchronized phase-collapsed scaffold, the row shore increases from `2.8e-6 D` to `5.085e-6 D`, the transverse shore from `0.0783D` to `0.14103D`, and the diameter family from `2.8e-6 D` to `5.65e-6 D`. The price is only a larger explicit inverse-`D` angle constant.

---

## 1. Start from the synchronized full rectangle

Use the full-rectangle metric saturation lock. It supplies

\[
E_*\times A_1^*
\]

with exact selected-cut support incidence and

\[
A_1^*\times B_*
\]

with complete strict-rhombus incidence, where

\[
\boxed{|E_*|,|A_1^*|>aD-o(D),
\qquad a={113\over20{,}000{,}000}=5.65\times10^{-6},}
\tag{PP.1}
\]

and

\[
|B_*|>0.3134D-o(D).
\]

The complete-rectangle orientation reduction deletes only `O(1)` ambiguous columns and keeps one consistent crossing orientation. Thus there is

\[
B_+\subset B_*
\]

with

\[
\boxed{|B_+|>bD-o(D),
\qquad b={1567\over10000}=0.1567,}
\tag{PP.2}
\]

such that real phase representatives can be chosen with

\[
{\pi\over3}<\beta_b-\alpha_a<{2\pi\over3}
\qquad(a\in A_*,b\in B_+).
\tag{PP.3}
\]

In particular (PP.3) holds on `A_1^* x B_+`.

Every diameter in `E_*` already spans every row in `A_1^*`, so any later thinning of the row or column shore preserves the entire diameter family `E_*`.

---

## 2. Exact additive phase decomposition on the synchronized product

As in the original phase-collapse proof, put

\[
\alpha^+=\max_{a\in A_*}\alpha_a,
\qquad
\beta^-=\min_{b\in B_+}\beta_b,
\]

\[
g=\beta^- -\alpha^+-{\pi\over3}>0,
\]

\[
r_a=\alpha^+-\alpha_a\ge0,
\qquad
q_b=\beta_b-\beta^-\ge0.
\]

Then for every `a in A_*`, `b in B_+`, the angular defect is exactly

\[
\boxed{
\delta_{ab}:=\beta_b-\alpha_a-{\pi\over3}
=g+r_a+q_b.
}
\tag{PP.4}
\]

Let

\[
S_1:=
\sum_{a\in A_1^*}\sum_{b\in B_+}\delta_{ab}.
\tag{PP.5}
\]

Every term is the angular defect of a distinct strict rhombus. The canonical global budget therefore gives

\[
S_1<C_{phase}D,
\qquad
C_{phase}={\pi^2\sqrt3(2+\sqrt3)\over12}.
\tag{PP.6}
\]

Define the synchronized-product average defect

\[
\Lambda_D:={S_1\over |A_1^*||B_+|}.
\tag{PP.7}
\]

Using (PP.1)--(PP.2),

\[
\boxed{
\Lambda_D
<
{C_{phase}\over ab}{1\over D}+o(D^{-1}).
}
\tag{PP.8}
\]

The exact density product is

\[
ab={177071\over200{,}000{,}000{,}000}
=8.85355\times10^{-7},
\tag{PP.9}
\]

and numerically

\[
{C_{phase}\over ab}
=6.0049477\ldots\times10^6.
\tag{PP.10}
\]

Averaging the exact decomposition (PP.4) over the synchronized product gives

\[
\Lambda_D
=g
+{1\over|A_1^*|}\sum_{a\in A_1^*}r_a
+{1\over|B_+|}\sum_{b\in B_+}q_b.
\tag{PP.11}
\]

All three terms are nonnegative, so each is at most `Lambda_D`.

---

## 3. Arbitrarily high fixed retention with inverse-`D` phase width

Fix any constant

\[
0<\varepsilon<1.
\]

Define

\[
A_\varepsilon
:=
\{a\in A_1^*:r_a\le\Lambda_D/\varepsilon\},
\]

\[
B_\varepsilon
:=
\{b\in B_+:q_b\le\Lambda_D/\varepsilon\}.
\tag{PP.12}
\]

Markov gives

\[
\boxed{
|A_\varepsilon|\ge(1-\varepsilon)|A_1^*|,
\qquad
|B_\varepsilon|\ge(1-\varepsilon)|B_+|.
}
\tag{PP.13}
\]

For every retained cross-pair, (PP.4), (PP.11), and (PP.12) give

\[
0<\delta_{ab}
\le
\left(1+{2\over\varepsilon}\right)\Lambda_D.
\]

Hence

\[
\boxed{
0<\theta_{ab}-{\pi\over3}
<
\left(1+{2\over\varepsilon}\right)
{C_{phase}\over ab}{1\over D}
+o(D^{-1})
}
\tag{PP.14}
\]

uniformly on `A_epsilon x B_epsilon`.

The retained shore sizes satisfy

\[
\boxed{
|A_\varepsilon|
>(1-\varepsilon)5.65\times10^{-6}D-o(D),
}
\tag{PP.15}
\]

\[
\boxed{
|B_\varepsilon|
>(1-\varepsilon)0.1567D-o(D).
}
\tag{PP.16}
\]

Because `A_epsilon subset A_1^*`, all bars in the original unthinned `E_*` still span every retained row:

\[
\boxed{
E_*\times A_\varepsilon
\text{ remains complete in exact selected-cut support incidence.}
}
\tag{PP.17}
\]

And because the two train shores remain internally noncrossing and use the same oriented branch, the signed monotone-grid argument gives one common crossing order on the complete product

\[
\boxed{A_\varepsilon\times B_\varepsilon.}
\tag{PP.18}
\]

Thus the synchronized inverse-`D` grid can retain an arbitrarily high fixed fraction of both available oriented shores. There is no intrinsic `1/2` Markov loss.

---

## 4. Concrete ninety-percent specialization

Take

\[
\varepsilon={1\over10}.
\]

Write

\[
A_{90}:=A_{1/10},
\qquad
B_{90}:=B_{1/10}.
\]

Then

\[
\boxed{|A_{90}|>5.085\times10^{-6}D-o(D),}
\tag{PP.19}
\]

\[
\boxed{|B_{90}|>0.14103D-o(D),}
\tag{PP.20}
\]

while the diameter shore is unchanged:

\[
\boxed{|E_*|>5.65\times10^{-6}D-o(D).}
\tag{PP.21}
\]

The angle coefficient in (PP.14) is

\[
21{C_{phase}\over ab}
=1.2610390189\ldots\times10^8,
\]

so the clean displayed bound

\[
\boxed{
{\pi\over3}<\theta_{ab}
<{\pi\over3}+{1.262\times10^8\over D}+o(D^{-1})
}
\tag{PP.22}
\]

holds for every `a in A90`, `b in B90`.

The strict-rhombus product itself has density

\[
(5.085\times10^{-6})(0.14103)
=7.1713755\times10^{-7},
\]

so

\[
\boxed{
|A_{90}||B_{90}|
>(7.1713755\times10^{-7}-o(1))D^2.
}
\tag{PP.23}
\]

---

## 5. The ninety-percent grid is also metrically macroscopic in two common directions

The metric train-grid span lemma applies directly. Both purified phase spreads are `O(1/D)`, so the train-adapted monotone coordinates transfer to one common row coordinate and one common column coordinate with only `O(1)` error over a source of diameter `D`.

Using (PP.20), every retained row has transverse crossing-center span

\[
>{\sqrt3\over2}(|B_{90}|-1),
\]

hence

\[
\boxed{
>(0.1221355-o(1))D.
}
\tag{PP.24}
\]

Using (PP.19), every retained column has crossing-center span

\[
>{\sqrt3\over2}(|A_{90}|-1),
\]

hence

\[
\boxed{
>(4.4037\times10^{-6}-o(1))D.
}
\tag{PP.25}
\]

Thus the concrete synchronized object is

```text
>5.65e-6 D actual diameter bars E_*
        x exact selected-cut support
>5.085e-6 D rows A_90
        x complete common-order strict-rhombus crossing
>0.14103 D columns B_90

all grid angles = pi/3 + O(1/D),
row-normal metric span >0.1221355 D-o(D),
column-normal metric span >4.4037e-6 D-o(D).
```

This retains `90%` of the synchronized row capacity and `90%` of the consistently oriented transverse capacity, without reducing the diameter population.

---

## 6. Interaction with the nested diameter rails

The fixed-birth-host and fixed-destination nested diameter rails extracted from `E_*` in the full-rectangle saturation theorem are not affected by row/column purification. They still have densities

\[
2.825\times10^{-6}
\]

and

\[
1.4125\times10^{-6}
\]

respectively, and every retained rail bar spans every row in `A_epsilon`, hence every row of `A90` in the concrete specialization.

Therefore the current high-`t` survivor has, simultaneously, a positive-density strictly nested actual-diameter rail and an almost-full synchronized inverse-`D` near-triangular grid of the dimensions above.

---

## 7. Frontier effect

The fixed-half phase-collapse constants were artifacts of applying Markov before the geometry had been localized to the hub-synchronized row block. After synchronization the same `O(D)` global defect is spread over a still-`Theta(D^2)` product, so any prescribed fixed retention fraction below one can be obtained at the cost of only a larger constant multiplying `1/D`.

This materially changes the remaining seam. A closing argument may now assume, after an arbitrarily small fixed density loss, that almost the entire `5.65e-6D` hub-synchronized row block and almost the entire `0.1567D` consistently oriented transverse shore form one inverse-`D` phase grid, while the full `5.65e-6D` diameter family spans every retained row.

What is still missing is the same precise bridge as before: selected-cut support does not locate the straight diameter chord's intersection point inside the train-grid patch. The next useful geometric theorem should exploit the much larger purified rectangle to control that location or to show that a nested diameter rail cannot thread through its ordered channels without violating near-antipodality or convex diameter-thrackle order.

**Disposition:** moved phase purification after hub/diameter synchronization, replacing fixed `1/2` losses by arbitrary fixed `epsilon` losses and giving a concrete `5.085e-6 D x 0.14103 D` synchronized inverse-`D` grid spanned by an unthinned `5.65e-6D` actual-diameter family. C-II and Level I remain open.
