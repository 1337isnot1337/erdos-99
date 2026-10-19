# Destination audit: PR #948 large-array boundary attachment

**Verdict: PASS at the exact conditional scope below.** This audit finds the analytic proof sound under its stated hypotheses and reproduces its finite controls. The destination candidate remains `unreviewed` in the registry; this record does not promote a theorem or alter Target C state.

**Reviewer:** OpenAI Codex, GPT-6 Luna xhigh, assigned independent reviewer. **Source author:** Worker 02 (the report and verifier identify the originating work). **Review date:** 2026-10-19. This is an agent review, not external human peer review.

## Exact review target and provenance

- Candidate: `TARGET-C-PR948-LARGE-ARRAY-BOUNDARY-ATTACHMENT`.
- Destination main / reviewed report commit: `7d0a450fe66991036541023f95c44c064a04b6a8` (tree `db766e0e25b562054df26aeec7e627d5a579dd6d`); `origin/main` matched this SHA at review time.
- Source: `1337isnot1337/e-99` PR #948, head `b7376d13b81e542055c5c904bf81bdaf1beb7b9e`, tree `4d2357368d1a2fa71b318741bf263e9aad342f8a`, source main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`, merge base `d999528cfaafd811a4a19bcfacd00f217c2fc375`. The source PR remains open. This audit is of the destination bytes, not a second historical source audit.
- State / priority / catalogue: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.
- Destination report SHA-256: `f2225a9ceebddb2b3318ed948bb94d247f2a61c9e73db80d7ce3567093e037c6` (source report SHA-256: `c091322e150383de1954b60453061df751821dc3962e6e80e9cf311f949e8e75`).
- Destination verifier SHA-256: `3cd1d82fd3d693166b89bd2d3ef08e522d3face7aaa9704ffc297cd5756421a9`.
- Saved finite certificate SHA-256: `40cbdce45f7c718d6623c97fd31643b52850d2d550d080441dd2cb393596e49d`.

The candidate record and artifact-index row at the destination are still `unreviewed`, `canonical: false`, and claim-free. The assigned task card's `existing_checks` is empty. Live overlap found PR #116, which audits a different PR #948 quarter-fold-face candidate; its scope does not include this attachment theorem. Discussion #83 has no matching handoff. No exact destination audit was found.

## Candidate lemma, hypotheses, quantity, and stop rule

For each fixed `delta>0`, there exist `epsilon_delta>0` and finite `D_delta` such that any source `P` with `D=diam(P)>=D_delta`, where `P` is a contact-minimal, triangle-free global unit-separated minimum-diameter source, satisfies `r >= epsilon_delta D` whenever it contains an **actual** complete bent unit-rhombic array `p_ij=z+x_i+y_j` with distinct source labels, every consecutive row/column edge a unit contact, every cell a strict rhombic contact face, and both cell counts `a,c >= delta D`. Here `r` counts distinct noncorner array-boundary vertices with an actual unit contact to a source label outside the array. The theorem does not require diameter-pair minimality; the report's whole-core corollary does.

The downstream quantity is this actual boundary-vertex count `r` (and hence at least `r/5` distinct outside labels, using the triangle-free unit-neighbor degree bound). It can exclude the route where the entire nonisolated core is a macroscopic complete bent array. It does not provide array extraction from an arbitrary core or a full-source endpoint.

Falsification target: find a gap in (i) the local opposite-star loading implication, (ii) the `r=o(D)` to dense regular-mesh limit, (iii) strict transverse monotonicity or the fixed-circle lens conclusion, or (iv) the common-corner tangent contradiction; replay the exact finite verifier and check its saved output. Stop at the conditional theorem if these steps hold. Do not infer the extraction premise or search for a C-II endpoint from the supplied-array result.

## Independent proof reconstruction

1. **Direction windows and internal contacts.** All row directions lie in an interval of width `< pi/3`; all column directions lie in a second interval with pairwise cross angles in `(pi/3,2pi/3)` and total interval width `< pi/3`. Projection on a family interval's bisector makes any `m`-edge chord longer than `(sqrt(3)/2)m`. For mixed-index differences, the cross-angle bound gives `|U +/- V|^2 > (|U|^2+|V|^2)/2`; if both increments are one, strict rhombic diagonal bounds instead give length `>1`. Thus the only internal unit contacts are designated grid edges. A regular noncorner boundary vertex therefore has exactly its three grid-contact rays.
2. **Opposite-star loading.** At opposite noncorner vertices `(i,0)` and `(i,c)`, the three-ray star gaps include `pi-tau` and `pi+tau`, where `tau=alpha_i-alpha_(i-1)`; the other gaps are strict cell angles below `pi`. For nonzero `tau`, exactly one star fails positive spanning and local contact-minimality forces that vertex to be a diameter endpoint, while the other star positively spans and cannot be a diameter endpoint because diameter endpoints are extreme. If `tau=0`, both are forced diameter endpoints but each is the midpoint of its two horizontal neighbors, contradicting extremality. The row case is symmetric. At most `r` index pairs per orientation are irregular because each irregular pair contains an externally attached boundary vertex.
3. **Compactness.** If no positive uniform `epsilon_delta` and onset exist, take a sequence with `D_n -> infinity`, `a_n,c_n >= delta D_n`, and `r_n/D_n -> 0`. Normalize by the full-source circumcenter and `D_n`. Since family chords exceed `(sqrt(3)/2)` times their edge counts and every source pair is at distance at most `D_n`, both `a_n/D_n,c_n/D_n < 2/sqrt(3)`. The piecewise-linear row and column paths are uniformly Lipschitz. Their rectangular interpolation is a convex combination of four actual array labels, so lies in the full-source circumdisk; it adds no source point. Arzela-Ascoli gives limiting paths `X,Y`, corner `z`, endpoints `A,B`, and closed direction windows. Both `A,B` are nonzero from the lower aspect bound.
4. **Strict transverse motion.** For every pair of path parameters `s<t`, expand the determinant of the positive partial row sum with the full column sum over unit cells. Each cell determinant exceeds `sqrt(3)/2`, giving `det(X(t)-X(s),B) >= (sqrt(3)/2) delta^2(t-s)>0`; the column identity is analogous. This survives the limit and excludes constant or stalled paths.
5. **Boundary points lie on two lens circles.** A good opposite-star index has exactly one diameter endpoint. The full-source circumradius estimate puts every such endpoint at radius `D_n/2 + O(sqrt(D_n))` from the full-source circumcenter. Since at most `r_n` indices are bad and `(r_n+2)/a_n,(r_n+2)/c_n -> 0`, good indices form vanishing-gap meshes. Uniform Lipschitz continuity and the disk upper bound extend the radial equality to every limiting parameter, including corners: for each `s`, `max(|z+X(s)|,|z+X(s)+B|)=1/2`, and likewise for `Y,A`.
6. **No lens-circle switching.** With `b=(0,h)`, a point in the intersection of the two radius-`R` disks satisfies `x^2+(y+h/2)^2+h^2/4+h|y+h/2| <= R^2`; equality at the common circle boundary forces `y=-h/2` and `x=+/-sqrt(R^2-h^2/4)`. These are the extreme `x` projections of the lens. The determinant monotonicity is strict monotonicity in `x`; neither intersection can occur at an interior path parameter, so continuity prevents switching which circle is active. `b=0` is ruled out by the nonzero endpoint; `|b|>=2R` is incompatible with a nonconstant strictly monotone path. Apply the lemma to both paths, reversing orientation for the second.
7. **Common-corner contradiction.** The fixed active circles intersect at the actual limiting corner `z+epsilon_x A+epsilon_y B`, on the same radius-`1/2` circle. Nonconstant circle paths have endpoint chord directions tending to their tangent: `2p dot h + |h|^2=0`, and the family direction cone of width at most `pi/3<pi` selects one of the two opposite tangent rays. The two limiting tangent lines at the common point coincide, so their oriented rays are parallel or antiparallel. The closed cross-angle interval `[pi/3,2pi/3]` excludes both. This contradiction rules out every sequence with `r_n/D_n -> 0`; the standard diagonal choice of thresholds therefore gives existential uniform `epsilon_delta,D_delta` for each fixed `delta`.
8. **Whole-core corollary.** If the array is the whole nonisolated core, it has `r=0`. When `a>=2`, a regular opposite pair provides an actual diameter endpoint with an array partner under the canonical diameter-pair-minimal normalization. The diameter upper constraint makes the endpoint a strict support point; adjacent row edges put its normal perpendicular to a direction in the row cone. All column directions then have one strict normal projection sign, forcing the diameter pair to join opposite rows. Writing its displacement as `Dn=r+B`, with `r` a row chord, gives `D <= sin(Delta_u)(D+|B|)+|B|`, hence `D < (7+4sqrt(3))c <14c`. The column-symmetric bound is `D<14a`. The one-cell cases are separately bounded by `D<=14`, and for `D>=15` both dimensions exceed `D/14`. The attachment theorem with `delta=1/14` contradicts `r=0`. Contact-isolated source labels remain in the full circumdisk/diameter constraints; none is deleted or counted as an insertion site.

## Dependency and lifecycle audit

- `C-FS-GEOM` is canonical for every noncollinear global source and gives the full-source circumradius bound used in the compactness step. A complete strict array is already noncollinear. The estimate is full-source, so isolates remain constrained.
- Local structure Lemma 5.1 and Theorem 6.1 in `docs/theory/01-local-structure.md` supply endpoint extremality and the contact-minimality-to-positive-spanning implication; triangle-free geometry bounds contact degree by five.
- `C-ZRF` is canonical on the nonisolated core of the contact-minimal then diameter-pair-minimal source and supports the whole-core corollary's claim that active diameter endpoints lie in that core. Its core-only stress/rigidity scope is not extended to isolates.
- The candidate registry also lists `C-RHOMBUS-POP`, which is canonical and preserves all source labels. Its face-area/population inequality is not invoked by the report's analytic argument; this dependency is overinclusive rather than load-bearing here.
- The destination report SHA differs from its frozen source SHA. This audit checks the destination report bytes as requested and does not recompute a source/destination full-text diff. The registry records the migration as provenance/redaction/link adaptation; the destination bytes contain the complete argument checked here.

## Adversarial checks and exact finite controls

I checked the proof's boundary cases as well as its generic geometry: strict array angles imply only the designated internal unit contacts; `tau=0` is explicitly impossible for a regular pair; bad-pair count charges distinct boundary vertices; corners need not be regular because the limiting equality follows by continuity from dense interior meshes; limiting cell angles may reach exactly `60` or `120` degrees without allowing parallel or antiparallel tangents; and no array-to-source extraction or endpoint move is asserted. The aspect-ratio coefficient is exact:

`(1 - sqrt(3)/2)(7 + 4 sqrt(3)) = 1 + sqrt(3)/2`, with `7+4sqrt(3)<14`.

The original verifier checks exact rational/algebraic ingredients: 174 lens-point identities, 420 oriented circle-chord identities and 21 tangent identities, 625 regular-star cases (500 nonzero-turn and 125 zero-turn), 81 bent-array fixtures with all 2,916 label-pair lower bounds and 486 determinant checks, and the exact aspect coefficient. It does not model global optimality, the full-source circumradius theorem, compactness, numerical constants, array extraction, a finite endpoint, or Level I.

Reproduction (Python 3.14.8):

```sh
python research-packages/e99-paired-20261019t091333z-local-09/verify.py
```

The package verifier reruns the pinned destination script and compares its stdout SHA-256 to the saved certificate SHA-256. This direct replay passed. The package metadata check returned `metadata-valid`, but its conservative static closure scan retained unresolved wrapper subprocess/file-read and imported verifier/helper surfaces; no isolated package replay was run. Exact command and input pins are in `VERIFY.json` and `SOURCES.json`.

## Exposure, predecessor comparison, and limits

Before reconstructing the destination proof I saw a prior memory summary naming PR #948's boundary-attachment route, its high-level conclusion, and the missing complete-array extraction bridge; the initial broad offline overlap output also showed adjacent Target C audits. I then derived the full argument from the exact destination report and checked the listed dependencies and finite verifier. This review is not blind to that high-level prior summary. No exact destination audit was present in the candidate registry or task-card coverage, and the live PR #116 audit is for a distinct quarter-fold-face candidate.

The proved scope is the conditional supplied-array theorem and its whole-core corollary. It does not imply that an arbitrary canonical survivor contains such an actual complete array; a virtual completion, partial grid, or independently supplied chart is insufficient. It does not create a full-source feasible finite endpoint or prove C-II or Level I. A, B, and C-II remain open; C-I remains closed.

## Open next question

- **Question:** Can every sufficiently large canonical C-II survivor be shown either to contain an actual complete bent array with `a,c >= delta D` and `r < epsilon_delta D`, or to admit a different source-level endpoint in the complementary regime?
- **Downstream use / exact quantity:** This decides whether the proved attachment lower bound `r >= epsilon_delta D` excludes the whole-core complete-array branch; it controls actual externally attached boundary vertices, not virtual sites or isolates.
- **Changed hypothesis:** Replace the report's supplied complete array by an array extracted from the actual canonical source, while retaining all source labels and complete unit-rhombic faces.
- **Outcomes:** An extraction with sublinear `r` contradicts the candidate theorem and excludes that branch; failure to extract redirects work to a finite full-source endpoint or to the complementary regime with explicit boundary contacts.
- **First action:** Starting from a canonical survivor's actual contact complex, prove a uniform complete-array extraction with both dimensions proportional to `D` and a source-level bound on distinct external boundary attachments.
- **Blocker:** No current proof derives that actual complete array and boundary count from an arbitrary survivor.

This audit is offered under Apache-2.0-compatible terms, retains Worker 02's attribution, and makes no claim of theorem promotion or human peer review.
