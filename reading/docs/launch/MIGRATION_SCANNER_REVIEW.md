> Generated reading edition · [exact source](../../../docs/launch/MIGRATION_SCANNER_REVIEW.md) · source SHA-256 `7cc4d29927decfb99bdc15975fe73aa4b5ed6044e70ff7b2693835e8fdbb7b06`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Exact mathematical grouping findings

Gitleaks 8.30.1 reports nine `generic-api-key` findings in three migration
assignment files. Each matched value is a mathematical report or verifier stem
stored as a grouping label. An independent agent inspected the exact committed
files and confirmed that these values name research documents or programs.

The reviewed Git blobs are:

| File | Git blob | Full SHA256 |
|---|---|---|
| `agent-1/evidence/source-main-three-way-assignment.jsonl` | `7e465ddb9ff53fb529200531c25844555ac2d4e4` | `c53df5cf13e198f26beffac7def573b62f61cd5d06f78570b64990d310c0cd27` |
| `agent-1/evidence/source-main-three-way-units.jsonl` | `15fc4368898a5dc48c595f7ad7e051156594a5b0` | `a53dbb9cae6e7f5a44a888c9fdea0458e3293da99e98b5b76b43de564afab474` |
| `agent-2/corpus-assignment.jsonl` | `92275d3ca0cd358ad03db1dd0d7e95437dc09d35` | `449d402bd36d5c001e83e08b65f78774074e794bd0fd25febb4f7df5ddeb739e` |

All paths have the prefix `docs/research/migration/2026-10-16/`.
The exact paths, line and column ranges, detector rule, fingerprints, redacted
matches, and mathematical values are registered in
`tools/review_migration_gitleaks.py`.

The release runner retains the original scanner command, complete report, and
raw exit code of one. It records a separate reviewed-finding result only if every
finding has an exact accepted identity. It reads committed bytes with Git
replacement objects disabled and verifies both complete blob hashes. Historical
occurrences must resolve their reported commit and path to the same reviewed
blob. An unchanged mathematical file can therefore retain its disposition across
a later merge, after its exact Git object is checked again.

This review adds no scanner suppression or general field, path, or rule
exclusion. An added finding, changed range, changed fingerprint, other rule,
changed blob, unavailable object, or malformed report remains a failure. The
original narrowly pinned historical negative-test fixture review remains in
force.

The exact recovered source fixture at
`docs/research/migration/2026-10-16/integration/source-main/tools/test_local_ci.py.source`
has Git blob `c613e6d61df45ce818cf3f3d21218e48947d0fa4` and SHA256
`0a54855e41dede9c9a4ace2923f8a1eff2f8c4aec29f7ce00822b17341a23f8a`.
Its two negative-test opening delimiters occupy the detector's exact line range
409–413 and column range 55–88. It contains no closing delimiter or encoded key
payload. This one path and complete blob have their own strict disposition.

The history scanner can repeat a finding for several parent diffs of an octopus
merge. The reviewer derives the exact allowed count from those committed parent
diffs and the matched source lines. An extra or missing occurrence fails; duplicate
reports are never accepted merely because their fingerprints match.

Real-Git regressions include a committed synthetic credential replacement,
additional findings, duplicate reports, changed identities, missing objects,
uncommitted substitutions, two commits with the exact reviewed bytes, a four-parent
merge with three qualifying diffs, and an altered source-fixture payload.
