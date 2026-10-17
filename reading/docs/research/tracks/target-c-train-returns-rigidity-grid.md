> Generated reading edition · [exact source](../../../../docs/research/tracks/target-c-train-returns-rigidity-grid.md) · source SHA-256 `5152bc5fdc6c1a17322ef36449474fb566362e7da5a54a98e25475a9a3fc9e0f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C train returns and rigidity-forced grids

**Status:** The reports from source PR #950 are unreviewed research in the
publication destination. Their source-side proof audit is retained as evidence;
it is not a destination audit or theorem promotion. The candidate registry
records each result, canonical dependency, obstruction, and next obligation.

## New candidate results

The full [Worker Slot 03 report](../../reports/target_c_train_return_length_budget_worker03_2026-10-10.md)
starts from the canonical quadratic-core C-II sequence with
$D\to\infty$ and $R_4/D^2\to r>0$.

- **Positive-length return quantile.** After removing only
  $O(D^{2/3})$ trains that meet loaded-hull sides, the report selects an
  unloaded endpoint on each remaining train's terminal unit edge. Audit 235
  then gives $(\kappa-o(1))D$ pairwise vertex-disjoint, nontrivial actual
  contact paths to distinct loaded vertices. Full-source Oler population
  bounds give linear route-length quantiles: for fixed $\theta\in(0,1)$,
  at least $(\theta\kappa-o(1))D$ paths have length at most
  $\pi D/(2\sqrt3(1-\theta)\kappa)+o(D)$. Contact isolates remain in the
  population count.
- **Same-component Type-II grid access.** Component concentration places a
  linear return family in one unloaded component. In Type II, the report uses
  face-tail access and a cell crop to build one common source-realized coherent
  grid within the permitted radius of linearly many return attachments. The
  root-to-grid continuations may overlap; only the train-root-to-attachment
  segments are mutually vertex-disjoint.
- **Rigidity brace.** For a connected set $X$ of unloaded core vertices,
  the candidate proves $|\delta_C(X)|\ge\operatorname{diam}(X)+2$. Its
  triangle-free planar block count is combined with canonical mixed rigidity
  on the nonisolated positive-contact core. Contact isolates are not assigned
  core coordinates or dropped from the source.
- **Attachment-to-grid linkage.** The common grid has Euclidean diameter at
  least $\gamma D$. The brace inequality, an endpoint-inclusive separator
  count, and vertex Menger yield at least
  $(\gamma/5-o(1))D$ pairwise vertex-disjoint actual-contact paths from
  distinct loaded attachments to distinct grid vertices, with an $O(D)$
  length quantile from full-source Oler.

The report's exact constants and proof dependencies are in the full text and
machine-readable [candidate registry](../../../../docs/targets/target-c/candidate-registry.json).
The [source PR file ledger](../../../../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl)
records the frozen source blobs and transformations.

## Proof correction in the source PR

The original source PR revision `6433d1db49a1363bfa65008eb78f6b15d6ef4ed7`
used a Menger cut argument only for separators disjoint from both terminal
sets and assumed one remaining component contained the whole grid. That is
insufficient for distinct-endpoint vertex Menger and can fail when a cut
contains terminals or splits the grid. The corrected source head
`cbf066bb7489115559bcda34f9f810a1d78826ce` charges each remaining component
meeting the grid separately and proves the factor-five bound for every
endpoint-inclusive separator. The [source audit](../../audits/pr950_autonomous_proof_audit_2026-10-15.md)
records the derivation and dependency audit. The old source blob and its exact
known defect are recorded as superseded provenance in the migration ledger;
use the corrected proof as the candidate.

## What remains open

The train-return linkage and the rigidity/Menger linkage end at attachment
sets that may be disjoint. Their path counts alone do not give a positive-density
common attachment-label subfamily, a direct train-root-to-grid linkage, or a
stress-weighted allocation. The report also shows why summing straight
port-to-target face charges can repeatedly count the same exceptional faces;
positive stress support alone gives no uniform price for selected paths.

Even a linear root-to-grid linkage would not be a finite competitor. The next
obligation is to prove a linear endpoint overlap or equivalent gammoid-rank
inequality (or establish direct source-wide flow), then construct a
same-cardinality competitor satisfying every lower pair bound and every old or
new actual-diameter upper bound, retaining all isolates. At diameter $D$, it
must remain triangle-free and strictly improve the lexicographic pair
(unit contacts, actual diameter pairs); a strict sub-$D$ competitor is also
valid. No C-II branch or Level I endpoint is closed here.

## Regressions and nonadvancing routes

- The exact Pell-grid family has disjoint unit-contact rows of length a positive
  constant times its diameter. It is nonglobal and does not have loaded
  diameter endpoints; it only rules out deriving sublinear route lengths from
  unit separation, triangle-freeness, and diameter alone.
- The marked-rail separator calculation is explicitly weaker than canonical
  Audit 133's return count; it is not a new capacity theorem.
- A geometric train shear does not check intersecting train constraints,
  outside lower pairs, actual-diameter upper pairs, or isolates.
- The face-defect and stress-weighted routes remain blocked by path-charge
  multiplicity and lack of a uniform stress lower bound, respectively.

Relevant active cards: [Type-II stress-mass access](../../../tasks/target-c-typeii-stress-mass-access.md)
and [face-coupled finite move](../../../tasks/target-c-face-coupled-move.md).
