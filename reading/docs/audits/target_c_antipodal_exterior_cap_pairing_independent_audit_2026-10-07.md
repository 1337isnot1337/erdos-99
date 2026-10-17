> Generated reading edition · [exact source](../../../docs/audits/target_c_antipodal_exterior_cap_pairing_independent_audit_2026-10-07.md) · source SHA-256 `aeffa6539fd521838695aa74330825cc1aef083856ddfd7fb4466f7244be79c5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2146051EED8C","canonical":true,"claim_ids":["C-ANTIPODAL-EXTERIOR-CAP-PAIRING"],"claim_statuses":{"C-ANTIPODAL-EXTERIOR-CAP-PAIRING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.115 — antipodal pairing of macroscopic exterior caps

**Date:** 2026-10-07
**Audit base:** `3df3de8cf50eef29bbcfbf1f8434e40fc478bba3`, tree `2cbd777b07594bb523f1ee3d57d8892a5e00abc5`
**Starting state:** `2026-10-07.audit.114`; C-I closed, C-II open, Level I open
**Source branch:** `research/sol/target-c-exterior-cap-closure-20261006`
**Frozen source commit:** `f4a362727779f6afc0f01738015112c04fdb73d5`
**Source artifact:** `docs/reports/target_c_antipodal_exterior_cap_pairing_2026-09-25.md`, SHA-256 `40d03e694318f912ee032917b83f7df35c8f2c8d7b4d55b46d81e8050c2afee0`
**Audit boundary:** Theorem 1 and Corollaries 1 and 3 of the source report. Corollary 2's cap ceiling is already a consequence of `C-DB-DENSITY`; the attempted paired-cap release is not audited as a theorem.
**Verdict:** PASS — promote `C-ANTIPODAL-EXTERIOR-CAP-PAIRING` with the sequence scope below.

## Exact statement promoted

Let `A_j` be any unbounded sequence of canonical contact-minimal, then diameter-pair-minimal, triangle-free global minimizers in the C-II normalization. Retain the full source, let `D_j=diam(A_j) -> infinity`, let `K_j=conv(A_j)`, and let `F_j` be the convex hull of the endpoints of the full actual diameter graph. Let `o_j` be the source circumcenter. For any sequence of Section-77 exterior caps `C_j` with

`liminf area(C_j)/D_j^2 > 0`,

there are distinct exterior caps `C'_j` of the same sources, for all sufficiently large `j`, such that

- `area(C'_j)-area(C_j)=o(D_j^2)`;
- if `z_j,z'_j` count the actual assigned contact-isolated source points, then `z'_j-z_j=o(D_j^2)`;
- along every convergent subsequence of normalized caps, `C'_j-o_j` has the half-turn image of the limit of `C_j-o_j` as its limit; and
- for `I_j=conv(Z_j)` and `I'_j=conv(Z'_j)`, the actual isolate hulls satisfy `d_H(I_j,C_j)=O(sqrt(D_j))`, `d_H(I'_j,C'_j)=O(sqrt(D_j))`, and `d_H(I'_j-o_j,-(I_j-o_j))/D_j -> 0`.

Consequently `z_j <= Z_ext,j/2 + o(D_j^2)`: one exterior cap cannot carry more than half of the total exterior source population to leading order. More quantitatively, for each fixed `epsilon>0`, at most `pi/(4 epsilon)` caps have area at least `epsilon D_j^2`, while the total isolate population assigned to smaller caps is at most

`(sqrt(pi epsilon)/a_0) D_j^2 + O(D_j)`, where `a_0=sqrt(3)/2`.

Thus, after choosing `epsilon` small, all but `O(sqrt(epsilon) D_j^2)+O(D_j)` exterior isolates lie in a bounded number (depending on `epsilon`) of macroscopic caps, and those caps occur in distinct antipodal pairs with equal leading populations. The result is asymptotic: it gives no exact finite symmetry, packet capacity, source-preserving release, triangle, or strict sub-`D` competitor.

## Independent reconstruction

The canonical inputs match the report's objects. Section 77.1 proves every endpoint of an actual diameter pair is an extreme point of the full source hull. On the canonical C-II source, the relative-interior stress has the full actual diameter graph as support, so `F_j` is the full actual force hull used by Sections 59, 77, and 80. Its vertices are exactly the actual diameter endpoints; no selected proper subgraph or scaffold is substituted.

First, `C-FS-GEOM` gives circumradius `R_j=D_j/2+O(sqrt(D_j))` and `R_j-r_j=O(sqrt(D_j))`. If `c_j` is an incenter, `|c_j-o_j|<=R_j-r_j`; hence

`B(o_j,D_j/2-O(sqrt(D_j))) subset K_j subset B(o_j,D_j/2+O(sqrt(D_j)))`.

The normalized source hull therefore converges to the centered radius-`1/2` disk. Every loaded vertex `b` lies in the outer annulus: its actual diameter partner `k` also lies in the circumdisk, so `D_j<=|b-o_j|+|k-o_j|` gives `|b-o_j|>=D_j/2-O(sqrt(D_j))`. The full-source half-turn estimate `C-FS-GEOM`, specifically FS.6, places `k` within `O(D_j^(3/4))=o(D_j)` of `2o_j-b`. Since `k` is itself a full-graph endpoint and thus a loaded vertex, every normalized loaded-vertex set is asymptotically invariant under the half-turn.

Second, `C-DB-DENSITY` places a disk of radius `(sin(rho)/2-o(1))D_j` about `o_j` inside `F_j`, where `rho=cos(rho)>0`. Thus `o_j` is interior to `F_j`, and every consecutive loaded-vertex chord has its outward cap arc of angular width less than `pi`. Pass to a subsequence where the two endpoints of `C_j`, normalized about `o_j`, converge to `u,v` on the radius-`1/2` circle. The open arc between them contains no point of the loaded-vertex limit set `S`; the half-turn invariance gives the corresponding empty opposite arc from `-u` to `-v`. Positive normalized cap area forces the original arc to have positive limiting width. Choosing a point strictly inside the opposite empty arc and taking the consecutive loaded vertices around it produces, for all large `j`, a distinct exterior cap `C'_j` whose normalized chord endpoints converge to `-u,-v`.

Third, the source-hull disk sandwich implies the two caps converge to opposite circular segments of equal area. Hence their area difference is `o(D_j^2)`. Section 80, equations (80.13)--(80.14), gives for each cap

`z_i=area(C_i)/a_0 + per(C_i)/2 - 1 - sigma_i`,

with `sigma_i>=0`, total `sum_i sigma_i=O(D_j)`, and total cap perimeter at most `2 pi D_j`. Thus every cap has `z_i=area(C_i)/a_0+O(D_j)`, uniformly over the cap choice. This proves equal leading populations, the half-population consequence, and the cap count from disjoint area.

For the actual isolate hull estimate, apply Oler to the unit-separated isolate set in `I_i=conv(Z_i)`. Because `per(I_i)<=per(C_i)=O(D_j)` and the cap count identity gives `a_0 z_i=area(C_i)+O(D_j)`, Oler yields `area(C_i)-area(I_i)=O(D_j)`. A macroscopic cap has inradius `r_i=Omega(D_j)`, since `area(C_i)<=r_i per(C_i)`. For any unit direction, if the support gap `t=h_{C_i}-h_{I_i}` exceeded `r_i`, the top triangle cut from an inball-to-support-point triangle would lie outside `I_i` and have area at least `r_i^3/D_j=Omega(D_j^2)`, contradicting the `O(D_j)` area deficit. For `t<=r_i`, the same triangle has outside area at least `r_i t^2/D_j`; the deficit therefore forces `t=O(sqrt(D_j))` uniformly in direction. This is precisely `d_H(I_i,C_i)=O(sqrt(D_j))` for nested convex bodies. Applying it to both caps and using their normalized half-turn convergence proves the isolate-hull conclusion.

Finally, the small-cap mass estimate follows directly from isoperimetry and the total perimeter bound: `sum_i sqrt(area(C_i))<=sqrt(pi)D_j`; multiplying by the largest square root among caps below `epsilon D_j^2` bounds their total area by `sqrt(pi epsilon)D_j^2`. Summing the cap Oler upper bounds adds only `O(D_j)` perimeter cost. This is an order-of-limits statement: the number of large caps depends on the chosen `epsilon`.

## Hostile scope checks

- The paired source is the same canonical global minimizer sequence, with every contact-isolated source point retained and assigned to an actual exterior cap.
- `C-DB-DENSITY` supplies an inball for the full actual force hull, not a scaffold or a chosen subset of diameter edges.
- Audit.94's exact six-spoke paired-cap family is nonglobal and fails canonical mixed-rigidity and loaded-diameter-density hypotheses. It does not contradict this extraction theorem; it does refute inference from paired caps, quadratic isolates, and boundary-order Oler slack alone to globality or a strict competitor.
- The attempted replacement leaving the loaded core fixed is invalid as a closure: it retains an actual diameter pair of length `D`. No finite motion, new contact, triangle, or diameter decrease follows from this audit.
- The result does not prove the Audit.85 four-tip separation hypothesis, a strict-safe slot, or any packet capacity.

## Dependencies and frontier disposition

Dependencies are canonical `C-FS-GEOM`, `C-DB-DENSITY`, `C-INACTIVE-CHAMBER`, and `C-FULLCORE-NEAR-DISK`. The theorem sharpens the exterior macroscopic-container branch: a quadratic exterior cap has an opposite cap with equal leading area and isolate population, and the actual isolate hulls share opposite normalized limits. The remaining exterior branch needs a paired-cap core release yielding an exact unit triangle or a same-cardinality strict sub-`D` source. Internal inactive chambers and the active full-core face-coupled endpoint remain separate. C-II and Level I remain open; the active prompt's immediate face-coupled full-core obligation is unchanged.
