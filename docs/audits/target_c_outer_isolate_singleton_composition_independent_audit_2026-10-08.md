<!-- theorem-state: {"artifact_id":"ART-5C0C14A5E156","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C Audit.129 — outer-isolate singleton-composition crosswalk

**Date:** 2026-10-08  
**Audit base:** `origin/main=0f970f223f1b6019c36eaee38dfba7c409b900b4`, state `2026-10-08.audit.128`  
**Source branch and frozen snapshot:** `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`  
**Source artifact:** `docs/reports/target_c_outer_isolate_blocker_collars_2026-10-05.md`, SHA-256 `253ff02de18c916d411360e5d1a87b371b4eb4efb3746c594dc9607290ce51f7`  
**Verdict:** **PASS — already subsumed**, for Section 6 under the canonical original-family owner-capacity hypotheses. No theorem ID or route change is warranted.

## Exact section audited

Section 6 assumes an already specified small O–O binary proposal family. After removing at most `2 d_H` upper-exception owners, its surviving singleton proposals preserve old contacts, keep old diameter pairs at distance at most `D`, keep old nondiameter pairs strictly below `D`, pass unary rhombus checks, and strictly shorten an old diameter. The report's preceding isolate dispatch puts every lower witness at old distance at most `5/4`. In the Type-II low-defect specialization it concludes

`r <= 150 (x_B + m_B) + 2 d_H`.

The claim is conditional on those proposal, dispatch, deletion, and survivor hypotheses. It does not extract the proposal family from a source.

## Independent comparison with canonical results

The family is the fixed O–O family of the report's Section 4 dispatch; proposals and isolate anchors are held fixed when owners are discarded. Its displacement cloud satisfies the report's strict long-pair threshold. Section 4 bounds lower-witness old lengths by `1+s<5/4`, so the canonical owner-capacity theorem applies with `t=5/4`, which lies in `1<t<sqrt(2)`.

Audit.114 independently proves `C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY` for this fixed, subfamily-stable proposal setting. It handles the fixed inactive-long-pair exception set of size at most `d_H`: each exceptional pair can spoil at most two singleton proposals, so at most `2d_H` owners are discarded. Every survivor then has the stated lower-witness, contact, upper-bound, and unary properties. Its endpoint count gives

`r <= 2 m_B + 3 (x_B + Z_out) + 2 d_H`.

In Type II, Audit.105's collar theorem substitutes `N<=48(x_B+m_B)` for the active isolate witnesses, and Audit.114 gives the stronger bound

`r <= 147 (x_B + m_B) + 2 d_H`.

This implies the Section 6 bound with coefficient 150. The `+2d_H` term is not a new extension: Audit.114 already proves it under the explicit fixed-family/subfamily-stability and fixed-assignment hypotheses. The collar input is exactly `C-OO-OUTER-ISOLATE-COLLAR-BOUND`; the owner accounting is exactly `C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY`.

## Scope and disposition

This crosswalk audits only the Section 6 composition. It does not promote the source report's broad O–O family extraction, guarantee the required motions or low-defect condition, establish simultaneous feasibility, or change C-II/Level I. The earlier Audit.105 note that Section 6 awaited a separate owner-count audit is resolved by Audits.106 and .114; this record makes the exact source-section subsumption explicit. The source report remains unreviewed as a whole because its other claims have separate scopes and dispositions.
