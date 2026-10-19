# Destination audit: PR #950 Type-II common-grid access

**Audit verdict: CONDITIONAL PASS for the common-grid implication only.** The crop, deficit, interface, local pseudogrid, and face-tail steps below check out under the stated inputs. The linear positive-return family is a separate candidate relation, not a canonical claim; this result is conditional on that family. Nothing here promotes the imported candidate, closes C-II, or supplies a finite competitor.

## Exact scope and pins

- Investigation: `audit-target-c-pr950-typeii-common-grid-access-paired-20261019`.
- Refined scope key: `36574f29b112091f79adf3e9`.
- Reviewed destination main: `7d0a450fe66991036541023f95c44c064a04b6a8`, tree `db766e0e25b562054df26aeec7e627d5a579dd6d`.
- State / priority / catalogue: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.
- Candidate: `TARGET-C-PR950-TYPEII-COMMON-GRID-ACCESS`, still `unreviewed` in the destination candidate registry.
- Destination report `docs/reports/target_c_train_return_length_budget_worker03_2026-10-10.md`: SHA-256 `4ba5214ff20a2548c7e04d01e821f85ea941ffce40dd1ee1d7673c905892941f`; Git blob `31c04a46396771ac41d9237e55af1538c0e8af3b`.
- Preserved source-side audit `docs/audits/pr950_autonomous_proof_audit_2026-10-15.md`: SHA-256 `8ea063ae82c8d4149fee0d21ab6f2eb0d53a6702c62c162a5dd5cfd08a56bb70`; Git blob `61d91aac5e797ef6fd29aa7d5c7cfa6f6ca7891f`.
- Source PR #950 is from `e-99` at head `cbf066bb7489115559bcda34f9f810a1d78826ce`, tree `80dd0d6db99d9aa6698ee6500c91a3f670c63aae`. This review uses the pinned destination bytes above; the preserved source audit is historical provenance, not the destination review.

The report hypotheses are a canonical C-II Type-II quadratic-core sequence with `D -> infinity`, `R_4/D^2 -> r > 0`, fixed `epsilon in (0,r)`, fixed `lambda > 0`, fixed phase tolerance `epsilon_g in (0,pi/6)`, and a fixed face-tail route radius. All source labels remain present, including contact-isolated points. The claim is only that a positive-density subfamily of distinct actual return attachments has `< lambda D` actual contact routes to every vertex of one common coherent grid. Root-to-grid concatenations may overlap; no endpoint overlap, congestion bound, stress payment, or finite move is claimed.

## Conditional common-grid lemma

Let `kappa_I > 0` be the return-density constant for a linear family of distinct first-loaded return attachments in one unloaded component `I_D`; the family comes from the separate candidate relation `TARGET-C-PR950-TRAIN-RETURN-LENGTH-QUANTILE`. The exact positive-length return proof and Oler quantile have their own independent destination audit in open draft PR #108, which explicitly excludes the common-grid construction. That relation is not canonical or promoted here, so I use it only as a conditional input.

For fixed `lambda`, apply canonical `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` with `eta = kappa_I/8`. It supplies a fixed `rho_0 > 0` and fewer than `eta D` exceptional attachment incidences. The return quantile leaves at least `(kappa_I/2 - o(1))D` distinct attachments before this deletion, hence at least `(kappa_I/4 - o(1))D` good distinct attachments remain (the arithmetic leaves `3 kappa_I/8`; the report uses the weaker quarter bound).

Write `P = P_{I_D}` for the actual convex attachment cell. By canonical `C-UNIFORM-HARMONIC-CELL-AREA`, for fixed `alpha > 0` and `d_0 = sin(pi/12)/4`, eventually `area(P) >= alpha D^2` and `diam(P) >= d_0 D`. Its diameter is at most `D`, and the convex perimeter-diameter bound gives `per(P) <= pi D`. If `d = diam(P)` and `w` is the width perpendicular to a diametral segment, then `area(P) <= d w`, so `w >= alpha D`. One side of the diametral line reaches height at least `w/2`; the triangle on the diametral segment and this point lies in `P`, has area at least `d w/4 >= d_0 alpha D^2/4`, and perimeter at most `3D`. Its inradius is at least `2 area/perimeter >= r_0 D`, where `r_0 = d_0 alpha/6`. Thus `P` contains a disk `B(o,r_0D)`.

Choose a fixed `rho in (0,min(rho_0/2,1))` and set `delta = rho r_0/2`. The perimeter bound partitions `partial P` into at most `N = ceil(pi/delta)` arcs of length at most `delta D`. Pigeonholing the good attachments gives at least `(kappa_I/(4N)-o(1))D` distinct return endpoints on one arc. Fix one, `a_*`; every selected `a` on that arc satisfies `|a-a_*| <= delta D`.

For each selected endpoint define its convex cell crop `Q_a = (1-rho)a + rho P`. Define the common disk `Q_* = (1-rho)a_* + rho B(o,r_0D/2)`. For every `x in B(o,r_0D/2)`, put

```text
x_a = x + ((1-rho)/rho)(a_* - a).
```

Then

```text
|x_a-o| <= r_0D/2 + ((1-rho)/rho) delta D
         = r_0D(1-rho/2) < r_0D,
```

so `x_a in P`. Also `(1-rho)a + rho x_a = (1-rho)a_* + rho x`. Hence `Q_*` lies in every `Q_a`, and convexity gives `Q_* subset P`. Since `Q_a subset B(a,rho D)` whenever `diam(P) <= D`, every common-crop point lies within `rho D < rho_0D` of every selected attachment. The common disk has area `pi rho^2 r_0^2 D^2/4`.

This uses the actual harmonic attachment cell `P`, not the convex hull of an arbitrarily selected grain. That distinction matters: the canonical Audit.173 rejected a crop of one selected grain's hull as insufficient to guarantee rhombic filling near every attachment; its repaired proof uses a crop of the full cell and the global cell-deficit estimate.

In Type II, canonical `C-HARMONIC-CELL-TILING` gives nonnegative local deficits `Delta_I = area(P)-A_{4,I}` with `sum_I Delta_I = o(D^2)`, so the selected cell has `Delta_I=o(D^2)`. Rhombi meeting the circular boundary `partial Q_*` lie in a constant-width boundary tube of area `O(D)`; their face interiors are disjoint and each strict unit rhombus has area at least `sqrt(3)/2`. Removing these `O(D)` faces and the `o(D^2)` cell deficit leaves `Omega(D^2)` area in actual unloaded-only strict rhombi wholly inside `Q_*`.

For fixed `epsilon_g`, canonical `C-COHERENT-GRAINS` removes only `O_{epsilon_g}(D)` additional rhombi and gives total physical interface perimeter `O_{epsilon_g}(D)`. Cropping along `partial Q_*` adds only `O(D)` faces and perimeter. The retained coherent components in `Q_*` therefore have total rhombus area `Omega(D^2)` and total perimeter `O(D)`. For component `j` with `R_j` rhombi and perimeter `P_j`, isoperimetry and the face-area lower bound give `P_j >= 2 sqrt(pi (sqrt(3)/2) R_j)`. Thus `sum_j sqrt(R_j)=O(D)` while `sum_j R_j=Omega(D^2)`, so one component has `R_j=Omega(D^2)` and `P_j=O(D)`.

That cropped component is still an edge-to-edge finite rhombic complex; all faces meeting the cut are removed, and holes are allowed. Its local train tracks terminate at the cropped boundary. Theorem 10.6 in `docs/theory/01-local-structure.md` applies to arbitrary finite edge-to-edge rhombic complexes, including holes: `P_j=2T_j`, `R_j <= T_j^2/4`, and its train-crossing graph is triangle-free. The exact pseudosegment statement used by the canonical `C-PSEUDO-GRID` proof is also in Fox, Pach and Suk, Theorem 2.12: at least `eta n^2` crossing pairs yield two all-crossing subfamilies each of size at least `c eta n`. I checked the primary [arXiv paper](https://arxiv.org/abs/2312.01028); its stated bound is linear in `eta n`, without a logarithmic loss.

Since `R_j=Omega(D^2)` and `T_j=O(D)`, the pseudosegment extraction yields two crossing shores of size `Omega(D)`. Triangle-freeness makes each shore internally noncrossing. The fixed phase cut supplies the same coherent three-phase frame to each local track; same-label tracks cannot cross because their angular separation is `< pi/6`, whereas an actual rhombus crossing requires separation `> pi/3`. The label supports of the two crossing shores are disjoint, so selecting a largest label class on each shore loses at most a factor two per shore. This gives a complete phase-coherent grid of linear shore sizes whose crossing rhombi and source vertices lie in `Q_*`, hence in `I_D` and within the face-tail route radius of every retained attachment.

For each selected attachment, the canonical face-tail theorem gives an actual route of fewer than `lambda D` contact edges to every source point of `I_D` within `rho_0D`; every grid vertex qualifies. For the `theta=1/2` return-length quantile, the terminal-to-attachment part has at most `(pi/(sqrt(3) kappa_I)+o(1))D` edges. Concatenation therefore gives routes to every vertex of the common grid of length at most `(pi/(sqrt(3) kappa_I)+lambda+o(1))D`. Only the terminal-to-attachment segments are vertex-disjoint; the continuations may overlap. No common-label overlap with the separate attachment-to-grid Menger family follows.

## Dependency and scope audit

| Input | Current status and use |
| --- | --- |
| `C-QUADRATIC-CORE-DISJOINT-TRAIN-RETURNS` | Canonical; supplies the underlying long-train/return scale. The positive-length same-component quantile used here is a separate candidate relation, treated conditionally. |
| `C-UNIFORM-HARMONIC-CELL-AREA` | Canonical; fixed positive cell area, diameter and bounded component count. |
| `C-TYPEII-FACE-TAIL-PORT-MULTIPLICITY` | Canonical; exceptional attachment-incidence count and actual short contact routes. |
| `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` | Canonical; separately provides per-attachment grid access. The common-crop extraction itself is supplied by the cell deficit/coherent-grain/pseudogrid chain below. |
| `C-HARMONIC-CELL-TILING` | Canonical in Type II; nonnegative cell deficits summing to `o(D^2)`. |
| `C-COHERENT-GRAINS` | Canonical; fixed-phase deletion and total interface perimeter `O(D)`. |
| `C-PSEUDO-GRID` | Canonical; finite extraction from the cropped coherent rhombic component, using local tracks stopped at its boundary. |

The task card's `existing_checks` concern a separate sparse-stress fixture; they do not review this grid. The `TARGET-C-PR950-TYPEII-COMMON-GRID-ACCESS` candidate record itself says no destination audit or finite verifier was supplied. The common-grid proof is analytic. The only applicable finite dependency checker I found is the face-tail port-multiplicity regression; the report itself records no computation. The listed `C-TYPEII-LOCAL-COHERENT-GRID-ACCESS` is not needed for the shared-target extraction, though it is an applicable canonical per-attachment input for the preceding individual-grid statement.

## Finite controls actually run

Under the shared compute lock, the current destination checker `research/verify_target_c_face_tail_port_multiplicity_2026_10_08.py` (SHA-256 `53f789d26c01b8d3643f3b0c7ff9a5f43f94afab4acb2af0a6ad84709c8c0583`) passed. Its three exact rational fixtures use 64, 128, and 256 antipodal diameter ports; aggregate reported checks are 42,784 full-source pairs, 96 flatness vertices, 15,680 port/body/radius incidences, 21 weighted identities, 84 Markov thresholds, 480 strip cases, and 448 prescribed-port triangles. The fixtures are explicitly nonglobal/contact-isolated and do not certify source augmented faces, Type-II sequences, or global optimality.

The new `verify.py` passed normally and under optimized Python. It checks eight exact rational directions in the common homothety identity and a negative control showing that separation above `rho*r_0/2` can move a translated point outside the larger disk. This is only a finite algebra fixture; it does not verify arbitrary convex-cell containment, the `o(D^2)` deficit, coherent cuts, or pseudogrid existence.

## Predecessors, overlap, and limits

I reconstructed the common-cell crop and finite pseudogrid argument from the destination report and canonical proofs before reading the preserved PR #950 source-audit conclusions. That source audit records a historical check of the common-grid proof, but its own preamble and current registry correctly say it is provenance-only in this destination. I then compared the independent derivation with it.

Live overlap review was refreshed at `2026-10-19T09:42:25Z`: complete pagination covered 48 open PRs, 0 open Issues and all 8 discussion/comment/reply records (four discussion threads). No prior exact common-grid destination audit appeared. Open PR #108 independently audits only the positive-return quantile; PR #112 audits only the endpoint-inclusive separator repair; PR #119 audits only the unloaded-set brace. Their exact bodies state that they do not audit the common-grid construction. The only PR added since the launch snapshot was #149, an unrelated large-array boundary-attachment audit. Discussion #83 has no PR #950/common-grid handoff. The separate scope distinctions are recorded in the run handoffs.

The local checker does not prove this asymptotic lemma. This audit does not re-audit the full return-quantile candidate, the separate attachment-to-grid Menger linkage, the rigidity brace, endpoint overlap, stress-mass allocation, or any finite competitor. Required repository-wide theorem-certificate replay is **deferred to the merging agent**. Level I and Target C-II remain open; C-I remains closed. Every source label, including contact isolates, is retained, and no lower/upper pair constraint is changed because no point is moved.

## Exact remaining lemma and downstream use

The next route-changing result remains a linear common-label overlap between the train-root-to-loaded-attachment family and the attachment-to-grid family, or a direct source-wide flow theorem. A positive overlap could produce a linear root-to-grid linkage; a counterexample would show that path counts alone cannot compose these two families. Even that linkage would still need a same-cardinality finite endpoint satisfying every lower bound and every old/new actual-diameter upper bound, and at diameter `D` it must remain triangle-free and strictly improve the lexicographic pair (unit contacts, actual diameter pairs).

## Attribution and AI disclosure

The proof candidate is first-party research from Worker Slot 03 / source PR #950. This destination audit and the small exact fixture were prepared by OpenAI Codex (GPT-6 Luna xhigh), reviewer slot `homelab-06`, independently of the originating proof and its checker. I used the cited paper only to check Theorem 2.12's stated input/output; no paper text was copied. The audit and fixture are offered under Apache-2.0. No human mathematical review or external validation is claimed.

## Reproduction

```sh
python -I -B research-packages/e99-paired-20261019t091333z-homelab-06/verify.py
python -I -O -B research-packages/e99-paired-20261019t091333z-homelab-06/verify.py
flock -x /home/cinna/.local/state/erdos99-host-compute.lock python research/verify_target_c_face_tail_port_multiplicity_2026_10_08.py
```

Package metadata checks establish only pinned inputs and declared commands. No full theorem-certificate suite was run.
