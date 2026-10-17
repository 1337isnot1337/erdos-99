> Generated reading edition · [exact source](../../../docs/audits/target_b_gpi_scope_independent_audit_2026-10-17.md) · source SHA-256 `6777fd8c89349c4b9fc8d9f678ffd057babd624a5d56d3c1c092ea2862dc79c8`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-82F1C1B51E22","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B GPI/MCP2 scope audit

**Classification:** scoped agent audit; no theorem promotion requested  
**Checked source:** `e396ea07887dd0528b817ce4e656ff0e6b01f8fb` (`main`)  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.7`  
**Task:** `audit-target-b-gpi-scope`  
**LEVEL I STATUS:** STILL OPEN; Target B remains open.

## Verdict

The explicit general phase interpolation estimate (GPI) and the fixed-parameter
summability step in MCP2 are valid under their stated hypotheses. The conclusion
is local to one coherent component that carries the global quadratic rhombus
core at its own scale. Section 50 does not establish that hypothesis for any
single retained component, and MCP2 does not supply the missing global inequality
across multiple grains. No full Target B or Level I conclusion follows.

The theorem-state entry `TB-DENSE-GRID` is canonical for this scoped chain. The
standalone GPI report is not itself marked canonical in the artifact metadata;
I treated the manifest entry as the authority and reconstructed the quantitative
implication below rather than relying on the report's status label.

## Exact scope and quantifier order

For one pure-rhombic, simply connected disk sequence, GPI uses coherent phase
classes of sizes `M >= b >= a`, `t=b/M >= tau > 0`, `s=a/M`, and

`Delta = [M(a+b)-E]/M^2`,

where `E` is the physical crossing count within the selected component. It also
requires: no transversal triangle; `o(1)` phase coherence; only `o(M^2)`
crossings involving trains outside the component; the component carries the
global quadratic rhombus core (`R=E+o(M^2)`); and `T=O(M)`. The pure-disk
rhombus-count transfer `n=R+O(M)` and strict triangular-lattice comparison are
used in the final upper bound. Under these conditions, for each fixed `tau`,

`liminf Delta >= 4*10^(-17) tau^2`.

The Section-50 parameter `lambda` must be fixed before `D -> infinity`.
Theorem 50.1 gives at most `C_T/lambda+1` retained components and a uniform
within-component angular error `O_lambda(D^(-1+eta))=o(1)` for fixed `eta in
(0,1)`. Since an `A`-phase train has at most `a+b <= 2b` neighbors,
`lambda D <= 2b`; with `M <= T <= C_T D`, this yields the fixed ratio
`tau >= lambda/(2 C_T)`. Thus the local GPI lower bound supplied by this route
is at least `4*10^(-17)*(lambda/(2 C_T))^2`, for each fixed `lambda`.

This is an iterated limit, not a uniform estimate for `lambda=lambda(D) -> 0`.
The `O_lambda(1)` component count and coherence remainder may depend on fixed
`lambda`.

## Reconstructed GPI implication

Write `x`, `y`, and `z` for the missing `AB` edges, missing `AC` edges, and
present `BC` edges. Triangle-freeness implies

`M z <= a x + b y`,

because each present `BC` edge has no common `A` neighbor, and each missing
`AB` or `AC` edge is charged at most `a` or `b` times, respectively. Therefore

`Delta*M^2 = x+y-z >= (1-s)x`,

and the largest/second-largest pair missing-floor lemma gives
`Delta >= mu_0*t*(1-s)+o(1)`, with `mu_0=8*10^(-5)`. As `t>=tau`,
`1-s <= Delta/(mu_0*tau)+o(1)`. A sequence with `Delta -> 0` must therefore
have all three class sizes asymptotically equal; this conclusion uses the
geometric missing-floor lemma, not graph theory alone.

Choose uniform random `a`-subsets of the `A` and `B` classes and keep all of
`C`. An `AB` edge survives with probability `s^2/t`; `AC` and `BC` edges
survive with probabilities `s` and `s/t`, each at least `s^2/t`. Some
restriction consequently has balanced density deficit

`epsilon_bal <= (t-s+Delta)/t <= (1-s+Delta)/tau`.

The balanced triangle-free stability lemma gives a phase pair with missing
density at most `4*sqrt(epsilon_bal)`. The dual-tree interval extraction then
retains a complete grid with loss
`L_grid <= 6*epsilon_bal^(1/4)+4*sqrt(epsilon_bal)+o(1)`. The trains discarded
by balancing are restored in the diameter estimate with their full adversarial
coordinate contribution `L_del=2(1-s)/s`; no sign assumption is made about
them. Under the contradiction hypothesis
`Delta < 4*10^(-17)*tau^2`, the bounds are eventually

`1-s < 5*10^(-13)`, `epsilon_bal < 10^(-12)`,
`L_grid < 0.00601`, and `L_del < 3*10^(-12)`.

The grid lower bound gives `D^2/a^2 > 2.95`. The original component's total
crossing count and the lattice comparison give
`D^2/a^2 < c*(s+t-Delta)/s^2+o(1) < 2.21`, where `c=2*sqrt(3)/pi`.
The strict margins contradict each other. The attached checker verifies the
displayed numerical inequalities using rational arithmetic and a Machin-series
lower bound for `pi`; it does not encode the geometric or graph-theoretic proof.

## MCP2 summability audit

For fixed `lambda`, every retained component has at least `lambda D+1` vertices,
while `T<=C_T D`, so the component count is `O_lambda(1)`. Section 50's
bounded graph diameter gives a phase-direction error uniform over those
components and equal to `o(1)` as `D -> infinity` with `lambda` fixed. Each
penetration depth satisfies `d_j=O(D)`. Hence the summed phase error obeys

`sum_j d_j o(D) = O_lambda(1)*O(D)*o(D) = o(D^2)`.

Each deleted physical crossing is incident to at most two retained components,
so `sum_j E_del(H_j) <= 2 E_del`. Combining the component PC3 lower bounds with
the at-most-two reuse of physical crossings therefore yields MCP2's additive
bound with the stated interface coefficient. Replacing `[x-y]_+` by `x-y`
weakens the lower bound and is valid. The fixed-`lambda` order is essential;
this reasoning does not justify summing componentwise little-oh terms while the
number of components grows with `D`.

## Falsification and remaining gap

The relevant counterchecks are the balanced-triangle-free control, the
largest-pair missing-floor control, the discarded-train restoration term, and
the fixed-`lambda` component count. None falsifies the stated local theorem.
Conversely, removing the component-core hypothesis breaks the final comparison:
other grains can contribute to global `R` and `D` while the selected component
has only `M=Theta(D)` trains. Section 50 permits several retained components
with quadratic crossing mass; PDG's density-only grid sizes can remain below
the `2D/sqrt(3)` PC3 cancellation threshold.

The exact outstanding Target B obligation is a full-source inequality

`G+E >= (sqrt(3)/4) B + (sqrt(3)/2)(t+chi-1)`,

including multi-grain physical crossings, deleted/interface crossings, virtual
noncrossing determinant mass, and topology corrections; alternatively one
needs an actual same-cardinality strict sub-`D` competitor. A one-component GPI
bound, fixed-`lambda` MCP2, finite grids, or their scalar combination does not
prove this transfer. Target B and Level I remain open.

## Reproduction and provenance

The refreshed overlap query at `2026-10-17T21:19Z` found no task-matching open
PR, Issue, or handoff for `audit-target-b-gpi-scope`. The snapshot contained
four open PRs, zero open Issues, and four handoffs overall; these were checked
before selecting this card. The review is scoped to the checked source SHA
above. The contributor-side repository-wide theorem certificate replay was not
run. The local CI planner returned `full-verification-required` with dependency
closure not established; required full replay is deferred to the merging agent
and is not a pass.

From the repository root:

```sh
python research/verify_target_b_gpi_scope_arithmetic_2026_10_17.py
python tools/check_public.py
git diff --check
```

The originating agent was OpenAI Codex (GPT-6; exact runtime variant not exposed).
This artifact is a scoped proof audit, not a second-agent promotion review and
not external human peer review.

Recorded runs: the arithmetic verifier passed all four groups of assertions;
`python tools/task_context.py audit-target-b-gpi-scope` resolved only the
canonical `TB-DENSE-GRID` claim and listed no certificate commands. The
reading-edition generator reported 2,169 source documents and 71,621 normalized
math pairs; its `--check` passed with zero errors. The final
`python tools/check_public.py` run passed with zero errors (1,451 artifacts,
94 certificates, 451 claims, 845 dependency edges; seven external paper links
were classified as nonredistributed references). `git diff --check` passed.
