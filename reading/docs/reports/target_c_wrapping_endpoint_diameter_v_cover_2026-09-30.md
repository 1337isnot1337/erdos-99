> Generated reading edition · [exact source](../../../docs/reports/target_c_wrapping_endpoint_diameter_v_cover_2026-09-30.md) · source SHA-256 `b83175634e7721feac71fa9068bf0f8b490a2e7c70dfa55c6cbe314b7c1d62f6`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2067CA58B3DB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — wrapping-endpoint antipodal diameter-V cover

Base main: b12708a602af4b17bbb8ecf61e5ed461e4bb2e15. Proof-only; C-II open.

Assume a positive-area center-wrapping carrier satisfies d_w/D -> lambda_1, where
lambda_1 + 4 lambda_1 sqrt(1-lambda_1^2) = pi/2.

Current main gives at this endpoint
    pi D - P_F = o(D),  P_F-q = o(D),  k=o(D),
with k=d_H+s_Z. Therefore
    q=pi D+o(D), d_H=o(D), h=q-d_H=pi D+o(D).

Put a_D=asin(1/(2D)). Order the h projective diameter directions cyclically,
with gaps g_i summing to pi. Let m count consecutive pairs whose diameter edges
are vertex-disjoint. The canonical metric gap bounds are
    g_i >= 2a_D for a shared-endpoint pair,
    g_i >= 4a_D for a disjoint pair.
Hence
    pi >= 2a_D(h+m).
Since 2D a_D -> 1 and h/D -> pi, this forces m=o(D).

The exact angular excess
    E_D = sum_i(g_i-2a_D-2a_D*1_{i disjoint})
        = pi-2a_D(h+m)
satisfies 0 <= E_D <= pi-2a_D h=o(1). Thus for every fixed epsilon>0,
all but o(D) gaps differ from their appropriate lower bound by <epsilon/D.
Together with m=o(D), all but o(D) direction adjacencies are shared-endpoint
pairs vx,vy with g_i=2a_D+o(D^-1), in density sense. Their free endpoints obey
    |x-y|=2D sin(g_i/2)=1+o(1).

Canonical near-disk convergence gives
    B(0,r_D) subset F_D subset B(0,R_D),
    r_D/D,R_D/D -> 1/2.
A hull chord of O(1) length subtends O(D^-1) polar angle. Hull sides on that
short arc have tangent directions in one o(1) cone, since any support normal n
at z obeys n dot z >= r_D and |z| <= R_D, so its radial deviation is at most
acos(r_D/R_D)=o(1). If x,y above were not consecutive hull vertices, their
short boundary chain would contain at least two sides of length >=1. Projection
onto the middle tangent would give |x-y|>=2-o(1), contradiction. Hence every
good free-end pair is a hull side.

The V-to-side map is injective. If the same x,y had two distinct common diameter
partners v,w, then with s=|x-y|<=D the two radius-D circle intersections satisfy
    |v-w|=2 sqrt(D^2-s^2/4) >= sqrt(3)D > D,
contradicting global diameter. Thus h-o(D)=pi D-o(D) distinct hull sides are
generated. Since q=pi D+o(D), all but o(D) hull sides are generated.

For a generated side xy of length s=1+o(1), its common diameter partner has
altitude H=sqrt(D^2-s^2/4) above the support line. Therefore
    H <= w_F(n_xy) <= D
and
    0 <= D-w_F(n_xy) <= D-sqrt(D^2-s^2/4)=O(D^-1).

THEOREM. At the exact rooted wrapping endpoint, after discarding o(D) loaded
hull sides, every remaining side xy has a unique loaded vertex v with
|v-x|=|v-y|=D and |x-y|=1+o(1); at its side normal, the loaded-hull width is
D-O(D^-1).

No computation, verifier, CI result, Euler-trail inference, deletion of isolated
points, or full-source affine-kernel extension is used. A regular odd shell is
a local regression, so this is not yet a contradiction. The next target is to
couple this antipodal V-cover to the current-main harmonic route-geodesicity and
rhombic train structure. The two-half-disk and macroscopic inactive-container
branches are unchanged.
