# Public corpus candidate: verification evidence

The scientific source is `5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`; current source main advanced to `aa9b45669ce7200a99f6ec4c58e1e3c23a57387f` by integrating localized CI only. All inherited claim records, statuses, scopes, edges, registrations and canonical module lists were compared equal. The source state-version label is `2026-10-10.audit.234`. Level I/A/B/C-II remain open; C-I is closed.

## Executed locally

| Command / check | Result | Measured time |
| --- | --- | --- |
| Locked CPython 3.14.7 environment; hash-locked Linux wheel installation | passed | installation not benchmarked |
| `python tools/run_theorem_certificates.py` | 94/94 registered certificates passed | 387.023 s |
| Selected proposal verifiers (unreviewed) | 16/16 passed | 34.669 s total |
| Additional frozen-source verifiers recovered from audit citations | 4/4 passed | 7.873 s total |
| `python -m unittest discover -s tests -v` | 8/8 adversarial omission/scope tests passed | 39.356 s |
| `python -m unittest tools.test_local_ci -v` | 60/60 localized CI tests passed | 6.357 s |
| `python tools/check_theorem_state.py` | passed | not separately benchmarked |
| `python tools/check_public.py` | 451 IDs / 845 edges / 94 registrations / 19 tasks; no unresolved local dependency | timing recorded at final gate |
| Gitleaks v8.30.1 tree scan, redacted | zero findings after correcting a synthetic key-header fixture | 0.798 s scanner time |

Exact certificate propositions, arithmetic implementations, parameter expressions, source hashes, output and limitations are in [registry](../../research/certificates.json) and [replay outputs](../../research/replay-results.json). A passing replay is not independent human proof review or a proof of the missing global implication. The additional proposal/frozen run records are published with the final verification receipt.

## Remaining gates at this candidate checkpoint

Independent fresh-clone A/B/C research sessions, final rights/provenance/privacy/history audit, exact release commit and visibility/anonymous-access verification are pending. The repository remains private at this checkpoint. Hosted Actions execution is not established; the source account has experienced restrictions. No paid usage or spending limit was changed.

## Independent whole-source alternatives: supplemental replay

After the original 94-certificate receipt, the post-baseline private PR #1005 mathematical reports and verifiers were selected for public inclusion as **unreviewed** (not registered canonical certificates). Their original Git blobs were byte-identically transferred, and both checkers were executed independently on Python 3.12 with SymPy in a separate audit workspace:

- `python research/verify_global_joint_phase_compatibility.py`: 9 dual-basis pairings, 3 cross-phase pairings, positive stress-only laminate, rotated-frame compatible laminate, and exact boundary-work identity — **PASS**.
- `python research/verify_global_separable_distortion_obstruction.py`: 499 odd-rim marginal checks, 122 exact cyclotomic all-pair Möbius identities, and Cayley–Menger nonplanarity determinant -72 — **PASS**.

These are independent computational replays of limited claims, not human proof reviews or tests of source-global optimality. The original comprehensive 94-certificate and public checker results were recorded on the earlier candidate; **the final integrated release commit has not yet been fully reverified**. Rights/history publication gates remain open.

## Independent release-security regression expansion

The earlier publication scanner inspected only the current Git tree. An independent synthetic reproduction demonstrated that a prior reachable deleted credential and restricted paper were missed, even when HEAD appeared clean. The revised scanner now traverses every reachable revision and historic blob (with a fail-closed size limit) and inspects commit messages and other branch refs. All **10** publication-audit fixture tests passed independently on Python 3.12, including deleted-secret, deleted-PDF, alternate-branch-secret and commit-message-secret cases. No actual private/public corpus full-history scanner execution is claimed until the final checkout is available. This improvement does not waive rights, personal author-email consent, full mathematical verification, or fresh outsider A/B/C research sessions.
