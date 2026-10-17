<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "034c82ad3c091d43429882825c0202bb3162e050", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_signed_local_window_cell_reduction_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "2bd6517e704822ef92d31da168339340e26919c86381454fc2d71f6b3e51f7be"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — SIGNED LOCAL-WINDOW braids reduce to one path cell or one train-fence cell

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the SIGNED / LOCAL-WINDOW branch; no canonical promotion claimed  
**Scope:** the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** upper-blocker LOCAL-WINDOW localization; bounded-noncrossing-degree SIGNED braid; stopped-train step-cone theorem; exact path support; proper-crosscut train model  
**Certificate:** `research/verify_target_c_high_t_tb1_signed_local_window_cell_reduction_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The LOCAL-WINDOW side of the SIGNED upper branch now contains a pairwise-properly-crossing vertex-disjoint braid

\[
F_D,
\qquad
|F_D|=D^{1/4-o(1)},
\]

whose endpoints all lie in one path window of width `O(D/log D)`. The whole window carries one common family

\[
B_D,
\qquad
|B_D|>(0.6536-o(1))D,
\]

of complete stopped trains crossing every selected row in the window in strict unit rhombi.

There is an exact uniqueness dichotomy in any such complete train rectangle which does not require inverse-`D` phase purification.

For a complete train with transverse contact direction `[u]`, the stopped-train theorem puts every midpoint step in the open projective interval

\[
\mathcal C(u)
=
\left([u]+{\pi\over3},[u]+{2\pi\over3}\right)
\pmod\pi.
\]

If two trains cross in a strict unit rhombus, their transverse directions differ projectively by a directed angle in `(pi/3,2pi/3)`. Their **closed** midpoint-step cones are therefore disjoint.

It follows that for any straight line `ell` and any complete rectangle `A x B` of crossing trains, one of the following holds:

- **ROW-UNIQUE:** `ell` meets every row in `A` at most once; or
- **COLUMN-UNIQUE:** `ell` meets every column in `B` at most once.

Indeed, if the line direction lies outside every closed column cone, COLUMN-UNIQUE holds. Otherwise it lies in the closed cone of some column `b_0`; that cone is disjoint from the closed cone of every row crossing `b_0`, so ROW-UNIQUE holds simultaneously for all rows.

Applying this chordwise and retaining one mode leaves a `D^(1/4-o(1))` SIGNED braid. Each mode then becomes an exact interval system.

In ROW-UNIQUE, every chord intersects exactly the selected rows in its exact path-support interval and no others. Pairwise crossing forces the corresponding closed endpoint-region intervals to intersect pairwise, so one-dimensional Helly gives one fixed path region `R_g` contained in every chord interval.

In COLUMN-UNIQUE, every chord intersects exactly the consecutive set of common columns separating its endpoint fence cells and no others. Pairwise crossing again gives a Helly point: one fixed `B_D` fence cell `C_h` lies in every chord's closed fence interval.

After one four-way split, a quarter-power braid therefore has one fixed relation to one fixed cell:

```text
THROUGH
LEFT-ANCHORED
RIGHT-ANCHORED
CELL-INTERNAL.
```

For the ROW-UNIQUE THROUGH class, every chord supports a common selected cut, so this subcase feeds directly into the existing SIGNED COMMON-CUT robust-owner-grid theorem. Thus the genuinely new LOCAL-WINDOW remainder is cell-local: either a polynomial crossing braid has an endpoint population anchored in one fixed path region, both endpoint populations lie in that region, or the corresponding exact alternatives hold for one fixed cell of a linear train fence.

---

## 1. Crossed train step cones are disjoint

Let `a,b` be complete stopped trains crossing in one strict unit rhombus. Write their fixed projective transverse contact directions as

\[
[u_a],\qquad [u_b].
\]

Choose representatives so that

\[
[u_b]=[u_a]+\delta\pmod\pi,
\qquad
{\pi\over3}<\delta<{2\pi\over3}.
\tag{LW.1}
\]

The interval (LW.1) is exactly the strict-rhombus condition: for a unit rhombus both noncontact diagonals exceed one, so the directed angle between its two side directions lies strictly between `pi/3` and `2pi/3`.

The midpoint-step theorem gives the open cones

\[
\mathcal C_a
=
\left([u_a]+{\pi\over3},[u_a]+{2\pi\over3}\right),
\tag{LW.2}
\]

\[
\mathcal C_b
=
\left([u_b]+{\pi\over3},[u_b]+{2\pi\over3}\right)
\pmod\pi.
\tag{LW.3}
\]

Normalize `[u_a]=0` on a projective circle of circumference `pi`. Then

\[
\overline{\mathcal C_a}
=
\left[{\pi\over3},{2\pi\over3}\right].
\tag{LW.4}
\]

Because of (LW.1), the closed cone of `b` wraps as

\[
\overline{\mathcal C_b}
=
\left[0,\delta-{\pi\over3}\right]
\cup
\left[\delta+{\pi\over3},\pi\right].
\tag{LW.5}
\]

The first interval in (LW.5) ends strictly before `pi/3`, while the second starts strictly after `2pi/3`. Therefore

\[
\boxed{
\overline{\mathcal C_a}
\cap
\overline{\mathcal C_b}
=\varnothing.
}
\tag{LW.6}

This is exact and uses only strict unit-rhombus geometry.

---

## 2. Dual-cone uniqueness for a complete train rectangle

Let `A` and `B` be two families of complete trains such that every

\[
a\in A,
\qquad b\in B
\]

crosses in a strict unit rhombus.

Let `ell` be any straight line with projective direction `[d]`.

The line/train uniqueness theorem says

\[
[d]\notin\overline{\mathcal C(u)}
\quad\Longrightarrow\quad
\ell\text{ meets the complete midpoint curve of the train }u
\text{ at most once}.
\tag{LW.7}

There are two cases.

### Case C

If

\[
[d]\notin\overline{\mathcal C_b}
\qquad\forall b\in B,
\]

then (LW.7) gives

\[
\boxed{
\ell\text{ meets every }b\in B\text{ at most once}.
}
\tag{LW.8}

### Case R

Otherwise choose `b_0 in B` with

\[
[d]\in\overline{\mathcal C_{b_0}}.
\]

For every `a in A`, equation (LW.6) applied to the crossing pair `(a,b_0)` gives

\[
[d]\notin\overline{\mathcal C_a}.
\]

Hence

\[
\boxed{
\ell\text{ meets every }a\in A\text{ at most once}.
}
\tag{LW.9}

Thus every straight line satisfies at least one of (LW.8)--(LW.9). No phase error or directional-capacity deletion is needed.

---

## 3. Apply the exact fork to the SIGNED LOCAL-WINDOW braid

Use the LOCAL-WINDOW outcome of the upper localization theorem. Let

\[
A_W
\]

be all selected rows inside the chosen window, and let

\[
B_W
\subseteq
\bigcap_{a\in A_W}\Gamma_a
\]

be the common column family after the window purification. Then

\[
\boxed{|B_W|>(0.6536-o(1))D}
\tag{LW.10}
\]

and every pair in

\[
A_W\times B_W
\]

crosses in a strict unit rhombus. The columns in `B_W` are pairwise noncrossing and have one common order on every row.

By the bounded-noncrossing-degree theorem, the localized SIGNED blocker population contains a vertex-disjoint pairwise-crossing braid `F_D` with

\[
\boxed{|F_D|=D^{1/4-o(1)}}.
\tag{LW.11}

Apply Section 2 to the supporting line of each chord. Split `F_D` according to whether the line uses Case R or Case C and retain the larger class. The retained family still has size

\[
D^{1/4-o(1)}.
\tag{LW.12}

---

## 4. ROW-UNIQUE gives exact path incidence

Assume Case R. Let one retained blocker `e=xy` have endpoint path regions

\[
x\in R_p,
\qquad y\in R_q,
\qquad p\le q.
\]

The exact path-support theorem gives

\[
I_A(e)=\{p+1,\ldots,q\}.
\tag{LW.13}
\]

For every `j in I_A(e)`, row `tau_j` separates the endpoints, so the segment meets it at least once. ROW-UNIQUE gives at most one intersection, hence exactly one.

For a row `tau_j` in the local window but outside (LW.13), both endpoints lie on the same side. Any line/train intersection in ROW-UNIQUE is proper because the signed line-normal coordinate is strictly monotone along the train. A single proper crossing would change sides, so with at most one intersection there can be none.

Therefore

\[
\boxed{
 e\cap\tau_j\ne\varnothing
 \iff
 j\in I_A(e),
}
\tag{LW.14}

and every nonempty intersection consists of one point.

Define the closed endpoint-region interval

\[
J_A(e)=[p,q].
\tag{LW.15}

Equation (LW.14) confines the whole segment to the closed path slab indexed by `J_A(e)`.

Take two retained chords `e,f`. If their intervals were disjoint, one selected row between the intervals would separate the two closed slabs, so the two segments could not cross. Since the braid is pairwise properly crossing,

\[
J_A(e)\cap J_A(f)\ne\varnothing
\qquad\forall e,f.
\tag{LW.16}
\]

Closed intervals on a line have Helly number two. Hence

\[
\boxed{
\bigcap_eJ_A(e)\ne\varnothing.
}
\tag{LW.17}

Choose one integer path-region rank

\[
g_D\in\bigcap_eJ_A(e).
\tag{LW.18}

Every retained chord therefore has

\[
p\le g_D\le q.
\tag{LW.19}

Split into the four exact types

\[
\begin{array}{ll}
\textbf{THROUGH}:&p<g_D<q,\\
\textbf{LEFT-ANCHORED}:&p<q=g_D,\\
\textbf{RIGHT-ANCHORED}:&p=g_D<q,\\
\textbf{CELL-INTERNAL}:&p=q=g_D.
\end{array}
\tag{LW.20}

One class has size `D^(1/4-o(1))`.

In THROUGH, every chord supports a common selected row (indeed both adjacent rows when `g_D` is internal). Thus this class is reducible to the existing COMMON-CUT SIGNED theorem with the stronger quarter-power input.

The other three classes place at least one whole endpoint population in the fixed path region `R_{g_D}`; CELL-INTERNAL places both there.

---

## 5. COLUMN-UNIQUE gives exact train-fence incidence

Assume Case C. The common columns

\[
b_1<\cdots<b_M,
\qquad
M=|B_W|>(0.6536-o(1))D,
\tag{LW.21}

are pairwise noncrossing proper crosscuts and define ordered fence cells

\[
C_0,\ldots,C_M.
\]

For a retained chord `e=xy`, let

\[
c(x)=s,
\qquad c(y)=t,
\qquad s\le t.
\]

Every column `b_{s+1},...,b_t` separates the endpoint cells and is met at least once. COLUMN-UNIQUE makes each such meeting unique. A column outside this interval has the endpoints on the same side; all intersections are proper and at most one, so there are none.

Hence

\[
\boxed{
I_B(e)=\{s+1,\ldots,t\},
}
\tag{LW.22}
\]

and the chord is confined to the closed fence interval

\[
J_B(e)=[s,t].
\tag{LW.23}

As in Section 4, pairwise crossing forces pairwise overlap of these closed intervals. Helly gives one fixed fence-cell rank

\[
h_D\in\bigcap_eJ_B(e).
\tag{LW.24}

After the same four-way split relative to `h_D`, one class of size

\[
\boxed{D^{1/4-o(1)}}
\tag{LW.25}

is uniformly THROUGH, LEFT-ANCHORED, RIGHT-ANCHORED, or CELL-INTERNAL with respect to one fixed cell `C_{h_D}` of the linear common train fence.

This is the LOCAL-WINDOW analogue of the existing source-wide `B_0` fence-cell reduction, but it uses the denser local common family `(0.6536-o(1))D` available across the whole low-defect window.

---

## 6. Frontier effect

The SIGNED localization dichotomy is now cell-local on both sides.

```text
COMMON-CUT:
    quarter-power crossing braid
    -> quarter-power robust owner grid
    -> ROW-UNIQUE one-sided cables or COLUMN-UNIQUE one fixed B_0 fence cell.

LOCAL-WINDOW:
    quarter-power crossing braid inside O(D/log D) path regions
    x one common >0.6536D train family
    -> exact dual-cone uniqueness fork
    -> either one fixed path region belongs to every chord interval
       or one fixed common-column fence cell belongs to every chord interval;
    -> after a four-way split, quarter-power THROUGH / anchored / internal type.
```

The ROW-UNIQUE THROUGH subcase is already a COMMON-CUT instance. The unresolved LOCAL-WINDOW geometry is therefore concentrated in anchored or cell-internal near-diameter braids: a `D^(1/4-o(1))` reversed crossing matching has one or both endpoint populations trapped in one fixed path cell or one fixed dense-train fence cell.

A closing theorem now needs a metric capacity/width bound for one such cell, or a way to combine the fixed SIGNED transverse projection and central near-diameter midpoint localization with the anchored endpoint population.

**Disposition:** proved an exact dual-cone row/column uniqueness theorem for complete train rectangles and reduced the entire SIGNED LOCAL-WINDOW braid to one fixed path cell or one fixed train-fence cell. C-II and Level I remain open.
