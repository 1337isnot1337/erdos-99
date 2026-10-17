> Generated reading edition · [exact source](../../../docs/audits/pr950_autonomous_proof_audit_2026-10-15.md) · source SHA-256 `8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-047AD4339705","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# PR 950 autonomous proof audit and endpoint-cut repair

> **Destination lifecycle:** source PR #950 proof-audit record, preserved as provenance and correction evidence. It is not an independent destination audit and does not promote the candidate. The endpoint-inclusive cut repair does not close the endpoint-overlap or finite-competitor obligations.

Date: 2026-10-15. Original exact head:
`6433d1db49a1363bfa65008eb78f6b15d6ef4ed7`.
The audited [report](../reports/target_c_train_return_length_budget_worker03_2026-10-10.md)
has 569 lines at that head. This audit examines its full proof and the repair
in this change. Classification: AI-audited candidate awaiting independent human
mathematical review. No canonical promotion or C-II/Level I closure is claimed.
The merged source state remains `2026-10-10.audit.234`.

## Substantive defect and repair

The original rigidity-to-grid argument treated only separators disjoint from the
loaded and grid terminal sets. Distinct-endpoint vertex Menger requires a lower
bound for endpoint-inclusive cuts. Deleting grid vertices can also split the
remaining grid among several components, so a single component containing the
whole grid cannot be assumed.

The repaired proof takes every component meeting the undeleted grid, applies
the rigidity-brace estimate componentwise, and charges all its leaving contacts
to the separator. A simple quotient path between a diametral pair of grid
vertices visits each chosen component once. The two units in each component's
brace estimate pay its two entry/exit edges; contacts internal to the separator
are debited twice from its degree budget and used at most once on the quotient
path. This proves `diam(X_D)<=5|S|` for every endpoint-inclusive separator and
retains the candidate linkage density `gamma/5`.

The argument includes a cut containing the entire grid or loaded terminal set,
a cut splitting the grid into many components, a path entirely in the separator,
and a diametral pair in the same remaining component. It uses actual unit
contacts and keeps isolates outside the core rigidity argument.

## Full proof and dependency audit

| Report step | Check and scope |
| --- | --- |
| Nontrivial long-train returns | Canonical Audit 206 bounds incident hull-ended crossings by `O(D^(5/3))`; each retained train has `ell D+O(1)` crossings, so only `O(D^(2/3))` are removed. A loaded-loaded terminal unit edge is an actual loaded-hull side under the stated finite adjacency hypotheses. Every remaining terminal has an unloaded endpoint. Audit 235 applies to the selected subbank, and its Menger paths are nontrivial. |
| Component concentration | The canonical uniform-cell-area theorem gives a fixed bound on nonempty unloaded components in either branch. Pigeonhole the selected roots, then reapply the subbank separator bound. Truncate paths at their first loaded vertex to obtain routes in the specified component and distinct attachment incidences. |
| Length quantiles | Full-source Oler gives `n<=pi D^2/(2sqrt(3))+O(D)`. Vertex-disjoint paths obey `sum(ell_i+1)<=n`; Markov counting gives precisely the reported retained-fraction constants. This includes contact isolates in the population bound. |
| Individual Type-II grid access | The port-multiplicity theorem controls actual attachment incidences. Removing fewer than `eta D` bad incidences from the Oler half-bank leaves the stated linear good family. Concatenation supplies routes without claiming their disjointness. |
| Common grid | Uniform cell area and diameter provide the stated inscribed-disk constant. An arc of length `delta D` contains a linear port family. The displayed translated half-radius disk lies in every homothetic crop. Global Type-II cell deficit controls this source-dependent disk; boundary trimming and fixed-phase cuts cost only `O(D)` faces/perimeter. Isoperimetry extracts a quadratic coherent piece; local trains stop at its crop boundary, so finite pseudogrid extraction retains all chosen source vertices inside the common disk. Fixed radii are chosen before letting `D` grow. |
| Rigidity-brace lemma | Triangle-free planar block Euler counting gives `2|X|-e_X>=diam(X)+2`, including bridge blocks and the one-vertex case. Fewer crossing contact rows would leave a nonzero internal flex supported on unloaded `X`. Two distinct fixed loaded diameter endpoints exclude a rigid-motion extension, contradicting the canonical mixed rank. No isolate or unloaded diameter row is silently introduced. |
| Distinct-endpoint grid linkage | Repaired above. Every endpoint-inclusive cut is charged, preserving the factor five and both terminal distinctness conclusions. The grid's distinct crossing rhombi give its Euclidean diameter lower bound by isodiametry. Oler then gives the second linkage's stated length quantile. |
| Optimized return constant | Implicit differentiation gives `5k+epsilon/(3sqrt(r-epsilon))=(2/3)sqrt(r-epsilon)`. Substituting `u=epsilon/r` yields `64(2-3u)^4=75r u^4(1-u)`. On `(0,2/3)` the left side strictly decreases and the right side strictly increases; endpoint limits give a unique maximizer. Numerical values are illustrative. |
| Marked-rail check | Degree at most five pays rail multiplicity. Hall applies once each rail has at least five vertices. One-sided marks remain deep in the same cap; Oler gives the compatibility inequality. Its constant is strictly weaker than Audit 133 because `pi^2<10`; no new capacity is claimed. |
| Failed extensions and regression scope | Graph disjointness does not bound straight-segment face multiplicity. Positive stress support supplies no uniform price. The Pell grids demonstrate only the unrestricted geometric length scale. The two linkage families can have disjoint attachment labels; no train-root-to-grid linkage or endpoint move follows without additional overlap. |

The proof uses canonical claim IDs and their recorded core/full-source scopes.
The contextual preprint supplies no mathematical premise. This audit does not
re-audit the canonical inputs or imply external peer review. Independent human
review must check the full repaired proof, especially crop/pseudogrid interfaces,
the componentwise endpoint-cut argument and the actual-label overlap limitation.

## Verification boundary

This is an analytic contribution; no finite test proves its unbounded claims.
The generated artifact index, theorem-state and promotion-transaction checks,
documentation links and patch whitespace are replayed for the repaired head.
The exact final head and command outcomes are recorded in the private closeout
receipt and PR audit record after the commit is created. No canonical manifest,
active route, prompt or certificate registration is changed.
