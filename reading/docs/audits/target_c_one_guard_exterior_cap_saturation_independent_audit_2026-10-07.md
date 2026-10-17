> Generated reading edition · [exact source](../../../docs/audits/target_c_one_guard_exterior_cap_saturation_independent_audit_2026-10-07.md) · source SHA-256 `0f9b223d2589ac1ec07111bc930981f88f6f1d7f6d157491e7d7df4725554466`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E06BC5F2CBCF","canonical":true,"claim_ids":["C-ONE-GUARD-EXTERIOR-CAP-SATURATION"],"claim_statuses":{"C-ONE-GUARD-EXTERIOR-CAP-SATURATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.113 — one-guard exterior-cap saturation

**Date:** 2026-10-07
**Audit base:** `3c1828f204a1a35cb7aff5347f3d2b40f20fe897`, tree `01bfec59632f00c3f7b1a6b4dd3b533257a5135a`
**Starting state:** `2026-10-07.audit.112`; C-I closed, C-II open, Level I open
**Source branch:** `research/sol/target-c-exterior-cap-closure-20261006`
**Frozen source commit:** `f4a362727779f6afc0f01738015112c04fdb73d5`
**Source artifact:** `docs/reports/target_c_exterior_packet_release_and_unloaded_core_cut_2026-10-06.md`, SHA-256 `6b8722e95d92cfc1c32f7bcc6d4ba5cd71f6138df657d73ce5be982d8299fa08`
**Verdict:** E.2 PASS — subsumed by Audit.112; E.3 PASS WITH NARROWED SCOPE — promote `C-ONE-GUARD-EXTERIOR-CAP-SATURATION`.
**Classification:** independently audited theorem; no computational certificate is claimed. The report's Section 3 antipodal-cap pairing argument is not audited here.

## Exact statement promoted

Let `A` be a triangle-free, unit-separated `n`-point global minimizer of diameter `D=D(n)>1`, chosen with the fewest unit contacts among triangle-free global minimizers of cardinality `n`. Let `B` be the set of actual diameter endpoints, `K=conv(A)`, and `F=conv(B)`. Let `V` be the set of source labels incident to at least one unit contact. Assume `F` has positive area and `V` is contained in `F`.

Choose a side `ab` of `F` and its outward unit normal `u`, with `u dot x <= c` for every `x in F`. The corresponding actual loaded-hull cap is the part of `K` on the outer side of this line. Let `Z` be the complete source population of that cap, equivalently all source labels `z` with `u dot z > c`. For any contact-active source label `v` in `V`, put `T=A` with `Z` and `v` deleted and define

`E = int(K) intersect {x : u dot x > c} intersect {x : |x-t| >= 1 for every t in T}`.

Let `Pack_1(E)` be the largest cardinality of a finite subset of `E` whose pairwise distances are at least one. Then

`Pack_1(E) = |Z|`.

The source-hull cap decomposition in `C-LOADED-HULL-CAP-BUDGET` makes `Z` the full exterior source population beyond the selected loaded side. The claim assumes that geometric setup and `V subset F`; it does not cover an arbitrary line that merely separates a proposed packet from selected retained labels.

## Independent proof

### Upper bound

Suppose `E` contains `|Z|+1` unit-separated sites, and choose a subset `Y` of exactly that size. Every site in `Y` is unit-clear from `T` by the definition of `E`. Since each site lies in `int(K)`, every distance from a site in `Y` to any point of `K` is strictly below `D`: equality would let the interior site move slightly farther from the other point while remaining in `K`, contradicting `diam(K)=D`. This also gives strict upper slack for pairs inside `Y`.

Every retained source label lies in the closed half-plane `u dot x <= c`; each point of `Y` lies in the strict opposite half-plane. Apply the canonical `C-SEPARATED-PACKET-RELEASE-OBSTRUCTION` with one packet, deletion set `Z union {v}`, and retained set `T`. It opens any exact new contacts among `Y` and between `Y` and `T` by a finite motion. The deleted label `v` was contact-active, and no label in `Z` has a contact because `V subset F`. Thus the deletion removes an old contact. The resulting source cannot have diameter below `D` by global optimality, or diameter `D` by contact-minimality. This contradiction proves `Pack_1(E) <= |Z|`.

### Lower bound

Every point in `Z` lies strictly beyond the cap's closing line and outside `F`. Because every contact-active label lies in `F`, points of `Z` are contact-isolated. Because every actual diameter endpoint lies in `B subset F`, no point of `Z` is an actual diameter endpoint. Therefore every source pair involving a label in `Z` has strict lower slack above one and strict upper slack below `D`.

Choose one point `w` in `int(K)`. Move each `z in Z` to `(1-epsilon)z + epsilon*w` for one sufficiently small positive `epsilon`. Each moved point lies in `int(K)` and remains strictly beyond the cap line. Finiteness of `A` and the strict pair margins ensure all moved points stay mutually unit-separated and at distance at least one from `T`. They provide `|Z|` sites in `E`, so `Pack_1(E) >= |Z|`. If `Z` is empty, this lower bound is immediate.

Combining the bounds proves equality. The proof does not need the secondary diameter-pair minimum, a stress polytope, or near-disk asymptotics.

## E.2 and scope dispositions

The finite one-cap clause of E.2 is an immediate instance of Audit.112: the cap line separates every retained source label from the packet, and the theorem explicitly allows exact packet-to-retained or packet-internal contacts when the stated involving upper margins are strict. For finitely many cap packets, the same result follows only when their cross-packet distances are strictly greater than one. No separate theorem ID is needed.

The claim that the two macroscopic caps in Section 3 exist and are separated by `Omega(D)` is not used or promoted. The geometric pairing argument in Section 3 remains unreviewed.

The E.3 source statement did not itself spell out the full source/cap normalization. The promoted version makes explicit the actual diameter endpoint set, positive-area loaded hull, complete cap population, positive-contact-core inclusion, and contact-minimal source selection. It requires sites in the open interior of the full source hull and only permits one omitted contact-active guard. It does not assert capacity for boundary sites, for arbitrary exterior regions, or after deleting multiple guards.

This is not a duplicate of canonical `C-EXTERIOR-CAP-STRICT-PACKET-CAPACITY`: that theorem concerns a hull-augmented contact-face cell with strict clearance from its wall path. Here the region lies in an actual loaded-hull exterior cap, is weakly clear of all retained source points, and omits one contact-active guard from the clearance set. Nor does the result follow from `C-EXTERIOR-STATIC-PACKET-BARRIER` alone at this scope: the present statement assumes the finite core-in-cap-hull condition `V subset F` and uses no strong-support normalization `C=C_*`, `H=H_*`; it also proves the matching lower bound by moving all cap isolates inward.

## Dependencies and frontier effect

The cap decomposition and `V subset F` input are canonical `C-LOADED-HULL-CAP-BUDGET`. The upper bound uses canonical `C-SEPARATED-PACKET-RELEASE-OBSTRUCTION`; the lower bound is the finite motion above. Contact-isolated labels outside the cap are all retained in `T` and remain in every pairwise clearance check.

This gives exact one-guard saturation of an actual exterior cap: removing one active contact label creates no additional weakly unit-clear interior site beyond the cap's existing isolate population. It does not supply a packet with surplus, settle the multi-cap pairing claim, or close the full-source finite-competitor obligation. C-II and Level I remain open.
