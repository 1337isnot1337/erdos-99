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

## Source PR #955 — global attainment and annular matching

The source baseline is main
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; the frozen open draft PR head is
`d5afc236a7b1de9567dcb6dda65d957ed91c726b`, tree
`5233d9c8b7774e29609ffaa68cc8dd346c4afa1c`, with merge base
`8c6f37127fbf119fe7ae3745babd1130a6628a09`. The PR's eight source-main-to-head
paths each have a row in the path ledger. Six mathematical/evidence files were
already present byte-identically in the destination; the one-contact report
was adapted only to remove local paths to a third-party paper and text
extraction, replacing them with the publisher DOI. The first-party proof text,
theorem scope, and primary-source attribution remain. The generated source
artifact index was rebuilt from destination state, and the changed source
README's PR #955 content was adapted into a focused destination track.

The one-contact proposition applies to each finite cardinality: starting with
any unit-separated source having an actual unit contact, a midpoint dilation
after moving the contact endpoints inward produces exactly one unit contact
and diameter at most `D + epsilon`, retaining all labels. Thus the triangle-
free and unrestricted diameter infima are equal for every `n >= 2`; Level I
at a given `n` is exactly nonattainment of the triangle-free infimum. It proves
neither eventual nonattainment nor a pointwise strict gap. The unique-contact
descent has no multiple-contact extension. Square, regular-pentagon, and
`n=8` global-optimum families remain finite regressions against broader
connectivity claims, not an unbounded counterexample. A weaker
stress-component route is expressly subsumed by canonical Section 64.3.

The separate annular result studies a specified full comparison packet `X`,
including every pair at distance at least `D`. Its exact strict-sub-`D`
retention size is `M_D(X)=|X|-tau(G_D(X))`; an angular deletion makes the
conflict graph bipartite and yields the stated matching-cover error. For
arbitrary clouds at `delta=c D^(-1/3)` the error is at most
`floor(8 sqrt(c) D^(1/3)+16 c^(3/2))`. The optional `O_c(1)` lattice result
uses the existing translation-uniform circle-count theorem and no stronger
discrepancy estimate. Full finite triangle-free packets and the
complete-bipartite saving examples are explicit **nonglobal** regressions;
they do not improve a universal reserve constant.

The destination reran the one-contact verifier and the annular verifier. The
annular run's aggregate JSON matches the frozen saved fixture exactly. Its
`--certificate-json` mode also generated and committed a separate 398,846-byte
certificate with 52 exact graph proofs (48 disk packets, three full-column
packets, and the odd-cycle case), plus kernel controls over 1,024 five-label
graphs and four mutations. The verifier script, saved aggregate fixture, and
generated certificate are linked from the track and candidate registry.

The exact remaining global bridge is a source-specific admissible packet with
`M_D(X) >= n` for every sufficiently large triangle-free global minimizer, or
another proof of eventual nonattainment. Lattice closeness and finite packets
do not supply it. The [focused track](../../tracks/global-level-i-attainment-annular-matching.md),
[machine-readable candidate records](../../../targets/target-c/candidate-registry.json),
and navigation in the active Target C frontier record both routes as
unreviewed. The source AI audit is retained as provenance; it is not a
destination promotion audit. No canonical theorem, Level I status, or C-II
status changed.

### Revalidated successor hashes for two source-main audit ledgers

The full source-provenance verifier found two stale public hashes in the
source-main artifact ledger: `target_c_integration_audit_ledger_2026-10-06.md`
and `target_c_referee_run_ledger_2026-10-10.md`. Both paths contain the later
source PR #947 audit-ledger successors, with their status guard and, for the
referee ledger, the documented workflow-status wording edits. The source-main
rows now point to those exact destination hashes and reference the frozen
PR #947 source heads and per-file records; their original source-main blobs
and hashes remain unchanged in the ledger. This reconciles provenance only;
it changes no mathematical claim or theorem-state.

## Source PR #956 — global reserve, lattice, interface, and stress regression

**Frozen source state:** main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; open draft PR #956 head `bbc549f36ac964fd7eee211782eb2c979d12af32`, tree `3d8550adf520dcacd17876d6ddf1970a6c9e857e`; merge base `eb51394f371aee958b0d9332f80faf75ae694b9e`. The PR adds four full analytic reports and four verifiers, modifies the artifact index, adapts the research README, and adds one source AI audit. All eleven source paths have exact blob/SHA-256, destination relation, lifecycle, rights treatment, and proof role in `ledger/source-pr-files.jsonl`.

### Distinct mathematics preserved

1. **Boundary zigzag.** A complete row-replacement and cross-packet ledger proves that every translate of the unit triangular lattice crop to radius `R >= 640000` admits a unit-separated competitor with at least `R/160000` additional points. Applying global minimality at strict smaller radius and then taking the radius to `D/2` yields `g_A >= D/320000` for every global minimizer with `D > 1280000`. This is a separate proof architecture from source PR #1008's stronger unreviewed `D/600` reserve for `D >= 10^6`; it is retained as a distinct derivation, not represented as an improvement or subsumed duplicate. Neither result is canonical.

2. **Lattice count, defect, and periodic motifs.** A finite subset of any translated unit-separated rank-two lattice with actual diameter `D >= 1` obeys `|S| <= aD^2 + 86D^(4/5) + 1`, `a=pi/(2sqrt(3))`, uniformly over shape, phase, and orientation. Conditional on item 1, the report obtains `k_rho(A,Lambda) >= (c-4a rho)D - 4a rho^2 - 86(D+2rho)^(4/5)`, with `c=1/320000`; for `rho=10^-7`, this yields at least `D/640000` labels outside every such lattice for sufficiently large global minimizers, including isolates. For `1 <= q <= D/16`, its full-periodic-packing estimate is `|S| <= aD^2 + 114q^(6/5)D^(4/5)+q`, conditional on the *whole infinite packing* being separated across all cosets. For a global minimizer with `D > 1280000`, the reserve then forces a growing period-cell population, but no periodic extraction. The exact separated 39-lattice finite union is a nonglobal, triangle-free regression and blocks the shortcut that finite lattice populations can be summed without validated interfaces.

3. **Straight interfaces.** For two full lattice half-planes with parallel front rows and every cross-pair unit-separated, the report proves `2g >= a0(1/s_A+1/s_B) - N(V_A-a0)/s_A - M(V_B-a0)/s_B`; at minimal covolumes it gives `g >= (h_A+h_B)/2`. It also retains a finite-window endpoint term. This does not supply complete half-plane extraction from canonical coherent grains, `o(D)` junction/outer costs, disjoint gap-area allocation, or an all-source-label decomposition. The report's link to canonical `C-COHERENT-GRAINS` is contextual; it does not strengthen that theorem.

4. **Stress and density regression.** The regular odd ring has positive contact and diameter equilibrium weights and exact mixed rigidity rank `2q-3`; it is locally isolated at fixed labels modulo rigid motions. Adding strictly interior, contact-isolated labels gives a triangle-free family with `n_q/D^2 -> a`, but the source is explicitly nonglobal: a same-cardinality competitor has diameter `<D-4`. It proves that the listed local stress, rigidity, hull, and density assumptions alone cannot force a uniform positive quadratic-density loss. It is neither a global minimizer nor a counterexample to Level I.

### Audit and release treatment

The source AI audit reconstructs the boundary and lattice proofs, checks the exact pair ledgers and literature scopes, reviews the infinite interface and finite-window hypotheses, and scrutinizes the ring stress and nonglobal comparison. Its private-receipt wording was rewritten to refer only to the source PR audit; its source claim that human review is required was corrected to the destination policy: a separate independent AI-agent exact-head review is required before consequential promotion. No mathematical claim was altered by that policy edit. Third-party papers are cited or linked, not copied. The destination artifact index was regenerated from retained destination content rather than replaced by the source index. The source README became a focused catalogue entry, not a wholesale overwrite.

The candidates remain outside theorem-state; no Level I, A/B, C-I, or C-II status changed. The four scripts validate finite/formal checks only and do not prove the universal analytic statements. Exact command results and environment are in the PR #956 verification receipt.

## Source PR #957 — joint diameter-cover exchange

**Frozen source main:** `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
**Frozen open draft head:** `a11e16998094ab3d7afd9fd07eff8b55909ec406`
(tree `77ce8dd135c2b4233f121bd448621d362841da06`). **PR branch merge base:**
`d6f953100d62a84de72e991642041fdd026e82ba`. The source PR had seven actual
branch-delta paths; their original blobs, treatment, rights/safety handling,
and destination hashes are recorded individually in `ledger/source-pr-files.jsonl`.
The separate source-main-to-head manifest includes stale snapshot differences
because source main advanced 24 commits beyond the branch base. Those differences
are not applied as PR changes.

### Mathematical content and lifecycle

For any unit-separated source `A` of diameter `D` and any unit-separated packet
`B` with diameter below `D`, the report defines the actual source diameter graph
`H` and complete lower/upper cross-conflict graph `G` (`<1` or `>=D`). For a
vertex cover `T` of `H`, let `nu_T` be the maximum matching between `B` and
`A minus T`. Its theorem proves that the maximum cardinality of a unit-separated
strict-`D` subset of the labelled union is exactly
`n+m-min_T(|T|+nu_T)`. Hence a global minimizer must obey
`|T|+nu_T >= m+1` for every supplied packet and cover, retaining every isolate.
The exact missing Level I theorem is existence of a unit-separated shorter
packet and actual-diameter cover with joint cost at most `m` for every
sufficiently large triangle-free global minimizer. No such packet existence is
proved, and the theorem-state remains unchanged.

Four small rational controls show that minimum-cardinality diameter covers
alone can fail, a smaller packet can still augment the source, a supplied
packet can fail even for the global square, and upper cross conflicts can form
`K_(4,3)`. Only the lower-conflict graph is planar. The all-`k` dense-star
construction has one unit contact, `n-2` contact isolates, triangular leading
population, a matching cross-conflict graph, and a same-cardinality competitor
at diameter `D-1/8`; it is explicitly nonglobal. Its role is to reject a
minimum-cover-first search, not to challenge Level I.

The run note preserves other explored mechanisms and their limits. Its rational
four-label cage is a separate local regression: for arbitrary prescribed `R`,
a triangle-free positive surrounding relation can coexist with a free radius-`R`
ball whose boundary is arbitrarily close to a contact-bearing center. It
prevents deriving a uniform local free-region propagation radius from
triangle-freeness alone. The four-label source is nonglobal. The destination's
existing two-copy similarity obstruction is related but distinct: the former
is a bounded local cage with an explicit arbitrary-radius placement, while the
latter is a dense ring with no uniform affine-span gap.

### Stale branch differences and release edits

The frozen branch's source-main-to-head name-status also shows older versions of
`target_c_atomic_orbit_sharp_detour_independent_audit_2026-10-08.md`,
`target_c_half_depth_fan_forest_independent_audit_2026-10-08.md`, and
`research/target_c_g0050_physical_boundary_propagation_2026-09-14.md`. None has a
commit in the actual `d6f9531..a11e169` PR range. The destination retains the
frozen source-main audit versions; the latest source-main G0050 file remains
separately queued in `source-main-artifacts.jsonl` and must be imported from the
frozen main version, not replaced with the stale branch snapshot.

The source AI audit was release-edited to distinguish provenance from the
destination's independent exact-head AI review. The run note's local worktree
and account-specific hosted-CI explanation were removed; it now records only
that hosted steps did not execute. The external Schurmann paper remains a
bibliographic citation/link only. The source index was not copied over the
destination catalogue, the destination index was regenerated, and the source
README was adapted. No claims were promoted; Level I, A/B, C-I, and C-II status
remain unchanged. The exact local verifier and repository check results are in
[`receipts/target-c-pr957-local-verification.json`](receipts/target-c-pr957-local-verification.json).

## Source PR #958 — colour lifts, planar rank barriers, and finite palettes

**Frozen source state:** main 42f0296d1aca068c809f74cee5dcdb4ebdb27c73; open draft PR #958 head 0a72556e786024c9313c7d6287e26c20c1e9b9b8, tree 7b37e2fc5af3bb2e0471a690195a21f9d9fd0d2c; merge base d6f953100d62a84de72e991642041fdd026e82ba, tree 3d6ac96556b891d7b17ea7c13ae9364e0c5082f0. The exact PR delta has 11 paths. Every path has a source blob, byte count, SHA-256, lifecycle, dependency and explicit disposition in ledger/source-pr-files.jsonl.

The three substantive documents preserve two complete first-party reports and one source AI audit. The audit was retained as provenance and edited to state the destination's exact-head review policy; it is not a substitute for destination review. The reports claim:

1. For every finite unit-separated source of diameter greater than one, squared-distance interpolation \(d'_{ij}{}^2=1+\lambda(d_{ij}^2-1)\) preserves contacts and strictly contracts every distance above one. Its centered Gram matrix has rank \(n-1\); this blocks a planar realization for \(n\ge4\).
2. A triangle-free contact graph is 2-degenerate, so three colours suffice. Assigning a regular-simplex height to each colour gives a contact-preserving strict diameter descent for every source label in \(\mathbb R^4\), for sufficiently small positive parameter. This does not give a planar endpoint. The square lift has rank three.
3. The specified lift flattens exactly when centered colour vectors lie in the centered source-plane span. Two used colours require parallel colour lines; three used colours cannot flatten for \(n\ge4\).
4. For supplied planar targets, all lower and strict upper constraints reduce to two explicit quadratics for every unordered pair at one common endpoint parameter. Feasibility of the endpoint does not require a feasible interpolating path, but the report does not supply targets for all global minimizers.
5. For a finite palette, an acceptable endpoint exists exactly when the complete lower/upper conflict graph has an independent transversal choosing one option per label.

**Content comparison with frozen source PR #960:** its report
global_planarity_and_radius_barriers_2026-10-12.md contains the same general
squared-distance interpolation and rank-\(n-1\) nonplanarity obstruction, with
parameter \(t=1-\lambda\). These are the same mathematical claim, so this
candidate is not counted as a distinct result from PR #960. PR #960 further
analyzes why rank-two truncation preserves the original affine image and gives
separate enclosing-radius and finite replacement results; those additions
are now preserved in the focused PR #960 track below. PR #958's triangle-free contact-colour
lift, exact flattening condition, all-pair endpoint quadratics, and palette
regressions are distinct and remain fully recorded here.

The finite source controls are deliberately bounded. A unit regular 43-gon has a verified three-translation strict endpoint with all 903 pairs checked, but it is nonglobal. For one fixed alpha and palette, the permissive 175-label system checks 2,039 constrained pairs and exhaustively rejects all \(3^{175}\) assignments. An independent 175-label packet checks all 15,225 pairs and has squared diameter below 183.2352, so the filled source is itself nonglobal. Thus a rim improvement need not extend to the inactive population, and a palette-specific failure is not a global obstruction.

**Exact destination verification:** the colour-lift verifier passed in isolated CPython 3.14.6 with SymPy 1.14.0 and mpmath 1.3.0. The palette verifier's self-contained 43-gon mode passed 4,100 Boolean-kernel controls and all 903 endpoint-pair checks with a 13-node search. Its 132/175 data-dependent run was not repeated because redistribution permission is unresolved. The source audit records its prior replay; this report does not claim an independent destination replay of those tables. Both analytic reports and the source audit remain noncanonical and unreviewed; no theorem-state, canonical claim, Level I, A/B, C-I, or C-II status changes.

**Per-file disposition:** the two reports, exact interval helper, palette verifier, colour-lift verifier and attribution JSON are integrated. The audit is retained with lifecycle clarification. The destination artifact index was regenerated, and the source README was adapted into destination navigation. The attribution JSON was transformed to remove an unavailable source-branch fixture pointer while preserving the prior-lineage note, source URLs, and hashes. Packomania's cci132.txt and cci175.txt are the two explicit rights-blocked source paths: the destination retains only their source URLs and hashes. The report and verifier describe how an authorized local copy can be passed with a fixture-directory argument. The inspected [Packomania homepage](https://www.packomania.com/) and [submission-format page](https://www.packomania.com/hints.html) did not provide an explicit redistribution grant.

The precise remaining global step is a planar, full-label endpoint of diameter strictly below D that respects every lower pair bound for every sufficiently large triangle-free global minimizer, or an independently established unbounded family of such global minimizers. A four-dimensional descent, one finite palette, a successful rim replacement, or finite exhaustive failure for one palette does not supply that statement.

## Source-main exact-phase packet and cross-shore batch

The next focused integration uses the same frozen source-main commit
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73` (tree
`e061f039eac44c286a00eacdcaa9a4cbbb877891`) and destination base
`4ce4fed103532ad42919896d025df1a6d4b72405` (tree
`84318253c282e851aa1bbbad1dfd2dbba389ba16`). It brings ten source-main Target
C reports into the destination and archives one older r1 report as an exact
historical source copy. Five supporting research files are integrated; the
laminar multishear proof itself was already an exact destination duplicate.
Source blobs, byte hashes, source lifecycle, link transformations, and
destinations are in the [artifact ledger](ledger/source-main-artifacts.jsonl),
[research-file ledger](ledger/source-main-files.jsonl),
[dependency ledger](ledger/source-main-dependencies.jsonl), and
[closed-PR file ledger](ledger/source-closed-pr-files.jsonl).

Mathematically, the r2 complete-grid report gives the stated joint switch
inequality and bounded-cusp consequence under its exact crosscut hypotheses.
The threshold packet reports separately establish edgewise transverse KKT
balance, many bounded support packets, strictly positive but not uniformly
bounded packet resultants, and an internal load shared across the opposite
shore's cut equations. The conditional two-cut shear shortens a linear
selected family when the opposite shore is not exact phase; this does not
control every actual diameter pair. The nested matching report gives
`Omega(D^(1/4))` pairwise-crossing actual-diameter edges with one common cut and
full or nested terminal opposite-shore support. These are distinct candidate
strengthenings and are not treated as redundant with the destination's cubic
support budget or canonical Type-II floor.

The exact remaining proof gap is quantitative and global: packet positivity
does not bound aggregate load away from zero, boundary and layer rows may pay
the opposite-shore correction, and the two-cut move does not produce a full
source endpoint. The exact-phase branch still leaves split-star and
inactive-interface cases. The imported full-span hostile audit's source
classification is preserved as provenance only; the destination artifact
state remains unreviewed. The old r1 joint-switch report is visibly superseded
by r2, and the historical train-closure route snapshot is archived without
retaining its source-side lifecycle as destination authority.

The exact laminar multishear verifier is run locally for its own finite scope.
The packet, r2, full-span-audit, and positive-prefix reports contain no
computational verifier. The route track and candidate registry record this
boundary and the missing whole-source endpoint. No canonical claim, C-II or
Level I status, inverse-phase correction, inclusion entry, or repository
visibility changes in this batch.

The selected closed-PR comparison records ten exact changed paths from source
PRs #603, #605, #606, #607, and #613. PR #603 is closed unmerged and its
current source-main versions remain the import baseline. The #605/#606 source
main reports and the #613 rail-deep-attachment report/verifier are queued for
the next focused source-main batches. PR #607's rail-saturation deletion did
not survive on source main; source main and destination retain the exact same
bytes. The source #613 generated artifact-index change is not copied; the
destination index is regenerated from its own artifact headers and manifest.

## Source PR #959 — reflected-scale criteria, moment obstruction, and capacity loss

**Frozen source state:** main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; open draft PR #959 head `e25041f236d268a7e815dacd346180989690ed71`, tree `a0b268d8b050e0350c8ae2ffb38c139fc6570dab`; merge base `a43c69dac7e7b0627dec2900e12c60fd4608d519`. The exact PR delta has nine paths. Each path has source blob SHA, byte count, SHA-256, lifecycle, dependencies, treatment, and destination mapping in `ledger/source-pr-files.jsonl`.

The three mathematical reports and both exact checkers are retained. The reflected-scale report proves a necessary-and-sufficient parity test for the actual two choices per label when a line, offset, and positive scales are supplied. Its finite certificate checks all 12,246 pairs on 157 labels, includes two contact isolates, and strictly lowers squared diameter from `916` to `865065744/1008005`; the source is nonglobal. Its infinite rectangle family escapes the stated affine obstruction, but its PSD stress is boundary-supported and does not imply full-source rigidity or optimality. The verifier also checks fixtures with 29,403 and 182,710 pairs.

The moment report proves that for any leading-density sequence, every feasible one-step reflected-scale endpoint with all labels retained and diameter at most `(1+o(1))D` has both squared scales tending to one. It allows arbitrary offsets and sign assignments and uses canonical Oler plus the empirical disk limit. It gives no rate, strict lower-order improvement, or endpoint existence. The finite moment identity retains the odd-moment terms that are not forced to vanish for finite asymmetric sources.

The Steiner report gives two distinct capacity regressions. The four-label rotated square is an actual triangle-free global diameter minimizer with `N(K)=4` and `N(SK)=3`. The separate unbounded rhombus family is triangle-free and exactly optimal for its fixed container, yet loses linearly many capacity sites after symmetrization; the large sources are nonglobal for diameter. This defeats the general `N(SK)>=N(K)` bridge and variants based only on triangle-freeness, fixed-container optimality, or leading density. It does not refute an eventual theorem using geometry specific to large global minimizers.

The historical source audit is preserved as first-party AI-audit provenance, with its claim that human review is required corrected to the destination policy: it is not the independent exact-head AI-agent audit required before consequential promotion. The run note retains the negative exploratory search only as historical, inconclusive evidence; account-specific hosted-CI details were removed, and no unexecuted CI is reported as passing. Two exact verifier files are byte-identical to source. No external PDFs, protected tables, private paths, or theorem-state changes are included.

The focused navigation is in [the PR #959 research track](../../tracks/global-reflected-scale-capacity-pr959.md), with machine-readable candidate claims in the [registry](../../../targets/target-c/candidate-registry.json). The next bridge is source-derived near-identity signs and scales satisfying every lower and upper pair constraint for all sufficiently large triangle-free global minimizers, or a full-label capacity/repacking result that uses their global geometry. No Level I or C-II closure is claimed. This is a separate route from the PR #958 colour/palette method and the PR #960 rank/radius analysis below; shared endpoint goals do not establish redundancy.


## Source PR #960 — factorized maps, sharp-reserve regression, and planar barriers

**Frozen source state:** main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; open draft head `c75e519426e3a88839567411fe3381160f3aa3cb`, tree `65f7e6e67cbead52038792617df9de48208d99d7`; merge base `a43c69dac7e7b0627dec2900e12c60fd4608d519`. All 11 PR paths have exact source and destination identities in the [per-file ledger](ledger/source-pr-files.jsonl).

The three complete reports and four executable verifiers, graph helper and source AI audit are retained. The source audit is provenance only; its references to a private closeout receipt were removed, and its review language now matches the destination independent exact-head AI-agent audit policy. The source README was adapted and the destination artifact index regenerated.

The balanced-incidence logarithmic obstruction is a realized special case of the stronger formal-array convex-hull theorem already present in `global_separable_distortion_obstruction_2026-10-12.md`; it is preserved as a direct full-source metric treatment and not counted as a new independent obstruction. PR #958 already has the same squared-distance interpolation rank-`n-1` result. PR #960 adds the rank-two truncation/affine limit, enclosing-radius obstruction and six-point equal-radius replacement.

Distinct additions are the constructive directed-cycle/DAG alternative (the acyclic case yields only an abstract full-pair array); an unbounded triangle-free nonglobal family meeting the sharp `D^(2/3)` population reserve while blocked by every vertex-factor map; and complete exact fixtures for graph separation, dense factorized stability, radius and diameter replacement. The sharp-reserve family fails the KKT identity and has a strict same-label horizontal contraction, so it is not a counterexample to global-minimizer results.

The [focused track](../../tracks/global-factorized-distance-planarity-pr960.md) links all reports and candidate entries. The missing step remains a source-derived planar strict-`D` endpoint with every lower and upper pair bound for every sufficiently large triangle-free global minimizer, or a unit triangle. No canonical claim or theorem-state is changed.

## Merged source PR #995 — vertex-factor pole test and hull/train reconciliation

The vertex-factor report and exact checker are preserved as noncanonical support. Its general Möbius/anti-Möbius classification and balanced-incidence obstruction overlap the existing stronger formal-array result and PR #960. Its distinct all-pair pole test gives strict-sub-`D` feasibility exactly when an inversion pole satisfies `M(x) < D^2 m(x)`, equivalently a finite family of strict quartic inequalities covering inactive pairs. It also retains a nine-label nonmetric factor array, a four-label three-dimensional metric with no planar realization, and an exact seven-label inversion competitor with two contact isolates and squared diameter `202/13 < 16`. These fixtures establish neither a large family nor globality.

The merged hull/train report maps five older Target C research programs and preserves a conditional same-host/chord fork with no diameter edge, route payment, or endpoint. The related bulk-separator checker is an exact duplicate of an existing file. The operational recovery record is excluded because it contains private preservation operations; no mathematical proof input is lost. The [PR #960/#995 track](../../tracks/global-factorized-distance-planarity-pr960.md) gives exact proof limits, next obligations, dependencies and commands. Source and destination per-file treatment is recorded in the [ledger](ledger/source-pr-files.jsonl).

## Source-only branch `research/sol/target-c-level1-gpt61-2026-10-04`

Frozen at head `9875cd6a77939bb6347353fc798ab8f9ab03ec3e` and tree
`198c83065add8175a921b4e9c55169e4690010a3`, this branch is not one of the
open PR heads. Its branch-specific delta is measured from merge base
`0351e2c529e01750f7aceb87f8f6f0cb9c21dea7` and comprises 19 paths. The
[`source-branch-files.jsonl`](ledger/source-branch-files.jsonl) records each
path's source commit, Git blob and SHA-256, source lifecycle, destination
relation, transformation, and rights treatment.

Five proof reports and five verifier scripts were exact destination
duplicates. The one-vacancy, actual unit-wall, boundary-vacancy, and triangular
two-pin proofs were retained as existing full reports; their identical
verifiers remain attached. The multishear report was also already present, but
its missing exact verifier is imported here. Three distinct full reports—one
boundary pin, two-side polynomial refill, and universal convex-pentagon
capacity—and their three exact verifiers are imported byte-for-byte. No
candidate is classified as redundant merely because it studies refill or
capacity: their angle ranges, deleted labels, polynomial margins, frame sizes,
and conclusions differ. Their exact individual scopes are in the [capacity
track](../../tracks/target-c-capacity-collective-refill.md) and registry.

The branch's synthesis addenda and reproduction summaries are preserved
through that track, the eight candidate records, and task prerequisites. Its
generated index was not copied; the destination index was rebuilt from its
own retained report headers. A source-only lifecycle narrative and one
nonmathematical conversation-specific closing line were omitted. All eight
verifiers pass with the recorded finite counts; none independently audits the
analytic statements, global optimality, or canonical source extraction. The
destination theorem-state, corrected inverse-phase demotion, and C-II/Level I
status remain unchanged. No third-party paper text, credentials, or private
infrastructure references were imported. Destination visibility remains
private.
