# Research review and theorem promotion

This policy separates checking a contribution from deciding whether it changes the
canonical theorem stack. The repository's [state lock](STATE.md),
[research workflow](RESEARCH_WORKFLOW.md), and target routes govern mathematical
authority. A PR, review, merge, certificate pass, or discussion post does not by itself
make a theorem canonical.

## Review the claim at the right level

Reviewers first identify what the submission asks the repository to accept:

1. **Artifact or workflow change.** Check whether the files, links, and commands work;
   inspect security and provenance implications where relevant.
2. **Computational evidence.** Reproduce the claimed run or inspect the exact/certified
   checker, inputs, arithmetic, and failure controls. State precisely what the
   certificate establishes and what it omits.
3. **Mathematical result or audit.** Check the full statement and proof against its
   definitions, dependencies, quantifiers, geometry, regressions, and applicability.
   Verify that a local, finite, scaffold, or arbitrary-packing result is not used as a
   theorem about every global minimizer without a proved bridge.
4. **Canonical promotion.** In addition to the mathematical audit, verify the promotion
   transaction and generated views required by `CONTRIBUTING.md` and
   `docs/RESEARCH_WORKFLOW.md`.

Review only the exact commit recorded in the PR. If the head changes materially, review
the new commit and state which earlier findings remain applicable. Review comments
should identify a file and statement, exact step, counterexample, missing hypothesis, or
reproducible failure. “Looks right” and a passing test suite are not mathematical audit
records.

## Ordinary research submissions

Exploratory reports, independent checks, computational tools, and negative results can
be merged as useful research artifacts without moving the frontier. Reviewers check
scope and provenance in proportion to the claim and record the appropriate lifecycle
classification: unreviewed, audited-working, conditional, regression, superseded, or
rejected. If no proof audit was performed, say so; merging the artifact does not silently
upgrade its status.

Preserve a partially correct result by isolating the proved statement from the failed
extension. Preserve a false or overstrong statement when it documents a useful exact
regression; mark the failed claim and its scope instead of deleting its history. When
work duplicates a predecessor, retain independent verification and explain exactly
what was checked. When it is superseded, link the replacement and retain any distinct
counterexample or limitation.

For a substantive new mathematical claim, use an independent reviewer who did not
produce the submitted proof or checker. A second review is especially useful when the
claim relies on delicate quantifiers, geometry, a literature import, or a load-bearing
certificate. Record reviewer identity, exact head commit, scope checked, commands or
proof steps inspected, and unresolved issues in the PR or linked audit. External peer
review must not be implied by internal review.

## Canonical promotion gate

Frontier-changing promotion is intentionally demanding. Before merge, the default
standard is two independent mathematical reviews by people other than the proof's
authors: one checks the complete proof and exact hypotheses end to end; the other
independently checks the central bridge, scope, dependencies, and relevant regressions.
At least one reviewer should have the subject expertise needed for the argument. For a
small claim with a short proof, the maintainers may make both reviews concise, but they
should retain two distinct checks. If that review capacity is unavailable, leave the
claim noncanonical and the PR open or merge it only as a clearly classified artifact.

The author must provide:

- the exact proposed theorem and its canonical objects, with all global or finite
  quantifiers stated;
- every theorem ID and nontrivial dependency, with status and source path;
- the complete proof or auditable proof module, not only a sketch or report summary;
- predecessor comparison, including the nearest failed and superseded variants;
- route-relevant regressions and explicit scope limitations;
- exact certificates and reproduction commands for load-bearing computation;
- the complete same-change state transaction: version, human state, route/current
  frontier, prompt if needed, dependency edges, certificate registrations, and generated
  views;
- author, contributor, source, and AI-assistance disclosures.

Reviewers independently check the proof; do not divide the argument into pieces and
assume the pieces compose unless the shared objects and interfaces are verified. The
review record must point to the reviewed commit and name any unchecked subclaims. The
maintainer then checks that the state transaction is complete and that the theorem-state
validator, relevant certificates, generated artifacts, and repository checks pass.
These mechanical checks establish repository consistency, not proof truth. Promotion is
complete only when the explicit state update is merged; report wording alone cannot
promote a claim.

## Attribution, conflict, and responsibility

Reviewers should check that reused proof ideas, code, data, and literature have accurate
source attribution and that the PR identifies predecessor work. Acknowledging a
contributor preserves credit without automatically assigning coauthorship. Before a
joint publication, its authors should discuss roles and authorship directly. Substantial
AI assistance must be disclosed with the tool/model when known and the work it performed.
Human contributors remain responsible for the correctness, scope, and provenance of the
submitted content.

Reviewers with a direct contribution to the result should disclose it and not count as
an independent reviewer for that result. A reviewer may ask for narrower claims, a
separate regression, or a handoff instead of rejecting an otherwise useful artifact.
The maintainer should record unresolved disagreements and avoid resolving a mathematical
dispute by authority alone; seek another independent check or retain both scoped
positions until the issue is resolved.


## Open participation and review identity

Participation and review are open; no fixed panel is required. Consequential canonical promotion requires independent human mathematical review. Agent audits are useful evidence and must be labelled as agent audits. Inherited canonical status is preserved as the source ledger's accepted state; it is not a retroactive assertion of independent human peer review. Maintainers enforce the distinction.
