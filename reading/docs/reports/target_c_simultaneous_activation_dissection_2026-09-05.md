> Generated reading edition · [exact source](../../../docs/reports/target_c_simultaneous_activation_dissection_2026-09-05.md) · source SHA-256 `2c346e10f3412d2ea8d85d1a6776b0da5fc5b6f5885472c7745269a721a3ed12`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-D94D49357065","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C simultaneous activation dissection

**Date:** 2026-09-05  
**Repository state:** `6e9d4467` (`main`)  
**Run type:** exact proof / C95 correction  
**Target:** Target C activation-boundary route  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

C94 leaves an `Omega(D)`-dimensional exact active-face tangent flat in the low-train pure-rhombic chain branch. C95 proves that every triangle-free first new unit contact lies in an old convex indentation pocket and individually closes a convex subpocket of area at least

`sqrt(3)/2`.

C95 then leaves a stated loophole: simultaneous first-contact subpockets may be nested, so their individual subpocket areas cannot be summed.

That loophole is removable. The individual nested subpockets need not be summed. The noncrossing new unit chords themselves dissect the old convex pocket into disjoint convex cells, and every cell except the unique one adjacent to the old hull chord is an all-unit polygon.

```text
C95 noncrossing outer activations
-> convex chord dissection
-> one all-unit convex cell per new chord
-> triangle-free cell has at least four sides
-> Oler (21.10)
-> additive sqrt(3)/2 shell-area charge per simultaneous new contact
```

## 2. Strongest genuinely new audited theorem

### Theorem — additive simultaneous activation charge

Let `C` be one old convex indentation pocket of a pure-rhombic contact disk. Thus `C` is bounded by an old chain of unit contact edges and one convex-hull chord `e_H`.

Suppose `M>=1` distinct new unit contacts first activate simultaneously inside `C` along a deformation that preserves all old unit contacts, and suppose the resulting source is triangle-free. Then the new unit segments are pairwise noncrossing and dissect `C` into `M+1` convex polygonal cells. Exactly one cell is incident with `e_H`. Every other cell is a convex equilateral polygon whose vertices are source points and has at least four sides.

Consequently the total area of the `M` cells not incident with `e_H` is at least

`M * sqrt(3)/2`.

In particular, if simultaneous first contacts occur across all old indentation pockets and their total number is `M_tot`, then the old shell defect satisfies

`G >= (sqrt(3)/2) M_tot`.

Equivalently,

`M_tot <= 2G/sqrt(3)`.

This charge is independent of nesting depth. The nesting caveat in C95 Section 6 is therefore not a genuine obstruction to summing the area cost of simultaneous activations.

### Scope

The theorem concerns simultaneous first **unit-contact** activations inside the old convex indentation pockets of the C95 pure-rhombic setting. It does not control first activations of new diameter pairs, and it does not by itself prove that C94's tangent-flat dimension forces many unit contacts to activate at one parameter value.

### Proof

C95 proves two facts that we use unchanged:

1. every triangle-free first new unit contact lies in an old convex indentation pocket;
2. distinct simultaneously activated unit segments are pairwise noncrossing, and no such segment passes through a third source vertex.

Fix one old pocket `C` and its `M` new unit chords.

Because `C` is convex, a noncrossing chord between two boundary vertices divides one current convex polygonal cell into two convex polygonal cells. Insert the `M` chords one at a time in any order compatible with the fixed noncrossing family. Inductively every chord lies in one current cell and splits it, so after all insertions there are exactly `M+1` cells, all convex, with pairwise disjoint interiors.

The original boundary of `C` consists of one hull chord `e_H` and old unit edges. Since `e_H` is one boundary segment, exactly one cell of the dissection is incident with the relative interior of `e_H`.

Every edge of every other cell is either

- an old unit contact edge from the pocket chain, or
- one of the newly activated unit chords.

Hence every non-hull cell is an equilateral polygon with side length one. Its vertices are old source vertices, so all mutual vertex distances are at least one.

If such a cell had three sides, all three sides would have length one and its three source vertices would form a unit equilateral triangle, contrary to the triangle-free hypothesis. Therefore every non-hull cell has `m>=4` sides.

Apply the canonical Oler-shell inequality (21.10) to one such cell `F`:

`area(F) >= c_0(m-2)`, `c_0=sqrt(3)/4`.

Since `m>=4`,

`area(F) >= 2c_0 = sqrt(3)/2`.

There are exactly `M` cells not incident with `e_H`, and their interiors are disjoint. All lie inside the old indentation pocket, hence inside the pre-existing shell region `K\R`. Summing gives

`area(union of non-hull cells) >= M sqrt(3)/2`.

Summing again over the old indentation pockets, whose interiors are disjoint, gives

`G >= M_tot sqrt(3)/2`.

This proves the theorem. `square`

### Dependencies

- `docs/reports/target_c_contact_activation_pockets_2026-09-01.md` (C95 localization and noncrossing first-contact chords)
- `docs/theory/03-oler-shell.md`, equation (21.10) (convex equilateral polygon area lower bound)

### Why it is new

C95 explicitly stops because the individually associated subpockets can be nested. The present argument changes the decomposition: instead of summing nested subpockets, it sums the **faces of the chord dissection**. Those faces are disjoint by construction, and all but one per old indentation pocket have only unit boundary edges. This removes nesting completely for simultaneous unit-contact activations.

## 3. Exact target implication

The C95 simultaneous-contact branch is now quantitative without any nonnesting selection:

`M simultaneous harmless new contacts => G >= (sqrt(3)/2) M`.

Therefore any first-event theorem producing `M>=cD` simultaneous new contacts immediately yields the proportional shell loss

`G >= c sqrt(3) D/2`.

The remaining activation-boundary problem is narrower than C95 states. It is no longer an area-disjointness problem. It is a **multiplicity/rank problem**:

> Can the `Omega(D)` exact active-face tangent flat be blocked in all directions while every first event contains only `o(D)` new unit contacts and while new diameter activations remain within the source-wide `|H|<=q` budget?

## 4. Exact remaining lemma

A sufficient next theorem is:

> **First-event multiplicity lemma.** In C94's low-train branch, there exists an exact-active continuation whose first non-old event either creates a unit equilateral triangle, activates `Omega(D)` new unit contacts simultaneously, or activates `Omega(D)` linearly independent new diameter constraints.

The second alternative now pays `Omega(D)` shell area by the theorem above. The third would have to be reconciled with Hopf--Pannwitz `|H|<=q=O(D)` and the C96 near-spanning diameter graph.

A weaker iterative version would also suffice if it guarantees that the disjoint all-unit cells produced over successive contact-activation stages remain chargeable without double counting.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Simultaneous new unit chords are noncrossing | already canonical | C95 |
| `M` noncrossing chords give `M+1` convex cells | proved | standard diagonal dissection of a convex polygon; direct induction |
| Exactly `M` cells avoid the old hull chord | proved | one boundary segment belongs to exactly one dissection cell |
| Every non-hull cell is all-unit | proved | boundary edges are old unit contacts or new unit contacts |
| Every non-hull cell has at least four sides in a triangle-free source | proved | a 3-cell would be a unit equilateral triangle |
| Additive area `>=M sqrt(3)/2` | proved | disjoint cells plus (21.10) |
| C94 forces `Omega(D)` simultaneous contacts | not proved | this is now the remaining rank/multiplicity step |

## 6. Regression tests

### Nested ladder

A long rectangular unit ladder can contain a long nested family of unit chords without triangles. The theorem correctly charges one unit-area quadrilateral cell per rung. Nesting is allowed; it is not free.

### Shared endpoints

Several noncrossing new chords may share an endpoint. The dissection argument still works. A triangular non-hull cell would itself be a forbidden unit equilateral triangle, so in the triangle-free branch every charged cell still has at least four sides.

### One chord

For `M=1`, the theorem reduces exactly to C95's individual charge `sqrt(3)/2`.

## 7. Failed routes and no-go results

No lower bound on the area **difference of two arbitrary nested convex unit-chord subpockets** is needed. Attempting to subtract the two C95 lower bounds is invalid. The correct additive objects are the dissection cells.

The theorem does not justify summing charges from different times after the contact graph has changed. A separate iterative invariant is required for sequential activations.

## 10. Canonical promotion recommendation

**Promote now after independent text audit.** The proof uses only C95 and the already canonical Oler cell inequality, and it directly removes the nesting caveat stated in C95 Section 6.

Suggested canonical edits:

- add a Target C frontier module after C96 or as a C95 refinement;
- update C95's frontier statement so nesting is no longer listed as the area obstruction;
- update the Target C route map/prompt so the remaining activation issue is stated as first-event multiplicity/rank plus new-diameter control.

## 11. Next run

Attack first-event multiplicity on the exact C94 active-equality realization set. The useful finite-dimensional object is the restriction of all currently inactive unit-contact and diameter gap functions to the tangent flat `L`. The goal is to show that a bounded feasible sector in a `d=Omega(D)`-dimensional exact-active stratum needs `Omega(D)` independent boundary functions; then separate those functions into contact and diameter activations and feed the contact side into the additive cell charge above.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
If M new unit contacts activate simultaneously in the old C95 indentation pockets and no unit triangle appears, the noncrossing chords dissect the pockets into exactly M disjoint non-hull convex all-unit cells. Each has at least four sides, so Oler (21.10) gives area >=sqrt(3)/2 per cell. Therefore G>=M sqrt(3)/2. Nesting costs area and is not a loophole.

Exact endpoint now:
C95's area-disjointness problem is closed for simultaneous activations. The remaining problem is to force high first-event multiplicity (or control an iterative sequence) from C94's Omega(D)-dimensional exact active flat while accounting for new diameter events.

Highest-value next lemma:
First-event multiplicity/rank: find a continuation whose first event has Omega(D) contact activations or Omega(D) independent diameter activations, unless a triangle or strict diameter decrease already occurs.

Authoritative inputs:
docs/reports/target_c_contact_activation_pockets_2026-09-01.md
docs/theory/03-oler-shell.md
```
