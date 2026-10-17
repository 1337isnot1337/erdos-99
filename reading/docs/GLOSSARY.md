> Generated reading edition · [exact source](../../docs/GLOSSARY.md) · source SHA-256 `34c82a498756ec183af62e1e0c682bc0b5c62529dde3d4ea4e6b9d093d39bb6f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Glossary

Short definitions for terms used throughout the E99 repository. Route-specific notation and hypotheses live in the [problem statement](problem/statement.md), [state lock](STATE.md), and the relevant route map.

| Term | Meaning in this repository |
| --- | --- |
| **Unit-separated configuration** | A finite point set in the plane in which the distance between every two distinct points is at least `1`. |
| **`D(n)`** | The minimum diameter among unit-separated planar configurations with `n` points. |
| **Global minimizer** | An `n`-point unit-separated configuration whose diameter equals `D(n)`. This is stronger than being locally optimal under small motions. |
| **Unit-contact graph** | The graph whose vertices are the points of a configuration and whose edges join pairs at distance exactly `1`. A unit equilateral triangle is a triangle in this graph. |
| **Level I** | The project’s full conjecture: for all sufficiently large `n`, every global minimizer contains a unit equilateral triangle. A disproof requires triangle-free global minimizers for an unbounded sequence of sizes. |
| **Target A** | The source-capacity and Schur-response proof route. Its global endpoint is the rank/deficit inequality recorded in the state lock. |
| **Target B** | The rhombic shell-stability proof route. It seeks the joint global inequality recorded in the state lock and Target B route map. |
| **Target C** | The KKT force-geometry and reciprocal-rigidity proof route. C-I is closed; C-II is open. |
| **Contact-isolated point** | A point with no incident edge in the unit-contact graph. In Target C source-population arguments, such a point remains part of the full source and must not be discarded just because it is outside the positive-contact core. |
| **Canonical** | A claim explicitly promoted into the active theorem state with its approved scope and dependencies. |
| **Audited-working** | Research independently audited for a stated purpose but not promoted as a canonical theorem premise. |
| **Conditional** | A claim whose conclusion depends on additional hypotheses that must remain visible. |
| **Regression** | A counterexample or obstruction that rules out a proposed inference or stronger claim in its stated scope. |
| **Unreviewed** | Research material not yet audited or promoted; it is a lead, not an established premise. |
| **Superseded / rejected / provenance** | Respectively: replaced by a later result; found invalid in its stated form; or retained as historical record. These labels do not make material useless, but they do not make it a current theorem premise. |

The status labels are controlled by [`docs/STATE.md`](STATE.md) and [`docs/state/theorem-state.yaml`](../../docs/state/theorem-state.yaml). See the [newcomer guide](START_HERE.md) for how to use them when choosing a research task.
