# Public outsider route evaluation, 2026-10-15

**Classification:** agent onboarding audit and exact finite evidence; no mathematical promotion.
**Public starting commit:** `afa7f7ec8b93b39efb921f4f47d132e4219b5df8`.
**State:** `2026-10-10.audit.234`; priority/catalogue `public-frontier.1`.

Three new clones were fetched independently from
`https://github.com/1337isnot1337/erdos-99.git`, with separately created virtual
environments. One auditor evaluated A, B and C-II in these isolated checkouts.
These are three route evaluations, not three independent mathematical reviews.
Only the public corpus, its public GitHub coordination surfaces and the current
machine environment were consulted. No private research checkout or remembered
project result supplied a premise. Substantial AI assistance: Codex performed the
navigation, finite replays, tooling repair and report; no human review is asserted.

The [machine receipt](onboarding-evaluation-2026-10-15.json) records the actual
commands and outcomes. Source-relative paths below can be used from any new clone.

## Start a route from a fresh clone

```sh
git clone https://github.com/1337isnot1337/erdos-99.git erdos-99-outsider
cd erdos-99-outsider
git rev-parse HEAD
python3 -m venv .venv
.venv/bin/pip install --require-hashes --only-binary=:all: -r tools/requirements-verification-linux-x86_64.lock
.venv/bin/python tools/check_public.py
```

The tested environment is CPython 3.14.7 on Linux x86_64. The wheel lock is for
CPython 3.14 / Linux x86_64; other platforms use the portable version pins linked
from [research reproduction](../../research/README.md). Assertions must remain
enabled. An unsupported wheel environment is not a failed mathematical result.

Actual navigation started at [README](../../README.md), [AGENTS](../../AGENTS.md),
[CONTRIBUTING](../../CONTRIBUTING.md) and [autoresearch](../../autoresearch.md), then
[state](../STATE.md), [problem](../problem/statement.md),
[bottleneck](bottleneck-brief.md), [priority](priority-state.json), a task card and
the named route. The review policy and research-family status supplied the lifecycle
and stopping rules. Full statements, proofs and their inline section references
remain necessary before using a premise.

## Initial failures and repair

The documented `tools/task_context.py` command initially returned four A files,
15 B files and 16 C-II files, with an empty `certificate_commands` list in every
case. Empty canonical lists in A/B are legitimate: the manifest does not attach
registered certificates to those route endpoints. However, the command also hid
reachable **supporting** scripts, including B's phase-cut checker and C-II's
Seed-90 checks. It did not follow theorem `depends_on` edges or registry
`proof_sources`. A's Section-175/177 sources had empty publication dependency
lists despite explicit load-bearing references to earlier sections.

The repair keeps registered certificates and unregistered supporting scripts in
separate output fields; import-only helpers are listed separately. It follows
manifest claim dependencies, preserves each reachable claim's lifecycle/scope,
and adds a [public section-to-file supplement](onboarding-prerequisites.json).
Missing or outside-repository prerequisite paths fail explicitly. Discovery never
executes a listed command. The original claim manifest and catalogue are unchanged.

The first repair regression caught another omitted edge: the unreviewed
quarter-fold report's checker was not reached by its publication dependency list.
The supplement now names that public checker explicitly. Five regression tests
then passed, including negative fixtures for absent/outside dependencies, an
executable fixture that would fail if discovery ran it, and lifecycle preservation.
All 19 original catalogue task-context queries completed.

After this patch, the three selected contexts resolve 43/16/360 files, respectively.
C-II reaches 169 manifest claims and 43 registered commands; A/B reach no registered
commands and do expose scoped supporting evidence. These are navigation counts,
not an independent proof audit or a certificate that no implicit reference remains.

## A: actual-source surplus and Schur response

Actual route: `target-a-locked-sector-surplus` → A27 (Section 175) → A29 (177).
Reading only those two endpoints leaves the actual-response, basis and stress
hypotheses underdefined. The supplement gives the earlier section chain, including
97/99/102/113/114, fixed-container source capacity 119–124, triangle-breaking 138,
the **154–155 source-alignment hypotheses used by 165**, stress 159, and 163–174.
It also retains the separate 176 zero-slack/source-matching obligation. The full
machine list is available with:

```sh
.venv/bin/python tools/task_context.py target-a-locked-sector-surplus
.venv/bin/python research/tube_shield_cut_audit.py
```

The finite audit passed **17,104** exact graph/tube/shield cases, with **15,056**
strictly improved lower bounds. Its domain is the 1,024 bipartite edge sets with
two basis vertices, two terminals, two interior rows, one exterior sink and the
prescribed basis matching, plus every tube and admissible shield-terminal subset.
Integer matching checks the stated finite cut bookkeeping. The one-path
`c → z → b → o` negative control shows why the tube charge cannot be dropped.

The inherited canonical route runs through 177. The older supporting report's
unreviewed header does not demote the later canonical module, and running the
unregistered checker does not promote that older report. The source-specific
inequality still required is
`|O_iso| + sum_i max(0, |O_i|-|C_i|) >= j_* + |T_Z|`.
The finite graphs encode no locked unit geometry, source realization or global
optimality. A useful bounded continuation is an independently checked three-channel
fan ledger retaining distinct sinks, `j_*`, and the interior tube charge; stop if
the argument yields only an `O(D)` count or silently identifies the independent
zero-slack matchings.

## B: multi-grain shell and interface payment

Actual route: `target-b-multigrain-transfer` → B README → the September-11
dense-grid/penetration/interpolation audit → its seven named source reports and
the phase-cut report. The task-context list resolves these public sources. The
reading must retain the pure simply connected rhombic disk scope, Section-50
fixed `lambda` before `D → infinity`, and GPI's **one dominant component** hypothesis.

```sh
.venv/bin/python tools/task_context.py target-b-multigrain-transfer
.venv/bin/python research/phase_cut_certificate.py
.venv/bin/python research/onboarding_two_grain_audit.py
```

The inherited checker reproduced the 30-direction model (135 edges, minimum cut
35, mean `75/2`), sharp C5 blowups, all **4,096** balanced `m=2` graphs and the
sliding-interval regression (57 edges, maximum biclique product 12).

The new supporting audit exhausts **2,025** integer incidence states: two fixed
one-edge grids, one pruned train, all six distinct-direction optional pairs and
all eligible penetration-charge assignments. Same-direction physical crossings
are excluded. A minimal failed naive budget has three physical crossings
`{01,03,23}`, while `03` is charged by both grids, giving total grid-plus-penetration
charge four. The MCP1 factor-two and MCP2 deleted-interface multiplicity bounds
pass throughout the domain. A separate determinant ledger, in units `sqrt(3)/2`,
records cross-grain virtual mass omitted by grain-internal sums.

This is a nonglobal combinatorial model. It proves neither planar realization nor
the PC penetration lower bounds, GPI additivity, topology correction, or shell
stability. The sufficient endpoint remains
`G+E >= (sqrt(3)/4) B + (sqrt(3)/2)(t+chi-1)`.
A bounded next result would price a shared interface in a source-realizable
two-grain construction, checking physical/deleted/virtual pair ownership before
summing; stop if the proof assumes a dominant grain or declares an unproved
interface error negligible.

## C-II: finite full-source geometry and capacity

Actual route: `target-c-face-coupled-move` → CURRENT → C-I restoration, the
core-only ZR/ZF module and the separate full-source geometry module → the supplied-W
and Type-II face-floor audits → their manifest dependencies. The prompt itself
instructs reading the canonical modules and promotion audits before the prompt.
The supplement supplies this order and two explicit finite obstruction branches.
The complete reachable source/claim list is large; a short task card is not the
whole proof chain.

```sh
.venv/bin/python tools/task_context.py target-c-face-coupled-move
.venv/bin/python research/verify_seed090_rhombus_contraction.py
.venv/bin/python research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py
.venv/bin/python research/verify_target_c_triangular_two_pin_capacity_2026_10_05.py
```

The exact Seed-90 checks passed source populations 305/1,471/4,519, retaining
121/1,159/4,015 contact isolates and accounting for 46,360/1,081,185/10,208,421
full-source pairs. Its comparison competitors establish these fixtures are
nonglobal. The checker also records why a hinge, an outside isolate and a spatial
realization cannot be silently substituted for planar full-source endpoint data.

The quarter-fold checker passed exact `Q(sqrt(15))` guardrails: a fixed center
collides with folded vertices 1,3,5,7; a separate flat-eight fixture replaces an
actual diameter pair; a 21-cycle has a smaller nonglobal grid competitor. The
capacity checker passed **716** elementary triangles and **228** admissible
triangles for `(3,3),(3,4),(3,7),(3,20),(3,80),(4,4)`. Its continuous upper bound
uses the audit's convexity/angular proof, not finite sampling. The exact capacity
statement concerns fixed triangular frames, not arbitrary macroscopic containers.

C-I is closed in the inherited ledger; C-II is open. Core rigidity does not extend
to isolate coordinates. Supplied-W deletion does not extract W or restore labels;
an already feasible endpoint theorem does not construct an endpoint. The bounded
next step is one face-coupled candidate with an explicit lower/upper squared-distance
ledger for **every** source label, all unary rhombus tests and restored population.
Stop at the first failed constraint or missing restoration. Closing C-II requires
strict contact loss at the actual diameter under the canonical minimality regime,
or a same-cardinality strict sub-D competitor, including the separate untouched
macroscopic-container obligation.

## A valid public contribution

**Integrated-candidate correction to the initial C-II exercise:** at diameter D,
the endpoint must remain triangle-free and strictly decrease the lexicographic
pair (unit contacts, actual diameter pairs). Preserving contacts and reducing
actual diameter pairs is a valid secondary branch; contact loss accompanied by a
new unit triangle is insufficient. A same-cardinality strict sub-D competitor is
a separate route. The shorter initial wording above omitted these conditions;
the active task/frontier and final repeat use the complete endpoint. The final
A prerequisite list also includes the finite Oler/topology module used by its
plateau and fixed-container arguments. Counts above remain historical.

Fetch current main, record its SHA/state/priority, preserve other work and create
an isolated branch. Query the selected task with `--live-overlap`; inspect matching
public PRs/issues and Discussions when available. Empty search results are scoped
coordination evidence, not an exclusive claim. New public main changed during this
audit; these initial results stay pinned to the starting commit and need an exact
integrated-snapshot repeat before a current-candidate readiness claim.

Choose one candidate lemma or finite model, state every hypothesis and its exact
implication to the route endpoint, name a falsification test and stopping condition,
and compare predecessor work. Put a proof/scoped report in `docs/reports/`, an
independent audit in `docs/audits/`, and executable evidence in `research/`. Include
exact inputs/arithmetic/bounds, commands, controls, provenance, limitations and AI
role. New claims default to unreviewed; agent auditing and human review remain
separate. Preserve credit and contribute only material that can be licensed under
the public contribution terms. A focused PR is optional when no durable result is
ready; this evaluation made no remote publication or theorem promotion.

```sh
.venv/bin/python -m unittest tools.test_task_context -v
.venv/bin/python tools/check_public.py
.venv/bin/python tools/local_ci.py --base-ref origin/main --require-localized
.venv/bin/python tools/run_theorem_certificates.py
git diff --check
```

An unknown-impact localized plan requests comprehensive verification/review; it is
not a full pass. The certificate runner is the explicit full replay. Finite
reproduction, mathematical proof, merge, publication clearance and canonical
promotion are distinct outcomes.
