# Contributing

Everyone is welcome to participate through Issues, Discussions and pull requests. No invitation, application, prior relationship or approved-agent status is required. Human and AI contributors may propose tasks, investigate independently, reproduce evidence, audit existing work, explore alternatives, submit counterexamples and report rigorous negative results.

## License and attribution

By submitting a contribution that you intend to be included in this repository, you agree to license that contribution under the repository's Apache License 2.0. You keep your authorship and should include your name or public handle in the contribution record. There is no separate CLA or DCO process.

Disclose third-party material and its license before including it. Prefer bibliographic references and links to publisher, author or institutional pages; do not upload a paper, scan or extracted text merely because it is accessible online. Do not submit private, confidential or personal information.

For AI-assisted contributions, identify the model or tool and version/date when known, describe what it generated or checked, and say which parts were independently verified. Authors remain responsible for correctness, attribution and license compliance.

## Choose and coordinate work

Start with the README, [problem definition](docs/problem.md), [current status](docs/current-status.md) and [task list](tasks/README.md). Search the task ID in open Issues, Discussions and pull requests. A claim issue should give a narrow scope, a concrete first step and an expiry date or release condition. Claims coordinate work; they do not reserve a result. You may start without opening a claim issue if the work is already clearly distinct.

Use Issues for bounded task claims, corrections, counterexamples and actionable review requests. Use Discussions for broad questions, method comparisons and coordination. Anyone may review or comment; no designated reviewer panel is required.

## Submit a result

Open a pull request for a focused change. The template asks for the exact claim, scope, evidence, reproduction, AI disclosure, attribution and review requested. State whether the contribution is author-checked, an unreviewed proposal, conditional, reproduced finite evidence, agent-audited, or human-reviewed. Explain rejected or superseded approaches when that record will help others.

Ordinary contributions may be accepted with an accurate evidence label even when no independent human reviewer is available. This does not make a result canonical. Consequential theorem statements require independent human mathematical review before maintainers promote them. An AI agent cannot serve as a human reviewer.

## Local verification

This repository uses only the Python standard library for its initial checks:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repo.py
python3 scripts/triangular_lattice.py --max-n 5
```

Tests check task metadata, local links and exact finite model output. They do not validate a mathematical proof or establish the full E99 theorem.
