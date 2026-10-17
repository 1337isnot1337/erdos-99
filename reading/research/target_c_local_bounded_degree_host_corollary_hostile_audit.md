> Generated reading edition · [exact source](../../research/target_c_local_bounded_degree_host_corollary_hostile_audit.md) · source SHA-256 `c2fe22376f28f3668112828ff91ba8e00dcb1bccf32cebaf59be5fdeaad62289`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "487fef539ceff78ea01dffcbd4a29ac42c68ab26", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_local_bounded_degree_host_corollary_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "90668b51c68382da0dd0cf96875470812e5e595b00f8d2265e776bac9dc863a2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — bounded-degree local defect-host corollary

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_local_bounded_degree_host_corollary.md`  
**Disposition:** PASS at proof-only Type-II frontier scope.  
**Theorem authority:** unchanged; C-II remains open.

## 1. Defect-degree conversion

The parent detour/face theorem supplies

$$
F_{loc}/D\ge
\left[(A_{DF}-6t_D-2\kappa_D)/4-o(1)\right]_+.
$$

The loaded-hull identity `q-x_B=Q+2k`, with `x_B\ge0`, gives

$$
Q/D\le(q-k)/D-k/D=t_D-\kappa_D.
$$

Every local face of degree greater than `K` contributes at least `K-3` to the same
global degree excess `Q`.  Under the recorded local-face fidelity, these charges are
injective, so

$$
F_{loc,>K}/D\le(t_D-\kappa_D)/(K-3).
$$

Subtracting yields exactly (BD.2).  No sign is reversed and no local face is counted
twice.

## 2. Degree-22 specialization

For `K=22`, subtracting `Q/19` changes the coefficients to

$$
\frac{A_{DF}}4-
\left(\frac32+\frac1{19}\right)t_D-
\left(\frac12-\frac1{19}\right)\kappa_D.
$$

At `t_D\le1.90` and `\kappa_D\le0.05`, with
`A_{DF}=12.19736577709914...`, the lower coefficient is

$$
3.049341444274785-2.950000000000000-0.022368421052632
=0.076973023222153...,
$$

which is strictly above the displayed `0.0769730` marker.  The arithmetic is safe
under the stated `o(1)` convention.

## 3. Scope

This corollary is conditional on the parent Section-118 frontier/common-cap profile,
the aggregate detour identity, and local-face fidelity.  It does not turn a linear
face or train-host population into a contradiction, does not use the rejected
five-host inference, and does not remove contact-isolated points.

**Final classification:** audited-working proof-only corollary; C-II and Level I remain
open.
