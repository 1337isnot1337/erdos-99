> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_eight_crossing_floor_2026-09-27.md) · source SHA-256 `e32f8d5e10544ca941b2e5816a61df7d6d47378a545ee83beda4ef5254346c78`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "7739c7212c4cb55c75d2072e150828394387ab52", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_eight_crossing_floor_2026-09-27.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5fdb840e1bbd5c021282c13c4708926340ec349eff17d3d627739df3a8ac3de6"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II: collapsed support-six blocks consume at least eight strict rhombi

Date: 2026-09-27

Status: unreviewed proof-level finite/global train-topology candidate. C-II remains open. The exact verifier was re-run during salvage; this report does not change canonical theorem status.

Companion verifier:
research/verify_target_c_support6_collapsed_eight_crossing_floor_2026_09_27.cpp

Salvage provenance: source branch `target-c-support6-eight-crossing-floor-20260927`, tip `a8d4b5d01401516e04c93a3b325ff5ace7ad5f53`. This report and verifier were copied onto current main without theorem-state or route changes.

The existing audited certificate proves that every global degree-pure collapsed
support-six block has at least seven internal strict-rhombus crossings. This note
checks the only new endpoint, exactly seven crossings, and eliminates it.

If $X_K$ is the number of strict-rhombus crossings whose two complete trains are
among the twelve internal relation trains of one collapsed support-six block $K$,
then

$$
\boxed{X_K\ge 8.}
\tag{EC.1}
$$

The new computation uses the same exact necessary conditions as the committed
seven-crossing-floor certificate: MI.1 mod-2 relation-cycle equations, one common
strict projective-angle vector, forced crossing rotations, and exact orientable
planarization genus.

## 1. Symmetry reduction

The committed collapsed rotation-cell census has 388 labelled feasible cells:
180 for the all-cross missing matching and 208 for the mixed missing matching.
The same sign-preserving face relabelings and common-anchor-line reflection used
by that census split them into 15 and 27 conservative symmetry orbits.

These symmetries preserve the seven-crossing question. Face/train relabeling merely
renames the MI.1 variables. Reflection sends every projective angle $x_e$ to
$3-x_e$ while reversing coherent train orientation, so the strict crossing
condition $1<|x_e-x_f|<2$ is invariant. The determinant sign defining the
crossing rotation transforms together with the train orientations, and relabeling
or reflection preserves genus zero of the planarized rotation system.

Therefore any realizable seven-crossing pattern in one of the 388 labelled cells
would transport to a realizable pattern in its chosen orbit representative. The
verifier reuses the committed transform_cell and cell_key implementation and
asserts representative counts 15 and 27.

## 2. Exact seven-set enumeration

There are 66 unordered pairs among the twelve internal relation trains. Row
reduction of all edge-disjoint relation-cycle MI.1 equations gives one binary
target $t$ and syndrome columns $s_j$. A selected seven-set $S$ satisfies all
MI.1 equations exactly when

$$
\bigoplus_{j\in S}s_j=t.
\tag{EC.2}
$$

The verifier enumerates every increasing seven-subset exactly once by a 3+4
meet-in-the-middle split. It stores every increasing triple by XOR syndrome,
loops over every increasing quadruple, and joins only triples whose final index
is smaller than the quadruple's first index.

For every MI.1-consistent seven-set, all seven selected crossing windows are then
added to the exact integer strict-difference system. Unselected pairs receive no
condition, so this remains a relaxation in the safe direction. For each jointly
feasible orientation, every permutation of selected crossings along each
multiply-crossed train is enumerated, the crossings are planarized, and the
orientable genus is computed from Euler characteristic.

Executed exact result:

$$
\begin{array}{c|r|r|r}
\text{matching type}&\text{MI.1 seven-sets}&\text{joint-angle seven-sets}&
\text{planar seven-sets}\\ \hline
\text{all-cross}&324634&964&0\\
\text{mixed}&543490&1580&0
\end{array}
\tag{EC.3}
$$

Total: 868124 MI.1-consistent seven-sets, 2544 jointly angle-feasible seven-sets,
and zero planar seven-sets across all 42 cell orbits.

All logical decisions are exact: bit arithmetic over $\mathbf F_2$, integer
strict-difference feasibility, finite permutation enumeration, and integer
Euler-characteristic genus. No floating-point comparison is used.

Together with the already audited exhaustive exclusion of 0 through 6 crossings
in all 388 cells, the zero count at exactly seven proves (EC.1).

## 3. Global payment consequence

Different collapsed support-six blocks have disjoint internal relation-train sets,
and a bounded strict rhombus belongs to exactly one pair of complete trains. The
same counting argument used for the previous seven-crossing floor now gives

$$
\boxed{R_4\ge 8c_6,\qquad c_6\le R_4/8.}
\tag{EC.4}
$$

Combining this with the committed tangent payment

$$
d_C\ge M_0+2c_6+(c_6-1)_+,\qquad
M_0=(b-f)/2+E_U+p_U
\tag{EC.5}
$$

gives, on the branch $c_6>0$,

$$
c_6\le (d_C-M_0+1)/3.
\tag{EC.6}
$$

Thus the current support accounting sharpens to

$$
\boxed{
\sigma_C\le
2n_0+n_2+n_1/7+x_U/7+
\min\{(d_C-M_0+1)/21,\ R_4/56\}.
}
\tag{EC.7}
$$

This is a strict strengthening of the collapsed support-six payment. It does not
exclude collapsed support-six blocks outright and does not close C-II by itself.
