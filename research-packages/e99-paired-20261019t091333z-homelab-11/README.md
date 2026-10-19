# Independent destination audit: PR #952 unequal-height isolate transport

**Verdict: CONDITIONAL PASS** for the report's strict-floor finite endpoint theorem under its stated supplied-group hypotheses. The shortest-path closure proof and the full-source finite replay are correct within that scope. The missing premise for C-II remains source extraction with at least one contact-bearing group surviving the exact floor closure. This review does not establish that premise, change the candidate's lifecycle, or promote a theorem.

Reviewer: OpenAI Codex session `/root`, GPT-6 Luna xhigh, assigned worker `homelab-11`. This is an AI-agent audit of the destination bytes; it is not an external or human mathematical review.

## Exact reviewed bytes and provenance

- Destination source commit and launch base: `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Theorem state: `2026-10-15.publication.2`; priority: `public-frontier.3`; catalogue: `public-frontier.9`.
- Candidate: `TARGET-C-PR952-UNEQUAL-HEIGHT-ISOLATE-TRANSPORT`, artifact ID `ART-982CE41762F7`.
- Candidate report `docs/reports/target_c_parallel_release_floor_closure_and_isolate_transport_2026-10-10.md`: SHA-256 `5a30ef0e3c15b781a79251c1bb9414b8ff6eb9229cb60c3ef6d0b25124beff4f`, Git blob `bd166e390d33923f828b704231e7fe53572c9265`.
- Finite verifier `research/verify_target_c_unequal_height_release_2026_10_10.py`: SHA-256 `7e96eaa6884dac9640358065430d426060dddfafca5a087a14ec831d3fb68a42`, Git blob `6ef4cb3f5ea7644b467411c09394e3fb6b379532`.
- Saved certificate `research/certificates/target_c_unequal_height_release_2026_10_10.jsonl`: SHA-256 `2f996f5307f5b237e78074464113d880f7683c9a816601f4874db8f5d81b8f7c`.
- The verifier's imported fixture helper `research/verify_target_c_source_realized_owner_sink_2026_10_10.py`: SHA-256 `df2cd04d208b0370cb85b3c15a2cef308b11be2a942058c724473456ad85da25`, Git blob `21de0d3ed504468f923620744d7391d0b74e50cb`. It was also read and its `Source`, interval-enclosure and symbolic-source constructors were inspected.

The three files in the assignment's `source-pins.json` matched their SHA-256 values and destination Git blobs at the reviewed commit. The candidate registry records the source lifecycle as **unreviewed** and has no `existing_checks` entry. The assigned broad catalogue card also has `existing_checks: []`.

### Source history versus destination review

The frozen source PR is [e-99 PR #952](https://github.com/1337isnot1337/e-99/pull/952). Its current GitHub head is `3536c0b6f6c2a929d9c96fffbdcfc480735fea3b`; it has no formal PR reviews. Its comments describe the prior work as needing mathematical review and later call the reconciliation mechanical, not a proof audit. The destination migration PR [#25](https://github.com/1337isnot1337/erdos-99/pull/25) reconciled files and finite outputs but explicitly did not perform the mathematical-review gate. The destination track and candidate registry continue to mark all five imported reports as unreviewed. This is the missing destination review of one pinned imported candidate, not a claim that the source history supplied an audit.

There is a source-head metadata defect: the destination track, candidate registry and destination PR #25 body contain the 39-character string `3536c0b6f6c2a929d9c96fffbdcfc480735fea3`, while the live source PR head is the 40-character SHA ending `...fea3b`. I did not edit those migration records or the candidate bytes. The audit binds to the exact destination blobs above; the malformed source pointer does not change the proof checked here, but the migration metadata should be corrected before relying on that pointer as a source pin.

I ran `python scripts/find_overlap.py --task target-c-face-coupled-move --offline --cache /home/cinna/.local/state/erdos99-pass/paired-20261019T091333Z/overlap.json --json` and inspected the exact-candidate matches and broader C-II hits. Live `gh` checks found no prior destination audit of this exact candidate or scope. Discussion #83 contains Target A/B handoffs, not this result. The broad query's PR #108 and #112 matches concern PR #950 return quantiles and endpoint-inclusive cuts. Live PRs #135 and #142 concern the separate seven-label PR #104 fixed-isolate/coupled-shear family; I inspected their full bodies and PR #104's body. Those finite motions are useful neighboring regressions, but they do not audit this supplied-group floor-closure theorem. No duplicate audit was present.

## Exact statement reviewed

Let a finite unit-separated planar source have diameter `D`. Fix a unit vector `v` and perpendicular `Jv`. Partition every source label into a nonempty fixed group `G_0` and disjoint nonempty moving groups `G_1,...,G_r`. Assume no old unit contact joins two different moving groups. Each moving group receives one height `s_i v`, with `s_0=0` and `0 <= s_i <= U_i`, where `U_i>0`. Isolates can be fixed, assigned to a moving group, or placed in their own moving groups; every source label and pair is retained.

For each old contact cut from `G_i` to `G_0`, orient its unit vector `r` from the moving label to the fixed label and define

`F_i = max(0, max{-2 r·v over cut contacts})`.

The strict-floor class allows `s_i=0` or `s_i>F_i`. For each cross-group source pair, include both difference inequalities that are exactly equivalent to its endpoint distance being at most `D`. For every old noncontact whose transverse coordinate satisfies `|z|<=1`, also include the strict difference inequality that preserves the sign of its old projected coordinate and keeps its distance strictly above one. Pairs with `|z|>1` need no lower arc. Add the height-bound arc `i -> 0` of cost `U_i`.

Start with `Z={0}`. Repeatedly compute the shortest directed path cost `c_i` from each positive group `i` to `Z`, and adjoin every `i` with `c_i<=F_i` to `Z`. At the fixed point, let `I` be the positive groups not in `Z`.

**Floor-closure theorem.** `I` is the largest possible active support of any endpoint in this strict-floor, original-order class. If `I` contains a contact-bearing group (one with an old contact to `G_0`), then a full-source endpoint exists with at least that group active. It satisfies all old lower constraints, all old and inactive upper constraints, retains every label, and has diameter at most `D`. It opens every old contact cut from active groups and creates no new contact. Therefore, for a triangle-free canonical contact-minimal source, such a surviving contact-bearing group contradicts global minimality if the diameter falls below `D`, and contradicts contact minimality if the diameter remains `D`.

The theorem is conditional on the supplied groups, direction and bounds. It does not assert that every canonical C-II source supplies them or that `I` contains a contact-bearing group.

## Independent proof reconstruction

Write `a=(p-q)·v`, `z=(p-q)·Jv`; after moving groups `i,j`, the squared distance is exactly `z^2+(a+s_i-s_j)^2`.

1. **Upper pairs.** Since the old distance is at most `D`, `u=sqrt(D^2-z^2)>=|a|`. The complete endpoint upper constraint is `s_i-s_j<=u-a` and `s_j-s_i<=u+a`. Both costs are nonnegative. These two arcs apply to actual diameter pairs and every formerly inactive pair alike; equality is allowed.
2. **Contact floors.** An old cut contact becomes `r+s_i v`, whose squared slack over one is `s_i(s_i+2r·v)`. For positive `s_i`, every cut contact opens exactly when `s_i>F_i`. Internal contacts do not change because their whole group translates together. The no-contact-between-moving-groups hypothesis means these are all old contacts that can change.
3. **Lower noncontacts.** If `|z|>1`, the endpoint remains strictly separated. Otherwise set `ell=sqrt(1-z^2)`. For an old noncontact, `|a|>ell`, so `a` has a nonzero sign. If `a<0`, retaining that sign and strict unit separation is `s_i-s_j<-a-ell`; if `a>0`, it is `s_j-s_i<a-ell`. Each relaxed graph cost is strictly positive. In particular, when `|z|=1`, `ell=0` and the strict inequality prevents a new unit contact at this boundary.
4. **Necessity of the zero closure.** Along any directed path from `i` to a group already forced to height zero, summing its difference inequalities gives `s_i` no greater than the path cost. A height-bound arc gives the same conclusion for a path ending at `0`. Thus every feasible height satisfies `s_i<=c_i`. If `c_i<=F_i`, its allowed domain forces `s_i=0`. Induction over the deletion rounds proves every group put in `Z` is zero in every feasible endpoint. Strict lower inequalities were relaxed to weak arcs here, which can only make the zero test harder to trigger; this does not falsely eliminate a feasible support.
5. **Sufficiency and maximality.** At the fixed point, `c_i>F_i>=0` for every `i∈I`; all `c_i` are finite due to the `i->0` bounds. Choose one `lambda` with `max_{i∈I}(F_i/c_i)<lambda<1`, put `s_i=lambda c_i` on `I` and zero on `Z`. Shortest-path triangle inequalities give `c_i<=c_j+c_ij` on every arc, and `c_i<=U_i`. Scaling preserves each weak upper inequality, including zero-cost arcs. It makes each positive-cost lower arc strict because `lambda c_ij<c_ij`, gives `s_i>F_i` on every surviving group, and respects every height bound. This activates all of `I`, while the necessity argument rules out any support outside `I`; hence `I` is exactly the maximal support.
6. **Geometric consequence.** The source's noncontacts remain strict by the lower arcs; old contacts are either unchanged inside groups/fixed labels or strictly opened across an active cut. No new unit contact appears. A triangle-free source therefore stays triangle-free and loses at least the contacts crossing an active contact-bearing group. All pairs were upper checked, so the diameter is at most `D`. No feasible continuous path between source and endpoint is needed for the global-minimum contradiction.

The report's signed-height addendum also checks out. For any difference inequality `t_i-t_j<=c` with `c>=0`, clipping to `t_i^+=max(t_i,0)` gives `t_i^+-t_j^+<=max(t_i-t_j,0)<=c`. For a strict lower arc with `c>0`, the clipped difference is either zero or remains below `c`. Negative groups return to zero and restore old cut contacts; the no-contact-between-moving-groups assumption prevents a restored contact from interacting with a separately moving group. If all contact-bearing groups are negative, reversing `v` first reduces to the positive case. Using bounds `2D` in both directions covers every signed height compatible with a fixed nonempty `G_0` and diameter at most `D`.

## Adversarial scope and declared dependencies

I checked the boundary and escape cases directly:

- Zero-cost upper arcs and zero-cost cycles are harmless; Dijkstra distances remain finite because every group has a positive bound arc to `0`. A group with `F_i=0` and `c_i=0` is forced to zero; a surviving isolate has `c_i>0` but cannot by itself produce contact loss.
- The strict theorem does not cover floor equality `s_i=F_i`, projected-order reversal, contact-preserving active floors, nonparallel movement, or discrete replacement. The adjacent inclusive-floor report is a separate theorem and was not reviewed here.
- The no-contact-between-moving-groups hypothesis is load-bearing for the contact-floor formula and signed clipping. I do not extend the theorem to groups with old contacts between them.
- A graph shortest path is an owner-variable certificate assembled from actual pair witnesses; it need not be a physical source-point path or a train. It supplies no geometric owner extraction.
- The three canonical IDs listed in the candidate registry are authoritative background, not a hidden bridge in this proof: `C-FULL-SOURCE-ISOLATE-NORMALIZATION` is a scoped isolate-centroid motion; `C-LONG-PAIR-ISOLATE-DISPATCH` is a binary core translation with its own isolate-anchor/exception system; `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN` concerns contact-preserving core isometries. The floor-closure proof does not use any of them to construct the supplied groups or force nonzero support. Their manifest status is canonical at this base; none closes the candidate's source-extraction obligation.
- The endpoint is a discrete feasible placement; no intermediate path is asserted. This is sufficient for the minimum-diameter/contact-minimal contradiction.

The canonical manifest keeps C-I closed and C-II open; Level I, A and B remain open. The candidate's registry lifecycle remains `unreviewed`. This package records review evidence only and performs no lifecycle or theorem-state update.

## Finite fixture and falsification checks

The report's unbounded nonglobal fixture adds an isolate `U=(5,3+5 delta_B/2)` to the eight-train source. In the exact common-vector regression, a selected owner's opposite rung contacts imply `x^2+y^2-delta_i y>=2a_i|x|`. Together with the small cloud and the old bottom diameter, a nonzero common move must have `y>0`, `y>=delta_i` and `|x|<S^2`. Selecting only A, only B, or both then makes respectively `Am0:Bm0`, `Cm0:Dm0`, or `Rm2:U` strictly shorter than one. This rules out every small common direction in that family, not independent heights.

The unequal-height endpoint repairs these exact blockers. With `U` fixed, `s_A=delta_A+delta_B/4` and `s_B=2 delta_B` open 24 contacts; the `Emj:Fmj` pairs have squared slack `(delta_B^2+delta_B^4)/16`, `Rm2:U` remains at `1+delta_B/2`, and the old diameter falls to `D^2-4H delta_B+4delta_B^2`. With a free isolate variable, the full-pair closure allows `s_A=s_B=s_U=9 delta_A/5`; the checker tests every pair involving `U` rather than assuming an anchor map. The examples are explicitly nonglobal and do not establish canonical optimality.

The verifier was rerun under the host compute lock:

```sh
flock -x /home/cinna/.local/state/erdos99-host-compute.lock \
  python3 research/verify_target_c_unequal_height_release_2026_10_10.py \
  --heights 30 31 100 --symbolic-limit
```

It exited 0. The captured stdout matches the committed JSONL certificate byte-for-byte. The three finite rows checked 47,960 + 48,840 + 128,880 = **225,680** full pair-state instances. They report 110, 111 and 180 labels; 124, 125 and 194 old contacts; 24 contacts lost in each qualifying unequal-height endpoint; all source upper pairs checked; all noncontacts strict; and the source marked nonglobal. The fixed-isolate closure retains active groups `[1,2]`; independent isolate transport has support `[1,2,3]` in all three runs. The symbolic-limit row has **13** boundary-critical pairs, each with four positive leading slack coefficients, and **5,858** other noncontacts already strict at the limit. The checker uses 120-bit rational square-root enclosures. A successful conservative-cost endpoint certifies feasibility; failure of that conservative graph would not prove exact algebraic infeasibility.

This replay also supports the report's continuity argument for the finite low cluster. Its all-sufficiently-large-`H` claim additionally uses the displayed uniform tail bounds: labels above the finite low cluster are separated from moved labels, and the only low labels below height one are the bottom diameter endpoints and their fixed counterparts. The finite checks alone do not establish the canonical source family.

The package-local checker checks that the captured replay is byte-identical to the pinned certificate and retains the expected row/count markers. It does not re-execute the original SymPy verifier; the original verifier command above was actually run in this session. The analytic theorem is audited in this README.

## Commands and remaining obligations

The original verifier replay, byte-for-byte certificate comparison, and package metadata check are recorded above. The package-local byte-integrity checker is declared in `VERIFY.json`; its command does not re-execute the original SymPy verifier. Public-integrity and local-CI results for the submitted head are recorded in the PR body. Repository-wide theorem-certificate replay was not run; required full replay is **deferred to the merging agent**.

### Open next question

- **Downstream decision and quantity:** Can the conditional floor-closure endpoint contradict the canonical C-II source by lowering the first lexicographic coordinate, the unit-contact count `|C|`?
- **Changed hypothesis:** Extract a canonical source family of disjoint moving core groups with no cross-group contacts and with at least one contact-bearing owner outside the exact full-source floor-closure zero set, while retaining every isolate variable and every lower/upper pair.
- **What either outcome enables:** A surviving contact-bearing owner gives an immediate contact-minimality contradiction at diameter `D` (or global-minimum contradiction below `D`). A collapse of every contact-bearing owner supplies an exact source-specific shortest-path certificate whose witness pairs can be fed into a new capacity or face-coupling argument.
- **First action:** Derive a canonical geometric bound that prevents all contact-bearing release floors from being reached by shortest paths in the actual all-pair cost graph.
- **Blocker:** No such source extraction or noncollapse inequality follows from the listed canonical dependencies or the finite nonglobal family.

## Attribution

The frozen source report credits Slot 01 and its first-party research; no external paper or text was imported. This destination audit was produced by OpenAI Codex, GPT-6 Luna xhigh, in the assigned reviewer role. The candidate remains unreviewed in the destination registry; this PR is a scoped independent audit record only, with no canonical promotion.
