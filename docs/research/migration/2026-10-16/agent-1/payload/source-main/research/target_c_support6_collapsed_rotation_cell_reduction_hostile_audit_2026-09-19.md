# Hostile audit — collapsed support-six exact rotation-cell reduction

**Date:** 2026-09-19  
**Audited note:** `research/target_c_support6_collapsed_rotation_cell_reduction_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support6_collapsed_rotation_cells_2026_09_19.cpp`  
**Disposition:** PASS at audited-working scope; theorem-state authority unchanged; C-II remains open.

## 1. Scope and dependency check

The note does not claim to exclude the collapsed support-six branch. It classifies the angle/order data forced by the already established local pentagon inequalities and derives a universal crossing requirement for any global realization.

The only recent ingredient that needs scope attention is the adjacent-turn lower bound

\[
\delta_i+\delta_{i+1}>2\pi/3.
\]

Although the source note used it downstream in a noncollapsed H5 branch, its proof is a standalone lemma for any strict convex equilateral pentagon satisfying the one-turn bound `delta_i<2pi/3`. The collapsed degree-pure faces satisfy exactly those hypotheses. Reusing the local lemma here does not import any noncollapsed reciprocal assumption.

## 2. The `2+2` orientation claim is exact

Normalize the anchor side to `+e_1` and choose each train's projective representative in the open upper half-plane. All four relation occurrences cannot have one sign because their vertical components would have one strict sign and could not close with the horizontal anchor.

For a `1+3` split, the first two physical turns sum to `pi+beta_1>pi`. For a `3+1` split, the final two turns sum to `2pi-alpha_3>pi`. Both contradict the strict two-turn upper theorem. Therefore every face has two `+` and two `-` relation occurrences.

The two occurrences of one complete internal train are negatives, so the `+` endpoint and `-` endpoint define a coherent orientation. Every relation vertex is therefore exactly `2`-out/`2`-in. No generic-position assumption is used.

## 3. The minus-anchor convention was checked

For a positive anchor, the `+` occurrences occupy the first half-plane after the anchor, so `A=out` and `B=in`.

For a negative anchor, rotate the face by `pi` to put the anchor on `+e_1`. This flips every relation occurrence sign. Consequently the first half-plane contains the original incoming occurrences, so `A=in` and `B=out`.

With that convention the physical side order in both cases is

\[
0,\alpha_{A_1},\alpha_{A_2},\pi+\alpha_{B_1},\pi+\alpha_{B_2}.
\]

The five scaled gap formulas in the note follow directly. This sign convention is the main place where an apparently harmless swap would corrupt the census; the verifier implements the same convention explicitly.

## 4. The strict-difference test is genuinely exact

After scaling by `3/pi`, every one-turn and adjacent-two-turn inequality has integer constants. There are 12 train-angle variables and one constant node. Strict difference feasibility fails exactly when a directed cycle has total integer weight at most zero.

A simple cycle has at most 13 edges. Under the replacement `c -> 14c-1`, a cycle of length `k<=13` and total integer weight `C` becomes `14C-k`, which is negative iff `C<=0`. Thus integer Bellman--Ford on the transformed system decides the strict system without floating point, epsilon tolerances, or rational approximation to `pi`.

The local compiler/runtime reproduction returned:

```text
all-cross matching: cells=180, orbits=15, genus g1=36 g2=60 g3=84, orientation-cell-counts 2x24 6x6 12x8
mixed matching: cells=208, orbits=27, genus g1=32 g2=72 g3=104, orientation-cell-counts 4x4 5x24 7x8 8x2
PASS: exact collapsed support-six angle-order census = 388 cells, 42 conservative symmetry orbits, no planar rotation cell.
```

## 5. The matching classification is complete

With three positive-anchor and three negative-anchor vertices, a perfect matching has either three cross-sign edges or one cross-sign edge. Zero or two cross-sign edges would leave an odd number of unmatched vertices in one sign class. The two canonical matchings in the certificate therefore cover every labelled matching up to sign-preserving relabeling.

The certificate separately enumerates all `2^12` orientations and retains exactly the `2`-in/`2`-out ones. It does not assume the 38-orientation count; that count emerges from the enumeration for each matching type.

## 6. The symmetry quotient is conservative

Only sign-preserving automorphisms of the canonical matching and reflection across the anchor line are identified. Reflection reverses projective order and flips the `+/-` representative sign, hence reverses every edge orientation and sends `(A1,A2,B1,B2)` to `(B2,B1,A2,A1)`.

Potential additional equivalences involving a global anchor-sign swap are deliberately not used. Therefore `42` is a valid upper bound on the number of symmetry representatives needed for the next search even if a larger symmetry group could reduce it further.

## 7. Ribbon genus implies a real crossing lower bound

The cyclic order used in the ribbon graph is the actual order of the four relation-train endpoints around each exceptional-face disk after deleting the anchor endpoint. If the twelve train arcs had no mutual crossings, they would give a planar embedding with exactly that rotation system, forcing genus zero. The certificate finds no such cell.

For the quantitative statement, resolve each transverse train crossing by a handle. With `X_K` crossings this embeds the same rotation system in an orientable surface of genus at most `X_K`. Hence its intrinsic ribbon genus satisfies `g_K<=X_K`.

This does not say that every topologically sufficient set of crossings is geometrically realizable. The strict-rhombus angle condition can forbid candidate crossings; that is exactly how the already committed Jordan obstruction kills the certified root box.

## 8. Non-implications

The census does not solve the nonlinear six-face closure equations inside every one of the 388 open cells. Some difference cells may contain no exact vector-closure solution.

It also does not prove that a cell with enough angle-compatible train pairs has a global stopped-train embedding. Crossing compatibility is necessary, not sufficient.

No support-seven corank coefficient is promoted from this result, and no theorem-state file should change.

**Audit disposition:** PASS. The new durable research statement is that every collapsed degree-pure support-six solution lies in one of 388 exact rational local angle/order cells, 42 under a conservative symmetry quotient, and every such cell has positive relation-rotation genus. Any global realization therefore needs internal relation-train crossings. The remaining attack is the exact crossing-threshold subdivision plus Jordan/vector-closure exclusion.
