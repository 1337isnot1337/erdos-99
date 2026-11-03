# Publication verification and remaining obligations

Scope: an isolated text research archive under this directory, plus the four
generated reading-edition mirrors and their navigation manifest required by the
repository's structural checker. The source was a
non-Git directory; its identity is the complete original-byte inventory and
the source-tree digest recorded in [inventory.json](inventory.json). No source
commit was invented. The upstream import base is
`b05cd57b15252fe99577de3edb0b73070e79544f`.

The following checks were performed during export:

- Compared all 4,853 original file paths, byte lengths and SHA-256 hashes,
  including every omitted input, against the inventory.
- Verified the forty payload shard hashes, inventory shard hashes and all 4,731
  unique published files reassembled from their ordered fragments,
  their per-record bytes/hashes, safe paths, complete source-to-export mapping
  and explicit omission reasons. Source scripts remain inert text.
- Ran a bounded privacy/credential scan over the decoded published content.
  The actual transformations were 3,108 private-home-path replacements and
  three embedded third-party-source omissions across 1,759 transformed files.
- Parsed all 308 archived Python source files without execution: no syntax
  errors. All included `.json` records parsed. No historical script, proof
  certificate or research launcher was executed as part of these checks.

Machine-readable results are [validation.json](validation.json) and
[export-report.json](export-report.json). The standard-library
[verifier](verify_snapshot.py) repeats the archive integrity checks; the optional
original-source comparison requires access to the private source directory.
The checked archive has no dependency on that directory for ordinary reading
or hash verification. The builder records the transformation policy. Git pins
the publication metadata and both scripts; the input inventory separately pins
the historical source.

Repository structural checks, the localized impact plan, overlap search and
release scan are recorded in the accompanying pull request with actual
commands and results. This document does not pre-assert their outcome.

Scientific review remains **partially_reviewed**. Syntax, hashes, file recovery,
privacy scans and a successful structural checker do not prove a mathematical
claim. Newly recovered worker answers have not received a new proof audit.
Historical computation outputs retain their original precision, local/global
limitations, failed attempts and missing dependencies. No all-optimizer
globality certificate or unrestricted asymptotic theorem is supplied.

Any repository-wide mathematical/certificate replay required by the localized
planner is **deferred to the merging agent**, not reported as passed. There is
no canonical promotion, exact-head mathematical approval or theorem-state
transaction in this contribution. Open scientific obligations and a feasible
next action are listed in [PROGRESS.md](PROGRESS.md).
