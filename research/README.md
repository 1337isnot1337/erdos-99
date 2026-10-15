# Reproduce the current evidence

The [registry](certificates.json) lists all 94 inherited registered certificates, their exact claim IDs, mathematical source statements/scopes and commands. Sources, helpers and fixtures are in this directory. Run from the repository root with assertions enabled; `python -O` would disable checks in these inherited verifiers and is not a valid replay.

```sh
python3 -m venv .venv
.venv/bin/pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock
.venv/bin/python tools/run_theorem_certificates.py
```

The locked wheel set targets CPython 3.14 / Linux x86_64. Portable version pins are in `tools/requirements-verification.lock`. Full replay is explicit Tier 2. Individual scripts retain exact rational, symbolic, interval or numerical diagnostic arithmetic and parameter bounds. Read each source/output and its linked proof before relying on it; the registry does not turn a diagnostic into an exact theorem.

Locally reproducible, independently reimplemented, and mathematically reviewed are separate properties. An inherited agent audit is not human review. The [verification record](../docs/launch/READINESS.md) reports actual commands/outcomes. A finite certificate proves only its encoded proposition and supplies no missing source-realization/global-optimality implication.

Use `python tools/task_context.py TASK-ID` to list the chosen task's transitive certificate prerequisites. New evidence packages include exact inputs, arithmetic, bounds, environment, commands, inspectable output, negative controls and explicit limitations. New proposal scripts outside the canonical registry remain unreviewed.
