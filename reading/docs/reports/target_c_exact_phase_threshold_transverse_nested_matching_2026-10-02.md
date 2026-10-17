> Generated reading edition · [exact source](../../../docs/reports/target_c_exact_phase_threshold_transverse_nested_matching_2026-10-02.md) · source SHA-256 `c038220804e831fe26cf7f5a2660356759ad0193c675fde6b591a8f94ba19def`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-EB26D7005982","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- threshold staircase yields a nested transverse matching

Date: 2026-10-02
Base main: fbeae9b3fa18a63e07573676b4e2e512a91ca4d5
Status: proof-only; C-II remains open.

Dependencies:
- docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md
- docs/reports/target_c_exact_phase_threshold_forest_lift_2026-10-01.md
- docs/reports/target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md
- docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md
- docs/reports/target_c_full_source_circumradius_response_2026-09-10.md

## Theorem

Use the threshold exact-phase notation on current main. Let T be the paired-staircase
tree on A-layers 0,...,m and let F be the selected physical diameter forest consisting
of the two representatives over each tree edge together with the parallel full-support
diameter. Every staircase interval contains the common A-train tau_r.

Then F contains a matching M of actual diameter edges with

    |M| >= (c_*/(24*3^(1/8)) - o(1)) D^(1/4),

such that every member crosses tau_r and all members are pairwise properly crossing.
Moreover one of the following holds.

FULL: every member of M has full support on the opposite retained B-shore.

NESTED: there is one extreme A-layer j_* in {0,m}, one fixed adjacent B-host subarc,
one fixed A-host interval, and one terminal side of the B-shore such that every member
of M joins that B-host subarc to that A-host, has its other endpoint in a distinct
internal A-layer, and has B-support a terminal prefix or suffix. In internal-layer
order, the terminal B-support indices are monotone, so these supports form a chain
under inclusion.

Thus the boundary-heavy alternative from the preceding report can be upgraded from
many carriers in one extreme A-layer to an ordered vertex-disjoint two-shore diameter
ladder.

## Proof

The forest-lift theorem gives F as a forest contained in the actual diameter graph H.
A forest of maximum degree Delta has an edge-coloring with Delta colors: remove a leaf
edge, color inductively, then use at its nonleaf endpoint a color unused by the at most
Delta-1 remaining incident edges. Hence every E-edge subforest of F has a matching of
size at least E/Delta(H).

The full-source shared-endpoint estimate gives

    Delta(H) <= (4*3^(1/8)+o(1)) D^(3/4),

and the retained threshold shore has

    m >= (c_*-o(1))D.

First suppose the number e_int of T-edges with both endpoints internal satisfies
e_int >= m/2. The transverse-rail theorem gives 2 e_int >= m selected diameter edges
with full B-support. They form a subforest, so they contain a matching of size at
least

    m/Delta(H)
      = (c_*/(4*3^(1/8))-o(1)) D^(1/4).

This is FULL. Every edge also crosses tau_r because every staircase interval contains r.

Now suppose e_int < m/2. As in the preceding report, one extreme tree vertex
j_* in {0,m} has degree greater than m/4. Delete the possible edge {0,m}; there remain

    d' > m/4 - O(1)

edges {j_*,b} with b internal, and therefore 2d' selected physical representatives.

Use the four host intervals I_A^+, I_B^+, I_A^-, I_B^- in cyclic order. On the two
A-hosts the B-layer coordinate is constant at 0 and n. For j_*=0, the two
representatives over {0,b} are L_0 U_b and L_b U_0. The internal endpoint U_b is on
the U-side A-host and has B-layer n; L_b is on the L-side A-host and has B-layer 0.
The extreme endpoint L_0 or U_0 lies either at the adjacent end of an A-host, producing
full B-support, or on the adjacent level-zero part of a B-host, producing a terminal
B-interval. The same statement, with orientation reversed, holds for j_*=m.

Thus these 2d' edges have only three B-support types:

    full, 0-terminal, n-terminal.

One type has at least 2d'/3 > m/6-O(1) edges. Its subforest therefore has a matching M
with

    |M| >= (m/6-O(1))/Delta(H)
         = (c_*/(24*3^(1/8))-o(1)) D^(1/4).

If the winning type is full, this is FULL.

Otherwise fix the winning terminal type. A fixed boundary tree edge contributes at
most one representative to a specified non-full terminal type, because its two
orientations use opposite internal A-hosts. Hence the members of M come from distinct
tree edges {j_*,b} and have distinct internal labels b.

All internal endpoints now lie on one A-host interval, while all extreme-layer
endpoints lie on one fixed adjacent B-host subarc. Along the A-host, the A-layer
coordinate is monotone; along that B-host subarc, the B-layer coordinate is monotone.
Order the matched edges by increasing internal A-layer. They are vertex-disjoint actual
diameters and therefore pairwise properly crossing. For chords joining two fixed
disjoint boundary intervals of a convex polygon, pairwise proper crossing forces the
opposite endpoint order on the second interval. Hence their B-layer endpoint indices
are weakly monotone. Since all supports are prefixes, or all are suffixes, the B
supports form a nested chain. This is NESTED.

All members still lie over staircase tree edges, so all cross tau_r.

## Remaining bottleneck

The threshold exact-phase branch is reduced further to an ordered two-shore object:

    Omega(D^(1/4)) pairwise-crossing actual diameters
    with one common A-cut,
    and either full B-support or nested terminal B-support.

The next target is to combine this matching/ladder with the exact B-shore KKT
equations, the complete strict-rhombus grid, or a finite contact-preserving motion.
No C-II closure is claimed.

No computation, numerical evidence, verifier execution, CI result, or unexecuted
verifier code is used.

## Slot 2 recovery provenance — 2026-10-05

Source branch: `research/threshold-transverse-nested-matching-r2-2026-10-02` at exact tip `344666a3f89543c18cecd90153e54522579bca0c`. No original PR was associated with this branch. This report is preserved as an unreviewed, proof-only Target C-II candidate; it does not change the current theorem state. No standalone verifier or computational certificate was present on the source branch.
