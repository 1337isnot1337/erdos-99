# Independent publication audit — current mathematical E99 corpus

**Candidate reviewed:** `1337isnot1337/erdos-99` commit
`b5984940a2258b8e2f58ba54ef6abe3141ab9a12` (2026-10-15).
**Pinned private scientific source:** `1337isnot1337/e-99` commit
`5dcbdc3dfa1f9be370602cc54d50e68eabb88f56`.
**Private source observed afterward:** `eb51394f371aee958b0d9332f80faf75ae694b9e`.

**Release decision: HOLD.** The substantial current corpus is staged and
its *declared* proof/task/source dependency graph is structurally consistent.
This is not yet a defensible assertion that all source rights, privacy,
historical metadata and final public-hosted behavior are cleared. Do not
flip the repository to public solely on the basis of this document.

## What the staged repository actually contains

- 889 committed file blobs at the pinned candidate.
- 804 source-derived retained files in the inclusion manifest: 734 from the
  pinned source main and 70 from ten explicitly pinned research-PR heads.
  The latter comprise 58 live, noncanonical proposals and 12 frozen
  supporting proof/verifier dependencies; **none is promoted by inclusion**.
- 3,959 source paths explicitly excluded. The 734 selected mainline files
  plus 3,959 excluded files account for all 4,693 blobs at the exact pinned
  source main. No mainline source path is lost from that inventory.
- 451 distinct claim IDs, including 372 canonical, 3 audited-working,
  62 regressions, 5 superseded and 9 rejected; 845 declared theorem edges.
- 94 registered finite certificate scripts/entries and 19 substantive
  research-task cards. Every referenced explicit claim prerequisite, named
  proof, audit, registered certificate and task-source path checked in this
  audit exists in the frozen candidate. The retained current Target C
  canonical module list is complete relative to the pinned source manifest.
- No `papers/` or `extracted/` directories, PDF/image/archive binaries,
  symlinks or submodules are present in the pinned committed public tree.
- Inclusion-manifest declared file-dependency edges all resolve and
  `unresolved_dependencies` is an empty array.

**Scope warning:** Structural reachability is not a proof of mathematical
validity, adequate implicit proof dependencies, safe program behavior, or
copyright ownership. The canonical theorem remains open at Level I.
A/B/C-II are open; C-I is closed.

## Independent checks and evidence

1. Compared the pinned source and public Git trees and traced inclusion and
   exclusion inventories as above.
2. Parsed the full published machine proof graph and research task catalogue;
   checked 451 unique claim IDs and 845 graph prerequisites against published
   paths; confirmed no missing explicit theorem, proof, audit, or task path.
3. Examined substantive source-to-public editorial size changes. Of the 804
   imported files, 74 have different recorded source and public SHA256 hashes.
   The largest deliberate condensation is `docs/STATE.md` (a state-navigation
   replacement; the detailed theorem manifest and proof modules are retained).
   The `docs/reports/campaign_ledger_2026-09-09.md` extract retains the
   conditional scalar theorem, nonglobal obstruction and adversarial regression
   sections while omitting historical branch/campaign and repo-status sections.
   This is a structural/content inspection, **not** a full mathematical
   equivalence certification of all 74 edited sources.
4. Independently fetched and SHA256-checked 12 edited proof/audit files against
   their recorded public checksums: 12/12 matched.
5. Independently sampled the README, live A/B/C route maps, source provenance,
   readiness notes, contributor instructions and a major proof manuscript for
   common token patterns, private-source URLs, selected worktree paths and
   email strings: no matches in that sample. The build worker reports a
   separate zero-finding Gitleaks scan and 94/94 local certificate replays.
   Those larger scans and replay results were **not independently rerun**
   by this review.
6. Reviewed the entire reachable list of 12 publication-staging commits;
   four commits have author email metadata using a personal email domain.
   Exact email values are deliberately omitted from this document.
7. Added `tools/audit_public_release.py` and six synthetic regression tests.
   The tool can check **every committed file's** manifest SHA256, restricted
   artifact paths, common credential markers, imported rights-clearance
   dispositions, and author/committer emails when executed against an
   actual local clone. Its test fixtures pass independently under Python 3.12.
   A full local run against the live 889-file candidate has not yet been
   independently executed.

## Release-blocking decisions

**1. Rights and attribution.** All 804 source-derived manifest entries still
say `publication_clearance: pending provenance/content review`. The owner
selected Apache-2.0 for original E99 works, but that selection cannot assign
third-party rights. Obtain a clear owner confirmation that the retained
original works can be distributed under Apache-2.0, identify any contributor
or third-party exceptions, and record exact disposition and notices. Do not
stamp all entries approved based only on a successful automated scan.

**2. Reachable commit metadata.** Four staging commits expose personal-domain
author emails in any future public Git history. Obtain explicit authorization
from the affected author(s) or rebuild the still-private destination as a
clean-root snapshot using author-approved public/noreply metadata. A `.mailmap`
file does not remove emails from existing Git objects. Do not expose the current
history by changing visibility without resolving this decision.

**3. New source delta since selection.** The source advanced 24 new file blobs
after `5dcbdc3d`, including two noncanonical global mathematical reports and
their exact verifiers introduced in private PR #1005, plus CI and preservation
artifacts. The public corpus must evaluate those **by mathematical relevance**:
import scoped new research if useful, or explicitly exclude it with rationale.
No canonical state change was observed in the source transition; this does not
make every new noncanonical report irrelevant.

**4. Final executable and outsider gate.** Rerun the full public corpus
integrity checker, full applicable certificate suite, publication scanner and
three independent fresh-clone A/B/C frontier task sessions against the
**final** release SHA. Hosted Tier 0 remains subject to an actual public-fork
runner canary and cost/namespace review; do not treat a skipped job as green.
The independent mathematical proof-review requirements are separate.

## Hosted CI control correction

The staged public workflow had an unconditional plan-job predicate for any
non-draft PR despite earlier owner instructions to leave hosted rollout off.
The accompanying audit change restores the explicit
`vars.E99_PUBLIC_CI == 'true'` opt-in gate. The Tier 1 replay gate remains
`vars.E99_PUBLIC_PACKAGE_REPLAY == 'true'`. Verify the merged workflow before
allowing public traffic. Do not alter billing or enable paid usage.

## Release checklist for the owner

- [ ] Approve the exact candidate's contributor/source Apache-2.0 rights and notices, or isolate uncleared files without breaking load-bearing proofs.
- [ ] Authorize the visible personal-domain Git commit emails or rebuild/sanitize clean-root history.
- [ ] Decide inclusion of post-baseline noncanonical current-source reports with explicit status labels.
- [ ] Execute the complete local release audit, corpus checker, applicable 94-certificate verification, and at least one A/B/C independent onboarding session each on the final frozen release candidate.
- [ ] Independently inspect the resulting security report and document unresolved exceptions.
- [ ] Confirm any hosted CI/cost settings without requiring blocked checks.
- [ ] Change visibility only after the release gate passes, then verify anonymous clone and task onboarding.

This review does **not** declare the mathematical problem solved, copyright
ownership established, the repo safe for publication, or a new source theorem
canonical. It documents current evidence, exact structural completeness and
the concrete remaining release gates. Update the audit with the final SHA
and results; do not reuse this candidate's conclusions after unreviewed edits.


## Follow-up: current-source PR #1005 reconciliation

A later independent source comparison identified the post-selection additions in `e-99` through `eb51394f371aee958b0d9332f80faf75ae694b9e`. The only substantive whole-source mathematical content newly relevant to the current public frontier consists of two noncanonical reports and their two exact SymPy verifiers. These four files are now included with **byte-identical** Git blobs, SHA256 provenance, noncanonical labels, and visible mathematical limits. The original historical campaign diary and administrative reconciliation audit are not transferred; CI-only and maintenance source changes were already addressed separately.

The inclusion manifest now describes **808** source-derived files: 804 prior entries plus four post-baseline whole-source additions. The inclusion/exclusion partition over the original source snapshot is unchanged; the later files have their own pinned source commit and are not misrepresented as part of the original source tree. The theorem-state version remains `2026-10-10.audit.234`; Level I/A/B/C-II remain **OPEN**, C-I **CLOSED**.

Both newly imported verifiers passed an independently executed Python/SymPy replay in an isolated audit workspace (499 odd-rim incidence cases, 122 exact cyclotomic pairs, the -72 nonplanarity fixture, formal three-phase pairing and two laminate controls). These certify **only** their stated finite/formal claims, not global optimality or a closure theorem.

**The release decision remains HOLD.** The complete final-candidate audit, 808 separate source rights dispositions, historic email authorization/clean-root decision, complete applicable 94-certificate sweep, and fresh-clone outsider A/B/C sessions are not waived by this addition. Current public visibility is still private; do not treat this file as permission to publish an unchecked commit.

## Independent historical-object security hardening

A release red-team exercise found a concrete false-negative in the original local audit: a synthetic credential or restricted PDF **committed and subsequently deleted** was undetected because only the current HEAD tree was inspected. A synthetic unsafe side branch and a secret embedded in a historical Git commit message were similarly outside the scanner's original coverage.

The revised `tools/audit_public_release.py` audits **every commit tree reachable through Git refs**, including deleted/renamed historical paths, all historical-only blob contents within an explicit 8 MB per-blob scan bound, and reachable commit messages. It rejects historical restricted archives or credential markers, historical uninspectable blobs and incomplete object enumeration. It does not echo matched secret values. HEAD-tree, manifest/hash, rights and author-email validation are retained.

All **10 synthetic security/inventory regression tests** passed independently (the original six plus the four new historical-visibility cases) in Python 3.12. This result validates the scanner on those fixtures; it is **not** evidence that the entire final E99 history has been cleared. A full run against the actual final Git clone, including all refs, is still required. This scan cannot establish authorship rights, independent mathematical review, or protection against every possible secret format.

**Publication decision remains HOLD:** imported rights provenance and existing personal-domain Git author metadata need explicit clearance or clean-root rebuilding. The source mathematical corpus and public CI switches are unchanged by this security patch.
