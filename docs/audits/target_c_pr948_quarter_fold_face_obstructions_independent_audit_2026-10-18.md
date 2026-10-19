<!-- theorem-state: {"artifact_id":"ART-D1153290BF46","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit: PR #948 quarter-fold face obstructions

**Verdict: PASS at the exact conditional scope below.** The proof reconstruction
supports the contact-release lemma, the exact-graph exclusion of bowed or
occupied eight-faces, and the short-arc/count reductions through degree 18. It
does not construct an endpoint or change the C-II or Level I status. The source
candidate remains unreviewed/noncanonical pending a separate maintainer
disposition; this audit is evidence, not a theorem-state transaction.

**Audit date:** 2026-10-18.

## Frozen source and audit boundary

- Destination `origin/main` and reviewed tree: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- The assigned artifact is the already published candidate
  `TARGET-C-PR948-QUARTER-FOLD-FACE-OBSTRUCTIONS`, imported from source PR #948
  at `b7376d13b81e542055c5c904bf81bdaf1beb7b9e` (source tree
  `4d2357368d1a2fa71b318741bf263e9aad342f8a`). It is not a review of any later
  fleet output.
- State / priority / catalogue: `2026-10-15.publication.2` /
  `public-frontier.3` / `public-frontier.9`.
- Published report:
  [`target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md`](../reports/target_c_quarter_fold_face_obstructions_slot02_2026-10-10.md),
  SHA-256 `e441995708568951a3dd5eafcd162bf398669a46eaab99c91f142efc46e18f2f`,
  destination blob `5bd64db4c7e9dcad18e20bb820fb5adab24785e5`. The recorded source
  SHA-256 is `7e40311e66f4aaf609274eb6ca24b4ac455836e32ff650765abc37189a5f6a52`.
- Exact verifier:
  [`verify_target_c_quarter_fold_face_obstructions_2026_10_10.py`](../../research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py),
  SHA-256 `ced2ae1bb3ee3834f0a36d5869d25c7aedc0e447df2c8bb17013cf1d4a0a7d89`,
  destination blob `55a505dda56672c174372f71a725de5471e93589`.
- Saved finite output:
  [`target_c_quarter_fold_face_obstructions_certificate_2026_10_10.json`](../../research/target_c_quarter_fold_face_obstructions_certificate_2026_10_10.json),
  SHA-256 `0ebf7367629a7555ce379b77f11af81b63d9e973eb0b84fd9a5eaee0512a3857`,
  destination blob `fad23c6de526520582ca54f079138ef1ade31e87`.

The candidate registry and pinned candidate record classify this report as
unreviewed and list no earlier exact-head checks. Destination Audits 83, 228,
and 229 independently establish the canonical face-classification, transformed
hull-cover, and minimum-face-size inputs. They do not audit the new finite
contact-release/automatic-faciality argument or the short-arc/count theorem in
this report. Audit 225's one-isolate bound has a different hypothesis and does
not subsume the reverse-cover argument here. The offline overlap intake had
complete saved coverage of the then-current open pull requests, Issues and
Discussions; its only open pull was unrelated Target A PR #102. A live read of
Discussion #83 likewise found no quarter-fold handoff. The assignment's
`existing_checks` list was empty.

## Concrete question and falsification plan

The candidate asks whether (i) an exact-contact-graph, full-source, unit-
separated endpoint of diameter at most `D` can carry a bowed nonconstant fold on
an old convex actual eight-face, and (ii) local boundary feasibility alone
forces each arc turn below `pi/3`, with opposite arc counts sufficiently close
to force even degree through 18. The first implication can remove an
exact-graph endpoint branch in the canonical C-II search; the relevant source
objective is the lexicographic pair (unit contacts, actual diameter pairs) at
diameter `D`, with all old lower and upper pairs retained. The second only
restricts candidate face signs and counts.

The falsification checks were: search for an edge or source label that could
enter the folded cycle despite the strict hull cover; test the reflex release
against every finite lower and upper pair margin; test the reverse cover against
an old interior isolate; challenge the count bound with an unequal opposite
pair and with odd degree 19 or larger; and replay the rational/algebraic bowed,
straight, and odd-cycle controls. Stop after these implications and controls:
no further endpoint search is part of this audit, and neither result may be
used as a source-extraction or global-closure theorem.

## Independent proof reconstruction

### Reflex-vertex contact release

For a simple bounded actual contact face in a finite unit-separated source, the
straight unit-contact graph is planar: a crossing of two nonincident unit edges
places a pair of distinct source labels at distance below one. A nonincident
label cannot lie in a unit edge either. Thus a reflex face vertex `v` has an
open face sector of angle greater than `pi` with no contact ray in it. The
complementary closed cone containing all unit-neighbor vectors has angle below
`pi`. Moving `v` a small distance along the direction opposite that cone's
bisector makes its dot product with every unit-neighbor vector strictly
negative, so each incident unit distance becomes strictly greater than one.

The reflex vertex is not extreme in the convex hull of the source, since the
face interior sector of angle above `pi` lies in that hull. An endpoint of an
actual diameter pair is uniquely exposed: if `|v-z|=D`, the supporting
functional in direction `(v-z)/D` has equality at no other source label.
Therefore the reflex vertex is not a diameter endpoint and every incident
upper pair has positive slack below `D`. Finiteness also gives positive slack
above one for every incident old noncontact. Choose the displacement smaller
than half of both applicable margins. The exact squared-distance derivative
strictly opens every contact; the triangle inequality preserves all old
noncontacts above one and all upper pairs below `D`. No label is deleted or
added, and the contact graph only loses edges, so triangle-freeness persists.
A smaller diameter contradicts global minimality; diameter `D` contradicts
contact minimality. This proves the finite contact-release lemma, including
contact isolates among the fixed labels.

### Exact-graph eight-face exclusion

For the old and folded convex face cycles, the signed quarter-turn multiplies
each consecutive-edge determinant by `s_(i-1)s_i`. The four sign transitions
have old turns strictly between `pi/3` and `2pi/3`, so their folded turns are
strictly negative. A convex folded cycle must therefore be clockwise. At every
same-sign vertex, convexity then forces its old turn to be zero. Hence a
nonconstant fold with both cycles convex has four straight arcs and a
parallelogram boundary.

Now let the full placement retain the old contact graph, be unit-separated,
and have diameter at most `D`. Global minimality makes it a contact-minimal
triangle-free minimizer at diameter `D`. The boundary-local minimum-face result
gives two edges per arc on an eight-face. If any arc bows, the canonical strict
transformed-hull cover puts every point of the boundary convex hull within
strict distance one of a boundary label. Unit separation therefore excludes
every other source label from that hull, including all isolates and core labels.
The folded cycle is simple by planarity, has no nonconsecutive contact chord by
exact-graph preservation and the old actual-face property, and contains no
other source label. It is consequently an actual bounded face in the new
placement. The bowed arc gives a positive turn determinant while transitions
remain negative, so that face is nonconvex, contradicting the contact-release
lemma. This rules out every bowed arc without assuming that the other labels
stay fixed or that the old embedding persists.

In the surviving straight case the reverse fold of the eight boundary labels
has increments `s_i J(s_i J q_i)=-q_i`, so it produces the old cycle up to a
translation. The transformed boundary labels themselves form a convex actual
face in the eight-label subsource: their only contacts are the cycle edges.
Applying the canonical weak hull cover to this reverse fold covers the old
face hull by closed unit disks centered at its boundary labels. Any old label
strictly inside the old actual face is a contact isolate and is strictly more
than one from every boundary label; that contradicts the cover. Thus the old
face is empty of source labels. This implication uses the weak cover, not a
strict-cover claim in the flat case.

The local angular corollary is also valid at its stated nonuniform scope. At
the quarter turn the compact boundary hull has a uniform strict-cover radius
`rho<1`. Perturbing each boundary label by at most `eta` moves the convex hull
by at most `eta` and the nearest boundary label by at most `eta`; choosing
`rho+2 eta<1` preserves the no-slot property. The mixed turn-determinant signs
persist on a sufficiently small angular interval. This gives a source-specific
interval, not a uniform bound as margins vanish.

### Short-arc and count reduction

Let `T_i` be the internal turn of arc `i`, and write its first and last edge
directions relative to its parallelogram-chord direction as `-a_i` and `+b_i`,
where `a_i,b_i>=0` and `T_i=a_i+b_i`. Consecutive parallelogram chords turn by
`kappa_i` and `kappa_(i+1)` with sum `pi`; the adjacent old transition turns
are

```text
tau_i     = kappa_i     - b_(i-1) - a_i
tau_(i+1)= kappa_(i+1) - b_i     - a_(i+1).
```

Adding and using `tau_i,tau_(i+1)>pi/3` gives
`T_i + b_(i-1) + a_(i+1) < pi/3`, hence `0<=T_i<pi/3`. The chord vector is
the sum of `r_i` unit edge vectors lying within `T_i/2` of the middle direction,
so its projection yields
`L_i >= r_i cos(T_i/2) > (sqrt(3)/2) r_i`, while the triangle inequality gives
`L_i<=r_i`. Opposite parallelogram chords have equal lengths. If their arc
counts are `R>=r`, it follows that `R < (2/sqrt(3))r`. An unequal pair with
smaller count `k<=6` would have `R>=k+1>=2k/sqrt(3)`, a contradiction because
`3(k+1)^2-4k^2=-k^2+6k+3>0` for `1<=k<=6`. The other two arcs each have at
least two edges, so the first unequal case is `(7,8)` and needs total degree
at least 19. Thus opposite counts are equal through degree 18, and every odd
convex actual face of degree at most 17 has constant signs.

No step assumes a full-source upper bound for the local count theorem. Conversely,
the endpoint exclusion specifically needs the exact graph and diameter-at-most-
`D` hypotheses. The proof does not imply a feasible nonaffine assignment.

## Falsification controls and reproduction

The published verifier uses exact rational / `Q(sqrt(15))` arithmetic and
enumerates complete finite pair ledgers. Under the shared single-threaded
compute lock I ran:

```text
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py > /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/homelab-14/quarter-fold-verifier-rerun.json
cmp /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/homelab-14/quarter-fold-verifier-rerun.json research/target_c_quarter_fold_face_obstructions_certificate_2026_10_10.json
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/venv/bin/python research/verify_target_c_face_coupled_quarter_folds_2026_10_07.py > /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/homelab-14/audit83-verifier-rerun.json
cmp /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/homelab-14/audit83-verifier-rerun.json research/target_c_face_coupled_quarter_folds_certificate_2026_10_07.json
```

Both outputs matched their saved JSON byte-for-byte. The first output hash is
`0ebf7367629a7555ce379b77f11af81b63d9e973eb0b84fd9a5eaee0512a3857`; it
checks the bowed eight-cycle and finite two-contact release, a straight mixed
eight-cycle with a diameter-pair switch, an odd 21-cycle, and all count vectors
with four arc lengths at least two and total degree 8–18. The odd 21-cycle has
an exact 25-site square-grid competitor bound of `D^2<=32<58`, so it is
explicitly nonglobal and blocks an all-odd-degree extrapolation. The second
output matches the Audit.83 regression certificate with SHA-256
`a4f9fcf2e94a8fca4f4ec188e6c04e0a1c3e073d4db25ee689241a876173253e`.
These runs verify finite arithmetic and the canonical compatibility controls;
they do not prove either universal analytic lemma or global optimality.

## Limits and next lemma

The report excludes only the stated full-source exact-graph endpoint branch;
it does not exclude endpoints that change contacts, other finite replacements,
or strict sub-`D` competitors. The short-arc result assumes a simple convex
actual face and a lower-feasible, triangle-free nonconstant boundary fold. It
does not control larger odd faces (degree 19 is the first unruled odd size),
labels outside eight-faces, inactive upper pairs, or realization of signs on
the entire core. The finite 21-cycle is a nonglobal regression, not evidence
about a global-minimizer family.

The remaining route lemma is: for every canonical C-II survivor, either
construct a nonaffine integrated sign field and a placement of every label
that keeps all old contacts unit, all noncontacts strictly above one, all old
actual-diameter pairs at most `D`, and every old nondiameter strictly below
`D`, while satisfying the surviving face constraints; or prove a different
same-cardinality finite replacement with the required lexicographic or strict-
`D` improvement. This audit supplies neither alternative.

## Provenance and review role

Source credit remains with the author of source PR #948, worker slot 02; the
imported artifact does not record that worker's model/session, so none is
inferred. This review was performed independently by agent `homelab-14`,
OpenAI GPT-6 Luna xhigh, on the immutable destination artifacts at the SHA
above. The repository's project sources are Apache-2.0-compatible; no external
paper text was imported. No human mathematical referee is claimed. No manifest,
claim lifecycle, priority, candidate status, or theorem state was changed.
