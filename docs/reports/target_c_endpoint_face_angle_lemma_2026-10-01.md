<!-- theorem-state: {"artifact_id":"ART-8D2F7F838617","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — endpoint face-angle lemma and phase-window bound

**Date:** 2026-10-01
**Status:** unreviewed proof-only candidate; C-II remains open.
**Salvage source:** `proof/target-c-inactive-corridor-phase-locking-20261001` at `30b0f56aa8ba9bae8c69d09612d94e5418ced704`.

The finite convex-polygon identity and inequality below are exact. The asymptotic phase-window conclusions additionally rely on the stated Section 84/90 and endpoint-interface hypotheses; those consequences remain unreviewed and do not alter current Target C status.

For every convex unit-edge bounded face C, choose boundary vertices a,b realizing L=diam(C), set u=(b-a)/L, and orient both a-to-b boundary arcs toward b. Each arc telescopes to L u, so

    sum_(e on boundary C) (1-e dot u) = per(C)-2 diam(C).

If M boundary edge occurrences have projective directions in an interval J whose projective distance from [u] is delta, every such occurrence has e dot u <= cos(delta). All summands above are nonnegative, hence

    M(1-cos(delta)) <= per(C)-2 diam(C).                         (1)

This is finite and exact. For a macroscopic bounded inactive face in canonical Section 84, per(C)/D tends to lambda>0 and diam(C)/D tends to lambda/2, so the right side of (1) is o(D). Therefore any fixed positive-density family M>=mu D of terminal edges from one Section-90 phase window forces delta=o(1): the doubled near-geodesic face axis is locked to that phase.

The two fixed Section-90 phase windows are separated by at least pi/3-4K/D. For any axis, one of its distances to the two windows is at least half this separation. Applying (1) gives

    min(M_A,M_B) (1-cos((pi/3-4K/D)/2)) <= per(C)-2 diam(C).

Thus a macroscopic Section-84 face has min(M_A,M_B)=o(D): one macroscopic inactive corridor cannot absorb linear endpoint populations from both inverse-phase shores.

Current main's endpoint interface alternative supplies a linear number of endpoints from one fixed phase shore on bounded nonquadrilateral faces. Since Section 84 allows at most 13 pi/eta faces of perimeter at least eta D, either a fixed positive share lies on macroscopic faces, in which case one such face carries linearly many endpoints and is phase-locked by (1), or for every fixed eta>0 only o(D) of those endpoints lie on faces of perimeter at least eta D. The interface alternative therefore splits into a phase-locked macroscopic corridor or a genuinely diffuse submacroscopic interface.

This is analytic proof work. C-II remains open. No computation, verifier, numerical experiment, or CI result is used.


**Classification:** unreviewed proof-only research. The exact finite inequality is recorded with its proof; its asymptotic application is conditional on its listed hypotheses. No theorem-state or route change is made.
