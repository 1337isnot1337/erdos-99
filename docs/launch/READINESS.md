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
