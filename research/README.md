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

## Source PR #951 — slot 07 vacancy release and restoration barriers

All seven proof reports are linked from
[the noncanonical proposal index](../docs/research/proposals.md) and
[Target C candidate registry](../docs/targets/target-c/candidate-registry.json).
They remain unreviewed and none is in the registered theorem-certificate set.

Run the five exact verifiers from the repository root:

- python3 research/verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10.py
- python3 research/verify_target_c_effective_fixed_wall_packet_slot07_2026_10_10.py
- python3 research/verify_target_c_near_coherent_one_vacancy_pinning_slot07_2026_10_10.py
- python3 research/verify_target_c_one_vacancy_full_chart_release_slot07_2026_10_10.py
- python3 research/verify_target_c_one_vacancy_side_pin_release_slot07_2026_10_10.py

The rhombic checker verifies the source patch, algebraic hop threshold fixtures,
whole-strip one-vacancy packets, and exact two-site capacity identities. Its
report proves the all-angle threshold and exterior shield analytically; the
fixtures do not prove canonical patch extraction or refill.

The effective packet checker covers actual perturbed walls, discrete packet
endpoints, diameter-star stress identities, and a finite already-spare refill
bay. The near-coherent checker proves finite pinned-equilibrium and anchored
rank regressions; these are not canonical normalized KKT stresses. The
full-chart and side-pin checkers inspect whole linear-segment minima or
additional actual-source fixtures. Their reports give analytic whole-path and
inward-normal arguments, but no canonical extraction, universal
stress-transversal, or last-label restoration. The unilateral local-rigidity
report is an analytic candidate without a separate verifier.

The exact fixed-wall capacity is one label below restoration. A near-coherent
fixed-boundary extension is false, and local continuous refill is blocked under
the listed stress/rank hypotheses. These are scoped route obstructions, not a
proof that every moved-wall or nonlocal discrete replacement fails.

## Source PR #947 — midpoint, anchor, and slow-chart audits

The [research track](../docs/research/tracks/target-c-midpoint-anchor-atlas.md)
and [candidate registry](../docs/targets/target-c/candidate-registry.json)
connect the source reports and second-referee records. Audit.246 claims
partner-uniform midpoint tails and moments and bounded-deficit pair
localization; Audit.247 proposes a positive-leaf boundary-distance improvement
from the destination's canonical (O(D^{-1/2})) to (O(D^{-2/3})); Audit.254
bounds two supplied-chart endpoint classes but assumes a bounded (K/D)-error
atlas. All three remain unreviewed in this repository and no finite verifier
encodes their analytic claims.

The source PR also records an exact near-triangular fixed-wall capacity
plateau, a continuous restored-pin displacement gap, and duplicate/subsumption
screens for selected quarter-fold, Type-II, shell-fold, radial-stress, and Oler
claims. Audit.236 retains only the corrected sequence-level (q=o(D))
conclusion under both original global premises; its source PR canonicalization
request is not adopted. The older global (K'/D) chart and (q=O(D^{4/5}))
inferences remain withdrawn. Source referee “PASS” entries are retained as
provenance and do not change destination theorem status.


## Source PR #950 — train returns and rigidity-forced grid linkages

The [research track](../docs/research/tracks/target-c-train-returns-rigidity-grid.md)
links the full 597-line report, the source endpoint-cut audit, and seven
machine-readable candidate/screen records. The candidate derives positive
length-return quantiles, a common Type-II grid, a rigidity brace, and an
independent attachment-to-grid linkage. The two linkage endpoint sets may be
disjoint; no stress-weighted payment or finite competitor follows. The prior
source proof revision's endpoint-cut defect and its repair are recorded
explicitly. Nothing is promoted in destination theorem-state.


## Source PR #948 — quarter-fold and complete bent-array routes

The seven mathematical reports, their seven exact finite verifiers, and seven JSON outputs were already present in the destination. The [focused research track](../docs/research/tracks/target-c-quarter-folds-bent-arrays.md) reconciles the proof scopes, finite-evidence limits, and missing endpoint/extraction bridges. All seven claims remain unreviewed and outside theorem-state. See the [candidate registry](../docs/targets/target-c/candidate-registry.json) and [per-file migration ledger](../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl).

## Source PR #952 — owner release, loaded anchors, and inclusive floors

The five reports, six finite outputs, and four verifier scripts were already
present in the destination. The [focused track](../docs/research/tracks/target-c-owner-release-loaded-anchor.md)
maps their conditional results and exact remaining bridge; the
[candidate registry](../docs/targets/target-c/candidate-registry.json) links
each proof to its finite evidence, canonical dependencies, and limitations.
The finite owner-sink and common-release cases are explicitly nonglobal. The
global gap is extraction of a canonical owner family with owner-respecting
loaded ports for every upper-relevant label and isolate, followed by a nonzero
solution of the exact full-source lower/upper closure. All five candidates
remain unreviewed and outside theorem-state. The [migration ledger](../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl)
records all 17 source PR paths, including the rebuilt index and adapted README.

## Source PR #956 — global reserve, lattice bound, interface payment, and regression

The [four-report track](../docs/research/tracks/global-population-lattice-interface-pr956.md) records all four unreviewed analytic scopes, the exact global hypotheses, regressions, and next proof obligations. Run the corresponding finite/formal checks from the repository root:

- `python3 research/verify_global_boundary_zigzag_2026_10_11.py`
- `python3 research/verify_global_lattice_population_bound_2026_10_11.py`
- `python3 research/verify_global_straight_interface_payment_2026_10_11.py`
- `python3 research/verify_global_stress_density_regression_2026_10_11.py`

The first three verifiers do not establish their universal analytic arguments; the lattice defect and periodic-motif consequences also depend on the unreviewed boundary reserve. The periodic finite-subset bound assumes `1 <= q <= D/16` and requires separation of the entire infinite packing, including cross-coset pairs. The fourth report is a nonglobal regression, not a global-minimizer counterexample. The source audit is preserved as provenance and does not satisfy the destination's independent exact-head review policy. The [per-file ledger](../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl) records exact source hashes and README/index transformations.

## Source PR #957 — exact joint diameter-cover exchange

The [joint-exchange track](../docs/research/tracks/global-joint-diameter-cover-exchange-pr957.md)
records the exact full-source matching identity, four geometric controls, the
all-`k` dense-star regression, the distinct free-region cage, provenance, and
the precise packet-existence obligation. Reproduce the finite/formal checks
from the repository root:

- `python3 research/verify_global_joint_exchange_2026_10_12.py`
- `python3 research/verify_global_exchange_star_family_2026_10_12.py`

These are exact rational finite checks. The supplied-packet theorem and
all-`k` population statement are proved analytically in the report; neither
verifier proves existence of a successful packet for every large global
minimizer. Source local paths and account-specific CI details were removed
from the historical run note and source audit; their source hashes and edits
are retained in the [per-file migration ledger](../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl).
