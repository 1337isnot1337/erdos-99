> Generated reading edition · [exact source](../../research/target_c_short_unit_wall_zero_capacity_2026-10-05.md) · source SHA-256 `5dcf4747929241143dfa4bd4f20c9b676c00d57da4f51271491688f3c32670fd`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "484b3fd60e55e78d0369e9682f9f68fc70267c41", "source_branch_refs": ["refs/heads/automation/target-c-short-unit-wall-zero-capacity-2026-10-05-v2"], "source_commit": "6756af64ff67d9dfd9cba059b6e27954aca1c8ee", "source_lifecycle": "not indexed", "source_path": "research/target_c_short_unit_wall_zero_capacity_2026-10-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fb6f69bcae048bd23496249ccbfb29146f9e599231dac5b3da20197b667e5b93"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: six-edge winding obstruction to wall-safe refill

Date: 2026-10-05
Base main: 0351e2c529e01750f7aceb87f8f6f0cb9c21dea7
State: 2026-10-05.audit.54
Status: proof-only Target C candidate; C-II and Level I remain open.

Audit.54 makes collective movable-wall activation a live full-core Target C problem. Canonical C-PENTAGON-WALL-DISJOINT-BULK supplies many pairwise source-vertex-disjoint terminal physical pentagon walls. Canonical C-EMBEDDED-WALL-REFILL uses, for a simple actual unit-contact wall C,

    W_C = {x in int(C): |x-b| > 1 for every wall vertex b}.

The direct idea of moving those same pentagon walls along the exact contact manifold until W_C acquires packing capacity is impossible.

## Six-edge winding lemma

Let C=(v_1,...,v_n) be a simple polygonal wall with |v_(i+1)-v_i| <= 1 for every i, cyclically. If n <= 6, then W_C is empty.

Proof. Suppose x is in W_C and put r_i=|v_i-x|>1. Since x is inside the simple polygon, the polygonal loop has winding number +1 or -1 about x. Let theta_i in (-pi,pi) be the principal oriented angle from v_i-x to v_(i+1)-x. Then

    sum_i theta_i = +/- 2 pi.                           (1)

Write a_i=|v_(i+1)-v_i|<=1. By the cosine law,

    a_i^2 = r_i^2+r_(i+1)^2-2 r_i r_(i+1) cos|theta_i|.

Therefore

    cos|theta_i|
      >= (r_i^2+r_(i+1)^2-1)/(2 r_i r_(i+1))
      > 1/2,                                             (2)

because

    r_i^2+r_(i+1)^2-r_i r_(i+1)-1
      = (r_i-r_(i+1))^2+r_i r_(i+1)-1 > 0.

Thus |theta_i| < pi/3 for every edge. Hence, by (1),

    2 pi = |sum_i theta_i|
         <= sum_i |theta_i|
         < n pi/3
         <= 2 pi,

a contradiction.

The threshold is sharp. A regular unit heptagon has circumradius 1/(2 sin(pi/7)) > 1, so its center belongs to W_C.

## Target C consequence

Every terminal physical pentagon in the audit.54 wall-disjoint train family has W_C empty, for every shape. Any finite exact-contact motion that preserves its five boundary contacts and keeps the wall simple still leaves a simple unit pentagon, so W_C remains empty.

Deleting wall vertices later as part of the diameter cover does not evade this obstruction: C-EMBEDDED-WALL-REFILL requires the certified packet to lie in the original W_C.

Therefore the implication

    terminal pentagon bulk
      + exact-contact motion preserving pentagon cycles
      -> positive embedded-wall refill capacity inside those same pentagons

is false.

A continuation through C-EMBEDDED-WALL-REFILL must instead break at least one pentagon boundary contact before certifying the replacement region, enlarge the terminal object to a composite simple unit-contact wall with at least seven boundary edges, or prove a new shield/replacement theorem with a protected region different from W_C. Seven boundary edges are only necessary, not sufficient: C-LARGE-WALL-LOCK-REGRESSION remains binding.

This is a finite analytic proof. No computation, verifier, or CI result is a premise. It remains proof-only and noncanonical and does not close C-II or Level I.
