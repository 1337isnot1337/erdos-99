<!-- theorem-state: {"artifact_id":"ART-6B8F96362F37","canonical":true,"claim_ids":["C-PSEUDO-GRID"],"claim_statuses":{"C-PSEUDO-GRID":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Section 73 pseudosegment-grid promotion audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## Scope audited

This audit covers Section 73 only in the quadratic positive-core branch after canonical Section 69. It proves complete-grid extraction inside one physical coherent grain even when that grain has holes. It does not promote any pure-disk common-order, crosscut, penetration, or additive-Cartesian conclusion.

## External theorem check

The external input was checked directly in Fox--Pach--Suk, *A structure theorem for pseudo-segments and its applications*, arXiv:2312.01028.

Their definition of a collection of pseudosegments requires that any two curves have at most one point in common and that no three curves have a common point. Their Theorem 2.12, attributed there to Fox--Pach, states that there is an absolute constant `c_PS>0` such that `N` pseudosegments with at least `eta N^2` crossing pairs contain two subcollections `C_1,C_2`, each of size at least `c_PS eta N`, with every curve of `C_1` crossing every curve of `C_2`.

The theorem uses crossing pairs, not arbitrary intersections, and the shore bound is linear in `eta N`; no logarithmic loss occurs.

## Internal dependency audit

1. Canonical Theorem 10.6 in `docs/theory/01-local-structure.md` applies to an arbitrary finite edge-to-edge strict-rhombus complex, including one with holes. Every local train centerline is a simple arc, every two centerlines cross at most once, no train closes, and every rhombus is one train-pair crossing. Its train-crossing graph is triangle-free.
2. Therefore a Section-69 physical grain with `R` retained rhombi and `T` local train segments gives exactly `R` crossing pairs among `T` pseudosegments.
3. Fox--Pach with `eta=R/T^2` yields all-crossing shores `C_1,C_2` with
   \[
   |C_1|,|C_2|\ge c_{PS}R/T.
   \]
4. The triangle-free train-crossing graph automatically makes each shore internally pairwise noncrossing: a crossing inside one shore plus any curve in the opposite shore would form a crossing triangle.
5. Section 69 gives `2T=P`. On the quadratic branch it supplies one grain with `R>=rD^2` and `P<=CD`, so `T<=CD/2` and hence
   \[
   |C_1|,|C_2|\ge(2c_{PS}r/C)D.
   \]
6. The phase purification is valid once the Section-69 bin shift is endpoint-safe. All train vertices of one physical grain lie in one retained train component and therefore one phase bin of width `epsilon<pi/6`. Same-label train directions differ by at most `epsilon`, while a strict unit-rhombus crossing has projective separation `>pi/3`; same-label trains cannot cross.
7. Choosing the largest label class in `C_1` loses at most a factor three. That label is forbidden in `C_2`; choosing the larger of the remaining two labels loses at most a factor two. Therefore the phase-pure shores satisfy the safe symmetric bound
   \[
   |A|,|B|\ge(c_{PS}/3)R/T=Omega(D).
   \]
8. Holes never enter the pseudosegment-density step. They remain relevant only to the next common-order/penetration theorem.

## Section-69 endpoint convention repair

The current Section-69 coarea proof says to delete an edge when a bin boundary lies strictly between its endpoint potentials. If a train potential lies exactly on a bin boundary, one boundary vertex could otherwise retain edges into both adjacent bins, so the later statement that a connected retained component lies in one bin is convention-dependent.

The repair is exact and measure-zero: exclude the finite set of shifts for which any train potential lies on a bin boundary, use half-open bins for every remaining shift, and delete precisely the edges whose endpoints lie in different bins. Removing finitely many shifts does not change the coarea integral or any bound in (69.6)--(69.9). One can choose a nonexceptional shift attaining the average or better.

No constant or downstream theorem changes.

## Promotable conclusion

Under the Section-69 quadratic-grain hypotheses, Section 73 canonically gives:

- a complete topological train grid with two internally noncrossing shores of size at least `c_PS R/T`;
- after the audit.28 phase-support sharpening, a complete distinct-phase grid with shores at least `(c_PS/2)R/T`;
- hence, whenever `R>=rD^2` and `P=2T<=CD`, both shore sizes are `Omega(D)`.

The sharpened factor `1/2` uses no new external input: the two all-crossing Fox--Pach shores have disjoint nonempty phase-label supports in `Z/3`, so each support has size at most two and its largest phase class contains at least half the shore.

The next quadratic-core obligation is not grid extraction. It is a boundary-budget penetration/common-order theorem, or a direct diameter contradiction from the complete holed grid. Section 73 does not assert the additive array hypothesis of Theorem 10.9.
