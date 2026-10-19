# Independent audit: PR #948 deep-face persistence and isolate deficit

**Verdict: PASS for the exact conditional statement in the destination report, with the canonical source tie-break stated explicitly below.** This review does not promote the candidate or change theorem state. It audits only `TARGET-C-PR948-DEEP-FACE-PERSISTENCE`, principally the loaded-component, face-persistence, and rigid-boundary isolate-deficit chain in §§3–5 of the pinned report. The separate active-bank and small-face-district claims in §§6–7, and the other PR #948 candidates, are outside this assignment.

## Reviewed bytes and lifecycle

- Destination repository: `1337isnot1337/erdos-99`.
- Reviewed destination main: `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state `2026-10-15.publication.2`; priority `public-frontier.3`; catalogue `public-frontier.9`.
- Historical source provenance: `1337isnot1337/e-99` PR #948, head `b7376d13b81e542055c5c904bf81bdaf1beb7b9e`, tree `4d2357368d1a2fa71b318741bf263e9aad342f8a`. The mathematical review here is of the destination bytes, not another review of that historical source PR.
- Candidate registry status at the reviewed destination: `unreviewed`; `canonical=false`; no source claim IDs. Destination report, verifier, and saved certificate all matched the assignment's destination SHA-256 and Git-blob pins.
- Report SHA-256: `7c1927a90124a376017a62a784d51851b478a9dd17efacb76505722d85bf3e37` (blob `b8d9e8bab6e4b2b1a21e7f77b57e7ade48b73c05`).
- Verifier SHA-256: `53cfc3d7ec915b5a5b903580f64b936473b5c86c1f223b8f0d23cef1a097cc7c` (blob `ae279ea2469e2f2fb5c13c503ea9607a62c4450c`).
- Saved certificate SHA-256: `51aee524684833326c94c5a4457d8ddc7afb4784759a4ec7761a6a03f2047ad7` (blob `fc73737489758899e2fad30e562ca0600e3965a6`).
- The verifier imports `research/verify_target_c_quarter_fold_face_obstructions_2026_10_10.py` for exact rational geometry (SHA-256 `ced2ae1bb3ee3834f0a36d5869d25c7aedc0e447df2c8bb17013cf1d4a0a7d89`).

The refreshed destination overlap scan found no audit of this candidate ID. The final private refresh at 2026-10-19 09:56 UTC covered 70 open PRs, 0 open Issues, 97 closed PRs, and 8 Discussions with comment/reply pagination. Closed PR #24 is the historical destination integration of source PR #948; its body says the seven candidate reports remain unpromoted and it is not a mathematical audit. Open PR #116 audits the distinct `TARGET-C-PR948-QUARTER-FOLD-FACE-OBSTRUCTIONS` candidate; its exact scope does not review this persistence/transport result. Discussion #83 and the predecessor handoff records contain no matching destination audit. I read PR #116 as overlap evidence and did not use its conclusions as proof of this candidate. The repository refresher initially failed because this host's `gh` rejects `--slurp`; a private complete cache was then refreshed with supported `gh api --paginate` calls and queried offline.

## Exact statement and hypotheses

Take the report's canonical C-II source, not a source selected only for minimum contact count: a triangle-free global minimizer in the stated `D >= 9` regime, selected first with minimum `|C|` and then minimum actual-diameter-pair count `|H|`, with every source label (including contact isolates) retained in any full-source endpoint. The nonisolated positive-contact core is connected; the canonical relative-interior contact stress is positive on every core contact, and a core vertex outside the loaded set `B` is a positive-weight harmonic average of its contact neighbors.

For face persistence, `F` is a simple convex actual bounded face of the old contact core, with boundary labels `W` and degree `m`; `Q` is a unit-separated placement of the entire core with exactly the old contact graph. The report's deep-face condition is the old-source distance `dist(p(W),p(B)) > C_m`, where

`C_m = floor(m^2/(2*pi*sqrt(3)) - m/2 + 1)`.

For the isolate-deficit result, the endpoint must also have a rigid boundary **as a point set**: `Q(W)=R(p(W))` for one Euclidean isometry `R`, so `F'=R(F)`. A component `T` of `G-W` is hypothesized to lie inside `F'`; `z` is the number of old contact isolates in `int(F)`. Boundary labels may be permuted by `R`. This is the report-specific embedding hypothesis; exact contacts alone do not make an arbitrary face rigid.

The minimum-`|H|` tie-break is load-bearing when the replacement keeps diameter `D`: the constructed competitor keeps `|C|` and removes at least one actual diameter pair. Under a literal reading with only contact-minimality, that branch would not contradict minimality. The report §1 and canonical `C-RHOMBUS-POP` dependency supply the required second tie-break; the abbreviated candidate summary should not be reused without it. The strict-sub-`D` branch needs only global optimality.

The listed dependency scopes were checked against the manifest. `C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION` and `C-QUARTER-FOLD-MINIMUM-FACE-SIZE` supply the four-transition and minimum-two-edge-arc facts used by Corollary 4.2. Canonical `C-RHOMBUS-POP` (including its `C-ZRF`/full-source geometry dependencies) supplies the connected canonical core, positive contact weights, loaded set, and harmonic equations used in Lemma 3.1. The report's Oler input is Lemma 21.1 in `docs/theory/03-oler-shell.md`. `C-FULL-SOURCE-ISOLATE-NORMALIZATION` is used only by the later §6 endpoint-count extension; `C-SHORT-WALL-ZERO-CAPACITY` and `C-UNIT-WALL-PACKET-POPULATION-BOUND` support later wall/population consequences, not the local §3–5 capacity proof. Those claims assert no outside-population bound or packet existence. The registry's candidate relation to `TARGET-C-PR948-QUARTER-FOLD-FACE-OBSTRUCTIONS` is not treated as a proved premise; the reviewed report supplies its own persistence argument.

## Proof reconstruction

1. **Every component outside a convex face contains an old loaded label.** Suppose a component `T` of `G-W` has no vertex in `B`. Every vertex of `T` then satisfies the positive contact-barycenter equation. For any linear functional, a maximum in `T` above all values on `W` propagates through positive weighted averages along the connected component until it reaches a boundary contact in `W`, a contradiction. Applying separation by a linear functional gives `p(T) subset conv(p(W))=F`. But `T` is outside the old actual face in the plane contact drawing; its core vertices cannot lie on a unit boundary edge or in the face interior. Contradiction. Connectedness of the core and positivity on every core contact are necessary here; the argument does not assume the endpoint's old loads persist.

2. **A nonfacial exact-graph endpoint component is small.** A unit-separated straight contact drawing is plane: two crossing unit edges would give distinct endpoints at distance strictly below one. Exact graph preservation forbids a new nonconsecutive unit chord of `W`. If the new cycle is not a bounded face, some component `T` of `G-W` lies inside it. The `m` boundary labels and `T` are unit-separated in the convex hull `K'` of the new boundary points. The polygon perimeter is at most `m`, hence `per(K') <= m`; the isoperimetric inequality gives `area(K') <= m^2/(4*pi)`. Oler's finite packing inequality,

   `N <= 2 area(K')/sqrt(3) + per(K')/2 + 1`,

   yields `m+|T| <= m^2/(2*pi*sqrt(3)) + m/2 + 1`, hence `|T| <= C_m`. Step 1 supplies `b in T intersect B`; an old contact path from `b` to `W` has at most `|T|` edges, so its old Euclidean distance to `W` is at most `C_m`. Therefore `dist(p(W),p(B)) > C_m` forces the old core face to persist. This bounds only core intrusions; it gives no bound on contact isolates or a uniform large-face tail.

3. **Nonconstant feasible quarter-folds bring a load close.** The canonical convex-face classification and minimum-face-size result reduce a nonconstant face fold to four transition arcs, each of length at least two. Transition turns in the folded cycle have the opposite sign from internal arc turns, which retain strict convexity. Thus the folded cycle is nonconvex. The strict-convexity premise follows from the same canonical source choice: a reflex vertex of a simple face is nonextreme in the source hull, and a straight vertex is the midpoint of its two unit face neighbors, so neither can carry an actual diameter. Its contact rays lie in the complement of the empty face sector, a closed cone of width at most `pi`. Moving the vertex a small amount opposite the cone bisector makes each incident squared distance `1 - 2*epsilon*d dot (w-v) + epsilon^2 > 1`; all other lower and upper margins remain strict by finiteness. This gives a full-source contact-losing, triangle-free feasible minimizer, contrary to contact minimality. If the folded cycle remained an actual bounded face, the full feasible endpoint would again be a triangle-free global minimizer with the same minimum contact count, contradicting this strict-convexity result. It is therefore nonfacial, and Step 2 places an old loaded label within `C_m` of the old boundary. This is conditional on the full-source feasible endpoint; it does not construct one.

4. **Rigid-boundary intrusion costs one isolate slot.** Suppose there is a guarded packet of `z` points inside `F'`, pairwise at distance at least one and strictly more than one from `Q(W) union Q(T)`; for `z=0` use the empty packet. Dilate slightly about an interior point so packet-internal unit pairs become strict while all strict guards and containment remain. Pull `Q(T)` and this packet back by `R^-1`; delete the old `T` labels and all `z` old interior isolates, then insert the same number of labels at the pulled-back positions. Every other source label, including every exterior isolate, remains fixed.

   The lower-pair ledger is complete. Isometry preserves component-internal distances and the number of wall contacts, including when the wall permutation changes contact labels. For an inserted point `x` and any retained nonwall point `a` outside `F`, segment `xa` crosses a unit wall edge `cd` at `w=(1-t)c+td`. From both endpoints being at least one from `c,d`,

   `|x-w|^2, |a-w|^2 >= 1-t(1-t) >= 3/4`,

   so `|x-a| >= sqrt(3) > 1`; if the crossing is at a wall vertex the lower bound is at least two. No retained old core point lies inside the actual face, and all old interior isolates were deleted. Packet guards handle the other inserted points against the component and wall.

   The upper-pair ledger is also complete. All inserted points lie in `int(F) subset int(conv(A))`. An interior point of a convex set of diameter `D` is at distance strictly below `D` from every point of that set; otherwise moving a small amount farther from the other point while remaining in the set contradicts its diameter. Thus every inserted-involving upper pair is strict, while retained-retained pairs are unchanged. This checks old active pairs and every previously inactive upper pair; none can become a new diameter.

   The replacement retains cardinality, preserves the total contact count, and stays triangle-free. The `T union W` contact graph is geometrically isomorphic to that in `Q`, with the isometry-induced wall permutation; no inserted point contacts a retained nonwall point, and packet points are isolates. By Step 1, `T` contains an old loaded label, so at least one old diameter incidence is removed and none is created. The result is either a strict sub-`D` global competitor or, at diameter `D`, a triangle-free minimizer with the same `|C|` and smaller `|H|`. Both contradict the full canonical source choice. Therefore the guarded packet capacity is at most `z-1`; an exact-graph endpoint's interior isolates form such a packet and obey the same deficit. The argument uses positions, not area slack or separately compatible exchanges.

The selected-face sum in Corollary 5.2 additionally requires pairwise-disjoint new interiors and the stated population bound on the other selected faces. It proves only a conditional outside-population increase; it does not identify evacuated labels or bound outside capacity.

## Adversarial checks and finite evidence

- Boundary-label permutation is handled by a point-set isometry, not a label-affine fold. The 13-label rational fixture checks all `78` pairs on each side (`156` total); the correct isometry preserves the complete distance multiset, while naive isolate transport gives squared clearance `128917/130000 < 1` and fails.
- The one-vertex intrusion fixture checks three full pair ledgers (`234` pairs). A loaded old leaf moves into the new cycle, loses a diameter incidence, and a `1/100` release opens its contact. Its straight old vertex is not positively equilibrated, so the fixture is explicitly nonglobal and is only a guardrail against dropping the harmonic hypothesis.
- A 13-point triangular-lattice comparator checks all `78` pairs and has squared diameter `16`, below both source-fixture values `18` and `324/13`; neither rational fixture is global.
- The exact-rational floor control encloses `pi` by Machin's alternating series and `sqrt(3)` by integer square roots, then verifies the same floor at both interval endpoints for every `m=5..32`. It verifies arithmetic, not Oler or the analytic persistence theorem.
- The local three-ray control enumerates all eight sign assignments; four collide, two leave the center in a half-plane, and two make it strictly surrounded with positive weights `13,10,13`. It models no globality or full-source move.

Reproduction from the reviewed base:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock \
  python research/verify_target_c_deep_face_transport_2026_10_10.py
```

The command exited `0`; its output matched the pinned saved certificate byte-for-byte. The checker uses Python `assert` statements, so the reported run is the ordinary interpreter run, not `python -O`. The exact area-packing input is Oler's finite inequality; the repository states and derives the normalization in `docs/theory/03-oler-shell.md`, and the primary reference is Norman Oler, [“A Finite Packing Problem” (1961)](https://doi.org/10.4153/CMB-1961-018-7). No external paper text was copied.

## Scope, limitations, and next lemma

The candidate remains unreviewed/noncanonical pending maintainer disposition. Level I, Target C-II, and the universal `every sufficiently large n / every global minimizer` question remain open. This audit proves no source extraction, endpoint existence, large-face tail, exterior isolate capacity, or universal same-cardinality replacement. The older local/nonglobal examples do not close those gaps.

The next missing lemma is to bound or realize the full-source isolate population outside a pairwise-disjoint bank of rigid face images under the diameter budget, or to construct a source-derived full-source endpoint meeting every lower bound, active and inactive upper bound, and isolate constraint. Either result changes whether the isolate deficits can be paid and hence the canonical actual-diameter-pair count `|H|`; proving the capacity bound would make the selected-face deficits contradictory, while a counterexample would identify the required moved-wall or nonlocal replacement mechanism.

**Review independence and credit.** This is an independent review by OpenAI Codex, GPT-6 Luna xhigh, worker `homelab-07`; the reviewer did not author, edit, or verify the candidate proof or checker before this pass. Source credit remains with PR #948, worker slot 02; that source report does not identify its model/session. No human mathematical review is claimed. This review records a conditional research result, not a promotion transaction.
