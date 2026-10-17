> Generated reading edition · [exact source](../../../docs/launch/MIGRATION_VERIFICATION.md) · source SHA-256 `bfeb988cd1cec4c5f1a19c2ddcb9316fa6e7c34c6491a6bb69c70b3106dc0f29`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Migration and release verification

Run the migration checks and original Gate 2 on the same clean candidate:

```sh
/path/to/locked-environment/bin/python tools/verify_migration_release_candidate.py \
  --output /absolute/new-detached-receipt \
  --gitleaks /path/to/gitleaks --actionlint /path/to/actionlint
```

Use the Python version, wheel hash lock, and scanner versions documented in
[Gate 2 verification](GATE_2_VERIFICATION.md). The optional `--source-repo`
argument adds the original source-backed provenance replay.

The wrapper runs the source-main union audit, recorded branch and worktree
evidence audit, and committed Markdown reference scan with the captured candidate
SHA. It then runs the original Gate 2
runner, including every registered certificate, all corpus and tooling tests,
publication checks, full Git history scans, and workflow lint. It retains the
original Gate 2 commands and registered checks. The runner adds only the exact
committed-object finding review documented in [the scanner review](MIGRATION_SCANNER_REVIEW.md).
Any reviewed changes to other baseline engineering files are accounted for by
the migration disposition and transformation records.

The new receipt directory contains the union, refs, and navigation JSON reports, command
logs, and the complete original Gate 2 receipt under `gate2/`. A passing wrapper
receipt requires every command to pass, an unchanged candidate, and a passing
underlying receipt for the exact same commit and tree. Reports for another commit
are not accepted. A missing or malformed underlying receipt fails verification.
The wrapper rejects shallow history and records all local ref identities before
and after execution. A ref change fails the combined gate because history scans
use `--all`. Use a stable isolated clone for the final receipt.

The union audit reconstructs the pinned 4,717-file source tree from committed
inventories and checks the combined dispositions, including the nested frozen
813-report source and destination identities. It requires no source clone.
The reference scan distinguishes active missing dependencies from literal
historical references and records exact archived counterparts where available.
An archived reference map does not repair an active missing dependency.

Run this command after the final integration merge. A receipt from before that
merge does not verify the resulting `main` commit. Passing automated verification
does not grant publication permission, recover unavailable uncommitted worktree
data, establish deprecation readiness, or promote any mathematical claim.
Level I remains open. The wrapper's `combined_checks_passed` covers only the four
recorded scopes; any remaining unknown working-copy history needs separate,
explicit handling before deprecation.
