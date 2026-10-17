# Proposed coordinator-owned updates from Agent 2

No shared state or registry file was edited in this branch. These append-only proposal manifests are inputs for coordinator review:

- `ledger/proposed-source-main-artifact-index-records.jsonl`: 60 source-main artifacts with source index metadata and noncanonical/unreviewed destination proposals. Twenty source IDs already occur in the destination index; those proposals use collision-free destination IDs and preserve original IDs as provenance.
- `ledger/proposed-artifact-index-records.jsonl`: six noncanonical/unreviewed records from PR #949 and #954. The #970 report is already an exact destination duplicate; the #1007 files are historical maintenance evidence rather than research-index entries.
- `ledger/proposed-rights-ledger-updates.jsonl`: 21 excluded source-main third-party items and two excluded Packomania fixture files, with exact source hashes and the no-import reason.
- `ledger/source-pr956-periodic-extension-dependency.jsonl`: exact path/hash relations for the PR #956 report, checker, audit, and catalogue referenced by #1007.

The active artifact index and global rights ledger remain unchanged. Proposal records make no canonicality, theorem-state, or redistribution-rights claim.
