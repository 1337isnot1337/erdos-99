> Generated reading edition · [exact source](../../../docs/audits/target_c_deep_same_host_attachment_independent_audit_2026-10-08.md) · source SHA-256 `b274deab1b13a34bde99f194f1679816ceabfcfdf8d68bbb4ba09a600b11bcb4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-B6686FDB4EF7","canonical":false,"claim_ids":["C-TYPEII-CAP-DEEP-SAME-HOST-ATTACHMENT"],"claim_statuses":{"C-TYPEII-CAP-DEEP-SAME-HOST-ATTACHMENT":"audited-working"},"index":"docs/state/artifact-index.jsonl","status":"audited-working","target":"target-c"} -->
# Target C Audit.158 — deep same-host attachment from a cap-local grain

**Date:** 2026-10-08

**Audit base:** `origin/main=c18aefc71544251a8b362d7d818cdfad8443a845`, state `2026-10-08.audit.154`.

**Frozen source:** `origin/research/sol-c2-deep-port-route-20261004` at `a2ccd6161519c7d27482a7c6e751cd44e595e1b6`, open PR #668.

**Source report:** `research/target_c_open_cell_host_cap_attachment_depth_2026-10-04.md`, blob `7db94ce2a0ae5e4385c539989b3b35c390c0684e`, SHA-256 `5193d8f6e0bef5d1edf05831b57a62d29c65fc9d96ed2e184e1fdcb9952e4065`.

## Exact conditional statement

Work along a selected canonical post-ZF C-II sequence in the Type-II branch, with actual source diameter `D` tending to infinity and every source point retained. Let `B` be the loaded actual-diameter endpoint set, the vertex set of the convex force hull `F`; then `diam(F)=D`. Suppose:

- `Q_*` is a set of points of `B` contained in a proper consecutive boundary interval `X_*`; its first and last points there are distinct `q_0,q_1`, and the boundary arc `Gamma_*` from `q_0` to `q_1` that follows `X_*` contains all of `Q_*`;
- `C_*=conv(Q_*)` has area at least `alpha D^2` for one fixed `alpha>0`;
- in one unloaded positive-contact component `I_*`, with loaded attachment set `A_* subset B` and harmonic cell `P_*=conv(A_*)`, there is a union `G_*` of strict source-rhombus faces with `G_* subset C_* intersect P_*` and `area(G_*)>=beta D^2` for one fixed `beta>0`.

These premises hold if the audited-working result `C-TYPEII-CAP-LOCAL-HARMONIC-GRID` supplies the grain under its fixed-area cap hypothesis and the additional proper-host-interval premise above also holds. The host-interval extraction from arbitrary canonical sources is not assumed proved.

Let `L` be the chord line through `q_0q_1`; choose signed perpendicular height `eta` positive on `Gamma_*`. Then there is an attachment `a_* in A_* intersect Gamma_*` such that

```text
eta(a_*) >= area(G_*)/D >= beta D.
```

It has an actual unit-contact neighbor `x_* in I_*`, with

```text
|a_*-x_*| = 1,
eta(x_*) >= beta D - 1.
```

The same host arc has linear chord detour:

```text
length(Gamma_*) - |q_0-q_1|
    >= D * (sqrt(1 + 4 beta^2) - 1).
```

## Independent proof

The chord `L` separates the two boundary arcs of the convex polygon `F` into opposite closed half-planes. Since every point of `Q_*` lies on `Gamma_*`, the convex hull `C_*` lies in `{eta>=0}`. Every loaded vertex on the complementary boundary arc has `eta<=0`.

The set `A_*` is finite and consists of loaded vertices. If it had no member in `Gamma_*` with positive height, then all attachments would have `eta<=0`; convexity would put `P_*` in that half-plane. Since `G_*` also lies in `C_* subset {eta>=0}`, it would lie on `L` and have zero area, contradicting `area(G_*)>=beta D^2`. Therefore

```text
H_* := max { eta(a) : a in A_* intersect Gamma_* }
```

is defined and positive. Every member of `A_*` has height at most `H_*`: on `Gamma_*` this is the definition, and on its complement the height is nonpositive. Convexity gives `P_* subset {eta<=H_*}`. Hence `G_* subset P_* intersect {0<=eta<=H_*}`.

Every section of `P_*` by a line parallel to `L` has length at most `D`, because `P_* subset F` and `diam(F)=D`. Integrating these sections over a height interval of length `H_*` gives

```text
area(G_*) <= D H_*,
```

so `H_*>=area(G_*)/D`. Choose `a_*` attaining `H_*`. By definition of the loaded attachment set, `a_*` has a unit-contact neighbor `x_*` in the same component `I_*`. Signed distance to a line is 1-Lipschitz, so `eta(x_*)>=eta(a_*)-1`.

Write `ell=|q_0-q_1|<=D`. Since `a_*` lies on the polygonal arc `Gamma_*` at height `H_*`, the arc length is at least `|q_0-a_*|+|a_*-q_1|`. At fixed height `H_*` above a chord of length `ell`, this sum is minimized when the projection of `a_*` is at the chord midpoint, giving

```text
length(Gamma_*) - ell >= sqrt(ell^2+4H_*^2)-ell.
```

The right side decreases with `ell` and increases with `H_*`. Using `ell<=D` and `H_*>=beta D` gives the claimed lower bound.

## Hostile scope checks

- The source report's assertion that the strong-SCC staircase supplies `Q_*`, its quadratic-area cap, and the designated host interval is not a canonical theorem-state entry. This audit treats the cap and proper interval as explicit hypotheses.
- The proper interval matters: an arbitrary loaded subset need not lie on one proper boundary arc, and if `Q_*=B` there may be no such arc. No same-host conclusion is claimed in that case.
- The argument uses actual loaded vertices and an actual positive contact into `I_*`. It does not drop or relocate any source point; contact isolates remain in the full configuration.
- No bound is obtained on the contact-path length from `x_*` to a rhombus of `G_*` or to the grid. The linear boundary detour is geometric and is not a Section-122 currency payment.
- Composed with the already audited-working `C-TYPEII-NEAR-PORT-GRID-EXTRACTION`, these premises supply its actual deep same-host attachment input and hence a fixed-radius near-port grid. The cap/interval extraction, a route from that port to the grid, currency payment, source-preserving move, strict sub-`D` competitor, and Level I conclusion remain unproved.

## Verifier boundary and disposition

The frozen source report contains no verifier or computation. The proof is an analytic convex-slice and chord-length argument; no finite check is claimed.

**Verdict: PASS WITH NARROWED CONDITIONAL SCOPE.** Record `C-TYPEII-CAP-DEEP-SAME-HOST-ATTACHMENT` as audited-working under the fixed-area cap-local grain and explicit proper-host-interval premises. It supplies an actual same-host loaded attachment and linear chord detour, but no route length or payment. Target C-II and Level I remain open; the canonical finite-move/payment obligation remains.
