<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d4420b07fdd8b03c6f88106bd24cc15ed398f39c", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_post186177_audit_synthesis_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "82be5c81fc190f55a3c2eb3aa46012e0ee6bd98311a979590ffdc3821511c722"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — post-1.86177 audit synthesis and surviving obstruction

**Date:** 2026-09-15
**Status:** audit/synthesis; no new closure claim
**Base:** `origin/main` at `c5f6f9669fc9` when this note was written
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

This note records the outcome of an independent post-`1.86177` research run. The run started from the corrected O--O path frontier, tested several flower/network extensions, and then hostile-audited the separate phase-zero path route. During the run, main advanced independently to a stronger high-`t` rectangle/cusp stack through `t<=1.8687`. Accordingly, this document is not a new frontier theorem. Its purpose is to preserve which candidate arguments survived, which were quantitatively dominated, and which local obstruction remained after audit.

## 1. The phase-zero path route through `t<=1.865` survives audit

The unmerged branch

`origin/research/c2-dominant-oo-t1865-sol-20260915`

contains a logically separate replacement for the retracted low-energy path arguments. The relevant chain is:

- `00ed89cf`: exact retained dominant O--O pair-weight certificate through `t<=1.865`;
- `0fe0ac11`: theorem statement for the retained pair-weight extension;
- `f2f7279d`: hostile audit of the retained pair-weight extension;
- `ba3910b0`: post-retraction audit of the two-shore phase-zero argument;
- `3c2e917d`: repaired frontier statement after the old low-energy path retractions;
- `5c063a67`: hostile audit of the full `t<=1.865` path/hub/interface composition.

The exact verifier was rerun during this audit. It gives

\[
P_{OO}^{dom}/D>0.0027-o(1)
\]

at `T=1.865`, with the exact rounded computation producing the stronger numerical margin

\[
P_{OO}^{dom}/D>0.0027121826889\ldots-o(1).
\]

Pigeonholing among at most three dominant projective phase classes therefore leaves a single shrinking phase window with retained pair weight

\[
>0.0009D-o(D).
\]

The separate phase-zero argument survives the September 15 path retractions because it does not infer oriented terminal branches from projective endpoint energy. Instead it applies the two-sided Section-157 bracing statement separately to the two Jordan shores of each O--O train. After deleting only `o(D)` pair weight near the two limiting antipodal phase-zero markers, every surviving crosscut separates the same two fixed boundary markers. Pairwise noncrossing then makes the crosscuts totally nested, so the complement dual is a path.

The corresponding exact interface verifier was also rerun. It yields one nonhub strip with either

\[
N_i\le 6981
\]

when optimizing switching count alone, or simultaneously

\[
N_i,L_i\le12694,
\qquad
B_i<{12695\over D}+o(D^{-1}).
\]

Thus the phase-zero path/hub/one-sided-interface theorem through `t<=1.865` is a valid independent structural result. It is no longer the repository frontier because main now contains a stronger route through `1.8687`.

## 2. The naive full-flower complement-capacity splice is dominated

For a set of fully rhombic pentagons, let `M_flower` denote the number of distinct complement trains terminating on those flowers, `P_c` the complement O--O population, and `N_c` the total complement-train population. Because an O--O train has both terminals outer while a flower-terminal train has a bounded terminal, these two train populations are disjoint. This gives the exact elementary bound

\[
P_{all}\ge M_{flower}+P_c-N_c.
\]

Combined with the existing flower allocation and complement O--O inequalities, this does force a through-splice lower bound. However, at the live endpoint near `t=1.86177`, the resulting normalized `K` floor is only about `1.3535`. The already audited general pentagon through-splice theorem forces approximately

\[
K\gtrsim1.7110.
\]

Therefore the new composition is quantitatively dominated. It should not be promoted as a separate theorem unless coupled to additional information that changes the objective, such as localized crossing deficit, phase allocation, or diameter blocking.

## 3. Full-flower escape/flex and two-blocker theorems are useful reductions, not closure

The separate flower branch contains two sound structural results:

1. full flowers satisfy an escape-or-flex alternative in train-rate coordinates;
2. every external strict-rhombus train is noncrossing with at least two of the five flower-terminal trains.

The first gives, for a flower set of size `F`, the exact train-network estimate

\[
E_{esc}\ge F/2
\quad\text{or}\quad
\dim\mathcal V_{flower}\ge F/4-1.
\]

The second localizes crossing loss: an external train crosses at most three members of one five-train flower fan.

Neither result closes the branch by rank or scalar counting alone. The flex dimension is only linear in `D`, so mixed-rigidity injectivity is compatible with a linear actual diameter family. The two-blocker theorem concerns train noncrossings, not diameter edges, so it does not supply a bounded-reuse diameter-incidence contradiction.

The potentially useful composition is therefore dominant-vs-complement allocation of flower-terminal occurrences, not another scalar Mantel or complement-capacity bound.

## 4. A simple one-sided transverse-sign contradiction does not work

After the phase-zero path and common-hub reduction, every nonhub strip has one-sided switching in the path sense: all switching diameter intervals point toward the hub. It is tempting to infer that all switching diameter vectors then have one transverse sign and contradict the two-sign bracing theorem. That inference is false.

One-sided path topology fixes which side of the path interval contains the exterior endpoint. It does not force all middle endpoints onto one of the two physical outer boundary arcs of the middle region. A one-sided strip can therefore still support both transverse signs. Any closure argument must use more than interval orientation alone.

## 5. Residual local blocker after the phase-zero reduction

The phase-zero marker geometry eliminates the non-antipodal TB2 regression: for adjacent selected trains with nonzero phase gap, a minimal two-bar tangent obstruction would force both endpoints of each blocker into shrinking marker neighborhoods, while a switching blocker must have one endpoint in the marker-free middle region. Hence the surviving local alternative is

\[
\text{TB1}
\quad\text{or exact parallelism of the adjacent train directions.}
\]

Exact parallelism is not excluded merely by the common-hub one-sided order. This is the correct residual obstruction on the older `t<=1.865` phase-zero path.

## 6. Current disposition after main advanced

While this audit was in progress, `origin/main` advanced to a stronger stack including

- a finite-defect KKT strip through `t<=1.8687`;
- a high-`t` complete rectangle through `t<=1.8687`;
- phase collapse of that rectangle; and
- an embedded finite cusp (`c5f6f966`).

That route supersedes the `1.865` phase-zero path as the live quantitative frontier. The correct next work should therefore attack the finite cusp/rectangle obstruction on current main, using the phase-zero audit only as an independent cross-check or as a source of local geometric lemmas.

**Disposition:** no C-II closure was obtained in this run. The phase-zero path through `1.865` was independently validated; the naive flower complement-capacity splice was rejected as dominated; rank-only flower closure and the one-sided transverse-sign shortcut were rejected; and the remaining older-path blocker was isolated as TB1/exact-parallel strip geometry. Current main has already moved to the stronger `1.8687` rectangle/cusp normal form.
