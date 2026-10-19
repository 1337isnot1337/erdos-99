<!-- theorem-state: {"artifact_id":"ART-49E9F78ACC61","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Target B: cross-component virtual determinant payment

**Date:** 2026-10-18  
**Classification:** scoped analytic lemma; unreviewed, noncanonical.  
**Source:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Task:** `target-b-multigrain-transfer`; investigation `frontier-target-b-multigrain-transfer-20261018`.  
**Originating agent:** OpenAI Codex, GPT-6 Luna xhigh; analytic proof and report.

Level I and Target B remain open; C-I is closed and C-II is open. This result is
not a source minimizer theorem and does not change the theorem state.

## Question and downstream quantity

Can a pair of distinct dense components in one actual pure rhombic disk have its
cross-component determinant mass paid by the global virtual missing-crossing
mass plus only the high-defect physical edges removed before pruning?

The exact quantity affected is the cross-component submass of

\[
M=\sum_{\substack{\tau<\sigma\\\tau,\sigma\text{ do not cross}}}
  |\det(u_\tau,u_\sigma)|
  =\operatorname{area}(Z)-\sum_{F\in\mathcal R}\sin\theta_F,
\]
the canonical Section 26.4 zonotope identity. The result below shows that if two
retained components contain linearly many trains in angular arcs separated by a
fixed positive angle, then their cross-component contribution to `M` is
quadratic. It retains the deleted-edge cost explicitly.

## Hypotheses

Work in a finite pure, simply connected, strict-rhombic disk of diameter `D`.
Use the train crossing graph and the Section 50.1 deletion order: first remove
all crossings with angular defect greater than `D^(-1+eta)`, then repeatedly
remove vertices of current degree less than `lambda D`, for fixed
`0 < eta,lambda < 1`. Write `E_hi` for the first, high-defect edge set and
`E_del` for all removed physical crossings. The canonical estimate is

\[
|E_{\rm hi}|\le C_\delta D^{2-\eta},\qquad
|E_{\rm del}|\le C_\delta D^{2-\eta}+C_T\lambda D^2.
\]

Let `H_1,H_2` be distinct connected components of the final retained graph.
Choose train subsets `A subset H_1` and `B subset H_2` with
`|A| >= alpha D` and `|B| >= beta D`, where `alpha,beta > 0` are fixed
independently of `D`. Suppose their train directions lie within angular radius
`epsilon` of respective centers `phi_1,phi_2`, and set

\[
s=|\sin(\phi_1-\phi_2)|>2\epsilon.
\]

Angles are measured modulo `pi`, as appropriate for unoriented train
directions. No claim is made that the canonical shell hypotheses force such
subsets to exist.

## Lemma: cross-component virtual mass after the edge payment

Let

\[
V_{A,B}=\sum_{\substack{\tau\in A,\sigma\in B\\
                         \tau,\sigma\text{ do not cross}}}
             |\det(u_\tau,u_\sigma)|.
\]
Then

\[
\boxed{V_{A,B}\ge \alpha\beta(s-2\epsilon)D^2
                     -C_\delta D^{2-\eta}.}
\]

In particular, for fixed `eta,alpha,beta,epsilon,phi_1,phi_2` satisfying the
hypotheses, all sufficiently large `D` obey

\[
V_{A,B}\ge \tfrac12\alpha\beta(s-2\epsilon)D^2.
\]
Since `V_{A,B}` is a sub-sum of `M`, the same lower bound holds for the global
virtual determinant mass.

### Proof

For every pair `tau in A`, `sigma in B`, classify it as either a physical
crossing or a noncrossing pair. The strict-rhombic train-pseudoline property
gives at most one crossing per train pair. The Section 26.4 zonotope formula
assigns determinant `|det(u_tau,u_sigma)|` to either case; in the crossing case
it is the area `sin(theta_F)` of the unique unit rhombus. Thus the exact
partition is

\[
\sum_{\tau\in A,\sigma\in B}|\det(u_\tau,u_\sigma)|
   =V_{A,B}+W_{A,B},
\]
where `W_{A,B}` is the determinant sum over the crossing pairs in `A x B`.

Every physical crossing between `H_1` and `H_2` belongs to `E_hi`. Indeed, if
it survived the initial edge deletion, its two endpoints would both survive
vertex pruning. Its edge would then remain in the final graph and connect the
two vertices into the same component, contrary to `H_1 != H_2`. Edges deleted
by pruning have a deleted endpoint, so they cannot be crossings between two
final retained components. Since each unit-rhombus determinant is at most one,

\[
W_{A,B}\le |E_{\rm hi}|\le C_\delta D^{2-\eta}.
\]

For each cross pair, choose real angle lifts with
`|phi_tau-phi_1| <= epsilon` and `|phi_sigma-phi_2| <= epsilon`. The function
`x -> |sin x|` is 1-Lipschitz, so

\[
|\det(u_\tau,u_\sigma)|
  =|\sin(\phi_\tau-\phi_\sigma)|\ge s-2\epsilon.
\]

Summing over `A x B` and subtracting the crossing payment proves the displayed
bound. The asymptotic form follows because `D^(2-eta)=o(D^2)` for fixed
`eta>0`. \(\square\)

## Why the deletion distinction matters

The full Section 50.1 deletion estimate includes `O(lambda D^2)` edges removed
when a vertex is pruned. Charging all of `E_del` here would lose a quadratic
term. That loss is unnecessary for cross-pairs of *final* retained components:
an edge deleted at a pruned endpoint cannot have both endpoints in the final
vertex set. Only the initial high-defect deletion can separate two surviving
vertices. The payment is therefore `C_delta D^(2-eta)`, with no
`C_T lambda D^2` term.

The bound is conditional in two essential ways. The component populations must
contain fixed linear-size angular subsets, and their angular centers must be
separated enough that `s-2 epsilon > 0`. Section 50.1 alone gives neither
condition: its minimum degree `lambda D` is not a fixed macroscopic population
independent of `lambda`, and it does not force different angular centers. If
`s <= 2 epsilon` or either subset is sublinear, the stated lower bound is
vacuous. These controls prevent using the lemma as a one-grain or universal
multi-grain conclusion.

## Relation to previous work

- Section 26.4 and the imported audit
  `docs/audits/target_b_virtual_zonotope_missing_crossing_audit_2026-09-05.md`
  give the global missing-pair determinant identity and its support-depth
  lower bound. They do not localize the virtual mass to a pair of retained
  components or charge cross-component physical rhombi to the initial
  high-defect deletion.
- `docs/audits/target_b_local_virtual_area_interface_audit_2026-09-05.md`
  bounds virtual mass incident to pruned trains. The present lemma concerns
  pairs whose two endpoints both survive pruning and lie in distinct retained
  components.
- The reviewed abstract interface report,
  `docs/reports/target_b_interface_capacity_2026-10-17.md` (PR #86), proves an
  incidence budget for supplied PC penetration sets. It explicitly does not
  realize a train graph or rhombic disk and does not include determinant area.
  The present result is geometric but conditional on separated macroscopic
  direction subsets; it does not replace or strengthen the abstract charge
  optimization.
- The canonical MCP2 and PC3 results still require fixed `lambda` and retain
  their stated coherence assumptions. This lemma does not alter their
  hypotheses or provide a grid, PC penetration bound, endpoint contradiction,
  topology correction, or shell-stability inequality.

The result supplies one local term in the required physical/deleted/virtual
ledger: for two separated retained components, almost all cross-pair
determinant mass is virtual, while any physical crossing between them is paid
by the subquadratic high-defect edge budget. It does not show how this positive
mass enters the exact Target B endpoint
`G+E >= (sqrt(3)/4)B + (sqrt(3)/2)(t+chi-1)`.

## Falsification checks and stopping condition

The proof depends on three checkable statements: (i) each strict-rhombic train
pair crosses at most once; (ii) a crossing between distinct final components
must lie in the initial high-defect set, not in an edge deleted at a pruned
endpoint; and (iii) the angular determinant lower bound is at least
`s-2 epsilon`. The proof fails if any of these statements fails in the
canonical model. Same-direction subsets (`s=0`) and subsets with
`s<=2 epsilon` are explicit negative controls: they produce no positive
quadratic bound.

Stop here unless an independent geometric result supplies the two fixed
macroscopic, angle-separated subsets or shows how `V_{A,B}` transfers into the
shell endpoint. Do not infer either from positive total crossing density,
fixed-`lambda` component count, a finite fixture, or GPI's one-dominant-component
hypothesis.

## Open next question

**Downstream decision:** whether the cross-component submass of `M` can be
inserted into the canonical Target B shell ledger without being canceled by
the support-depth term. **Quantity affected:** `V_{A,B}` above. **Changed
hypothesis:** derive two retained components with direction subsets of sizes
`alpha D,beta D` and angular separation `s>2 epsilon`, with fixed positive
constants. If this hypothesis is forced by shell constraints, the lemma gives
an explicit positive quadratic virtual term after paying all cross-component
deleted edges. If it is not forced, the next result must identify the phase
alignment or population loss that prevents that term, without assuming a
dominant grain. A useful next step is an exact proof or obstruction for this
macroscopic separated-subset extraction in an actual two-component disk.

No external literature or nonpublic source is used. The result and prose are
original Apache-2.0-compatible contribution; OpenAI Codex assisted with the
analytic proof and report. No independent AI-agent audit or theorem promotion
has occurred.
