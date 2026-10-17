# Publication audit

The active audit concerns the current repository and the results actually
reported for it. It does not enforce a migration snapshot.

## Active scope

- Current theorem claims retain their stated assumptions, lifecycle and scope.
- Proof, audit, certificate and task dependencies must resolve.
- Generated mathematical views must agree with their current sources.
- Current files and reachable Git history receive credential and restricted-content scans.
- A release run records its commands and results and checks that its checkout
  stayed consistent during execution.

See [release verification](GATE_2_VERIFICATION.md) for the runnable procedure.
Routine documentation changes do not require a full mathematical replay.

## Removed migration machinery

Import-completeness checks, frozen-source verification, historical reference
audits, rights-manifest reconciliation, source-byte pinning, migration repair
tools and their tests have been deleted. The old import records remain
historical data. They are not an allowlist of files that contributors may edit.

The owner authorization recorded during import and the project's license
remain in force. Ordinary Git attribution is accepted. No new per-file
permission or hash ledger is required for normal project edits.

## Publication status

This cleanup does not change any mathematical claim or establish a new full
certificate result. Level I remains open. Actual verification results belong
with the changes or releases they cover.

Hosted execution remains unverified until jobs execute successfully. The
repository remains private until the owner changes visibility.
