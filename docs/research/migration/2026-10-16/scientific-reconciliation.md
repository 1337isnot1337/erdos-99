# Scientific reconciliation: source-main Target C batch 1

**Status: INCOMPLETE.** This report reconciles the first preserved source-main
batch with the destination's mathematical authority. It is not a proof audit of
each imported report and it does not close Target C or any part of Level I.

## Frozen comparison

- Source main: `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`, tree
  `e061f039eac44c286a00eacdcaa9a4cbbb877891`; source theorem-state
  `2026-10-10.audit.234`.
- Destination base: `60c2576b4893a7e9001d2c8bfbe5cfb64c1c969f`, tree
  `f4d73c1080b3b4a1b7757f5fd96109b6cd4b5c76`; theorem-state
  `2026-10-15.publication.2`.
- The destination state remains authoritative. It has 370 canonical C claims,
  4 audited-working claims, 62 regressions and 14 rejected or overridden claims.
  Level I, A, B and C-II remain open; C-I remains closed only in its stated
  scope.

The source theorem-state snapshot counted 371 canonical C entries, 3
audited-working entries, 62 regressions and 14 rejected or overridden entries.
The one-claim difference is reconciled by the destination's inverse-phase
correction below: the source still treats that claim as canonical, while the
destination records it as audited-working. Do not combine these theorem-entry
counts with artifact-index row counts; they count different objects.

The frozen source index contains 1,287 Target C artifact records: 193 marked
`canonical`, 3 `audited-working`, 28 `regression`, 2 `superseded`, 37 `mixed`,
and 1,024 `unreviewed`. Its separate `canonical` flag is true on 230 records,
and 263 records name claims. These are source provenance labels, not
destination decisions. The complete row-by-row record, including each claim ID,
dependency, source blob, lifecycle and disposition, is in
[`ledger/source-main-artifacts.jsonl`](ledger/source-main-artifacts.jsonl).

## Reconciliation of this batch

- **911** source Target C artifacts had no destination file at their original
  path. This batch integrates **85** of them as noncanonical research: **83**
  source-main audits and two linked reports needed to restore the low-response
  audit link and the cyclic fan-flip audit/report evidence chain
  (`target_c_fan_flip_isolate_escape_2026-10-02.md` and
  `target_c_low_response_mu_floor_2026-09-12.md`). The other **826** missing
  reports are queued for later focused batches.
- **338** source artifacts are exact duplicates of destination content, verified
  by SHA-256. This includes 337 exact same-path copies and one identical artifact
  already represented at another path.
- **38** source versions differ from a destination file at the same path. The
  destination bytes remain in place; each source version is retained under
  `docs/archive/source-e99-main-42f0296d/` with a historical warning and exact
  source/public hashes.
- The full direct Markdown dependency closure has **100** records: 31 missing
  source paths, 11 changed source versions, and 58 exact destination copies.
  This batch resolves 4 missing dependency records linked by its imported audit
  closure, and preserves the 11 changed versions (which can overlap the 38
  source-artifact conflict snapshots); the other 27 missing report dependencies
  remain queued. It verifies **84** of the full **384** evidence edges; the other
  300 remain recorded and queued. All 18
  report link corrections are recorded but await their parent report batches.
  No PDF collection or extracted third-party text was copied. No dependency in
  the full closure is marked rights-blocked.

This closure follows Markdown links. Code or fixture paths mentioned only as
inline text are not certified present by this batch's link scan. The full source
research tree is part of the queued next import, where those references will be
checked against the copied scripts and data.

The imported records do not become canonical merely because the source index
calls them canonical or because a source report calls itself an independent
audit. Destination theorem-state, proof graph, current Target C document and
publication inclusion were not replaced. The generated artifact index now
records the added documents; theorem-state counts and claim edges remain
unchanged. Source artifact metadata is retained in the migration ledger so that
later reviewers can assess useful proofs, corrections, computations and failed
routes without confusing historical status with acceptance.

## Correction that must survive the migration

The source's same-path version of
`target_c_global_inverse_phase_face_tail_exclusion_independent_audit_2026-10-09.md`
is source-labeled canonical. It is archived with an explicit warning because
the destination's later reconciliation withdraws the global `K'/D`-Lipschitz
chart and the unsupported `q=O(D^(4/5))` inference. The destination keeps
`C-GLOBAL-INVERSE-PHASE-FACE-TAIL-EXCLUSION` audited-working under the corrected
sequence-only argument and the original common-frame and face-tail hypotheses.
The archived source text is evidence of the earlier claim, not a usable premise.
The current correction and its scope are stated in the
[publication reconciliation](../../../publication/scientific-reconciliation.md)
and [Target C current state](../../../targets/target-c/CURRENT.md).

## Remaining reconciliation

The source-main `research/` subtree contains 2,707 Target C files: 152 exact
destination duplicates, 19 source dependencies referenced from reports, and
2,536 remaining research files. This batch includes the two research files
linked from its audits; the other 17 linked files await report batches. The
route tree has 157 Target C documents; their file-by-file queued, duplicate and
dependency states appear in
[`ledger/source-main-files.jsonl`](ledger/source-main-files.jsonl). The pinned
source inventory also contains 21 open PR heads; the proposals and other
historical PR work have not been reconciled into this batch. In particular,
PRs #947, #948, #950, #951, #952, and #955–#960 require separate content-level
comparison with the current destination before retaining any additions.

Accordingly, this batch establishes source identity and preserves substantial
research content; it does not establish that every source mathematical claim is
correct, that every older proof avoids the withdrawn inference, or that the
research-corpus migration is complete. The authoritative promotion and release
gates remain unchanged.

## Second batch — source PR #1008

The source PR inventory was refreshed against the frozen snapshot before this
batch: all 21 open PR numbers and exact head SHAs still match. The selected
source is draft PR #1008 at `ad1bda373a5cbd8c666040f64b4f6ecd83223e31`,
based on `eb51394f371aee958b0d9332f80faf75ae694b9e`; its recorded diff contains
five paths. Its report and two exact evidence files are integrated. The changed
research README is represented by a destination navigation entry; the source
artifact-index edit is regenerated from the imported report's metadata. Every
path has an explicit disposition and source hash in the open-PR file ledger.

The new report claims, still as **unreviewed**, that every global minimizer with
\(D>16384\) has
\[
g_A\ge\gamma D-\frac{\sqrt D}{4\sqrt2}-60,
\qquad \gamma=0.001939936045\ldots,
\]
and gives \(g_A\ge D/600\) for \(D\ge10^6\). The report states that this
asymptotically improves the canonical \(D^{2/3}\) reserve, but it does not
supersede any manifest claim. Its finite counterexample shows that triangle-free
packings with high reserve need not be global minimizers; this blocks removing
the global-optimality hypothesis from the proposed Target C upper-reserve
bridge. It does not supply that bridge or a C-II endpoint. The full scope,
canonical comparisons, proof dependencies, obstruction, and next obligations
are machine-readable in [the candidate registry](../../../targets/target-c/candidate-registry.json).

The exact verifier replay passed five finite geometry cases, all constant and
sign checks, 150 rotation identities, and two rejected collision controls. Its
output JSON matches the source fixture byte for byte. The code does not verify
the analytic average over all radii or global-minimizer optimality. The imported
report's source-era request for human review does not override the destination's
current independent AI-agent exact-commit review policy. The theorem-state,
publication inclusion set, canonical certificate registry, and target status
were not changed.

## Third batch — pinned source PR #951

The source open-PR snapshot was refreshed before this batch. The source main
remained 42f0296d1aca068c809f74cee5dcdb4ebdb27c73, the 21 open PR identities
and heads were unchanged, and PR #951 remained at
0023585a98d8f5f23df64174a091c143710ba78a. Its recorded branch merge base is
d999528cfaafd811a4a19bcfacd00f217c2fc375; the five destination evidence
verifiers and seven reports are all absent at their destination paths before
this batch.

The imported candidate family preserves seven distinct mathematical
contributions: (1) exact rhombic vacancy-hop and two-site-capacity results;
(2) exact fixed-strip weak and strict restoration capacities; (3) a
near-coherent fixed-boundary pinning regression; (4) a one-vacancy full-chart
release with full-source pair checks; (5) one-vacancy side-pin release; (6) an
effective discrete packet and wall-span stress identity; and (7) a conditional
unilateral local-rigidity barrier. Reports are first-party source bytes and
every source lifecycle label is unreviewed; there is no canonical promotion.
The seven report artifact IDs, fifteen evidence files, and two handled metadata
files are separately listed in the PR ledger.

The main positive conclusions are conditional reduced-source results. Under
actual chart, patch, and stress-transversal hypotheses, one literal vacancy
can release a chart, row, or side pins while retaining every other source
label and respecting the reported lower and upper constraints. The results
leave one label missing and do not extract their hypotheses from every
canonical source. The exact coherent-strip capacity is one below restoration
with its wall fixed. The local rigidity candidate rules out continuous local
refill under full-support stress and mixed-core rigidity; the
near-coherent regression rules out a continuous fixed-boundary strictification
based only on arbitrarily small train-angle variation. These findings narrow
the route but do not prohibit changed-wall or nonlocal discrete replacements.

Five source verifiers and fixtures are preserved. Their finite checks include
exact rational / Q(sqrt(15)) arithmetic, whole-segment quadratic minima,
source and upper-pair checks, multiple rhombic angles, near-coherent pinned
equilibria, and negative route controls. The scripts do not prove the
all-parameter analytic theorems, canonical source extraction, global
optimality, universal stress-transversal, or restoration. Each command and
post-import output comparison is recorded in the committed PR #951 verification
receipt. The candidate registry maps each theorem/obstruction to evidence,
canonical dependencies, scope, and next proof obligation.

No theorem-state, target status, 94-entry canonical certificate registry, or
publication-inclusion entry changes in this batch.



The #951 local replay completed in an isolated temporary directory. All five
source verifiers exited successfully, and each generated JSON fixture was
byte-identical to its imported source fixture. The rhombic replay checked 224
source pairs, 5,000 strip source pairs, 4,512 endpoints, 2,120 strict inserted
pairs, 5,000 weighted-cap identities, and 906 exact disk samples. The
near-coherent replay checked 40,128 source pairs, 1,808 weighted edges, 768
equilibria, and 4,608 anchored rows. The full-chart replay checked 20,168
source pairs, 74,464 segment pairs, 18,616 endpoints, and 17,232 strict chart
pairs. The side-pin replay checked 6,844 source pairs, 12,474 endpoints, 6,751
strict endpoints, 87,318 path-sample pairs, and 490 strict-descent pairs. The
effective-packet replay also passed and its regenerated fixture matched exactly.
Fixture hashes and commands are in the [PR #951 local verification receipt](receipts/target-c-pr951-local-verification.json).

The full destination canonical runner then passed all 94 of 94 registered
certificates with zero failures. On this batch tree, `check_theorem_state.py`
passed; `build_artifact_index.py` reported 538 artifacts; and `check_public.py`
reported zero errors, 94 certificates, 451 claims, 845 dependency edges, 810
retained source files, and 20 tasks (`mathematical_proof=false`). These checks
validate the destination integrity and finite computation, not the analytic
claims in the seven unreviewed reports. The theorem-state remains
`2026-10-15.publication.2`; no canonical status, publication inclusion, or
repository visibility was changed.
