> Generated reading edition · [exact source](../../../docs/reports/target_c_fixed_star_bounded_switch_cusps_2026-10-01.md) · source SHA-256 `5fd2f8e919c915cf4deb745741c9622bcd96c60ab5cecedffe56d0e425935d15`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0A13823D9C8E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- bounded switching cusps inside the fixed-star complete grid

Date: 2026-10-01
Base main: 91be6776e6748b0f449ccfff69bca1e352d1b75d
Status: proof-only; C-II remains open.

## Theorem

In the current fixed-star endpoint branch, after the local witness-cell extraction, let A'={tau_1,...,tau_m} and B'={sigma_1,...,sigma_n} be the complete global O--O rectangle. Current main gives m,n >= (c_*-o(1))D, where c_* = kappa^4/(16 pi^3 C_K M_K), C_K=floor(4K)+2 and M_K=2 floor(4K)+3.

For adjacent selected A'-cuts define N_i^A as the number of actual diameter rows whose signed incidence changes between tau_i and tau_{i+1}. Put H_0 = ceil(8 pi/c_*)+1. Then

  #{i : 1 <= N_i^A <= H_0} >= (c_*/4-o(1))D.

The same holds on the B' shore. Each such switching graph is a caterpillar forest with at most H_0 edges. If both switch orientations occur, all middle endpoints lie on one middle outer-boundary arc in the audited right-prefix / optional-hub / left-suffix order.

Moreover at least (c_*/(4(H_0+3))-o(1))D of these A'-interfaces can be chosen so that their adjacent train pairs are pairwise disjoint and their switching-diameter edge sets are pairwise disjoint. The symmetric statement holds for B'. Every retained cusp still has the same two fixed full-span opposite-sign witness diameter edges on its shore and is crossed by every train of the opposite linear shore.

## Proof

Exact laminar interval support restricted to A' says that the signed incidence sequence of every actual diameter row is zeros, then one constant nonzero sign on a contiguous interval, then zeros. Thus one row can switch at at most two adjacent selected positions, and

  sum_i N_i^A <= 2h.

At the exact rooted endpoint current main gives h = pi D + o(D), so sum_i N_i^A <= (2 pi+o(1))D.

The current complete-grid rank theorem gives s_A := #{i:N_i^A>0} >= ceil(m/2)-1 >= (c_*/2-o(1))D. The number of active interfaces with N_i^A > H_0 is at most (2 pi/H_0+o(1))D < (c_*/4+o(1))D. Subtracting proves the first bound. The proof on B' is identical.

Fix one retained interface and keep only its two proper O--O crosscuts. Their complement has coarse regions L,M,R. Exact interval support says every switching diameter has exactly one endpoint in M: a left switch joins L to M and a right switch joins M to R. Hence the switching graph is bipartite. Since the actual diameter graph is a straight-line convex thrackle, this bipartite subgraph is a forest. The audited adjacent-switching theorem gives the caterpillar and one-arc prefix/suffix refinement. Unselected train crosscuts inside the coarse regions do not affect the argument.

The fixed witness pair for the A' shore crosses every selected A' cut, so its incidence is nonzero and constant on all selected coordinates. Hence neither fixed witness edge belongs to any switching set.

For the disjoint-packet extraction, form a conflict graph on retained interfaces. An interface conflicts with at most two neighbors through a shared train. It contains at most H_0 switching diameter edges, and each such edge can switch at at most one other selected interface. Thus the conflict degree is at most H_0+2. A greedy independent set retains at least a 1/(H_0+3) fraction.

Finally, the complete product A' x B' is untouched. Every retained A'-cusp is crossed by all n >= (c_*-o(1))D trains of B', with the same strict-rhombus common order and the Section-90 inverse-phase bound pi/3+O(1/D). The argument is symmetric on B'.

## Remaining target

The fixed-star branch now contains linearly many pairwise separated finite packets of the form

  two adjacent same-shore O--O cuts
  + two fixed full-span witness rows
  + O_{K,kappa}(1) ordered switching rows
  + Theta(D) common transverse O--O trains.

The next useful step is a local incompatibility theorem for this bounded ordered cusp against the common transverse grid. The split-star and inactive-interface branches remain open.

No computation, verifier, numerical evidence, or CI result is used.
