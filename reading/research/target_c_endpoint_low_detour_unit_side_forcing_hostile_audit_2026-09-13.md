> Generated reading edition · [exact source](../../research/target_c_endpoint_low_detour_unit_side_forcing_hostile_audit_2026-09-13.md) · source SHA-256 `ece68aef093269afb2c9945ae540bc7f975f7f5b8c0707a16d57abb47969b376`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9b4ba9575532a543edc9285479a7567205b9ae88", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_endpoint_low_detour_unit_side_forcing_hostile_audit_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "346567f9ba025a22cef5f2c97241d6c7fa1f4b3b197b4204e508a3391034e590"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — low-detour endpoint unit-side forcing

**Date:** 2026-09-13  
**Reviewed:** `target_c_endpoint_low_detour_unit_side_forcing_2026-09-13.md`  
**Disposition:** PASS at proof-only Section-118 endpoint scope.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Endpoint floor and detour threshold

The strict aggregate gap supplies `alpha=pi(2-sqrt(3))/20`, while the audited
Section-118 moment profile supplies `S118`. Thus `q-k >= (S118+alpha)D-o(D)`.
Section 172 supplies

```math
\liminf(b-\operatorname{per}(F))/D
\ge(m/D+k/D-(\pi-S118-\alpha))_+-o(1).
```

The threshold `K0=pi-T0` is therefore used with the correct sign.

## 2. Low-branch inequality

Under `m+k<K0D-o(D)`, one has `m<K0D-k+o(D)`. Since `q=(q-k)+k`,

```math
q-m\ge T0D+k-(K0D-k)-o(D)
 =(2T0-pi)D+2k-o(D).
```

This proves `e_BB/D >= 2T0-pi-o(1)`. It does not require a lower bound on `m`, and
it does not reverse a liminf inequality.

## 3. Exact ledger transfer

The Type-II identity `e_BB=Q+2k+u_B` is audited independently. Subtracting `2k`
from the low-branch bound gives `Q+u_B>=E0D-o(D)`; no claim that either summand
alone is large is made.

The bound `k<K0D+o(D)` follows from `m>=0` and the low-branch assumption. Since
`d_H,s_Z>=0` and `k=d_H+s_Z`, each is at most this bound.

## 4. Scope check

The same-carrier Section-118 assumption is used only for the floor `T0`. The result
does not touch Type I, contact-isolated points, or theorem-state authority.

**Audit verdict:** PASS. This is a valid endpoint narrowing, not a C-II closure.
