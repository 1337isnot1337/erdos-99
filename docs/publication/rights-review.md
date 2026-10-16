# Source rights and publication provenance — Gate 1

**Gate 1 project-controlled rights: owner authorization received and recorded.**
This is a scoped copyright/provenance decision, not a technical-release receipt,
a legal warranty that every sentence is original, or authorization to make the
repository public. **Publication remains HOLD** pending Gate 2 (verification of
the actual release commit) and Gate 3 (explicit visibility approval).

The controlling machine-readable owner declaration is
[`owner-rights-authorization.json`](owner-rights-authorization.json),
which pins the **exact Git blob** of
[`inclusion.json`](inclusion.json) (`96df5a7db05e8b65e8bca605a770d0b09ab27596`).
The owner provided a blanket grant for all **810 included files** developed
through the owner's AI agents. That statement is retained as an
[owner-authored GitHub record](https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207244081):
"all of those 810 are all work i have done with my AI agents. i authorize anything done with them."
The project already chose Apache-2.0 for expression within its rights. No
individual permission from the AI tools is a required release gate.

On 2026-10-16, the owner separately authorized publication and reuse of their
first-party research and AI-agent-generated material in the frozen Target C
migration. The coordinator recorded that instruction in
[`first-party-migration-authorization.json`](first-party-migration-authorization.json),
which covers 813 frozen reports and 21 supporting files (834 unique source
paths) through an additive rights ledger. Four support paths were newly
imported in the coordinator support batch; 17 had already been integrated and
retain their individual provenance rows. This authorization is separate from
the 810-entry inclusion manifest, does not grant rights to independently owned
expression, and is a coordinator record of the owner's instruction rather than
a signed owner statement.

The previous owner-attested inclusion-manifest blob was
`f521850703b01b204399613d640a0b99ca895080`. The current blob has the same 810
public paths, source commit and 12 source pins. An exact entry comparison found
eight records changed only in `public_sha256` and/or `editorial_change`; their
source paths, source commits, source blobs, source hashes and public paths are
unchanged. The release auditor checks this comparison against the prior blob
and requires the exact current blob above.

## Exact evidence and disposition

At reviewed commit `1d0345edf011961be67425b3a5d2f6be8e0a29f7`
(tree `5306421c024728fb2892ba17ee62a9b0c1760d00`),
the manifest contains 810 distinct imported records from **12 source pins**.
An independent GitHub-object cross-check compared each manifest source
path, blob SHA and mode against its exact recorded source commit:

| Item | Observed |
| --- | ---: |
| Imported entries present in publication tree | 810 / 810 |
| Entries with matching pinned source path, blob and mode | 810 / 810 |
| Source entries byte-identical to publication Git blob | 726 |
| Publication-modified entries (source and publication blobs differ) | 84 |
| Known original-versus-public executable mode corrections | 4 |
| Current tracked regular files (including publication-only files) | 918 |
| Restricted paper PDFs or other forbidden binary archive formats present | 0 |

The 84 differences are **not** evidence that original authorship changed:
the manifest explicitly records publication edits, source identities, and
resulting public hashes. The four mode changes were documented during
release preparation. The earlier release engineer's local candidate
verified all 810 source/public SHA256 records and 4,793 versioned source
records; the current GitHub cross-check verifies source blob identities
but is **not** a replacement for Gate 2's current-commit content-hash
and immutable-checkout replay.

The earlier committed
[`rights-inventory.json`](rights-inventory.json) is a **historical**
808-source-entry, 902-total-file inventory from
`b734ed1a7b095ed9791159f53170fa7182d3c7fa`.
It must not be mistaken for the final 810-entry inventory.
The detached release agent reported a later 810-entry/917-file inventory
with 43 groups at `30af2cca`; it is not available inside this repository.
The current 918-file tree includes subsequent publication changes.
Owner authorization therefore binds to the *exact 810-entry inclusion
manifest*, independent of a stale supplemental grouping report. Rebuild
the all-file rights inventory if a subsequent release task needs current
per-file Git history, without manufacturing an alias map.

**Disposition:** owner-controlled original project expression in these 810
imported records is authorized for publication and redistribution under
the project's existing Apache-2.0 selection. Preserve all credited
contributors, cited mathematicians, licenses and source-specific notices.
This disposition relies on the owner's factual representation about
their project and agents; commit author strings by themselves neither
prove ownership nor identify independent rights holders.

## Specific external-expression review

Five publications-related paths were examined as distinct from
project-origin reports:

- `docs/literature_review.md`
- `docs/problem/literature_baseline.md`
- `docs/problem/literature_archit_das_stress_rhombic_audit_2026-10-08.md`
- `docs/reports/erdos_problem_99_1.6.0.md`
- `docs/reports/target_c_woodall_diameter_topology_2026-09-10.md`

They contain bibliographic references, analysis, theorem restatements
and project arguments. **No third-party paper PDF/extraction is retained.**
The Woodall document attributes the imported graph-classification theorem
to Woodall and the Collins–Roberts account. The large older composite
report contains links and self-contained research exposition; this audit
does not assert a line-by-line similarity comparison against every
cited paper. Facts and equations can be restated with proper attribution;
third-party original prose, figures, or code would need a compatible
license, permission, or replacement if substantial copying is found.

The eight localized-CI paths inventoried in
`tools/audit_public_rights.py` were inspected. Their stated
adaptation source is the owner-operated `e-99` proposal
`d54097cb96b1c5fcbb6eca57843b53e7b8a6dd2e`.
The `NOTICE` separately attributes workflow inspiration to
[CrocSwap/integer-mult-bounds](https://github.com/CrocSwap/integer-mult-bounds),
whose upstream license was checked as Apache-2.0 in the earlier audit.
That reference does not establish direct source-code copying; this
inspection found no concrete conflicting third-party license claim.

**Exception ledger:** no specific non-owner material requiring separate
redistribution permission has been identified in the focused review.
This is not a guarantee that automated or manual review can find every
possible copyright overlap. If one is identified, determine the
relevant source license or replace/exclude the expression while retaining
mathematical dependencies.

## Existing Git-history privacy decision

The owner accepts publication of their own `cinnajdavis@gmail.com`
Git author/committer email, as
[recorded on PR #9](https://github.com/1337isnot1337/erdos-99/pull/9#issuecomment-6207434631).
A separate live review on 2026-10-15 traversed **47 Git commits reachable
through 22 advertised refs** and observed no other personal-domain email,
only that address and standard GitHub `noreply` variants. The expanded
migration history was audited on 2026-10-16 with all advertised PR-head refs
fetched. It contains one additional distinct non-noreply identity with 14
author/committer occurrences. That identity has no owner authorization
recorded and remains a release blocker; no
email addresses are reproduced here, and public history has not been rewritten.
It does **not** promise that GitHub retains no unadvertised objects,
nor waive actual credential or non-email privacy findings.
The owner wishes to keep the current `1337isnot1337/erdos-99`
repository and its pull-request history.

## Remaining technical and approval boundaries

1. **Gate 1 owner declaration:** the prior declaration remains scoped to the
   810-entry inclusion set; the 2026-10-16 instruction and additive record
   separately cover 813 frozen Target C reports and 21 support files. No known
   third-party redistribution exception was identified. The root license and
   owner instruction cannot relicense independently owned expression.
2. **Gate 2 technical receipt:** required on the actual final `main`
   commit. The older full 94-certificate/109-tool/8-corpus receipts
   belong to their pinned earlier trees. The manifest retains historical `publication_clearance: pending ...`
   annotations. The release auditor now **explicitly checks the separate
   Git-blob-pinned owner attestation**, preserving default failure for a changed
   manifest, unapproved email, or declared external-rights exception.
   Gate 2 must rerun the complete release suite at the final commit; this
   scoped authorization never changes mathematical metadata.
3. **Hosted CI:** account infrastructure has not executed a canary;
   disclose this limitation. Local verification can establish its
   own separate tested scope.
4. **Gate 3 visibility:** only a separate explicit owner instruction
   can make the repository public. This declaration alone is not it.

Historical scanner findings and stale 808-file "OWNER DECISION REQUIRED"
entries are evidence of *earlier* audits, not proof the present owner
has withheld permission. New evidence must still be checked at its own
commit and tree; no license statement proves theorem validity.
