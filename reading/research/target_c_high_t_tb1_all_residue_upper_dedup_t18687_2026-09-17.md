> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_all_residue_upper_dedup_t18687_2026-09-17.md) · source SHA-256 `fd69e9da1d51331d3f1c6b983341c74db05b73774bb8b9081d08a250c5350a9c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 17 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "dc5edb28d85ff1d4a9623a74196ddb16b0be6848", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_all_residue_upper_dedup_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "cd8d2f446cf2ba1d3e113605ea3ec43fbb8b841d1cb0dc62b46f755e2504f833"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — repeated-upper rigidity removes the cross-residue UPPER duplication loss

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the all-residue Horn aggregation; no canonical promotion claimed  
**Scope:** one-sign strong-TB1 exact swaps through `t=(q-k)/D<=1.8687`  
**Dependencies:** five-row capsule theorem; all-residue Horn aggregation; double-witness collapse; bounded row-parallel `D-O(D^-2)` packing; Oler O--O path-capacity theorem  
**Certificate:** `research/verify_target_c_high_t_tb1_all_residue_upper_dedup_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The all-residue Horn theorem conservatively divided both LOWER and UPPER classwise blocker counts by two when the six modulo-six systems were merged. That factor is necessary for LOWER: the same short pair may obstruct the singleton swap at both endpoint layers, and a positive-density repeated LOWER family is not presently excluded.

For UPPER it is unnecessary. A source pair which is an UPPER exact-swap witness at two distinct one-sign strong-TB1 interfaces is precisely a repeated upper witness. The audited double-witness theorem then places it in the shell

```math
D-O(D^{-2})\le |xy|<D
```

and in one common inverse-`D` projective row cone. The row-parallel almost-diameter packing theorem says that the **entire source contains only `O(1)` such pairs**.

Therefore cross-residue repetition can remove only `O(1)` UPPER blockers. Aggregating all six Horn systems yields the stronger source-wide budget

```math
\boxed{
N_L+N_U>
\left({s_0\over16}-o(1)\right)D,
\qquad
s_0={791\over320{,}000{,}000},
}
\tag{UD.1}
```

where `N_L` counts distinct permanent inverse-`D` near-unit blockers and `N_U` counts distinct injectively owned inverse-`D` near-diameter UPPER blockers.

In particular one metric type has density at least

```math
\boxed{
\delta_*:={s_0\over32}
={791\over10{,}240{,}000{,}000}
=7.724609375\times10^{-8}.
}
\tag{UD.2}
```

This improves the equal-density all-residue dichotomy from `s0/48` to `s0/32`.

On the UPPER side, flexible-scale localization therefore improves again. With

```math
A_*={14\over3\sqrt3}
```

the localized same-type coefficient becomes

```math
\boxed{
c_{\rm dedup}
:={\delta_*\over6A_*}
={113\sqrt3\over40{,}960{,}000{,}000}
=4.77836282362\ldots\times10^{-9}.
}
\tag{UD.3}
```

This is exactly three times the single-largest-mod-six coefficient and `3/2` times the first all-residue coefficient.

---

## 1. Retain the six class masses

Use the notation of the all-residue theorem. After deleting the source-wide `O(1)` genuine-upper binary exceptions, the one-sign coordinate set `P_D` satisfies

```math
|P_D|>
\left({s_0\over2}-o(1)\right)D.
\tag{UD.4}
```

Partition it into the six residue classes modulo six. For every class `P_r`, the six-spaced Horn poison theorem gives one of the following conservative labels:

```math
\begin{array}{ll}
L:&\text{at least }|P_r|/4-O(1)\text{ distinct LOWER blockers},\\[1ex]
U:&\text{at least }|P_r|/8-O(1)\text{ distinct UPPER blockers}.
\end{array}
\tag{UD.5}
```

The U label includes both a permanent-UPPER winner and an implication-forest winner; the latter actually supplies the stronger `|P_r|/2` count, which is not needed here.

Write

```math
P_L:=\sum_{r:L}|P_r|,
\qquad
P_U:=\sum_{r:U}|P_r|,
\qquad
P_L+P_U=|P_D|.
\tag{UD.6}
```

---

## 2. LOWER still has multiplicity two

Across different residue systems, one lower blocker pair can be selected at both physical layers containing its two endpoints. The exact layer-support identity gives multiplicity at most two, but the repeated-witness theorem allows a linear repeated LOWER matching.

Therefore the safe global LOWER count remains

```math
\boxed{
N_L\ge {P_L\over8}-O(1).
}
\tag{UD.7}
```

Any large loss in (UD.7) is itself structured: repeated lower blockers are, up to `O(1)` exceptions, a vertex-disjoint family with

```math
1<|xy|\le1+O(D^{-2})
```

and common projective direction within `O(D^{-1})` of the row phase. No use of that extra structure is needed for the present theorem.

---

## 3. An UPPER blocker cannot repeat across residue systems except `O(1)` times

Consider a source pair `h=xy` which occurs in two distinct classwise UPPER extractions. Then `h` is a previously strict pair whose singleton exact swap reaches or violates the diameter boundary at two distinct one-sign strong-TB1 interfaces.

The role of `h` inside a residue-class Horn system is irrelevant here. It may be

- a permanent one-coordinate UPPER blocker;
- a persistent two-coordinate UPPER blocker; or
- the source pair realizing a selected implication-forest arc.

In every case, occurrence at coordinate `i` means that `h` is an UPPER exact-swap witness for interface `i`. If it occurs again at `j\ne i`, it is a double witness.

The repeated-witness collapse theorem applies to any strict pair serving as a witness at two interfaces. Uniform constants `A,L` exist such that every repeated UPPER pair obeys

```math
\boxed{
D-{A\over D^2}\le |h|<D,
\qquad
d_{\mathbb{RP}^1}([h],[u_*])\le {L\over D}.
}
\tag{UD.8}
```

The row-parallel almost-diameter packing lemma then gives

```math
\boxed{
N_{\rm repeated,UPPER}=O_{A,L}(1).
}
\tag{UD.9}
```

Thus, after deleting only `O(1)` duplicate UPPER pairs, the six classwise UPPER families are source-pair disjoint.

Within each class the extracted UPPER family already has an injective owner coordinate: permanent blockers are deduplicated from coordinate incidences, and implication-forest arcs have distinct tails. The six coordinate classes are disjoint. Deleting the `O(1)` cross-class duplicates preserves an injective owner map.

Consequently

```math
\boxed{
N_U\ge {P_U\over8}-O(1).
}
\tag{UD.10}
```

This is the improvement over the previous `P_U/16` bound.

---

## 4. Source-wide blocker budget and equal-density dichotomy

Adding (UD.7) and (UD.10),

```math
N_L+N_U
\ge
{P_L+P_U\over8}-O(1)
={|P_D|\over8}-O(1).
\tag{UD.11}
```

Using (UD.4),

```math
\boxed{
N_L+N_U>
\left({s_0\over16}-o(1)\right)D.
}
\tag{UD.12}
```

Numerically,

```math
{s_0\over16}
={791\over5{,}120{,}000{,}000}
=1.544921875\times10^{-7}.
\tag{UD.13}
```

At least one summand in (UD.12) is larger than half the right side, giving

```math
\boxed{
\max\{N_L,N_U\}>
\left({s_0\over32}-o(1)\right)D.
}
\tag{UD.14}
```

This proves (UD.1)--(UD.2).

The sum form (UD.12) is stronger than the displayed dichotomy and should be retained downstream. For example, any future upper bound `N_L\le\lambda D+o(D)` immediately forces

```math
N_U>
\left({s_0\over16}-\lambda-o(1)\right)D.
```

---

## 5. Flexible-scale UPPER localization at the new density

Assume UPPER is the winning metric type in (UD.14). Section 3 gives a distinct family of more than

```math
(\delta_*-o(1))D,
\qquad
\delta_*={s_0\over32},
\tag{UD.15}
```

UPPER near-diameter blockers with injective ownership and exact selected-cut interval support.

The path-specific Oler theorem gives

```math
m\le(A_*+o(1))D,
\qquad
A_*={14\over3\sqrt3}.
\tag{UD.16}
```

The scale-free localization proof uses a rich-cut/window threshold `delta_*/(3A_*)` and then one factor `1/2` for the SIGNED/THIN type split. Therefore its same-type coefficient is

```math
\begin{aligned}
c_{\rm dedup}
&={\delta_*\over6A_*}\\
&={791\over10{,}240{,}000{,}000}
\cdot{\sqrt3\over28}\\
&=\boxed{{113\sqrt3\over40{,}960{,}000{,}000}}\\
&=4.77836282362\ldots\times10^{-9}.
\end{aligned}
\tag{UD.17}
```

Hence for every `L_D->infinity`, `L_D=o(D)`, the UPPER winner yields either

```math
(c_{\rm dedup}-o(1))L_D
```

SIGNED or THIN blockers on one common row with full angular defect `O(D/L_D)`, or that many same-type blockers in one `2L_D+O(1)` path window with total row/terminal cost `O(L_D)`.

The existing `(0.6536-o(1))D` common train scaffold and circumcenter flanks survive unchanged.

Relative to previous coefficients,

```math
\boxed{
{c_{\rm dedup}\over\widehat c_{*,6}}=3,
\qquad
{c_{\rm dedup}\over c_{\rm all}}={3\over2}.
}
\tag{UD.18}
```

---

## 6. Frontier effect

The modulo-six thinning is now only an internal device for proving six independent Horn statements. Once the six systems are aggregated, repeated-upper rigidity recovers almost all of the UPPER occurrence count.

The one-sign Horn obstruction has the source-wide budget

```text
N_LOWER + N_UPPER > (s0/16-o(1)) D,

where
    LOWER = five-row inverse-D near-unit blockers,
    UPPER = injectively owned inverse-D near-diameter blockers.
```

Thus one metric side has density `s0/32`, and an UPPER winner localizes with coefficient `4.77836282362...e-9` at every diverging sublinear scale.

C-II remains open. The LOWER seam is still the finite five-row near-unit classification, with any heavy repeated subfamily already forced into an ultra-near-unit row-parallel matching. The UPPER seam remains the SIGNED/THIN metric-order closure inside the dense common train scaffold.

**Disposition:** used the bounded repeated-UPPER theorem to remove the factor-two cross-residue loss on UPPER blockers, proved the sum budget `N_L+N_U>(s0/16-o(1))D`, improved the equal-density Horn dichotomy to `s0/32`, and raised the flexible-scale UPPER localization coefficient to `4.77836282362...e-9`. C-II and Level I remain open.
