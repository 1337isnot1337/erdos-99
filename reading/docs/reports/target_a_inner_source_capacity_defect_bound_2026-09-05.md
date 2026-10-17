> Generated reading edition · [exact source](../../../docs/reports/target_a_inner_source_capacity_defect_bound_2026-09-05.md) · source SHA-256 `8b116ad50697bcbdfd7d00ea87f0ede54e0c37366e9782178350c1a29f678e34`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "554a417b60002742988da446404c138ebf4b1f7d", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_inner_source_capacity_defect_bound_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a8d6f544f176fc1ad3c741fe93190296292dc23d4bf5b14ae4ad2ac2426a572d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A inner-source capacity defect is boundary-order

**Date:** 2026-09-05  
**Run type:** exact cross-theorem consequence  
**Target:** zero-slack descent-or-gates branch, Section 168.3  
**Depends on:** Theorem 168.3; exterior source-gate boundary budget  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

In the zero-slack branch let

`A^0 subset H`

be the triangle-free fixed-hull capacity source from Section 168, and let

`X^* subset K^*`

be the plateau-terminalized response optimum with

`m^*=|X^*|`, `d=diam(K^*)`.

Section 168.3 defines

`k=|A^0 cap K^*|`,

`r=m^*-k`.

The same section proves that **every** matching saturating `X^*` into `A^0` has at least `r` matched source endpoints outside `K^*`.

The exterior source-gate boundary theorem proves, independently, that for every such zero-slack saturating matching,

`#{x in X^*: matched source label a_x notin K^*} <= 12d+9`.

## 2. Exact consequence

Combine the lower and upper counts for one arbitrary saturating matching.

### Theorem — inner-source capacity defect bound

`r <= 12d+9`.

Equivalently,

`|A^0 cap K^*| >= m^*-(12d+9)`.

Thus the genuine triangle-free fixed-hull capacity source already places all but boundary-order many of the full `m^*` response-hull capacity slots inside `K^*`.

### Proof

Theorem 168.3 gives at least `r` exterior source labels in every saturating matching. The exterior-gate boundary theorem gives at most `12d+9` exterior labels in the same matching. Hence `r<=12d+9`. Since `r=m^*-|A^0 cap K^*|`, the equivalent form follows. `square`

## 3. Relation to the descent branch

If `r=0`, Section 168.3 already gives a strict plateau descent: `A^0 cap K^*` is a triangle-free `m^*`-point global optimum of diameter `d`.

The theorem here shows that failure of exact descent is confined to a boundary-order defect:

`1 <= r <= 12d+9`.

This is stronger than merely knowing that transverse source gates exist. It says there are never more than boundary-order missing genuine-source points from the smaller optimum hull.

## 4. What is still missing

Section 168.3 explicitly warns that `r` is not yet the Schur demand

`s=Delta_Lambda-d_int`.

This theorem does not reverse that warning. No inequality `r>=s` or `r<=s` follows formally from the definitions now in hand.

The useful new target is therefore sharper:

> Either relate the Schur demand `s` to the boundary-order inner-source defect `r`, or use the `m^*-O(d)` genuine source points already inside `K^*` to prove the three-sector population inequality of Section 174 directly.

A successful inequality `s<=r` would close the zero-slack branch immediately after combining with a sector/gate nullity bound; it is not claimed here.

## 5. Handoff

```text
LEVEL I STATUS: STILL OPEN.

Section 168.3:
  every X*->A0 saturating matching has >=r exterior labels,
  r=m*-|A0 cap K*|.

Exterior-gate theorem:
  every such matching has <=12d+9 exterior labels.

Therefore exactly:
  r<=12d+9,
  |A0 cap K*|>=m*-(12d+9).

So the smaller response hull is already filled by the genuine triangle-free source up to boundary order. The remaining bridge is r versus the Schur demand s, or a direct sector-population use of this near-full inner source.
```
