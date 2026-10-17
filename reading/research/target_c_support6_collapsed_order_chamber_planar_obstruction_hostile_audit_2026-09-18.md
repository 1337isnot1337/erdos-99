> Generated reading edition · [exact source](../../research/target_c_support6_collapsed_order_chamber_planar_obstruction_hostile_audit_2026-09-18.md) · source SHA-256 `10831b0469bb3ed7f9bce01f52057e541b6c6ce5668f2f14c75a4f30058d16b0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bd8b961e380b635dea74c8fa9c8a6173b32543bb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support6_collapsed_order_chamber_planar_obstruction_hostile_audit_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "b391eb88ebe57678dcd3c6a890fc1bd535c7c3e9deeb13da43b0036b5c291930"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — collapsed order-chamber planar obstruction

**Date:** 2026-09-18  
**Audited source:** `target_c_support6_collapsed_order_chamber_planar_obstruction_2026-09-18.md`  
**Certificate:** `verify_target_c_support6_collapsed_order_chamber_planar_obstruction_2026_09_18.py`  
**Disposition:** PASS for the stated local-order-chamber scope; no theorem-state change

## 1. What is actually fixed

The local contraction certificate proves a root in a small box and proves that every
root in that box has the recorded five-side cyclic order at each of the six bounded
faces. The audit therefore accepts those six rotations only for this chamber. It does
not infer that every collapsed solution has the same rotations.

## 2. Crossing restrictions

The projective-angle interval test is conservative: a pair is admitted only when the
whole certified angle interval is strictly above `pi/3`. Pairs sharing a bounded
stopping face are removed by the independently hostile-audited endpoint-fan theorem.
The train crossing graph is additionally filtered for triangles, and no assumption is
made that a train can cross at most one other train. Repeated crossings of one train
with different trains are allowed.

## 3. Rotation-system enumeration

For every retained crossing subset, the verifier enumerates every order of multiple
crossing points along each train. At each crossing it uses both alternating cyclic
rotations. The six terminal rotations are held fixed. The face permutation is computed
from the resulting integer dart successor map. A planarization has Euler
characteristic two, equivalently `F=E-V+2`; every tested system fails this equality.

The exact counts are seven angle-eligible endpoint-disjoint crossing pairs, 128 legal
subsets, and 9,971 rotation systems. No floating-point decision enters the enumeration.

## 4. Scope limitation

This is not a universal collapsed-branch theorem. It excludes one certified local
cyclic-order chamber. Other collapsed closure components, other cyclic orders, or a
global configuration whose support-six block is not represented by this chamber are not
covered. The result also does not assert that a topological routing would satisfy all
metric source inequalities; it proves the stronger absence of such a routing for this
chamber under the necessary train constraints.

**Audit disposition:** pass at conditional scope.
