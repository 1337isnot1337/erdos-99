> Generated reading edition · [exact source](../../../docs/audits/target_c_exterior_cap_hull_and_cover_independent_audit_2026-09-14.md) · source SHA-256 `424bf60a24a415a0120bc718cff28f37e5e9d292742ec6865c8cb4807df70b9a`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E4E28D4D9D44","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — exterior-cap hull stability and erosion covering

**Date:** 2026-09-14
**Artifact audited:** `docs/reports/target_c_exterior_cap_hull_and_cover_2026-09-14.md`
**Target:** C-II / macroscopic-container branch
**Verdict:** audited-working finite lemmas; no Level I closure

## 1. EC.1 hull stability

The proof is valid. For a convex body with inball radius `r`, inner-parallel
coarea and perimeter monotonicity give `area(C)<=r per(C)`, hence
`r>=alpha D/P_0`. Oler applied to the actual isolated source set `S` in its hull
`H` gives `area(C)-area(H)<=O(D)`, using `per(H)<=per(C)`.

For a support deficit `t=h_C(u)-h_H(u)`, the triangle with apex at a support point
of `C` and base the two inball endpoints perpendicular to `u` lies in `C`. Its cap
of depth `s<=min(t,r)` has area at least `r s^2/D`, since the triangle altitude is
at most `D`. If `t>r`, this is at least `kappa^3D^2`, contradicting the `O(D)`
area deficit for large `D`; otherwise `t^2<=O(D)`. Taking all support directions
gives the claimed `O(sqrt(D))` Hausdorff error and inner-disk inclusion.

No limiting argument, equality assumption, or isolate deletion is used.

## 2. EC.2 contact-minimal covering

Let `x` be in the one-unit erosion of a convex cap `C` and farther than one from
all isolate points in `int(C)`. Every source point outside `int(C)` is reached from
`x` only after crossing `partial C`, so its distance from `x` is at least
`dist(x,partial C)>1`. Thus `x` is strictly farther than one from every source.

Replacing any nonisolated source vertex by `x` preserves cardinality, all separation
constraints, and diameter at most `D(n)`. Minimality of `D(n)` makes the new diameter
equal to `D(n)`, while the new point has no unit contact and the old nonisolated
vertex had at least one. This contradicts the contact-minimal representative. The
argument does not require the replacement to preserve a KKT stress or diameter pair.

The application to an actual exterior cap is valid because all nonisolated core
vertices lie in the force hull and hence outside the cap interior; source points on
the closing chord are handled as boundary points.

## 3. Regression audit

The strained triangular patch with spacing `1+1/m` is an exact fixed-container
regression. Its cells have circumradius `<1`, so closed unit disks cover the cap
even though no strict insertion exists. Its Oler slack is linear in its diameter.
Therefore EC.1 plus EC.2 cannot be promoted to a protected strict exchange without
an additional coupling to the diameter-carrying core.

## 4. Remaining gap

The audited results establish only

```text
quadratic exterior cap + linear perimeter/slack
    -> source hull fills cap to O(sqrt(D)) and erosion is covered
```

They do not provide a source-preserving strict sub-diameter deformation, an exact
unit equilateral triangle, or a global replacement theorem. The macroscopic-cap
branch remains open.
