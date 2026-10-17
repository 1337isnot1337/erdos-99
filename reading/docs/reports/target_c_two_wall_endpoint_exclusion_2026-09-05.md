> Generated reading edition · [exact source](../../../docs/reports/target_c_two_wall_endpoint_exclusion_2026-09-05.md) · source SHA-256 `981379b8726036a70ceb4518febbf8f069f19826ab0c369cc5c7b80859e5058b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-30D7390AF6DA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — regression: attempted two-wall endpoint exclusion

**Date:** 2026-09-05  
**Branch:** `research/target-c-c97-caterpillar-fan-capacity-2026-09-04`  
**Run type:** regression / theorem retraction  
**Target:** exact envelope endpoint from the audited C80–C96 chain-face branch  
**Status:** RETRACTED; LEVEL I STILL OPEN

## 1. Retracted claim

An earlier revision of this report claimed that the exact scalar endpoint

`T/D -> 2.932935111451...`

is impossible.  That claim is **not proved** and must not be used.

The valid exact scalar result from
`target_c_exact_two_side_capacity_envelope_2026-09-05.md` remains:

`T/D >= 2.932935111451...`

for every fixed subsequential low-train limit.  The older fully certified strict bound

`liminf T/D > 2.9328`

also remains valid.

This regression concerns only the attempted strict exclusion of the optimized endpoint.

## 2. What in the attempted proof was valid

Suppose a survivor sequence approaches the exact scalar endpoint.  Equality in the
TS4 envelope does force, at leading atomic order,

`q=o(1)`,

`lambda=mu=r_*/2+o(1)`.

Saturation of one side wall also forces a strong interior-prefix normal form.  For any
fixed `0<p<r_*/2`, after discarding `o(D)` exceptional short rows, the first `pD`
nested rows have a common exact-chain interval of length

`(sqrt(1-3p^2/4)-o(1))D`.

Furthermore, the longitudinal part of the one-side parallelogram inequality forces
the two chain-adjacent residual phase populations to balance inside every such
macroscopic prefix:

`b_p-c_p=o(1)`.

These equality consequences are still useful and may be re-proved/promoted separately
if needed.

## 3. The invalid step

The failed argument selected only a proper subgrid:

- a common central subfamily `A'` of exact chain trains;
- selected residual phase rows `B'` and `C'` from fixed interior prefixes.

It then invoked the trimmed-grid phase-star theorem as if every train outside
`A' union B' union C'` contributed only `o(D)` to an opposite-corner displacement.
That is false.

Theorem TG1 in
`target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md` controls trains outside the
**full complete grid families** `A union B` only when their crossings with that full
star are `o(D^2)` after fixed trimming.  In the attempted application there remain
linear populations of unselected trains in the **same three coherent phases**:

- exact chain tracks in `P\A'`;
- residual `B`-phase rows outside `B'`;
- residual `C`-phase rows outside `C'`.

Those trains can have `Theta(D^2)` crossings with the selected subgrid.  TG1 therefore
does not make their displacement contribution `o(D)`.  They may shift the selected
corner difference by `Theta(D)` and can erase the numerical margin.

The previous sentence claiming that `q=o(1)` made all such external effects negligible
confused *atomic complement mass outside the chain three-phase orbit* with
*unselected trains inside the same coherent phase classes*.  They are different.

## 4. Explicit sanity check

At the scalar endpoint put

`a=r_*/2=0.4664675557...`.

For a small selected prefix `p=1/5`, the two wall intervals do share a chain block of
normalized length

`M=2sqrt(1-3p^2/4)-1=2sqrt(0.97)-1`.

If one ignored all unselected same-phase trains, the selected three-phase diagonal
coefficient would indeed be

`M^2+3p^2=5-4sqrt(0.97)>1`.

But the omitted center-phase population alone has size `1-M`, and the omitted leaf
phase populations have linear size `a-p`.  They are not controlled by an `o(D^2)`
external-crossing budget.  Allowing these coherent populations to enter the same train
coordinate difference destroys the claimed direct contradiction.

Thus the positive coefficient above is not a valid lower bound for an actual source
distance.

## 5. Correct frontier

The correct promotion problem is stronger than merely finding a positive-density
complete subgrid.  One needs one of the following:

1. a **phase-complete trimming theorem** that absorbs all same-phase trains outside the
   selected grid and still gives a diameter lower bound; or
2. an exact train-coordinate cut whose opposite corners are separated by no omitted
   same-phase tracks; or
3. a quantitative inequality charging the omitted same-phase displacement against the
   crossings it must spend through the saturated walls.

Until such a theorem is proved, the exact optimized scalar endpoint remains admissible
by the current audited record.

## 6. Surviving theorem stack

This regression does not affect:

- the exact TS4 envelope and root `r_*=0.932935111451...`;
- the strict audited polynomial certificate `liminf T/D>2.9328`;
- the C87 staircase tree and exact length spectrum `{1,...,D}`;
- the C93 secondary-separator incidence budget;
- the C96 common-cut caterpillar theorem;
- the Target B trimmed-grid theorem for a **full** complete coherent phase star.

No endpoint exclusion should be cited from this file.
