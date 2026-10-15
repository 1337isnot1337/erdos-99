<!-- theorem-state: {"artifact_id":"ART-15A7FF07B8CB","canonical":false,"claim_ids":["C-CAPPED-WALL-ACTUAL-DIAMETER-ESCAPE-REGRESSION"],"claim_statuses":{"C-CAPPED-WALL-ACTUAL-DIAMETER-ESCAPE-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Target C capped-wall actual-diameter escape: independent audit

Date: 2026-10-07. Audit base: `origin/main` at `5cfc5b346365454f029320e495a492488ca5f513`, state `2026-10-07.audit.95`. Target C has C-I closed and C-II open. The audited source is the immutable Worker1 snapshot `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`.

## Verdict

**PASS — promote the exact conditional full-packet escape theorem and its finite nonglobal examples as regression `C-CAPPED-WALL-ACTUAL-DIAMETER-ESCAPE-REGRESSION`.** The claim is about the entire capped grid packet under an explicit source-contact hypothesis. It does not extend the motion through arbitrary retained outside points, extract such a packet from a canonical source, or establish any global-minimizer or Level I conclusion. The C-II endpoint is unchanged.

The frozen source report is `docs/reports/target_c_capped_wall_actual_diameter_escape_2026-10-06.md`, Git blob `e019013be36f59e21c46fb8edb28ae11825854b0`, SHA-256 `a5697b751c55865bd29f583df12d21d3488cb0c6392280c1bdd728dc1fbb1d61`. Its self-contained verifier is Git blob `38dad7459ea5439b1e0e649d2a38a1ec7537ab05`, SHA-256 `ee5498832d78693ded2a96e636e2a38c8ef680b98b84f9e13eea0c75a5a7cffa`. The report and verifier blobs are identical at the overnight Worker1 tip `9204dc1469359e5b22a8bfe9429dfb391dec4b4d`.

## Exact audited statement

Let `M>=24`; let `u,v` be unit vectors whose smaller angle `phi` satisfies `49/100 < cos(phi) < 1/2`; and include every grid point `p_ij=i u+j v`, for `0<=i,j<=M`. Choose finitely many distinct boundary grid edges with integer index `8<=k<=M-9`, and attach one outward regular unit pentagon to each chosen edge. For an oriented base edge `a b`, write `w=b-a`, let `n` be its outward unit normal, set `c72=(sqrt(5)-1)/4`, `c36=(sqrt(5)+1)/4`, `s72=sqrt(10+2sqrt(5))/4`, and `s36=sqrt(10-2sqrt(5))/4`; the cap's five vertices in cyclic order are

`a`, `b`, `c=b+c72 w+s72 n`, `d=a+(1/2)w+(s72+s36)n`, and `e=a-c72 w+s72 n`.

Optionally add four outward leaves at `c+s72 w+c72 n`, `d+n`, `e-s72 w+c72 n`, and `d+(15/17)w+(8/17)n`. Assume the entire source consists of exactly these distinct points, is unit-separated, and has exactly the stated contacts: grid-neighbor edges, cap 5-cycles, and the four listed leaf edges per cap when leaves are included.

Under those hypotheses:

1. The unique actual diameter pair is `p_00,p_MM`, with squared distance `2(1+cos(phi))M^2`.
2. For every sufficiently small positive `epsilon`, rotating `u` clockwise by `epsilon`, holding `v` fixed, and carrying each cap/leaf with its base preserves every actual unit contact, keeps every other pair strictly above one, and makes every source pair strictly shorter than the old diameter. The packet therefore has a same-cardinality feasible strict-diameter competitor and is not globally diameter-minimizing.
3. The actual contact graph is triangle-free. The packet has no normalized nonnegative KKT stress on its actual active rows: its only active diameter row has squared derivative `-2M^2 sin(phi)<0` along this contact-preserving motion.

The exact-contact hypothesis is part of the theorem. It is verified by exhaustive interval checks only for the two concrete packets below; the theorem does not assert that the cap configuration has this contact set for every `M`, cap selection, or leaf choice.

## Independent reconstruction

### Actual diameter

The cap and leaf offsets from their base midpoints have Euclidean norm below three, and their outward normal coordinate has the sign of the corresponding side. Since `sin(phi)>sqrt(3)/2`, both coefficients of any such offset in the oblique unit basis `u,v` have absolute value below `3/sin(phi)<2sqrt(3)<7/2`. The cap index range places each base midpoint coordinate in `[8.5,M-8.5]`. Thus the whole source lies in the five closed coefficient boxes

`G=[0,M]x[0,M]`, `B=[5,M-5]x[-7/2,0]`, `T=[5,M-5]x[M,M+7/2]`, `L=[-7/2,0]x[5,M-5]`, and `R=[M,M+7/2]x[5,M-5]`.

For coefficient difference `(a,b)`, squared distance is `a^2+b^2+2c ab`, where `c=cos(phi)`. This is a convex quadratic on each product of boxes, so its maximum occurs at a pair of box vertices. For each of the 190 unordered pairs of the 20 listed box vertices, subtract `2(1+c)M^2` and substitute `M=24+z`. The result is `A(c)z^2+B(c)z+C(c)` with `A,B,C` affine in `c`. Exact endpoint arithmetic at `c=49/100` and `c=1/2` gives `A<=0`, `B<=0`, `C<0`, except for the single opposite grid-corner pair, where all three coefficients are zero. Affinity gives the same inequalities throughout the closed cosine interval; since `z>=0`, all non-corner box pairs are strictly shorter. Strict convexity within `G` then gives the unique actual diameter pair stated above.

### Feasible motion and strict upper bound

Rotating `u` clockwise while fixing `v` increases the angle from `u` to `v`. Each grid edge remains a unit vector. A cap built from its base direction `w` and outward unit normal `n` has successive edge vectors

`w`, `c72 w+s72 n`, `-c36 w+s36 n`, `-c36 w-s36 n`, `c72 w-s72 n`,

where `c72=(sqrt(5)-1)/4`, `c36=(sqrt(5)+1)/4`, and `c72^2+s72^2=c36^2+s36^2=1`. These identities make all five cap edges exactly unit. Each optional leaf offset is one of `(s72,c72)`, `(0,1)`, `(-s72,c72)`, or `(15/17,8/17)` in the orthonormal `(w,n)` frame, so all listed leaf contacts are also exactly preserved. Caps based on `u` rotate with `u`; caps based on `v` translate with their grid base. Thus the entire listed contact set stays at unit length.

For a sufficiently small positive angle, `cos(phi+epsilon)` remains in `(49/100,1/2)` and is strictly less than `cos(phi)`. The same five-box certificate applies to the moved packet, giving its actual squared diameter as `2(1+cos(phi+epsilon))M^2`, strictly below the old value. Every initially noncontact pair was strictly longer than one; finiteness and continuity therefore preserve all lower constraints for sufficiently small `epsilon`. No uniform positive motion size is claimed. Since the whole moved source is below the old diameter and every pair stays at least one, this is a direct same-cardinality competitor, independent of spare-site, energy, or pinned-wall arguments.

The unique active diameter has squared derivative `-2M^2 sin(phi)`, while every active contact derivative is zero. Pairing any normalized nonnegative KKT stationarity relation with this velocity would give a strictly negative value for a quantity that stationarity requires to be zero. Hence no such stress exists for the actual active rows.

### Exact finite source checks

The frozen verifier uses outward rational intervals at scale `10^24`. Its interval operations are exact integer floor/ceiling operations; square roots are enclosed using integer square roots. Contact equalities follow from the exact vector identities above, while every noncontact lower bound and every upper bound is checked over all pairs.

| Source | Points | Caps | Listed contacts | Pair checks, old and target |
| --- | ---: | ---: | ---: | ---: |
| `M=24`, ordinary caps | 649 | 8 | 1,232 | 210,276 |
| `M=32`, caps with outward leaves | 1,145 | 8 | 2,176 | 654,940 |

The checker confirms the listed graph is triangle-free; every unlisted source and target pair has a certified squared-distance lower bound above one; the unique source diameter is the opposite grid-corner pair; and every target pair lies below a conservative lower bound on the old squared diameter by more than `1/10,000,000`. The box certificate reports all 380 exact endpoint-coefficient checks. Reproduction command:

`python3 research/verify_target_c_capped_wall_actual_diameter_escape_2026_10_06.py`

The captured deterministic JSON is `research/target_c_capped_wall_actual_diameter_escape_certificate_2026_10_07.json`, SHA-256 `63646030a29923f2f1c45751dbc5860868e2fafd650873fa8a89de883b853137`.

## Hostile scope checks

- The bound is on the actual entire-packet diameter, not on a selected or pinned wall. The unique loaded pair is explicitly identified.
- Every source pair is included in the finite checks, including all grid, cap, and leaf cross-pairs. In the general implication, exact contact completeness plus finiteness is what permits a source-dependent small motion.
- The source itself need not be globally optimal; indeed the conclusion proves it is not. No globally optimal or canonical source is inferred.
- No arbitrary exterior source point is carried by the motion. A capped patch inside a larger source may have additional lower contacts or upper diameter constraints, and this theorem does not move through them.
- The `cos(phi)=1/2` endpoint is used only for the closed box upper certificate. The source theorem has the strict upper inequality; at the endpoint the unlisted grid diagonals become unit contacts.
- Audit.93 already shows that large stopped-train bulk and pentagon frustration alone do not force fixed-wall refill surplus when boundary pins are not actual loads. Audit.94 gives a distinct paired exterior-cap regression. This result adds an entire-packet strict-diameter escape with an actual unique diameter pair; it does not duplicate either scope.

## Canonical disposition

Promote one regression ID, `C-CAPPED-WALL-ACTUAL-DIAMETER-ESCAPE-REGRESSION`, with this exact conditional source class and the two verified finite realizations. Do not promote the source report's prospective embedding discussion as an arbitrary-source theorem. Do not claim a uniformly feasible amplitude, source extraction, a canonical C-II exclusion, or Level I progress.

The exact remaining C-II obligations are unchanged: a source-realized face-coupled finite move satisfying every full-source lower and actual-diameter upper constraint, or an independently quantified source-specific physical obstruction payment; the separate macroscopic-container branch still needs capacity or a strict competitor. C-I remains closed, C-II and Level I remain open.
