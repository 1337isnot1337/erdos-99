> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_direct_witness_injection_t18687_2026-09-17.md) · source SHA-256 `31eb800a5ba08cbe77f03920936b16377b4ea21e309aeb392c5d4ae30967b0e9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7e4c501a7f09266cba9d86fd909e643d39bb844b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_direct_witness_injection_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c08c2b32d6dd1c82eb5eee178d21eec37c99282e6f320a98c06797449c83f6f4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact-swap witnesses are source-wide injective up to `O(1)`

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the one-sign strong-TB1 exact-swap branch; no canonical promotion claimed  
**Scope:** one-sign strong-TB1 interfaces through `t=(q-k)/D<=1.8687`  
**Dependencies:** exact-swap obstruction theorem; one-row LOWER classification; exact double-witness collapse; row-parallel almost-diameter packing; Oler O--O path-capacity localization  
**Certificate:** `research/verify_target_c_high_t_tb1_direct_witness_injection_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The Horn machinery is no longer needed to obtain a positive-density metric obstruction on the one-sign strong-TB1 branch.

Let

```math
s_0={791\over320{,}000{,}000}.
```

On the current one-sign branch, after the two-sign/WIDE-PAIR alternative has been excluded, the interface set `M_D` satisfies

```math
\boxed{
|M_D|>
\left({s_0\over2}-o(1)\right)D.
}
\tag{DI.1}
```

The exact-swap obstruction theorem gives every `i in M_D` a previously strict source pair `e_i` which becomes invalid at the exact contact swap of layer `R_i`. It is either

```math
1<|e_i|\le1+q_i
\tag{DI.2}
```

or

```math
D-q_i\le|e_i|<D,
\tag{DI.3}
```

with `q_i=O(D^{-1})` uniformly.

The new one-row LOWER theorem removes the only unbounded repetition mechanism. A LOWER pair cannot witness two distinct one-sign interfaces at all. Repeated UPPER pairs are already source-wide `O(1)`. A single pair also cannot be LOWER at one interface and UPPER at another, because the two original-length windows (DI.2)--(DI.3) are disjoint for sufficiently large `D`.

Therefore one may choose the exact-swap witnesses so that, after deleting only `O(1)` interfaces,

```math
\boxed{
i\ne j\Longrightarrow e_i\ne e_j.}
\tag{DI.4}
```

Hence the source contains more than

```math
\boxed{
\left({s_0\over2}-o(1)\right)D
=
(1.2359375\times10^{-6}-o(1))D
}
\tag{DI.5}
```

distinct exact-swap witness pairs. Splitting only once by metric type gives the direct dichotomy

```math
\boxed{
\max\{N_L,N_U\}>
\left({s_0\over4}-o(1)\right)D
}
\tag{DI.6}
```

with

```math
{s_0\over4}
={791\over1{,}280{,}000{,}000}
=6.1796875\times10^{-7}.
\tag{DI.7}
```

This is six times the pre-one-row `s0/24` equal-density Horn floor and four times the weaker `s0/16` Horn propagation recorded immediately after the one-row theorem. Those older statements remain valid but are no longer the strongest density route. Horn structure remains useful for directed dependency questions; it is unnecessary for the basic LOWER/UPPER population count.

If UPPER wins, the existing flexible-scale Oler localization may be run directly on the injectively owned family. Its same-type localized coefficient becomes

```math
\boxed{
 c_{\rm dir}
 ={(s_0/4)\over6A_*}
 ={113\sqrt3\over5{,}120{,}000{,}000}
 =3.82269025889\ldots\times10^{-8},
}
\tag{DI.8}
```

where

```math
A_*={14\over3\sqrt3}.
```

If LOWER wins, every blocker has support depth exactly one and is the opposite diagonal of the unique strict unit rhombus on its support row. The global one-row ladder extraction then gives more than

```math
\boxed{
\left({s_0\over8}-o(1)\right)D
=(3.08984375\times10^{-7}-o(1))D
}
\tag{DI.9}
```

good one-row blocker gadgets. One fixed complete train belongs to the phase-pure transverse family of more than

```math
\boxed{
(6.49770768665\ldots\times10^{-8}-o(1))D
}
\tag{DI.10}
```

of them, and a pairwise-distinct-row subfamily still has density more than

```math
\boxed{
(3.24885384333\ldots\times10^{-8}-o(1))D.
}
\tag{DI.11}
```

---

## 1. Every one-sign interface has an exact witness

At interface `i`, write the exact contact swap as

```math
v_i=-q_iw_i,
\qquad q_i=|a_i+b_i|>0.
```

The cone-collapse theorem gives

```math
q_i=O(D^{-1})
\tag{DI.12}
```

uniformly over the one-sign population. The exact-swap obstruction theorem, using contact minimality at the second contact intersection, proves that some previously strict pair must hit one of the two metric boundaries at the exact swap. Thus one may choose a witness `e_i` satisfying (DI.2) or (DI.3) for every `i in M_D`.

Call these two possibilities LOWER and UPPER.

---

## 2. A pair cannot repeat with different metric types

Suppose one source pair `e` were a LOWER witness at interface `i` and an UPPER witness at interface `j`. Its original length `ell=|e|` would satisfy

```math
1<\ell\le1+q_i
```

and

```math
D-q_j\le\ell<D.
```

There is a fixed `Q` with `q_i,q_j<=Q/D` for all sufficiently large `D`. Hence repetition of different metric types would require

```math
D-{Q\over D}
\le1+{Q\over D},
```

or

```math
D-1\le {2Q\over D},
```

which is false for all sufficiently large `D`.

Therefore

```math
\boxed{
\text{a repeated exact-swap witness must hit the same metric boundary at both interfaces.}
}
\tag{DI.13}
```

---

## 3. LOWER repetition is impossible

Assume a source pair `e=xy` is a LOWER exact-swap witness at two distinct one-sign strong-TB1 interfaces.

The one-row LOWER classification proves more than short bandwidth: every LOWER exact-swap witness has exact selected-cut support depth one and is a diagonal of the unique strict unit rhombus on that support row. The same theorem combines this with the exact double-witness alignment and proves

```math
\boxed{
N_{\rm repeated,LOWER}^{\rm exact}=0
}
\tag{DI.14}
```

for all sufficiently large `D`.

So no LOWER source pair can occur twice in the witness assignment.

---

## 4. UPPER repetition costs only `O(1)` interfaces

If a pair is an UPPER witness at two distinct one-sign interfaces, the exact double-witness theorem gives

```math
D-|e|=O(D^{-2})
```

and places its projective direction in an `O(D^{-1})` neighborhood of the common row line.

The row-parallel almost-diameter packing theorem bounds the total number of source pairs with this geometry by `O(1)`. Therefore

```math
\boxed{
N_{\rm repeated,UPPER}^{\rm exact}=O(1).
}
\tag{DI.15}
```

A source pair has only two endpoints and can be affected by translations of at most two physical layers. Thus the `O(1)` repeated UPPER pairs account for only `O(1)` witness-interface incidences beyond their first occurrences.

Combining (DI.13)--(DI.15), the map

```math
i\longmapsto e_i
```

is injective after deleting `O(1)` members of `M_D`. This proves (DI.4)--(DI.5).

---

## 5. Direct metric dichotomy

Partition the distinct witnesses from (DI.5) into LOWER and UPPER sets. Then

```math
N_L+N_U>
\left({s_0\over2}-o(1)\right)D.
\tag{DI.16}
```

Therefore

```math
\max\{N_L,N_U\}
>{1\over2}
\left({s_0\over2}-o(1)\right)D
=
\left({s_0\over4}-o(1)\right)D,
```

which proves (DI.6).

Each witness keeps the interface at which it was selected as its owner. Because the witness pairs are distinct, the owner map is injective. This is exactly the ownership property required by the downstream UPPER localization and LOWER support-overlap arguments.

---

## 6. UPPER propagation

Assume

```math
N_U>
\left({s_0\over4}-o(1)\right)D.
\tag{DI.17}
```

The flexible-scale UPPER localization proof uses only a linear family of distinct near-diameter blockers, injective owner coordinates, exact selected-cut interval support, the Oler path-row cap, and the global defect/terminal budgets. It does not require that the family was produced by the Horn graph.

Thus substitute

```math
\delta_{\rm dir}:={s_0\over4}
```

for the former Horn input density. The latest Oler path-capacity form gives localized same-type coefficient

```math
{\delta_{\rm dir}\over6A_*}
={113\sqrt3\over5{,}120{,}000{,}000},
```

proving (DI.8).

For every `L_D->infinity` with `L_D=o(D)`, one obtains either at least

```math
(c_{\rm dir}-o(1))L_D
```

SIGNED or THIN blockers on one low-defect selected row, or that many in one `2L_D+O(1)` low-cost path window. The existing `(0.6536-o(1))D` common train scaffold and circumcenter flanks are unchanged.

---

## 7. LOWER propagation

Assume instead

```math
N_L>
\left({s_0\over4}-o(1)\right)D.
\tag{DI.18}
```

Every LOWER blocker has exact support one selected row. Injective owner coordinates imply that one support row is used by at most two blockers: its two possible owners are the adjacent path layers.

Let `F_k` be the full angular-defect cost on row `tau_k`. Charging `F_k` to every blocker supported there counts each row at most twice, so the total charged cost is `O(D)`. Retaining the low-cost half gives (DI.9).

Every good row has the standard phase-pure family

```math
|P(e)|>(0.6436-o(1))D.
```

The complete-train count is

```math
T_D<(T_*+o(1))D,
\qquad T_*={6121\over2000}.
```

Averaging blocker/train incidences gives one fixed train on more than

```math
\left(
{s_0\over8}{0.6436\over T_*}-o(1)
\right)D
```

good blocker rows. The exact coefficient is

```math
{1{,}272{,}719\over19{,}587{,}200{,}000{,}000}
=6.49770768665\ldots\times10^{-8},
```

which proves (DI.10).

Since any support row occurs at most twice, retaining one of two row-disjoint color classes gives (DI.11) with exact coefficient

```math
{1{,}272{,}719\over39{,}174{,}400{,}000{,}000}.
```

---

## 8. Frontier effect

The one-sign strong-TB1 seam can now be stated without any residue-class loss:

```text
one-sign interfaces > (s0/2-o(1))D;
one exact-swap witness per interface;
LOWER witness repetition: impossible;
UPPER witness repetition: O(1) source-wide;
cross-type repetition: impossible;
therefore distinct witnesses > (s0/2-o(1))D;
therefore one metric type > (s0/4-o(1))D.
```

The Horn closure system remains relevant if one needs simultaneous-swap dependency structure, but it is no longer the right tool for counting blocker density.

The remaining LOWER target is local and exact: each witness is the near-unit diagonal of one strict rhombus on the owner strip boundary. The remaining UPPER target is the existing SIGNED/THIN metric-order closure, now with the larger coefficient (DI.8).

**Disposition:** proved source-wide injectivity up to `O(1)` for exact-swap witnesses, raised the direct LOWER/UPPER metric floor to `s0/4`, and propagated the gain to both the Oler-localized UPPER branch and the one-row LOWER ladder. C-II and Level I remain open.
