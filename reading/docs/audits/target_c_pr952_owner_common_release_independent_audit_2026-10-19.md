> Generated reading edition · [exact source](../../../docs/audits/target_c_pr952_owner_common_release_independent_audit_2026-10-19.md) · source SHA-256 `6289ec80954c7832d22a0ec7746b41632aa255938ee3f6f654cb7158dbca5423`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BD5F4180D5EE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit: PR #952 owner common-release implication

Date: 2026-10-19. **Verdict: PASS within the exact supplied-family hypotheses
below.** This is a conditional finite-source audit, not a theorem-state
promotion. Target C-II and Level I remain open.

## Exact object and lifecycle

I audited the destination-main bytes at `7d0a450fe66991036541023f95c44c064a04b6a8`
(tree `db766e0e25b562054df26aeec7e627d5a579dd6d`), with theorem state
`2026-10-15.publication.2`, priority `public-frontier.3`, and catalogue
`public-frontier.9`. The exact candidate is
`TARGET-C-PR952-OWNER-COMMON-RELEASE-IMPLICATION` in
[`candidate-registry.json`](../../../docs/targets/target-c/candidate-registry.json), where
it remains `unreviewed` and has no source claim IDs.

The reviewed destination report is
[`target_c_outer_owner_amplification_and_common_release_2026-10-10.md`](../reports/target_c_outer_owner_amplification_and_common_release_2026-10-10.md),
SHA-256 `8c7fd0295ab13dbb533d2ed00d426070e9a70fa4cc2bd7659936ec430613540d`,
Git blob `1a3881b621b45d79ab86e0a1ca0143a0860e2310`. The exact verifier is
[`verify_target_c_source_realized_owner_sink_2026_10_10.py`](../../../research/verify_target_c_source_realized_owner_sink_2026_10_10.py),
SHA-256 `df2cd04d208b0370cb85b3c15a2cef308b11be2a942058c724473456ad85da25`,
Git blob `21de0d3ed504468f923620744d7391d0b74e50cb`. The two scoped saved
outputs are `target_c_owner_amplitude_release_2026_10_10.jsonl` (SHA-256
`af7b444cecfeb35a8f1229286b9ba43e3604a3bd13cf7fcaf4afc77699268c52`) and
`target_c_common_release_implication_2026_10_10.jsonl` (SHA-256
`1627c1eda0c61088187b04d6cae71a012993428b36162b19cfb3fa83e2446b66`). All
four hashes match the pinned destination main bytes.

The destination provenance record identifies source PR #952 at source main
`42f0296d1aca068c809f74cee5dcdb4ebdb27c73` and records head
`3536c0b6f6c2a929d9c96fffbdcfc480735fea3` with tree
`a6503b1817dbd885f9378ca42677d811fe363c84`. The recorded head is 39 hex
characters; a live read of source PR #952 at the final refresh gives the full
head `3536c0b6f6c2a929d9c96fffbdcfc480735fea3b`, with the same tree. The live
PR remains open and has zero GitHub review records. This is a pre-existing
source-pointer discrepancy; I audited the destination report hash above, not
the source report's distinct SHA-256
`9d3bc1c881aa3cb05148b6c8b2054db36fa8e93f00c8a0acf0069c358c06ba19`
(source blob `0f3a2127aeffe3cfaf56a1193d96a0afc198ad31`). The registry records
an operational hosted-CI redaction as the destination/source report difference.
Destination PR #25 reconciled the import and artifact metadata, but did not
audit the proof. The final private overlap refresh at 2026-10-19 09:56 UTC
covered 70 open PRs, 97 closed PRs, 0 open issues, and all 8 Discussions with
comments/replies. Its Discussion #83 handoffs are unrelated to this candidate.
Open destination PR [#153](https://github.com/1337isnot1337/erdos-99/pull/153)
audits sibling candidate `TARGET-C-PR952-UNEQUAL-HEIGHT-ISOLATE-TRANSPORT`,
and [#157](https://github.com/1337isnot1337/erdos-99/pull/157) audits sibling
candidate `TARGET-C-PR952-INCLUSIVE-FLOOR-LOCKED-RELEASE`. Their exact reports
and questions differ from this owner-common-release candidate. The exact-scope
overlap search found no completed destination audit. This is the missing
destination review, not a repeat of the source-side maintenance review.

## Statement checked

For its canonical application, let `A` be the contact-minimal, then
actual-diameter-pair-minimal triangle-free global source with `D>=9`, connected
positive-contact core `V`, and full actual diameter graph `H`. Retain all
source labels, including contact isolates. Write
`d_H=|V(H)|-|E(H)|`. Supply pairwise disjoint,
nonempty proper core owners `G_i` and an unowned core label. Owner `i` has
nonzero displacement `d_i=delta_i v_i`, with unit `v_i` in an oriented angular
interval of width `w<pi/2`. The exact source hypotheses in report Section 2
include: old contacts are preserved for every binary selection of these
owners; each proposed singleton is weakly upper-safe on every old actual
diameter pair; the source owners come from the stated subfamily-stable stopped
O–O system; bounded-face isolates receive its compatible rigid assignment;
other isolates follow the fixed long-pair anchor map or stay fixed; and the
fixed exceptional inactive-upper set `E` has `|E|<=d_H`. Put
`L=sqrt(D^2-1)`, `gamma=D-L`, and
`s=diam{0,d_1,...,d_r}`.

The audit checks four conditional claims:

1. **AB:** for `M>1`, `Ms<min(gamma,sqrt(2)-1)` and
   `theta_M=w/2+asin(Ms/(2D))<pi/2`, deleting at most
   `2d_H+4 floor(F_D(theta_M))` owners gives an upper-safe full-source
   amplitude box, where
   `F_D(theta)=1+(D sin(theta)+2 L_D)/cos(theta)` and `L_D=7D^(2/3)`.
   Contacts remain lower-safe when each amplitude is `0` or at least `1`.
2. **CT:** if
   `delta_max+4 sin(w/4)<rho<min(gamma,sqrt(2)-1)` and
   `theta_b=w/2+asin(rho/(2D))<pi/2`, the report's bounded deletion gives
   upper-safe common translations and opens every selected owner-to-fixed
   contact. The exact lower tests then have only directed implications and
   forced-zero unaries, with no pairwise incompatibility clause.
3. **UCC:** for any supplied common `b` that opens every owner-to-fixed old
   contact, compiling *all* local lower and upper states of *all* source pairs
   gives that implication/unary system. The maximal assignment sets to zero
   exactly the owners that can reach a unary. It is nonzero iff a sink strongly
   connected component has no unary blocker. A nonzero model gives a
   same-cardinality triangle-free endpoint with fewer old contacts and
   diameter at most `D`.
4. **IM:** under the stated positive contact stress, nonnegative actual-
   diameter stress, exact owner cut and singleton upper-safety hypotheses,
   the report's stress-imbalance estimate bounds a positive-stress actual
   loaded-port projection and the number of owners with imbalance at least a
   prescribed threshold.

The canonical quantity affected is the fixed-`D` contact count for UCC, and
the actual loaded-port normal projection for IM. No extraction of these owners
from every canonical minimizer is part of these claims.

## Independent proof reconstruction

### Full-source upper safety and contact opening

For an actual diameter pair with endpoints in distinct owners `i,j`, write
`g_i,g_j` for the squared-length changes when only one owner moves by `M d_i`
or `M d_j`. After deleting every owner with a growing singleton witness,
`g_i,g_j<=0`; the simultaneous squared change is

```math
g_i+g_j-2M^2 d_i\cdot d_j<0,
```

because the direction interval is acute. Pairs inside one owner are unchanged,
and pairs with only one moving endpoint are the tested singleton states.
Consequently every vertex of the `{0,M}^r` amplitude cube passes every actual
diameter upper test. For a fixed source pair its squared distance is convex in
the amplitudes, so every point of the cube is bounded by its corner values.

All endpoint displacements lie in the convex hull of `{0,M d_i}`. Its diameter
is at most `M s`. The fixed dispatch makes protected long inactive pairs have
equal endpoint displacements, `E` endpoints are fixed, and every other
inactive pair begins at length at most `L`; its new length is at most
`L+Ms<D`. This proves the full-source upper ledger, including isolate pairs.
For an old cut contact of owner `i`, exact preservation at amplitude one gives
`r dot d_i=-delta_i^2/2` when `r` is the moving point minus the fixed point,
and hence

```math
|r+x_i d_i|^2=1+x_i(x_i-1)\delta_i^2.
```

Thus the stated `0`-or-`[1,M]` amplitudes do not shorten old contacts. If some
`x_i>1`, connectedness of `V`, properness, and the no-cross-owner-contact fact
give a cut contact that opens. This is contact loss only when every old
noncontact remains strictly above one. Amplitudes in `(0,1)` instead shorten
their cut contacts, so the convex upper-safe box is not a lower-feasible path
from zero to `M`. The AB hypotheses do not guarantee a lower-feasible amplitude
vector.

The owner deletion count follows from the finite full-source midpoint bound:
for each selected actual-diameter normal `n` in a window of half-width `theta`,
`p=m+(D/2)n` with `|m-o|<=L_D`. Its tangent-coordinate span is at most
`D sin(theta)+2L_D`. In convex boundary order consecutive selected support
points have forward tangent projection at least `cos(theta)` times their
chord, hence at least `cos(theta)` by unit separation. Thus a window contains
at most `F_D(theta)` loaded endpoints, uniformly over the partner choices.
Each chosen diameter normal really is a strict supporting normal at its
endpoint: for partner `p'`, endpoint `p`, and any other source point `x`,
the diameter bound gives
`n dot (x-p)<=-|x-p|^2/(2D)<0`, where `n=(p-p')/D`. This justifies placing
the selected endpoints in convex-boundary order.
The two opposite windows contain at most `2 floor(F_D(theta))` endpoints.
The witness-edge subgraph of `H` has at most as many edges as incident
vertices by `C-WOODALL`; each edge charges at most two owner labels. This gives
the `4 floor(F_D(theta))` term. At most `2d_H` additional owners fix the
endpoints or isolate anchors of `E`.

For AB, an unsafe amplified singleton has `r dot v_i` between
`-M delta_i/2` and `-delta_i/2` when `r` is moving-point minus fixed-point.
Since `|r|=D` and `delta_i<=s`, its projective direction is within
`asin(Ms/(2D))` of `Jv_i`, hence within `theta_M` of `Jv`. The endpoints
incident with all such witness pairs can be assigned witness partners; the
partner-uniform count controls them in the two opposite windows. Each edge
charges at most two owner sets, so the number of deleted owners is at most
twice the number of witness endpoints, giving the stated factor `4`.

For CT, a selected contact has `r dot v_i=-delta_i/2`. With
`|v-v_i|<=2 sin(w/4)`, translation by `b=rho v` changes its squared length by
at least
`rho(rho-delta_i-4 sin(w/4))>0`. A singleton upper witness for `b` has
`r dot v>-rho/2`, while the original owner direction has
`r dot v_i<=-delta_i/2<0`. If `r dot v<=0`, its projection magnitude is less
than `rho/2`, so it lies within `asin(rho/(2D))` of a perpendicular. If
`r dot v>0`, the sign change from `r dot v_i<0` to `r dot v>0` occurs within
the `w/2` direction interval. In both cases its projective direction lies in
one of the two `theta_b` windows. The same partner-uniform window and
`C-WOODALL` count proves the CT deletion bound. The cloud `{0,b}` has diameter
`rho`; the fixed dispatch
and `rho<gamma` protect inactive pairs. If a diameter pair crossed two
surviving distinct owners, the two weakly safe singleton squared changes would
sum to `2 rho^2>0`, impossible. Thus all actual upper pairs are safe.

### Exact implication system and canonical contradiction

For a noncontact between different moving owners, state `00` and `11` have the
old squared distance `1+c`, with `c>0`; this remains true for an actual or
inactive upper pair because both endpoints move together in state `11`. With
common translation `b`, singleton lower slacks are

```math
c+2r\cdot b+\rho^2,\qquad c-2r\cdot b+\rho^2.
```

For lower-only CT tests their sum is `2c+2rho^2>0`, so at most one can be
nonpositive. In UCC, an upper failure can occur in either singleton state;
each failed `10` state contributes `i -> j`, each failed `01` state contributes
`j -> i`, and both failures correctly give both implications. A pair against a
fixed label contributes a forced-zero unary if its selected state fails a
lower or upper test. Pairs within one owner and pairs of two fixed labels are unchanged. This exhausts all
full-source pairs; it does not infer inactive-upper safety from a weighted
average.

Let `Z` be the vertices that can reach a unary. Every feasible selected set is
implication-closed, so it cannot meet `Z`. Conversely `V_imp minus Z` has no
unary and is implication-closed: an edge from outside `Z` into `Z` would give
the source vertex a path to a unary. Therefore this complement is the unique
maximal feasible model. A nonempty complement contains a sink SCC with no
unary; conversely such a sink supplies a nonzero model. Because at least one
core label is fixed and `V` is connected, a nonzero model cuts a contact to
the fixed core. All old noncontacts are strict by the compiled constraints,
all old contacts are unchanged or opened, and all labels remain. The result is
triangle-free, has fewer contacts, and has diameter at most `D`. Globality
rules out strict sub-`D`; at `D`, canonical contact-minimality rules it out.
Thus `Z` must contain every owner in a canonical source. This contradiction
uses all old lower and actual/inactive upper pairs.

### Stress-imbalance estimate

For an owner cut with contact stress masses `A_i^+,A_i^-`, exact contact
preservation gives the two crossing contact directions
`-delta_i v_i/2 +- sqrt(1-delta_i^2/4) J v_i`. If
`sigma_i=|A_i^+-A_i^-|/(A_i^++A_i^-)`, the norm of their weighted sum is
`A_i c_i`, where

```math
c_i=\sqrt{\delta_i^2/4+(1-\delta_i^2/4)\sigma_i^2}.
```

Summing the KKT equilibrium over the owner cancels internal rows and equates
this resultant to the positive-weight sum of crossing actual-diameter vectors.
If `B_i` is their total diameter weight, triangle inequality gives
`A_i c_i<=D B_i`. Its projection opposite `v_i` is exactly
`A_i delta_i/2>0`, which also forces `B_i>0`. The beta-weighted mean of
`-n dot v_i` is
`A_i delta_i/(2D B_i)<=delta_i/(2c_i)`. At least one positive-beta port is
no larger than this mean. Singleton upper safety makes every such projection
strictly positive. For `sigma_i>=sigma_0`, `delta_i<=s<2` gives

```math
-n_i\cdot v_i\le {s\over2\sigma_0\sqrt{1-s^2/4}}=z_0.
```

The chosen endpoints are distinct across disjoint owners and their normals
fall in the two opposite windows of half-width
`w/2+asin(z_0)`. The same full-source window count gives
`2 floor(F_D(theta_0))`. The acute-window and `z_0<1` hypotheses are necessary
for this counting step; the argument makes no statement about owners that do
not have a positive-stress cut or independently upper-safe singleton.

For the stronger relative-imbalance form, define
`R_i=sigma_i sqrt(1-delta_i^2/4)/delta_i`. The IM.2 estimate is exactly
`-n_i dot v_i<=1/sqrt(1+4R_i^2)`. Thus `R_i>=T` puts the normal within
`atan(1/(2T))` of one of the perpendicular directions and gives
```math
\#\{i:R_i\ge T\}\le
2\left\lfloor F_D\bigl(w/2+\arctan(1/(2T))\bigr)\right\rfloor.
```
At `w=0`, substitution yields the stated
`2+D/T+4L_D sqrt(1+1/(4T^2))` upper bound. For `w=O(1/D)` and fixed
`T>=1`, this is `D/T+O(D^(2/3))`. These tail bounds retain the same
singleton-upper-safe and positive-stress owner hypotheses.

Also, when `s<gamma<=1/D`, `w=O(D^(-1/3))`, and
`sigma_0=D^(-2/3)`, one has `z_0=O(D^(-1/3))` and
`theta_0=O(D^(-1/3))`; since `L_D=7D^(2/3)`, the IM.3 count is
`O(D^(2/3))`. This is only an upper bound on the supplied highly imbalanced
owners; it does not imply that any linearly large owner family exists.

## Canonical dependency scope

The report's exact finite window count uses the canonical full-source midpoint
claim `C-FS-DIAMETER-MIDPOINT-D2-3` (`D>=7`), not merely the weak-limit
atomlessness statement `C-CII-ACTUAL-DIAMETER-NORMAL-ATOMLESS`. The bound
`|m-o|<=7D^(2/3)` is uniform over all source labels, so the `F_D` derivation
applies to this `D>=9` C-II source and arbitrary partner choices. `C-WOODALL`
supplies the actual-diameter subgraph inequality needed in the witness count.
The fixed `E` and isolate-anchor ledger uses
`C-LONG-PAIR-ISOLATE-DISPATCH` only as a structural partition: for AB's
different owner amplitudes, the report separately assumes protected long-pair
endpoints receive equal displacements and explicitly does not substitute the
single-vector dispatch theorem as an amplitude-box theorem.

The lower-face localization uses canonical `C-NEAR-UNIT-CONFLICT-GEOMETRY`
and `C-OO-LOWER-BLOCKER-LOCALIZATION` under the report's stopped O–O cut,
small-cloud, and bounded-face isolate-transport hypotheses. For CT.1 the cloud
is below both `gamma` and `sqrt(2)-1`; its angular width is correspondingly
small. The exact UCC pair compiler itself is stronger and does not need a
face-localization result: all source pairs are entered directly. Canonical
`C-DISJOINT-SWAP-2SAT` is a comparison, not a shortcut for UCC, since UCC
allows contacts to open and includes actual/inactive upper clauses.

For IM I use the report's positive contact-stress and owner-cut assumptions,
with nonnegative active-diameter stress from the canonical relative-interior
KKT setup; the current `C-MIXED-CORE-ONE-ROW-REDUNDANCY` entry supplies
nonzero weights on its active contact and diameter rows. `C-ZRF` is core-only:
isolates are not stress variables, and this audit does not extend its rigidity
statement to them. The registry also lists
`C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN`; that claim is core-only and is not
needed for UCC's contact-loss implication or IM's force balance.

## Finite controls and adversarial checks

I inspected the exact verifier's source construction and all-pair loops. It
uses rational/algebraic coordinates, 120-bit rational square-root enclosures,
and checks every unordered source pair in each declared state. Under the host
compute lock I ran, on CPython 3.14.6:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python3 research/verify_target_c_source_realized_owner_sink_2026_10_10.py --heights 30 31 100 --symbolic-limit --amplitude-repair --common-implication-system
```

Exit status was 0. The nine-state all-pair counts were 52,974 (`H=30`, 109
labels), 53,955 (`H=31`, 110 labels), and 143,379 (`H=100`, 179 labels),
total 250,308. Each height had two old actual-diameter pairs; every other pair
was checked below `D`, and lower states were checked exactly. The three
fixtures are connected, triangle-free and explicitly marked nonglobal with no
positive-KKT claim. They have no contact-isolated labels, so the finite runs do
not exercise the isolate-anchor map or exceptional set `E`; those remain
conditional parts of the analytic full-source ledger. The common endpoint
removed 24 contacts, kept every old noncontact strictly above one, and
strictly lowered the exact rational diameter squared. Its full-source
implication witnesses are `A => B` and
`B => A`, with no unary blocker and maximal model `(1,1)`. The amplitude
repair removed 12 contacts. These are regression fixtures, not canonical
sources.

The symbolic-limit replay found 5,751 strictly separated noncontacts and 11
critical `t=0` pairs among 5,762 noncontacts. Every amplitude-repair and
common-release critical slack has positive leading coefficient; this matches
the report's sufficiently-large-height argument. It does not itself prove
uniform family extraction from canonical minimizers. The proof's remaining
height-uniform estimates separate the fixed low cluster from the vertical
chain: the former is bounded in `[-6,6] x [0,23]` and its internal squared
diameter is at most `673`; cross-distance to later chain sites is maximized at
the top site, while bottom moving labels give the stated AR/CR diameter. Thus
the strict leading slacks give a sufficiently-large-height lower-feasible
range, and the report separately proves the upper maximum. The three finite
heights alone do not establish that onset.

I separately reconstructed the exact square control for the necessity of
singleton upper-safety in IM. With
`eps=200/10001`, `eta=9999/10001`, `u=(eps,eta)`, and left-column displacement
`d=2 eps u`, exact SymPy rational arithmetic gives all four old contacts
squared length `1` and the two old diameter squared changes
`-7999200/100020001` and `+7999200/100020001`. The contact stress
`Omega=(1,-1,1,-1)(1,-1,1,-1)^T/2` has rank one, contact coefficients
`alpha=1/2`, diameter magnitudes `beta=1/2`, and annihilates the two coordinate
rows and constants. Thus the owner is contact-preserving and has
imbalance `sigma=1`, but is not singleton-upper-safe. It lies outside IM's
hypotheses and demonstrates why the upper-safety sign is needed.

The square is indeed the finite four-point optimum: for a convex quadrilateral,
one interior angle is at least `pi/2` and its two incident unit-separated
sides force the opposite diagonal to have squared length at least `2`. If one
point lies strictly inside the triangle of the other three, two of its three
rays make angle at least `2pi/3`, forcing an outer distance at least
`sqrt(3)`. If it lies on a triangle edge, the two collinear subsegments each
have length at least one, so that edge has length at least `2`. A collinear
four-point source has diameter at least `3`. This verifies the control's small
global premise, while its `D=sqrt(2)` remains outside the candidate's `D>=9`
counting scope.

The square control was run with this exact arithmetic check:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python3 - <<'PY'
import sympy as s
R = s.Rational
eps, eta = R(200, 10001), R(9999, 10001)
u = s.Matrix([eps, eta])
d = 2 * eps * u
assert eps**2 + eta**2 == 1 and d.dot(d) == (2 * eps)**2
pts = [s.Matrix(p) for p in [(0,0),(1,0),(1,1),(0,1)]]
owner = {0, 3}
new = [p + d if i in owner else p for i, p in enumerate(pts)]
contacts = [(0,1),(1,2),(2,3),(0,3)]
assert [(new[i]-new[j]).dot(new[i]-new[j]) for i,j in contacts] == [1]*4
changes = [s.simplify((new[i]-new[j]).dot(new[i]-new[j])-2)
           for i,j in [(0,2),(1,3)]]
assert changes == [-R(7999200,100020001), R(7999200,100020001)]
k = s.Matrix([1,-1,1,-1])
X = s.Matrix([[p[0] for p in pts], [p[1] for p in pts]])
Omega = k*k.T/2
assert k.T*s.ones(4,1) == s.zeros(1,1) and k.T*X.T == s.zeros(1,2)
assert Omega.rank() == 1
assert all(Omega[i,j] == -R(1,2) for i,j in [(0,1),(1,2),(2,3),(3,0)])
assert all(Omega[i,j] == R(1,2) for i,j in [(0,2),(1,3)])
PY
```

## Adversarial limitations and notation repair

The algebra and exact pair ledgers support AB's upper box, CT/UCC's implication
closure, and IM under the hypotheses stated above. Two report phrases reverse
the vector arrow relative to their equations: the AB witness inequalities and
the IM.1 contact vectors require
`r = owner/moving point - fixed/complement point`. The report text calls these
vectors “from the moving endpoint to the fixed endpoint” and “from `G_i` to
its complement.” Reversing those arrows restores the displayed signs; the AB
deletion count is projective and uses both opposite windows, so its count is
unchanged. This is a notation correction, not a missing geometric hypothesis.

The AB contact-loss argument applies when a lower-feasible amplitude has some
`x_i>1`. Its all-binary case `x_i in {0,1}` has no contact loss; the report
explicitly relies there on a separate unreviewed weighted-gain candidate
`SG`. I do not use the canonical core-only contact-isometry gain claim to
certify a full-source endpoint with isolates, and do not audit or endorse SG
here. UCC's contact-loss theorem does not need that extension.

The verifier does not test AB, CT or IM as universal analytic statements; its
fixtures are exact finite nonglobal examples. No unbounded canonical O–O
family satisfying CT.1, no unary-free sink SCC in an actual canonical source,
and no same-cardinality canonical endpoint is extracted. The precise next
lemma remains the report's Section 9 source-extraction-plus-unary-avoidance
statement for every sufficiently large canonical C-II source, with all
isolates and all lower/upper pair constraints retained.

No theorem-state, candidate lifecycle, route, priority, or certificate
registration was changed. The candidate remains unreviewed on destination
main; this report records an independent conditional audit only.

## Attribution and AI role

The candidate source and finite fixtures are attributed to Slot 01 and source
PR #952 as recorded in the destination candidate registry. This audit and its
exact square calculation were produced by an independent OpenAI Codex GPT-6
Luna xhigh reviewer session, separate from the source author. No external text,
paper, or PDF is reproduced. This report is an Apache-2.0-compatible original
audit contribution.
