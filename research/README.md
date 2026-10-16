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

## Additional noncanonical whole-source verifiers

Two source-identical formal/global-obstruction reports postdate the pinned canonical corpus and are available through [current research proposals](../docs/research/proposals.md). They do **not** add to the 94 registered theorem certificates and must not be treated as canonical premises.

With SymPy 1.14.0 from the pinned verification environment, run:

```sh
python3 research/verify_global_separable_distortion_obstruction.py
python3 research/verify_global_joint_phase_compatibility.py
```

The first checks finite odd-rim incidence and Möbius identities, including a nonplanarity fixture. The second checks formal stress/strain identities and both fixed-frame and rotated-laminate tests. Neither establishes global optimality, source-field extraction, or the Level I conjecture.

## Source PR #1008 population-reserve candidate

The [unreviewed report](../docs/reports/population_reserve_independent_reconstruction_2026-10-15.md)
gives a twelve-arc boundary construction and its all-real-radius averaging
proof. Its exact-constant and finite-geometry checker is
`python3 research/verify_population_reserve_twelve_arc_2026_10_15.py --extended
--output /tmp/population-reserve-twelve-arc.json`; the committed fixture is
`research/population_reserve_twelve_arc_2026_10_15.json`. The checker does not
certify the analytic averaging theorem, literature priority, or global
optimality. The candidate registry records its exact claim, source hashes,
validation, canonical comparators, and missing Target C implication. This
script is noncanonical evidence and is intentionally not added to the registered
theorem-certificate set.
