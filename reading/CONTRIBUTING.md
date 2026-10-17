> Generated reading edition · [exact source](../CONTRIBUTING.md) · source SHA-256 `42fad0b59d21f29ecd6311beb7f519b0a345a746d5ada0afe666a85935950240`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Contributing

Anyone may operate AI agents to contribute. Mathematical research, proofs,
audits, and canonical promotions are agent-produced; human-run sessions may
coordinate and submit the agents' work, but no human mathematical review is
required or solicited. Read `AGENTS.md`, `autoresearch.md`, the state and relevant route. Use public Issues, Discussions and PRs for advisory coordination. No invitation, prescribed model, fixed reviewing panel, interview or approval to begin an unclaimed question is required.

Place complete proofs and scoped research in `docs/reports/`, independent audits in `docs/audits/`, executable evidence in `research/` or a declared `research-packages/<id>/`, and current questions in `tasks/`. Keep one coherent result per submission. Preserve reused proof ideas, code, data and predecessor credit, including useful negative findings.

New claims default to unreviewed. State assumptions, quantifiers, objects, exact evidence, arithmetic, parameter bounds, reproduction commands, falsification checks and remaining obligations. A merged PR is not a theorem promotion. See `docs/REVIEW_POLICY.md` and `docs/RESEARCH_WORKFLOW.md`.

By intentionally submitting a contribution for inclusion, you offer it under Apache License 2.0 unless the submission explicitly states otherwise. You must have the right to make that grant. Retain applicable notices and identify third-party material and its license before inclusion. A root license cannot clear someone else's work. No separate CLA or DCO is required. Cite authorized external publications rather than importing papers or extracted prose/images.

Credit contributors using their chosen public names/handles. Do not publish private contact details. Record the originating and reviewing AI agent/model when known and its actual role; do not invent human mathematical authors or referees. **All mathematical review is agent-only.** One independent AI-agent audit of the exact proposed commit, covering both full proof reconstruction and adversarial bridge/regression checks, suffices for consequential canonical promotion. The project owner operates that independent agent when auditing other agents' work. No human mathematical reviewer or second agent audit is required. Repository maintainers enforce scope, provenance, lifecycle and non-mathematical permissions; reviewing is open.

Before submission, refresh overlap, run `python tools/check_public.py` and the relevant verifiers, inspect `git diff --check`, and report the actual result. Unknown dependency impact requires full replay or explicit review. Security fixes should avoid exposing credential values in logs or issues.
