# Contributing

For an open-ended session, use [autoresearch](autoresearch.md): check existing
handoffs before drawing a card, inspect source-bound coverage and leave one useful
result or precise next action. Keep one investigation thread; no separate session
report is required. The [package guide](docs/research/research-package-guide.md)
offers an optional scaffold with an **Open next questions** section.

Authorized maintainers use [delta-only intake](docs/research/pr-intake.md), the
exact-head ledger and persistent scheduling cache. [Archive intake](docs/research/research-archive-intake.md)
preserves isolated sources with scientific obligations still open. Publication,
scope verification and canonical promotion remain separate decisions.

Anyone may operate AI agents to contribute. Mathematical research, proofs,
audits, and canonical promotions are agent-produced; human-run sessions may
coordinate and submit the agents' work, but no human mathematical review is
required or solicited. Read `AGENTS.md`, `autoresearch.md`, the state and relevant route. Use public Issues, Discussions and PRs for advisory coordination. No invitation, prescribed model, fixed reviewing panel, interview or approval to begin an unclaimed question is required.

Place complete proofs and scoped research in `docs/reports/`, independent audits in `docs/audits/`, executable evidence in `research/` or a declared `research-packages/<id>/`, and current questions in `tasks/`. Keep one coherent result per submission. Preserve reused proof ideas, code, data and predecessor credit, including useful negative findings.

New claims default to unreviewed. State assumptions, quantifiers, objects, exact evidence, arithmetic, parameter bounds, reproduction commands, falsification checks and remaining obligations. A merged PR is not a theorem promotion. See `docs/REVIEW_POLICY.md` and `docs/RESEARCH_WORKFLOW.md`.

By intentionally submitting a contribution for inclusion, you offer it under Apache License 2.0 unless the submission explicitly states otherwise. You must have the right to make that grant. Retain applicable notices and identify third-party material and its license before inclusion. A root license cannot clear someone else's work. No separate CLA or DCO is required. Cite authorized external publications rather than importing papers or extracted prose/images.

Credit contributors using their chosen public names/handles. Do not publish private contact details. Record the originating and reviewing AI agent/model when known and its actual role; do not invent human mathematical authors or referees. **All mathematical review is agent-only.** One independent AI-agent audit of the exact proposed commit, covering both full proof reconstruction and adversarial bridge/regression checks, suffices for consequential canonical promotion. The project owner operates that independent agent when auditing other agents' work. No human mathematical reviewer or second agent audit is required. Repository maintainers enforce scope, provenance, lifecycle and non-mathematical permissions; reviewing is open.

Edit documentation, tooling and research normally through Git. Migration checkers have been deleted. Historical import records impose no source-clone, hash-refresh or ledger-update requirement.

Linux is not required to contribute or run ordinary checks. Follow the Windows,
macOS or Linux setup in `README.md` and use
`tools/requirements-verification.lock`. The optional isolated package replay
backend needs Linux and Bubblewrap. Tests for that backend report a skip when
its runtime or isolation capabilities are unavailable; record those limits with
your results.

Before submission, refresh overlap, run `python tools/check_public.py`, inspect `git diff --check`, and report the actual result. Run tests for changed behavior and the new or changed verifiers and experiments needed to support your contribution. Contributors are not required to replay the repository-wide theorem-certificate suite. Report any required full replay as **deferred to the merging agent**, including unresolved mathematical dependency impact; this does not claim full verification or block submission of an otherwise reviewable PR.

The merging agent resolves verification scope and performs any required full suite on the final integration candidate before merging, recording the tested commit/tree, environment, commands and results. An ordinary prose or workflow edit still needs only structural checks; a declared mathematical input cannot use that exemption. See [verification ownership](docs/ci/README.md#verification-ownership). Security fixes should avoid exposing credential values in logs or issues.
