# Target C-II: B-hull clause capacity across the O--O dual-tree hub

Date: 2026-10-06.
Authority: main 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1, state 2026-10-05.audit.62.
Status: proof-only Target C reduction. C-II and Level I remain open.

Use the audit.61 narrow-window O--O system and its pairwise-disjoint proper crosscuts. Let Dtree be the complement-dual tree.

For each actual diameter pair h, let P_h be the unique path between its endpoint regions. Any two such paths intersect. Shared source endpoints are immediate. For two disjoint diameter pairs, canonical planar diameter geometry gives alternating cyclic endpoint order on the convex boundary. If the two tree paths were disjoint, a dual edge on their connector would separate the two endpoints of one pair from the two endpoints of the other; the corresponding proper crosscut separates the outer boundary into two intervals, which is incompatible with alternating order.

Tree Helly therefore gives one region R_* on every actual-diameter support path. Root Dtree at R_*. No component C of Dtree-R_* can contain both endpoint regions of an actual diameter pair.

Now let B be the canonical actual-diameter endpoint set. For one component C, its unique edge to R_* is a proper crosscut. The C-shore occupies one cyclic outer-boundary interval. Actual diameter endpoints are extreme source vertices, so B_C={b in B: region(b) in C} is a cyclic interval in the B-hull order. A cyclic interval of a cycle has at most two cycle edges leaving it.

A surviving audit.61 B--B near-unit clause that reaches the unit boundary has old length at most 1+s, with s < 1/(D+sqrt(D^2-1)). For D>=7 this is below 13/12. Canonical C-LOADED-NEAR-UNIT-ADJACENCY therefore makes every such physical pair a B-hull side. Consequently every hub component C satisfies

    number of B--B near-unit clause pairs with exactly one endpoint in C <= 2.

This is a physical source-pair theorem; it does not identify owners with regions. If d_* is the degree of R_*, summing branch incidences gives the safe global estimate that at most 2 d_* distinct B--B clause pairs join different hub pieces.

Thus each nonhub branch has no internal actual diameter pair and at most two physical B--B near-unit clauses leaving it. A large owner-level contradiction must therefore use owner recurrence across hub branches, non-B endpoint clauses, or remain mostly internal to branches. The next Target C step is to pay cross-branch owner recurrence using audit.53 return/depletion or outer-occurrence currency.

The abstract diameter-path Helly observation has September proof-only prior art; the new step here is its composition with audit.62 B-hull adjacency. The separate fourteen-edge bandwidth estimate on this worker branch is not used. Unary rhombus tests, at-most-d_H inactive upper exceptions, and the macroscopic inactive-container branch remain separate.

All statements above are analytic finite arguments. No computation or verifier output is a proof premise.