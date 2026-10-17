> Generated reading edition · [exact source](../../../docs/audits/target_c_rigid_face_isolate_transport_independent_audit_2026-10-09.md) · source SHA-256 `46f52688a330d693376ce9bea6fe5f9987f08396654851e62ffde157e5e85e74`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B7D7C740170E","canonical":true,"claim_ids":["C-INTEGRATED-FOLD-RIGID-FACE-ISOLATE-TRANSPORT"],"claim_statuses":{"C-INTEGRATED-FOLD-RIGID-FACE-ISOLATE-TRANSPORT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: transport of isolates in rigid faces

**Date:** 2026-10-09. **Audit:** 227.
**Audit base:** `origin/main=66377af17f06a04ed8ce503de81301a6618f6eca`, state `2026-10-09.audit.220`.
**Frozen source:** `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`.
**Source report:** `docs/reports/target_c_small_convex_contact_face_quarter_fold_exclusion_2026-10-09.md`, SHA-256 `ec4bb6ac4e7c6096d7921074d1326c6ec55494d422d67cbff976637c55802f23`, Section 7.2.

## Verdict

**PASS — promote `C-INTEGRATED-FOLD-RIGID-FACE-ISOLATE-TRANSPORT` with the exact embedding and residual-ledger hypotheses below.** The source's conclusion is valid, but its cited convex-wall shield is unnecessary and would not cover arbitrary nonconvex faces. A direct crossing estimate proves the needed lower separation for any simple polygonal face. The convex-coefficient identity gives a strict upper-pair margin.

## Exact conditional statement

Let a finite unit-separated source have a finite plane contact core. Let `F` be any of its bounded faces with a simple polygonal boundary cycle of actual unit contacts; convexity is not required. Consider a finite integrated quarter-fold endpoint of the core with diameter budget `D`. Assume:

1. every old core contact remains at distance one, every old core noncontact remains strictly farther than one, and every core pair is at distance at most `D`;
2. the old bounded face cycles remain the corresponding actual bounded faces in the new plane embedding;
3. every retained source label outside the interiors of constant-sign bounded faces already satisfies the complete lower and upper pair ledger with the core and with every other such retained label.

For every bounded face on whose boundary all integrated fold signs equal one constant sign, its boundary is carried by one rigid quarter-turn and translation. Move each old contact-isolated source label in that face by this same isometry. Then all pairs involving these transported labels satisfy the full lower ledger, and all upper pairs are strict below `D`. In particular:

- distances within one face are unchanged;
- a transported isolate and any core vertex outside its face are separated by more than `sqrt(3)`;
- isolates transported from distinct bounded faces are separated by more than `sqrt(3)`;
- for any transported isolate `x` and any other endpoint label `z` whose distances to all core vertices are at most `D`, `|x-z|^2 < D^2-1`.

Thus inserting these transported labels completes the full endpoint pair ledger whenever the remaining labels passed the assumed residual ledger. The claim does not establish that the core endpoint or embedding exists.

## Independent proof

### Constant-sign faces move rigidly

For a cyclic boundary edge vector `q_i`, the integrated quarter-fold increments are `U_{i+1}-U_i=s_iJq_i`, where `s_i` is its sign. If `s_i=s` on the whole face boundary, then every increment is the same orthogonal image `sJq_i`. Summing around the cycle shows that all boundary labels undergo one common rotation by `sJ` and one translation. The face-embedding assumption means the bounded region is carried by the same isometry, so transporting its old interior labels preserves its strict clearance from every face-boundary vertex and preserves all distances between labels in that same face.

### Lower-pair crossing estimate

For a unit boundary edge `cd` and a point `w=(1-t)c+td`, `0<=t<=1`, the weighted-square identity gives

```math
|x-w|^2=(1-t)|x-c|^2+t|x-d|^2-t(1-t)|c-d|^2.
```

If an old contact-isolated point `x` has strict clearance `|x-c|,|x-d|>1`, then `|x-w|^2>1-1/4=3/4`. If an endpoint point `z` is lower-feasible from every core vertex, so `|z-c|,|z-d|>=1`, the same identity gives `|z-w|^2>=3/4`.

Take any core vertex or residual isolate `z` outside the face of `x`. The segment `[x,z]` exits that simple bounded face at some point `w` on a unit boundary edge. Since `w` lies between `x` and `z`,

```math
|x-z|=|x-w|+|w-z|>\sqrt3/2+\sqrt3/2=\sqrt3.
```

If the crossing is at a boundary vertex, the corresponding endpoint distance is at least one and the same strict conclusion holds. This proof works for nonconvex simple faces and does not use `C-ONE-VERTEX-CONVEX-WALL-SHIELD`, whose wall hypothesis is convexity. For isolates in two distinct bounded faces, choose the first exit point from the first face and the last entry point into the second along their connecting segment; both endpoint pieces are strictly longer than `sqrt(3)/2`, so their distance also exceeds `sqrt3`.

### Upper-pair margin

Every point in a bounded polygonal face lies in the convex hull of its boundary vertices, whether or not the face is convex. Write the transported isolate as `x=sum_i lambda_i v_i`, with `lambda_i>=0`, `sum_i lambda_i=1`, and `v_i` the face's core boundary vertices. For any endpoint point `z`,

```math
|x-z|^2=\sum_i\lambda_i|v_i-z|^2-\sum_i\lambda_i|v_i-x|^2.
```

The residual/core upper ledger gives `|v_i-z|<=D` when `z` is core or an outer residual isolate. If `z` is an isolate in another bounded face, express `z` as a convex combination of that face's core boundary vertices; the core upper ledger and the triangle inequality again give `|v_i-z|<=D`. The variance term is strictly greater than one because `x` remains strictly farther than one from every boundary vertex. Therefore `|x-z|^2<D^2-1`. For two isolates in the same rigid face, distances are preserved; applying the same identity also shows their upper pair is strictly below this bound.

## Hostile checks and limits

- **Nonconvex bounded faces:** the source's appeal to a convex-wall theorem is not valid for arbitrary faces. The boundary-crossing estimate repairs this without requiring convexity.
- **Equality at one endpoint:** the residual point may be exactly one from both ends of a crossed edge, giving distance `sqrt(3)/2` to the crossing point. The transported isolate's distance is strictly larger, so the sum remains strictly greater than `sqrt(3)`.
- **Face embedding:** lower/upper pair feasibility of the moved core alone does not prove that old bounded faces persist. This remains an explicit, unproved hypothesis.
- **Contact isolates:** every old label in a face is transported; none is discarded. The result gives no placement for labels in nonconstant faces and no way to satisfy the embedding or residual-ledger assumptions.
- **Global scope:** this is a conditional endpoint-extension lemma, not a canonical source move, strict diameter improvement, C-II closure, or Level-I result.

No finite verifier encodes the geometric crossing or variance identities. Their steps are exact for finite polygonal faces and use no approximation or asymptotic claim.
