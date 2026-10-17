# global-joint-phase-source-extraction

**Investigation:** `global-joint-phase-source-extraction-current-20261017`. **Status:** open. Source: `e396ea07887dd0528b817ce4e656ff0e6b01f8fb`.

Downstream use: Name the downstream claim or decision this result can change, the exact quantity it controls, and the remaining hypothesis before extending the investigation.

**Track / priority:** alternative-approach / exploratory whole-source frontier; selection weight 3 (attention only).

## Exact objective

For an **arbitrary sufficiently large triangle-free global minimum-diameter configuration**, can the discrete source geometry be converted into a globally compatible, bounded strain field $F$ and divergence-free stress field $S$ in **one controlled material reference frame**, with grain rotations, seam jumps, boundary work, inactive pair constraints and all source labels accounted for? Either prove a rigorous source-extraction and strict same-cardinality diameter-improvement implication, or produce a precisely scoped counterexample to a proposed extraction lemma.

This is an exploratory route, not a canonical reduction. Proving field-phase rigidity only for a chart supplied as an additional hypothesis is not the objective.

## Definitions, hypotheses and complete prerequisites

- [Exact Level I statement](../docs/problem/statement.md): every global minimizer, eventual quantifier, actual source cardinality
- [Authoritative theorem state](../docs/state/theorem-state.yaml): Level I remains open, and no independent continuum source-extraction theorem is promoted
- [Shared local structure](../docs/theory/01-local-structure.md): inspect the canonical contact/diameter constraints and actual source geometry
- [Target C current frontier](../docs/targets/target-c/CURRENT.md): contact isolates, mixed stress scope, and finite versus infinitesimal source realization
- [Global joint stress/strain phase mechanism](../docs/reports/global_joint_stress_strain_phase_mechanism_2026-10-12.md): **unreviewed, noncanonical** formal candidate and counterexamples
- [Global separable-distortion obstruction](../docs/reports/global_separable_distortion_obstruction_2026-10-12.md): **unreviewed, noncanonical** transformation obstruction and planar-realizability warning

Use exactly the boundedness, periodic/zero-trace boundary conditions and common-frame hypotheses in the joint-phase report. In phase $i$, $S_i$ is supported on two triangular directions, and $\operatorname{sym} F_i=t_i E_i$ with $t_i>0$. The formal cross-phase product is negative only when stress and strain are expressed in the **same** material frame. Independently rotated grains can admit a compatible laminate even when each local phase looks favorable.

The reports are proposed mathematical arguments, not audited canonical dependencies. Independently reconstruct any report lemma before using it in a new theorem.

## Relation to Level I

A successful global result must apply to all sufficiently large triangle-free **global** minimizers and force a unit equilateral triangle or a same-cardinality unit-separated planar configuration of diameter strictly below $D(n)$. Formal fields, infinitesimal strains, approximate densities and nonglobal examples cannot close the question by themselves.

## Existing obstructions

- A positive stress-only rank-one laminate can have isotropic mean and correct determinant mean despite different missing directions.
- An independently rotated pair of positive phases can share stress and have a rank-one-compatible strain jump.
- A finite or cut grain chart can carry boundary and internal seam work; small seam length alone cannot bound its normalized contribution.
- Field norms may become unbounded, stress/opening amplitudes may degenerate, and source contact isolates must remain included.
- Even a single-grain field conclusion would leave the strict source competitor or unit-triangle implication open.
- Separable vertex-distance transformations are exactly Möbius/anti-Möbius when planar-realizable, and full incidence-marginal certificates can block improvement; formal factor improvement may not be planar-realizable.

## First bounded experiment and falsification

Choose one proposed discrete-to-continuum extraction rule for a **two-grain finite source**. State its scale, geometric interpolation, orientation frame, $F/S$ bounds, exact lower unit-separation constraints and all actual diameter-pair tests.

Compute the seam jump/traction and resulting boundary work before discarding any interface. Stress-test against the report's independently rotated laminate and the odd-rim nonglobal full-source family. If the extraction silently changes material frame or allows source labels to vanish, exhibit the exact failure and stop. A proof-only path can instead independently verify the periodic double-integral argument and derive the required quantitative bounds, identifying the precise missing source hypothesis.

Methods: exact symbolic linear algebra, distributional integration identities with explicit hypotheses, finite-source geometric feasibility checks, bounded certificate-based negative tests.

## Expected evidence

- A precise, independently reviewable extraction lemma with actual source hypotheses, common-frame selection, uniform bounds and seam/boundary costs, **or** a reproducible counterexample to one necessary proposed bridge.
- Explicit accounting for every source point, including contact isolates, and all relevant separation and diameter constraints.
- A correct implication either to an actual same-cardinality strict-sub-$D$ competitor or to a clearly isolated **remaining** lemma.
- A statement separating what was proved about formal fields from what was proved about planar global minimizers.

## Falsification and stopping

Test every proposed implication against the rotated compatible laminate and the stress-only laminate, with the same frame and positivity assumptions actually used. Do not infer field extraction from a one-grain chart, an equilibrium stress alone or a numerical observation.

Stop when the result only establishes conditional field compatibility or cannot bound normalized seam/boundary work. Record the precise obstructing term and a next feasible experiment rather than promoting the formal theorem.

## Reproduction

Install the pinned verification environment described in [research/README.md](../research/README.md), then run:

```sh
python3 research/verify_global_joint_phase_compatibility.py
python3 research/verify_global_separable_distortion_obstruction.py
python3 tools/task_context.py global-joint-phase-source-extraction
python3 tools/check_public.py
```

The first two checks were independently replayed on Python 3.12 with SymPy 1.14.0; both passed their **finite/formal** checks. They are outside the registered 94-certificate canonical corpus. Rerun them yourself and inspect the arguments, not only the printed PASS lines.

## Remaining lemma and limitations

Extract and control a common compatible $F/S$ field from **every** canonical source to which the method claims to apply, including source realization, phase rotation, seams, transition amplitudes, isolates, and boundary-work terms. Then derive the strict full-source competitor or forced triangle. Both implications are currently unproved.

A finite model, an independently agent-checked formal-field theorem, a nonglobal example or a restricted periodic-domain result is not Level I closure.

## Live overlap and session scope

Run `python3 scripts/choose_research_task.py --task global-joint-phase-source-extraction --live-overlap --json` and inspect competing public Issues, Discussions and PRs.

Default to one bounded 30–60 minute attempt at an exact extraction sublemma, counterexample or independently checked intermediate identity. State source commit, hypotheses, verifiers, what failed or succeeded, and the next exact obligation.
