# Target C-II — Oler center packing caps a canonical O--O path at `2.69431 D`

**Date:** 2026-09-17  
**Status:** proof-only path-capacity strengthening; no canonical promotion claimed  
**Scope:** canonical simple O--O dual paths used by the high-`t` Target C reductions  
**Dependencies:** phase-free O--O path-region saturation; exact interval support; six-row Oler center-packing theorem  
**Certificate:** `research/verify_target_c_high_t_oler_oo_path_capacity_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The new Oler center-packing estimate is not only a short-pair lemma. Applied to one source segment joining the two extreme regions of a canonical O--O dual path, it improves the global path-length constant.

Let

\[
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m
\]

be a canonical simple O--O dual path. The audited phase-free region-saturation theorem gives a source vertex in every `R_i`; in fact every region contains an endpoint of an actual diameter edge. Choose

\[
x\in R_0,
\qquad
y\in R_m.
\]

Then

\[
|x-y|\le D,
\]

and exact path separation forces the straight segment `xy` to meet all `m` selected rows.

The Oler center-packing theorem for a source segment of length `L` gives

\[
N\le1+{14L+5\pi\over3\sqrt3}.
\]

With `N=m` and `L<=D`,

\[
\boxed{
m\le
{14\over3\sqrt3}D
+1+{5\pi\over3\sqrt3}.
}
\tag{PC.1}
\]

Thus

\[
\boxed{
m\le(2.69430125622\ldots)D+4.023\ldots .}
\tag{PC.2}
\]

In asymptotic form,

\[
\boxed{
m\le(A_*+o(1))D,
\qquad
A_*:={14\over3\sqrt3}=2.69430125622\ldots .}
\tag{PC.3}
\]

This is strictly better than the `T_*=3.0605` total-complete-train bound previously used as a generic upper bound for the number of rows on the selected path.

One immediate consequence is a better coefficient in the flexible-scale UPPER Horn localization theorem. There the only use of `T_*` in the path-counting argument is to bound the number of selected cuts/windows. Replacing it by `A_*` changes the same-type localization coefficient from

\[
{\gamma_7\over48T_*}
\]

to

\[
\boxed{
\widehat c_{*,7}
:={\gamma_7\over48A_*}
={113\sqrt3\over143{,}360{,}000{,}000}
=1.36524652103\ldots\times10^{-9},
}
\tag{PC.4}
\]

where

\[
\gamma_7={113\over640{,}000{,}000}.
\]

Hence, for every scale `L_D->infinity` with `L_D=o(D)`, every UPPER Horn branch has either

\[
(\widehat c_{*,7}-o(1))L_D
\]

same-type blockers on one common low-defect row, or that many same-type blockers in one `2L_D+O(1)` low-defect window.

The normalized defect conclusions and the `(0.6536-o(1))D` common train scaffold are unchanged.

---

## 1. Extreme-region loading supplies the diameter-length transversal

The phase-free path-region saturation theorem applies to every canonical simple O--O dual path used here. It gives

\[
R_i\cap V(S)\ne\varnothing
\qquad(0\le i\le m),
\tag{PC.5}
\]

and in fact supplies an actual diameter endpoint in each region.

Choose source vertices `x in R_0` and `y in R_m`. Since the source has diameter `D`,

\[
L:=|x-y|\le D.
\tag{PC.6}
\]

Every selected row `tau_j` separates `R_0` from `R_m`. Therefore the connected segment `xy` crosses every one of the `m` proper crosscuts.

So the Oler row-crossing theorem applies with

\[
N=m,
\qquad L\le D.
\]

Substitution immediately gives (PC.1).

No KKT mass, common phase, TB1 sign, or diameter activity of the pair `xy` is needed. Diameter is used only as the source-wide upper bound on `|x-y|`.

---

## 2. Comparison with the previous path-count input

The upper-blocker localization proof previously used

\[
m\le T_*D+o(D),
\qquad
T_*={6121\over2000}=3.0605,
\tag{PC.7}
\]

because every selected row is a complete stopped train and the global train ledger bounds the total number of such trains.

Equation (PC.3) is path-specific and stronger:

\[
A_*=2.69430125622\ldots<T_*=3.0605.
\tag{PC.8}
\]

The ratio is

\[
{T_*\over A_*}=1.13591603498\ldots .
\tag{PC.9}
\]

Thus every localization coefficient whose denominator came only from the selected-path row count improves by about `13.6%`.

This does **not** replace `T_*` in arguments counting all complete stopped trains source-wide. In particular, the permanent-LOWER theorem that pigeonholes one fixed transverse train through many local ladders still correctly uses the global complete-train count `T_*D`.

---

## 3. Flexible-scale UPPER localization with the path cap

Retain the notation of the seven-spaced flexible-scale theorem. Its owned UPPER family has density

\[
\delta_{0,7}={\gamma_7\over8}.
\]

At scale `L=L_D`, define the rich-cut/window threshold using `A_*` instead of `T_*`:

\[
\widehat\vartheta_7
:={\delta_{0,7}\over3A_*}.
\tag{PC.10}
\]

For long supports, poor cuts carry at most

\[
(A_*D+O(1))\widehat\vartheta_7L
=
\left({\delta_{0,7}\over3}+o(1)\right)DL.
\]

For short supports, the number of two-block candidate windows is at most

\[
{A_*D\over L}+O(L^{-1}),
\]

so poor windows again contain at most `(delta_{0,7}/3+o(1))D` blockers.

After the SIGNED/THIN split, the localized same-type coefficient is

\[
{\widehat\vartheta_7\over2}
={\delta_{0,7}\over6A_*}
={\gamma_7\over48A_*}
=\widehat c_{*,7},
\]

which proves (PC.4).

All defect estimates are unchanged:

- COMMON-CUT: `F_j=O(D/L)=o(D)`;
- LOCAL-WINDOW: `C_W=O(L)=o(D)`.

---

## 4. Frontier effect

The Oler center argument now controls both ends of the short/long scale:

```text
one source segment of length L
    -> at most 1 + (14L+5pi)/(3sqrt3) selected O-O rows;

L=1+O(1/D)
    -> at most 6 rows;

L<=D between the two extreme path regions
    -> total canonical O-O path length <= 2.694301257 D + O(1).
```

The first specialization enabled seven-spaced Horn thinning. The second tightens every path-counting step in the UPPER localization theorem.

This still does not close any SIGNED/THIN metric normal form. It removes another avoidable constant loss and shows that the same Oler-center mechanism controls both local blocker bandwidth and global path capacity.

**Disposition:** proved the path-specific cap `m<=(14/(3sqrt3))D+O(1)` and upgraded the seven-spaced flexible UPPER localization coefficient to `1.36524652103...e-9`. C-II and Level I remain open.
