<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "ddbb16875b3207b853434460ed7b91f23a9c335d", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_thin_two_sided_incidence_purification_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "981b507aef1d2dfc459b69a936d7252186c7065f6d16dd32b07ac3b699342293"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - two-sided incidence purification for the logarithmic THIN braid/fence

**Date:** 2026-09-17  
**Status:** proof-only combinatorial strengthening of the logarithmic THIN braid/fence theorem; no canonical promotion claimed  
**Scope:** THIN side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** logarithmic THIN braid/fence tradeoff; phase-pure flank extraction  
**Certificate:** `research/verify_target_c_high_t_tb1_thin_two_sided_incidence_purification_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The logarithmic braid/fence theorem gives, on a polynomial-height common row stack,

- `k_D=Theta(log D)` vertex-disjoint THIN hull chords, every two crossing properly;
- `k_D` fixed left-flank complete trains and `k_D` fixed right-flank complete trains, all pairwise noncrossing;
- after the existing phase split, at least `k_D/2` trains on each flank in one fixed inverse-`D` column phase.

What it does not control is whether an individual THIN chord meets an individual fixed train away from the selected rows. That incidence pattern could a priori be arbitrary.

A finite bipartite-pattern argument removes most of that arbitrariness without making any geometric assumption about the intersection multiplicity. Define

\[
\chi(e,b)=
\begin{cases}
1,&\text{if the straight THIN chord }e\text{ meets the complete stopped-train midpoint curve }b,\\
0,&\text{otherwise.}
\end{cases}
\tag{IP.1}
\]

Then a diverging sub-braid and diverging phase-pure subfences can be selected so that `chi` is constant on each whole side.

> **Two-sided incidence-purification theorem.** Let `F_D` be the braid and let `L_D,R_D` be phase-pure left and right fixed train subfences from the logarithmic braid/fence theorem. There are subsets
> \[
> F_D'\subset F_D,\qquad L_D'\subset L_D,\qquad R_D'\subset R_D
> \]
> of common size
> \[
> \boxed{
> s_D=\left({1\over4}-o(1)\right)\log_2\log D
> }
> \tag{IP.2}
> \]
> and bits
> \[
> \sigma_L,\sigma_R\in\{0,1\}
> \]
> such that
> \[
> \boxed{
> \chi(e,b)=\sigma_L
> \quad(e\in F_D',\ b\in L_D')
> }
> \tag{IP.3}
> \]
> and
> \[
> \boxed{
> \chi(e,b)=\sigma_R
> \quad(e\in F_D',\ b\in R_D').
> }
> \tag{IP.4}
> \]
>
> Thus the arbitrary braid/fence incidence matrix collapses to four exact global cases:
> \[
> (\sigma_L,\sigma_R)\in
> \{(0,0),(1,0),(0,1),(1,1)\}.
> \tag{IP.5}
> \]

At the concrete half-exponent choice from the parent theorem, all selected objects still coexist on the same

\[
D^{1/2-o(1)}
\]
common inverse-`D` phase rows. Every selected left train remains below the `-0.01D` row-normal circumcenter level on every retained row, every selected right train remains above `+0.01D`, the train families remain pairwise noncrossing and phase-pure, and the selected THIN chords remain vertex-disjoint and pairwise properly crossing.

No claim is made that a chord and a train meet at most once. The theorem deliberately records only the binary relation (IP.1), so it does not import an unproved straight-chord/stopped-train pseudoline property.

---

## 1. Finite two-sided binary-pattern lemma

Let

\[
F=\{e_1,\ldots,e_k\}
\]
be any finite set, and let `L,R` be two other finite sets. Give arbitrary binary relations

\[
\chi_L:F\times L\to\{0,1\},
\qquad
\chi_R:F\times R\to\{0,1\}.
\]

### Lemma IP.1

Suppose integers `s,k,n` satisfy

\[
|F|\ge4s,
\qquad
|L|,|R|\ge n,
\qquad
16^s s\le n.
\tag{IP.6}
\]

Then there exist

\[
F'\subset F,\quad L'\subset L,\quad R'\subset R,
\qquad
|F'|=|L'|=|R'|=s,
\tag{IP.7}
\]

and bits `sigma_L,sigma_R` for which both binary relations are constant on the corresponding complete rectangles:

\[
\chi_L(e,b)=\sigma_L
\quad(e\in F',\ b\in L'),
\tag{IP.8}
\]

\[
\chi_R(e,b)=\sigma_R
\quad(e\in F',\ b\in R').
\tag{IP.9}
\]

### Proof

Choose any `4s` elements

\[
F_0\subset F.
\]

Every `b in L` determines one binary pattern in `{0,1}^{F_0}`. There are at most

\[
2^{4s}=16^s
\]
patterns, so one pattern occurs on at least

\[
{|L|\over16^s}
\ge {n\over16^s}
\ge s
\tag{IP.10}
\]
left trains. Choose `s` of them and call the set `L'`.

Inside the common `4s`-bit pattern, at least `2s` coordinates carry the same bit. Retain exactly `2s` such coordinates and call that set `F_1`; call the common bit `sigma_L`. Then

\[
\chi_L(e,b)=\sigma_L
\quad(e\in F_1,\ b\in L').
\tag{IP.11}
\]

Now classify the elements of `R` by their binary patterns on the `2s` coordinates of `F_1`. There are at most

\[
2^{2s}=4^s
\]
patterns. Hence one pattern occurs at least

\[
{|R|\over4^s}
\ge {n\over4^s}
\ge 4^s s
\ge s
\tag{IP.12}
\]
times, where the penultimate inequality uses `n>=16^s s`.

Choose `s` right elements with that pattern and call the set `R'`. At least `s` coordinates of the common `2s`-bit pattern have one common bit `sigma_R`; choose exactly `s` such coordinates and call them `F'`.

Then (IP.9) holds by construction. Since `F' subset F_1`, equation (IP.11) remains valid and gives (IP.8). This proves the lemma. `square`

The constants are intentionally elementary. No Ramsey theorem or asymptotic regularity lemma is needed.

---

## 2. Apply the lemma to the THIN braid and phase-pure train fence

Use any fixed constant

\[
0<c<{1\over\log C_*},
\qquad
C_*=15650.8108585888\ldots,
\]
from the logarithmic braid/fence theorem, and write

\[
k_D=\lfloor c\log D\rfloor.
\tag{IP.13}
\]

The parent theorem gives a `k_D`-edge THIN braid `F_D` and `k_D` fixed trains on each circumcenter flank. Splitting each flank by its two possible inverse-`D` column-phase signs leaves phase-pure sets satisfying

\[
|L_D|,|R_D|\ge \left\lfloor{k_D\over2}\right\rfloor.
\tag{IP.14}
\]

Put

\[
n_D:=\min(|L_D|,|R_D|)
\]
and define `s_D` to be the largest integer satisfying

\[
4s_D\le k_D,
\qquad
16^{s_D}s_D\le n_D.
\tag{IP.15}
\]

Use the actual geometric incidence (IP.1) for both binary relations. Lemma IP.1 gives subsets

\[
F_D',L_D',R_D'
\]
of size `s_D` and the two bits `sigma_L,sigma_R`, proving (IP.3)-(IP.4).

Everything inherited from the parent theorem is monotone under taking subsets. In particular:

1. `F_D'` is still vertex-disjoint and pairwise properly crossing;
2. `L_D' union R_D'` is still pairwise noncrossing and has the same common two-block order on every retained row;
3. `L_D'` and `R_D'` remain separately inverse-`D` phase-pure;
4. every chosen braid chord and every chosen train crosses every retained row;
5. all chosen braid support intervals still contain the same consecutive selected-cut block;
6. the left and right rowwise crossing locations still lie outside the fixed `+-0.01D` circumcenter corridor.

The row family itself is not thinned in this extraction.

---

## 3. Size of the purified incidence system

Since

\[
k_D=\Theta(\log D),
\qquad
n_D=\Theta(\log D),
\tag{IP.16}
\]
condition (IP.15) is governed by

\[
4s+\log_2s\le\log_2n_D.
\tag{IP.17}
\]

It follows that

\[
s_D\le {1\over4}\log_2n_D
\tag{IP.18}
\]
and, conversely, for example

\[
s={1\over4}\left(\log_2n_D-2\log_2\log_2n_D\right)
\]
satisfies (IP.17) after taking an integer floor for all sufficiently large `D`. Hence

\[
\boxed{
s_D=
\left({1\over4}-o(1)\right)\log_2 n_D
=
\left({1\over4}-o(1)\right)\log_2\log D.
}
\tag{IP.19}
\]

The additional requirement `4s_D<=k_D` is asymptotically harmless because `s_D=Theta(log log D)` while `k_D=Theta(log D)`.

At the symmetric half-exponent choice

\[
c={1\over2\log C_*},
\]
the parent theorem retains

\[
D^{1/2-o(1)}
\tag{IP.20}
\]
common rows. Therefore one source simultaneously contains

```text
(1/4-o(1)) log_2 log D pairwise-crossing THIN hull chords;
(1/4-o(1)) log_2 log D fixed phase-pure left trains;
(1/4-o(1)) log_2 log D fixed phase-pure right trains;
D^(1/2-o(1)) common near-equilateral rows;
and one exact two-bit global braid/fence incidence type.
```

---

## 4. Why this is a real reduction and what it does not prove

Before this extraction, the `Theta(log D)` braid against the `Theta(log D)` two-sided train fence carried two arbitrary binary incidence matrices. A later geometric argument would have had to work uniformly over all of them.

After purification, an unbounded subsystem has only four incidence types:

```text
00: every selected braid chord avoids every selected train on both flanks;
10: every selected braid chord meets every selected left train and avoids every selected right train;
01: every selected braid chord avoids every selected left train and meets every selected right train;
11: every selected braid chord meets every selected train on both flanks.
```

The reduction is exact and source-level. It is also deliberately modest: `meet` means nonempty intersection of the straight chord with the complete midpoint train curve. It does not say that the intersection is unique, transverse, located in the common row stack, or contained in a strict rhombus. None of those stronger facts currently follows from the cited dependencies.

The next THIN closure target can therefore be split cleanly into four finite geometric cases. The `10`, `01`, and `11` cases should be attacked with the stopped-train monotonicity/slope-cone theorem and the near-diameter chord direction. The `00` case requires a separation/order argument showing that a growing pairwise-crossing hull braid cannot avoid growing phase-pure train bundles on both circumcenter flanks while crossing the same polynomial-height row stack.

**Disposition:** reduced arbitrary two-sided braid/train incidence to one of four exact homogeneous patterns on a `(1/4-o(1)) log_2 log D` by `(1/4-o(1)) log_2 log D` by two subsystem without shrinking the polynomial-height common row scaffold. C-II and Level I remain open.
