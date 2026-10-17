> Generated reading edition · [exact source](../../../docs/audits/target_c_section146_face_rank_endpoint_stability_2026-09-12.md) · source SHA-256 `aa0f4bd226a38f0656c1603edacf4825bf0c2b41bbb9ef7ca7511f4fcf53fa75`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-2B9D5006AA72","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Section-146 face-rank endpoint stability

**Date:** 2026-09-12
**Reviewed:** docs/reports/target_c_section146_face_rank_endpoint_stability_2026-09-12.md
**Disposition:** PASS at proof-only/audited-working Type-II scope.
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

Checks:

1. Substituting $`t=y-s_Z/D`$ into §146.5 gives
   $`t-(d_H+s_Z)/(9D)\ge C_{146}`$, so $`t\le C_{146}+\eta`$ implies
   $`(d_H+s_Z)/D\le9\eta+o(1)`$.
2. The §146 face lower bound and $`Q\ge f`$ give
   $`Q-f\le(9/4)\eta D+o(D)`$. Since $`Q-f`$ is the sum of degree excess beyond
   five, the pentagon count has the stated linear lower bound.
3. The exact outer ledger $`b=2h-Q-2s_Z`$, together with the face lower bound and
   $`\operatorname{per}(F)/D\to\pi`$, gives
   $`b-\operatorname{per}(F)\le(9/4)\eta D+o(D)`$.
4. The proof-only identity
   $`2f-\operatorname{rank}C_{\rm face}=\sigma_C`$, with
   $`0\le\sigma_C\le s_Z`$, gives the stated rank lower bound. It is used only on
   the positive-contact core and does not extend the affine kernel to isolates.
5. The conclusion is conditional and structural. It does not assert that the
   high-rank pentagon network is impossible and does not promote theorem state.

The linear outer-detour and inactive-container branches remain unresolved.
