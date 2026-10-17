> Generated reading edition · [exact source](../../../docs/reports/target_c_activation_rank_sequential_audit_2026-09-05.md) · source SHA-256 `3d7a310bb0150027c3d20ace17e0bae21ac680880e038fa393abb4cc2b22ec3c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-38CA77E00F73","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C activation-rank / sequential-contact audit

**Date:** 2026-09-05  
**Repository state:** `da39c212` (`main`)  
**Run type:** hostile proof audit / rejected closing routes  
**Target:** Target C exact-active continuation after C94-C95  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Purpose

Two unmerged C97-era notes propose to close the large exact-active-flat branch by combining activation rank with contact-pocket area:

- `target_c_mixed_activation_capacity_2026-09-05.md` on `research/target-c-c97-common-cut-metric-2026-09-05`;
- `target_c_shell_contact_capacity_2026-09-05.md` on the same branch.

The first tries to force one first boundary event to have rank comparable with the dimension of the current exact-active flat. The second tries to sum noncrossing contact chords over an entire sequential continuation.

Neither inference is justified. This report isolates the exact failures and records the strongest valid replacement statement.

## 2. Failure of the one-event rank argument

Let `L` be a `k`-dimensional feasible tangent/continuation space inside the current exact-active realization stratum. A boundary event at a point of a path in `L` may introduce one new independent active constraint. There is no general reason that the constraints active at that **single first boundary point** must have rank `k` on `L`.

The elementary model is the cube

`[-1,1]^k`.

It is a bounded `k`-dimensional feasible region, but a generic ray from the origin reaches the relative interior of one facet. The first boundary event has rank one, not rank `k`.

Therefore the implication

`dim L = k  =>  some first boundary event has activation rank >= k`

is false without an additional theorem specific to the Erdős #99 realization set.

C_ACT does not supply that theorem. C_ACT says that newly active constraints at a first admissible event have zero multiplier for the transported original KKT stress and hence do not shrink the original stress face merely by activation. It does not force simultaneous activation of enough independent constraints to span the old tangent flat.

### Audit result

Any proof step in C102 that requires one first boundary point to block all `k` directions of the C94 flat is rejected.

## 3. Failure of the sequential noncrossing argument

At one fixed source configuration, two distinct unit segments between source vertices cannot cross transversely: if they did, one of the four endpoint distances would be less than one. This is the valid geometric fact used by C95 and by the simultaneous dissection theorem on `main`.

It does **not** follow that unit contacts activated at different times along a deformation form one globally noncrossing chord family on the vertex labels.

A contact `ab` may become active at one parameter value and later become inactive. A different contact `cd` may become active at another parameter value. The two labelled chords `ab` and `cd` need never coexist as unit segments in one source. Consequently the fixed-configuration crossing prohibition gives no relation between them.

Thus one cannot place all contacts ever activated along a continuation into one chord dissection of the original indentation pockets unless an additional persistence or monotonicity theorem is proved.

The same issue affects the shell bookkeeping. After an activation and subsequent motion,

- the old hull chord may move;
- the pocket geometry may change;
- a previously active contact may open;
- a later charged cell may overlap in the plane with an earlier charged cell.

Hence the fixed-source disjointness argument cannot simply be iterated through time.

### Audit result

Any C103 claim that the **entire sequential set** of activated contacts is one noncrossing family, or that all of their C95 pocket charges can be summed without a persistence invariant, is rejected.

## 4. Strongest valid statement retained

The valid theorem is the simultaneous one already committed on `main`:

> At one fixed first-contact event in the old C95 convex indentation pockets, if `M` new unit contacts activate simultaneously and no unit equilateral triangle appears, the noncrossing new chords dissect the old pockets into exactly `M` disjoint non-hull all-unit convex cells. Each cell has at least four sides, so Oler gives area at least `sqrt(3)/2` per cell. Therefore
>
> `G >= M sqrt(3)/2`.

This theorem removes C95's nesting loophole **within one simultaneous event**. It does not imply a bound on the total number of contacts activated at different events.

## 5. What would repair the sequential route

Any one of the following would be sufficient to make a sequential charge legitimate:

1. **Persistence theorem.** Along a chosen continuation, every newly activated unit contact remains active thereafter. Then all activated contacts coexist at the endpoint and are pairwise noncrossing there.
2. **Nested-region invariant.** Associate to every activation a region of the original shell that is provably disjoint from all regions charged at earlier events, even if contacts later open.
3. **Monotone potential.** Construct a scalar shell/contact potential that decreases by a fixed amount per independent activation and cannot increase under admissible continuation.
4. **One-event multiplicity theorem.** Prove directly that some single event has `Omega(D)` simultaneous contacts; then the existing simultaneous theorem already gives `Omega(D)` shell loss.

No such statement is presently canonical.

## 6. Exact consequence for the active research program

The activation route remains open at the following point:

```text
C94: dim exact-active flat = Omega(D)
  + C_ACT: future activations carry zero old-stress multiplier
  + simultaneous pocket theorem: M simultaneous contacts cost M sqrt(3)/2 shell area
  ?
Need persistence, a monotone charge, or a genuine high-multiplicity theorem.
```

Pure dimension counting cannot fill the question mark. A high-dimensional feasible set may encounter only low-rank facets one at a time.

## 7. Audit classifications

| Statement | Classification | Reason |
| --- | --- | --- |
| Simultaneous first-contact chords at one source are noncrossing | valid | fixed-configuration unit-separation geometry |
| `M` simultaneous harmless contacts cost `M sqrt(3)/2` shell area | valid | disjoint all-unit chord-dissection cells |
| A `k`-flat forces one first event of rank at least `k` | false in general | cube/facet countermodel |
| Contacts activated at distinct times form one noncrossing labelled family | unjustified / false as an inference | contacts need not coexist |
| Sequential C95 charges are automatically disjoint | unjustified | pocket geometry and active set can change |
| C102/C103 as currently written close the C94 branch | rejected | both rely on the preceding invalid implications |

## 8. Handoff

```text
LEVEL I STATUS: STILL OPEN.

Do not use C102's one-event-rank inference.
Do not use C103's across-time noncrossing inference.

Safe activation result:
At a single simultaneous event, M harmless new unit contacts force G >= M sqrt(3)/2.

Live missing theorem:
Persistence / monotone sequential charge / genuine Omega(D) simultaneous multiplicity.
```
