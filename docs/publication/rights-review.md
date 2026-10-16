# Rights and clean-history release gate

The Apache-2.0 selection is already recorded. The remaining rights question is
whether the project can grant that license for the retained source expression.
No automated result in this review grants permission or changes a pending
inclusion disposition.

[The grouped inventory](rights-inventory.json) binds each reviewed retained file
to its public SHA256, source commit/blob/SHA256 where available, opaque Git
contributor identity IDs, path history, and one shared provenance group. It covers its
exact `public_candidate`, not later edits. The original review of `afa7f7e`
checked all 808 source inclusion hashes across 12 source pins; no mismatch was
found. Publication-created replacements and CI adaptations are inventoried too.
Two public-only tools, `tools/check_active_route_summaries.py` and
`tools/check_theorem_state_pr.py`, are byte-identical to the pinned source; their
source identities are recorded as unmanifested source evidence pending inclusion
repair. Same-path evidence for other public replacements is a derivation lead,
not an assumption that they are original. Recreate the inventory against the final candidate before accepting sign-off:

```sh
python tools/audit_public_rights.py --source /path/to/private-source-clone --ref RELEASE_SHA --output /private/e99-final-rights.json --private-identities /private/e99-author-map.json
```

This source-only release-engineering audit is optional for a reader of the public
corpus. Mathematical reproduction uses the retained public corpus and never needs
that private clone. An exit code of zero means the evidence hashes/path history
were checked; the printed `OWNER DECISION REQUIRED` remains a release hold.

## What was established

- The included source files have exact checked identities; the inventory groups
  repetitive permission questions. Author labels observed in private Git history
  are represented only by opaque IDs in public artifacts. The optional external
  private map retains the name-to-ID correspondence and keeps IDs stable when
  regenerated. These labels are attribution evidence, not proof that they
  represent separate people or that an account owner holds all rights. Existing
  deliberately credited mathematical authors remain credited in the corpus.
- The pinned private source has contributor instructions but no root `LICENSE`
  or `NOTICE`. Its existing contribution policy does not supply an inbound
  Apache grant for all past contributions. The new public `CONTRIBUTING.md`
  defines prospective submission terms; it does not retroactively clear the
  private archive.
- `NOTICE` and `provenance.md` record the owner's Apache selection and retain
  mathematical attribution. The construction scripts repeat that selection;
  they do not contain independent contributor permission receipts.
- Literature baseline/review documents, the older composite proof manuscript,
  and the Woodall import contain attributed mathematical statements and project
  exposition of external results. They need expression/quotation judgment distinct
  from ownership of project proofs. Inspection found citations and mathematical
  restatements; it did not establish permissions for substantial copied prose.
  Keep load-bearing statements and author credit while resolving any exception.
- Eight localized-CI paths have a concrete additional derivation lead in the
  `NOTICE`-named source proposal `d54097cb`; the inventory records full source
  commit/blob/hash for each. Their adaptation preserves project provenance;
  an attribution sentence alone does not prove that every upstream code fragment
  was owner-controlled.
- `NOTICE` identifies CrocSwap/integer-mult-bounds as workflow inspiration. Its
  [public license](https://github.com/CrocSwap/integer-mult-bounds/blob/d359705715f45a25d46c593a542e8d071c47160a/LICENSE)
  was independently fetched and identified as Apache-2.0. This establishes the
  upstream license offer (blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`,
  SHA256 `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4`), not a claim that arbitrary E99 files originated there.
  No integer-multiplication mathematics was imported by this work.
- There are no imported paper/extraction files in the audited candidate. This
  avoids redistributing the source archive's bundled papers; citations do not
  assign the external authors' rights to E99.

## Smallest owner sign-off

Apply these questions once to the exact final inventory digest, listing only
exceptions by path/group. Do not require 808 repetitive signatures.

1. **Rights confirmation.** Confirm that the retained project-authored material,
   including publication adaptations, is original work you may distribute under
   the already selected Apache-2.0 terms. Using the external private identity map, confirm whether the observed
   contributor and worker/bot identities are your controlled authoring aliases. For any independent
   contributor, employer-owned work, third-party code or substantial quoted prose,
   identify the affected paths and provide the actual permission/license evidence,
   or identify material to replace/exclude while preserving proof dependencies and
   credit. The current manifest remains pending until that factual confirmation
   and exception review is recorded.
2. **Clean destination choice.** Authorize an unused remote for the prepared
   clean-root snapshot, keeping the staging repository private; if the final
   repository must retain the current name, separately authorize the private
   staging rename/new-remote migration. This avoids disclosing inherited Git
   author/committer metadata. No personal email authorization is needed for
   discarded staging history. Final visibility authorization remains a separate
   decision after all release gates pass.

The first answer can clear a grouped original-work disposition only if it supplies
credible ownership/alias facts and identifies exceptions. The second answer does
not clear rights or authorize making any repository public.

## History exposure and implemented remedy

[The redacted history receipt](rights-history-evidence.json) enumerates the
advertised branches, tags and GitHub pull-request head refs in an isolated mirror.
It found 9 unique historical commits with personal-domain metadata in both author
and committer fields: 18 role findings. Email values are intentionally omitted.
This expands the earlier four-staging-commit finding. The mirror's exact observed
refs, heads and timestamp are recorded in the receipt; later safe commits do not
remove earlier objects. Unadvertised retained GitHub objects cannot be proven
absent by a Git ref listing.

The implemented `tools/prepare_clean_public_snapshot.py` creates a **local**
repository with the identical immutable candidate tree, one parentless synthetic
snapshot commit, no remote, no alternate store, and no inherited commit/tag
objects. It copies committed blobs without checkout filters, checks executable
modes/tree identity, counts all objects rather than reachable commits alone, and
runs strict Git integrity checking. It never rewrites the private source or
staging repository. Its synthetic attribution labels an automated export; credit
for mathematics remains in the corpus and `NOTICE`.

```sh
python tools/prepare_clean_public_snapshot.py --source /path/to/public-candidate --ref RELEASE_SHA --destination /private/e99-clean-root
```

Run the full final content/security/rights gate against the resulting clean-root
SHA as well. The tree is identical, while a fresh commit identity is expected.
The exporter is preparation, not permission or a publication operation.

Force-pushing a new root to the current staging repository would leave the
privacy question unresolved because PR refs and retained GitHub objects can
survive branch replacement. A `.mailmap` changes display; it cannot sanitize
stored commit objects. The current staging destination remains private-only
unless affected authors explicitly authorize its metadata or GitHub confirms
complete removal. An unused remote is the prepared conservative path.

## Blocker ledger

| Item | State | Evidence or remaining action |
| --- | --- | --- |
| Exact retained source hashes and contribution grouping | RESOLVED for recorded candidate | Inventory; regeneration command above |
| Pending archive contributor/third-party permissions | OWNER DECISION REQUIRED | First grouped sign-off; inclusion entries remain pending |
| Clean-root export implementation | RESOLVED | Four isolation/preservation regression tests; exact tree and all-object verification |
| Current staging Git/PR-history metadata exposure | OWNER DECISION REQUIRED | Redacted receipt; unused-remote migration or explicit affected-author consent |
| Detecting every possible copied expression/secret | NONBLOCKING as an impossible universal certification | Retain concrete content/security scans and investigate actual findings; never call a scanner legal clearance |
| Visibility | OWNER DECISION REQUIRED | Final explicit authorization only after rights/privacy and technical gates |

No mathematical status, source quantifier, proof dependency or theorem claim is
promoted by these release-engineering changes. Substantial AI assistance was used
for this audit and tooling. Independent human mathematical review remains distinct.
