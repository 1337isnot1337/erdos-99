> Generated reading edition · [exact source](../../../docs/audits/target_c_c102_bounded_variation_audit_2026-09-05.md) · source SHA-256 `5de852f931d55b4aa8df38670273258ff189f23a3d154cade041495c220aaa9b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A7AEE625D02B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Audit — Target C C102 dominant-separator bounded variation

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_c_dominant_separator_bounded_variation_2026-09-05.md`  
**Verdict:** PASS in the pure simply connected strict-rhombic regime once C100 gives a nested dominant separator family.  
**LEVEL I status:** STILL OPEN.

## 1. Constant signed vector on one prefix interval

For one oriented diameter bar `h=xy`, train coordinates use

`d_(h,tau)=epsilon_tau(y)-epsilon_tau(x) in {-1,0,1}`.

When the dominant separator trains are pairwise noncrossing and ordered, the endpoint side labels define prefix levels. If `x` is oriented from lower to higher prefix level, then for every separator between those levels the side-label change has the same sign. Therefore

`d_(h,tau) r_h`

is one constant vector on one consecutive interval and zero outside it.

PASS.

## 2. Vector form of the two train KKT identities

For a fixed train `tau_j`, define

`F_j=sum_h beta_h d_(h,j) r_h`.

The train-angle KKT equation is

`F_j dot J a_j=0`.

The exact train virtual-work identity gives

`F_j dot a_j=A_j`,

where `A_j=sum_(e in tau_j)alpha_e`. Under C65 every actual contact stress is positive, so `A_j>0`.

In the plane these two scalar identities imply exactly

`F_j=A_j a_j`.

PASS.

## 3. Dominant contribution and lower norm bound

Orient the dominant diameter `za` from `z` to `a`. Every separator is oriented from the `z` side to the `a` side, so its coefficient is `d=+1`. Thus the dominant contribution to every `F_j` is exactly

`bD u`.

The residual vector is

`G_j=F_j-bD u`.

All residual diameter vectors have norm `D` and total beta mass `eta=1-b`, hence

`|G_j|<=D eta`.

Therefore

`|F_j|>=D(b-eta)=D(2b-1)`.

PASS.

## 4. Total variation of the residual sequence

Extend `G_j` by zero before the first and after the last separator. One residual diameter contributes one fixed vector of norm `beta_h D` over one interval. It has exactly one entry jump and one exit jump. Its contribution to total variation is therefore exactly `2 beta_h D` unless its interval is empty, in which case it contributes zero.

Summing by the triangle inequality gives

`TV(G)<=2D sum_(h!=h_0)beta_h=2D eta`.

No cancellation assumption is used.

PASS.

## 5. Normalization estimate

For nonzero vectors `x,y`,

`|x/|x|-y/|y||<=2|x-y|/min(|x|,|y|)`.

Apply this to consecutive `F_j`, including the virtual endpoints `F_0=F_(k+1)=bD u`. Every norm is at least `D(2b-1)`, and `TV(F)=TV(G)`. Therefore

`TV(a)<=4 eta/(2b-1)`.

The angular bound follows from

`2 sin(phi/2)>=2phi/pi` for `0<=phi<=pi`.

PASS.

## 6. Shortest-path inheritance

C99 identifies contact distance with the number of separating trains. Hence a shortest `z`-to-`a` contact path crosses each dominant separator once and no other train. Nested separators must be crossed in stack order. The crossing edge direction from the `z` side to the `a` side is the oriented train vector `a_j`.

Thus the shortest path inherits exactly the same ordered direction sequence and total-turn bound.

PASS.

## 7. Scope

C102 does not imply straightness. A convex polygonal arc may have arbitrarily many vertices while its total turning tends to zero. Therefore the theorem does not by itself recover C97's non-extreme internal chain vertices or terminal twist.

Audited conclusion:

> Once `beta_(za)=b>2/3`, C100 makes the separator family nested and C102 bounds the total chordal variation of its ordered train directions by `4(1-b)/(2b-1)`. In C71-B this tends to zero, and a shortest unit-contact path between the dominant diameter endpoints has the same vanishing total curvature.
