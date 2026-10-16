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


## Fourth batch — pinned source PR #947

The source snapshot still has main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
PR #947 remains open and frozen at head
`1afb7e64d47c5619d872d32759b0e01f1526fd5a` (tree
`48b678c0d2695002595dc8aa9eaa6d1ac909e31b`), merge base
`d999528cfaafd811a4a19bcfacd00f217c2fc375`. Destination PR #21 merged as
`53527e354fd545325744f828c93278bcf6437bd4` with tree
`399b0e3407cd36721dd2361bd4cc9aa3ccfcd61a`; this batch is based on that tree.
All 20 changed source paths have exact source and destination blob/SHA records
in the PR file ledger.

The mathematical audit bodies in this PR were already present in the
publication destination from the source-main batch. Their destination copies
retain explicit unreviewed lifecycle banners where source PR #947 changed
frontmatter to `canonical`. The fused-sign/residual-tail screen is byte-identical.
The source PR's six-line historical Audit.202 summary is subsumed by the
complete destination historical proof record, which preserves the original
text beneath a prominent withdrawal notice. The destination does not restore
its global `K'/D`-Lipschitz-chart inference or `q=O(D^(4/5))` rate.

The source PR adds 68 lines to the integration audit ledger and 209 lines of
referee-run provenance beyond the source-main destination copies. Those records
are appended beneath explicit warnings that source “PASS/promote” findings are
not destination mathematical audits or theorem-state transactions. Three
nonmathematical source workflow-status sentences were generalized to state
only that the required checks did not execute workflow steps; the original
source file hash is retained in the ledger. Generated
source state (`docs/STATE.md`, theorem-state, status/graph views, and artifact
index) is recorded by hash but not copied over destination authority; the
candidate registry and this reconciliation record every status proposal and
its disposition.

The candidate registry adds seven unreviewed candidate/regression records,
one audited-working inverse-phase correction record, and one nonclaim/duplicate-
screen record. The source PR proposed five new canonical IDs, canonical status
for the corrected inverse-phase result, a stronger positive-leaf bound from
`O(D^-1/2)` to `O(D^-2/3)`, and a fixed-wall displacement regression. Destination
status remains unchanged: the inverse-phase result is audited-working with
`q=o(D)` only under both stated global premises; the positive-leaf claim keeps
its existing canonical `O(D^-1/2)` bound; all other proposed claims remain
unreviewed. The midpoint moments do not count near-diameter pairs. The
slow-chart result assumes a supplied bounded atlas and gives no extraction or
finite competitor. The near-triangular one-pin capacity is frame-dependent and
counts only the fixed interior wall.

The source second-referee records for midpoint tails, positive-leaf anchoring,
and the corrected inverse-phase proof are preserved as source evidence. No
finite verifier was supplied for the new universal audit claims, and those
source referee conclusions were not independently re-performed in this batch.
The destination's full canonical certificate suite and integrity checks are
run on the batch tree; they check existing canonical assets and links, not the
analytic claims in the unreviewed source reports. No theorem-state, registered
certificate, publication-inclusion entry, or repository visibility change is
made.

## Fifth batch — pinned source PR #950

The frozen source main remains `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`
(tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`). Source PR #950 is open at
head `cbf066bb7489115559bcda34f9f810a1d78826ce` (tree
`80dd0d6db99d9aa6698ee6500c91a3f670c63aae`); its branch merge base is
`9327a3a13f0641f2a8c1897aec0c088be016743a` (tree
`2f01e4c1abe49de6fc24bef28e750adebc5b56bc`). The destination batch starts at
`73bbc4ae4bf65ce6a02fcc2c4bde33b31124e742` (tree
`54713dc034018b862dc0aa69c85a921540dd5a2e`). Three current source paths are
recorded: a 597-line proof report, a 62-line source audit, and a generated
artifact-index update. The two mathematical files were absent from the
previous destination tree. Both were imported with a short destination
lifecycle banner; their proof text and source artifact IDs are retained. The
source artifact index was not copied over destination authority; the
reproducible destination index was rebuilt.

The source report contains four distinct unreviewed claims: an
`O(D)`-length quantile for a positive-density family of nontrivial
vertex-disjoint train returns; a common source-realized coherent grid for a
positive Type-II return subfamily; the unloaded-core rigidity brace
`|delta_C(X)| >= diam(X)+2`; and a separate linear attachment-to-grid
Menger linkage. The proof audit corrects the earlier endpoint-cut omission:
Menger separators may meet either terminal set and may split the grid, so the
brace budget must be charged component by component. The corrected argument
establishes an endpoint-inclusive factor-five cut bound. The source-side audit
is preserved as evidence but is not a destination independent audit or
promotion; all new claims remain unreviewed.

The exact prior source report revision at `6433d1db49a1363bfa65008eb78f6b15d6ef4ed7`
had blob `bdfc1517b63358cf7710cdbcbe79e4081686cda8` and SHA-256
`e9eba70c7577aad8eddfdf6ec7ddc792250717861c84f0d5537260aaa8543a8f`. It
restricted separator checks to cuts disjoint from both terminal sets and
assumed one remaining component contained the whole grid. That revision is not
copied as an active proof; its exact hash and defect are recorded as superseded
PR-history provenance in `ledger/source-pr-files.jsonl`, while the corrected
proof and audit are retained in full.

The principal unresolved step is a positive-density overlap between the
train-return attachment labels and the independently constructed
grid-linkage attachment labels, or an equivalent direct full-source flow
inequality. Separate linear path counts do not imply such overlap. The report
also gives no uniform KKT stress price for selected paths and no summable
face-defect route charge; neither path family produces a finite competitor.
The exact Pell regression is nonglobal and shows only that separation,
triangle-freeness, and diameter alone permit linear-length disjoint paths. A
marked-rail cut calculation is explicitly weaker than canonical Audit 133.

The candidate registry contains five unreviewed proof-claim records, one exact
regression record, and one nonadvancing-screen record. No source or destination
theorem-state transition, active-route status, or certificate registration is
changed. The authorized 810-entry publication-inclusion membership is
unchanged; its SHA-256 for the edited current Target C prompt is refreshed to
cover this navigation addition. The source report says computation was
not used and provides no finite verifier for its asymptotic claims; the
canonical certificate replay validates only already registered destination
premises. The destination remains private and Gate 2 is not claimed.


## Sixth batch — frozen source PR #948 and retained-copy privacy reconciliation

The source baseline remains `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`
(tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`). Source PR #948 is open
at head `b7376d13b81e542055c5c904bf81bdaf1beb7b9e` (tree
`4d2357368d1a2fa71b318741bf263e9aad342f8a`), with merge base
`d999528cfaafd811a4a19bcfacd00f217c2fc375` (tree
`4eff9ef7cd946225c5810ba23c1f0012a2c77355`). The destination batch starts
from `a10c36842bcd60442f87345ef45e62112faa8c63` (tree
`b631245c34871a3508089b90ec184235a726777a`).

The frozen PR diff has 23 paths: seven mathematical reports, seven verifiers,
seven JSON outputs, the generated source artifact index, and `research/README.md`.
All seven reports were already present at the same destination paths. Exact
line comparison found that each proof body differed only in the publication
transformation from a direct source-PR URL to an internal provenance link,
except for the two historical hosted-CI paragraphs described below. The seven
verifier scripts and seven JSON outputs are exact Git-blob duplicates of the
frozen PR head. They were therefore recorded as duplicates or already fully
represented; none was blindly overwritten. The source artifact-index update
was replaced by the destination-generated index. The source README was not
copied wholesale; its PR-948 mathematical summaries and verifier limits are
preserved in the focused [quarter-fold/bent-array research track](../../tracks/target-c-quarter-folds-bent-arrays.md).

The final PR head also retains two proof-scope clarifications from its history.
Commit `62ad4278120750dba98b13e468e5698e81fe1153` adds the loaded-port
three-contact sign pattern, states that simultaneous feasibility is not shown,
and records that isolate coordinates stay fixed in the reduced rank argument.
Commit `ff83fd52` replaces the earlier weak-dual connectivity explanation with
a curve-through-bounded-faces proof for a 2-connected plane graph. Both
clarifications are already present in the destination report copies. The
source head history was checked; no separate historical report revision with
a distinct retained theorem or counterexample was found.

The research track and seven new registry records describe: (1) convex-face
and eight-face quarter-fold restrictions; (2) deep-face persistence and
isolate-deficit transport; (3) rigid-cycle persistence and the conditional
positive pinned-stress certificate; (4) exclusion of nonconstant large faces
at a feasible full-source quarter-fold; (5) the four-unit rhombic dual-defect
identity and complete-array pair involution; (6) the actual diameter-forest
theorem for complete bent arrays; and (7) linear external boundary attachment
for macroscopic complete arrays. The registry links each claim to its report,
verifier, fixture, canonical inputs, scope limits, and next obligation. All
seven remain **unreviewed**; theorem-state is unchanged. The essential global
bridge remains extraction of the actual complete macroscopic array or a
source-realized full-source endpoint with every lower/upper pair and isolate
retained. Neither branch closes C-II or Level I.

Each of the seven destination scripts was rerun against its already-present
source-identical file and exited zero. The exact finite scope is listed in the
track. These checks validate their declared finite arithmetic only; they do not
certify globality, universal compactness, endpoint existence, or asymptotic
claims by enumeration.

A release-safety sweep removed historical account-specific hosted-CI billing
explanations from the two PR-948 reports that contained them and from two
already-retained first-party reports, one source-main file and one report at
the frozen PR-952 head. The mathematical claims and local-check outcomes were
retained. Source blobs and SHA-256 hashes remain in the inclusion manifest and
per-file ledgers; only the public-copy hashes changed. PR #952 is fully
reconciled in the seventh batch below. The source-main
seed090 row likewise records the existing copy and keeps its cross-target
mathematical reconciliation queued. The authorized inclusion set remains
810 entries.

No canonical dependency, theorem status, registered certificate, or repository
visibility changed. The source remains frozen at its recorded main SHA; all 21
source PR head SHAs still match the recorded open-PR inventory. The destination
remains private. Publication Gate 2 is not claimed and Gate 3 was not requested.


## Seventh batch — frozen source PR #952 owner-release and loaded-anchor research

The frozen source main remains `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`
(tree `e061f039eac44c286a00eacdcaa9a4cbbb877891`). Source PR #952 was open at
head `3536c0b6f6c2a929d9c96fffbdcfc480735fea3` (tree
`a6503b1817dbd885f9378ca42677d811fe363c84`), with merge base
`d999528cfaafd811a4a19bcfacd00f217c2fc375` (tree
`4eff9ef7cd946225c5810ba23c1f0012a2c77355`). The destination batch starts
from `621f7c7dcd5b12c949f83951d1d1521e09bbbe17` (tree
`978550c0ab3248aee7ac41d9e8b5438a53c5687a`).

The exact source diff contains 17 paths: five first-party proof reports, six
saved JSONL finite outputs, four Python verifiers, the generated source
artifact-index update, and `research/README.md`. The per-file ledger has one
row for every path, with the frozen source commit, Git blob, SHA-256, destination
path, destination blob/hash, role, lifecycle, and disposition. Four full reports,
all six outputs, and all four verifiers were already byte-identical in the
destination. The fifth report,
`target_c_outer_owner_amplification_and_common_release_2026-10-10.md`,
was already retained with its mathematical content unchanged; only two lines
describing an account-specific hosted-CI billing annotation were replaced by a
neutral statement that the historical run executed no steps. Its original
source blob/hash remain recorded. The source artifact index was not copied;
the destination index was regenerated. Its source README was adapted into the
new focused [owner-release and loaded-anchor research track](../../tracks/target-c-owner-release-loaded-anchor.md).

The PR's successive final-report additions are preserved at the frozen head.
They develop five distinct candidate packages, all still **unreviewed**:

1. Component anchoring proves a crossing actual-diameter port for each
   contact component under exact contact-preserving owner translation. Under
   canonical relative-interior stress and acute owner directions, every
   nonzero contact-preserving binary selection has positive weighted old-
   diameter gain. Mixed-component refinement is upper-safe after its stated
   deletion bound. An exact connected nonglobal source has a zero-only reduced
   lower formula, so the reduced hypotheses do not imply feasibility.
2. Strict floor closure constructs unequal-height endpoints from exact
   full-source costs, and allows isolates independent variables. The finite
   common-height obstruction does not rule out unequal-height/isolate motion.
3. Inclusive floor closure adds weak equality at contact-opening floors while
   preserving strict pair constraints. Its lexicographic closure returns the
   unique maximal feasible support; the contact-loss version is complete in
   its class, and the locked-contact branch gives a canonical contradiction
   for a surviving proper core group even at its positive floor. An equal-cost
   all-weak path cannot force elimination.
4. The loaded-anchor box gives upper safety under same-owner coverage of every
   upper-relevant label, including assigned isolates. The full-core near-disk
   corollary gives a loaded hull vertex within
   `D(2 eta + sqrt(2 eta)) + rho` of a near-diameter label, but does not supply
   same-owner or crossing-diameter incidence. A native-direction box and an
   Audit.106-conditional owner-count inequality are also preserved in the
   report.
5. Amplitude/common-release candidates build exact implication systems that
   include actual upper pairs, with stress imbalance controlling a loaded-port
   projection. A nonzero maximal assignment would give contact loss, but the
   report's source-extraction plus unary-avoidance theorem is still missing.

The intermediate PR history was checked for changes to these scopes. Commit
`a7a6dfda` supersedes the earlier CT-only next theorem with UCC, which includes
actual upper-pair clauses; `c998f842` adds the stress-imbalance bound and updates
the source-extraction obligation. Commit `8053f34b` adds the native-direction
box and LDE family bound, expanding the finite loaded-anchor count from 324 to
744 pair states. Commit `a223a304` adds mixed-component refinement to the
component report, while `2dea92b9` adds signed clipping to unequal-height
transport. The final reports and candidate registry use these later scopes;
the earlier CT-only obligation and 324-state count are not presented as current.

The focused track, five new registry entries, research proposal index, root
`research/README.md`, Target C `CURRENT.md`, bottleneck brief, and three live
task cards now point to the exact reports, verifiers, outputs, canonical
dependencies, limits, and next obligations. There are 36 candidate-registry
records total after this batch; all five PR #952 records remain unreviewed and
the canonical theorem-state, C-II status, and registered certificate set are
unchanged.

The reproduced finite checks pass on their stated scopes: the inclusive-floor
run enumerates 620 supports and 180 geometric pair states; loaded-anchor runs
cover 744 pair states in nine nonglobal fixtures; source-realized owner-sink,
amplitude, and common-implication modes verify their 194,684 and 250,308 pair
instance families and exact limiting slacks; unequal-height release checks
225,680 pair states. All six verifier outputs reproduce their retained JSONL
fixtures byte-for-byte. These are not proof of canonical extraction, universal
claims, or global optimality. The single exact missing bridge remains a
canonical owner family with owner-respecting loaded ports for every
upper-relevant point and isolate, followed by nonzero support in the exact
full-source lower/upper closure (or a source-specific obstruction/payment).
No full-source endpoint for every canonical minimizer follows from PR #952.
