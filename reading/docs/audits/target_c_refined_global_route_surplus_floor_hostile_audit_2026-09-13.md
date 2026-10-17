> Generated reading edition · [exact source](../../../docs/audits/target_c_refined_global_route_surplus_floor_hostile_audit_2026-09-13.md) · source SHA-256 `f36744eb79d2243fc19692e64a1cb3ef988e330b3f098cfa32485770d9bb43b1`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CCBA2FA4207F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C refined global route-surplus floor

**Date:** 2026-09-13  
**Reviewed:** `research/target_c_refined_global_route_surplus_floor_2026-09-13.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS at proof-only scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Dependence on the repaired atom bound

The only non-elementary input is the audited-working Section-155 `N=2` inequality,
which is usable only with the repaired finite-to-limit phase-atomization lemma and
the fixed-epsilon Section-142 saturation input. The audit does not promote either
input or extend it to Type I.

## 2. Quadratic certificate

With

```math
U_2(\lambda)=((\pi+\lambda)^2+1225\lambda^2)/2,
```

the coefficient of

```math
H(\lambda)=(4\sqrt{\Delta_2}+\lambda-153/1250)^2-U_2(\lambda)
```

is `-612`. A concave function on a compact interval has its minimum at an endpoint.
Using `4 sqrt(Delta_2)>3.8092` and `pi<3.14160`, the endpoint lower margins are
greater than `8.65` and `0.006`, respectively. The right side being squared is
positive, so the square comparison has the correct direction. This proves the
short-detour inequality (RG.4).

## 3. Liminf split

If the normalized outer detour is at least `153/1250`, the route surplus is already at
least `153/1250`. If a subsequence has smaller detour, pass to a convergent subsubsequence
and apply Section 155 with `N=2`; (RG.4) gives the same lower bound after adding the
detour. No uniform convergence in the detour parameter is assumed beyond the
subsequence limit supplied by the Section-155 statement.

## 4. Limits

The result is a modest improvement of an existing explicit floor. It does not control
the positive-detour branch, does not identify local harmonic-cell detours, and does
not produce a strict diameter descent or a unit triangle. Contact-isolated source
points remain outside the positive-core train measures and are not deleted.

**Final verdict:** PASS at proof-only scope; C-II remains open.
