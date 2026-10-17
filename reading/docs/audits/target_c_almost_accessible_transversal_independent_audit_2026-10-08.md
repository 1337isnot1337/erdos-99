> Generated reading edition · [exact source](../../../docs/audits/target_c_almost_accessible_transversal_independent_audit_2026-10-08.md) · source SHA-256 `54c93dfec11d5b3ef7aea5cb65fc4624c2758e9e911fe9c73fe99f00542e36e1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-5AF8246B929B","canonical":true,"claim_ids":["C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL"],"claim_statuses":{"C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: almost-accessible stress transversal

**Date:** 2026-10-08
**Audit base:** `origin/main=1e0977c5c2e2e312fe932502bd81e825d5cfed4c`, state `2026-10-08.audit.166`.
**Frozen source branch:** `research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f` (10 main-only / 24 branch-only commits at refresh).
**Candidate commit:** `099540dc282606f425fb98a8123d8308a5a81677`.
**Source report SHA-256:** `3e56c1a4558b8b23290399097c24ae8de7c69706b15ad7e40c6ec1b7d6e72f67`.
**Exact verifier SHA-256:** `dd8f1366fd02455feb5900bf5ff1663e955bfeb7208d50ceed178b25b906b14d`.

The source report and verifier are unchanged at the refreshed branch tip. The source branch was not modified. The source report was authored against state `.148`; each canonical premise below was checked against `.166`.

## Verdict

- **PASS — promote `C-ALMOST-ACCESSIBLE-STRESS-TRANSVERSAL`** at the finite canonical-source scope in Section 1. It gives a deletion `R=U union Y`, with `U` inside any supplied nonempty loaded set `W` and at most `min(b_0,s_Z)` additional unloaded-core labels, for total size at most `s_Z+1`. The reduced full source is nonempty and has a strict first motion.
- **CONDITIONAL ONLY:** the Type-II grid-access conclusion remains conditional on the separate unreviewed uniform-cell/global-diameter-access candidate. This audit proves no extraction or existence theorem for `W`.
- The separate exceptional-star classification mentioned by the source report is excluded and remains unreviewed. No star hypothesis is needed for the promoted theorem.
- C-II and Level I remain open; the cardinality-restoration and finite-move/payment obligations remain.

## 1. Exact statement and current authority

I checked current `C-EXTREME-TRANSFER`, `C-CONTACT-FACE-REGULARITY`, `C-LOADED-ONLY-STRESS-CYCLE-OBSTRUCTION`, and `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE`, together with Sections 21, 57, and 64 and the current Target C source-scope rule. The input is the contact-minimal, then diameter-pair-minimal triangle-free C-II source with `D>=9`. Let `V` be the nonisolated positive-contact core, `B` the **full actual diameter-endpoint set**, `I=V\\B`, and `P` the normalized nonnegative equilibrium-stress polytope with `dim_aff(P)=s_Z`. Contact-isolated points remain in the full configuration and are not assigned stress-core coordinates. The current full-source route identifies every actual diameter pair as loaded; the proof below counts actual rows, not a selected stressed subgraph.

For any nonempty supplied `W subset B`, set

- `f_b(s)=sum_{h incident to b} beta_h` for `b in W`;
- `g_r(s)=sum_{c incident to r} alpha_c` for `r in I`;
- `b_0=|H[B\\W]|`, the number of actual diameter edges with both endpoints outside `W`.

The promoted conclusion is that there exist `U subset W` and `Y subset I` such that `R=U union Y` satisfies

`|R|<=s_Z+1`, `|Y|<=min{b_0,s_Z}`,

and no normalized source stress has both zero beta mass incident to `U` and zero contact mass incident to `Y`. Consequently, deleting `R` leaves a nonempty full source with no normalized retained-source KKT stress, so the canonical finite strict-motion alternative gives a straight first motion opening all retained actual unit contacts and shortening all retained actual old-`D` pairs. Contact isolates stay in the retained source. This is a reduced-cardinality result only.

## 2. Contact-row independence and the exceptional-face dimension

Let `P_0=P intersect intersection_{b in W}{f_b=0}`. Each `f_b` is nonnegative affine on `P`, so `P_0` is a face, possibly empty. If it is nonempty, every beta coordinate outside `E_0=H[B\\W]` is zero.

The canonical contact-face regularity theorem applies to this same triangle-free C-II core and gives `rank R_C=|C|`. If two equilibrium stresses have the same beta vector, their contact difference lies in `ker(R_C^T)`, hence is zero. Thus projection from the affine equilibrium space to beta coordinates is injective. A normalized beta vector supported on `b_0` edges lies in a simplex of affine dimension `b_0-1`; consequently

`dim_aff(P_0)<=b_0-1`.

Because `W` is nonempty and every endpoint in `B` is incident to a positive row of the canonical relative-interior stress, `P_0` is also a proper face of `P`. Hence, when nonempty, `dim_aff(P_0)<=s_Z-1`. This dimension argument uses all contact rows and all actual diameter rows under the current loaded-source convention; no selected-support graph is substituted.

## 3. Two-stage face cover

I independently checked the finite exposed-face lemma. Let `P` have affine dimension `d`; let `P_0` be a nonempty face of dimension `p` cut out by zero sets of nonnegative affine functions `f_w`; and let nonnegative affine functions `g_y` have no common zero on `P_0`. Choose an inclusion-minimal set `Y_0`, of size `k`, whose zero faces already have empty intersection with `P_0`.

For each `i in Y_0`, minimality supplies `s_i in P_0` with `g_i(s_i)>0` and `g_j(s_i)=0` for every other `j in Y_0`. Evaluating the `g_j` on an affine dependence proves the `s_i` are affinely independent, so `k<=p+1`. Let `F=P intersect intersection_{i in Y_0}{g_i=0}`. If `F` is empty, `Y_0` alone is a cover and `k<=p+1`. If `F` is nonempty, choose `t in F`; the linear parts of the `g_i` evaluate the vectors `s_j-t` as a positive diagonal matrix. They have rank `k` on the affine direction space of `P`, so `dim_aff(F)<=d-k`. Since `F intersect P_0` is empty, Helly on `F` selects at most `d-k+1` of the `f_w` zero faces whose intersection with `F` is empty. Thus the combined cover has at most `d+1` indices, not the sum of two independent `p+1` Helly bounds.

The verifier's simplex and cube-simplex join cases check this finite dimension accounting only; the general lemma is proved analytically above.

## 4. Application to loaded and unloaded reactions

For each `r in I`, `g_r` is nonnegative affine. A stress with `g_r=0` for every `r in I` has no positive contact row incident to any unloaded core vertex and is supported wholly on the loaded set. The canonical Audit.111 loaded-only stress-cycle theorem applies: every such normalized stress, if it exists, has positive diameter support incident to every vertex of `B`. Since `W` is nonempty, no such stress lies in `P_0`. Therefore

`P_0 intersect intersection_{r in I}{g_r=0}=empty`.

If `P_0` is nonempty, apply the two-stage lemma with `d=s_Z`, `p<=min(b_0-1,s_Z-1)`, the family `{f_b:b in W}`, and `{g_r:r in I}`. It selects `Y subset I` and `U subset W` with

`|Y|<=min(b_0,s_Z)`, `|Y|+|U|<=s_Z+1`,

such that no source stress has all `g_r=0` for `r in Y` and all `f_b=0` for `b in U`. If `P_0` is empty, ordinary Helly selects `U subset W`, `|U|<=s_Z+1`; take `Y=empty`.

A normalized stress on the retained source, extended by zero on every row incident to a deleted label, would satisfy those zero-face conditions, a contradiction. Thus the retained source has no normalized stress. The finite KKT/strict-motion theorem applies to its complete retained contact and old-`D` row sets. Contact isolates remain labels, and all their inactive pair constraints persist by the finite source-dependent margins.

## 5. Nonemptiness and boundary cases

If `P_0` is nonempty, a normalized stress has positive beta on some edge of `E_0`; both endpoints lie outside `W`, so they are not deleted by `U subset W`. At least one retained label remains.

If `P_0` is empty and `W` is proper in `B`, a loaded vertex outside `W` remains. If `W=B`, the set `B\\{b}` meets every actual diameter edge for any `b in B`; it therefore already has empty common zero face. Helly can be applied to this proper subfamily, so `U` can be chosen proper and a loaded source point remains. This argument uses that actual diameter edges have distinct endpoints and that every normalized stress has total beta mass one.

The `Y` labels are in `I`, not among contact isolates. The theorem does not move or discard contact isolates during deletion.

## 6. Verifier audit and conditional boundary

Inspected and reran `research/verify_target_c_exceptional_star_face_2026_10_08.py` at the frozen branch tip. It uses exact rational and `Q(sqrt(3))` arithmetic through the checked helper. It verifies seven finite nonglobal planar fixtures, complete actual pair/contact/diameter/triangle censuses, contact-row and mixed-rigidity ranks, equilibrium and PSD stress matrices, explicit smaller same-cardinality grid competitors, and 64 abstract two-stage simplex/join face cases. Those fixtures test edge cases and the finite dimension bookkeeping; they do not establish the analytic theorem, canonical optimality, or a universal grid set. The script also contains finite data for a separate star-face candidate; no claim from that candidate is promoted here.

The grid corollary remains conditional on the unreviewed uniform-cell/global-diameter-access candidate. Even if that premise supplies `W` with `b_0<=eta D`, the result only locates a deletion of at most `s_Z+1` labels, with at most `eta D` unloaded-core exceptions. The paths and grids may overlap, and no deleted-label restoration or same-cardinality strict-`D` competitor follows.

## 7. Canonical disposition

Promote only the finite mixed loaded/unloaded stress-transversal theorem. Keep the grid-access use conditional, and leave the separate star-face sharpening at its frozen research artifact. The current C-II finite-move/payment obligation and Level I remain open.
