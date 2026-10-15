<!-- theorem-state: {"artifact_id":"ART-EF73D8616731","canonical":true,"claim_ids":["C-ROOTED-CROSSCUT-MARKED-INTERVAL-CAPACITY"],"claim_statuses":{"C-ROOTED-CROSSCUT-MARKED-INTERVAL-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: rooted crosscut branch interval capacity

**Date:** 2026-10-08  
**Audit base:** `origin/main=b1b0a9a05f787a675973c36c6120530777c9040c`, state `2026-10-08.audit.149`  
**Frozen source:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`  
**Source artifact:** `research/target_c_dual_tree_hub_boundary_capacity_2026-10-06.md`, SHA-256 `ff447fbe9ddfdc7e0c559da44951951efea029e5933f90c1cde96e4e21fcd519`  
**Related source report:** `docs/reports/target_c_hub_owner_terminal_capacity_audit_2026-10-06.md`, SHA-256 `61e16a888f99858fc6af890c05f4ac1ba27efd0394ea6e65434b29412dbf3468`

## Verdict

**PASS WITH NARROWED SCOPE — promote `C-ROOTED-CROSSCUT-MARKED-INTERVAL-CAPACITY`.** In a disk cut by pairwise disjoint proper crosscuts, fix a root region and assign each marked boundary point to one incident region. The marks assigned to any component after deleting the root form a cyclic interval, so at most two consecutive marked-cycle pairs cross that component.

The research note's stronger inference that no nonhub branch contains both endpoints of an actual diameter pair is **not valid** when a loaded mark is a crosscut endpoint. Audit.138 already records the exact endpoint regression. The interval-capacity theorem below does not use that inference. The source-level identification of every lower clause with a single assigned boundary region remains conditional on that assignment being the one used by the motion model.

No route-map obligation is removed. C-II and Level I remain open.

## Exact audited statement

Let `X` be a closed topological disk cut by a finite family of pairwise disjoint proper crosscuts, and let `T` be its dual region tree. Let `B` be a finite cyclically ordered set of distinct marked points on the boundary of `X`. Assign each mark `b` to exactly one region whose closure contains `b`; this permits a mark at a crosscut endpoint, with either incident region chosen. Fix a root region `r` in `T`. For each component `C` of `T-r`, put

`B_C = {b in B : the assigned region of b lies in C}`.

Then `B_C` is empty, all of `B`, or a consecutive cyclic interval in the order on `B`. Consequently, at most two cycle edges of `B` have exactly one endpoint in `B_C`. The same bound holds for any selected family of such cycle edges, including any family of lower-clause pairs already known to be consecutive in `B`.

## Independent proof

The component `C` is attached to `r` by one dual-tree edge, corresponding to one crosscut `gamma`. The crosscut separates the disk into two sides and divides its boundary into two arcs. The union of the regions indexed by `C` is the side not containing `r`. Its boundary marks are precisely the marks in one of those arcs, with the two crosscut-endpoint marks optionally assigned to either adjacent region. A point at the endpoint of a descendant crosscut is incident only to regions on the `C` side, so its assignment cannot create an extra interval. Thus the marks assigned into `C` are a consecutive block, possibly empty or all of `B`.

In a cyclic order, a proper nonempty consecutive block has at most two boundary adjacencies to its complement. Empty and full blocks have none. This proves the bound. No diameter-pair support, owner labeling, force balance, or source optimality is used.

## Source application and scope limit

In the canonical O--O application, every old loaded-endpoint pair that can become a lower witness under a translation cloud of diameter `s < D - sqrt(D^2 - 1)` has old length at most `1+s`. For `D >= 7`,

`D - sqrt(D^2 - 1) = 1 / (D + sqrt(D^2 - 1)) < 1/12`,

so such a pair has length below `13/12`. By canonical `C-LOADED-NEAR-UNIT-ADJACENCY`, it is a side of the loaded-endpoint cycle. Therefore, **if** each loaded endpoint is given the single region assignment used to define branch membership in the motion model, at most two such physical loaded-loaded lower clauses cross each rooted branch. The assignments at crosscut endpoints must be specified; this audit does not infer them from set-valued endpoint support.

The broader assertion “every nonhub branch has no internal actual diameter pair” is refuted by the one-crosscut example in [Audit.138](target_c_diameter_support_crosscut_hub_independent_audit_2026-10-08.md): if the two marks of a diameter pair are the crosscut endpoints, either dual region can be selected as hub and the other closed shore is incident to both marks. The hub theorem alone cannot exclude that pair. The per-branch cycle-edge bound remains valid because it counts interval boundary adjacencies and does not require a branch to contain no complete diameter pair.

## Verifier boundary and canonical disposition

The source branch has no verifier for this topological claim. I reran its exact owner-system verifier at the frozen source SHA; it passed 14,182 tree-bank checks, 110,887 pinned Horn checks, and 72 binary packets. Those checks do not encode the crosscut-to-boundary interval proof, mark assignment, or source-level clause interpretation. They are finite abstract regressions only.

Promote only `C-ROOTED-CROSSCUT-MARKED-INTERVAL-CAPACITY`, with the assigned-mark convention in the theorem statement. Do not promote the source report's no-internal-diameter-branch inference. The loaded-loaded lower-clause application is conditional on the actual motion model supplying the same single-region assignment. The O--O supply, branch population, compatible source motion, and strict sub-`D` endpoint remain open.
