# Frozen Target C report shard 1

This shard covers source artifact-index positions 0–162 from the frozen 813-path
selector: 163 report paths, lexicographically ordered, at source commit
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree
`e061f039eac44c286a00eacdcaa9a4cbbb877891`). The destination comparison point is
`358af8253f85ab7b9cdbf976ce186ee8426718e4` (tree
`66e596e4da875bab2bbdf4bacac51d17eeb2b466`).

The per-report ledger is [`shard-1-reconciliation.jsonl`](shard-1-reconciliation.jsonl).
It records each source blob and SHA-256, source-index lifecycle, report-internal
status, result and scope anchors, source-local path references, destination
baseline relation, exact destination SHA-256, rights/provenance treatment, and
disposition. Every imported report is byte-identical to the frozen source blob.

## Disposition and authority

All 163 paths were absent by path from the frozen destination tree and are now
integrated as noncanonical research. The source artifact index marks all 163
`unreviewed`, with no claim IDs or dependency/supersession edges. That source
lifecycle is retained; report-internal descriptions such as “proved candidate”
are provenance, not independent destination audits. The shard changes no
theorem-state or publication-authority file. It does not reinstate the withdrawn
global inverse-phase chart or rate.

The ledger does not assert mathematical redundancy from topic overlap. A
stronger-successor or exact-duplicate disposition requires a comparison of the
actual hypotheses, conclusion, constants, and proof scope. No such relation is
claimed here where that comparison has not been established.

## Cross-shard references

The reports mention 61 distinct local source paths. Of these, 34 are present in
the frozen source but absent from the frozen destination baseline. They include
other Target C reports and verifier scripts, so they are recorded as unresolved
cross-shard references rather than copied outside this shard. The exact list,
source/destination presence flags, and report-by-report references are in the
JSONL ledger. The central integration owner must resolve references that are
load-bearing for an active proof or verifier, and can retain the others as
historical citations.

## Rights and verification boundary

The owner’s migration instruction authorizes first-party research and
AI-generated project material. This shard imports the Markdown reports only; it
does not copy third-party papers, PDFs, extracted text collections, or external
attachments. External literature references remain attributed as in source.
The source index does not encode per-file author/license metadata.

For every report, the frozen source commit, source blob object ID, and source
SHA-256 were checked; destination bytes were compared exactly and have the same
SHA-256. No independent mathematical audit is claimed. The reports’ proofs,
conditional hypotheses, and finite evidence remain at their source-stated
scopes.
