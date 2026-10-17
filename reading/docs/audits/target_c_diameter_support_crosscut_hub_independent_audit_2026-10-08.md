> Generated reading edition · [exact source](../../../docs/audits/target_c_diameter_support_crosscut_hub_independent_audit_2026-10-08.md) · source SHA-256 `7e2f38dc36f9777fcf18210c7eb4f8a64c8775eebb8da3e41094883ba0cd4010`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-EE4A3718E7B5","canonical":true,"claim_ids":["C-CROSSCUT-HUB-ENDPOINT-SHORE-REGRESSION","C-DIAMETER-SUPPORT-CROSSCUT-HUB"],"claim_statuses":{"C-CROSSCUT-HUB-ENDPOINT-SHORE-REGRESSION":"regression","C-DIAMETER-SUPPORT-CROSSCUT-HUB":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: diameter support hub for a proper crosscut tree

**Date:** 2026-10-08  
**Audit base:** `origin/main=541faab02c97e56d4704708bbdcdf279d23f694c`, state `2026-10-08.audit.137`  
**Frozen source:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`  
**Source report:** `docs/reports/target_c_hub_owner_terminal_capacity_audit_2026-10-06.md`, SHA-256 `61e16a888f99858fc6af890c05f4ac1ba27efd0394ea6e65434b29412dbf3468`  
**Source verifier:** `research/verify_target_c_hub_owner_systems_2026_10_06.py`, SHA-256 `0618e67333980c32b867b64272a099a6edbc30c2d47d6913e8ea7ccf38c9414b`

## Verdicts

- **PASS WITH NARROWED SCOPE — promote `C-DIAMETER-SUPPORT-CROSSCUT-HUB`.** In a disk cut by pairwise disjoint proper crosscuts, the support subtrees of any finite family of boundary pairs that pairwise share an endpoint or alternate on the boundary have a common region. The set-valued endpoint convention below handles diameter endpoints that coincide with crosscut endpoints.
- **REGRESSION VALID — promote `C-CROSSCUT-HUB-ENDPOINT-SHORE-REGRESSION`.** The common-hub result alone does not imply that every nonhub branch contains no diameter pair if a marked endpoint lies on a crosscut. Such an endpoint has incident regions on both sides.
- **FAIL — proof gap; do not promote the fourteen-cut tube estimate.** The frozen report names a straight witness segment, a `sqrt(3)` tube, distinct rhombi, and a prior area calculation, but gives neither an exact inequality nor definitions and proof of the cut-to-rhombus injection. The source verifier does not encode this geometry.
- **No C-II frontier change.** The hub lemma supplies no owner capacity beyond Audits .63/.127, no finite source move, and no strict sub-`D` competitor. C-II and Level I remain open.

## Exact theorem promoted

Let `X` be a closed topological disk and let `Gamma` be a finite family of pairwise disjoint proper crosscuts of `X`. A crosscut is a simple arc with distinct endpoints on `partial X` and interior in `int(X)`. Let `T` be the dual graph whose vertices are components of `X \\ Gamma` and whose edges correspond to crosscuts; for disjoint proper crosscuts, `T` is a tree.

For a boundary mark `p`, let `R(p)` be the set of complementary regions whose closures contain `p`. This is one region unless `p` is a crosscut endpoint; at a crosscut endpoint it consists of the two regions incident to that crosscut. For an unordered pair `e={p,q}`, let `S_e` be the smallest subtree of `T` containing `R(p) union R(q)`.

Suppose a finite family `E` of such boundary pairs has the property that every two distinct pairs either share a mark or have four distinct endpoints that alternate in cyclic order on `partial X`. Then

```math
\boxed{\bigcap_{e\in E} S_e\ne\varnothing.}
```

### Independent proof

If two pairs share an endpoint `p`, both support subtrees contain `R(p)`, so they intersect. Now take disjoint pairs with alternating endpoints. If their support subtrees were disjoint, a tree edge would separate them. Its crosscut `gamma` separates `X` into two sides and separates the boundary into two intervals. Since each support subtree avoids that tree edge, both endpoint-region sets of each pair lie on one side. A pair endpoint at an endpoint of `gamma` would be incident to regions on both sides and would force its support subtree to contain the edge, so none of the four marks is an endpoint of `gamma`. The two marks of each pair therefore lie in one of the two boundary intervals, and the two pairs lie in opposite intervals. Their endpoints cannot alternate, a contradiction.

Thus the support subtrees are pairwise intersecting. The finite subtree Helly property gives a common tree vertex. This argument permits crosscut endpoints to coincide with the boundary marks by using all incident regions in `R(p)`; it does not silently choose one side at such an endpoint.

### Canonical diameter application

When the marked boundary pairs are actual loaded-diameter edges in the canonical occurrence disk, `C-WOODALL` gives the required pairwise condition: two edges share an endpoint or their four extreme endpoints alternate in force-hull order. `C-LOADED-HULL` puts the distinguished endpoint occurrences in that same cyclic order on the outer contact-face walk, and `C-OWNER-REGION-TREE-RECURRENCE` supplies the dual tree for the specified pairwise-disjoint proper O--O crosscuts. The theorem then gives a common region on every loaded-diameter support subtree, provided every endpoint in the application is represented by its boundary mark.

This source application concerns the loaded diameter pairs represented in that disk. It is not a claim about an unrepresented source point or contact isolate.

## Regression against the broader branch inference

Take a disk with one proper crosscut whose endpoints are `p` and `q`, and mark the pair `{p,q}`. The dual tree has two regions and the pair's support subtree contains both. Either region can be chosen as a common hub, but the other branch's closed shore is incident to both `p` and `q`. Thus the common-hub theorem alone does not establish that a nonhub branch contains no complete marked pair when endpoints on crosscuts have no unique region assignment. This is an exact topological regression only; it is not a canonical-source counterexample. A source-level branch exclusion needs either an explicit endpoint-avoidance/unique-region hypothesis or a separate boundary-incidence argument.

The source report's further conclusion that each such branch has at most two loaded-loaded lower witnesses also needs that branch-to-loaded-hull-interval correspondence. This audit does not promote it.

## Fourteen-cut tube estimate withheld

At the frozen source tip, the hub report says that each separating non-singleton midpoint cut meets a straight witness segment in a strict rhombus, distinct selected cuts use distinct rhombi in a narrow window, and the rhombi lie in the segment's `sqrt(3)` tube. It then refers to a predecessor's area estimate and rational constant calculation. It does not state the resulting cut bound or provide the segment, midpoint-cut, tube-area, or injection definitions needed to reconstruct it. The source verifier enumerates owner-labelled trees, Horn systems, and abstract terminal budgets; its exact output does not test this geometric assertion.

The exact audit blocker is therefore: state the finite inequality with all constants and hypotheses, define the witness segment and midpoint-cut intersection, prove the injective assignment to distinct strict rhombi, and give the tube-area calculation. Until that is supplied, the fourteen-cut bound remains unreviewed and is not an input to the promoted hub theorem.

## Dependencies and certificate boundary

Canonical dependencies for the loaded-diameter application are `C-WOODALL`, `C-LOADED-HULL`, and `C-OWNER-REGION-TREE-RECURRENCE`. The argument itself is a finite topological proof and has no certificate dependency.

I inspected and reran the exact source verifier at the frozen SHA. It passed 110,887 pinned Horn checks, 14,182 tree-bank checks, and 72 binary packets. The code explicitly treats geometry and source realization as unencoded; it does not verify the support-hub lemma, the branch-exclusion inference, or the fourteen-cut tube estimate. These finite checks are regression evidence only.

## Claim ledger

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Pairwise alternating/shared boundary pairs have a common support region | PASS WITH NARROWED SCOPE | Canonical `C-DIAMETER-SUPPORT-CROSSCUT-HUB` |
| The support-hub theorem alone leaves no complete pair in every nonhub branch, including cut-endpoint marks | REGRESSION VALID | `C-CROSSCUT-HUB-ENDPOINT-SHORE-REGRESSION`; unique-region or endpoint-avoidance hypotheses are needed for that corollary |
| A nonhub branch has at most two loaded-loaded lower witnesses | NOT PROMOTED | Requires an independently established branch-to-loaded-hull-interval map |
| Fourteen non-singleton cuts fit in the cited tube | FAIL — proof gap | No exact inequality, definitions, injection proof, or reproducible verifier proposition at the frozen source |
| Level I or C-II closure | NOT CLAIMED | No source motion, replacement, or global-minimizer contradiction |

## Frontier effect

The common support region is now available as a canonical finite topological input in its exact proper-crosscut scope. The owner-capacity results remain governed by Audits .63 and .127. The source-level finite-move endpoint still requires every old contact, full-source lower pair, actual diameter, inactive upper pair, and unary rhombus test; this audit does not change it.
