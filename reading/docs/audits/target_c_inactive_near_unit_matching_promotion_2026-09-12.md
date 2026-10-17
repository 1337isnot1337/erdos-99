> Generated reading edition · [exact source](../../../docs/audits/target_c_inactive_near_unit_matching_promotion_2026-09-12.md) · source SHA-256 `2f31c7d450b22ab97b0e23f7a42e86e11136f618448f8e6f78e9f8adf96be08f`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-24A2E3036987","canonical":true,"claim_ids":["C-INACTIVE-NEAR-MATCHING"],"claim_statuses":{"C-INACTIVE-NEAR-MATCHING":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C near-unit isolate matching promotion audit

**Date:** 2026-09-12

This note records the independent hostile audit of
docs/targets/target-c/81-near-unit-isolate-matching-audit.md.

## Certified chain

1. Let C be a convex chamber of area A and perimeter P containing a specified
   unit-separated isolate set Z of size z. Define
   sigma=A/a_0+P/2+1-z. Finite Oler gives sigma>=0.
2. For the graph joining isolate pairs at distance at most 1+epsilon, take a
   maximum matching of size nu. Its unmatched set has pairwise distances
   strictly greater than 1+epsilon; otherwise the matching was not maximal.
3. Scaling the unmatched set and chamber by 1/(1+epsilon) makes the unmatched
   set unit-separated. Oler gives
   z-2nu <= A/[a_0(1+epsilon)^2]+P/[2(1+epsilon)]+1.
   Substitution of the slack identity yields exactly
   2nu >= (A/a_0)(1-(1+epsilon)^(-2))
   +(P/2)(1-(1+epsilon)^(-1))-sigma.
4. For 0<epsilon<=1, the area factor is at least 3epsilon/4 and the perimeter
   term is nonnegative, so
   nu >= 3A epsilon/(8a_0)-sigma/2.
5. In the canonical macroscopic Section-77 chamber, A>=alpha D^2 and
   sigma<=S D. Taking epsilon=K/D with
   K>4a_0S/(3alpha) gives a positive linear matching lower bound. Every
   matching edge remains strictly longer than one because the selected points
   are contact-isolated in the full source.

## Scope and non-conclusions

The theorem applies only to the actual isolate subset in a convex chamber. It does
not assert a unit contact, simultaneous pair-closing compatibility, a KKT weight,
or a diameter-decreasing motion. It is compatible with strict near-triangular
packings whose gaps are O(1/D).

## Disposition

The finite matching inequality and its inverse-diameter application are valid and
should be promoted as C-INACTIVE-NEAR-MATCHING, depending on
C-INACTIVE-CHAMBER and standard finite Oler scaling. C-II remains open.
