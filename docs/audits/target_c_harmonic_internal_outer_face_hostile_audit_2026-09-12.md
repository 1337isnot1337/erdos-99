<!-- theorem-state: {"artifact_id":"ART-5FC137F72642","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Target C harmonic internal outer-face lemma

**Date:** 2026-09-12  
**Audited artifact:** `research/target_c_harmonic_internal_outer_face_2026-09-12.md`  
**Disposition:** PASS at the stated proof-only face-localization scope; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This audit checks the geometric lemma that attachment edges of one unloaded harmonic
component remain in the original outer face of its internal graph. It does not
promote the lemma or infer a global source-preserving deformation.

## 1. Convex separation of attachment vertices

Canonical harmonic trapping gives

`I_r subset int(P_r)`, where `P_r=conv(A_r)` and `K_r=conv(I_r)`.

Thus `K_r subset int(P_r)`. Every `a in A_r` is an extreme loaded force-hull
vertex, so `a` is not in `K_r`. This proves the required separation of each added
attachment endpoint from the convex hull of the original unloaded graph.

The argument does not identify contact-isolated source points with `I_r` and does not
require the full source to have an affine stress kernel.

## 2. Attachment edges cannot enter an old bounded face

Let `G_r=C[I_r]`. The full straight-line positive-contact graph is planar, so the
relative interior of an attachment edge `[a,u]` meets neither a vertex nor an edge
of `G_r`; the same holds for a loaded-loaded edge `[a,b]` with both endpoints in
`A_r`.

Near `a`, the edge lies outside `K_r` and hence in the unbounded component of
`R^2\G_r`. If a later interior point lay in an old bounded face, the connected open
segment between the two points would have to cross the boundary of that face. That
boundary is contained in `G_r`, contradicting planarity. The only possible contact
with `G_r` is the intended endpoint `u`, which does not invalidate the relative
interior statement.

The same argument started from either endpoint handles a loaded-loaded edge. It also
allows bridges and disconnected face boundaries because it uses complementary
components, not a Jordan-simple outer cycle.

## 3. Face preservation

All added vertices and edge interiors lie in the closure of the original outer-face
region. Later added edges may subdivide that region, so the correct conclusion is
only that original bounded faces survive unchanged; it is not that the iterated outer
face remains literally unchanged after every insertion.

An original bounded face cannot be split or entered by an added edge. Conversely, a
bounded face created in the outer region has a boundary containing an added loaded
vertex or added edge, and therefore is not an all-unloaded face of `G_r`. Hence the
bounded all-unloaded faces of the induced harmonic graph are exactly the original
bounded faces of `G_r`.

Canonical Section 82 then supplies the strict-rhombus classification for the
degree-four faces, giving the stated correspondence with unloaded-only rhombi.

## 4. Local currency checks

The local Eppstein identity

`k_r+Q_r=2(delta_r+r_r)`

is applied to `G_r` with occurrence-counted outer walk, so holes and bridges are
retained. Every outer edge has unit length, hence `per(K_r)<=k_r`.

Every attachment vertex is within distance one of some vertex of `I_r`; because
`K_r+B(0,1)` is convex and contains all of `A_r`, it contains
`P_r`. Monotonicity of perimeter for nested convex bodies gives

`per(P_r)<=per(K_r+B(0,1))=per(K_r)+2pi<=k_r+2pi`.

No reverse perimeter inequality is used. The local identities are therefore valid
with the stated additive `2pi` boundary loss.

## 5. Scope and classification

The audit passes the HOF face-localization lemma and its local perimeter currency as
proof-only candidate content. It does not establish that local boundary currencies
sum injectively across components, does not remove exceptional-face or outer-walk
detour losses, and does not close either the full-core or macroscopic-container
branch.

**Final audit verdict:** PASS at the stated proof-only scope; C-II remains open.
