<!-- theorem-state: {"artifact_id":"ART-53B2C78707E5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent audit disposition — sign classes and residual-closure tails

Date: 2026-10-10\
Audit base: `origin/main=ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`\
Frozen fused-review source: `origin/research/level-i-fused-review-20261009=6132201c1d3056ca68a222217094acb819f5b4d7`\
Frozen residual source: `origin/research/target-c-residual-closure-20261005=ed535f5a3a45e3921d91a29c38a0cb37f1d27921`

This note records an independent disposition of the exact remaining theorem-shaped scopes identified in the fused review and the closed PR #722 snapshot. It does not alter theorem state.

## 1. Fused quarter-fold report, Section 6

Candidate: Section 6 of `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`.

**Exact result and verdict: PASS — already subsumed.** For an eligible face-closed quarter-fold with every contact retained and a full-source unit-separated, triangle-free endpoint, the train-sign equalities on a simple convex five-, six-, or seven-sided actual contact face are already consequences of canonical `C-QUARTER-FOLD-MINIMUM-FACE-SIZE`: a nonconstant eligible sign pattern requires at least eight sides. The source-realized two-hop equalities are canonical `C-QUARTER-FOLD-SOURCE-COMPATIBILITY`. Adding these equalities as edges in a defined graph makes every sign assignment constant on each connected component by construction; if that graph is connected, there is one common sign. Each nonconstant eligible physical face has degree at least eight and therefore spends at least four in the canonical defect `Q=sum_F(deg(F)-4)` over bounded nonquadrilateral physical contact faces.

No separate claim ID is warranted. The derivation adds no new geometric step beyond the two canonical constraints and graph connectivity. Connectivity is not established for general canonical sources. Contact isolates remain part of endpoint feasibility, but they are not train-sign variables. A constant sign makes the integrated potential a rigid rotation on a connected contact component; this sign statement alone does not specify isolate or disconnected-component placement in a full-source endpoint. Accordingly, the report's phrase about absence of “nonaffine stress currency” is not promoted as a separate full-source motion or stress theorem.

No finite verifier is relevant to this compositional result. No quarter-fold endpoint, isolate relocation, source motion, or capacity is produced.

## 2. Residual-closure outer-isolate owner bound

Candidate: Section 6 of `docs/reports/target_c_outer_isolate_blocker_collars_2026-10-05.md`, SHA-256 `253ff02de18c916d411360e5d1a87b371b4eb4efb3746c594dc9607290ce51f7`.

**Exact result and verdict: PASS — already canonical, with the zero-defect endpoint stated non-strictly.** In its stated Type-II near-disk scope, put `A=x_B+m_B`. The collar estimate in Section 5 gives `N<=48A`, strictly when `A>0`; if `A=0`, it gives `N=0`. The canonical loaded-neighbor and fixed-family capacity bounds give `k<=2m_B+3x_B+3N<=147A` for surviving singleton proposals, strictly when `A>0`; when `A=0`, `k=0`. Restoring at most `2d_H` upper-exception proposals gives `r<=147A+2d_H`. This is weaker only in presentation than, and exactly within the hypotheses of, canonical `C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY` (Audit.114). The report's looser `150A+2d_H` follows immediately as well. Its owner family remains a supplied family of individually tested proposals; neither its existence nor simultaneous feasibility is inferred.

No duplicate ID or state bump is appropriate. The source's strict shorthand must not be applied at `A=0`; the promoted conclusion is non-strict there. The arithmetic is exact, and it uses the collar and family hypotheses in their promoted scopes. No new verifier is claimed. The actual O–O proposal extraction and a feasible full-source move remain unproved.

## 3. Other residual-closure tails

- `target_c_loaded_neighbor_outer_owner_bound_2026-10-05.md`: the loaded-neighbor incidence theorem is canonical from Audit.42; its fixed-subfamily original-family extension is canonical from Audit.52 and Audit.114. The report explicitly makes no general multishear extraction or simultaneous-feasibility claim. A broader synthesis without fixed proposal identities and subfamily-stability hypotheses is not a theorem candidate.
- `target_c_generic_isolate_anchor_localization_2026-10-05.md`, Section 4: the degree-three fan-reflection clause is already subsumed by the exact finite collision regression in Audit.102. Its broader route synthesis does not state a new quantified theorem.
- `target_c_outer_isolate_blocker_collars_2026-10-05.md`, Sections 1 and 7: these name actual O–O proposal extraction, source-contact preservation, upper safety, and source-move realization as missing premises. No proof of those steps appears in the frozen report, so there is no positive claim to promote or a countertheorem to audit here.

**Frontier effect:** none. The snapshots contain no additional independently promotable theorem among these tails. The exact source-level extraction/move bridge remains an open discovery obligation. No discovery branch or source worktree was modified.
