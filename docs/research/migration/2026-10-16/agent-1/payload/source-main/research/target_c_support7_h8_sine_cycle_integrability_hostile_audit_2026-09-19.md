# Hostile audit — support-seven `H8` sine-cycle integrability

**Date:** 2026-09-19  
**Audited source:** `target_c_support7_h8_sine_cycle_integrability_2026-09-19.md`  
**Verdict:** passes as a necessary-and-radial-sufficiency reduction; it is not a support-seven exclusion.

## 1. Law-of-sines orientation

For triangle `0ij`, `rho_j=|0j|` is opposite the angle at `i`, namely `A_ij=angle 0ij`, while `rho_i=|0i|` is opposite `A_ji=angle 0ji`. Therefore

\[
\rho_j/\rho_i=\sin A_{ij}/\sin A_{ji}
\]

has the correct orientation. Reversing the directed edge negates the logarithmic cochain.

## 2. No zero-sine division in `H8`

The claim is restricted to the fully convex eight-point branch. No three hull vertices are collinear, so each ground triangle `0ij` used here is nondegenerate and its two non-ground angles lie in `(0,pi)`. Their sines are strictly positive. The logarithms and ratios are therefore defined.

## 3. Relation graph, not the whole reciprocal graph

Only relation edges among vertices `1,...,7` are used. Each such edge has both ground edges `0i` and `0j` present because all missing edges lie in `L` among the non-ground vertices. Thus every required triangle `0ij` exists.

The relation graph has fourteen edges and seven vertices. For both allowed complement types it is connected, so its cycle rank is eight. The exact certificate verifies a fundamental-cycle matrix of rank eight over `Q` for canonical representatives.

## 4. Converse is intentionally limited

Vanishing cycle sums makes the edge log-ratio cochain exact. This is sufficient to assign positive radial lengths `rho_i`, unique up to common scale, that realize all edge ratios (1.1). It does not by itself prove that the resulting points realize every prescribed reciprocal angle, signed equilibrium, pentagon closure condition, or convex order. The source explicitly limits the converse to radial-ratio compatibility.

## 5. Independence statement

The eight fundamental cycles are independent in the graph cycle space. This does not imply that the eight nonlinear sine equations are functionally independent as equations in the force-gap variables. No such Jacobian-rank claim is made.

## 6. Scope against the current endpoint

The reduction supplies a concrete nonlinear target for the twelve remaining convex `H8` reflection orbits. It does not touch `H6/H7`, where ground triangles may encounter different order-type and degeneracy issues, and it does not improve the global support coefficient on its own.

**Disposition:** the sine-cycle identities and the count of eight fundamental consistency conditions are correct. Future work may use them for an interval or analytic exclusion, but this note alone leaves C-II open.
