> Generated reading edition · [exact source](../../../docs/launch/RELEASE_CANDIDATE.md) · source SHA-256 `6b424c07040a8918feaa10aeeaf71cc9956df667e112ba32f67dfae343f5a084`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Publication candidate 0.1.0-rc.4

This is an open research corpus. **LEVEL I STATUS: STILL OPEN.**
Target A, Target B, and C-II remain open; C-I is closed within its recorded scope.
The publication work changes presentation and operational tooling, with no
mathematical claim promotion.

## Current inventory

- 451 claim IDs, 845 declared theorem edges, and 94 registered certificates.
- 23 current task cards.
- 810 original inclusion records, with unchanged source identities.
- 813 frozen Target C reports and 21 support files in the separate migration ledger.

The [GitHub reading edition](../../README.md) provides compatible math,
public bibliography links, and navigation to the original code/data. Every page
links to its exact source and records its source hash. Frozen proof and archive
bytes remain intact; the edition is a generated presentation view.

The task selector resolves prerequisite IDs through the generated public theorem
graph. Its regression tests exercise the complete catalogue and reject unknown
IDs or unrelated proof mappings. Gate 2 now directly runs both the selector and
the reading-edition check.

The current reading fix preserves blockquote/list containers and GFM table cells.
The [presentation repair ledger](../../../docs/publication/reading-tex-repairs.json) records
source-hash-bound TeX escape and punctuation corrections; truncated quotations
remain literal text. Every reading page links directly to the current theorem
state. Original proof bytes and mathematical lifecycles remain unchanged.

Candidates `0.1.0-rc.1`, `0.1.0-rc.2`, and `0.1.0-rc.3` are superseded
presentation candidates. Their tags remain immutable; their receipts do not
verify the current commit. A new final-commit release replay is still required
before publication.

## Release evidence and remaining decisions

Gate 1's recorded source authorization remains limited to the same first-party
material. The [editorial-change ledger](../../../docs/publication/publication-polish-20261017.json)
binds operational edits to exact baseline bytes and modes, preserving each original.
It grants no new third-party rights. Source identities and mathematical lifecycle
records are unchanged.

Use the [complete migration/release procedure](MIGRATION_VERIFICATION.md) with
CPython 3.14.7, the wheel hash lock, Gitleaks 8.30.1, and actionlint 1.7.7.
The final receipt must identify the tagged commit and tree, preserve raw scanner
results and exact finding reviews, and report candidate/ref immutability.
The private draft release is the delivery point for those detached receipts and
their SHA-256 checksums. An earlier receipt never verifies a later commit.

The repository remains private pending the separate visibility decision.
Hosted execution remains unavailable/unverified; skipped jobs and startup failures
are not passing tests. Local verification is the advertised reproduction route.
After an authorized public launch, verify anonymous clone access and the documented
task-selection command from a fresh checkout.

## Historical records

Older 20/21/22-task counts and pending-PR descriptions in preserved release records
describe their respective historical snapshots. PR #16 merged on 2026-10-16, and
the schema identifier is now `urn:erdos-99:theorem-state.schema`.
The PR #75-only namespace canary is archived with its exact original bytes;
it no longer creates irrelevant checks on future pull requests.

The two unknown historical working-copy states remain explicitly unknown.
The source provenance archive stays intact.
