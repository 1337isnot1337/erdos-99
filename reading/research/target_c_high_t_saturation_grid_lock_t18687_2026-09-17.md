> Generated reading edition · [exact source](../../research/target_c_high_t_saturation_grid_lock_t18687_2026-09-17.md) · source SHA-256 `54b8c1f121e88a53f1411b76887aed215cbb64e1c368c347142ba176a039e6b7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5071cf04f2c2c710211299f595d04730b085954c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_saturation_grid_lock_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "48e6129d9ac18e2acec451f0b653a40d98c5a5bdecddf1ffc5152f0d4edf5adc"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — region saturation locks an unconditional diameter rail to the common train grid

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` complete rectangle and phase collapse; phase-free path-region saturation; diameter-path Helly hub and one-sided switching; full opposite-or-terminal nesting theorem  
**Certificate:** `research/verify_target_c_high_t_saturation_grid_lock_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The complete-rectangle theorem and the region-saturation theorem have so far been used mostly in parallel. They can be synchronized directly.

The phase-collapsed train rectangle supplies a row family

$$
A_0\subset\{\tau_1,\ldots,\tau_m\},
\qquad
|A_0|>{7\over625000}D-o(D)=0.0000112D-o(D),
\tag{SG.1}
$$

and a transverse family

$$
|B_0|>{783\over10000}D-o(D)=0.0783D-o(D),
\tag{SG.2}
$$

such that every `A_0 x B_0` crossing is one strict rhombus with common order and

$$
0<\theta_{ab}-{\pi\over3}
<{7.7\times10^6\over D}+o(D^{-1}).
\tag{SG.3}
$$

On the other hand, every internal path region contains an actual switching diameter and every nonhub switch points toward the common hub. A median argument on the row indices now produces a linear family of actual diameter bars whose selected-cut supports contain one common linear subfamily of `A_0`.

Thus the high-`t` survivor contains an unconditional three-layer scaffold

```text
actual diameter bars E_0
        x
phase-collapsed path rows A_1
        x
common transverse trains B_0
```

where every `E_0` bar spans every `A_1` cut and every `A_1 x B_0` pair is a near-equilateral strict rhombus.

---

## Theorem SG — a linear diameter family spans a linear phase-collapsed row block

Let `R_k` be the common diameter-routing hub. Remove from `A_0` the at most two path cuts incident with `R_k`, if present. One strict side of the hub then contains a row subfamily `A^side` with

$$
|A^{side}|>{7\over1250000}D-o(D).
\tag{SG.4}

Reverse the path if necessary so these rows are pre-hub. Write their selected-path indices as

\[
j_1<j_2<\cdots<j_R<k.
\tag{SG.5}

Put `L=floor(R/2)` and take the last `L` rows,

\[
A_1=\{\tau_{j_{R-L+1}},\ldots,\tau_{j_R}\}.
\tag{SG.6}
$$

Then

$$
\boxed{
|A_1|>{7\over2500000}D-o(D)
=2.8\times10^{-6}D-o(D).
}
\tag{SG.7}

Because the indices in (SG.5) are distinct positive integers,

\[
j_{R-L+1}-1\ge R-L\ge L.
\tag{SG.8}
$$

For every internal region `R_i` with

$$
1\le i<j_{R-L+1},
$$

region saturation supplies at least one actual switching diameter bar `e_i` incident with `R_i`. Since `i<k`, one-sided switching sends its other endpoint to a region `R_{b_i}` with `b_i>=k`. Its exact selected-cut support is therefore

$$
I_i=\{i+1,\ldots,b_i\}.
\tag{SG.9}

In particular every row index in `A_1` lies in every such support:

\[
\boxed{
j_s\in I_i
\qquad(1\le i<j_{R-L+1},\ s\ge R-L+1).}
\tag{SG.10}

Equation (SG.8) supplies at least `L=|A_1|` such birth regions, so choose any `L` of them. Their selected switching bars form a family `E_0` with

\[
\boxed{
|E_0|>{7\over2500000}D-o(D).
}
\tag{SG.11}

The bars are distinct because an actual diameter interval containing the hub has at most one endpoint region on this strict pre-hub side.

Equations (SG.10)--(SG.11) give an exact complete support-incidence rectangle:

\[
\boxed{
E_0\times A_1
\text{ is complete in selected-cut incidence.}
}
\tag{SG.12}

Equivalently, every diameter in `E_0` has endpoints on opposite sides of every O--O crosscut in `A_1`.

No exact-antipodal or strong-TB1 hypothesis is used.

---

## 1. The same rows retain the full common transverse train grid

Because `A_1 subset A_0`, all conclusions of the phase-collapse theorem persist without loss on the transverse shore `B_0`:

\[
\boxed{|B_0|>0.0783D-o(D),}
\tag{SG.13}

and for every `a in A_1`, `b in B_0`,

\[
\boxed{
{\pi\over3}<\theta_{ab}
<{\pi\over3}+{7.7\times10^6\over D}+o(D^{-1}).
}
\tag{SG.14}

Every cross-pair is a distinct strict rhombus, both train shores are internally noncrossing, and the crossing order is common on both shores.

Combining (SG.12) and (SG.14), the current high-`t` source contains simultaneously

\[
|E_0|>2.8\times10^{-6}D-o(D),
$$

$$
|A_1|>2.8\times10^{-6}D-o(D),
$$

$$
|B_0|>0.0783D-o(D),
$$

with

```text
E_0 -> every bar spans every A_1 selected cut;
A_1 x B_0 -> complete common-order strict-rhombus grid;
all A_1 x B_0 angles = pi/3 + O(1/D).
```

This is an unconditional synchronization between actual diameter geometry and the inverse-`D` train grid. Earlier common-grid force-cell results synchronize stronger KKT metadata but only on the exact-force branch; (SG.12)--(SG.14) hold before resolving the exact-antipodal/strong-TB1 fork.

---

## 2. A nested grid-spanning diameter lane

The birth endpoints of `E_0` lie in distinct pre-hub regions. Split them by the two physical birth host arcs. One host class `E_1` has

$$
\boxed{
|E_1|>{7\over5000000}D-o(D)
=1.4\times10^{-6}D-o(D).
}
\tag{SG.15}

Every bar of `E_1` still spans every row of `A_1`. Applying the full opposite-or-terminal nesting theorem to `E_1` gives, in increasing birth-interface order,

\[
I_1\supsetneq I_2\supsetneq\cdots,
\tag{SG.16}

and every partner endpoint lies on the opposite physical host or on `T_m`.

Thus there is an unconditional **grid-spanning nested diameter rail** of density `1.4e-6`: every rail support contains the same `2.8e-6D` phase-collapsed row family, and those rows all meet the same `0.0783D` transverse family at angle `pi/3+O(1/D)`.

If a single physical destination is required, one of the opposite-host or far-terminal subrails has

\[
\boxed{
>{7\over10000000}D-o(D)
=7\times10^{-7}D-o(D).
}
\tag{SG.17}

---

## 3. Endpoint-disjoint synchronized braids

The births are distinct and lie strictly before the hub while all partners lie hubward, so partner collisions are the only endpoint collisions inside `E_0` or `E_1`. With

\[
\Delta(H_D)\le(4\,3^{1/8}+o(1))D^{3/4},
\tag{SG.18}

we obtain the following endpoint-disjoint, hence pairwise-crossing, diameter subfamilies:

- from `E_0`:
  \[
  \boxed{
  >\left({7/2500000\over4\,3^{1/8}}-o(1)\right)D^{1/4}
  }
  \tag{SG.19}
  $$
  with coefficient `6.10179880010e-7`;
- from the nested one-birth-host lane `E_1`:
  $$
  \boxed{
  >\left({7/5000000\over4\,3^{1/8}}-o(1)\right)D^{1/4}
  }
  \tag{SG.20}
  $$
  with coefficient `3.05089940005e-7`;
- after fixing one physical destination:
  $$
  \boxed{
  >\left({7/10000000\over4\,3^{1/8}}-o(1)\right)D^{1/4}
  }
  \tag{SG.21}
  $$
  with coefficient `1.52544970003e-7`.

Every retained bar still spans every row in `A_1`; thinning diameter endpoints does not change the train grid.

---

## 4. Why this is different from the deep exact-force common-grid theorem

The deep exact-force common-grid theorem is stronger locally. It associates force pairs, exact antipodal cancellation, and coercive dipole directions to selected deep cells. The present theorem does not recover those facts.

What it adds is an unconditional bridge:

```text
phase-free region saturation
        +
common diameter hub
        +
phase-collapsed complete train rectangle
        |
        v
linear actual-diameter family E_0
whose every support contains one common linear A_1 row set,
while A_1 crosses the same macroscopic B_0 column set
at pi/3 + O(1/D).
```

So a closing argument no longer has to choose between “many actual diameters from region saturation” and “the common inverse-`D` train grid.” A linear family of actual diameters is now locked to that grid at the level of exact cut incidence.

This still does not prove C-II. Selected-cut incidence is topological; it does not by itself give a quantitative lower bound on the Euclidean crossing angle between a diameter chord and a row train, nor does it attach KKT mass to the bars in `E_0`. The next useful step is to exploit the straightness/near-antipodality of the diameter chords inside this common ordered near-triangular grid, or to intersect this unconditional scaffold with the force-labeled blocker population without paying away the linear row set.

**Disposition:** synchronized a `2.8e-6 D` actual-diameter family with a `2.8e-6 D x 0.0783 D` common-order inverse-`D` train grid, and extracted a `1.4e-6 D` nested grid-spanning rail. C-II and Level I remain open.
