> Generated reading edition · [exact source](../../research/target_c_support6_h5_terminal_rotation_genus_2026-09-18.md) · source SHA-256 `cbb3c5ab4d7cb6b3d582c58e0e0abd69abe2681e0a3f5d2a3b5a9f409784e26a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "2224e9004b84645b66d2af92df534bc2f27df805", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_h5_terminal_rotation_genus_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8891e5a3c14cf1357c854ee479b0c33555a3a4580829d6063de266ebbdaa22f0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every noncollapsed support-six H5 terminal rotation is nonplanar

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** the 48 uniform and 80 simple-wall labelled survivors of the noncollapsed support-six reciprocal H5 reduction  
**Depends on:** `target_c_support6_reciprocal_h5_reduction_2026-09-18.md`; the double-wall exclusion; the regular five-force tournament test  
**Certificate:** `research/verify_target_c_support6_terminal_rotation_genus_2026_09_18.py`  
**Classification:** conditional global-embedding obstruction, not a metric realization or C-II closure

The finite H5 reduction leaves 48 labelled uniform survivors and 80 labelled simple-wall survivors. For each survivor, take the cyclic order of the five force sides at each of the six non-ground reciprocal vertices. Pair the two occurrences of each of the twelve non-ground relation sides with opposite boundary orientation, and leave the six ground-anchor sides unpaired.

The resulting exact orientable rotation surface is never planar:

$$
\boxed{g\in\{2,3\}\quad\text{for every one of the 128 labelled H5 survivors}.}
$$

The computation uses only integer chirotope signs, integer edge signs, permutation enumeration of the regular 5-tournament, and a disjoint-set calculation of vertex classes. No coordinates, floating-point tolerances, or metric root assumptions enter.

## 1. Terminal rotation construction

At a non-ground reciprocal vertex `i`, the regular-force-tournament condition already certified in the H5 reduction determines a cyclic order of the five incident force sides. Label the corresponding terminal pentagon sides by the neighbors `j`, with `j=0` denoting the outside/anchor side. If the occurrence of side `{i,j}` at face `i` starts at corner slot `k`, the occurrence at face `j` has the opposite vector and is glued by

$$
(i,k)\sim(j,m+1),\qquad (i,k+1)\sim(j,m),
$$

where `m` is the slot of `i` in face `j`. This is the orientation-preserving translation pairing forced by opposite force vectors.

There are six pentagonal cells, twelve paired relation-side classes, and six boundary anchor sides. The certificate computes the number `V` of corner classes, the number `b` of boundary components, and

$$
\chi=V-18+6=V-12,
\qquad
g={2-b-\chi\over2}.
$$

The surface is connected because the non-ground relation graph is `K_6` minus a perfect matching, hence connected.

## 2. Exact finite output

The certificate returns the following distributions, indexed by `(V,b,g)`:

$$
\begin{array}{c|rrrr}
& (6,2,3)&(7,1,3)&(7,3,2)&(8,2,2)\\ \hline
\text{uniform}&26&12&6&4\\
\text{simple wall}&62&10&4&0
\end{array}
$$

Thus every noncollapsed H5 sign/order survivor has terminal rotation genus at least two. The previously excluded higher-codimension ground-collinearity strata do not add cases.

As a finite sensitivity check, the certificate also leaves a selected subset of relation-side pairs unglued and recomputes the surface. Reaching genus zero requires at least three such pairs in every case. The exact minimum-cut distributions are

$$
\begin{array}{c|cc}
&3&4\\ \hline
\text{uniform}&30&18\\
\text{simple wall}&44&36
\end{array}
$$

This is a statement about the terminal rotation model: it does not identify an unglued pair with a particular canonical train corridor, and therefore is not itself a linear global train lower bound.

## 3. Conditional planar consequence

If the twelve residual trains were literally the twelve shared sides of these six physical bounded faces, with no intervening train corridor, additional face, or overlap, their union would be a compact connected orientable planar surface with boundary. Every compact connected subsurface of the plane has genus zero, contradicting the certified `g>=2` rotation calculation.

Therefore any actual canonical realization of a noncollapsed H5 block must use genuinely nontrivial global structure absent from the direct-side model: a complete stopped train must pass through intervening structure, terminal sides must not be directly paired as assumed, or the local cells must fail to form an embedded disjoint planar subcomplex. In the simpler model where global routing only breaks direct side pairings, at least three relation pairs must be broken. This is the exact global condition left by the finite rotation audit.

This conditional implication is the useful frontier reduction. It does **not** assert that canonical stopped trains are direct shared face sides; the repository's train construction may include corridors. It also does not exclude metric reciprocal equilibria, because the rotation calculation ignores lengths and only uses necessary sign/order data.

## 4. Dependency chain and limits

$$
\text{H5 sign/order survivor}
\to
\text{terminal rotation genus }g\ge2
\to
\text{no direct-side planar embedding}
\to
\text{any global realization needs corridor/extra-structure compatibility}.
$$

The last arrow is not yet a contradiction with C-II. The next finite global task is to show that the required corridor/extra-structure routing is incompatible with the planar contact-face incidence and train-boundary currency, or to lift one of the 128 cases to the full metric equations and rule it out. The collapsed support-six branch is separate and locally realizable under the certified conditions in its regression note.

No theorem-state file is changed.

**Disposition:** proved a complete exact terminal-rotation obstruction for the direct-side model of every noncollapsed H5 sign/order survivor; classified the surviving global escape as nontrivial corridor/embedding structure. C-II remains open.
