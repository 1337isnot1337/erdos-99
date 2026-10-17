> Generated reading edition · [exact source](../../../docs/audits/target_c_primitive_shell_leaf_forcing_promotion_2026-09-12.md) · source SHA-256 `10d9a59af6893150d870e255bfcec2a0c8ace21b3cf4fbd70087e88ce775bb0d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C99212E041F6","canonical":true,"claim_ids":["C-PRIMITIVE-SHELL-LF"],"claim_statuses":{"C-PRIMITIVE-SHELL-LF":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — primitive-shell leaf-forcing promotion audit

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## Scope audited

This audit covers only the exact primitive all-loaded unit-shell normal form

```math
m=0,\qquad d_H+s_Z=2,\qquad C=C_q,
```

with the CG/LF conclusions restricted to `q>=6`. It does not promote the primitive-shell reduction as a general Woodall theorem and does not claim a uniform lower bound on any individual KKT weight.

## Dependency audit

The current Section 72 proof was checked against canonical `audit.24` rather than against the historical CY/CG/LF reports.

1. `C-ZRF` is now correctly scoped to the nonisolated positive-contact core. In the primitive shell that core is exactly the `q`-vertex unit contact cycle, so the mixed rigidity rank is `2q-3` on the precise vertex set used by Section 72.
2. The full mixed support has `q+h=2q-d_H` rows. Therefore the signed equilibrium-dependence space has dimension `3-d_H=s_Z+1`, and diameter-total normalization reduces the normalized KKT stress polytope to affine dimension `s_Z=2-d_H`.
3. Section 72 independently proves that every normalized stress retains every cycle contact and loads every terminal. Thus for `q>=6` every selected diameter support has at least three edges and satisfies the hypotheses used by canonical `C-ZTA`.
4. Canonical `C-ZTA` already includes the SEPq separator/degree contradiction. Hence the additive/zero-transfer phase is impossible for every selected stress in this primitive shell; no unreviewed historical SEPq lemma is needed.
5. Every contact coefficient is positive throughout the compact normalized stress polytope, so proper polytope faces can only arise from diameter coordinates reaching zero.
6. A full-H leaf terminal has only one possible actual diameter edge. Since every selected support edge-covers all terminals, that leaf edge is positive for every normalized stress and cannot define a boundary face.
7. If `s_Z>0`, a full-dimensional `s_Z`-polytope has at least `s_Z+1` facets. Distinct facets require distinct vanishing diameter coordinates, and none can be a full-H leaf edge. This yields at least `s_Z+1=3-d_H` nonleaf–nonleaf full-diameter edges.
8. For `(d_H,s_Z)=(2,0)` the normalized stress polytope is a singleton. The facet argument is unavailable, so no nonleaf-edge lower bound is promoted there. The separate full-support rigidity-circuit conclusion remains valid.
9. The `d_H=1` statement that the nonleaf spine has at least two edges uses canonical `C-WOODALL` and is valid under the same primitive-shell scope.

## Promotable conclusion

The corrected Section 72 theorem is canonical under the scope above:

- `dim S=s_Z=2-d_H`;
- every normalized stress retains the complete positive contact cycle;
- every full-H leaf diameter edge stays positive throughout `S`;
- for `s_Z>0`, at least `s_Z+1=3-d_H` full-diameter edges join two nonleaf vertices;
- for `s_Z=0,d_H=2`, no facet-derived nonleaf-edge lower bound is asserted.

This is structural information for the primitive P1/S1 endpoint. It does not close S1 or C-II.
