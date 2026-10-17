> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_global_train_obstruction_hostile_audit_2026-09-19.md) · source SHA-256 `14b2737ed882639deafa2d2b252236d73457d089d8020a0dcbfbb8208cf95797`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "28e63969bebe37022155ec47b2325db843f22be4", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_global_train_obstruction_hostile_audit_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6b5adac9ecb42e3d4b577b84e809732489d74e202e9f655657e8183142b24f01"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — collapsed support-six Jordan train-cycle obstruction

**Date:** 2026-09-19  
**Audited note:** `research/target_c_support6_collapsed_global_train_obstruction_2026-09-19.md`  
**Certificate:** `research/verify_target_c_support6_collapsed_global_train_obstruction_2026_09_19.py`  
**Disposition:** PASS at the stated certified-root-box scope; C-II remains open.

## 1. Scope check

The theorem excludes the full rigorous radius-`10^-10` solution box around the already certified collapsed local root. It does not claim to exclude every collapsed support-six solution. This distinction is load-bearing because the local closure system has a two-dimensional regular family near the witness and may have other order/angle cells elsewhere.

The note correctly changes the status of the existing witness from “locally feasible, global status unknown” to “locally feasible but globally impossible as a stopped-train/rhombus source.”

## 2. The train arcs used in the Jordan curve are legitimate

The audited train primitive gives each nonsingleton complete train a simple midpoint path through its rhombi. Distinct train paths can meet only by sharing a rhombus, where they cross. A singleton train shared by two exceptional faces can be represented by an arbitrarily short transverse connector through the common edge midpoint; this changes no crossing relation and gives the same topological incidence.

The three cycle trains are `01,12,02`. The exact interval certificate proves

```math
|u_{01}\cdot u_{12}|,
|u_{12}\cdot u_{02}|,
|u_{02}\cdot u_{01}|>{11\over20}>{1\over2}.
```

A strict unit rhombus crossing would require absolute dot product `<1/2`. Hence the three train arcs are pairwise disjoint away from their prescribed terminal faces.

Inside each strict convex exceptional face, the chord between the two selected side midpoints lies in the face interior. Train midpoint paths do not enter an exceptional-face interior except at their terminal side midpoint. Therefore the three train arcs plus the three face chords form a simple closed curve. There is no omitted graph-edge crossing inside a face.

## 3. The side assignment from the rotation system is consistent

The certificate rechecks throughout the entire root box the counterclockwise orders

```math
F_0:(a,02,04,05,01),
\quad
F_1:(a,15,01,13,12),
\quad
F_2:(a,23,12,24,02).
```

Orient the Jordan cycle `0->1->2->0`. In an oriented ribbon neighborhood of a simple cycle, the counterclockwise sector from the incoming half-edge to the outgoing half-edge is the same chosen side of the curve at every vertex disk; depending on the global orientation it is either the bounded or unbounded side, which is irrelevant.

At `F_0`, incoming `02` to outgoing `01` contains `04,05`. At `F_2`, incoming `12` to outgoing `02` contains `24`, while `23` lies in the complementary sector. Therefore `04` and `23` leave the Jordan cycle on opposite sides. This is a purely combinatorial consequence of the certified rotation orders; no metric interpolation is used.

## 4. The spoke trains really transport the side labels

The certificate proves `|u.v|>11/20` for every pair of `04` with a cycle train and every pair of `23` with a cycle train. Thus neither complete train can cross the Jordan curve through a rhombus.

They also cannot meet one of the three internal face chords: `04` and `23` terminate at the indicated cycle face and their other terminal face, and between terminal exceptional faces a train path lies in rhombi. It cannot pass through the interior of a third exceptional face.

Hence the entire `04` connection remains on the side on which it leaves `F_0`, placing `F_4` there, while the entire `23` connection remains on the opposite side, placing `F_3` there. The fact that an exceptional face is a disk and is disjoint from the Jordan curve means all of its other train attachments inherit that same side label.

## 5. `34` is a mandatory relation train and cannot cross the separator

For matching `M={03,14,25}`, the degree-pure support-six relation graph is `K_6\setminus M`; in particular `34` is an internal relation train.

Since `F_3` and `F_4` lie in opposite components of the complement of the Jordan curve, any arc joining them must meet the curve. The `34` train cannot meet a face chord for the same terminal-face reason as above. Therefore it would have to cross at least one of `01,12,02` in a rhombus.

The certificate proves

```math
|u_{34}\cdot u_{01}|,
|u_{34}\cdot u_{12}|,
|u_{34}\cdot u_{02}|>{11\over20},
```

so all three possible rhombus crossings are forbidden. This is a direct Jordan contradiction. It does not depend on how many other trains exist outside the six-face gadget; external trains cannot repair a continuous `F_3`--`F_4` arc that itself is unable to cross the separator.

This last point is important. An earlier exploratory holonomy approach tried to enumerate only crossings with the eighteen gadget trains; that would have been invalid because global relation trains may cross arbitrary outside trains. The committed Jordan proof does **not** make that restriction and is immune to that failure mode.

## 6. Interval certification is sufficiently strong

The verifier copies the rational centers and radius from the exact local-root certificate, uses a rational Machin enclosure for `pi`, and uses rational Taylor/Lagrange enclosures for sine and cosine. It independently rechecks the three face orders and all fifteen no-crossing pairs.

The weakest required dot-product margin at the recorded center is the `04`--`02` pair, about `0.55647`; the certified target is only `11/20=0.55`, while the root radius is `10^-10`. The interval proof therefore has substantial slack. No decimal angle comparison or numerical optimizer enters the logical test.

The locally reproduced certificate output is:

```text
PASS: certified side orders at F0,F1,F2 are unchanged throughout the root box
PASS: all 15 required train pairs satisfy |u.v| > 11/20 > 1/2
PASS: the full certified collapsed root box is excluded by the Jordan train-cycle obstruction
```

## 7. Non-implications

This theorem does not prove that the collapsed branch is empty. A different solution of the six-face closure equations could change the cyclic rotation cell, make one of the three cycle trains cross-compatible with another, make one of the side-transport spokes cross the separator, or make the forced opposite-side connector cross-compatible with the cycle.

It also does not alter the support-seven coefficient globally. The tangent-payment theorem remains the unconditional statement for arbitrary collapsed blocks.

What is new is a validated global obstruction schema: a relation triangle that is itself noncrossing, together with two noncrossing side-transport spokes and an opposite-side relation edge that is also noncrossing, is impossible. The certified local witness lies strictly inside such a forbidden cell.

**Audit disposition:** PASS. The known collapsed local root is not a globally realizable train gadget. The next route toward full support-six exclusion is to classify all collapsed closure solutions by rotation/crossing cell and apply the same Jordan separator test cell-by-cell, or prove that every admissible cell contains such a forbidden relation triangle.
