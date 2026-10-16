<!-- theorem-state: {"artifact_id":"ART-7B97D27268B3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C independent-referee run ledger — 2026-10-10

## Run lock

- Refreshed `origin/main`: `f4ebe9aaba65abece20f18fe778ee0662ec7544b`.
- Theorem state: `2026-10-10.audit.231`; C-I closed, C-II open, Level I open.
- Live owner-order branch snapshot: `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`.
- Audit.63's source snapshot: `51853ce9752c065663fd407289c6d46adc767f69`.
- Exact source reports and four associated verifiers listed below had no changes between the Audit.63 snapshot and the live owner-order tip. Their previous independent audit and verifier results therefore apply to the frozen live copies.

This pass reconciles current live-branch artifacts with the canonical stack. It makes no new mathematical promotion. The underlying reports are preserved on the live research branch; no discovery branch was changed.

## Priority A disposition

| Frozen source artifact | Claim reviewed | Verdict and canonical disposition | Verifier / remaining caveat |
| --- | --- | --- | --- |
| `docs/reports/target_c_hub_owner_terminal_capacity_audit_2026-10-06.md` | Selected terminal capacity and owner-region recurrence | **PASS — already canonical:** Audits.63/127 promote `C-OO-TERMINAL-OWNER-CAPACITY`, `C-OWNER-REGION-TREE-RECURRENCE`, `C-ACUTE-BINARY-OO-LAMINARITY`, and the scoped overlap-aware run/root allocation. Audit.63 also registers the exact abstract Horn packet as a regression. | Audit.63 reran the exact hub-system certificate. Its proposed fourteen-cut tube/range estimate was left unreviewed there and later withheld by Audit.138 for a missing exact cut-to-rhombus bound. Do not use it. |
| `docs/reports/target_c_terminal_oo_depletion_and_short_pocket_clauses_2026-10-06.md` | Short-pocket binary witness budget, `N_OO=o(D)`, and face-ledger consequence | **PASS — already canonical:** Audit.63 promotes `C-BINARY-LOADED-WITNESS-POCKET-BUDGET` and `C-OO-TERMINAL-TRAIN-POPULATION`; Audit.128 records the exact long-pocket regression. Later sink and side-pocket audits sharpen the binary sink scope. | The exact verifier checks finite geometry and arithmetic only; the asymptotic shore/KKT argument is analytic and appears in Audit.63. No source move follows. |
| `docs/reports/target_c_binary_owner_laminarity_and_crossing_scope_2026-10-06.md` | Independent binary owners versus crossing multishears | **PASS — already canonical:** Audit.63 promotes `C-ACUTE-BINARY-OO-LAMINARITY` and the exact crossing-multishear regression. Its scope does not cover general crossing multishears as independent owners. | The rational strict-rhombus verifier was rerun in Audit.63; all exact pair-distance checks pass. The regression does not assert source realization. |
| `docs/reports/target_c_one_vertex_convex_wall_shield_2026-10-06.md` | Full-source one-vertex convex-wall shield and five-/six-edge threshold | **PASS — already canonical:** Audit.63 promotes `C-ONE-VERTEX-CONVEX-WALL-SHIELD` and registers the exact two-deletion isolate regression. | The wall verifier was rerun in Audit.63. The shield supplies no arbitrary macroscopic-wall capacity or source extraction. |

Audit.151 separately promotes the singleton bad-terminal count `|S|<=x_B+m_B` and rejects the unsupported fourteen-cut path-range extension. Audit.184/185 and Audit.213 later refine acute binary sink and loaded-side-pocket accounting under their exact hypotheses. These later theorems do not supply source-level O--O family extraction or a finite C-II competitor.

## Canonical-state correction

Audit.114 already promotes `C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY` from the frozen PR #722 source report. Under its fixed subfamily-stability, disjointness, amplitude, isolate-dispatch, and lower-witness hypotheses,

`r <= 2 m_B + 3 (x_B + Z_out) + 2 d_H`,

with the Type-II refinement `r <= 147 (x_B + m_B) + 2 d_H`. The claim bounds a specified proposal family; it does not extract that family. `docs/STATE.md`, Target C `CURRENT.md`/`README.md`, and the active continuation prompt still called this deletion bound unaudited. This pass corrects those stale summaries without changing theorem state or the C-II endpoint.

## One-deficit isolate-accounting disposition

| Frozen source artifact | Claim reviewed | Verdict and canonical disposition | Verifier / remaining caveat |
| --- | --- | --- | --- |
| `docs/audits/target_c_one_deficit_isolate_accounting_second_referee_2026-10-10.md` from `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82` | Full-source `z<=N-1` fixed-wall exchange and its treatment of contact isolates | **PASS WITH NARROWED SCOPE — already canonical:** Audits.77/.80/.107 remain valid. The exchange counts and deletes every strict-interior label, including isolates, with one wall vertex; it retains every label outside the wall, including exterior isolates. It does not preserve interior-isolate identities. No new theorem, state bump, or route change. | Independent reconstruction is recorded in [`target_c_one_deficit_isolate_accounting_independent_audit_2026-10-10.md`](target_c_one_deficit_isolate_accounting_independent_audit_2026-10-10.md). The frozen verifier exited 0 with exact finite checks only; it does not establish the analytic all-`M` result. |

The source report and verifier hashes match the values recorded in the second-referee note. The fixed-wall proof still depends on `C-ONE-DEFICIT-ALL-M-STRICT-PACKET`, `C-ONE-VERTEX-CONVEX-WALL-SHIELD`, and `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`. The theorem-state manifest now points the existing canonical `C-ONE-DEFICIT-ALL-M-SOURCE-EXCLUSION` claim to this independent audit; its statement, status, and state version are unchanged. Target C `CURRENT.md` and the active continuation prompt now distinguish deleted interior labels from retained exterior isolates. The frozen discovery branch and PR #737 were not changed.

## One-corner packet second-referee disposition

| Frozen source | Claim reviewed | Verdict and canonical disposition | Verifier / remaining caveat |
| --- | --- | --- | --- |
| `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`; source theorem report at `6ee89d204688df2de70594e08ad6b12edeb9145a` | Audit.72's all-`M` strict packet and full-source `z<=N-2` contact-loss exchange | **PASS — already canonical:** the exact layer-peeling proof and exchange survive independent reconstruction. No theorem-state, dependency, or frontier change. | The report, packet verifier, and velocity certificate are byte-identical at the source report snapshot and live owner-order tip. The exact verifier passed at `M=3,4,6` (489 first-variation checks, 9,072 inserted-pair upper checks, 1,137 old-source checks, and 1,137 endpoint-pair checks). These finite cases corroborate but do not prove the all-`M` stress peeling. The separately canonical one-vertex shield handles every retained exterior label, including isolates. |

The independent check tracked the complete actual unit-neighbor graph through the six shells, including nonradial cross-layer edges at corners: these are killed at their outer noncorner endpoints before corner balance is used. At the missing-guard corner all remaining radial projections are positive; at radius one the absent center removes the last possible inward-chain balance. The opposite retained guards also certify nonaffinity. The Oler residual is the separate arithmetic consequence `z<=N`, leaving `{N-1,N}` under its area hypothesis; the packet exchange itself excludes only `z<=N-2`. The nested-hexagon helper's later output-label correction changes “arbitrary” to “chosen” cancellation fields and does not enter the packet verifier's proof. No defect or new implication was found, so a duplicate canonical audit artifact is not warranted.

## Refreshed branch and PR dispositions

Refreshed after the isolate-accounting audit. `origin/main=282ca64103a9b598bdd2f1cfe51bd87dab713b3a`, state `2026-10-10.audit.231`; all four research refs below remain at the same frozen tips recorded before the audit.

| Refreshed source | Current disposition | Remaining scope |
| --- | --- | --- |
| `origin/research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`; PR #722 is closed | **PASS — already integrated or superseded.** Audit cycle 176 in `docs/audits/target_c_integration_audit_ledger_2026-10-06.md` reconciles all 16 branch-only reports. This run independently confirmed the exact tip and closed PR state. | No unique unreviewed theorem remains on this snapshot. The packet/refill and source-motion gaps recorded by those audits remain open mathematically. |
| `origin/research/sol/target-c-exterior-cap-closure-20261006` at `f4a362727779f6afc0f01738015112c04fdb73d5` | **PASS — existing scopes audited.** The five branch-only reports map to Audits.84/.85, .94, .139–143, .150, .183, and .188 in the current audit/state stack. | The cap/grain extraction, cardinality-restoring refill, and simultaneous/source-level payment are still missing; do not treat reduced-source descents or fixed-cell capacity as those results. |
| `origin/research/sol/target-c-overnight-closure-20261007` at `c6a75bd708e553c4feb3a540e0b17f3b65e22a82` | **PASS — substantive fixed-wall modules already dispositioned.** Audit.175 reconfirms the four Priority A reports; the remaining one-deficit, sorting, local stress, wall-chart, and profile modules are recorded at their exact canonical scopes in Audits.66, .71–.82, and .107. Handoff files are provenance, not theorem claims. | No arbitrary-wall extraction or C-II endpoint follows. This reconciliation relies on the current audit artifacts; it does not claim a second proof audit of every previously audited module. |
| `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`; open PR #737 | Four Priority A claims remain byte-for-byte unchanged from their Audit.63 source and are already canonical; the other report claims map to the existing fixed-wall, shell, and wall-shield audits listed above. No discovery branch was modified. | Leave PR #737 open while its distinct handoff, literature, and research checkpoint artifacts remain preserved there; this run did not merge or close it. |

The older fourteen-cut dual-tree path-range claim remains **FAIL — proof gap** under Audit.138: the exact cut-to-rhombus/tube bound is missing. Audit.148/.149 provide narrower six-/five-row bounds only under their stated supplied-path hypotheses.

## Remaining queue

1. If PR #737 advances, snapshot the new tip and audit only theorem claims changed since the refs above; leave the discovery branch intact.
2. The actual full-source moving-wall extraction/refill and finite C-II competitor remain discovery obligations. No current audit of the listed snapshots supplies them.

## Validation record

The source report and verifier comparison from Audit.63's frozen source commit to the live owner-order tip returned no changed paths for the four Priority A reports or their four verifiers. This pass did not rerun those four individual mathematical verifiers. On the integration worktree, `build_artifact_index.py --write --write-headers`, `generate_theorem_state_views.py`, `check_theorem_state.py`, and `check_active_route_summaries.py` passed. The full registered theorem-certificate suite passed all 94 unique certificates. `git diff --check` passed.

For the one-deficit follow-up at base `496abf9d1d0d080f5f992f1c74619f166de0d011`, the artifact index and generated theorem views were rebuilt; theorem-state and active-route checks passed. The CI-supported unittest command `python3 -m unittest tools/test_check_theorem_state.py tools/test_check_theorem_state_pr.py tools/test_check_active_route_summaries.py` passed all 22 tests. The frozen one-deficit verifier exited 0, and the full registered theorem-certificate suite passed all 94 unique certificates. `git diff --check` passed.

For the one-corner second-referee check at the `f4ebe9a` main base, the exact packet verifier passed with the counts listed above. No theorem-specific test was added or run. The artifact-index rebuild found no generated metadata changes; only this ledger changed.

## Audit.232 finite hull-side train-capacity second referee

- **Main snapshot:** `90bb0d2822d6f7fa5b89bd58f9f27b108b3adc18`, state `2026-10-10.audit.231`.
- **Frozen theorem source:** `fdc40cc7844aaa8b5f949f59a8c1607edf43d65a`. The candidate report and verifier hashes recorded by Audit.232 were independently compared against that snapshot and current main; both blobs are unchanged.
- **Claim:** for the finite canonical post-ZF C-II source with `C=C_*`, `H=H_*`, every source label retained, and positive-area actual loaded force hull, the train/hull ledger gives `5(q-k)+x_B+m_B >= 3P_F-2`, with the exact good-interval and terminal-count clauses in `C-FINITE-HULL-SIDE-TRAIN-CAPACITY`.
- **Verdict:** **PASS — already canonical.** No theorem statement, dependency, lifecycle, or C-II frontier change.

The vulnerable bridge was the passage from alternating good hull-side endpoints to the triangle-free train-crossing graph. Reconstruct the medial path of a train by joining consecutive contact-edge midpoints through the center of each traversed quadrilateral. Each contact edge belongs to one train; these paths do not run through source vertices or nonquadrilateral faces. Within a rhombus, two distinct paths can meet only at its center, exactly the opposite-edge crossing counted by the canonical train-crossing graph. `C-ZRF` puts every active `H` endpoint in the nonisolated contact core `V`; `C-ATTACH-CURRENCY` places `V` in the convex hull `F`. Thus every train path lies in the disk `F`, with a good terminal midpoint on each corresponding unit hull side. Alternating endpoints force an intersection, hence an actual rhombus crossing. At each such crossing the two projective train directions differ by more than `pi/3`; three pairwise crossings would require three cyclic gaps each greater than `pi/3` on a projective circle of length `pi`, which is impossible. A singleton boundary contact edge has only one oriented hull-side incidence, so it is not a double-good train.

The remaining arithmetic is exact: `T=(q-k)+2f`; at most two trains have two good terminals; each other train consumes a bad outer occurrence or a bounded nonquadrilateral-face incidence, totaling at most `x_B+m_B+4f+Q`. Since `Q>=f` and `Q=2(q-k)-b`, this yields `3b<=5(q-k)+x_B+m_B+2`; the interval paths give `P_F<=b`. All contact-isolated source labels remain in the full configuration and in unit-separation checks; they are not silently inserted into the core train graph.

The frozen exact verifier passed: 383 rational unit-separated triangle-free sources (354 with repeated outer walks, 225 with repeated loaded-vertex occurrences), 183,212 exact depletion ledgers, and the unit-square sharpness fixture. These checks do not establish the universal topological argument or global minimality. The theorem supplies no finite move or C-II closure.

## Current-authority pointer correction

On the same main snapshot, `docs/STATE.md` named `.230` as the current state version while the manifest and generated state header were `.231`; `docs/targets/target-c/CURRENT.md` said current claim authority ran only through Audit.108. Corrected these two pointers to `2026-10-10.audit.231`. The older `.54` header in `CURRENT.md` explicitly labels its generated ID list as a dated snapshot and is left as historical material.

This referee increment does not bump `state_version`: it corrects scope documentation and records a second audit of an already canonical theorem without changing its claims. The state checks had passed before the prose correction, showing that they do not enforce these free-text version pointers.


## Audit.234 central-vacancy classification second referee

- **Main snapshot:** `75c3d462044bf98210ff08713695e0c5420c5f53`, state `2026-10-10.audit.231`.
- **Frozen source:** `origin/research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`. The source report and finite verifier hashes match Audit.234 (`964e7d9d...271fe4` and `67f73a8f...7b061`).
- **Claim reviewed:** for fixed `M>=3`, a feasible `N-1` interior cloud in the specified six-sided wall converging to the radius-`M-1` triangular chart with its center omitted is eventually an exact sorted-rate packet with its center deleted, and therefore contains `6(M-2)` unit triangles.
- **Verdict:** **PASS — already canonical, exact chart scope retained.** The first-order rows yield the stated radial permutahedron; the selected stress forces equality at a permutation vertex; sector recurrences then fix the full velocity. The relative-interior normal-cone argument supplies positive first-order weights on every weak active row, while the exact contact matrix has full moving-column rank. The resulting `O(theta)` local isolation closes the passage from limiting velocity to an exact packet. No arbitrary one-deficit chart, uniform-in-`M` onset, extraction from a source, or C-II/Level-I consequence follows.

The verifier was independently run at the frozen source: 14 exact packet cases, 37,773 pair checks, 2,412 first-row checks, 1,016 subset checks, and exact packet triangles/energies; its sampled ranks are finite checks only. I found no omitted moving-site contact-row class or invalid first-order-to-finite inference. The theorem and dependencies were already canonical, so this second audit adds no state bump or route change.
