> Generated reading edition · [exact source](../../../docs/reports/target_c_cellwise_oler_capacity_2026-08-31.md) · source SHA-256 `7db0bfbb8696846bbb6d56dcb5bfeca196b07fdb2e84357a30d6ebee117d98b0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-728525D59FE9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C45: cellwise Oler capacity for the harmonic response decomposition

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C36-C43 and canonical Oler finite-packing inequality  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `I_r` be the unpinned harmonic components, `A_r` their distinct loaded attachment sets, and

`P_r=conv(A_r)`.

C43 proves the cell interiors are pairwise disjoint. Apply Oler separately to the unit-separated set `I_r union A_r` inside `P_r`.

Let

- `n_I=sum_r |I_r|`;
- `a=sum_r |A_r|`;
- `c=c_I`;
- `G=area(F)-sum_r area(P_r)>=0`.

Then

`(sqrt3/2)(n_I+a-c) <= area(F)-G + (sqrt3/4) sum_r per(P_r)`.

Since every cell has diameter at most `D`, `per(P_r)<=pi D`, so

`(sqrt3/2)(n_I+a-c) <= area(F)-G + (sqrt3 pi/4) D c`.

If `c>0`, C38 gives `q-q_used<=e_BB`, while `a>=q_used`. For the force-visible contact-core population `m=n_I+q`, this yields

`m <= (2/sqrt3)(area(F)-G) + (pi/2)D c + c + e_BB`.

Using `area(F)<=pi D^2/4`,

`m <= Delta_2 D^2 -(2/sqrt3)G +(pi/2)D c + c + e_BB`,

where `Delta_2=pi/(2sqrt3)`.

This isolates an exact attachment-cell area deficit. It is not yet a Level I contradiction because the perimeter correction can be `o(D^2)` rather than `O(D)`, and contact-isolated source points lie outside `m`.

## 1. Oler on one cell

For any unit-separated finite set `S` in a convex body `K`, canonical Oler gives

`(sqrt3/2)(|S|-1) <= area(K)+(sqrt3/4)per(K)`.

Apply this to `S_r=I_r union A_r` in `P_r`:

`(sqrt3/2)(|I_r|+|A_r|-1) <= area(P_r)+(sqrt3/4)per(P_r)`.

Summing and using C43 gives

`(sqrt3/2)(n_I+a-c) <= area(F)-G +(sqrt3/4)sum_r per(P_r)`.

## 2. Diameter-perimeter simplification

Every planar convex cell `P_r` has diameter at most `D`, so the convex perimeter-diameter inequality gives `per(P_r)<=pi D`. Hence

`(sqrt3/2)(n_I+a-c) <= area(F)-G +(sqrt3 pi/4)Dc`.

## 3. Full core population

Let `q=|B_+|` and `q_used=|union_r A_r|`. Since `a>=q_used` and C38 gives `q-q_used<=e_BB` when `c>0`,

`n_I+a-c >= m-e_BB-c`.

Therefore

`m <= (2/sqrt3)(area(F)-G)+(pi/2)Dc+c+e_BB`.

The isodiametric area bound `area(F)<=pi D^2/4` gives the displayed `Delta_2 D^2` form.

## 4. Phase interpretation

If `c=O(1)`, the perimeter correction is only `O(D)`. Then a cell-area gap `G` exceeding the finite boundary correction, together with control of source points outside the force-visible core, would produce a genuine global capacity contradiction.

In the general near-minimal phase C33 gives `c+e_BB=o(D)`, so C45 yields only

`m <= Delta_2 D^2 -(2/sqrt3)G + o(D^2)`.

This is a real finite-packing reduction but not enough by itself because triangle-free configurations can approach optimal density and because `m` need not equal the source cardinality.

## 5. Exact one-component endpoint

C44 shows the zero-defect exact partition has one component with `A_1=B_+`. Then `P_1=F` and `G=0`, so C45 reduces exactly to ordinary Oler on the whole force-visible core. No artificial gain is claimed in the hardest endpoint.

## Regression audit

- One component attached to all `B_+`: `G=0`, ordinary Oler is recovered.
- Multiple disjoint cells: unused force-hull area enters with the favorable exact term `-(2/sqrt3)G`.
- Many cells: the `Dc` perimeter term is the explicit obstruction.
- Contact-isolated source points are not counted by `m`.
