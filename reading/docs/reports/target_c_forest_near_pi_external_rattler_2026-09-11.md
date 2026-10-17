> Generated reading edition · [exact source](../../../docs/reports/target_c_forest_near_pi_external_rattler_2026-09-11.md) · source SHA-256 `0919ba63fd0459eb4eb48b30e0e81d082989e57dfeef51e2e97c19c72534b4c2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4C27D79C5129","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_forest_near_pi_external_rattler_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=b99332cc9b900540def3be1913b800fe05a46380; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C: forest near-pi endpoint gives subquadratic external source population

Date: 2026-09-11
Status: new proved lemma, HOLD and unpromoted
Scope: the post-ZF forest diameter branch with `s_Z=0` and `q/D -> pi`.

## Exact use

This result is intended to remove the external-source population from the first-order
forest endpoint. It does not close C-II. The remaining contradiction would need a
sharper rate, or an independent upper bound on the forest surplus.

Let `A_j` be the full source configuration, `D_j` its minimum diameter, `F_j` the
force hull, `K_j=conv(A_j)`, and `q_j` the number of loaded vertices of the actual
diameter graph. Let `N_{F,j}=|A_j cap F_j|`. The source points outside `F_j` include
all contact-isolated source points; none are discarded.

## Proposition

Assume the established post-ZF estimates for this branch:

1. the loaded vertices are boundary vertices of `F_j` and are pairwise at distance
   at least one;
2. `diam(F_j), diam(K_j) <= D_j`;
3. the full-source external-annulus estimate

   `pi/4 * |A_j minus F_j| <= area(K_j)-area(F_j)`
   `+ (per(K_j)+per(F_j))/2 + pi/4`;

4. the full-source rhombic transport estimate, with fixed `a_0>0`, `c_0`, and
   nonnegative angular excess `E_j`,

   `a_0 N_{F,j} <= area(F_j)+c_0 per(F_j)+a_0-E_j`;

5. the standard minimum-diameter asymptotic
   `n_j/D_j^2 -> pi/(2 sqrt(3))`.

If `q_j/D_j -> pi`, then

`|A_j minus F_j| = o(D_j^2)`,
`area(K_j minus F_j) = o(D_j^2)`,
`area(F_j)/D_j^2 -> pi/4`,
`E_j/D_j^2 -> 0`, and every normalized Hausdorff limit of `F_j` and `K_j` is the
unit disk.

## Proof

Since the loaded vertices occur on the boundary in cyclic order, their consecutive
boundary chords have length at least one. Hence

`q_j <= per(F_j) <= pi D_j`.

The second inequality is the perimeter-diameter inequality for a planar convex body.
The hypothesis `q_j/D_j -> pi` therefore gives `per(F_j)/D_j -> pi`.

Take any subsequence and normalize by `D_j`. By boundedness, pass to Hausdorff limits
`F_j/D_j -> F` and `K_j/D_j -> K`. The perimeter convergence for convex bodies gives
`per(F)=pi`, while `diam(F),diam(K)<=1` and `F subset K`. The width formula gives

`per(F) = integral_0^pi w_F(theta) dtheta`

where `w_F` is the usual unoriented width. Thus the mean width of `F` is
`per(F)/pi=1`. Every width is at most the diameter, so `w_F(theta)<=1` for all
`theta`. Continuity and mean width one force `w_F(theta)=1` for every theta. Thus
`F` has constant width one.

A constant-width-one convex body is maximal inside a convex body of diameter at most
one. Indeed, if `x in K minus F`, strict separation supplies a unit vector `u` with
`u dot x > h_F(u)`. Choose `y in F` with
`u dot y = -h_F(-u)`. Then

`u dot (x-y) > h_F(u)+h_F(-u) = 1`,

which contradicts `diam(K)<=1`. Therefore `K=F`.

The same argument applies to every convergent subsequence. Consequently
`area(K_j)/D_j^2-area(F_j)/D_j^2 -> 0`; convex-body area is continuous under
Hausdorff convergence. The external-annulus estimate, divided by `D_j^2`, now gives

`|A_j minus F_j|/D_j^2 -> 0`,

because both perimeters are `O(D_j)`. This also proves
`N_{F,j}/D_j^2 -> pi/(2 sqrt(3))`.

Set `a_0=sqrt(3)/2`, as in the rhombic cell estimate. Then

`a_0 N_{F,j}/D_j^2 -> pi/4`.

Divide the transport inequality by `D_j^2`. Since `per(F_j)=O(D_j)` and `E_j>=0`,
it gives `liminf area(F_j)/D_j^2 >= pi/4`. The isodiametric inequality and
`diam(F_j)<=D_j` give the reverse bound `area(F_j)/D_j^2 <= pi/4`. Hence
`area(F_j)/D_j^2 -> pi/4`. Equality in the isodiametric inequality then forces
the limit `F` to be the unit disk. Since every normalized limit of `K_j` equals the
corresponding limit of `F_j`, the same is true for `K_j`.

Finally, the same inequality rearranges to

`0 <= E_j/D_j^2 <= area(F_j)/D_j^2 + o(1) - a_0 N_{F,j}/D_j^2`,

so `E_j/D_j^2 -> 0`. This proves the proposition.

## What this does not prove

The conclusion is only first-order. It gives no `O(D_j)` bound for the external
population or for the area/perimeter defect, and it gives no opposing inequality for
`nu_D=(e_BB+2s_C-3d_H)/D`. The known positive forest surplus floor therefore remains
compatible with this proposition. Also, perimeter saturation gives a constant-width
limit, not a disk; the argument uses the diameter bound and the full-source transport
inequality to force the area limit.

The exact surviving endpoint is the forest branch with `s_Z=0`, `q/D -> pi`,
`min_{e != f} K_{ef}<0`, and possible external population `o(D^2)`. A closure would
need to convert the response obstruction or the `3d_H` charge into a contradiction at
this endpoint. The proposition is not such a conversion.
