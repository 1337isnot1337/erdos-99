# Research review and theorem promotion

This policy separates checking a contribution from deciding whether it changes the
canonical theorem stack. The repository's [state lock](STATE.md),
[research workflow](RESEARCH_WORKFLOW.md), and target routes govern mathematical
authority. A PR, review, merge, certificate pass, or discussion post does not by itself
make a theorem canonical.

**Permanent project policy: mathematical research, proof auditing, and canonical
promotion are performed exclusively by autonomous AI agents. No human mathematical
reviewer, referee, expert panel, or human approval is required or requested.**
One independent agent audit is required for consequential promotion; they are identified as *agent reviews*,
never misrepresented as human peer review. Review independence, mathematical validity,
and explicit theorem-state promotion remain mandatory.

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

For a substantive new mathematical claim, assign a separate reviewing AI agent that
did not produce, edit, or verify the submitted proof or checker. Use an isolated
session/context with the exact immutable PR-head SHA and its own audit notes.
Independent review means a genuine separate investigation, not a second prompt
summarizing the proposing agent's output or a self-review with a new title.

Record the reviewing agent/session identifier, model when known, exact commit,
scope, source inputs, proof steps checked, reproduction commands and outputs,
counterexample attempts, and unresolved obligations. If any reviewer contributed
to the proof or checker, disclose that overlap and do not count the review as
independent. A changed substantive head requires a fresh scope-aware review.
Internal agent review is not external human peer review; never claim otherwise.

## Canonical promotion gate

Frontier-changing canonical promotion requires **exactly one independent AI-agent
mathematical audit** of the proposed theorem at the exact PR-head commit, before
the promotion transaction is merged. There is **no human mathematical review**
requirement and no second reviewer requirement. The project owner may initiate
and operate the independent reviewing AI agent to audit other agents' work;
using the owner's GitHub account to submit the audit does not invalidate
independence.

The one reviewing agent must combine both responsibilities in **one substantive
audit**:

1. **Full proof reconstruction:** independently check the exact statement,
   definitions, hypotheses, every global/finite quantifier, the load-bearing
   dependency chain, literature inputs, and all steps in the complete proof.
   Where practical, derive the crucial step before reading the proposed proof.
2. **Adversarial bridge and regression testing:** actively try to falsify
   the decisive implication, identify missing hypotheses, replay relevant exact
   verifiers, test known counterexamples, and challenge any transfer from
   finite/local/scaffold evidence to a universal statement about minimizers.

The reviewer must be an AI-agent session independent of the originating proof
and checker, with genuinely fresh mathematical inspection. The operator may
be the same project owner supervising multiple agents, but the review may not
be a self-check by the agent that authored the theorem. Different model
families, multiple reviews, and a separate human mathematical referee are not
required. A CI pass, autogenerated summary, or bare GitHub approval does not
count as this audit.

The reviewer issues a documented PASS, CONDITIONAL, or FAIL, with an exact
head SHA, agent/model when known, proofs and code examined, tests actually
run, scope, counterexample attempts and limitations. A FAIL or unresolved
load-bearing gap prevents canonical promotion until the submitted result is
repaired and the **single independent agent audit** is updated or repeated.
A follow-up audit needed to resolve failure is a correction, not a default
second-review requirement. Agent-maintained repository controls may merge
validated promotion transactions, but a merge alone never establishes
mathematical authority.

The author must provide:

- the exact proposed theorem and its canonical objects, with all global or finite
  quantifiers stated;
- every theorem ID and nontrivial dependency, with status and source path;
- the complete proof or auditable proof module, not only a sketch or report summary;
- predecessor comparison, including the nearest failed and superseded variants;
- route-relevant regressions and explicit scope limitations;
- exact certificates and reproduction commands for load-bearing computation;
- the complete same-change state transaction: version, readable state, route/current
  frontier, prompt if needed, dependency edges, certificate registrations, and generated
  views;
- exact originating/reviewing agent identities and model versions when available,
  contributor credit, proof/code/data provenance, external sources, and AI-assistance disclosure.

Reviewers independently check the proof; do not divide the argument into pieces and
assume the pieces compose unless the shared objects and interfaces are verified. The
review record must point to the reviewed commit and name any unchecked subclaims. The
maintainer then checks that the state transaction is complete and that the theorem-state
validator, relevant certificates, generated artifacts, and repository checks pass.
These mechanical checks establish repository consistency, not proof truth. Promotion is
complete only when the explicit state update is merged; report wording alone cannot
promote a claim.

## Attribution, conflict, and responsibility

Auditing agents check that reused proof ideas, code, data, and literature have
accurate attribution and rights metadata. Preserve credit to actual contributors
and sources; do not invent human proof reviewers, human authorship, or external
validation. Record the model/agent involved and its mathematical or coding role
when identifiable. Authorship of any later publication is a separate legal and
editorial question; a proof audit never grants copyright or redistribution rights.

An agent that originated, edited, or supplied a load-bearing component cannot
count as an independent mathematical reviewer of that result. A reviewing agent
may request narrower claims, a separate regression, or a bounded handoff rather
than giving an unsupported PASS. The integrating agent records disagreements and requests a corrected proof or
further investigation by the independent reviewer, retaining conditional or
noncanonical claims while material disputes remain unresolved.

All mathematical review and promotion decisions use the agent-only process.
Repository account owners still control visibility, licensing, permissions, and
legal rights; automation cannot assert third-party permission or release consent.

## Autonomous research governance

Keep main protected by required PRs, trusted state/integrity checks, and an
appropriate controlled merge mechanism. Request **agent review artifacts** for
changes to active theorem modules, load-bearing certificates, or canonical
dependencies. Consequential mathematical promotions use the single-agent audit gate
above even if GitHub's native approval mechanism cannot represent an independent
reviewing agent session. An automatically applied GitHub "approved" label is not evidence
of proof verification. Human approval is never a mathematical promotion gate.

Allow open autonomous contributions and independent audits without invitations,
a fixed panel, or any human mathematical sign-off. Assign narrow merge permissions
to accountable automation/maintainer identities and preserve auditable SHA-bound
review records. No specific proprietary model is required. Be explicit when the
available review capacity is insufficient; leave the result unreviewed rather than
waiving the gate.

Security checks, third-party license obligations, contributor consent, account
ownership, and authorization to make a private repository public are distinct
from mathematical review and are not silently waived by this policy.

This document itself does not change repository visibility, access-control
settings, CI billing, release permissions, or licensing.

