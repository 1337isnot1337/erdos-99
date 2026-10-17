# Erdős Problem #99 — sol xhigh full-settlement run

Run in `/home/cinna/math` with **GPT-5.6 Sol**, reasoning effort **xhigh**,
and local repository/tools access. Select the model and effort in the runner;
this text does not configure them. Prepared against `main` at `3f37ef0` on
2026-09-10. If the checkout has advanced, reconcile the changed dependencies.
This is a whole-problem launch prompt, not a theorem-state promotion.

## Objective and success criterion

Conduct sustained mathematical research aimed at a complete proof or disproof
of Erdős Problem #99. Execute the research, develop the missing mathematics,
and audit the finished argument. A plan, survey, restated frontier, conditional
closing lemma, or improved numerical constant is not the requested outcome.

For unit-separated planar sets define
\[
D(n)=\min\{\operatorname{diam}A: A\subset\mathbb R^2,
\ |A|=n,\ |x-y|\ge1\text{ for }x\ne y\}.
\]
Prove
\[
\exists n_0\ \forall n\ge n_0\ \forall A,
\quad |A|=n,\ \min_{x\ne y}|x-y|\ge1,
\ \operatorname{diam}A=D(n)
\Longrightarrow A\text{ contains a unit equilateral triangle}.
\]
Alternatively, construct triangle-free global minimizers for unbounded
cardinalities and prove their global optimality. A finite example, local minimum,
asymptotically optimal family, or one triangle-containing minimizer per
cardinality does not settle the problem. An affirmative proof may have a
nonexplicit threshold, but its existence must be uniform over all minimizers.

Work in one context; do not delegate to separate agents. Choose tactics
autonomously. Target C-II is the initial priority because C-I is closed and
the latest report brings the entire source population into force geometry.
You may switch to A, B, an infinite-family disproof, or a new global route
when you can state a stronger concrete closing implication. Route preference
is not a mathematical assumption.

## Bootstrap and trust boundaries

Read in this order, using paths relative to the repository root:

1. `AGENTS.md`, `CONTRIBUTING.md`, `docs/README.md`, and
   `docs/RESEARCH_WORKFLOW.md`.
2. `docs/problem/statement.md`, `docs/problem/literature_baseline.md`, and the
   three route maps: `docs/targets/target-a/README.md`,
   `docs/targets/target-b/README.md`, `docs/targets/target-c/README.md`.
3. `docs/targets/target-c/56-ci-restored-frontier.md`, then
   `docs/targets/target-c/01-force-hull-and-shear.md`.
4. The shared theory used by your argument: `docs/theory/01-local-structure.md`,
   `docs/theory/02-nonlinear-and-regressions.md`, and
   `docs/theory/03-oler-shell.md` for packing/shell estimates. Complete the
   selected route's active modules and promoted audited addenda as required
   by `AGENTS.md` before introducing new mathematics on that route.
5. `docs/prompts/README.md` and the selected route's active prompt, only as
   operational context. Resolve its older mathematical wording against the
   route map and controlling corrections.

Record the starting commit and working-tree state. Treat explicitly promoted
results as a trusted theorem library, with their exact hypotheses. Reopen an
old proof only for a specific dependency issue exposed by your new argument.
Do not reconstruct the frontier from archives or read every historical report.
The named working reports below are targeted candidate inputs, not exceptions
to the promotion rules. Audit any candidate and its unpromoted dependencies
before using it in a proof. A report's self-description as “proved” or
“audited” does not make it canonical.

## Current mathematical state: do not roll it back

**C-I is closed.** The promoted September 9 orientation/dependency audit proves
\[
\Omega_s=L_C(\alpha_s)-L_H(\beta_s)\succeq0
\]
for every normalized source KKT stress. This uses the actual circular-planar
response, affine equilibrium, and one consistent projective cut/orientation
of the diameter thrackle. C63's convergent Newton–Hoffman correction gives
finite weak-row release. Contact minimality gives `C=C_*`; minimizing diameter
pairs second gives `H=H_*` and the promoted common-stress-kernel local form.
Use these results; do not spend the run re-closing C-I.

**C-II is open.** Exclude every sufficiently large triangle-free global source
chosen first to minimize contacts and then diameter pairs, retaining all
contact-isolated points. Only the nonisolated core is the connected positive
contact network. Explain why exclusion of this representative excludes an
arbitrary original counterexample. Do not also impose hull saturation: that
separate normalization may increase diameter-pair count.

The heptagon-plus-center force-bulk regression remains valid. The old pentagon
PSD “regression” is withdrawn because its cut and orientation were incompatible.
Restoring PSD does not promote every later C-II assertion or eliminate isolates.

## First closing opportunity: full-source capacity

Read `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`.
Audit FS.1–FS.4 against its cited canonical inputs. Its proposed consequences
hold for every selected normalized stress of every global source, without a
small-isolate assumption:
\[
R(K)=D/2+O(\sqrt D),\qquad P_*=2D-O(\sqrt D),
\qquad \theta_{\rm shared\ diameter}=O(D^{-1/4}).
\]
It also gives almost-antipodal diameter endpoints about a common source
circumcenter and radialization of the actual response on coordinate fields.
These are unpromoted proof-report results to verify, not a Level I solution.

Here is an exact whole-source endpoint. With
\[
K=\operatorname{conv}A,\quad P=\operatorname{per}K,\quad
a_0=\sqrt3/2,\quad c_0=\sqrt3/4,
\]
\[
\delta_K=\pi D^2/4-\operatorname{area}K,\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1),
\]
the unconditional strict translated-lattice comparison and Oler give
\[
\delta_K+\mathscr O_A<c_0P.
\]
Derive from triangle-freeness and the actual global-source structure the
opposite inequality
\[
\boxed{\delta_K+\mathscr O_A\ge c_0P,}
\]
or construct an `n`-point unit-separated competitor of diameter strictly below
`D`. Merely renaming this contradiction “NC” is not progress: supply the new
geometric, response-to-population, or finite-rearrangement theorem that forces it.

FS's exact odd-shell tests are mandatory. Near-saturation `P_*/D -> 2` does
not imply an almost-full-weight diameter matching or a small response trace:
the shell retains at most asymptotically half its diameter weight in a matching,
yet its actual PSD response has trace defect `2D^2-2` and affine core kernel.
Dense isolated fillings retain these properties without a global-optimality
certificate. Identify exactly where your proposed closure uses information
these examples lack. Near radiality on two coordinate fields is not an
operator bound on arbitrary boundary data; a nearly minimal containing radius
is not near-maximal force-hull area.

## Alternative C-II opportunity: the post-ZF rigidity/face route

If using this route, audit the separate candidate chain in:

- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`;
- `docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md`;
- the C56 minimum-transfer proof cited there;
- `docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md`;
- `docs/reports/target_c_zf_exact_defect_budget_addendum_2026-09-09.md`.

Z/ZC/ZR/ZF claim maximal scalar stress rank and mixed equality-bar rigidity
on the `v` nonisolated core vertices, giving `e+h>=2v-2`. Here `e` counts
contacts, `h` diameter pairs, `b` the outer-face walk with multiplicity, and
`Q_f=sum_bounded_faces(deg(F)-4)`. The exact sufficient contradiction is
\[
\boxed{b+Q_f>2h,\quad\text{equivalently }e+h\le2v-3.}
\]
Any proof must account for the full source, exceptional faces, bridges,
components, and isolates instead of assuming a pure rhombic disk.

After accepting ZF/ZS, `q>=h>=delta>=ceil(D)` and
`sigma_B>=ceil(D)-2`; the older `sigma_B=o(D)` normal form is unavailable
for that source. Do not revert to it. Consult
`docs/reports/campaign_zm_zs_reconciliation_2026-09-09.md` when using ZM/C44.

Use later reports selectively: the September 9 mixed redundant-rigidity report
gives at least three actual diameter bypass edges for a contact bridge with
two nonsingleton sides. The Dirichlet/PI feedback report reaches
`liminf (e_BB+2s_C)/D>=0.4702` but explicitly lacks a closing upper bound.
Do not iterate that scalar constant as an end in itself. A useful improvement
must cross a proved contradictory threshold or eliminate a remaining class.
Equality-bar universal rigidity is not rigidity of the packing inequalities:
the PSD KKT/bar stress has the opposite proper-stress signs for those inequalities.

## Other exact endgames remain available

**A:** Prove the source-specific inequality
\[
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda,
\qquad\text{equivalently }d_{\rm sc}\ge\Delta_\Lambda,
\]
or a strict competitor with the required source cardinality. The route map
reaches Sections 168–174, beyond the active prompt's 163–167 snapshot. Use
the zero-slack/descent and locked stress-sector branches. Section 174 states
the exact sector-population obligation. The unpromoted tube-only refinement
`docs/reports/target_a_tube_only_cut_2026-09-08.md` may reduce the required
shield charge after audit. Fixed-hull Hall capacity cannot be exceeded.
Closing only A still requires the remaining global branch coverage.

**B:** Prove the topology-correct joint shell inequality
\[
G+E\ge(\sqrt3/4)B+(\sqrt3/2)(t+\chi-1),
\]
with the route's exact definitions; global minimizers satisfy the strict
reverse inequality. The promoted phase-cut/coherent-family addendum excludes
specified coherent near-extremal cores, not every jammed survivor. Supply its
missing coverage or a diameter-feasible strict competitor. B alone does not
dispose of the flexible branch.

**New route/disproof:** Give a precise replacement theorem and a complete
quantifier-preserving reduction. For a disproof, exhibit unbounded
cardinalities and a matching global lower bound/certificate for the proposed
triangle-free minimizers. Good numerical packings are not that certificate.

## Work discipline and persistence

Before investing in a lemma, state its exact implication to a closing
inequality or feasible construction, including the required sign, margin,
cardinality, and class of sources covered. Maintain a compact proof-obligation
ledger separating trusted inputs, candidate dependencies, new proofs, rejected
claims, and remaining branches. Give complete mathematical proofs and
certificates, not a transcript of exploratory reasoning.

Test universal claims early against the relevant route regressions. In
particular, local rigidity/near-equilateral density does not force a triangle;
planarity, Hall circuits, and common-neighbor witnesses do not force simultaneous
Schur nullity; positive support or many strict minors does not give a numerical
conductance floor; free finite Kuperberg moves require proved exterior
compatibility. Preserve exact boundary/topology terms when the contradiction
is one integer. If changing representatives, name what is preserved: the RA
rattler-absorption representative need not retain `C=C_*`, `H=H_*`, or ZF.

After a useful theorem, push it through the remaining proof. A failed mechanism
is a reason to change mechanisms, not to end with a list of suggestions. Do not
stop merely because a result is new, the problem is open, or the next step is
difficult. Continue while a concrete in-scope avenue remains; do not invent a
time/token budget. At an actual execution limit, preserve the precise checkpoint
and report honestly. Never manufacture closure to satisfy the requested outcome.

Use tools for the research. Read `research/README.md` before computations;
record encoded/omitted assumptions, arithmetic, and proof scope. Use exact or
certified finite witnesses where possible. Search literature for a named missing
theorem, prefer primary sources, and check exact hypotheses, normalization,
constants, and the finite-container/global-optimality bridge. Baseline papers
are under `papers/primary/`. Numerical output alone is not global optimality.

You may make reversible, in-scope local research edits and run non-destructive
checks without routine approval. Preserve unrelated changes and follow desktop
isolation instructions. Do not publish, push, message people, or change external
state. Follow the repository's audit/promotion procedure for any theorem edits.

## Completion audit and output

Perform a distinct adversarial audit of any claimed solution: every new lemma,
dependency, equality case, normal-form transition, and surviving branch. Check
all pairwise separations and all diameter constraints in finite competitors,
and uniform thresholds in asymptotic arguments. Locate the decisive use of
global optimality beyond properties satisfied by the shell regressions.

Write a dated report using `docs/reports/REPORT_TEMPLATE.md`, with full proofs
or exact certificates and precise dependency citations. Link reproducible
checks, classify nonproved claims, and record promotion recommendations.
Run the relevant checks from `CONTRIBUTING.md`.

Begin the final response with exactly one of:

`LEVEL I STATUS: SOLVED`

`LEVEL I STATUS: DISPROVED`

`LEVEL I STATUS: STILL OPEN`

If settled, state the complete theorem, decisive new step, global quantifier
coverage, and report/certificate links. If not settled, state that directly
and give the strongest genuinely new proved result (or say none), its exact
effect on the endpoint, the precise unresolved implication, decisive failed
routes/regressions, and files changed. A conditional proof must remain labeled
conditional. Honesty about a remaining gap is mandatory; finding a gap is not
the objective of the run.
