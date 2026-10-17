> Generated reading edition · [exact source](../../../docs/audits/target_c_exceptional_diameter_star_face_independent_audit_2026-10-08.md) · source SHA-256 `5c05ea10d81ded2d6efe9ff738f61b0da17459178c6c64a63c351339bf633f55`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6E12905439EB","canonical":true,"claim_ids":["C-DIAMETER-STAR-STRESS-CHAIN-CLASSIFICATION","C-NONSTAR-DIAMETER-CYCLE-STRESS-REGRESSION","C-STAR-EXCEPTIONAL-FACE-ONE-UNLOADED-TRANSVERSAL","C-TWO-EDGE-STAR-TRIANGLE-HYPOTHESIS-REGRESSION"],"claim_statuses":{"C-DIAMETER-STAR-STRESS-CHAIN-CLASSIFICATION":"canonical","C-NONSTAR-DIAMETER-CYCLE-STRESS-REGRESSION":"regression","C-STAR-EXCEPTIONAL-FACE-ONE-UNLOADED-TRANSVERSAL":"canonical","C-TWO-EDGE-STAR-TRIANGLE-HYPOTHESIS-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: exceptional diameter-star face

**Date:** 2026-10-08
**Audit base:** `origin/main=3c96c9e2eab86debc680f315d39df932928bc13c`, state `2026-10-08.audit.167`.
**Frozen source branch:** `research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f` (11 main-only / 24 branch-only at refresh).
**Candidate commit:** `099540dc282606f425fb98a8123d8308a5a81677`.
**Source report SHA-256:** `477c2244c29e8046ebaa059517327da4811e17c9b5cae5270c8b02f520dc59b6`.
**Exact checker SHA-256:** `dd8f1366fd02455feb5900bf5ff1663e955bfeb7208d50ceed178b25b906b14d`.
**Exact helper SHA-256s:** `179f20fb42827f6b3aa3b7afa5b982b16ff4da49abb77373edaf1a48bd514252` (`Q(sqrt(3))` geometry), `195f076d5580bbe082c732ab578f6e2a6d16eb624fb538d3980cb621dc5cecca` (exact rank/PSD arithmetic).

The report and checker match the frozen source snapshot. The discovery branch was not changed. The audited base is after Audit.171, so the empty-face consequence may use canonical `C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL`.

## Verdict

- **PASS — promote `C-DIAMETER-STAR-STRESS-CHAIN-CLASSIFICATION`.** For a finite triangle-free unit-separated planar source with `D>1`, any normalized nonnegative equilibrium stress whose positive diameter support is contained in one actual diameter star has exactly one positive diameter edge. Its positive contact support is the straight unit chain between the diameter endpoints; `D` is an integer and the contact coefficients equal `D` under `sum beta=1`.
- **PASS — promote `C-STAR-EXCEPTIONAL-FACE-ONE-UNLOADED-TRANSVERSAL`.** In a canonical C-II source, when `E_0=H[B\\W]` is empty or lies in one actual diameter star, the zero-beta exceptional face is empty or a singleton chain stress. A stress-killing deletion has size at most `s_Z+1`, with at most one unloaded-core label; it leaves a nonempty full source with a strict first motion.
- **REGRESSION VALID — promote `C-TWO-EDGE-STAR-TRIANGLE-HYPOTHESIS-REGRESSION` and `C-NONSTAR-DIAMETER-CYCLE-STRESS-REGRESSION`** at the exact finite scopes below. The first shows why triangle-freeness is needed; the second blocks widening “one star” to merely connected diameter support.
- These statements do not extract a star-shaped `E_0` from an arbitrary C-II source, restore deleted labels, or close C-II/Level I.

## 1. Exact audited statements and authority

For the finite statement, let `A` be any finite planar unit-separated set of actual diameter `D>1`, with no unit equilateral triangle. Let `C` be all actual unit-contact rows and `H` all actual diameter rows. A normalized equilibrium stress is nonnegative on these rows and satisfies `sum_H beta=1`. Its positive diameter support is `{h in H: beta_h>0}`.

If this support is contained in a star with hub `a`, it consists of exactly one edge `ab`. The positive contact support is the unique collinear chain `a=p_0,p_1,...,p_m=b`, with unit consecutive distances, `m=D` an integer, `alpha_(p_j p_(j+1))=m`, and `beta_ab=1`. Other source rows have stress coefficient zero. No global-minimality, PSD, or mixed-rigidity hypothesis is used.

For the canonical consequence, use the contact-minimal then diameter-pair-minimal triangle-free C-II source with `D>=9`, `C=C_*`, `H=H_*`; let `V` be the nonisolated positive-contact core, `B` the full actual diameter-endpoint set, `I=V\\B`, and `P` the normalized stress polytope with affine dimension `s_Z`. All contact-isolated source labels remain in the full configuration. Given any nonempty supplied `W subset B`, put `E_0=H[B\\W]` and let `P_0` be the face with zero beta mass incident to `W`.

When `E_0` is empty or contained in one actual diameter star, either `P_0` is empty or it is the single chain stress above. There are `U subset W`, `Y subset I` with `R=U union Y`, `|R|<=s_Z+1`, and `|Y|<=1`, killing every normalized retained-source stress. The retained source is nonempty and has a straight first motion that opens every retained actual contact and shortens every retained actual old-`D` pair. This is reduced-cardinality descent only.

Canonical inputs checked at `.167` are `C-EXTREME-TRANSFER` (stress-polytope dimension), `C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL` (empty-face deletion, including nonemptiness), and `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE`. The global Level I quantifier remains unchanged: no finite nonglobal fixture is a minimizer result.

## 2. Independent reconstruction of the stress geometry

Write `B_s` for the endpoints of the positive beta rows and `C_s` for the positive contact rows of one stress. A positive diameter endpoint has a strict supporting functional: for a diameter partner `b'` and any source point `q!=b`,

`(b-b') dot (q-b) <= -|q-b|^2/2 < 0`.

All positive diameter reactions at `b` therefore have the same strict sign under this functional. Equilibrium forces positive contact support at `b`. A positive-contact component with no positive diameter endpoint is impossible by pairing its equilibrium with positions: the contact coefficients are nonnegative, each contact has squared length one, and the resulting sum can vanish only if every coefficient vanishes. At vertices without positive diameter reaction, equilibrium makes the position a positive weighted average of its positive-contact neighbors. Applying the finite maximum principle to each contact component gives

`V(C_s) subset conv(B_s)`.

Now suppose the positive beta support is a star centered at `a`, with leaves `b_i=a+D u_i`. Since the full source diameter is `D`, every two leaf directions have chord at most one on the unit circle: their smaller angular separation is at most `pi/3`. The extreme leaf directions consequently span an arc of width at most `pi/3`; the two extreme segments from `a` are exposed sides of `conv(B_s)`.

At either extreme leaf, the only positive diameter reaction lies along that side. Every positive contact neighbor lies in `conv(B_s)` on one closed side of the same line. Taking the normal component of equilibrium forces every such neighbor onto the line. At an internal point of the resulting boundary segment there is no positive diameter reaction, so contact equilibrium requires a unit neighbor in both line directions. Finiteness and unit separation force the chain to continue in unit steps until it reaches `a`. Thus each extreme arm contains its first unit point `a+u_-` or `a+u_+`.

If there were two positive diameter edges, those first unit points would be at distance `2 sin(theta/2)<=1`. Strict inequality violates unit separation; equality makes a unit equilateral triangle with `a`. Both are excluded. Hence a star stress has only one positive diameter edge.

With only `ab` in positive diameter support, `B_s={a,b}` and the contact support is trapped in the segment `[a,b]`. The same one-dimensional equilibrium argument gives the unique unit chain. Its length is the integer `m=D`; equilibrium at an endpoint gives contact multiplier `m` when `beta_ab=1`. The support rows are the `m` chain contacts plus the endpoint diameter row, a rigidity circuit of rank `m`; no finite flex or globality follows from this stress classification.

## 3. Exceptional-face deletion

Every stress in `P_0` has positive beta support in `E_0`. If `E_0` is empty or lies in one star, the preceding theorem shows `P_0` is empty or is one chain-stress vertex. In the empty case, `C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL` gives `U subset W`, `|U|<=s_Z+1`, and no unloaded exceptions, with the retained-source nonemptiness already proved there.

In the singleton case choose an internal chain vertex `r`. It is a positive-contact core vertex but not a diameter endpoint, so `r in I`. Its incident contact mass `g_r=sum_(c incident r) alpha_c` is positive on the chain stress (`g_r=2D`). The zero face `F_r=P intersect {g_r=0}` is therefore proper and disjoint from `P_0`. If `F_r` is empty, deletion of `r` alone kills every normalized stress. Otherwise `dim_aff(F_r)<=s_Z-1`; finite Helly on `F_r`, applied to the nonnegative zero-beta faces for `b in W`, selects `U subset W` with `|U|<=s_Z` and `F_r intersect intersection_(b in U){f_b=0}=empty`. Thus `R=U union {r}` kills every stress and `|R|<=s_Z+1`, `|R\\W|=1`.

A retained-source stress would extend by zero to the forbidden face intersection. At deleted loaded endpoints, zero beta reaction forces zero contact reaction by the strict supporting functional. `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE` then gives the full retained-source strict first motion. In the singleton case the chain endpoints are outside `W` because their edge lies in `E_0`; they remain retained, so the reduced source is nonempty. All contact isolates remain in the global configuration and retain their inactive pair margins.

This is a one-exception improvement only under the actual star hypothesis. It does not classify general forests, cycles, multiple stars, or arbitrary exceptional-edge sets.

## 4. Exact regressions at the hypothesis boundary

The frozen checker uses exact `Q(sqrt(3))` coordinates and `Fraction` coefficients.

- **Triangle-free hypothesis.** Its two-arm source has two length-10 rays at angle `pi/3`, 21 points, actual diameter `10`, and a unit equilateral triangle at the hub. A normalized nonnegative stress has positive beta `1/2` on the two hub-to-tip diameter edges, so its positive diameter support is a two-edge star. Complete census, equilibrium, PSD/rank checks pass. A same-cardinality square grid has diameter squared `32<100`. This is a finite nonglobal regression to dropping triangle-freeness.
- **Star-support hypothesis.** For arm lengths `6,8,10`, three unit chains at mutual angle `2pi/3` give triangle-free sources with `19,25,31` points and actual diameter squared `108,192,300`. The actual positive diameter support is the 3-cycle among the outer tips, with beta `1/3` on each edge and contact weights equal to the arm length. Exact complete censuses and equilibrium/stress checks pass. The mixed rigidity ranks are respectively `20,26,32`, below `2n-3`; same-cardinality square-grid competitors have diameter squared `25,32,50`. These examples refute only a universal extension from star supports to arbitrary connected supports; they do not satisfy canonical mixed rigidity or global optimality.

These regressions are deliberately scoped to those failed generalizations. Neither is a counterexample to a canonical C-II theorem.

## 5. Verifier boundary and frontier effect

Reran `research/verify_target_c_exceptional_star_face_2026_10_08.py` from the frozen source snapshot. It checks the three straight-chain fixtures (`D=10,11,12`), the two-arm triangle fixture, the three-arm cycle fixtures (`L=6,8,10`), complete actual pair/contact/diameter/triangle censuses, exact equilibrium, contact/mixed ranks, rational PSD ranks, explicit smaller square-grid competitors, and 64 abstract simplex/cube-simplex face-count cases. The abstract polytopes are not planar source models. The checker does not prove the universal stress geometry, canonical face theorem, grid extraction, source optimality, or cardinality restoration; those are analytic or remain open.

The canonical consequence improves the finite deletion budget from at most `b_0` unloaded exceptions to one when `E_0` lies in one diameter star. It does not show that `E_0` has that structure for a canonical source. No W extraction, refill, same-cardinality competitor, C-II closure, or Level I conclusion follows.

## 6. Local validation

- The frozen exact checker passed; it verifies finite fixtures and abstract face counts only.
- `python3 tools/build_artifact_index.py --write --write-headers`, `python3 tools/generate_theorem_state_views.py --write`, `python3 tools/check_theorem_state.py`, and `python3 tools/check_active_route_summaries.py` passed.
- All 22 theorem-state, PR-checker, and active-route tooling tests passed.
- The complete registered theorem-certificate suite passed: 90 unique certificates.
- Touched authority-document local links and `git diff --check` passed.
- The PR-base transaction check is run after the promotion commit is created.
