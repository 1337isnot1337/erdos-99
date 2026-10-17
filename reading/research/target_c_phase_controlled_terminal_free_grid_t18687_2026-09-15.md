> Generated reading edition · [exact source](../../research/target_c_phase_controlled_terminal_free_grid_t18687_2026-09-15.md) · source SHA-256 `c6a7adfe77c03ecc88f2da02889488d9844d15cd4500f394e22a7eb8fb595ed1`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bb9048f152925624d1b8d64748c298c6d0cd8137", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_phase_controlled_terminal_free_grid_t18687_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "98904ba0e12400b6c1fd8a26b77d33eefd7a357d5fd65e3d7da67b768c2d663b"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a phase-controlled terminal-free grid corridor at `t<=1.8687`

**Date:** 2026-09-15  
**Status:** proof-only local normal-form strengthening  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** high-`t` rectangle joint cusp; terminal-free rhombic corridor theorem; simple triangle-free stopped-train crossing graph  
**Certificate:** `research/verify_target_c_phase_controlled_terminal_free_grid_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The terminal-free corridor theorem used the full oriented common-column family `B_+`. The joint cusp provides a smaller but much more rigid subfamily `B_0 subset B_+`:

$$
\boxed{|B_0|>0.0783D-o(D),}
\tag{PG.1}
$$

and for every `b in B_0` and both selected adjacent O--O rows `a_0,a_1`,

$$
\boxed{
0<\theta(a_r,b)-{\pi\over3}
<{1.416\times10^7\over D}+o(D^{-1}).
}
\tag{PG.2}
$$

Apply the same terminal-cell argument to the ordered `B_0` crosscuts. Since the selected strip has at most `1,108,999` terminal occurrences, one obtains a consecutive terminal-free run of `B_0` column gaps of length

$$
\boxed{
>{783\over11{,}090{,}000{,}000}D-o(D)
>7.06\times10^{-8}D-o(D).
}
\tag{PG.3}
$$

Every selected column in this run lies in one inverse-diameter projective phase window:

$$
\boxed{
\operatorname{diam}_{\mathbb{RP}^1}\{[b]:b\text{ is a selected }B_0\text{ column in the run}\}
<{2.832\times10^7\over D}+o(D^{-1}).
}
\tag{PG.4}
$$

The two row phases themselves obey

$$
\boxed{
d_{\mathbb{RP}^1}(a_0,a_1)
<{7.08\times10^6\over D}+o(D^{-1}).}
\tag{PG.5}
$$

Thus the clean corridor already contains a linear two-row-by-many-column scaffold converging uniformly to an exact triangular-lattice two-phase grid.

There is an additional exact topological statement, independent of the `O(D^{-1})` estimates. Every individual terminal-free ladder cell is **rectangularly saturated** by the complete stopped trains that meet it: all such trains split into two through-families, each family is internally noncrossing, and every cross-family pair crosses exactly once in a strict rhombus. No third terminal behavior can occur inside the cell.

---

## 1. The phase-controlled clean run

The joint-cusp Markov selection gives `B_0` with (PG.1)--(PG.2). Order the columns by their common crossing order on the two selected rows. As in the terminal-free corridor theorem, the between-row portions are disjoint proper crosscuts of the parent strip.

There are `|B_0|-1` internal cells between consecutive `B_0` crosscuts. A terminal occurrence cannot lie on an internal selected centerline, so at most

$$
L_0:=1{,}108{,}999
$$

of these cells contain any stopped-train terminal. Removing the bad cells leaves at most `L_0+1` clean runs. Therefore the longest run has at least

$$
{|B_0|-1-L_0\over L_0+1}
$$

cells. Using `|B_0|>0.0783D-o(D)` gives

$$
>{0.0783\over1{,}109{,}000}D-o(D)
={783\over11{,}090{,}000{,}000}D-o(D),
$$

which proves (PG.3).

As before, every cell in the run is internal to the selected O--O strip and therefore contains no actual diameter endpoint and no bounded nonquadrilateral contact face.

---

## 2. Uniform column-phase collapse on the entire run

The `B_0` selection lies on one common oriented branch. Choose compatible lifts `alpha_0,alpha_1` for the row phases and `beta_b` for the column phases so that

$$
\delta_{rb}:=\beta_b-\alpha_r-{\pi\over3}>0.
$$

Equation (PG.2) gives

$$
0<\delta_{rb}
<{1.416\times10^7\over D}+o(D^{-1})
$$

for every selected run column and both rows.

For any two run columns `b,b'`, using one fixed row,

$$
|\beta_b-\beta_{b'}|
=|\delta_{0b}-\delta_{0b'}|
\le\delta_{0b}+\delta_{0b'}.
$$

Hence

$$
|\beta_b-\beta_{b'}|
<{2.832\times10^7\over D}+o(D^{-1}),
$$

which proves (PG.4). The row bound (PG.5) is inherited unchanged from the joint cusp.

Thus every selected row/column crossing in this whole linearly long run has the same oriented triangular-limit pattern, not merely one averaged microcell.

---

## 3. Exact rectangular saturation of a terminal-free cell

Fix one clean internal cell `K` between consecutive selected columns `b_0,b_1`. Its four train-centerline sides are subarcs of

$$
a_0,\ b_1,\ a_1,\ b_0
$$

in cyclic order; adjacent boundary trains cross at the four corner rhombi, while opposite boundary trains are noncrossing.

Take any complete stopped train `sigma` distinct from the four boundary trains and suppose its centerline meets `int K`.

Because `K` contains no train terminal, `sigma` cannot end inside `K`. Because two complete trains cross at most once, `sigma` cannot enter and leave through the same boundary train. Finally `sigma` cannot cross two adjacent boundary trains: if it crossed, say, `a_0` and `b_0`, then the three trains

$$
\sigma,\ a_0,\ b_0
$$

would be pairwise crossing, contradicting triangle-freeness of the stopped-train crossing graph.

Therefore `sigma` crosses exactly one pair of opposite sides. There are only two possibilities:

- **column-like:** `sigma` crosses both rows `a_0,a_1`;
- **row-like:** `sigma` crosses both columns `b_0,b_1`.

No third behavior occurs.

Let `mathcal C_K` be the column-like family and `mathcal R_K` the row-like family.

### Same-family noncrossing

Two distinct trains of `mathcal C_K` both cross `a_0`. If they crossed each other they would form a crossing triangle with `a_0`. Hence `mathcal C_K` is pairwise noncrossing. Likewise `mathcal R_K` is pairwise noncrossing because every member crosses `b_0`.

### Cross-family completeness

For `c in mathcal C_K` and `r in mathcal R_K`, the portions inside `K` are proper arcs joining opposite pairs of sides of a topological quadrilateral. Such arcs must intersect. Complete trains cross at most once, so they intersect exactly once. The intersection is the center of a strict rhombus.

Consequently, after adjoining the two boundary columns to `mathcal C_K` and the two boundary rows to `mathcal R_K`, the train-crossing graph realized in `cl K` is exactly

$$
\boxed{K_{p,q}}
\tag{PG.6}
$$

for some `p,q>=2`, with every cross edge realized by one distinct strict-rhombus crossing.

This is an exact finite statement; no phase limit is used.

---

## 4. Frontier effect

The live obstruction now contains a region with all of the following properties simultaneously:

```text
terminal-free for a linear number of consecutive cells;
no bounded exceptional contact face;
no actual diameter endpoint;
>7.06e-8 D selected transverse train gaps;
all selected transverse phases in an O(1/D) window;
two O-O row phases in an O(1/D) window;
every selected row/column rhombus angle = pi/3+O(1/D);
each clean cell is an exact complete-bipartite train grid.
```

This removes local branching and endpoint defects from the near-triangular scaffold. The remaining obstruction is external: the complete trains extend beyond the corridor, and the selected row multishear is still locked by the one-sided finite diameter interface outside it.

A useful next theorem should couple that external ordered diameter-thrackle interface to the exact rectangular train order, rather than treating the active diameter rows as an arbitrary finite cusp.

**Disposition:** proved a macroscopic phase-controlled terminal-free grid corridor and exact rectangular train saturation through `t<=1.8687`. C-II and Level I remain open.
