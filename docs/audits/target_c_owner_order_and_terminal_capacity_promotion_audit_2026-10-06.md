<!-- theorem-state: {"artifact_id":"ART-26B9B9E13513","canonical":true,"claim_ids":["C-ABSTRACT-OWNER-HORN-PACKET","C-ACUTE-BINARY-OO-LAMINARITY","C-BINARY-LOADED-WITNESS-POCKET-BUDGET","C-CROSSING-MULTISHEAR-INDEPENDENT-OWNER-REGRESSION","C-ONE-VERTEX-CONVEX-WALL-SHIELD","C-OO-TERMINAL-OWNER-CAPACITY","C-OO-TERMINAL-TRAIN-POPULATION","C-OWNER-REGION-TREE-RECURRENCE","C-TWO-WALL-DELETION-EXTERIOR-SHIELD-REGRESSION"],"claim_statuses":{"C-ABSTRACT-OWNER-HORN-PACKET":"regression","C-ACUTE-BINARY-OO-LAMINARITY":"canonical","C-BINARY-LOADED-WITNESS-POCKET-BUDGET":"canonical","C-CROSSING-MULTISHEAR-INDEPENDENT-OWNER-REGRESSION":"regression","C-ONE-VERTEX-CONVEX-WALL-SHIELD":"canonical","C-OO-TERMINAL-OWNER-CAPACITY":"canonical","C-OO-TERMINAL-TRAIN-POPULATION":"canonical","C-OWNER-REGION-TREE-RECURRENCE":"canonical","C-TWO-WALL-DELETION-EXTERIOR-SHIELD-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent promotion audit — Target C owner order, terminal capacity, and wall shield

**Date:** 2026-10-06  
**Audit base:** 583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1  
**Starting state:** 2026-10-05.audit.62  
**Audited source snapshot:** research/sol/target-c-owner-order-closure-20261006 at 51853ce9752c065663fd407289c6d46adc767f69  
**Verdict:** PASS for the exact claims below; the terminal span bound has a universal nonexplicit constant, with a sequence-dependent onset threshold.  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

The live research branch advanced during this audit: first to 1b09620bfb5788e1d8732076f6f7538dec137e89, then to ece938d9. The intervening commits add the capped-wall report/verifier, edit the common-angle train report, and add a separate odd-shell barrier-payment report/verifier plus run notes. A path comparison confirms that none modifies the four source reports or four verifiers audited here. This audit uses only the recorded immutable snapshot above.

## 1. Starting canonical endpoint

Audit.62 leaves the full-core finite-motion obstruction at outer-face owner/implication structure, cyclic loaded near-unit clauses, explicit unary rhombus blockers, and at most d_H inactive upper exceptions. The separate macroscopic inactive-container branch is open. The relevant canonical inputs are C-LINEAR-NONMATCH, C-LOADED-NEAR-UNIT-ADJACENCY, C-NEAR-UNIT-CONFLICT-GEOMETRY, C-FULLCORE-HULL-DEPLETION-FLOOR, C-GOOD-HULL-SINGLETON-CHARGE, C-FS-GEOM, C-TERMINAL-PHYSICAL-FRUSTRATION, C-CONTACT-FACE-REGULARITY, C-EMBEDDED-WALL-REFILL, and C-SHORT-WALL-ZERO-CAPACITY.

The audit separates finite combinatorial supply from source realization and from the full-source finite-motion endpoint. None of the new results establishes C-II closure.

## 2. Owner terminal-capacity theorem

Let B_bad be the exact bad outer-terminal-occurrence bank in the canonical loaded-hull decomposition. Audit.52/55 establish B_bad = x_B + m_B, with terminal occurrences counted with multiplicity. In the Section 61 train system, every complete train has two terminal occurrences; at most two trains have two good force-hull ends, and any two such good trains cross.

For any selected family of O--O trains, every train other than a two-good-ended train consumes a distinct occurrence of B_bad: choose one of its bad ends. This is injective because terminal occurrences partition across complete trains. Therefore:

    T_OO ≤ x_B + m_B + 2.

In a projective direction interval of width strictly less than pi/3, two selected trains cannot cross: canonical Section 61 requires projective separation greater than pi/3 for a crossing. Thus at most one selected train has two good ends, giving:

    T_OO ≤ x_B + m_B + 1.

This is a supply bound only. It does not extract a beneficial motion or imply that a useful pinned assignment exists.

### Region-tree recurrence

For T_OO pairwise disjoint proper crosscuts of an occurrence disk, the complementary-region dual is a tree with T_OO + 1 regions. Label each region by its translation, choose one reference region labelled zero, and let c_i count connected components of regions carrying nonzero owner label i. With K_own distinct nonzero owner labels and

    rho_own = sum_i(c_i - 1),

the K_own + rho_own = sum_i c_i components occupy distinct non-reference regions. Hence:

    K_own + rho_own ≤ T_OO.

Combining with the narrow-window train bound gives:

    K_own + rho_own ≤ x_B + m_B + 1.

For a nonempty owner population, K_own ≥ 1, so rho_own ≤ x_B + m_B. Repeated labels and branching are allowed; no owner-connectivity premise is used. The separate proposed overlap allocation involving loaded-run counts and unary rhombus roots is **not** promoted here: its mapping from each loaded-run boundary occurrence to a distinct owner-assigned train bank was not independently established.

The exact tree script checked 14,182 finite tree/label/bank cases through six edges. The proof is the region count above; finite enumeration is a regression check, not its infinite proof.

## 3. Acute independent binary owners are laminar

Assume the precise finite model of C-OO-LOWER-BLOCKER-LOCALIZATION: selected global stopped O--O cuts form proper crosscuts of the connected positive-contact core; every old contact remains a unit contact under every independent binary owner selection; each nonzero owner translation has norm below one; distinct nonzero translations are mutually acute; selected cut increments are nonzero; and each crossing of train centerlines occurs in a strict unit rhombus.

Canonical C-NEAR-UNIT-CONFLICT-GEOMETRY classifies the only possible ownership patterns on a strict rhombus under those hypotheses: all four vertices fixed, all four in one owner, or one adjacent pair in one owner with the other two fixed. The first two patterns activate no crossing train. In the last pattern only the two opposite moving/fixed contacts change; those contacts lie on the same one of the two crossing trains. Therefore two crossing trains cannot both be active. The selected trains are pairwise noncrossing and their occurrence-disk dual is a tree, without a narrow direction-window assumption. Since any two good-ended trains cross, at most one is fully good, so the terminal bound T_OO ≤ x_B + m_B + 1 holds in this binary scope.

This theorem concerns independent binary owner variables. It does not identify general crossing multishear train variables with independent owners.

### Exact crossing-scope regression

The rational strict rhombus in the source verifier has vertices 0, u = (1,0), w = (5/13,12/13), and u+w. The two noncontact diagonals have squared lengths 16/13 and 36/13. With the stated exact rational rotation, all four independent train-bit states preserve the four unit sides and keep both diagonals above one; both trains are active in state 11. But treating the three nonzero region translations Δu, Δw, and Δu+Δw as independent owners leaves the old contact from u to u+w with squared-length excess:

    -47928/13000013 < 0

in the singleton-owner state selecting only u. The verifier checks every pair in all train and owner states exactly. This is a finite scope regression, not a canonical source or a global-minimizer counterexample.

## 4. Loaded binary witnesses spend a long outer pocket

Consider the narrow-window binary owner model above. Let ab be a loaded-loaded lower witness with 1 < |ab| ≤ 13/12. By canonical C-LOADED-NEAR-UNIT-ADJACENCY, ab is a side of the actual loaded hull. Charge each distinct physical witness to its unique outer interval between consecutive loaded endpoints.

If that interval has length two, its actual boundary path is a-z-b with |az| = |zb| = 1. The chord length is greater than one: equality would give a forbidden unit equilateral triangle. Since |ab| ≤ 13/12 < sqrt(2), the angle between the two unit contact rays is theta = 2 arcsin(|ab|/2), which lies in (pi/3, pi/2).

If a,b have distinct nonzero owners, z cannot have either owner because an old contact would join distinct acute moving owners. It cannot have a third moving owner for the same reason, so z is fixed. Both contacts would then be selected train cuts whose projective directions differ by theta > pi/3, impossible in one direction window of width < pi/3. Thus a binary loaded witness cannot be charged to a two-edge interval.

Writing each nonunit loaded-hull interval length as ell_i ≥ 2, the exact identities are:

    x_B = sum_i(ell_i - 1)
    m_B = number of nonunit intervals
    u_B = x_B - m_B = sum_i(ell_i - 2).

Every surviving binary witness uses a distinct interval with ell_i ≥ 3, which contributes at least one to u_B. Therefore:

    N_BB_binary ≤ u_B.

This counts distinct physical witnesses, not logical clauses duplicated from one side. It does not exclude unary loaded-pair clauses, arbitrary-angle witnesses, or crossing multishears. It rules out the first four-train abstract packet's u_B = 0 data in this source-level narrow-window scope; the strengthened four-train packet at u_B = 3 remains only an abstract model with no source realization.

## 5. Terminal O--O train population and ledger

Let a canonical full-core Type-II sequence satisfy

    q/D → pi,    u_B = o(D),

and retain every contact isolate. Let N_OO count all complete stopped trains with both terminal occurrences on the old outer contact face, including singleton bridges. Then:

    N_OO = o(D).

Here is the independent reconstruction. For an outer interval of length ell ≥ 3, ell ≤ 3(ell - 2), so the total terminal-occurrence mass on long intervals is at most 3u_B = o(D). At most 3u_B/2 O--O trains have neither a good unit-hull terminal nor a two-edge-pocket terminal, since each such train uses two distinct long-interval occurrences.

For a two-edge pocket with loaded chord length c in (1,2], its terminal unit side u and outward unit normal n to the chord satisfy |det(u,n)| = c/2 ≥ 1/2. The same lower bound holds for a good unit-hull terminal. Suppose, contrary to the needed geometric consequence, that along a subsequence a train with one of these anchored ends has terminal midpoint displacement o(D). Since midpoint steps have length one and project strictly in one cone, the whole train lies within o(D) of its anchored terminal. The other terminal is then o(D)-close. Every loaded-hull interval outside the o(D) long-pocket budget has length one or two; even a terminal in a long interval is within o(D) of its loaded endpoint. Thus the two ends lie on a shrinking arc of the near-disk force hull. The corresponding side of the proper crosscut has loaded vertices in a single o(D)-diameter cap, so no actual diameter pair is internal to that positive-contact shore.

If the shore has no loaded core vertex, summing its positive contact equilibrium gives a nonzero coherent train force with no diameter reaction, impossible. Otherwise sum the actual KKT equations over the core vertices in this shore. Internal terms cancel. Every crossing contact contributes a positive multiple of the same oriented train vector u. Every actual diameter reaction at a shore vertex has direction

    r_h = 2(b - o) + O(D^(3/4)),

where o is the common circumcenter, b is the local loaded endpoint, and the error is uniform by canonical C-FS-GEOM. Near-disk convergence makes all such r_h/D converge to one radial direction. Since the terminal contact satisfies |det(u,n)| ≥ 1/2, the positive diameter reactions lie in a strict cone separated from the contact line and cannot balance the nonzero contact resultant. This contradiction also rules out an anchored singleton bridge.

The shore contradiction rules out an admissible sequence on which an anchored train has o(D) span. Every remaining anchored non-singleton train therefore contains at least epsilon D strict rhombi for a universal nonexplicit epsilon, with an onset threshold that may depend on the sequence. Each rhombus is incident with at most two complete trains. Canonical C-TERMINAL-PHYSICAL-FRUSTRATION gives R_O = o(D^2) rhombi incident with all outer-ended trains. Hence:

    N_OO ≤ 3u_B/2 + 2R_O/(epsilon D) = o(D).

The no-submacroscopic-span contradiction also yields a universal nonexplicit epsilon across all sequences in (2). If no such epsilon existed, for each k one could choose a canonical sequence with infinitely late anchored spans at most 2D/k, then select a sufficiently late term with q/D within 1/k of pi and u_B/D below 1/k. These diagonal choices would form a sequence satisfying (2) with anchored span o(D), contradicting the shore argument. The onset threshold may depend on the sequence, and no numerical epsilon or effective D_0 is supplied.

For the exact face ledger, write K_top = d_H + s_Z, X = Q - f, and let S_BB be singleton trains with two bounded physical-face ends. Outer terminal occurrences give N_OB = b - 2N_OO, and the canonical train count is T = q - K_top + 2f. Thus:

    N_BB = T - N_OO - N_OB = 2f - x_B - K_top + N_OO.

After deleting outer-ended trains, every remaining rhombus crosses two BB trains. The simple triangle-free train-crossing graph and Mantel therefore give:

    N_BB - S_BB ≥ 2 sqrt(R_4 - R_O).

Use f = q - x_B - 2K_top - X, R_4/D^2 → pi/(2sqrt(3)), q/D → pi, and N_OO = o(D). The exact inequality yields:

    3x_B + 5K_top + 2X + S_BB ≤ [2(pi - s) + o(1)]D
    s = sqrt(pi/(2sqrt(3))).

This excludes only terminal bank combinations with a fixed positive margin above the displayed threshold. Smaller linear singleton/train-surplus banks remain compatible. No return endpoint is assigned across a particular owner separator by this argument.

The source candidate's exact verifier was independently run. It checked 1,154 anchor cases, 47,314 positive-cone cases, 36,138 finite ledger cases, and the stated long-pocket regression with rational arithmetic. The verifier does not prove source KKT existence, near-disk compactness, or the analytic shore argument; those were audited above against canonical dependencies.

## 6. One-vertex shield for a convex unit-contact wall

Let F be a convex polygon whose sides are actual unit contacts in a unit-separated source A, choose one wall vertex v, and let a,b be its wall neighbors. Define:

    W_F,v = {x in int(F): |x-w| > 1 for every wall vertex w other than v}.

Every x in W_F,v is strictly farther than one from every old source point outside int(F) except the deleted v. For |x-v| > 1, this is the canonical unit-edge crossing shield. Otherwise translate v to zero, put r = |x| ≤ 1, and let K_v be the convex cone spanned by the unit neighbor vectors a,b. Since x is in int(K_v), strict clearance from a,b gives:

    x·a < r^2/2,    x·b < r^2/2.

For any exterior direction u outside the interior of K_v, the maximal dot product x·u occurs on a boundary ray, so x·u ≤ mu := max(x·a,x·b) < r^2/2 ≤ 1/2. If an old exterior point q = t u lies in this case, source separation from v gives t ≥ 1, whence:

    |x-q|^2 ≥ r^2 + t^2 - 2t mu ≥ r^2 + 1 - 2mu > 1.

If q outside F lies inside the cone, the segment [x,q] first exits through a wall edge with both endpoints retained (it cannot leave through an edge incident with v). At an exit point z = (1-s)c + sd, the weighted-square identity and unit side length give |x-z| > sqrt(3)/2 and |q-z| ≥ sqrt(3)/2, so |x-q| > sqrt(3). Thus the shield covers all exterior source points, including contact isolates.

If S = A intersect int(F) and a finite unit-separated packet Y subset W_F,v has |Y| ≥ |S| + 1, delete S union {v} and insert |S| + 1 points after a sufficiently small dilation of Y. Strict guards and finiteness preserve every new-old lower constraint; dilation makes every new-new distance strict. No new contact appears. Every inserted point is inside the old source hull, so every pair involving it is strictly shorter than the old diameter D; old-old distances are unchanged. The new set is triangle-free and has diameter at most D, but loses at least the two wall contacts at v. Global optimality or contact-minimality therefore excludes this wall/packet.

For a convex unit wall with at most five edges, W_F,v is empty. The ear triangle at v is covered by the unit disks centered at a,b; a point clear of both lies inside the polygon formed by the remaining vertices and cannot lie on chord ab. The remaining boundary consists of at most three unit edges and the closing chord of length at most two. Seen from a strict interior point clear of all retained vertices, each unit edge subtends less than pi/3 and the closing chord less than pi, so the positive winding angles sum to less than 2pi, impossible.

Six edges are the first possible one-deletion threshold. The exact verifier confirms the reported convex unit hexagon with a strict site after deleting one vertex, a retained-wall squared-distance margin 33/256, and unchanged local packet diameter. In a canonical physical unit hexagon face, the interior has no contact-isolated source point by C-SHORT-WALL-ZERO-CAPACITY. The one-vertex endpoint then excludes any site covered by at most one closed unit disk centered at a wall vertex. Hence every interior point must be covered by at least two such disks. This is a necessary wall-shape condition, not a packet capacity theorem for arbitrary hexagons.

The two-deletion regression is exact: the source consists of the unit square vertices and the isolate q = (1/2,-9/10). After deleting the bottom vertices, x = (1/2,1/20) is clear of both retained top vertices but:

    |x-q|^2 = 361/400 < 1.

Thus the one-vertex shield cannot be iterated across two deleted wall vertices without extra guards.

## 7. Audit ledger and exact dispositions

| Claim | Verdict | Disposition |
| --- | --- | --- |
| Narrow-window selected O--O terminal capacity | PASS | Canonical C-OO-TERMINAL-OWNER-CAPACITY |
| Disjoint-crosscut owner region recurrence | PASS | Canonical C-OWNER-REGION-TREE-RECURRENCE |
| Acute independent-binary owner laminarity | PASS | Canonical C-ACUTE-BINARY-OO-LAMINARITY |
| Loaded binary witness budget N_BB_binary ≤ u_B | PASS | Canonical C-BINARY-LOADED-WITNESS-POCKET-BUDGET |
| Terminal N_OO = o(D) and exact face ledger | PASS WITH QUALIFIED RATE | Canonical C-OO-TERMINAL-TRAIN-POPULATION; epsilon is universal and nonexplicit, onset may depend on the sequence |
| One-vertex convex unit-wall shield and endpoint | PASS | Canonical C-ONE-VERTEX-CONVEX-WALL-SHIELD |
| Three-owner crossing rhombus | REGRESSION VALID | C-CROSSING-MULTISHEAR-INDEPENDENT-OWNER-REGRESSION |
| Two-deletion square/isolate packet | REGRESSION VALID | C-TWO-WALL-DELETION-EXTERIOR-SHIELD-REGRESSION |
| Four-train hub/Horn packet | ABSTRACT REGRESSION VALID | C-ABSTRACT-OWNER-HORN-PACKET; it is not a source realization, and its u_B = 0 narrow-window data are excluded by the long-pocket theorem |
| Overlap-aware owner run/root allocation in hub report Eq. (5) | CONDITIONAL ONLY | No promotion: owner-run boundary occurrences were not independently injected into distinct per-owner train banks |
| Common-diameter hub and fourteen-cut tube estimate | UNREVIEWED | Not needed by the promoted claims; no independent reconstruction here |
| Source geometry or KKT realization of any Horn packet | NOT CLAIMED | No such source is supplied |
| C-II or Level I closure | NOT CLAIMED | Full-core and macroscopic-container gaps remain |

## 8. Verifiers and computation

The four copied scripts are exact finite checks:

- verify_target_c_hub_owner_systems_2026_10_06.py: integer trees, labels, Boolean Horn truth tables, and abstract packet counts. It checks the finite encoded obstruction and combinatorial identities only.
- verify_target_c_terminal_oo_geometry_2026_10_06.py: rational two-edge-pocket angles/determinants, positive-cone sign cases, exact ledger cancellations, and a long-pocket regression. It does not verify the asymptotic source/KKT proof.
- verify_target_c_binary_crossing_scope_2026_10_06.py: rational rotation and all pairwise distances in train and independent-owner states; it establishes the stated finite regression only.
- verify_target_c_one_vertex_wall_shield_2026_10_06.py: exact arithmetic in Q(sqrt(808669)) for the six-edge wall/packet and rational arithmetic for the two-deletion regression. The universal shield and five-edge impossibility are analytic, not sampled.

Each was rerun at the immutable source snapshot; all completed successfully. No floating-point comparisons are load-bearing. No external literature was used.

## 9. Exact frontier effect and remaining obligation

In every canonical full-core Type-II sequence with q/D → pi and u_B = o(D), no linear O--O train bank is available: N_OO = o(D). In the narrow-window independent-binary branch, distinct loaded binary lower witnesses also number at most u_B. A live finite-motion proof in this branch must therefore obtain its linear obstruction/repair currency from outer-to-bounded or bounded-to-bounded face-coupled trains, unary rhombus tests, and the actual full-source diameter/upper constraints. It may not infer that a linear O--O family exists from owner topology, return lengths, or bad-terminal budgets.

The one-vertex shield removes one deleted wall vertex from the guards needed by embedded-wall replacement and excludes a strict one-site activation inside any canonical physical unit hexagon. It does not provide packet capacity for regular hexagons, large locked walls, or macroscopic containers.

**Exact next C-II lemma:** in the terminal q/D → pi, u_B = o(D) regime, construct a source-realized finite move or discrete replacement from the remaining outer-to-bounded/bounded-to-bounded train and face system that passes every old contact, full-source lower pair, actual diameter, inactive upper pair, and unary rhombus test and yields strict contact loss at diameter D or a strict sub-D competitor.

**Promotion recommendation:** promote only the six finite/asymptotic claims and two exact scope regressions listed above. Keep Level I open.
