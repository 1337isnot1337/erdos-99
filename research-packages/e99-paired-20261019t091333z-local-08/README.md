# Destination exact-head audit: PR #948 rigid-cycle pinned stress

**Audit result:** the conditional rigid-cycle, isolate-capacity, and old-stress boundary claims pass at their stated scopes, with one formal wording correction: Lemma 3.1 must explicitly require every free component to be connected by positive-weight edges to a pin. The proof uses this grounding, and both applications in Theorems 4.1 and 5.1 establish it. The candidate remains unreviewed in the destination registry; this audit does not promote it.

**Audit date:** 2026-10-19.  
**Destination candidate commit:** 7d0a450fe66991036541023f95c44c064a04b6a8.  
**Candidate:** TARGET-C-PR948-RIGID-CYCLE-PINNED-STRESS.  
**Scope key:** 6fd935ac9c17cc38d5b5506a.  
**State / priority / catalogue:** 2026-10-15.publication.2 / public-frontier.3 / public-frontier.9.  
**Source provenance:** 1337isnot1337/e-99 PR #948, head b7376d13b81e542055c5c904bf81bdaf1beb7b9e, tree 4d2357368d1a2fa71b318741bf263e9aad342f8a.  
**Reviewed destination report SHA-256:** a3c36980e3710fc84b318a90a987aaf98940a6384a7e6681cfc60d3b6e4be783.  
**Destination verifier SHA-256:** c6e8793f9a06cd0d3c337c537ca04dc4d75173a92eb98c16329f2a374d212302.  
**Saved finite-control SHA-256:** 6d620fe5baa1a27fccdd34dffddb16cd33e984faeaa44d1cd58d18f5842b41cf.

**Audited destination report:** [target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md](../../docs/reports/target_c_rigid_cycle_pinned_stress_and_arc_stars_slot02_2026-10-10.md).

This is a destination-byte review. The registry still says unreviewed; the source lifecycle also says unreviewed. The open PR #116 is an audit of a different PR #948 face-obstruction candidate. Discussion #83 has no handoff for this rigid-cycle candidate, and the live open-PR search found no exact duplicate. No source-repository audit conclusion is used here.

## Exact question and hypotheses

Let P be the canonical triangle-free global minimizer chosen first with the fewest unit contacts and then with the fewest actual diameter pairs; D is its minimum diameter, and the proof's cited C-II normal form uses D >= 9. Contact-isolated labels remain in the full source. The audited candidate asks whether a positive contact equilibrium, pinned pointwise by a simple old unit-contact cycle carried by one Euclidean isometry, forces the old interior contact network to persist; and whether full-source exact-graph feasibility then preserves its core and isolate populations. A separate conclusion assumes the old contact weights split into separately balanced sign classes at every core vertex away from the old outer walk.

The full-source statements assume the same finite source labels, unit separation, diameter at most the minimum diameter D, the exact old contact graph, and pointwise equality of the boundary labels under one isometry. Pointwise pinning matters: congruence of the boundary point set after relabeling does not give the pinned energy comparison.

These statements affect only conditional C-II endpoint feasibility: whether a proposed fold can intrude into a rigid face, how many source isolates a face can contain, and whether checking all old outer-walk pairs certifies every core upper pair. They do not construct a globally feasible endpoint or close C-II or Level I.

## Pinned proof inputs

The exact report, its finite verifier and saved JSON are listed in SOURCES.json with destination hashes. The proof reconstruction also pins [C-I restoration, items 4 and 5](../../docs/targets/target-c/56-ci-restored-frontier.md), [local KKT equilibrium](../../docs/theory/01-local-structure.md), the [rigid-face isolate transport audit (227)](../../docs/audits/target_c_rigid_face_isolate_transport_independent_audit_2026-10-09.md), the [quarter-fold compatibility audit (83)](../../docs/audits/target_c_face_coupled_quarter_fold_independent_audit_2026-10-07.md), the [listed mixed-core rigidity dependency](../../docs/audits/target_c_finite_mixed_core_rigidity_independent_audit_2026-10-07.md), the [destination candidate registry](../../docs/targets/target-c/candidate-registry.json), and the [current Target C route](../../docs/targets/target-c/CURRENT.md). The two helper modules imported by the candidate verifier are also hash-pinned in SOURCES.json.

## Independent proof reconstruction

### Positive pinned-net identity

For a free set T, let d_i = r_i - q_i and d_w = 0 on pinned vertices. For every bar ij incident to T, equality of its lengths in q and r gives

0 = a_ij ( |r_i-r_j|^2 - |q_i-q_j|^2 )
  = a_ij ( 2(q_i-q_j)·(d_i-d_j) + |d_i-d_j|^2 ).

Summing each such edge once, the linear terms combine to twice the sum over i in T of d_i·sum_j a_ij(q_i-q_j), which vanishes by equilibrium. Therefore

sum_{ij incident to T} a_ij |d_i-d_j|^2 = 0.

Positive weights force d_i=d_j along every positive bar. If every connected free component reaches a zero-displacement pin, all its displacements vanish. No lower or upper feasibility, proximity, or planarity is needed for this identity.

There is a small formal omission in the generic wording of Lemma 3.1. A nonempty pin set W plus the statement that every outside neighbor lies in W does not, literally, force any free component to have an outside neighbor. For example, a single free vertex with no incident bar and an unrelated nonempty pin set satisfies those words but can move. The proof's final sentence recognizes the required condition: positive-weight bars must connect every free vertex to a pin. State that as an explicit hypothesis (or require a nonempty pin boundary for each free component). This is not a gap in the report's applications: each old or new interior contact component is separately shown to reach the cycle W.

### Old interior and full-source core persistence

For Theorem 4.1, noncrossing of unit edges makes W a separator of the old contact graph. Every contact component strictly inside W attaches to W; every such vertex is strictly inside the full-source convex hull and hence has no active diameter constraint. The old KKT equilibrium therefore reduces there to positive contact equilibrium. After applying the inverse boundary isometry, the old pinned identity fixes every old interior core vertex. This argument needs no endpoint separation or upper bounds.

For Theorem 5.1, Q is a same-cardinality unit-separated placement with diameter at most D and the exact old graph. Since D is the global minimum, diam(Q)=D. The unchanged graph is triangle-free and has the source's minimum contact count, so Q is itself a contact-minimal global minimizer. C-I restoration supplies a relative-interior stress with positive weight on every contact at Q; no secondary diameter-pair minimum at Q is needed. No positive support on every new actual-diameter pair is used. Each contact component newly inside W attaches to W and contains no Q-diameter endpoint because its labels lie strictly inside the Q hull. The positive contact weights are in equilibrium there. Compare Q(T) with the rigid image of P(T), fixing the cycle labels pointwise. The identity forces equality, so an old exterior core component cannot enter the new interior. Theorem 4.1 supplies the reverse inclusion and the coordinates of old interior core labels.

### Isolate population and capacity

Suppose the new interior has fewer contact isolates than the old interior, by delta >= 1. Replace the new interior isolates with rigid images of all old interior isolates. Distances involving an inserted isolate and the old interior core are unchanged and strictly greater than one; boundary distances are also strictly greater than one. Any remaining label lies across the unit cycle, and the unit-wall crossing bound makes these lower distances greater than sqrt(3). For upper bounds, each old interior isolate is in the convex hull of the wall. If x is a convex combination of wall vertices and y is any retained label, then the variance identity gives

|x-y|^2 = sum_i lambda_i |w_i-y|^2 - sum_i lambda_i |w_i-x|^2 < D^2.

The strict term is positive because x is strictly inside the cycle. Applying the same identity to both variables makes pairs of inserted isolates strictly shorter than D as well. Thus the enlarged configuration has n+delta labels, at most D diameter, and exactly the old contact count.

Delete one nonisolated core vertex, losing at least one contact, and delete delta-1 contact isolates. This returns to n unit-separated labels and leaves the count of contacts strictly below the canonical minimum. If the diameter is below D this contradicts global minimality; if it is D it contradicts contact minimality. Reversing P and Q gives the opposite isolate-count inequality using only contact minimality of Q. Hence the bounded-interior isolate counts are equal. This proves the stated capacity corollary: a lower-feasible intrusive core cannot admit a full-source packet of all old isolates with unit clearance and diameter at most D.

For Theorem 6.1, assume a convex old face F, an exact-graph lower-feasible core placement Q whose wall point set is isometric to W, and an intrusive component T placed inside the image of F. Let z be the old interior-isolate count, U = T minus the labels adjacent to W, and a = alpha(G[U]), the independence number. Let mu be the maximum size of a unit-separated packet in int R(F) whose points are strictly farther than one from Q(W) union Q(T). Choose an independent set S of size s = min(z,a), and a guarded packet of k = z-s sites if such a packet exists. Delete T and the z old interior isolates; insert the pulled-back Q(T), the packet, and the s old sites P(S).

The count is |T|+k+s = |T|+z. Since F is an actual face, old core labels in S and every other retained core label lie outside its interior. Internal and wall contact counts of T are preserved as geometric point sets; wall relabeling changes no count. The T union W point set is an isometric copy of its subconfiguration in Q, so it has no unit triangle. Every other pair crossing the wall is strictly longer than one by the crossing bound. S creates no contacts to W or to retained core labels, because S is independent, avoids N(W), and its old component has no other external contact; it also stays separated from inserted points across the wall. The packet is dilated slightly to open any internal unit pairs while retaining its strict guards. The result is triangle-free and has the old contact count.

Every inserted interior point is strictly inside the old diameter hull, so all its upper pairs with old retained positions are strictly below D. Other retained pairs remain at most D. Contract all current contact isolates a small amount toward the centroid, fixing the core; finite strict lower margins persist, and this opens every isolate-involving diameter equality. Each old component T contains a loaded label, since otherwise its positive old equilibrium and the maximum principle place it in conv(W)=F, where an old actual face has no core vertex. Thus the replacement removes at least one old actual diameter pair and creates none, contradicting the secondary diameter-pair minimum. Therefore z >= a+1, and the guarded packet capacity satisfies mu <= z-a-1. This theorem is a full-source competitor argument built from a lower-feasible core, not a claim that every core placement extends.

The stated coarse bound on a is also valid: a triangle-free unit-contact graph is planar and has maximum degree at most five, so |U| >= |T|-5|W|. Every induced subgraph of G[U] is triangle-free planar and has average degree below four (with the one- and two-vertex cases immediate), hence G[U] is 3-degenerate. Greedy coloring in reverse degeneracy order uses four colors, giving a >= ceil(|U|/4) >= ceil((|T|-5|W|)_+/4). This is a graph bound on actual old source labels, not an area estimate.

### Conditional old-stress boundary certificate

For the old positive contact weights a_ij and the old outer-walk vertex set O, assume at every i outside O that the positive-sign contacts separately balance:

sum_{j:s_ij=+1} a_ij(P_i-P_j) = 0.

Old equilibrium makes the negative-sign sum zero too. Under the integrated fold equation Q_j-Q_i = s_ij J(P_j-P_i), each such vertex is harmonic for the same positive contact weights. Every component of the contact core minus O meets O. The finite weighted maximum principle puts Q(V) inside conv(Q(O)); consequently diam(Q(V)) = diam(Q(O)). Checking every pair in O therefore certifies all core upper pairs, including previously inactive ones. An isolate y also passes its core upper pairs if |y-Q_o| <= D for every o in O; isolate-isolate pairs remain separate.

The proof is sound under this exact balance hypothesis. Uniform signs at an interior star are sufficient. A nonuniform four-star is covered only when its rays form two genuinely collinear opposite pairs, their signs agree pairwise, and old equilibrium makes each pair's weights equal. The two-hop compatibility rule supplies that sign equality. A nonrhombic four-star is not covered. The theorem supplies no sign assignment and no isolate placement. Its conclusion is only an upper bound at most D: an old inactive pair may become a new diameter pair, so the certificate alone does not preserve the secondary diameter-pair count needed for a C-II contradiction.

## Dependencies and scope limits

- C-I restoration gives C=C_* from contact minimality and H=H_* only from the secondary minimum. The full-source proof at Q uses contact minimality alone for positive contact weights.
- Local KKT equilibrium supplies zero contact force at vertices with no active diameter incidence.
- Audit 227 supplies the wall-crossing lower bound and strict convex-combination upper bound used in the isolate arguments.
- Audit 83 supplies the two-hop sign rule used only in the sufficient local implementation of the balance condition.
- The registry's C-MIXED-CORE-FINITE-RIGIDITY dependency is stronger than needed for these conditional statements: it requires exact lengths on all active contact and diameter edges of the core. It cannot derive a pointwise rigid W from contact-length preservation and upper bounds alone. Here pointwise rigidity is an explicit hypothesis.
- The registry's relation to the separate deep-face persistence candidate is a route relation; it is not used to infer an endpoint or a source-wide reserve.
- Sections 7 and 8 of the shared report concern additional arc-star and loaded-support claims outside this candidate row and were not audited under this assignment.

Finite verification cannot prove the equilibrium, global-minimality, separation, convexity or stress hypotheses for every canonical source. In particular, no universal source extraction, full-source feasible fold, independent-site reserve for every canonical source, or Level I result follows.

## Finite controls and falsification

The candidate verifier uses exact rational arithmetic for the oblique 16-label grid: 120 source-pair checks, 24 contacts, four interior equilibria, a grounded contact Laplacian with determinant 192, and a positive tested displacement energy 1770/847. It enumerates all degree-three and degree-four local sign patterns and checks the stated crossing/compatibility regression. Its leaf-intrusion regression lacks the positive equilibrium at the leaf and therefore does not contradict the pinned theorem.

The finite fixture supports the identity and local controls only. It does not encode contact minimality, full-source globality, arbitrary boundary cycles, the isolate-capacity argument, or the universal old-stress boundary theorem. The verifier imports the two helper modules pinned in SOURCES.json; those hashes are checked by this package.

The declared `verify.py` command replays the exact destination verifier and compares its stdout byte-for-byte with the saved JSON certificate. The separate package metadata check executes no commands. That replay checks the finite controls at the destination SHA; the analytic proofs above remain independent mathematical reasoning.

## Verification status

The metadata-only command `python scripts/research_package.py --package research-packages/e99-paired-20261019t091333z-local-08 --check-only` returned `metadata-valid`, with `full_verified=false`, `replay_authorized=false`, and `executed_commands=false`. The direct exact verifier wrapper then ran under the shared host compute lock and passed: its 2,828-byte stdout matched the saved certificate byte-for-byte (SHA-256 `6d620fe5baa1a27fccdd34dffddb16cd33e984faeaa44d1cd58d18f5842b41cf`), and the unattached-pin wording control passed. The metadata audit still reports conservative unresolved static Python import/capability closure in the wrapper and pinned helper scripts, so isolated package replay remains unauthorized; this does not change the direct local replay result.

## Next exact obligation

Construct a canonical source-derived nonconstant integrated fold that satisfies the pointwise rigid-face constraints, the old-stress balance where needed, every core lower bound, every actual and inactive core upper bound, and a simultaneous guarded placement for every contact isolate. Alternatively, prove a source-level full-source competitor without assuming this endpoint. The changed hypothesis is a source-realized sign field plus complete isolate restoration; the affected quantities are the diameter-pair count at D or the full-source diameter. A successful construction could enter the canonical C-II endpoint test; an obstruction would eliminate this fold route. Stop this audit here: the exact conditional candidate and its finite controls are reviewed, but no endpoint is constructed.

First step: write the complete lower and upper pair ledger for one proposed integrated sign field, including all inactive core pairs and every isolate. The blocker is that the current candidate supplies neither a source-derived sign field nor a simultaneous isolate placement.

## Provenance and attribution

This first-party audit is offered under Apache-2.0 and imports no external literature. The originating source candidate is PR #948, worker slot 02; this independent review is OpenAI Codex, GPT-6 Luna xhigh. The destination candidate lifecycle remains unreviewed pending a maintainer's disposition. Required repository-wide theorem-certificate replay is deferred to the merging agent.
